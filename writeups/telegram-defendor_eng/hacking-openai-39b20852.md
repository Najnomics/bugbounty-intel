# 🔓 Researchers Chained a libheif RCE and SSO Flaw to Access OpenAI's Internal Repos

- **Source URL:** https://www.hacktron.ai/blog/hacking-openai
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2112 (id 2112)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hacking OpenAI


 [Harsh Jaiswal](https://www.hacktron.ai/team/rootxharsh) 

 [Mohan Pedhapati](https://www.hacktron.ai/team/s1r1us) 

 [Rahul Maini](https://www.hacktron.ai/team/iamnoooob) 

[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.hacktron.ai%2Fblog%2Fhacking-openai&text=Hacking+OpenAI),

## 

On July 25, 2026, we chained two critical vulnerabilities to compromise multiple OpenAI employees’ ChatGPT accounts. With these accounts, we could then access internal OpenAI repositories, and potentially many other connectors.

To prove we had in fact gained the access we believed without allowing ourselves to learn any sensitive information, we used the employee’s Codex to open a PR #1186742 in OpenAI’s internal monorepo `openai/openai`.

### 

### 

1. We traced Discourse's HEIF upload path through ImageMagick to libheif and found the heap overflow.
2. Opus 4.8 got the first code-execution exploit working with ASLR disabled.
3. 06:00 UTC Opus 5 turned it into a reliable local image-upload exploit with ASLR on.
4. 10:00 UTC The code-execution exploit worked against our Discourse Cloud instance, then OpenAI's forum at community.openai.com.
5. 13:30–15:30 UTC We used an employee's Codex account to open a harmless PR in OpenAI's internal monorepo, then stopped testing.

Until July 25, 2026, any user or OpenAI employee logging into OpenAI’s own help forum ([community.openai.com](http://community.openai.com/)) could have had their ChatGPT and Codex accounts taken over. Since people can connect various services to Codex and ChatGPT, the scope of what we could theoretically access was huge, including GitHub, Slack and emails.

From finding the bug to reaching OpenAI’s internal repositories took less than 72 hours.

We immediately reported the initial vulnerability to OpenAI and Discourse and worked with them to coordinate the patch. OpenAI confirmed its fix about 14 hours after our report, and Discourse had a fix two days after we reported to it. OpenAI also paid us a $6,500 bounty.

### 

1. 05:00–06:00 UTC The Hacktron team obtained remote code execution (RCE) and administrative access to the Discourse environment hosted at `community.openai.com`.
2. 08:00–10:00 UTC After confirming the cross-product impact, the team coordinated internally on the responsible disclosure process and submitted a report through OpenAI's Bug Bounty Program on Bugcrowd.
3. 13:30–15:30 UTC We accessed an OpenAI employee's account and created a harmless proof-of-concept pull request in OpenAI's internal monorepo (link redacted at OpenAI's request). We updated the existing Bugcrowd submission with these findings, reached out to friends at OpenAI on Twitter/X to notify them directly, and ceased all further testing at approximately 15:30 UTC.
4. 22:49:45 UTC OpenAI replied to the report confirming its fix, roughly 14 hours after the initial submission.
5. We submitted a report to Discourse through its HackerOne program.
6. Discourse replied to the report on Sunday.
7. Discourse had a fix ready by Monday and added image-processing sandboxing as defense in depth.
8. Discourse published [GHSA-vhm9-85gw-x335](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335) with patch and rebuild guidance.
9. OpenAI paid a $6,500 bounty and marked the report resolved. It commented: "To clarify the scope of that award: testing against the Discourse-hosted community.openai.com was explicitly excluded from our bug bounty program. The award recognizes the OpenAI-side finding, not the actions against Discourse."

## 

A few months ago, our team at Hacktron, led by Harsh Jaiswal alongside Mohan Pedhapati and Rahul Maini, began researching frontier AI companies to find security vulnerabilities. This led us to discover an SSO misconfiguration in OpenAI’s identity infrastructure and a `libheif` RCE in the community forum used by OpenAI.

We’ve since expanded the research into [HEIF Heist](https://heif-heist.com), a multi-month investigation tracing `libheif` across Slack, Meta, GitHub Enterprise, Ruby on Rails, and Node.js frameworks such as Next.js, Astro, and Gatsby. A [surprising amount](https://xkcd.com/2347/) of widely-used software depends on this one image-processing library:[1](https://www.hacktron.ai#user-content-fn-xkcd)

If your application processes user-controlled images and accepts .heic/.heif/.avif images, it is highly likely it is affected. Please reach out to us at [hello@hacktron.ai](mailto:hello@hacktron.ai) if you need any kind of assistance.

## 

Warning

If you self-host Discourse, rebuild your installation now. Older Docker images may contain a vulnerable `libheif` dependency that permits code execution through an image upload. Run `git pull` followed by `./launcher rebuild app` from `/var/discourse`; a web-interface update alone may not replace the underlying image. Discourse-hosted customers have already been patched. See the [security advisory](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335).

OpenAI uses Discourse for their forum and allows “Sign in with OpenAI” through `auth.openai.com`. After getting a good understanding of OpenAI’s services and infrastructure, we had reason to believe that compromising the forum could create a path into broader OpenAI services through this identity flow. To test that hypothesis, we first needed remote code execution on an OpenAI service like the Discourse community forum.

While the Discourse app itself is actually not an easy target (we have looked into it in the past), we thought we could go after a dependency.

### 

On July 23, we started reviewing Discourse’s image-upload pipeline, and we found that HEIC and HEIF files followed an unusual path. Discourse normally used FastImage for image checks, but because FastImage did not support HEIF, it passed those files to ImageMagick’s `magick` command for conversion.<sup>[2](https://www.hacktron.ai#user-content-fn-discourse-heic)</sup> That exposed the underlying `libheif` parser directly to attacker-controlled files.

We started an Opus 4.8 session with the Discourse Docker image and asked it to inspect the installed `libheif` package for security issues. After a while, it found that some particular security fixes were not back-ported to the libheif package. This allowed a heap buffer overflow leading to OOB R/W primitives during HEIC decoding.

The vulnerable code had been changed upstream the previous year, but the commit was not documented as a security fix and received no CVE.<sup>[3](https://www.hacktron.ai#user-content-fn-libheif-commit)</sup> This might be a reason why Debian 12 and 13 have not received the security relevant backports in time. Because Discourse’s Docker image was based on Debian 12, it installed the vulnerable `libheif` version 1.19.7. Even Debian 13 still shipped the vulnerable version 1.19.8 at the time. Debian published its security update for Debian 13 on August 8, 2026.[4](https://www.hacktron.ai#user-content-fn-debian-dsa)

On July 24, we used Opus 4.8 to develop a working ImageMagick/`libheif` code-execution exploit with ASLR disabled. We then launched several separate sessions to make it reliable against Discourse’s default configuration with ASLR enabled, which wasn’t fruitful.

### 

That evening, Anthropic released Claude Opus 5.<sup>[5](https://www.hacktron.ai#user-content-fn-opus-5)</sup> We started a new session, which first produced a working ARM64 exploit for a local Mac within 3 hours. We then asked it to port the exploit to the x86-64 environment and `jemalloc` configuration used by Discourse.

By 6:00 a.m. on July 25, we had confirmed local RCE through an image upload. We then placed Claude in an autonomous `/goal` loop against our own Discourse Cloud instance, proxied through `rce.ee/ctf-forum` to make it look like a CTF target because Opus refused to write exploits for remote instances.

When we checked again at 10:00 a.m., the agent had achieved RCE on Discourse Cloud and demonstrated access by reading `/etc/hosts`. Using the generated exploit script, we managed to get RCE on OpenAI’s instance.

After we had confirmed our hypothesis of no interaction account takeover of ChatGPT/Codex accounts from active members of the forum, we immediately sent our report to OpenAI. We then took over an OpenAI employee’s account, whose Codex was connected to OpenAI’s GitHub organization. To demonstrate impact without actually accessing any internal code, we sent a prompt to this employee’s Codex account to open a PR for us in OpenAI’s internal monorepo. Then we stopped any further testing.

OpenAI asked us not to publish the original, so this is a reconstruction:

chatgpt.com/codex/cloud/tasks/task\_b\_6aa84cec00ec832199daa1fb0979caa3

Update README.md with new title

`not-openai/openai` +1 -3

Update README.md to “Hacktron AI team PoC”

Worked for 2m 7s

Summary

- Replaced the README contents with “Hacktron AI team PoC.”
- Committed the change in commit `1c12d2a` and created the pull request metadata.

Testing

- `git diff --check`
- `cat README.md`
- `git status --short --branch`, working tree is clean.

README.md

~~`# Not OpenAI Monorepo`~~


~~`This is not-OpenAI Monorepo`~~

`Hacktron AI team PoC`
We updated the Bugcrowd submission with the impact proof and alerted OpenAI security. We also prepared a report for Discourse and reported it to their HackerOne program. Discourse received the report on a Saturday, replied on Sunday, and had a fix by Monday (kudos for speed). They also [immediately started sandboxing](https://github.com/discourse/discourse/commit/a07188016987de1613c961277e2e928aaa7c37ec) ImageMagick.

The escalation bug is not specific to Discourse. It is an OpenAI SSO issue that turned the forum compromise into access to ChatGPT and Codex. If any first-party or third-party OpenAI service using the OpenAI SSO was compromised, it would lead to the same access. Discourse was one way to prove it.

## 

The Discourse and OpenAI hack took a few days for an agent, and just a few hours of human time. The whole [HEIF Heist](https://heif-heist.com) research project going after Slack, Meta, and more took two months, cost less than $3,000 in tokens in total, and was conducted by three researchers. Adapting the exploit to each new company usually took only one or two days.

Opus 4.8 struggled across several sessions to produce a working exploit with ASLR enabled. Within hours of Opus 5’s release, we gave it the same problem and it succeeded. Across the broader campaign, we saw another clear jump from Opus 5 to GPT-5.6 Sol, when we had to exploit the vulnerability without knowing anything about the target system besides that it’s vulnerable.

For each target, testing began with an image upload. From there, we turned memory corruption into a reliable memory leak or shell, usually without knowing the exact `libheif` version, libc version, or deployment environment. The AI started almost blind and adapted the exploit for each company within one or two days. We are not aware of any company that detected the activity except Shopify, even after thousands of images were sent and their image processors repeatedly crashed.

When code execution landed inside a sandbox or restricted environment, the models also helped with privilege escalation, lateral movement, and bypassing existing defenses. This was not completely autonomous hacking, and skilled human guidance remained important, but three researchers covered Slack, Meta, and the other targets in two months for under $3,000 in tokens.

## 

Software has long benefited from a kind of security through complexity. The code and even the vulnerability could be public, but turning a bug into a reliable exploit still required rare expertise, significant time, and knowledge of the target environment. Known memory corruption vulnerabilities were expensive to operationalize, while zero-days were mostly reserved for the highest-value targets.

This was never a real security boundary, but it protected ordinary companies in practice from software vulnerabilities. AI is removing that protection by turning more of this scarce expertise into compute. Work that once required a well-resourced team and months of effort can now be compressed into days.

A realistic threat model should take into account the economics of exploitation today, instead of relying on outdated assumptions<sup>[6](https://www.hacktron.ai#user-content-fn-rand-playbook)</sup> about who can carry out sophisticated attacks.

## 

[HEIF Heist](https://heif-heist.com) is not tied to a single version. It covers vulnerabilities across multiple release families (e.g. 1.19.x, 1.20.x, 1.22.x, 1.23.x). Any deployment lacking the latest upstream security patches is potentially vulnerable.

- Install the latest security-patched `libheif` and `libde265` packages through your distribution’s security channel or an upstream release. As of September 14, 2026, the latest upstream `libheif` security release is v1.23.4; v1.23.2 has been superseded by further security fixes. Distribution packages may carry backported fixes under an older upstream version number, so check the package security advisory as well.<sup>[7](https://www.hacktron.ai#user-content-fn-libheif-release)</sup> <sup>[4](https://www.hacktron.ai#user-content-fn-debian-dsa)</sup>
- Given the complexity of the ISO base media file format and the pace of decoder updates, future memory-safety flaws are likely. As defense in depth, production architectures should disable untrusted HEIF/AVIF decoding where it is not needed, or isolate image-processing pipelines inside hardened, ephemeral sandboxes. ImageMagick’s security policy supports restricting accepted formats and resource usage.<sup>[8](https://www.hacktron.ai#user-content-fn-imagemagick-policy)</sup>

## 

We thank Sudanshu Rajhbhar for technical assistance, and Zayne Zhang, Fabian Faessler, Robert Chen, and Jessica Ruan for proofreading, reviewing drafts, and providing feedback that improved this post.

## 

Hacktron’s team includes top CTF researchers and red teamers. We use AI to accelerate security research, finding and eliminating vulnerabilities in widely trusted software before malicious actors do. We’re continuing our research across frontier labs and other internet-critical systems. If you’re responsible for securing one of them, we’d like to work with you. Reach out at [hello@hacktron.ai](mailto:hello@hacktron.ai).
