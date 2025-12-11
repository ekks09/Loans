import os
import httpx
import hashlib
import hmac
from typing import Optional

PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")
PAYSTACK_BASE_URL = "https://api.paystack.co"

class PaystackService:
    def __init__(self):
        self.secret_key = PAYSTACK_SECRET_KEY
        self.base_url = PAYSTACK_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }
    
    async def initialize_transaction(self, email: str, amount: int, reference: str, callback_url: Optional[str] = None) -> dict:
        url = f"{self.base_url}/transaction/initialize"
        payload = {
            "email": email,
            "amount": amount * 100,
            "reference": reference,
            "channels": ["mobile_money"],
            "currency": "KES"
        }
        if callback_url:
            payload["callback_url"] = callback_url
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload, headers=self.headers)
                data = response.json()
                if data.get("status"):
                    return {
                        "success": True,
                        "authorization_url": data["data"]["authorization_url"],
                        "access_code": data["data"]["access_code"],
                        "reference": data["data"]["reference"]
                    }
                return {"success": False, "message": data.get("message", "Transaction initialization failed")}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    async def verify_transaction(self, reference: str) -> dict:
        url = f"{self.base_url}/transaction/verify/{reference}"
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=self.headers)
                data = response.json()
                if data.get("status") and data["data"]["status"] == "success":
                    return {
                        "success": True,
                        "status": "success",
                        "amount": data["data"]["amount"] // 100,
                        "reference": reference,
                        "message": "Payment verified successfully"
                    }
                return {
                    "success": False,
                    "status": data["data"]["status"] if data.get("data") else "failed",
                    "amount": 0,
                    "reference": reference,
                    "message": data.get("message", "Verification failed")
                }
        except Exception as e:
            return {"success": False, "status": "error", "amount": 0, "reference": reference, "message": str(e)}
    
    def verify_webhook_signature(self, payload: bytes, signature: str) -> bool:
        computed_signature = hmac.new(
            self.secret_key.encode('utf-8'),
            payload,
            hashlib.sha512
        ).hexdigest()
        return hmac.compare_digest(computed_signature, signature)

paystack_service = PaystackService()
