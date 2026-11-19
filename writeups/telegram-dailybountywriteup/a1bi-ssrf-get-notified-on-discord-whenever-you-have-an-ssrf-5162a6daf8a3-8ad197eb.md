# SSRF!

- **Source URL:** https://medium.com/@a1bi/ssrf-get-notified-on-discord-whenever-you-have-an-ssrf-5162a6daf8a3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143251/https://medium.com/@a1bi/ssrf-get-notified-on-discord-whenever-you-have-an-ssrf-5162a6daf8a3
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1919 (id 1919)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF! : Get notified on discord whenever you have an SSRF

I was not a fan of automation. I was only using tools to do subdomain enumeration and directory brute forcing. The reset of my testing was completely manual.

Whenever I test SSRF, i use [https://app.interactsh.com/](https://app.interactsh.com/) and burp collaborator to see the callback. Lately I have put a decent amount of time testing on SSRF in particular and learned new strategies by myself.

I came to know that it is a good idea if I create a tool to test SSRF for myself. So, the first step will be creating a 24/7 active link which I can use to hit and get notified as soon as I have a callback.

For that, I created a site on a free hosting service and hosted a php file in it. Whenever the URL of the site gets hit by any service, I get a callback on my discord server. It also displays the IP address and user-agent of the vulnerable service as shown below.

To do that, I used [000webhost.com](https://in.000webhost.com/free-website-sign-up) to host a simple site freely. As everyone knows, anyone can create an account here. And then, you should create a discord server.

I think that explaining the process of making this in simple steps is pretty enough. So, here it goes :

1. Go to your discord and create a new discord server
2. create a channel > click on its settings > integrations > webhook
3. create a webhook and copy the `webhookurl`
4. Go to : [https://in.000webhost.com/free-website-sign-up](https://in.000webhost.com/free-website-sign-up) and sign up and then login.
5. Click on `Manage website` on websites lists, and go to the site’s dashboard
6. click on `file manager` and then click on `upload files`. Now you will be redirected to the `file manager`
7. Open `public_html.` Remove the `index.html` and create a new file called `index.php`
8. Copy the following php code to `index.php`then replace the **webhook url** in the code with your’s and save.

````
<?php
date_default_timezone_set('Asia/Kolkata'); //Change this if you need to
$date = date('Y-m-d H:i:s');
$ip_address = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$endpoint = $_SERVER['REQUEST_URI'];
$log_message = "**Seems like you have a HIT**\n```Date: $date\t\nIP: $ip_address\t\nUser-Agent: $user_agent\t\nPath: $endpoint```\n";
// echo $log_message;
echo "<body><h1>Hit Me Harder :) </h1></body>";
$webhook_url = "https://discord.com/api/webhooks/10589949/E9uS3k9MxnI5CiIfmtmXHfornTObgZ_xl"; // replace with your webhook URL
$message = array("content" => "$log_message"); // the message you want to send
$ch = curl_init($webhook_url);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-type: application/json'));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($message));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_exec($ch);
curl_close($ch);
?>
````
The SSRF notifier is set by now. You can go to https://\<your-site>.000webhostapp.com to test the callback. And you will probably receive a notification on your discord similar to the above screenshot if everything goes well.

## So, what is the advantage of using this?

1. You can see the notification on any devices where-ever you can use discord.
2. You are making this notifier from scratch. So you can upgrade this to test internal redirects and content discoveries and more.
3. You see what you want to see : the IP address and the user-agent, since I don’t find any other good alternative tool that does this.

4\. It will be active 24/7.

5\. You will get the callback if it is done using some libraries and not just a headless browser particularly.

Hope you like this content. Please follow my account so that I can make more content like this.
