# Stored XSS in an Admin Alert Component via an Admin-Editable Store Name

- **Source URL:** https://medium.com/@zyadatef2462003/stored-xss-in-an-admin-alert-component-via-an-admin-editable-store-name-2bbc910e2fe4
- **Fetched from:** https://medium.com/feed/@zyadatef2462003
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14949)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**TL;DR:** In the admin panel of a Ruby on Rails e-commerce platform, the alert component renders its message with .html\_safe — i.e. without HTML escaping. The one code path that feeds it (the bulk store-destroy failure flash) builds that message from the **store name**, an admin-editable field, interpolated through a non-\_html I18n key (which does not escape) and joined with a raw "\<br/>". So a store whose name contains an HTML/JS payload executes in the admin's browser when a bulk store-destroy partially fails. Confirmed on a live install: \<img src=x onerror=...> was rendered verbatim into the DOM, not escaped.

### Introduction

Stored XSS is often found not in the obvious user-facing inputs, but in the quiet admin paths where a field is assumed to be “trusted” and rendered without escaping. This finding is exactly that: an admin-editable field (a store name) flows into an admin alert component that deliberately marks its message as HTML-safe, and the escaping that Rails would normally do for free is switched off along the entire path.

The result is JavaScript execution in the admin context. In a multi-admin / role-separated store, a lower-trust admin who can only edit a store name can land script in a higher-trust admin’s session.

### Background: the two halves of the bug

Output-escaping bugs in Rails almost always come down to two questions: **where is the data rendered (the sink)**, and **where does the data come from (the source)**. Here both halves line up badly.

### The sink — a component that opts out of escaping

The admin alert component renders its message like this:

\<!-- ui/alert/component.html.erb -->

\<p class="font-normal text-sm text-black leading-none">\<%= @message.html\_safe %>\</p>

Rails escapes interpolated output by default. Calling .html\_safe on the message explicitly turns that protection **off** — whatever string arrives in @message is written into the DOM as raw HTML. That is safe only if every caller guarantees the message is already sanitized. Nothing enforces that.

### The source — a message built from the store name

The one channel routed to this unescaped component is the flash\[:alert\] raised when a bulk store-destroy partially fails. The controller builds its summary like this (simplified):

\# stores\_controller#destroy

failure\_summary = failed.map { |record|

t(".error.description", name: record.name, reason: ...) # plain key, NOT \_html

}.join("\<br/>") # raw string join

Two things make the store name dangerous here:

1. The locale key is the **plain** one — description: "%{name}: %{reason}" — not a \_html key. In Rails, only \*\_html I18n keys auto-escape their interpolations; a plain key does **not** escape %{name}.
2. The pieces are joined with a raw "\<br/>" string rather than a safe join, so the whole thing stays an ordinary (unsafe) string carrying the raw name.

So an unescaped store name travels, unescaped, all the way into a component that then renders it unescaped. Everything else in the admin goes to the auto-escaping Toast component; flash\[:alert\] is the one path wired to the unescaped Alert component.

### Steps to reproduce

1. In the admin, set a store’s **Name** to: \<img src=x onerror=alert(document.cookie)>
2. Trigger a bulk store-destroy that fails for at least one store (e.g. attempt to delete the default store / a store that cannot be removed).
3. The failure alert renders, and the store name executes as HTML/JS in the admin’s browser.

### Proof of Concept and results

A script renders the **real** admin Alert component with the controller’s exact message-construction path, so the result reflects production rendering, not a mock. It (1) rebuilds the flash message the way the controller does, then (2) renders the actual component and checks whether the payload came out raw or escaped.

### Results

=== admin stored XSS via store name (rendered component) ===

\[1\] built flash message string:

"\<img src=x onerror=alert(document.cookie)>: can't be deleted"

html\_safe? false (interpolation did NOT escape the name)

contains raw payload? true

\[2\] rendered component HTML (message paragraph):

\<p class="font-normal text-sm text-black leading-none">\<img src=x onerror=alert(document.cookie)>: can't be deleted\</p>

==============================

payload rendered RAW (executable): true

payload rendered ESCAPED (safe): false

RESULT: STORED XSS CONFIRMED (store name rendered unescaped in admin)

The payload is written into the paragraph verbatim — the \<img> tag is live markup, not escaped text — which is what makes the onerror handler fire.

*(Insert the attached terminal screenshot here.)*

### Impact

JavaScript execution in the admin context. The concrete consequences:

- In a **multi-admin / role-separated deployment**, a lower-trust admin who can edit a store name can land script in a higher-trust admin’s session when the failed bulk-destroy alert renders — enabling session / CSRF-token theft and actions performed as the victim admin.
- In a **single-admin store** it is self-XSS, which is why the overall rating is Low.

Beyond this one path, the hard-coded .html\_safe is a **latent footgun**: any future flash\[:alert\] assignment that happens to carry user-influenced data becomes XSS for free, with no extra mistake required.
