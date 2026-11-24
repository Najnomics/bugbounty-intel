# Found a Juicy XSS Bug on a Website …

- **Source URL:** https://medium.com/@coderjack0/found-a-juicy-xss-bug-on-a-website-ebca1f64d450?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230308152645/https://medium.com/@coderjack0/found-a-juicy-xss-bug-on-a-website-ebca1f64d450
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1880 (id 1880)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Found a Juicy XSS Bug on a Website …

Hey Guys,

Bugz\_bunne This side, :)

And am gonna tall you today how I find a XSS bug in a website.

So let’s started and I hope you will learn more about after reading this bug hunting..

I was looking some new websites who recently register on [*heacker one*](http://hackerone.com).

And i was lucky got a new website who register on hacker one platformer

So i grab the opportunity and start attacking..

Frist of all i read all in scoop and out scoop and look all domains that they provide.

I make a folder in my kali Linux so its makes me more clear where i‘am store my all details about my target

*mkdir target*

And than i make a txt file inside in target folder and than i save all domains in a file while using

*gedit domian*

next step to find domain's so i use

*cat domain | assetfinder -subs-only | anew findoms*

Usage of assetfinder:

 **-subs-only**

Only include subdomains of search domain


i get all the sub domains in findoms folder

Next step .. i use the httprobe

*cat findom | httprobe -c 80 -prefer-https | anew httprespong*

Usage of httprobe:

-c int

set the concurrency level (split equally between HTTPS and HTTP requests) (default 20)

-method string

HTTP method to use (default “GET”)

-p value

add additional probe (proto:port)

-prefer-https

only try plain HTTP if HTTPS fails

-s skip the default probes (http:80 and https:443)

-t int

timeout (milliseconds) (default 10000)


I so i moved to the next step………..

# Finding The all url response in a terminal

so i use

*while read url; do echo -n “$url “; curl — head — silent — output /dev/null — write-out “%{http\_code}\n” “$url”; done \< httprespong*

so i use 4 different tool in a one command.. let me explain how the command work’s

*while* for url read,

*do* is a built-in command in the Linux shell that executes a command or a list of commands repeatedly until a specified condition is met.

*echo* for Printing a message on the screen for the user to read.

*curl* for To retrieve a file or web page from a server:

*Done* section is used to indicate the end of a loop.

after tapped on enter button i have to wait all for all response

after waiting few minutes result will be comes on the screen

some url comes with 400,403,500,000

and some comes with 200,302

next step to check all the 200 respond section to find vulnerability

luckily i found a search option that can contain *xss* vulnerability

so grab the chance and submit the bug But unfortunately that bug was claimed by the other person :(.

hard luck for i only get this bug in 20 mins and also i shear my report what i submit on the [hackerone](http://hackerone.com) platform.
