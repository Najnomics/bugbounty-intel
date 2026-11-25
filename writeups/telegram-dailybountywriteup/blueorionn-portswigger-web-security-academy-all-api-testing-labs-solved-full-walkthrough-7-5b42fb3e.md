# PortSwigger Web Security Academy

- **Source URL:** https://medium.com/@blueorionn/portswigger-web-security-academy-all-api-testing-labs-solved-full-walkthrough-799fce0dca50
- **Fetched from:** https://medium.com/@blueorionn/portswigger-web-security-academy-all-api-testing-labs-solved-full-walkthrough-799fce0dca50?source=rss-1b9945f1869b------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14901 (id 14901)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Blueorionn / Tue, 08 Sep 2026 04:00:08 GMT

The API Testing labs in PortSwigger Web Security Academy go beyond classic web vulnerabilities and teach you how to attack the hidden machinery behind modern applications: undocumented endpoints, leaked API documentation, unsupported HTTP methods, hidden parameters, mass assignment, and server-side parameter pollution. This guide walks through every lab step by step, showing how to map an API’s attack surface with Burp and turn what you find into exploitable bugs.

**Lab Objective:**

To solve the lab, find the exposed API documentation and delete carlos. You can log in to your own account using the following credentials: wiener:peter.

**Solution:**

Start by fuzzing for common API paths — visiting /api in your browser immediately pays off, as the site exposes its full API documentation without any authentication.

This reveals a REST API documentation page listing every supported method: GET /user/\[username\], DELETE /user/\[username\], and PATCH /user/\[username\].

With the API fully mapped for us, deleting carlos is just a matter of sending a DELETE /api/user/carlos request.

To solve the lab, log in as the administrator and delete carlos.

This lab gives us a password reset form, so start by triggering a password reset for administrator and find the POST /forgot-password request in your Proxy history. Send it to Repeater and resend it a few times — the response is consistent, which means we have a stable input point to play with.

Now let’s probe how the back-end handles our input. Change the **username** to something invalid like administratorx and you get the following error:

`{"type":"ClientError","code":400,"error":"Invalid username."}`
Next, inject a URL-encoded & into the value: username=administrator%26x=y. The error changes to **Parameter is not supported** — that’s a huge hint. It means our username value isn’t treated as plain data; it’s being embedded into a server-side query string, and the & we injected is being parsed as a parameter separator.

If & gets injected, so should #. Appending a URL-encoded # (username=administrator%23) truncates the internal query string and the server responds with **Field not specified**. So the internal request contains a parameter we just chopped off — one called field. Confirm it by injecting username=administrator%26field=x%23, which returns Invalid field: the internal API recognizes the injected parameter, we just need a valid value.

Let’s try an obvious candidate next. Change the injected parameter to field=email (username=administrator%26field=email%23) and the original response comes back — meaning email is a valid field on the internal user object.

Check the /static/js/forgotPassword.js file from earlier — it leaks the password reset endpoint and the fact that it takes a **reset\_token** parameter: /forgot-password?reset\_token=${resetToken}. If the reset token is just another field on the user object, we can ask the internal API for it directly: username=administrator%26field=reset\_token%23. The response returns the administrator’s password reset token.

`{"result":"upt51imrd7boklfguda76iwwrrx2y0dx","type":"reset_token"}`
Now visit /forgot-password?reset\_token=YOUR\_TOKEN in the browser, set a new password, log in as administrator, and delete carlos from the admin panel.

To solve the lab, exploit a hidden API endpoint to buy a **Lightweight l33t Leather Jacket**. You can log in to your own account using the following credentials: wiener:peter.

Log in to your account with the credentials wiener:peter, then click on “**Lightweight “l33t” Leather Jacket**” product and look at your Proxy history — alongside the usual page requests, there’s an interesting one: GET /api/products/1/price.

The front-end is fetching prices through a REST API, and that’s our way in. Send it to Repeater and change the method to OPTIONS — the response tells us the endpoint also allows PATCH. A price endpoint you can modify? That’s worth investigating.

Change the method to PATCH and the server complains about a wrong Content-Type — it wants application/json. Add the header and an empty JSON body {}, and the next error message does the API mapping for us: the body is missing a price parameter. These errors are basically interactive documentation. Send {“price”:0} and the request succeeds.

Reload the jacket’s product page — it now costs $0.00. Add it to your basket and place the order to solve the lab.

To solve the lab, find and exploit a mass assignment vulnerability to buy a **Lightweight l33t Leather Jacket**. You can log in to your own account using the following credentials: wiener:peter.

Log in as wiener:peter, add the **Lightweight “l33t” Leather Jacket** to your cart, and try to place the order — you will get *INSUFFICIENT\_FUNDS* error.

Look for the API requests behind it in your Proxy history: there’s a GET /api/checkout and a POST /api/checkout.

Comparing the two is the key move here. The GET response shows us the full internal object, and it contains a chosen\_discount parameter that the POST request never sends. That’s a classic mass assignment setup — the backend object has a field we’re allowed to control but the front-end never exposes.

Send the POST /api/checkout to Repeater and add the chosen\_discount parameter to the JSON body:

```
{
  "chosen_discount": {
    "percentage": 100
  },
  "chosen_products": [
    {
      "product_id": "1",
      "quantity": 1
    }
  ]
}
```
The discount applies, the jacket becomes affordable, and the lab is solved.

Trigger a password reset for administrator, grab the POST /forgot-password request from your Proxy history, and send it to Repeater. The goal is to figure out what the back-end actually does with our username value.

```
{
  "type": "error",
  "result": "The provided username \"administratorx\" does not exist"
}
```
Next, inject a URL-encoded # into the value: administrator%23. The error changes to **Invalid route .** This tell us that URL-encoded # (username=administrator%23) truncates the internal path and returns an Invalid route error.

```
{
  "type": "error",
  "result": "Invalid route. Please refer to the API definition"
}
```
Injecting ./administrator returns the original response and ../administrator breaks the route again. So our username is being concatenated into an internal REST URL without escaping, which means we can traverse.

Let’s find out how deep we are. Add traversal sequences one at a time: ../%23, ../../%23, and so on, until ../../../../%23 returns **Internal Server Error** — we’ve walked out of the API root.

Probe for common definition files: username=../../../../openapi.json%23 returns an error that conveniently leaks the internal API structure: /api/internal/v1/users/{username}/field/{field}.

Now we know the exact route shape: username=administrator/field/email%23 returns the original response — confirming the injected field segment works. The /static/js/forgotPassword.js leaks the reset endpoint and its parameter name passwordResetToken: /forgot-password?passwordResetToken=${resetToken}.

Try username=administrator/field/passwordResetToken%23 — but the API rejects it: the application’s default API version doesn’t support that field.

```
{
  "type": "error",
  "result": "This version of API only supports the email field for security reasons"
}
```
Back up to the versioned root and request the older API: username=../../v1/users/administrator/field/passwordResetToken%23. This returns the administrator’s password reset token.

```
{
  "type": "passwordResetToken",
  "result": "uztcu3wjvjcavwqd254ywgs5av08u7tq"
}
```
Visit /forgot-password?passwordResetToken=YOUR\_TOKEN in the browser, set a new password, log in as administrator, and delete carlos from the admin panel.
