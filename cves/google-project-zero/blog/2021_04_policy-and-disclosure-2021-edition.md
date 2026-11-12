# Policy and Disclosure: 2021 Edition - Project Zero

Source: https://projectzero.google/2021/04/policy-and-disclosure-2021-edition.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Tim Willis, Project Zero


At Project Zero, we spend a lot of time discussing and evaluating vulnerability disclosure policies and their consequences for users, vendors, fellow security researchers, and software security norms of the broader industry. We aim to be a vulnerability research team that benefits everyone, working across the entire ecosystem to help make 0-day hard.


We remain committed to adapting our policies and practices to best achieve our mission,  demonstrating this commitment at the beginning of last year with our [2020 Policy and Disclosure Trial](/2020/01/policy-and-disclosure-2020-edition.html).


As part of our annual year-end review, we evaluated our policy goals, solicited input from those that receive most of our reports, and adjusted our approach for 2021.

# Summary of changes for 2021


Starting today, we're changing our Disclosure Policy to refocus on reducing the time it takes for vulnerabilities to get fixed, improving the current industry benchmarks on disclosure timeframes, as well as changing when we release technical details.


The short version: Project Zero won't share technical details of a vulnerability for 30 days if a vendor patches it before the 90-day or 7-day deadline. The 30-day period is intended for user patch adoption.


The full list of changes for 2021:

| 2020 Trial ("Full 90") | 2021 Trial ("90+30") | 
| Public disclosure occurs 90 days after an initial vulnerability report, regardless of when the bug is fixed. Technical details (initial report plus any additional work) are published on Day 90. A 14-day grace period\* is allowed. Earlier disclosure with mutual agreement. | Disclosure deadline of 90 days. If an issue remains unpatched after 90 days, technical details are published immediately. If the issue is fixed within 90 days, technical details are published 30 days after the fix. A 14-day grace period\* is allowed. Earlier disclosure with mutual agreement. | 
| For vulnerabilities that were actively exploited in-the-wild against users, public disclosure occurred 7 days after the initial vulnerability report, regardless of when the bug is fixed. In-the wild vulnerabilities are not offered a grace period\* Earlier disclosure with mutual agreement. | Disclosure deadline of 7 days for issues that are being actively exploited in-the-wild against users. If an issue remains unpatched after 7 days, technical details are published immediately. If the issue is fixed within 7 days, technical details are published 30 days after the fix. Vendors can request a 3-day grace period\* for in-the-wild bugs. Earlier disclosure with mutual agreement. | 
| Technical details are immediately published when a vulnerability is patched in the grace period\*. (e.g. Patched on Day 100 in grace period, disclosure on Day 100) | If a grace period\* is granted, it uses up a portion of the 30-day patch adoption period. (e.g. Patched on Day 100 in grace period, disclosure on Day 120) | 


Elements of the 2020 trial that will carry over to 2021:

| 2020 Trial + 2021 Trial | 
| 1. Policy goals: Faster patch development Thorough patch development Improved patch adoption | 
| 2. If Project Zero discovers a variant of a previously reported Project Zero bug, technical details of the variant will be added to the existing Project Zero report (which may be already public) and the report will not receive a new deadline. | 
| 3. If a 90-day deadline is missed, technical details are made public on Day 90, unless a grace period\* is requested and confirmed prior to deadline expiry. | 
| 4. If a 7-day deadline is missed, technical details are made public on Day 7, unless a grace period\* is requested and confirmed prior to deadline expiry. | 


\* The grace period is an additional 14 days that a vendor can request if they do not expect that a reported vulnerability will be fixed within 90 days, but do expect it to be fixed within 104 days. Grace periods will not be granted for vulnerabilities that are expected to take longer than 104 days to fix.  For vulnerabilities that are being actively exploited and reported under the [7 day deadline](https://security.googleblog.com/2013/05/disclosure-timeline-for-vulnerabilities.html), the grace period is an additional 3 days that a vendor can request if they do not expect that a reported vulnerability will be fixed within 7 days, but do expect it to be fixed within 10 days.

# Rationale on changes for 2021


As we discussed in last year's "[Policy and Disclosure: 2020 Edition](/2020/01/policy-and-disclosure-2020-edition.html)", our three vulnerability disclosure policy goals are:

1. Faster patch development: shorten the time between a bug report and a fix being available for users.
2. Thorough patch development: ensure that each fix is correct and comprehensive.
3. Improved patch adoption: shorten the time between a patch being released and users installing it.


Our policy trial for 2020 aimed to balance all three of these goals, while keeping our policy consistent, simple, and fair. Vendors were given 90 days to work on the full cycle of patch development and patch adoption. The idea was if a vendor wanted more time for users to install a patch, they would prioritize shipping the fix earlier in the 90 day cycle rather than later.


In practice however, we didn't observe a significant shift in patch development timelines, and we continued to receive feedback from vendors that they were concerned about publicly releasing technical details about vulnerabilities and exploits before most users had installed the patch. In other words, the implied timeline for patch adoption wasn't clearly understood.


The goal of our 2021 policy update is to make the patch adoption timeline an explicit part of our vulnerability disclosure policy. Vendors will now have 90 days for patch development, and an additional 30 days for patch adoption.


This 90+30 policy gives vendors more time than our current policy, as jumping straight to a 60+30 policy (or similar) would likely be too abrupt and disruptive. Our preference is to choose a starting point that can be consistently met by most vendors, and then gradually lower both patch development and patch adoption timelines.


For example, based on our current data tracking vulnerability patch times, it's likely that we can move to a "84+28" model for 2022 (having deadlines evenly divisible by 7 significantly reduces the chance our deadlines fall on a weekend). Beyond that, we will keep a close eye on the data and continue to encourage innovation and investment in bug triage, patch development, testing, and update infrastructure.

# Risk and benefits


Much of the debate around vulnerability disclosure is caught up on the issue of whether rapidly releasing technical details benefits attackers or defenders more. From our time in the defensive community, we've seen firsthand how the open and timely sharing of technical details helps protect users across the Internet. But we also have listened to the concerns from others around the much more visible "opportunistic" attacks that may come from quickly releasing technical details.


We continue to believe that the benefits to the defensive community of Project Zero's publications outweigh the risks of disclosure, but we're willing to incorporate feedback into our policy in the interests of getting the best possible results for user security. Security researchers need to be able to work closely with vendors and open source projects on a range of technical, process, and policy issues -- and heated discussions about the risk and benefits of technical vulnerability details or proof-of-concept exploits has been a significant roadblock.


While the 90+30 policy will be a slight regression from the perspective of rapidly releasing technical details, we're also signaling our intent to shorten our 90-day disclosure deadline in the near future. We anticipate slowly reducing time-to-patch and speeding up patch adoption over the coming years until a steady state is reached.


Finally, we understand that this change will make it more difficult for the defensive community to quickly perform their own risk assessment, prioritize patch deployment, test patch efficacy, quickly find variants, deploy available mitigations, and develop detection signatures. We're always interested in hearing about Project Zero's publications being used for defensive purposes, and we encourage users to ask their vendors/suppliers for actionable technical details to be shared in security advisories.

# Conclusion


Moving to a "90+30" model allows us to decouple time to patch from patch adoption time, reduce the contentious debate around attacker/defender trade-offs and the sharing of technical details, while advocating to reduce the amount of time that end users are vulnerable to known attacks.


Disclosure policy is a complex topic with many trade-offs to be made, and this wasn't an easy decision to make. We are optimistic that our 2021 policy and disclosure trial lays a good foundation for the future, and has a balance of incentives that will lead to positive improvements to user security.
