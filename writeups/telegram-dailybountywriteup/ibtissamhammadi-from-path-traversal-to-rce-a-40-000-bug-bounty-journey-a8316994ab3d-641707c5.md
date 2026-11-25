# From Path Traversal to RCE

- **Source URL:** https://medium.com/@ibtissamhammadi/from-path-traversal-to-rce-a-40-000-bug-bounty-journey-a8316994ab3d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250119062751/https://medium.com/@ibtissamhammadi/from-path-traversal-to-rce-a-40-000-bug-bounty-journey-a8316994ab3d?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8528 (id 8528)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Path Traversal to RCE: A $40,000 Bug Bounty Journey

## How a Simple File Path Led to Complete Server Control

*A collaborative hunt that turned a simple vulnerability into a major security find*

# The Beginning of Our Hunt

You know that feeling when you stumble upon something that others might have missed? That’s exactly what happened when our port scan revealed [http://admin.target.com:8443](https://web.archive.org/web/20250119062751/http://admin.target.com:8443/). Despite getting a **404 error**, something told us to dig deeper.

I always say, “Never ignore a 404 on an admin panel. It might be hiding something valuable.”

Working alongside **Orwa Atyat**, we embarked on what would become an exciting security research journey. Little did we know this would lead to a **$40,000 bounty**.

# Our First Break: The Discovery Phase

The investigation started with a simple fuzzing test at [http://admin.target.com:8443/FUZZ](https://web.archive.org/web/20250119062751/http://admin.target.com:8443/FUZZ). Here’s what we uncovered:

1. An /admin/ directory that redirected to /admin/faces/jsf/login.XHTML
2. A mysterious /admin/download/ endpoint
3. A *seemingly empty* response that would prove crucial later

**“Empty responses often hide the most interesting secrets,” my partner reminded me.**


# The Download Directory: Our Gateway

The /download/ directory was like a locked door waiting to be opened. We figured it needed:

- A valid file path
- The right parameter
- *the right touch* to reveal its secrets

It only worked in **/admin/**\*, but this proved our guess was right — we had found a path traversal bug.

# The Game-Changing Log File

Sometimes, great discoveries come from unexpected places. The **/incident-report** endpoint was a lucky find — it gave us a surprise: [**incident-report-xxxxxx.zip**](https://web.archive.org/web/20250119062751/http://incident-report-xxxxxx.zip/).

Inside those logs, we found:

- Admin credentials (MD5-hashed)
- The password: Glglgl123
- *A whole new world* of possibilities

# Breaking Through: The Groovy Console

After we logged in with the new credentials, something shocking was found — a Groovy console in export\_step2.xhtml.

**“Finding a Groovy console in a production environment is like finding keys to the kingdom.”**


The implications were massive:

- **Arbitrary Code Execution** possibilities
- Potential for *data exposure*
- **Privilege escalation** opportunities

# Solving the Output Mystery

Here’s where things got interesting. The Groovy console was working, but we couldn’t see any output. Then it hit us — what if the /incident-report endpoint could show us what we needed?

Our workflow became:

1. Log into the admin panel
2. Execute commands through the Groovy console
3. Retrieve outputs from /incident-report

# The Final Reward

Our methodical approach paid off. By reporting our findings step by step:

1. First, the admin credentials
2. Then, the [**Remote Code Execution**](https://web.archive.org/web/20250119062751/https://www.bugcrowd.com/glossary/remote-code-execution-rce/) capability

The result? A **$40,000 bounty** and a valuable lesson in persistence.

# Key Takeaways

1. **Persistence is everything** in bug hunting

- Every small discovery can lead to something bigger
- Never give up on a promising lead
- **Thoroughness matters more than speed document** everything
- Test every assumption
- Follow every thread
- **Quality over quantity** reporting builds trust
- Honest findings get better rewards
- *Detailed documentation* makes a difference

# In Conclusion

This journey with OrwaGodfather showed us that the best findings come from checking everything. A simple search can turn into something big.

In bug hunting, patience and persistence are not good traits — they are needed for success.
