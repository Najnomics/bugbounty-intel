# Horizontal Privilege Escalation via IDOR

- **Source URL:** https://scriptjacker.medium.com/horizontal-privilege-escalation-via-idor-viewing-editing-and-deleting-b10936ad4eb1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251230183925/https://scriptjacker.medium.com/horizontal-privilege-escalation-via-idor-viewing-editing-and-deleting-b10936ad4eb1?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12069 (id 12069)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Horizontal Privilege Escalation via IDOR: Viewing, Editing and Deleting

Hey Hackers, I am Parth Narula. A penetration tester, bug hunter, red teamer and overall a security researcher. I live for those moments where a bit of out-of-the-box thinking cracks open a critical vulnerability.

This is the story of how I found an IDOR vulnerability that allowed me to view, edit and delete punch tickets belonging to other companies simply by changing a number in the URL.

I was browsing the services section in SaaS Staging Environment that was in scope of the project.

The bundle page looked ordinary: a bundle name, price, number of occasions and a compact edit icon. The URL ended in a simple numeric ID like `/client/setup/services/bundle/115` which immediately made me curious.

Curiosity took over :)

I changed the ID in the address bar from `115` to `116` and hit enter `/client/setup/services/bundle/116`. The page loaded normally. It was not an error.

It was another company’s bundle. The name changed, the payout company changed. That one quick change revealed that the page was simply rendering whatever ID it received from the client without checking whether the logged in user should see it.

I was able to see that punch ticket name is 10 X massage which belong to another company. To confirm, I again changed ID in URL from `115` to `114` and yes it worked. Now, we got the IDOR fro viewing the details of other company bundle.

However is that limited to read only? Lets take the things even further.


That was already bad because it exposed business data from other tenants, but I was more interested in what actions I could take.

I clicked the edit button in About and change the price from `6600` to `66000` and Number of occurrences from `10` to `4` and click save changes.

I refreshed the victim bundle page and the change was visible there in `/client/setup/services/bundle/116`. I had just edited another company’s bundle settings by swapping a number in the request.

Next I tested deletion. The Remove action triggers a DELETE request to an API endpoint like `/extreme/api/booking-bundles/{id}`. I intercepted the delete request.

I changed the ID to a victim bundle ID and forwarded it. The server replied `HTTP/1.1 200 OK` and the response body contained `true`.

After refreshing the UI the victim bundle was gone. As now we can that the error message is shown.

I repeated these edits and deletes across multiple IDs. The pattern never changed. The API accepted any ID I supplied and performed the requested action without confirming that I was authorized to access or modify that resource.

## Lessons Learned

1. **If you can view it, try to change it:** When an application allows you to view another object by changing an ID, always test edit and delete actions as well. IDOR vulnerabilities rarely stop at read access and often extend to full modification or deletion.
2. **UI restrictions mean nothing without backend checks:** Hiding buttons or limiting actions in the interface does not enforce security. Always intercept requests and test whether the backend actually verifies ownership and permissions.
3. **Simple parameters often lead to serious impact:** Sequential IDs and predictable object references are high value targets. A single missing authorization check can turn a low effort test into a multi tenant data breach or business logic compromise.

I hope you learn something new. Follow for more amazing articles and give claps if you like this one :)

Need expert pentesting services? 

visit [https://scriptjacker.in](https://web.archive.org/web/20251230183925/https://scriptjacker.in/) or let’s collaborate on your next project! 🤝

Want to learn from my experiences? Check out my articles on [https://blogs.scriptjacker.in](https://web.archive.org/web/20251230183925/https://blogs.scriptjacker.in/)
