# XSS in Hidden Input Without User Interaction

- **Source URL:** https://medium.com/@mhmodgm54/xss-in-hidden-input-without-user-interaction-acbd530c89b6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251123030052/https://medium.com/@mhmodgm54/xss-in-hidden-input-without-user-interaction-acbd530c89b6
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9878 (id 9878)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS in Hidden Input Without User Interaction

## Introduction

In this write-up, I will explain a reflected Cross-Site Scripting (XSS) vulnerability I discovered on a target we’ll call `example.com`The interesting part of this XSS is that it occurs inside a **hidden input field** and **executes automatically**, without requiring any user interaction such as pressing keys or clicking buttons.

## Discovery Steps

I initially discovered the XSS vector while testing a parameter called `p1` in the following URL:

`https://example.com/edit?method=&service=&p1=evil`
Here, the `p1` parameter was reflected directly inside a hidden input field in the HTML response:

`<input type="hidden" name="P1" value="evil">`
At first, I attempted a basic payload that requires user interaction to trigger:

`<input type="hidden" name="P1" value="evil" accesskey="X" onclick="alert(1)" >`
This approach only works when the user presses `Alt + Shift + X`, which **lowers the impact and reliability** of the XSS, making it less practical for exploitation

## Exploiting Without User Interaction

To increase the severity and achieve execution **without user interaction**, I searched for payloads that trigger automatically. After some testing, I found a working payload that executes directly in **Chrome, Edge, and Brave**, though it does **not work in Firefox or Safari**.

Here’s the main concept behind the payload:

`oncontentvisibilityautostatechange=alert(document.cookie) style=display:block;content-visibility:auto`
To successfully inject this into the reflected value inside the `value` attribute, I enclosed the entire injection in double quotes to close the attribute properly:

`<input type="hidden" name="P1" value="evil"oncontentvisibilityautostatechange=alert(document.cookie) style=display:block;content-visibility:auto "">`
As a result, the `alert(document.cookie)` executes **immediately**, without requiring any user action. This significantly increases the impact and exploit-ability of the XSS

## Conclusion

This write-up demonstrates how XSS in a hidden input field can still be dangerous, especially when exploited with a payload that doesn’t rely on user interaction. Always test beyond basic payloads to explore edge cases and increase severity.

I hope this quick write-up was helpful to fellow researchers!

*أن رجلا جاء إلى رسول الله صلى الله عليه وسلم فقال : ( يا رسول الله ! أيُّ الناس أحبُّ إلى الله ؟ فقال : أحبُّ الناس إلى الله أنفعهم للناس…)*
