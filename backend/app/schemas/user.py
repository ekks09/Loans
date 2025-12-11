from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserRegister(BaseModel):
    phone: str
    id_number: str
    password: str

class UserLogin(BaseModel):
    phone: str
    password: str

class UserResponse(BaseModel):
    id: int
    phone: str
    id_number: str
    loan_limit: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: Optional['UserResponse'] = None

UserResponse.model_rebuild()

class TokenRefresh(BaseModel):
    refresh_token: str

class MessageResponse(BaseModel):
    message: str
