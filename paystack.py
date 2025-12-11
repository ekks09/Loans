import hmac
import hashlib
import json
import requests
from config import PAYSTACK_SECRET_KEY, PAYSTACK_WEBHOOK_SECRET

PAYSTACK_BASE = "https://api.paystack.co"

def init_transaction(email, amount_kobo, callback_url=None, metadata=None):
    url = f"{PAYSTACK_BASE}/transaction/initialize"
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "email": email,
        "amount": amount_kobo,
    }
    if callback_url:
        payload["callback_url"] = callback_url
    if metadata:
        payload["metadata"] = metadata
    resp = requests.post(url, headers=headers, json=payload, timeout=15)
    resp.raise_for_status()
    return resp.json()

def verify_transaction(reference):
    url = f"{PAYSTACK_BASE}/transaction/verify/{reference}"
    headers = {"Authorization": f"Bearer {PAYSTACK_SECRET_KEY}"}
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    return r.json()

def verify_webhook_signature(body_bytes, signature_header):
    """
    Paystack sends X-Paystack-Signature header containing HMAC SHA512 of the raw body
    using your PAYSTACK_WEBHOOK_SECRET as key.
    """
    if not PAYSTACK_WEBHOOK_SECRET:
        raise RuntimeError("PAYSTACK_WEBHOOK_SECRET not set")
    computed = hmac.new(PAYSTACK_WEBHOOK_SECRET.encode(), body_bytes, hashlib.sha512).hexdigest()
    return hmac.compare_digest(computed, signature_header)
