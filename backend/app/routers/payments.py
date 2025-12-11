import uuid
import json
from fastapi import APIRouter, Depends, HTTPException, status, Request, Header
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.auth import get_current_user
from app.models.user import User
from app.models.loan import Loan
from app.models.transaction import Transaction
from app.schemas.payment import (
    PaymentInitRequest, PaymentInitResponse, PaymentVerifyResponse,
    WebhookPayload, TransactionResponse
)
from app.services.paystack_service import paystack_service

router = APIRouter(prefix="/api/payments", tags=["Payments"])

@router.post("/initialize", response_model=PaymentInitResponse)
async def initialize_payment(
    request: PaymentInitRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    loan = db.query(Loan).filter(
        Loan.id == request.loan_id,
        Loan.user_id == current_user.id
    ).first()
    
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found"
        )
    
    if loan.status == "repaid":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Loan already repaid"
        )
    
    reference = f"LOAN_{loan.id}_{uuid.uuid4().hex[:8].upper()}"
    email = f"{current_user.phone}@microloan.app"
    
    # Initialize payment with M-Pesa support
    result = await paystack_service.initialize_transaction(
        email=email,
        amount=loan.total,
        reference=reference,
        callback_url=request.callback_url,
        phone=current_user.phone
    )
    
    if not result.get("success"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result.get("message", "Payment initialization failed")
        )
    
    new_transaction = Transaction(
        loan_id=loan.id,
        reference=reference,
        amount=loan.total,
        status="pending",
        transaction_metadata=json.dumps({
            "loan_id": loan.id,
            "user_phone": current_user.phone,
            "payment_method": "mpesa"
        })
    )
    db.add(new_transaction)
    db.commit()
    
    return PaymentInitResponse(
        authorization_url=result["authorization_url"],
        access_code=result["access_code"],
        reference=reference
    )

@router.get("/verify/{reference}", response_model=PaymentVerifyResponse)
async def verify_payment(
    reference: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.reference == reference).first()
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )
    
    loan = db.query(Loan).filter(Loan.id == transaction.loan_id).first()
    if not loan or loan.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to verify this transaction"
        )
    
    result = await paystack_service.verify_transaction(reference)
    
    if result.get("success"):
        transaction.status = "success"
        loan.status = "repaid"
        
        user = db.query(User).filter(User.id == current_user.id).first()
        if user.loan_limit < 60000:
            user.loan_limit = min(user.loan_limit + 2000, 60000)
        
        db.commit()
        
        return PaymentVerifyResponse(
            status="success",
            reference=reference,
            amount=result["amount"],
            message="Payment successful. Loan marked as repaid."
        )
    else:
        transaction.status = "failed"
        db.commit()
        
        return PaymentVerifyResponse(
            status="failed",
            reference=reference,
            amount=0,
            message=result.get("message", "Payment verification failed")
        )

@router.post("/webhook")
async def paystack_webhook(
    request: Request,
    x_paystack_signature: str = Header(None),
    db: Session = Depends(get_db)
):
    payload = await request.body()
    
    if x_paystack_signature:
        if not paystack_service.verify_webhook_signature(payload, x_paystack_signature):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid webhook signature"
            )
    
    data = await request.json()
    event = data.get("event")
    event_data = data.get("data", {})
    
    if event == "charge.success":
        reference = event_data.get("reference")
        if reference:
            transaction = db.query(Transaction).filter(Transaction.reference == reference).first()
            if transaction:
                transaction.status = "success"
                loan = db.query(Loan).filter(Loan.id == transaction.loan_id).first()
                if loan:
                    loan.status = "repaid"
                    user = db.query(User).filter(User.id == loan.user_id).first()
                    if user and user.loan_limit < 60000:
                        user.loan_limit = min(user.loan_limit + 2000, 60000)
                db.commit()
    
    return {"status": "success"}

@router.get("/transactions", response_model=list[TransactionResponse])
async def get_transactions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    loans = db.query(Loan).filter(Loan.user_id == current_user.id).all()
    loan_ids = [loan.id for loan in loans]
    transactions = db.query(Transaction).filter(Transaction.loan_id.in_(loan_ids)).order_by(Transaction.created_at.desc()).all()
    return transactions
