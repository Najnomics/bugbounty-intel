# How I Earned 252.60 USDC from an ENS Bug

- **Source URL:** https://medium.com/@anandvashishtha/how-i-earned-252-60-usdc-from-an-ens-bug-a31c8a253f5f
- **Fetched from:** https://medium.com/@anandvashishtha/how-i-earned-252-60-usdc-from-an-ens-bug-a31c8a253f5f?source=rss-bcf77b713b98------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14959 (id 14959)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ANAND VASHISHTHA / Sun, 25 Oct 2026 16:52:26 GMT

*While building AdReceipt for ETHOnline, I found a transfer flow that could fail after changing a name’s payment address.*

The name transfer failed. The payment address had already changed.

The ENS name still belonged to its original owner, but someone sending ETH to that name could now send it to the recipient of the unsuccessful transfer.

That was the inconsistent state I reproduced and reported in the ENS Audit Competition on Immunefi. The project confirmed it as a new Medium-severity finding. On October 9, 2026, it became a paid report.

The story started while I was building something else.

During ETHGlobal’s ETHOnline hackathon, I was working on **AdReceipt**: a project where AI agents help manage sponsored recommendations inside AI answers, with verifiable payment receipts showing who paid for each placement and how much.

We intended to use ENS in that project. While exploring the ecosystem, I came across the ENS Audit Competition and began looking for vulnerabilities alongside the hackathon work.

Working on an integration gave me a practical reason to understand what the interface promised, which permissions it relied on, and what happened when a user action failed.

The finding emerged from the transfer flow in the competition version of ENS Explorer. Understanding it requires one distinction that is easy to overlook: owning a name and receiving payments through that name are separate things.

An ENS name provides a readable identifier that can resolve to a cryptocurrency address. Instead of copying a long wallet address, a sender can enter a name and let their wallet look up the destination.

Two pieces of state matter here.

**Ownership** determines who controls the name. **The ETH address record** determines which address receives an ETH payment when someone resolves that name.

Those values can legitimately be different. Owning a name does not automatically mean every payment to it must arrive in the owner’s wallet.

The problem in my report was how Explorer changed those values during a transfer — and what happened when the process stopped halfway through.

From the user’s perspective, transferring a name looks like one task. Underneath the interface, it can involve several independent transactions. Each successful transaction changes blockchain state on its own.

That difference becomes important when a later transaction fails. An earlier success does not disappear just because the overall workflow ends with an error.

The affected flow involved a particular combination of permissions: the owner could transfer the name and edit its address records, but could not change the resolver attached to it.

A resolver is the component that provides records such as the name’s ETH payment address.

Because the owner lacked permission to detach it, Explorer hid the resolver-detachment option. But the option to update the ETH address remained selected and disabled, accompanied by this explanation:

*Not needed while the resolver is being detached.*

The generated transaction plan contained no resolver-detachment action.

That sentence was therefore giving the user a false explanation of what the application was about to do.

The underlying mistake was a mismatch between two versions of the form’s settings: options, the choices stored in the form, and effectiveOptions, the choices that could actually be carried out under the owner’s permissions.

The transaction builder used the second version. It correctly excluded an unavailable resolver-detachment action. The interface still used the first version when disabling the ETH-address option and explaining it.

In plain English, the application built its transaction plan from one understanding of the situation and explained that plan using another.

That mismatch affected whether the user could understand and control a change to the name’s payment destination.

The plan updated the name’s ETH address to the selected recipient before attempting the ownership transfer. These were separate transactions.

If the address update succeeded but the ownership transfer failed, the name remained with the original owner while its ETH address continued pointing to the selected recipient.

The recipient’s ability to accept or reject the transfer made this state security-relevant. The report showed that a recipient could cause the ownership step to fail after the address change had already taken effect.

I reproduced the result against the competition code in a local blockchain fork, including the browser flow and the resulting name resolution. All payments in this demonstration stayed inside that local test environment.

I also checked the consequence beyond the transfer error. An independent test payer resolved the ENS name normally, received the changed destination and sent a small test payment there. The recipient received it. Restoring the address record afterward corrected future resolution, but did not reverse that completed payment.

The resulting mismatch was straightforward:

That was the substance of the finding: a misleading explanation combined with a silently inconsistent result after failure.

I submitted the report on September 14, 2026 (IST). Immunefi escalated it, and the ENS project confirmed it as a valid new finding with a final severity of **Medium**.

The severity reasoning matters as much as the acceptance.

The address left in the record belonged to the recipient the owner had already selected. The application had not substituted an unrelated address without the owner’s involvement. The owner also retained the name and the ability to repair its address record.

Those constraints limited the severity. The report did not establish permanent name loss or permanent loss of control.

At the same time, selecting someone as a transfer recipient does not make every intermediate outcome obvious. A failed transfer could leave a payment destination changed, and the interface had given an incorrect explanation for that change.

The design lesson is to make related changes succeed or fail together where the permissions and architecture allow it. This is what an atomic operation provides. Otherwise, the application needs safe sequencing, a clear account of any changes that remain after failure, and a practical way to restore the previous record.

The payout arrived on October 9: **252.6023 USDC**, with **$252.52** shown as its value at payment time and no Immunefi fee deducted.

You can read the [published report #93008](https://reports.immunefi.com/ens-or-audit-competition/93008-w-a-medium-recipient-controlled-transfer-failure-leaves-ens-resolution-attacker-controlled-and?utm_source=chatgpt.com).

The engineering lesson I took from it was to examine the state left behind by a workflow, especially when only part of it succeeds. A transaction can behave correctly in isolation while the surrounding application leaves the user with a result they did not understand they were approving.

UI explanations belong in that analysis. When an interface tells someone why an option is disabled or what will happen to a payment address, that text influences a security-relevant decision. It needs to reflect the same effective settings that generate the transactions.

This paid finding also sits alongside less visible outcomes. Most of my other findings across platforms such as HackerOne, Bugcrowd and Intigriti have been duplicates. I also currently have four vulnerabilities triaged in a single HackenProof program. I’m keeping its name and technical details private.

It has also sharpened a question I want to keep asking while building and reviewing applications: **if this workflow fails here, what has already changed?**

— **Anand Vashishtha** · [anand0x on Immunefi](https://immunefi.com/profile/anand0x/?utm_source=chatgpt.com)
