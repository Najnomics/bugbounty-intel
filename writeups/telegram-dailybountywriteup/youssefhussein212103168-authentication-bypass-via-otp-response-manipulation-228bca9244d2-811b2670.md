# Authentication Bypass via OTP Response Manipulation

- **Source URL:** https://medium.com/@youssefhussein212103168/authentication-bypass-via-otp-response-manipulation-228bca9244d2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821175940/https://medium.com/@youssefhussein212103168/authentication-bypass-via-otp-response-manipulation-228bca9244d2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9806 (id 9806)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Authentication Bypass via OTP Response Manipulation

# Summary

During my latest penetration testing engagement , I discovered a high authentication bypass vulnerability in the registration and OTP verification process. An attacker can register an account using invalid or fake data and manipulate server responses to bypass both mobile number verification and OTP validation. This vulnerability allows full unauthorized access to the platform without the need for a legitimate mobile number or email address.

# 🐞 Vulnerability Details

- **Vulnerability Type**: Authentication Bypass via Response Manipulation
- **Affected Endpoint**: `/my-account`
- **Authentication Required**: No
- **Impact**: High **— Full Account Creation & Authentication Bypass**

# 🧪 Steps to Reproduce

# 1. Navigate to Registration Page

Go to: `https://target.com/my-account/` and click on `تسجيل جديد (New Registration)`.

# 2. Submit Fake Data

Fill in the registration form with:

- **Mobile number**: (any fake data)
- **Password**: Any
- **First Name / Last Name**: Any
- **Email**: Any

*Note: There is no client-side validation on the registration inputs.*


# 3. Intercept Registration Request with Burp Suite

- Send the form.
- Intercept the **server response** in Burp Suite.
- Observe the response contains a **failure message** due to invalid mobile number.

# 4. Manipulate Registration Response

- Change the response manually in Burp Suite:
- Forward the modified response to the browser.

*💥 The OTP input field now appears even though the number is invalid.*


# 5. Submit Fake OTP

- Enter any random number (e.g., `000000`) in the OTP field.
- Intercept the **OTP verification request** and its **response**.

# 6. Manipulate OTP Verification Response

- Modify the response code to simulate a valid OTP:
- change success message from failure to success

```
success:false
code:0
success:true
code:2
```
- successfully registered with fake data

# Impact

- **Severity**: High
- **Risk**:
- Allows **unauthenticated attackers** to **register fake accounts**.
- Completely **bypasses phone number validation** and **OTP verification**.
- May lead to **spam account creation**, **fraud**, or **abuse** of the platform.
- Enables **automated bot registrations** without any identity verification.

# Mitigation Recommendations

1. **Enforce Backend Validation**

- Ensure all OTP checks and number verifications are performed **server-side**.
- Never rely on client responses for critical flows like OTP confirmation.

**2. Use Strong Server Response Integrity**

- Sign server responses (e.g., HMAC or tokens).
- Implement **response authenticity validation** to prevent tampering.

**3. Rate Limit OTP and Registration Attempts**

- Add rate-limiting and CAPTCHAs to mitigate automated abuse.

**4. Use Session Tokens**

- Tie the OTP verification to a unique session and phone number.

# 📌 Conclusion

This vulnerability allows attackers to fully bypass the mobile number verification and OTP process, leading to critical authentication flaws. Without addressing this, the platform is at risk of bot attacks, impersonation, and mass fake account creation. Immediate remediation is recommended.
