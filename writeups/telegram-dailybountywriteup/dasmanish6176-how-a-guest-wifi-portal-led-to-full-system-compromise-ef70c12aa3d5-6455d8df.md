# How a Guest WiFi Portal Led to Full System Compromise

- **Source URL:** https://medium.com/@dasmanish6176/how-a-guest-wifi-portal-led-to-full-system-compromise-ef70c12aa3d5
- **Fetched from:** https://medium.com/@dasmanish6176/how-a-guest-wifi-portal-led-to-full-system-compromise-ef70c12aa3d5?source=rss-85853724a5d8------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14908 (id 14908)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Dasmanish / Sat, 12 Sep 2026 06:08:49 GMT

**How a Guest WiFi Portal Led to Full System Compromise**

**Hack Smarter World Walkthrough**

**1. Initial reconnaissance**

I started with a full TCP port scan to identify the exposed attack surface. Three interesting services were available: an HTTP application on port 80, the standard SSH service on port 22, and a second SSH service on port 2222.

**2. Web application / JavaScript discovery**

While inspecting the application’s static assets, I found a JavaScript source map. Source maps are often extremely useful during security testing because they can expose original source files that were hidden during production deployment.

**3. API information disclosure**

The endpoint was accessible without authentication and returned active guest information. The application therefore exposed data that could be used to interact with another authentication mechanism.

**4. Portal authentication**

The leaked room and guest information could then be supplied to the portal’s login endpoint. The server accepted the combination and created an authenticated session.

**5. Discovering SSTI**

curl -i -b /tmp/hsw.cookies \

-c /tmp/hsw.cookies \

-X POST http://10.1.139.131/profile \

--data-urlencode 'display\_name={{7\*7}}'

I tested whether the profile field was being safely rendered or interpreted as a server-side template. The expression {{7\*7}} was evaluated and returned 49, confirming server-side template injection.

**6. SSTI → RCE**

After confirming SSTI, I verified whether the template context could reach Python’s underlying functionality. The resulting command execution confirmed OS-level code execution as www-data.

**7. Local enumeration**

**8. The SSH key vulnerability**

A private SSH key should generally **not be world-readable**.

**9. SSH lateral movement**

**10. Credential leakage through .bash\_history**

George’s shell history contained credentials used to switch to another local account. This provided a second pivot from George to David.

**11. David + adm**

David was a member of the adm group. On Debian/Ubuntu systems, this commonly provides access to system logging data, making /var/log an interesting source of information.

**12. The root credential leak**

The provisioning log contained a credential intended for a root-level synchronization process. Because David could read the log through his adm membership, the credential was exposed.
