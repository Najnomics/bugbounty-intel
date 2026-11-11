# tedivm-ai-rcession

- **Source URL:** https://blog.tedivm.com/rants/2026/10/the-ai-rcession-has-begun/
- **Fetched:** 2026-11-11
- **Researcher:** 0xacb
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

Over the last week we've seen a frightening number of exploits announced to the public, followed by a lot of panic and warnings of disaster. If you paid attention to some news stories you'd think society was on the brink of collapse. We aren't about to see the fall of society, but we are going through a dramatic shift; and the companies with the most tech debt are going to be hit the hardest.

What is really important to understand is that the last week is not a one off event. The industry has started calling this [Black October](<https://en.wikipedia.org/wiki/Black_October_(information_security)>) (I believe [404 Media](https://www.404media.co/php2shell-black-october-ai-is-changing-everything-about-hacking-no-one-knows-what-happens-next/) coined the term). This is fitting, as Black Tuesday was not just a single event but the start of the Great Depression. What we saw last week is the same; we aren't just seeing a crappy week in security, but an example of what the next few years are going to look like.

This isn't a depression though. If we're sticking with economic terms this is much closer to a recession, where a lot of overextended companies are going to find themselves in trouble. The rise in vulnerabilities being found is only going to continue increasing for the next few years, and it is going to push the process and practices of many companies to the brink. At the same time though companies with engineer rigor and adherence to best practices will be able to weather the storm. The AI RCEsession isn't about cash flow, this time it's about tech debt.

## The Tech Debt Reckoning

The security vulnerabilities found were discovered by AI, not created by them. The RCEs found range from 7 to 21 years old, far longer than AI has been used for coding. None of these vulnerabilities are particular novel or complex: we didn't need AI to create an entirely new class of vulnerability, it just had to do a thorough enough code review to find what was there.

| Vulnerability | Age | 
|---|---|
| PHP2Shell | 14 years | 
| GitLab | 12 years | 
| Node.js | 7 years | 
| Plex2Shell | 17 years | 
| Linux | 7 years | 
| Next.js | 7 years | 
| NGINX | 21 years | 

The reason we haven't found these vulnerabilities before is simply because we haven't focused the resources to do so. Instead of paying a security researcher to analyze the code, we pay software developers to add features (if we're paying anyone at all). Most security research isn't handled by the teams building their own software, but by a mixture of amateurs chasing bug bounties, security companies looking to boost their reputations, and the occasional penetration test ordered to meet some sort of governance requirement.

I'm not trying to downplay the power of AI. The fact that an agent can run overnight and find what would normally take a team of security experts weeks or months to find is impressive. My point is just that AI hasn't changed the software itself; it has changed how quickly and cheaply we can find these vulnerabilities. AI isn't the adversary coming to destroy us, it's the auditor pointing out our decades of neglect and lack of investment in secure systems.

This tech debt isn't just limited to the software with the vulnerability. If it were this wouldn't be an issue: an update would come out, people would install it, and the vulnerabilities would be removed. This should be a fairly straight forward process: the idea of [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration), the practice of automatically rebuilding and testing software from its various components, was invented in the 1980s and formally defined in 1992. Throw in practices like immutable infrastructure, configuration as code, infrastructure as code, and everything else that has been standard practice since about 2012 and dealing with this situation should be as simple as triggering a deployment.

Unfortunately that is not the case. Despite these best practices being known and having existed for literal decades there are a number of teams who just do not use them. For these folks their deployment times don't measure in minutes, but days and weeks. This isn't just a guess either, we can look at the [DORA DevOps Repos 2024](https://dora.dev/research/2024/dora-report/) report for real numbers.

| Change Lead Time | Percentage of Teams | 
|---|---|
| Less than a Day | 19% | 
| Between one day and one week | 22% | 
| Between one week and one month | 35% | 
| Between one and six months | 25% | 

Only 19% of teams operate on a level where they can deploy on demand, with 60% needing to take a week or longer before they can actually push out a new change. That means that when a security vulnerability comes out more than half of the teams running software have to scramble to get a patched version out. This may have worked when it only happened once or twice a year, but when you're dealing with a handful of vulnerabilities a week with AI backed adversaries that just doesn't cut it. Companies with this level of tech debt are won't be able to handle the situation we're in.

## The Correction

For decades now companies have been able to hide their tech debt, but now with AI that debt is being called in.

If you're a high performing team you likely have very little to worry about. While it's true that even high performing teams still have vulnerabilities in their code, they can use AI to find them and then feel comfortable deploying them. Even if third party code they use becomes vulnerable they have the ability to rapidly push out an update, often with a single click of a button. These teams also are more likely to have tools like Web Application Firewalls that give them more options, and as new security techniques like [dependency cooldowns](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns) are created they are nimble enough to adopt them in days instead of months.

On the other end of things there are going to be problems. If a zero day vulnerability comes out on Tuesday and your processes involve manual testing and a month long deployment cycle then your business is going to be either hacked or offline by Friday. At this point if these teams aren't dedicating serious resources to improving their processes and ability to rapidly deploy then I wouldn't bet on them surviving the next three years.

## Time for Reforms

So what do you do to set yourself up for success? Unlike many blog posts on this topic today I'm not here to sell you a product, and don't believe in a magic piece of technology that will solve this. Instead I recommend a mix of existing best practices and AI assistance.

Start at the source code.

- Every pull request made should have a full test suite that runs against it. You should always feel safe about what you are deploying.
- You should use AI to find gaps in your tests and fill them. Even at 100% code coverage there are likely configurations and use cases that aren't being tested.
- The dependencies you tested should be the ones you deploy: use a package manager and lockfile to ensure that.
- Those dependencies should be kept up to date. Use something like Dependabot or Renovate, with dependency cooldown, to open pull requests allow your tests to run so you can validate the updates are smooth.
- Utilize AI to scan your code for security, both on new pull requests and on a regular schedule to find any issues that are present.
- Finally, this entire process should end with an immutable artifact (a container or package) that you can deploy.

I can hear some teams saying: what about the servers, the infrastructure, the configuration? Well, this is 2026, so all of that should be code too. This leads to the next step: deployment.

- All of your deployments should be automated, and should push the artifacts created by your CI system.
- If a deployment fails it should rollback.
- Minimize what you expose to the general internet.
- Slap a gateway in front of your APIs so you can throw up the occasional emergency rule to prevent any zero day exploit running around

[If this sounds like basic software engineering practices you aren't wrong.](https://blog.tedivm.com/guides/2026/03/beyond-the-vibes-coding-assistants-and-agents/#wait-arent-these-just-general-best-practices) There is no magic bullet, just the basic practices that are often left aside in the rush to deliver features. AI absolutely will not save you if that AI can't build on a stable foundation.

## Stronger Foundations

This might be a RCEssion, but it's not a crash. The world is not going to end, civilization is not on the brink of collapse. The teams that are impacted the most are the ones with the most tech debt, and they'll get replaced by the ones that practice engineering rigor.

The bigger impact in the long term will be a more secure world, at least from a software perspective. The old vulnerabilities are getting fixed, the old teams are being forced to adapt or disappear, and developers are able to audit their own code on demand. Once we pay down this tech debt we'll all be better off for it.
