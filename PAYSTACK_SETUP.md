# Paystack M-Pesa Integration Guide

## Table of Contents
1. [Getting Started with Paystack](#getting-started-with-paystack)
2. [M-Pesa Setup](#mpesa-setup)
3. [Integration in Your App](#integration-in-your-app)
4. [Testing](#testing)
5. [Production Setup](#production-setup)
6. [Troubleshooting](#troubleshooting)

---

## Getting Started with Paystack

### What is Paystack?
Paystack is a payment gateway that allows you to accept payments in multiple ways:
- **M-Pesa** (Mobile Money in Kenya)
- **Card Payments**
- **Bank Transfers**
- **Mobile Money** (other African countries)

### Step 1: Create Paystack Account

1. Go to https://paystack.com
2. Click **Sign Up**
3. Fill in your details:
   - Business Name: "MicroLoan"
   - Email: your@email.com
   - Password: strong password
4. Click **Create Account**

### Step 2: Verify Your Account

1. **Email Verification:** Click link in verification email
2. **Phone Verification:** Add and verify your phone number
3. **Business Verification:** Upload:
   - Business registration documents (or ID if freelancer)
   - Bank account details
4. Wait for Paystack to verify (usually 1-24 hours)

### Step 3: Get Your API Keys

Once verified:

1. Go to **Settings** ⚙️
2. Click **API Keys & Webhooks**
3. You'll see:
   - **Secret Key** (starts with `sk_test_` for testing or `sk_live_` for production)
   - **Public Key** (starts with `pk_test_` for testing or `pk_live_` for production)

### Step 4: Save Your Keys

**Important:** These are SECRET! Never share them.

Copy and paste into your `.env` file:

```env
PAYSTACK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxxx
PAYSTACK_PUBLIC_KEY=pk_test_xxxxxxxxxxxxxxxxxxxxx
```

---

## M-Pesa Setup

### What is M-Pesa?

M-Pesa is a mobile money service by Safaricom (Kenya's largest telecom):
- Users transfer money using **phone number and PIN**
- Available on any phone (smart or basic)
- Fast and secure payment method
- Perfect for unbanked populations

### Enable M-Pesa on Paystack

#### Test Mode Setup (Free - for development)

1. Go to Paystack Dashboard
2. Click **Settings** ⚙️
3. Go to **Payment Options**
4. Find **Mobile Money** section
5. Select **Kenya**
6. Toggle **M-Pesa** to **ON**

Paystack will provide:
- **Test Till Number** (for testing)
- **Test Phone Numbers** (to use during testing)
- **Instructions** for test payments

#### Live Mode Setup (Real Money)

To accept real M-Pesa payments:

1. **Upgrade Account:** Contact Paystack support
2. **Complete KYC:** Full business verification
3. **Set Up Till:** 
   - Option A: Get Paystack-managed till number
   - Option B: Use your existing Till number (if you have one from Safaricom/bank)
4. **Banking Details:** Link your bank account for settlements
5. **Request Live Keys:** Paystack will provide production keys

---

## Integration in Your App

### How the Payment Flow Works

```
User                 Your App              Paystack              M-Pesa
 |                     |                      |                    |
 |--Apply for Loan----->|                      |                    |
 |                     |                      |                    |
 |<--Show Pay Button----|                      |                    |
 |                     |                      |                    |
 |--Click "Pay Now"---->|                      |                    |
 |                     |---Initialize----->|                    |
 |                     |<--Auth URL--------|                    |
 |                     |                      |                    |
 |<--Redirect to PayStack Page|              |                    |
 |                     |                      |                    |
 |---Enter Phone & PIN-->|                    |                    |
 |                     |                    |---Send USSD----->|
 |                     |                    |                |
 |<--M-Pesa Prompt----|<---M-Pesa Prompt---|<---Prompt------|
 |                     |                    |                |
 |--Enter PIN (on phone)----M-Pesa Popup----->|                |
 |                     |                    |<--Confirm------|
 |                     |                      |                |
 |                     |<--Verify Payment----|                |
 |                     |                      |                |
 |<--Success Page------| (Loan marked repaid) |                |
```

### Your App Configuration

The Paystack integration is already built into your app!

**Backend Code:** `backend/app/services/paystack_service.py`

**Frontend Code:** `frontend/payment.html`

### Test the Integration Locally

```bash
# Start your app
RUN_APP.bat

# Go to http://localhost:8000
# 1. Register account
# 2. Apply for loan
# 3. Click "Pay Now"
# 4. Enter Paystack test phone number
# 5. Complete test payment
```

---

## Testing

### Test Phase 1: Basic Setup

1. **Verify Keys Are Set:**
   ```bash
   # Check .env file has:
   PAYSTACK_SECRET_KEY=sk_test_...
   PAYSTACK_PUBLIC_KEY=pk_test_...
   ```

2. **Check API Documentation:**
   - Start your app
   - Go to http://localhost:8000/docs
   - Look for `/api/payments/initialize` endpoint
   - Click "Try it out"

### Test Phase 2: End-to-End Payment

1. **Create Test Account:**
   - Go to http://localhost:8000
   - Register: Phone `0712345678`, Password `test123`

2. **Apply for Loan:**
   - Click "Apply for Loan"
   - Select 5,000 KES
   - Click "Apply Now"

3. **Make Test Payment:**
   - Go to Dashboard
   - Find your loan
   - Click "Pay Now"
   - Enter test phone number Paystack provides
   - Click "Proceed to Payment"

4. **Complete on Paystack:**
   - You'll be redirected to Paystack
   - Follow test payment instructions
   - Check your loan is marked "Repaid"

### Test Scenarios

| Scenario | Test Data | Expected Result |
|----------|-----------|-----------------|
| Valid payment | Phone: 254712345678<br>Amount: 5000 KES | Payment succeeds |
| Wrong PIN | Enter wrong M-Pesa PIN | Payment fails |
| Timeout | Don't complete M-Pesa within time | Payment cancelled |
| Already paid | Try to pay same loan twice | Error shown |
| Exceed limit | Try to apply 70,000 KES (over 60,000 limit) | Application rejected |

---

## Production Setup

### Before Going Live

#### 1. Upgrade Paystack Account
- Contact Paystack support: support@paystack.com
- Request live access
- Complete additional KYC if needed

#### 2. Get Live Keys
- Paystack will provide production keys
- They start with `sk_live_` and `pk_live_`

#### 3. Update Your App

```env
# Remove _test_ from keys
PAYSTACK_SECRET_KEY=sk_live_xxxxxxxxxxxxxxxxxxxxx
PAYSTACK_PUBLIC_KEY=pk_live_xxxxxxxxxxxxxxxxxxxxx

# Update URLs if hosting
BACKEND_URL=https://your-domain.com
FRONTEND_URL=https://your-domain.com
```

#### 4. Set Up Webhook

Paystack can notify your app about payments:

1. Go to **Settings** → **API Keys & Webhooks**
2. Add Webhook URL:
   ```
   https://your-domain.com/api/payments/webhook
   ```
3. Select events:
   - `charge.success` ✅
   - `charge.failed` ✅
4. Save

Your app already handles webhooks in `backend/app/routers/payments.py`

#### 5. Banking Details

1. Go to **Settings** → **Bank Accounts**
2. Add your business bank account
3. Select settlement schedule:
   - **Instant** (settled immediately)
   - **Daily** (settled once per day)
   - **Manual** (settle when you request)

#### 6. Test Live Setup

1. Make test transactions with:
   - Real phone numbers
   - Small amounts (100-500 KES)
   - Different payment methods (if enabled)

2. Verify in Dashboard:
   - Transaction appears in **Transactions** tab
   - Settlement appears in **Settlements** tab
   - Balance updates correctly

---

## Troubleshooting

### Payment Initialization Fails

**Error:** "Transaction initialization failed"

**Causes:**
- Invalid Paystack keys in `.env`
- Paystack account not verified
- M-Pesa not enabled for your country
- Network timeout

**Solutions:**
1. Verify keys are copied correctly (no extra spaces)
2. Go to Paystack dashboard and check account status
3. Confirm M-Pesa is enabled in Payment Options
4. Check internet connection
5. Try again in a few moments

### Payment Completes But App Shows "Failed"

**Cause:** Webhook not set up or not receiving events

**Solutions:**
1. Go to Paystack dashboard → API Keys & Webhooks
2. Verify webhook URL is correct and accessible
3. Check webhook test by Paystack
4. Verify backend is running and reachable
5. Contact Paystack support if webhook keeps failing

### Phone Number Not Recognized

**Possible Issues:**
- Incorrect format (should be 254712345678, not +254... or 0712...)
- Not a valid M-Pesa number
- Using test number in live mode (or vice versa)
- Safaricom network issue

**Solutions:**
1. Verify phone number format:
   - ✅ `254712345678` (correct)
   - ❌ `+254712345678` (wrong - no +)
   - ❌ `0712345678` (wrong - no country code)
2. For test: Use Paystack-provided test numbers
3. For live: Use real M-Pesa enabled numbers

### Paystack Test vs Live

| Feature | Test Mode | Live Mode |
|---------|-----------|-----------|
| Keys Start With | `sk_test_`, `pk_test_` | `sk_live_`, `pk_live_` |
| Real Money? | No, test only | Yes, real payments |
| Test Numbers | Provided by Paystack | Real phone numbers |
| Settlements | Not actual | Go to your bank account |
| Support | Sandbox testing | Real transactions |

### Check Transaction Status

1. Go to Paystack Dashboard
2. Click **Transactions**
3. Search by:
   - Reference number (LOAN_123_ABC...)
   - Phone number
   - Amount
4. Click transaction to see details:
   - Status (success/failed)
   - Amount
   - Channel used
   - Customer info
   - Settlement status

### Contact Paystack Support

- **Email:** support@paystack.com
- **Chat:** Available in dashboard
- **Hours:** Business hours, West African Time
- **Response:** Usually within 2-24 hours

---

## FAQ

**Q: Is my money safe with Paystack?**
A: Yes! Paystack is PCI-DSS compliant and regulated by CBN (Nigeria's central bank).

**Q: How long until money reaches my bank?**
A: Depends on your settlement schedule:
- **Instant:** 5-15 minutes
- **Daily:** Next business day
- **Manual:** When you request

**Q: Can I accept payments from other countries?**
A: Yes! Paystack supports:
- Kenya (M-Pesa)
- Nigeria (all methods)
- Ghana, Uganda, South Africa, etc.

**Q: What are the fees?**
A: Usually 1.5-5% depending on method. Check Paystack pricing page.

**Q: Can I refund payments?**
A: Yes! Go to Transactions → click transaction → Refund button.

**Q: Is there a minimum payment amount?**
A: Minimum is usually 1 KES. Check Paystack documentation.

**Q: Can I test without real money?**
A: Yes! Use test mode with Paystack-provided test numbers.

---

## Additional Resources

- [Paystack Documentation](https://paystack.com/docs)
- [M-Pesa Integration Guide](https://paystack.com/docs/payments/mobile-money/)
- [API Reference](https://paystack.com/docs/api/)
- [Webhooks Guide](https://paystack.com/docs/webhooks/)
- [Status Pages](https://status.paystack.com/)

---

**Your app is ready to accept M-Pesa payments!** 🎉

Next steps:
1. Get Paystack account and API keys ✅
2. Add keys to `.env` ✅
3. Test payments with RUN_APP.bat ✅
4. Go live with production keys ✅
