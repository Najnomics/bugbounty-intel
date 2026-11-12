# 🔐 OAuth Vulnerabilities in Exchanges: Risks of Account Takeover

- **Source URL:** https://osec.io/blog/2025-10-16-how-we-broke-exchanges-oauth-misconfigurations
- **Fetched from:** https://osec.io/blog/how-we-broke-exchanges-oauth-misconfigurations/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/909 (id 909)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How we broke exchanges: a deep dive into authentication and client-side bugs

[Bruno Halltari](https://osec.io/authors/bruno/),

[Caue Obici](https://osec.io/authors/caue/)

[#web3](https://osec.io/tags/web3/)

[#oauth](https://osec.io/tags/oauth/)

[#exchanges](https://osec.io/tags/exchanges/)

[#mobile](https://osec.io/tags/mobile/)

[#wallets](https://osec.io/tags/wallets/)

OAuth misconfigurations show how common dev settings can lead to account takeovers. Explore real cases where failing to account for differences between desktop and mobile environments left SDKs, exchanges, and wallets vulnerable to exploits.


## Exploiting OAuth

Our main research focus was related to recent vulnerabilities we found in some of our audits. One common issue we find is related to OAuth misconfigurations that can be exploited to achieve account takeover. To understand the vulnerability and the exploit itself, we first need to dig into the different OAuth flows and the configurations that can be made in the Google Cloud Console.

### Google authentication flows

During our research, we identified various Google Authentication flows that require different exploitation methods. The new/most recent flow is called GSI, which mainly uses `postMessage` for communication with the Relying Party (RP), and the old one mostly uses `redirect_uri` to send the token back to the RP.

#### GSI (new flow)

The GSI flow also has two ways to authenticate the user to the RP:

- Using FedCM API
- Without using FedCM API

FedCM (Federated Credentials Manager) is a new browser API that lets users authenticate natively to an RP using a third-party IdP.

##### FedCM method

The FedCM method basically follows this [user experience](https://privacysandbox.google.com/cookies/fedcm/why#user-interaction). Users can log in by clicking a login button (which will open a “choose your account” prompt window) or by 1-tap UX (see images below).

The normal flow, clicking the “sign in” button:

One-Tap popup shown when you open the page:

Both flows use FedCM API to authenticate using Google IdP service, which makes some CORS requests to the IdP server to return the token. After authenticating the first time, when the user returns to the same website after some time, it is possible to automatically reauthenticate using [FedCM auto-reauthentication](https://github.com/w3c-fedid/FedCM/issues/429), which has certain preconditions that must be met.

##### Non-FedCM method

This method uses a popup window (or iframe) to open the Google OAuth consent page and return the token via `postMessage`:

1. The user clicks the sign in button
2. RP opens a popup/iframe to [https://accounts.google.com/o/oauth2/v2/auth](https://accounts.google.com/o/oauth2/v2/auth) with some important parameters like `client_id` and `origin`
3. The user clicks the “Continue” button to authorize authentication
4. They get redirected to [https://accounts.google.com/gsi/transform](https://accounts.google.com/gsi/transform)
5. /gsi/transform sends the token back to the RP via `postMessage` (after some SYN/ACK messages)

#### OAuth 2.0 old flow

The old flow also redirects the user to the Google OAuth consent page and then returns the token via a `redirect_uri` provided in the URL and validated by a whitelist configuration:

1. The user clicks the sign in button
2. RP opens a popup/iframe to [https://accounts.google.com/o/oauth2/v2/auth](https://accounts.google.com/o/oauth2/v2/auth) with some important parameters like `client_id` and `redirect_uri`
3. The user clicks the “Continue” button to authorize authentication
4. They get redirected to `redirect_uri` with the token in the query parameters or `location.hash`

#### Different configurations

These two flows must be configured differently in the Google Cloud Console. There are two whitelist configurations that we can control:

- Authorized origins
- Authorized redirect URIs

The described GSI flow doesn’t use any redirection to send the token back to the RP, so the authorized redirect URI is not that important in the GSI flow. It uses the authorized origins to verify if the RP page is actually allowed to be authenticated using that `client_id`.

The actual verification in the GSI flow happens in the CORS requests made by FedCM or in `/oauth2/v2/auth` by checking the `origin` query parameter.

In the old flow, the `redirect_uri` parameter passed in the `/oauth2/v2/auth` endpoint is validated against the authorized redirect URIs.

## Note

The new GSI flow can also have a different flow using `redirect_uri` validation. To execute this flow, you need to specify [login\_uri](https://developers.google.com/identity/gsi/web/reference/js-reference#login_uri) while using the SDK.

### Localhost exploit

During one of our audits, we found a bug related to how developers test the OAuth flow in their development environment. Developers often whitelist the `localhost` origin because it is considered trusted for local testing.

Actually, this is partially true, as it depends on which security assumptions you make. This can be an issue in a mobile environment, as mobile apps can open localhost webservers without many permissions, and having a malicious app installed is not considered a significant issue on mobile since all applications are sandboxed. This configuration allows a malicious application to “escape” the sandbox and attack another system.

#### Exploit

To exploit this misconfiguration, we first needed to understand the OAuth flow used by the target. If the OAuth implementation follows a standard flow without using Google Sign-In (GSI), we can extract the token via `location.hash` or `location.search`. To achieve this, we developed a Kotlin application that spins up a local web server:

In this case, the prompt parameter can be omitted from the URL. This way, if the victim is already logged in, the OAuth 2.0 prompt interaction will be skipped.

If Google Sign-In (GSI) is being used, we found that it’s possible to use the `auto_select` parameter to trigger automatic reauthentication and bypass user interaction:

We also reported this vulnerability to the Web3Auth mobile SDK, Slush Wallet, Kukai Wallet, and several other web3 platforms. As mentioned earlier, this issue could have allowed account takeover with zero user interaction if the user had installed an application that exploited the localhost redirect.

## Note

Each team responded promptly, communicated clearly, and shipped fixes quickly. Their diligence set a strong example for coordinated response and helped ensure user security across the ecosystem.

### How to mitigate

The proper way to mitigate this issue is to disallow localhost in the live environment. Developers should have a separate staging OAuth environment with a different client ID for testing purposes. It’s important to ensure that tokens generated using the test client ID are not valid in the live environment.

## Exploiting CORS

Another bug we found during our research was related to CORS misconfiguration and how different browsers handle mixed content requests.

While checking for other bugs in exchanges, we found a CORS (Cross-Origin Resource Sharing) configuration allowing credentials and `http://` schema for any subdomain:

### CORS misconfiguration by lack of TLS

This case requires specific preconditions. The idea is to redirect the user to an insecure subdomain of `exchange.com` and spoof the response by intercepting and tampering with the victim’s network packets.

However, while testing it by simulating an MITM attack, we figured out that this type of attack behaves differently amongst the main browsers:

- **Chrome**: won’t work because cookies are not sent in `http://` → `https://` requests, even if same-site.
- **Firefox and Safari**: works since cookies are sent from an insecure context `fetch()`.

### Exploit

To exploit it, we must follow some steps:

1. Force the victim to enter an insecure webpage in the exchange subdomain
2. Deliver the malicious script to the victim using MITM (Man-In-The-Middle)
3. Use `fetch()` with CORS to do something malicious using the victim’s account

To exploit the CORS issue, an attacker must first get the victim to load an insecure subdomain. This can be achieved through techniques such as spoofing Wi-Fi or creating a fake public network that automatically opens the insecure page as the captive portal.

Once the redirect to the `http://` website is made, if the attacker is in an adjacent network, it is possible to intercept the HTTP request/response (or DNS resolve) and tamper with the returning page. The returning page should have a malicious script that exploits the CORS misconfiguration:

During our research, the misconfiguration we found was in an API with an endpoint to return the session token, so the impact was an account takeover (ATO) with some limitations since exchanges usually have MFA to perform some actions like withdrawing.

### Mitigation

As mitigation, it is recommended to remove all `http://` URLs from the CORS configuration, including localhost, since a local web server in a mobile environment can abuse it.

## Tip (Additional remediation)

Configure the HSTS policy to include all subdomains and prevent insecure subdomains from loading in the browser.

## Conclusion

In conclusion, our deep dive into authentication and client-side bugs within exchange platforms revealed several vulnerabilities stemming from misconfigurations. These types of attacks show the complexity of securing client-side applications due to the different contexts and environments they can operate in.

It also demonstrates how development configurations can harm the application’s security if they are also used in production. Thus, auditors must always understand in which environments and contexts the application will/can be run in, and ensure that the configurations are not insecure for use in production.
