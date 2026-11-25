# The Shipment You Shouldn’t Be Able to Touch

- **Source URL:** https://medium.com/@ohyunwoods663/the-shipment-you-shouldnt-be-able-to-touch-525fbc4b7277
- **Fetched from:** https://medium.com/@ohyunwoods663/the-shipment-you-shouldnt-be-able-to-touch-525fbc4b7277?source=rss-7470840c773c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14970 (id 14970)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ohyunwoods / Thu, 05 Nov 2026 23:58:58 GMT

A missing authorization bug in Solidus (GHSA-m8v9–2qv9-xrpj)

I found this one while reading the Solidus API controllers. I noticed one endpoint checked permission on the first shipment it received but looked up the second one with a plain \`find\_by!\`. I tested it, it worked, and I reported it privately to the maintainers. They fixed it fast. This is the story.

To explain it, meet Sam. Sam works at the East warehouse of an online store built on Solidus. The store admin gave Sam a narrow permission: manage shipments at East only.

can :manage, Spree::Shipment, stock\_location\_id: user.stock\_locations.pluck(:id)

That is a sensible rule. Let’s see if it holds.

Sam tries to update a shipment at the West warehouse.


Sam — PUT /api/shipments/WEST-B → Solidus

Sam ← — — — — 401 Unauthorized — — Solidus

Blocked. The rule works.

Solidus has another endpoint, \`transfer\_to\_shipment\`, that moves items from one shipment to another. Sam picks a source shipment at East (allowed) and a target shipment at West (not allowed).


Sam — POST /transfer\_to\_shipment → Solidus

source: EAST-A (Sam can manage)

target: WEST-B (Sam cannot)

Sam ← — — — 202 Success — — — — — Solidus

It worked. Order A’s item is now sitting inside order B’s shipment.


Source shipment -> authorize! (checked)

Target shipment -> find\_by! (never checked)

The controller verified Sam could manage the source, then loaded the target with a plain lookup:


@desired\_shipment ||= Spree::Shipment.find\_by!(number: params\[:target\_shipment\_number\])

No authorization. No check that both shipments belong to the same order. The item also keeps its original line item, so order B ends up holding something it never ordered.

Before After

Order A: \[Shirt\] Order A: \[\]

Order B: \[Mug\] Order B: \[Mug, Shirt\] \<- no line item for Shirt

Moderate (CVSS 5.1). Someone’s shirt could ship to the wrong customer, and both orders end up with inconsistent records. But:

\- No data is exposed.

- Customers and anonymous users cannot trigger it.

- The attacker must already have \`:manage\` on the source shipment and know the target shipment number.

- Only stores with custom, conditional permissions are affected. Default Solidus roles already grant access to all shipments.

The patched versions look up the target inside the source order and authorize it:

ruby

@desired\_shipment = @original\_shipment.order.shipments.find\_by!(number: params\[:target\_shipment\_number\])

authorize! :update, @desired\_shipment


Target on another order -> 404

Target Sam can’t update -> 401

If you cannot upgrade yet, the advisory includes a small initializer you can drop in as a workaround.

Authorization bugs hide in endpoints that take two IDs. The first one gets checked because it is the obvious one. The second one slips through. When you review an endpoint, ask the same question for every ID in the request: who is allowed to touch this?

Also, test with restricted roles. Admin accounts hide this kind of bug.

Upgrade \`solidus\_api\` to 4.6.5, 4.7.3, or 4.8.1. If you only use the default permission sets, you are not affected.

Credit to the Solidus maintainers, especially jarednorman, for the quick triage and patch.

Advisory: [https://github.com/solidusio/solidus/security/advisories/GHSA-m8v9-2qv9-xrpj](https://github.com/solidusio/solidus/security/advisories/GHSA-m8v9-2qv9-xrpj)
