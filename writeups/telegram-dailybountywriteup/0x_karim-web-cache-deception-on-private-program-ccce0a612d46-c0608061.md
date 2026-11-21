# web cache deception on private program

- **Source URL:** https://medium.com/@0x_karim/web-cache-deception-on-private-program-ccce0a612d46?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250225193735/https://medium.com/@0x_karim/web-cache-deception-on-private-program-ccce0a612d46
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8897 (id 8897)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello, I’m 0x\_karim from Morocco, passionate about cybersecurity, particularly in discovering vulnerabilities in websites and applications. I enjoy analyzing systems, identifying weaknesses, and working on improving their security. I’m always eager to enhance my skills through continuous learning and participating in cybersecurity challenges. I believe in contributing to making the digital space safer for everyone.😊

Before we begin , this is a private program, so let’s give it a name target.com

1. the first step was to gather all the javascript file names
2. I entred the files names that were collected into chatgpt and asked him to create 100 new javascript files in the same format that the website follows
3. I performed fuzzing on all the javascript input points on the website, and one file worked for me /js/test-test.js → this is an alias
4. start analyzing javascript file i found an endpoint leak information on user -> https://target.com/test/test
5. I tried many vulnerabilities on this endpoint, but it appears to be well-secured however after testing “web cache decepection”

it turned out to be vulnerable, as it stores user information if added “/hack.css” → [https://target.com/test/test](https://target.com/test/test)/hack.css , the victim information will be stored on “/hacker.css” so that if the attacker open [https://target.com/test/test](https://target.com/test/test)/hack.css he will be able to steal the victim data
