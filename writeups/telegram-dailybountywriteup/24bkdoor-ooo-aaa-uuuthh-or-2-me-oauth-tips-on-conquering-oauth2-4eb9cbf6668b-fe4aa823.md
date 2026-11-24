# “Ooo aaa uuuthh” or 2 me, OAuth ! Tips on conquering OAuth2!

- **Source URL:** https://medium.com/@24bkdoor/ooo-aaa-uuuthh-or-2-me-oauth-tips-on-conquering-oauth2-4eb9cbf6668b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230508042928/https://medium.com/@24bkdoor/ooo-aaa-uuuthh-or-2-me-oauth-tips-on-conquering-oauth2-4eb9cbf6668b
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2604 (id 2604)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **“Ooo aaa uuuthh” or 2 me, OAuth ! Tips on conquering OAuth2!**

## Author: [24BkDoor](https://medium.com/u/56e285e5a007?source=post_page-----4eb9cbf6668b--------------------------------)

**What is OAuth2?**

OAuth2 is a popular protocol for securing API access and authorization. In OAuth2, the client ID and client secret are two distinct pieces of information used for client authentication. In this response, we will provide more scripts and examples to elaborate on each key point regarding client ID and client secret.

## **Importance of protecting client ID and client secret**

As mentioned earlier, the client ID is a public identifier, while the client secret is a private key. The client ID is not considered sensitive information and is often included in URLs or query parameters. However, the client secret should be kept confidential and not shared publicly.

*Example:*

Here is an example of how client ID and client secret are used in OAuth2 authentication flow:

```
python
import requests
# Obtain client ID and secret from OAuth2 provider
client_id = 'your_client_id'
client_secret = 'your_client_secret'
# Request access token from OAuth2 provider
auth_url = 'https://oauth2.provider.com/token'
payload = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
response = requests.post(auth_url, data=payload)
# Extract access token from response
access_token = response.json()['access_token']
```
*Breakdown:*

In this script, the client ID and client secret are used to authenticate the client and obtain an access token from the OAuth2 provider. It is important to protect both pieces of information to prevent unauthorized access to client resources.

## **Protecting client secret**

Extra precautions should be taken to protect the client secret. This includes not sharing it publicly, storing it securely (e.g., using encryption), and rotating it periodically.

Here is an example of how to encrypt the client secret using the Fernet cryptography library in Python:

*Example:*

```
python
from cryptography.fernet import Fernet
# Generate encryption key
encryption_key = Fernet.generate_key()
# Encrypt client secret
client_secret = 'your_client_secret'
cipher_suite = Fernet(encryption_key)
encrypted_secret = cipher_suite.encrypt(client_secret.encode('utf-8'))
# Decrypt client secret
decrypted_secret = cipher_suite.decrypt(encrypted_secret).decode('utf-8')
```
*Breakdown:*

In this script, the client secret is encrypted using the Fernet cryptography library. The encryption key can be stored securely and used to decrypt the client secret as needed. This provides an extra layer of protection for the client secret.

## **Potential security risks**

If an attacker gains access to the client ID, they may be able to see which APIs the client is authorized to access, but they would not be able to make requests without the client secret. If an attacker gains access to the client secret, they would be able to make unauthorized requests on behalf of the client.

Here is an example of how an attacker can use an exposed client secret to make unauthorized requests:

*Example:*

```
python
import requests
# Exposed client secret
client_secret = 'your_client_secret'
# Malicious API request
api_url = 'https://api.example.com/malicious'
payload = {'param1': 'value1', 'param2': 'value2'}
headers = {'Authorization': 'Bearer ' + client_secret}
response = requests.post(api_url, data=payload, headers=headers)
```
*Breakdown:*

In this script, an attacker can use an exposed client secret to make unauthorized requests to the API. The attacker includes the client secret in the Authorization header of the request, allowing them to authenticate as the client and make unauthorized API requests.

## **Real-world examples**

There have been numerous real-world examples of client ID and client secret leaks in the past, including in bug bounty reports.

Here are a few examples of those:

*Bug bounty report for Fitbit*

In this bug bounty report, the researcher was able to obtain the client ID and client secret for the Fitbit API from a publicly accessible JavaScript file on the company’s website. The researcher was then able to use the client secret to make unauthorized requests to the Fitbit API.

Bug bounty report for Fitbit: [https://hackerone.com/reports/78176](https://hackerone.com/reports/78176)


*Twitter API keys exposed*

In 2017, Twitter announced that it had discovered a bug that exposed the client ID and client secret for its API. The company advised developers to regenerate their API keys and implement additional security measures to protect their apps.

Twitter API: [https://blog.twitter.com/developer/en\_us/topics/tools/2017/api-keys-and-access-tokens.html](https://blog.twitter.com/developer/en_us/topics/tools/2017/api-keys-and-access-tokens.html)


*Google+ API data leak*

In 2018, Google announced that it had discovered a bug in the Google+ API that had exposed the client ID and client secret for third-party apps. The company shut down the API and advised developers to update their apps and implement additional security measures.

Google+ data leak: [https://www.blog.google/technology/safety-security/project-strobe/](https://www.blog.google/technology/safety-security/project-strobe/)


## To conclude

These examples highlight the importance of protecting client ID and client secret and the potential risks associated with their exposure. It is essential for developers to implement robust security measures and regularly review and update them to ensure the protection of client resources.
