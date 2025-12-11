from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class PaymentInitRequest(BaseModel):
    loan_id: int
    callback_url: Optional[str] = None

class PaymentInitResponse(BaseModel):
    authorization_url: str
    access_code: str
    reference: str

class PaymentVerifyResponse(BaseModel):
    status: str
    reference: str
    amount: int
    message: str

class WebhookPayload(BaseModel):
    event: str
    data: dict

class TransactionResponse(BaseModel):
    id: int
    loan_id: int
    reference: str
    amount: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
