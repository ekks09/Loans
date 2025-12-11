import os
import httpx
import hashlib
import hmac
from typing import Optional

PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")
PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY", "")
PAYSTACK_BASE_URL = "https://api.paystack.co"

class PaystackService:
    def __init__(self):
        self.secret_key = PAYSTACK_SECRET_KEY
        self.public_key = PAYSTACK_PUBLIC_KEY
        self.base_url = PAYSTACK_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }
    
    async def initialize_transaction(self, email: str, amount: int, reference: str, callback_url: Optional[str] = None, phone: Optional[str] = None) -> dict:
        """Initialize a Paystack transaction with M-Pesa support"""
        url = f"{self.base_url}/transaction/initialize"
        payload = {
            "email": email,
            "amount": amount * 100,  # Paystack uses cents
            "reference": reference,
            "currency": "KES"
        }
        
        # Add mobile money channels for M-Pesa
        if phone:
            payload["channels"] = ["mobile_money"]
            payload["mobile_money"] = {
                "phone": phone,
                "provider": "mpesa"
            }
        else:
            payload["channels"] = ["mobile_money", "card", "bank"]
        
        if callback_url:
            payload["callback_url"] = callback_url
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload, headers=self.headers)
                data = response.json()
                
                if data.get("status"):
                    return {
                        "success": True,
                        "authorization_url": data["data"]["authorization_url"],
                        "access_code": data["data"]["access_code"],
                        "reference": data["data"]["reference"],
                        "message": "Transaction initialized successfully"
                    }
                return {
                    "success": False,
                    "message": data.get("message", "Transaction initialization failed")
                }
        except httpx.TimeoutException:
            return {
                "success": False,
                "message": "Request timeout. Please try again."
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error initializing payment: {str(e)}"
            }
    
    async def verify_transaction(self, reference: str) -> dict:
        """Verify a Paystack transaction"""
        url = f"{self.base_url}/transaction/verify/{reference}"
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(url, headers=self.headers)
                data = response.json()
                
                if data.get("status"):
                    transaction_data = data.get("data", {})
                    status_value = transaction_data.get("status")
                    
                    if status_value == "success":
                        return {
                            "success": True,
                            "status": "success",
                            "amount": transaction_data.get("amount", 0) // 100,
                            "reference": reference,
                            "message": "Payment verified successfully",
                            "customer_code": transaction_data.get("customer", {}).get("customer_code"),
                            "authorization": transaction_data.get("authorization")
                        }
                    else:
                        return {
                            "success": False,
                            "status": status_value,
                            "amount": 0,
                            "reference": reference,
                            "message": f"Payment status: {status_value}"
                        }
                return {
                    "success": False,
                    "status": "failed",
                    "amount": 0,
                    "reference": reference,
                    "message": data.get("message", "Verification failed")
                }
        except httpx.TimeoutException:
            return {
                "success": False,
                "status": "timeout",
                "amount": 0,
                "reference": reference,
                "message": "Verification timeout. Please try again."
            }
        except Exception as e:
            return {
                "success": False,
                "status": "error",
                "amount": 0,
                "reference": reference,
                "message": f"Error verifying payment: {str(e)}"
            }
    
    def verify_webhook_signature(self, payload: bytes, signature: str) -> bool:
        """Verify Paystack webhook signature"""
        computed_signature = hmac.new(
            self.secret_key.encode('utf-8'),
            payload,
            hashlib.sha512
        ).hexdigest()
        return hmac.compare_digest(computed_signature, signature)
    
    async def get_transaction_details(self, reference: str) -> dict:
        """Get detailed transaction information"""
        url = f"{self.base_url}/transaction/{reference}"
        
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(url, headers=self.headers)
                data = response.json()
                
                if data.get("status"):
                    return {
                        "success": True,
                        "data": data.get("data", {})
                    }
                return {
                    "success": False,
                    "message": data.get("message", "Failed to get transaction details")
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error getting transaction details: {str(e)}"
            }

paystack_service = PaystackService()

