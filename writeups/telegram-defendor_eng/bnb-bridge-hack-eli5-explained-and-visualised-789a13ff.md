# 🚨 BNB Bridge Hack Explained

- **Source URL:** https://composable-security.com/blog/bnb-bridge-hack-eli5-explained-and-visualised
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/171 (id 171)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[Your AI Coding Agent Has a Shell. Here’s How to Sandbox It.
                
                
                    Not by default. The real question is not whether you trust the AI, but what it can reach when something goes wrong. Agentic Coding \[…\]](https://composable-security.com/blog/your-ai-coding-agent-has-a-shell-heres-how-to-sandbox-it/)
                
            
            
             
         
    

In October 2022, the BNB Bridge was [attacked for almost $600M](https://bscscan.com/tx/0x05356fd06ce56a9ec5b4eaf9c075abd740cae4c21eab1676440ab5cd2fe5c57a).

I wanted to dig deeper to understand the fundamentals of the root cause and this article is its visualized ELI5 explanation and possible fix.

## What makes this hack so special?

This hack was special for how it was handled and how the vulnerability was “fixed”. First of all, the [Binance Smart Chain was halted](https://twitter.com/BNBCHAIN/status/1578148078636650496).

Secondly, the [blacklist functionality was added to the BNB Chain](https://github.com/bnb-chain/bsc/commit/5b35b3902372dfcd9fb45fbd90683f0a1f66aa1e) implementation and the attacker’s address was hardcoded. Last, but not least the [precompiled contract used for Merkle proof verification was suspended](https://github.com/bnb-chain/bsc/blob/5b35b3902372dfcd9fb45fbd90683f0a1f66aa1e/core/vm/contracts_lightclient.go#L160) so any contract that used it was DoSed (it has been [restored 5 days later](https://github.com/bnb-chain/bsc/commit/cb131fabe5fb9570180e7030a293a984f17c2446)).

## Initial analysis

Right after the hack, many security researchers started to analyze the hack and were looking for the bug.

Sam has summarised the first analysis of the hack and prepared PoC:

Later, Dedaub pointed out the root cause and proposed a solution:

Last kudos to Emiliano who found the tx that was used by the attacker and explained why the proof was much shorter than in sam’s PoC:

That was not enough for me, so below you will find the ELI5 explanation of the bug, with a lot of diagrams because I really like them. We will start with the introduction to Merke trees, so if you are familiar with that, you can jump to the **Merke proof of multiple nodes**.

## Merkle tree introduction

Let’s start with a problem. Imagine you have some data values and allow users to prove that they own a specific one. Of course, these values must remain secret until they are revealed by their owners.

The natural approach would be to hash the values. Keep the hashes, and later ask the user for the original value that they own. Hash it, and check whether it exists in the set of hashed values.

Where would you store these hashes to protect them from manipulation? Of course, the obvious answer is to keep it on-chain. But, another problem arises here. It would be very costly to store all those values on-chain.

This is the moment where the Merkle tree comes in and solves the problem. Below is an example of a binary (meaning that each node has two sub-nodes) Merkle tree.

The green nodes are called the leaves of the tree and they are equal to the data values (or their hashes).

The white nodes are hashes from each level of the tree, e.g. the hash H1.1 is the hash of concatenated values of nodes 1 and 2; the hash H1.2 is the hash of concatenated values of nodes 3 and 4, but hash H2.1 is the second level hash and is calculated as the hash of H1.1 and H1.2 hashes.

It is important to remember that the ordering matters here, which means that the hash of nodes 1 and 2 is **not equal** to the hash of nodes 2 and 1.

The grey node R is the root hash, the hash of all hashes and is **the only value kept on-chain**.

To sum up the Merkle tree structure, it allows to keep only one hash for **any** number of data values and to prove that some specific value is one of the leaves. How, you’d ask?

## Merkle proofs

Now, that you understand the Merkle tree structure, let’s cover the process of proving that some specific value (kept in one of the leaves) is in fact part of the tree. The tree is represented only by the root hash, which means that we have to somehow start from the bottom of the tree and end up with the hash equal to the root.

See the simple example below where we want to prove that the value V1 is part of the tree.

We could get all the green leaves, hash them up, and check whether the resulting hash is equal to hash R. But, if we had all leaves (from a trusted source) we could easily check whether the value V1 is one of them, right? The case is that we do not have all the values and even if we had, that operation would be too costly.

There is a much better solution, especially from the optimization perspective. Notice that if we had a P1 value, we could calculate H1. Then, if we had P2, we could calculate H2 using H1, and in the end, we would be able to get R if we had P3.

These blue nodes — P1, P2, P3 — are called *the path* which is specific for each proven value. These three are needed for the yellow node — V1.

Optimisation side note: as you can see we do not need to calculate all hashes but just as many as the height of the tree. It means that the computational complexity of this process is logarithmic — the one you would dream to have for many different algorithms.


The above example was quite easy because all path nodes were the left sub-node of the hash nodes. Check out the below example in which we want to prove the same — the inclusion of the V1 value in the tree.

The difference between this example and the previous one is that here the path nodes (blue) are not always on the left side, e.g. P1 is hashed on the right side, P2 is on the left side and P3 is again on the right side, i.e. the H1 is hash(V1,P1), but H2 is hash(P2, H1).

It means that each path node has to know whether it should be hashed on the left or right side. One of the ways to solve it is to have two attributes in each path node, *Left* and *Right*. When the node value should be hashed on the left side, the *Left* attribute is set and the *Right* is nulled; and the opposite.

Then, when hashing, the algorithm would check whether the *Left* attribute is set and use the path node value on the left side, or the opposite — when the *Right* attribute is set, use the path node value as the right part of the data to be hashed.

A side note: This is only one of many possible ways of knowing on which side should the path node be used but this one was used in the vulnerable code and is part of the root cause.


Using the above approach, we could redraw our diagram as the following.

## Merkle proof of multiple nodes

Let’s complicate a bit more. Imagine that you want to prove the existence of multiple values (e.g. V1 and V2) in the tree, like in the example below.

Of course, we could handle two separate proofs with V1 value and its blue nodes path, and V2 value and its red nodes path. However, such an approach would not be gas optimised and we love gas optimisation.

Instead, we could calculate the whole path of only one, left-most value — V1 — to calculate and verify the root hash R, and…

…for the rest values (which would be V2 in this example), we would need only to calculate the sub-path because for each one of them, one hash will appear on the path of V1 or will be one of the intermediary hashes on the V1’s way to root hash.

In the above example we can see that P1.3 (a node from V1’s path) and H2.2 (hash of V2’s node P2.2 and hash H2.1) is the same node, and so is their value. It means that we do not need to go upper for V2 value, because we have already confirmed the correctness of P1.3 aka H2.2 node.

It is worth noting that the closer the values V are to the left-most value, the less operations are needed. Below I present another diagram as an exercise to check how long (or rather short) path is for the V2 value.

Now, if you are a security-minded person, you would probably ask: what if both *Left* and *Right* attributes were set or were null? And that is how we are getting close to the bug…

## The root cause

The BNB Bridge allows you to verify multiple values (that execute some transfers when verified, by the way) in the same way as described above.

In fact, it uses the [iavl](https://github.com/cosmos/iavl) library to handle that process. Here is the implementation of recursive [COMPUTEHASH](https://github.com/cosmos/iavl/blob/de0740903a67b624d887f9055d4c60175dcfa758/proof_range.go#L237) function which is responsible for that (*notice the comment in line 260, we will come back to that later*).

The root cause of the hack was that **the code that bridge uses for verification of Merkle proof does not take into account** that the path nodes, set by user — therefore coming from untrusted source, can have **both *Left* and *Right* attributes set**.

Let’s use a slightly modified version of the previously presented proof example.

All malicious data is red. As you can see the node P2 has been modified. It contains the legitimate value on the Left side and malicious one on the Right. The malicious right value is a hash of malicious leaf V2 that contains some unauthorized transfer.

What is important is that the ordering of leaves is V1, V2, which means that the bridge will check the root hash for V1 node which iscorrect as the V1 and path P1, P2 and P3 values are legitimate.

However, when it moves to the next leaf verification, V2, the root hash is already verified and the function only checks whether the hash or V2’s sub-path is on the right side of V1’s path.

In simple two steps, the V2’s verification process is the following:

- Take the empty path to calculate V2’s root hash which is equal to the direct hash of V2 value because there are no nodes in the path to hash its value with.
- [Check whether this hash is on the right side of the current path’s node](https://github.com/cosmos/iavl/blob/de0740903a67b624d887f9055d4c60175dcfa758/proof_range.go#L278) and it is, because the attacker just put it there.

**Basically, the root cause is that the function took the left side of the path node for the root hash verification and the right side of the path node for the verification of subsequent leaves.**

Of course, this attack is feasible only if both the proven values V1, V2 and their paths are user-controlled, but guess what — they are user-controlled.

## Fix

The general fix for that issue would be to make sure that the sides that are used for subsequent leaves verification are the same that are used for root hash verifications. In other words, if the *Left* side was used to calculate the root hash, the *Right* side **cannot** be used for subsequent leaves verification.

However, the fix was not introduced in [iavl](https://github.com/cosmos/iavl) library because, as I mentioned before, [this library assumes that the path nodes are correct and do not have both sides set](https://github.com/cosmos/iavl/blob/de0740903a67b624d887f9055d4c60175dcfa758/proof_range.go#L260).

Therefore, the BNB Chain had to introduce a fix in its node implementation. [They added a verification step does detects nodes with both sides set](https://github.com/bnb-chain/bsc/blob/cb131fabe5fb9570180e7030a293a984f17c2446/core/vm/contracts_lightclient.go#L228) and returns an error.

## Lessons learned

The main take-away from this issue is that **it is important to calculate the values consistently**. In this example, both the root hash itself and the hash calculated during subsequent leaves verification should take into account both sides of the node.

Another lesson is to **be careful when doing gas optimization** as it is an easy way to introduce a security bug.

The best way to avoid this type of issue is to regularly audit the code and use the help of security experts. If you want to verify the security of your bridge smart contract, please **[contact me](mailto:damian.rusinek@composable-security.com)** and let’s have a free security consultation.

Meet Composable Security

Get throughly tested by the creators of Smart Contract Security Verification Standard
