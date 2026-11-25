# From CSPT to DOM XSS

- **Source URL:** https://medium.com/@AstroKrypTech/from-cspt-to-dom-xss-chaining-an-open-redirect-with-malicious-json-71a58c462c2a
- **Fetched from:** https://web.archive.org/web/20261109151455/https://medium.com/@AstroKrypTech/from-cspt-to-dom-xss-chaining-an-open-redirect-with-malicious-json-71a58c462c2a
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14941 (id 14941)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# From CSPT to DOM XSS: Chaining an Open Redirect with Malicious JSON

Bonus: A webhook.site alternative for security testing

A client-side path traversal vulnerability in the application’s profile-page loader allows an attacker to influence the URL used for a JSON API request. By supplying traversal sequences in a query parameter, the request can be redirected from the expected API endpoint to an open redirect. The redirect then points to an attacker-controlled JSON response.

The application accepts that response as valid object data and inserts one array field into the DOM using `innerHTML`. This creates a DOM-based XSS condition.

## Affected Functionality

The affected workflow is a public profile page that loads an object using an identifier from the URL:

`const id = new URLSearchParams(location.search).get("id");````
fetch(`/api/user/${id}`)
        .then(response => {
            if (!response.ok) throw new Error('User not found');
            return response.json();
        })
        .then(user => {
            displayUser(user);
            loading.classList.add('hidden');
            details.classList.remove('hidden');
        })
        .catch(err => {
            console.error('Error loading user:', err);
            showError();
        });
```
