# North-South

- **Source URL:** https://medium.com/@affanhaxor/north-south-cylab-security-academy-write-up-geo-based-routing-6ce5a7df9815
- **Fetched from:** https://medium.com/@affanhaxor/north-south-cylab-security-academy-write-up-geo-based-routing-6ce5a7df9815?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14960 (id 14960)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Tue, 27 Oct 2026 05:26:30 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Category:** Web Exploitation

**Difficulty:** Easy

**Topic:** GeoIP, Nginx Routing, Geographic Access Restrictions

Web applications sometimes use a visitor’s geographic location to decide which content or services they can access. This can be useful for regional content delivery, compliance, or traffic management. However, when geographic routing is treated as a strong security control, it can create weaknesses.

In the **North-South** challenge on CyLab Security Academy, the website initially displayed a message saying that no flag was available in my region. The challenge included an Nginx configuration file that revealed how requests were routed based on the visitor’s country.

By reviewing the configuration and understanding its GeoIP-based routing logic, I identified the required country and accessed the correct backend to retrieve the flag.

I started by opening the challenge website in my browser. The page displayed a simple interface with a red navigation bar labeled “Home” and a welcome message.

Below the heading, the application showed:

No flag in this region!

This response suggested that the website was routing requests to a backend that did not contain the flag. Instead of guessing, I decided to examine the configuration provided with the challenge.

The configuration file revealed that the application used Nginx along with the GeoIP2 module. This module can determine a visitor’s country using their source IP address and a geographic database.

The relevant configuration was:

```
geoip2 /etc/nginx/GeoLite2-Country.mmdb {
    auto_reload 5m;
    $geoip2_data_country_code default=ZZ country iso_code;
}
```
```
upstream north {
    server 127.0.0.1:8000;
}
```
```
upstream south {
    server 127.0.0.1:9000;
}
```
```
server {
    listen 80;
```
```
    location / {
        if ($geoip2_data_country_code = IS) {
            proxy_pass 
        }
```
[http://south;](http://south;)
proxy\_pass [http://north;](http://north;)

}

}

This configuration contains three important parts.

**GeoIP2 country detection:** The server uses the GeoLite2 country database to determine the country code associated with the request.

**Two upstream services:** The north service points to 127.0.0.1:8000, while the south service points to 127.0.0.1:9000.

**Country-based routing:** If the detected country code is IS, Nginx sends the request to the south backend. Otherwise, the request is sent to the north backend.

The country code IS represents Iceland.

The most important part of the configuration is this condition:

```
if ($geoip2_data_country_code = IS) {
    proxy_pass http://south;
}
```
proxy\_pass [http://north;](http://north;)

In simple terms, the routing behavior is:

The initial response indicated that my normal connection was reaching the backend that returned the message “No flag in this region!”

This helped me understand that the challenge was not primarily about finding a hidden page or exploiting a login form. The key was to understand how the server selected a backend based on geographic information.

After identifying Iceland as the required country, I used a VPN service that offered an Iceland location.

I connected to the Iceland endpoint and then refreshed the challenge website. This changed the public IP address seen by the target server to one associated with the selected VPN location.

The GeoIP2 lookup could then identify the connection as originating from Iceland. As a result, the Nginx routing condition matched, and the request was forwarded to the south backend.

The page returned the flag instead of the original regional restriction message.

After connecting to the Iceland VPN endpoint and refreshing the website, the application displayed the following flag:

`academy{g30_b453d_r0u71n9_7fb7365e}`
This confirmed that the routing condition was the key to solving the challenge.

The challenge relied on geographic routing at the reverse-proxy layer.

Nginx used the GeoIP2 module to determine the country associated with the incoming connection. The result was then used to choose between two backend services.

When the request came through an IP address geolocated to Iceland, the country code matched IS. Nginx therefore routed the request to the south service, which returned the flag.

This challenge also demonstrates why simply adding a country-related HTTP header is not necessarily enough. Unless the server is explicitly configured to trust and process such a header, changing a value like X-Forwarded-For does not change the actual source IP address used by the GeoIP lookup.

In this case, using an Iceland VPN changed the network origin of the request, allowing the routing condition to match.

This challenge highlights several important lessons for developers and security testers.

**Geographic restrictions are not authentication.** A country-based routing rule should not be the only protection for sensitive information or privileged functionality.

**Review reverse-proxy configuration.** Nginx and other reverse proxies can influence which backend receives a request. Misconfigured routing may expose services or content that should remain restricted.

**Do not blindly trust forwarded headers.** Headers such as X-Forwarded-For should only be trusted when they are set by known, correctly configured proxies. Client-supplied values should not be treated as reliable identity information.

**Protect backend services independently.** Each backend should enforce appropriate authentication and authorization rather than relying entirely on the proxy to keep sensitive content hidden.

**Test geographic controls carefully.** Security assessments should verify whether location restrictions are implemented as intended and whether sensitive resources remain protected when routing conditions change.

For a real-world application, geographic routing should be treated as an additional policy rather than a replacement for proper access control.

The North-South challenge was a useful demonstration of how geographic information can influence web application routing. By inspecting the Nginx configuration, I identified the country-code condition and understood why the initial request returned a different response.

Connecting through an Iceland VPN caused the request to match the configured routing rule, allowing access to the backend containing the flag.

The main takeaway is that geographic routing controls where a request goes, but they should not replace authentication and authorization. Understanding the configuration behind an application can often reveal the reason for unexpected behavior and help identify weaknesses in its security design.

*This write-up is intended for educational purposes in the CyLab Security Academy lab environment. Test only systems you own or have explicit permission to assess.*

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
