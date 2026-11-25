# MatchTheRegex

- **Source URL:** https://medium.com/@affanhaxor/matchtheregex-cylab-security-academy-write-up-understanding-regular-expressions-8924d1863799
- **Fetched from:** https://medium.com/@affanhaxor/matchtheregex-cylab-security-academy-write-up-understanding-regular-expressions-8924d1863799?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14959 (id 14959)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Mon, 26 Oct 2026 05:44:00 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Category:** Web Exploitation

**Topic:** Regular Expressions (Regex), Client-Side JavaScript Analysis

**Difficulty:** Medium

Regular expressions, commonly known as regex, are used to search, validate, and match text according to a specific pattern. They are widely used in web applications for input validation, form processing, and data filtering.

In this MatchTheRegex challenge on CyLab Security Academy, the objective was to understand the expected input pattern and provide a value that satisfied the application’s matching condition.

Rather than guessing random inputs, I explored the page, inspected its behavior, and reviewed the JavaScript source code. This helped me identify the pattern and submit the correct input to retrieve the flag.

After opening the challenge, I found a simple webpage with an orange header labeled “academy” and a form titled **Valid Input**. The form contained a text field and a Submit button.

The page did not provide a detailed explanation of the expected input. This suggested that I needed to investigate how the form validated the submitted value.

I started by entering a simple value, hiii, and clicking Submit.

The application displayed an alert saying:

wrong match! Try again!

This confirmed that the application was checking the input against a specific matching condition. Since an arbitrary string did not work, I decided to inspect the page’s source code to understand how the validation was implemented.

I opened the page source and examined the JavaScript responsible for submitting the form.

The code included the following function:

```
function send_request() {
    let val = document.getElementById("name").value;
```
```
    fetch(`/flag?input=${val}`)
        .then(res => res.text())
        .then(res => {
            const res_json = JSON.parse(res);
            alert(res_json.flag);
            return false;
        });
```
return false;

}

This code retrieves the value entered in the input field and sends it to the /flag endpoint as the input parameter. The response is then parsed as JSON, and the resulting flag value is displayed in an alert.

I also noticed a comment in the source that provided a useful clue about the expected pattern:

// ^a.....y!?

This clue directed my attention toward regular expressions rather than ordinary text validation.

A regular expression defines a pattern that text must match. In this challenge, the important clue was:

^a.....y!?

The main characters to understand are:

The central part of the pattern, a.....y, therefore represents a sequence beginning with a, followed by five characters, and ending with y.

For example, the word academy has seven letters: a followed by cadem, and then y. The five dots can match the five middle letters.

This explains why the pattern a.....y is meaningful for the challenge. The dots are regex wildcards, not punctuation that must appear literally in the matched text.

After identifying the clue, I returned to the challenge page and entered:

a.....y

I then clicked Submit. This time, the application accepted the input and displayed the flag in an alert.

The key was understanding the expected regex pattern instead of repeatedly trying unrelated strings.

The flag displayed by the application was:

`academy{succ3ssfully_matchtheregex_4d5352dc}`
This challenge reinforced several useful concepts:

Although this challenge focuses on regex matching, it also demonstrates a few important development practices.

**Validate input on the server.** Client-side checks can be modified or bypassed, so security-sensitive validation must be performed by the server.

**Handle user input safely.** When sending input through a URL, developers should encode it correctly, for example by using URLSearchParams, to avoid problems with special characters.

**Avoid exposing sensitive information.** Challenge applications may intentionally return flags to successful requests, but production applications should ensure that protected data is only returned after proper authorization.

**Use regex carefully.** Complex or poorly designed regular expressions can cause performance problems. Patterns should be tested against expected inputs and designed to avoid excessive backtracking.

MatchTheRegex was a useful exercise in understanding regular expressions and analyzing client-side JavaScript. By testing an invalid input, inspecting the source code, and interpreting the regex clue, I identified the required pattern and successfully retrieved the flag.

The main takeaway is that understanding how a pattern works is often more useful than guessing values. A few characters in a regular expression can completely change how an application interprets an input.

*This write-up is intended for educational use in the CyLab Security Academy lab environment. Test only systems you own or have explicit permission to assess.*

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
