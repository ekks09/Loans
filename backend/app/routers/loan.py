from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.utils.auth import get_current_user
from app.models.user import User
from app.models.loan import Loan
from app.schemas.loan import (
    LoanPreviewRequest, LoanPreviewResponse, LoanApplyRequest,
    LoanResponse, LoanListResponse
)

router = APIRouter(prefix="/api/loans", tags=["Loans"])

FEE_STRUCTURE = {
    3000: 200,
    5000: 350,
    6000: 460,
    7000: 460,
    8000: 460,
    10000: 1000,
    20000: 2000,
    30000: 3000,
    40000: 4000,
    50000: 5000,
    60000: 6000
}

def calculate_fee(principal: int) -> int:
    if principal < 3000 or principal > 60000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Loan amount must be between 3,000 and 60,000"
        )
    
    if principal in FEE_STRUCTURE:
        return FEE_STRUCTURE[principal]
    
    if 6000 <= principal <= 8000:
        return 460
    
    sorted_amounts = sorted(FEE_STRUCTURE.keys())
    for i, amount in enumerate(sorted_amounts):
        if principal < amount:
            return FEE_STRUCTURE[sorted_amounts[i-1]] if i > 0 else FEE_STRUCTURE[sorted_amounts[0]]
    
    return FEE_STRUCTURE[60000]

@router.post("/preview", response_model=LoanPreviewResponse)
async def loan_preview(request: LoanPreviewRequest):
    fee = calculate_fee(request.principal)
    return LoanPreviewResponse(
        principal=request.principal,
        fee=fee,
        total_repayable=request.principal + fee
    )

@router.post("/apply", response_model=LoanResponse)
async def apply_loan(
    request: LoanApplyRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if request.amount > current_user.loan_limit:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Amount exceeds your loan limit of {current_user.loan_limit}"
        )
    
    active_loan = db.query(Loan).filter(
        Loan.user_id == current_user.id,
        Loan.status.in_(["pending", "approved", "disbursed"])
    ).first()
    
    if active_loan:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have an active loan. Please repay it first."
        )
    
    fee = calculate_fee(request.amount)
    total = request.amount + fee
    
    new_loan = Loan(
        user_id=current_user.id,
        amount=request.amount,
        fee=fee,
        total=total,
        status="approved"
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    
    return new_loan

@router.get("/history", response_model=LoanListResponse)
async def get_loan_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    loans = db.query(Loan).filter(Loan.user_id == current_user.id).order_by(Loan.created_at.desc()).all()
    return LoanListResponse(loans=loans, loan_limit=current_user.loan_limit)

@router.get("/{loan_id}", response_model=LoanResponse)
async def get_loan(
    loan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    loan = db.query(Loan).filter(Loan.id == loan_id, Loan.user_id == current_user.id).first()
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found"
        )
    return loan
