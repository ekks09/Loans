from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoanPreviewRequest(BaseModel):
    principal: int

class LoanPreviewResponse(BaseModel):
    principal: int
    fee: int
    total_repayable: int

class LoanApplyRequest(BaseModel):
    amount: int

class LoanResponse(BaseModel):
    id: int
    user_id: int
    amount: int
    fee: int
    total: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class LoanListResponse(BaseModel):
    loans: list[LoanResponse]
    loan_limit: int
