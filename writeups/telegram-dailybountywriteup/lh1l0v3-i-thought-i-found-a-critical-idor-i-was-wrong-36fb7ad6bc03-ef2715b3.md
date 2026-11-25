# I Thought I Found a Critical IDOR. I Was Wrong.

- **Source URL:** https://medium.com/@Lh1l0v3/i-thought-i-found-a-critical-idor-i-was-wrong-36fb7ad6bc03
- **Fetched from:** https://medium.com/@Lh1l0v3/i-thought-i-found-a-critical-idor-i-was-wrong-36fb7ad6bc03?source=rss-d52919da229d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14892)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Lh1l0v3 / Mon, 31 Aug 2026 19:51:02 GMT

I have been spending more time doing vulnerability research lately, and one of the things I have started doing differently is looking at source code when I can. It gives me a different view of an application than simply sending requests through Burp and watching the responses.

A few days ago, I was reviewing the source code of a WireGuard management portal that was part of an Intigriti program. I was looking at how the application handled peer objects and, more specifically, how it decided whether a user was allowed to access another peer.

That was where I thought I had found something serious.

The application had different API versions, and when I compared the peer handling code, I noticed that the newer version was explicitly checking whether the current user was allowed to access the peer after retrieving it.

The code looked roughly like this:

peer, err := s.peers.GetPeer(ctx, id)

if err != nil {

return nil, err

}

if err := domain.ValidateUserAccessRights(ctx, peer.UserIdentifier); err != nil {

return nil, err

}

return peer, nil

That made sense. The application retrieves the peer and then checks whether the authenticated user has permission to access it.

I then looked at the older API implementation.

This was the part that caught my attention:

```
func (p PeerService) GetPeer(ctx context.Context, id domain.PeerIdentifier) (*domain.Peer, error) {
    return p.peers.GetPeer(ctx, id)
}
```
There was no ValidateUserAccessRights() in the service method.

The same pattern appeared in the method responsible for retrieving a peer’s configuration.

At first, this looked like a classic broken object-level authorization problem. The API accepted a peer identifier, passed it down to retrieve the object, but I couldn’t see an ownership check in the service layer.

I then looked at what was actually contained in the peer configuration.

That made the potential impact much more interesting.

The peer model contained the WireGuard private key. If an authenticated user could retrieve another user’s peer configuration, this would not simply be a case of viewing somebody else’s data. A WireGuard configuration contains the credentials needed for that peer to authenticate to the VPN.

So I started thinking about the attack from that perspective.

If I could get another user’s peer ID and request their configuration, could I get their private key? If I could get the private key, could I use it to connect to the VPN as that user?

There were also endpoints for modifying and deleting peers, which made the potential impact even larger if the authorization issue really existed.

I documented the code paths, explained the possible impact, and submitted the report to Intigriti as a Critical vulnerability.

Then the triager came back with a problem.

They pointed out that I had only reviewed one part of the application.

The peer service I had focused on was not the final place where the authorization decision was made. Those methods delegated the actual operation to another component, and the underlying implementation in wireguard\_peers.go contained the authorization checks.

In other words, I had looked at this:

API handler

↓

Peer service

and stopped there.

The actual flow continued:

API handler

↓

Peer service

↓

Peer manager

↓

Authorization check

That changed everything.

I went back into the repository and followed the call chain properly.

The underlying peer implementation did enforce ValidateUserAccessRights() for the relevant operations. I also traced the configuration path that I had considered vulnerable and found that it eventually reached the configuration manager, where the authorization check was also enforced.

So the conclusion I had reached from the API service layer was wrong.

The application wasn’t simply retrieving another user’s peer without checking ownership. The authorization check existed, just lower down in the call chain than where I had been looking.

At that point, I had two choices.

I could try to argue that the API service itself should have performed the authorization check, or I could accept that the security boundary was actually being enforced somewhere else.

The second option was obviously the correct one.

I replied to the triager and told them that I had followed the implementation deeper and confirmed that the authorization check was present in the actual call path. I also acknowledged that I had initially missed the separate configuration manager.

The report was closed as Not Applicable.

No bounty.

And that was completely fair.

The interesting thing about this finding is that I don’t consider the entire investigation a failure.

The initial hypothesis was reasonable. I found an apparent difference in authorization handling between two API versions, identified a sensitive object, traced how the private key reached the response model, and thought through what the impact would be if the authorization boundary could actually be bypassed.

Where I failed was in proving the final part.

I saw that the authorization check was missing from the service method and treated that as evidence that authorization was missing from the operation itself.

Those are two different things.

In source code review, especially when dealing with authorization, I think this is an easy mistake to make. You find a function that accepts an object identifier, you don’t see an ownership check, and your brain immediately connects it to IDOR.

But the question shouldn’t be whether a particular function contains an authorization check.

The question should be whether an unauthorized request can make it all the way to the sensitive operation without being stopped.

That means following the call chain until I understand where the actual security decision is made.

This was also a good reminder that comparing two versions of an application can give you useful clues, but it can also mislead you if you assume that both versions enforce security in exactly the same layer.

The newer API performed the check in the service layer. The older API delegated the operation to a component that performed the check itself.

From the outside, those implementations can look very different.

From a security perspective, however, the important question is whether the authorization boundary is actually enforced.

In this case, it was.

I originally opened the report thinking I might have found a critical vulnerability.

By the time I closed it, I had learned that I hadn’t.

I’m actually glad I followed it to the end instead of trying to defend a conclusion that the code didn’t support.

There is a temptation in vulnerability research to become attached to a finding once you have spent hours working on it, especially when the potential severity is high. But the goal isn’t to prove that every suspicious piece of code is vulnerable.

The goal is to understand what the application actually does.

Sometimes that process ends with a valid vulnerability.

Sometimes it ends with a duplicate.

Sometimes a triager can’t reproduce what you found.

And sometimes, as happened here, you go back through your own work and realise that you stopped reading one layer too early.

That is still useful research experience.

The next time I see a missing authorization check during source review, I know exactly what I will do before calling it an IDOR:

I’ll follow the call chain. *Ciao*.
