# The quantum state of Linux kernel garbage collection CVE-2021-0920 (Part I) - Project Zero

Source: https://projectzero.google/2022/08/the-quantum-state-of-linux-kernel.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

A deep dive into an in-the-wild Android exploit

Guest Post by Xingyu Jin, Android Security Research

This is part one of a two-part guest blog post, where first we'll look at the [root cause](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-0920.html) of the CVE-2021-0920 vulnerability. In the second post, we'll dive into the in-the-wild 0-day exploitation of the vulnerability and post-compromise modules.

# Overview of in-the-wild CVE-2021-0920 exploits

A surveillance vendor named Wintego has developed an exploit for Linux socket syscall 0-day, CVE-2021-0920, and used it in the wild since at least November 2020 based on the earliest captured sample, until the issue was fixed in November 2021.  Combined with Chrome and Samsung browser exploits, the vendor was able to remotely root Samsung devices. The fix was released with the [November 2021 Android Security Bulletin](https://source.android.com/security/bulletin/2021-11-01), and applied to Samsung devices in Samsung's December 2021 security update.


Google's Threat Analysis Group (TAG) discovered Samsung browser exploit chains being used in the wild. TAG then performed root cause analysis and discovered that this vulnerability, CVE-2021-0920, was being used to escape the sandbox and elevate privileges. CVE-2021-0920 was reported to Linux/Android anonymously. The Google Android Security Team performed the full deep-dive analysis of the exploit.


This issue was initially discovered in 2016 by a RedHat kernel developer and disclosed in a public email thread, but the Linux kernel community [did not patch](https://patchwork.ozlabs.org/project/netdev/patch/CAOssrKcfncAYsQWkfLGFgoOxAQJVT2hYVWdBA6Cw7hhO8RJ_wQ@mail.gmail.com/) the issue until it was re-reported in 2021.


Various Samsung devices were targeted, including the Samsung S10 and S20. By abusing an ephemeral race condition in Linux kernel garbage collection, the exploit code was able to obtain a use-after-free (UAF) in a kernel sk\_buff object. The in-the-wild sample could effectively circumvent CONFIG\_ARM64\_UAO, achieve arbitrary read / write primitives and bypass Samsung RKP to elevate to root. Other Android devices were also vulnerable, but we did not find any exploit samples against them.


Text extracted from captured samples dubbed the vulnerability “quantum Linux kernel garbage collection”, which appears to be a fitting title for this blogpost.

# Introduction

CVE-2021-0920 is a use-after-free (UAF) due to a race condition in the garbage collection system for SCM\_RIGHTS. SCM\_RIGHTS is a control message that allows unix-domain sockets to transmit an open file descriptor from one process to another. In other words, the sender transmits a file descriptor and the receiver then obtains a file descriptor from the sender. This passing of file descriptors adds complexity to reference-counting file structs. To account for this, the Linux kernel community designed a special garbage collection system. CVE-2021-0920 is a vulnerability within this garbage collection system. By winning a race condition during the garbage collection process, an adversary can exploit the UAF on the socket buffer, sk\_buff object. In the following sections, we’ll explain the SCM\_RIGHTS garbage collection system and the details of the vulnerability. The analysis is based on the Linux 4.14 kernel.

## What is SCM\_RIGHTS?

Linux developers can share file descriptors (fd) from one process to another using the [SCM\_RIGHTS datagram with the sendmsg syscall](https://man7.org/linux/man-pages/man7/unix.7.html). When a process passes a file descriptor to another process, SCM\_RIGHTS will add a reference to the underlying file struct. This means that the process that is sending the file descriptors can immediately close the file descriptor on their end, even if the receiving process has not yet accepted and taken ownership of the file descriptors. When the file descriptors are in the “queued” state (meaning the sender has passed the fd and then closed it, but the receiver has not yet accepted the fd and taken ownership), specialized garbage collection is needed. To track this “queued” state, this [LWN article](https://lwn.net/Articles/779472/) does a great job explaining SCM\_RIGHTS reference counting, and it's recommended reading before continuing on with this blogpost.

## Sending

As stated previously, a unix domain socket uses the syscall sendmsg to send a file descriptor to another socket. To explain the reference counting that occurs during SCM\_RIGHTS, we’ll start from the sender’s point of view. We start with the kernel function unix\_stream\_sendmsg, which implements the sendmsg syscall. To implement the SCM\_RIGHTS functionality, the kernel uses the structure scm\_fp\_list for managing all the transmitted file structures. scm\_fp\_list stores the list of file pointers to be passed.

| struct scm\_fp\_list { short count; short max; struct user\_struct \*user; struct file \*fp\[SCM\_MAX\_FD\]; }; | 


unix\_stream\_sendmsg invokes scm\_send ([af\_unix.c#L1886](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/af_unix.c#L1886)) to initialize the scm\_fp\_list structure, linked by the scm\_cookie structure on the stack.

| struct scm\_cookie { struct pid \*pid; /\* Skb credentials \*/ struct scm\_fp\_list \*fp; /\* Passed files \*/ struct scm\_creds creds; /\* Skb credentials \*/ #ifdef CONFIG\_SECURITY\_NETWORK u32 secid; /\* Passed security ID \*/ #endif }; | 


To be more specific, scm\_send → \_\_scm\_send → scm\_fp\_copy ([scm.c#L68](https://elixir.bootlin.com/linux/v4.14.277/source/net/core/scm.c#L68)) reads the file descriptors from the userspace and initializes scm\_cookie->fp which can contain SCM\_MAX\_FD file structures.

Since the Linux kernel uses the sk\_buff (also known as socket buffers or skb) object to manage all types of socket datagrams, the kernel also needs to invoke the unix\_scm\_to\_skb function to link the scm\_cookie->fp to a corresponding skb object. This occurs in unix\_attach\_fds ([scm.c#L103](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/scm.c#L103)):

| … /\* \* Need to duplicate file references for the sake of garbage \* collection. Otherwise a socket in the fps might become a \* candidate for GC while the skb is not yet queued. \*/ UNIXCB(skb).fp = scm\_fp\_dup(scm->fp); if (!UNIXCB(skb).fp) return -ENOMEM; … | 


The scm\_fp\_dup call in unix\_attach\_fds increases the reference count of the file descriptor that’s being passed so the file is still valid even after the sender closes the transmitted file descriptor later:

| struct scm\_fp\_list \*scm\_fp\_dup(struct scm\_fp\_list \*fpl) { struct scm\_fp\_list \*new\_fpl; int i; if (!fpl) return NULL; new\_fpl = kmemdup(fpl, offsetof(struct scm\_fp\_list, fp\[fpl->count\]), GFP\_KERNEL); if (new\_fpl) { for (i = 0; i \< fpl->count; i++) get\_file(fpl->fp\[i\]); new\_fpl->max = new\_fpl->count; new\_fpl->user = get\_uid(fpl->user); } return new\_fpl; } | 


Let’s examine a concrete example. Assume we have sockets A and B. The A attempts to pass itself to B. After the SCM\_RIGHTS datagram is sent, the newly allocated skb from the sender will be appended to the B’s sk\_receive\_queue which stores received datagrams:

sk\_buff carries scm\_fp\_list structure


The reference count of A is incremented to 2 and the reference count of B is still 1.

## Receiving

Now, let’s take a look at the receiver side unix\_stream\_read\_generic (we will not discuss the MSG\_PEEK flag yet, and focus on the normal [routine](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/af_unix.c#L2445)). First of all, the kernel grabs the current skb from sk\_receive\_queue using skb\_peek. Secondly, since scm\_fp\_list is attached to the skb, the kernel will call unix\_detach\_fds ([link](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/scm.c#L125)) to parse the transmitted file structures from skb and clear the skb from sk\_receive\_queue:

| /\* Mark read part of skb as used \*/ if (!(flags & MSG\_PEEK)) { UNIXCB(skb).consumed += chunk; sk\_peek\_offset\_bwd(sk, chunk); if (UNIXCB(skb).fp) unix\_detach\_fds(&scm, skb); if (unix\_skb\_len(skb)) break; skb\_unlink(skb, &sk->sk\_receive\_queue); consume\_skb(skb); if (scm.fp) break; | 


The function scm\_detach\_fds iterates over the list of passed file descriptors (scm->fp) and installs the new file descriptors accordingly for the receiver:

| for (i=0, cmfptr=(\_\_force int \_\_user \*)CMSG\_DATA(cm); i\<fdmax; i++, cmfptr++) { struct socket \*sock; int new\_fd; err = security\_file\_receive(fp\[i\]); if (err) break; err = get\_unused\_fd\_flags(MSG\_CMSG\_CLOEXEC & msg->msg\_flags ? O\_CLOEXEC : 0); if (err \< 0) break; new\_fd = err; err = put\_user(new\_fd, cmfptr); if (err) { put\_unused\_fd(new\_fd); break; } /\* Bump the usage count and install the file. \*/ sock = sock\_from\_file(fp\[i\], &err); if (sock) { sock\_update\_netprioidx(&sock->sk->sk\_cgrp\_data); sock\_update\_classid(&sock->sk->sk\_cgrp\_data); } fd\_install(new\_fd, get\_file(fp\[i\])); } … /\* \* All of the files that fit in the message have had their \* usage counts incremented, so we just free the list. \*/ \_\_scm\_destroy(scm); | 


Once the file descriptors have been installed, \_\_scm\_destroy ([link](https://elixir.bootlin.com/linux/v4.14.277/source/net/core/scm.c#L119)) cleans up the allocated scm->fp and decrements the file reference count for every transmitted file structure:

| void \_\_scm\_destroy(struct scm\_cookie \*scm) { struct scm\_fp\_list \*fpl = scm->fp; int i; if (fpl) { scm->fp = NULL; for (i=fpl->count-1; i>=0; i--) fput(fpl->fp\[i\]); free\_uid(fpl->user); kfree(fpl); } } | 

## Reference Counting and Inflight Counting

As mentioned above, when a file descriptor is passed using SCM\_RIGHTS, its reference count is immediately incremented. Once the recipient socket has accepted and installed the passed file descriptor, the reference count is then decremented. The complication comes from the “middle” of this operation: after the file descriptor has been sent, but before the receiver has accepted and installed the file descriptor.


Let’s consider the following scenario:

1. The process creates sockets A and B.
2. A sends socket A to socket B.
3. B sends socket B to socket A.
4. Close A.
5. Close B.

Scenario for reference count cycle


Both sockets are closed prior to accepting the passed file descriptors.The reference counts of A and B are both 1 and can't be further decremented because they were removed from the kernel fd table when the respective processes closed them. Therefore the kernel is unable to release the two skbs and sock structures and an unbreakable cycle is formed. The Linux kernel garbage collection system is designed to prevent memory exhaustion in this particular scenario. The inflight count was implemented to identify potential garbage. Each time the reference count is increased due to an SCM\_RIGHTS datagram being sent, the inflight count will also be incremented.


When a file descriptor is sent by SCM\_RIGHTS datagram, the Linux kernel puts its unix\_sock into a global list gc\_inflight\_list. The kernel increments unix\_tot\_inflight which counts the total number of inflight sockets. Then, the kernel increments u->inflight which tracks the inflight count for each individual file descriptor in the unix\_inflight function ([scm.c#L45](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/scm.c#L45)) invoked from unix\_attach\_fds:

| void unix\_inflight(struct user\_struct \*user, struct file \*fp) { struct sock \*s = unix\_get\_socket(fp); spin\_lock(&unix\_gc\_lock); if (s) { struct unix\_sock \*u = unix\_sk(s); if (atomic\_long\_inc\_return(&u->inflight) == 1) { BUG\_ON(!list\_empty(&u->link)); list\_add\_tail(&u->link, &gc\_inflight\_list); } else { BUG\_ON(list\_empty(&u->link)); } unix\_tot\_inflight++; } user->unix\_inflight++; spin\_unlock(&unix\_gc\_lock); } | 


Thus, here is what the sk\_buff looks like when transferring a file descriptor within sockets A and B:

The inflight count of A is incremented

When the socket file descriptor is received from the other side, the unix\_sock.inflight count will be decremented.


Let’s revisit the reference count cycle scenario before the close syscall. This cycle is breakable because any socket files can receive the transmitted file and break the reference cycle:

Breakable cycle before close A and B

After closing both of the file descriptors, the reference count equals the inflight count for each of the socket file descriptors, which is a sign of possible garbage:

Unbreakable cycle after close A and B

Now, let’s check another example. Assume we have sockets A, B and 𝛼:

1. A sends socket A to socket B.
2. B sends socket B to socket A.
3. B sends socket B to socket 𝛼.
4. 𝛼 sends socket 𝛼 to socket B.
5. Close A.
6. Close B.

Breakable cycle for A, B and 𝛼

The cycle is breakable, because we can get newly installed file descriptor B’ from the socket file descriptor 𝛼 and newly installed file descriptor A' from B’.

## Garbage Collection

A high level view of garbage collection is available from [lwn.net](https://lwn.net/Articles/779472/):


"If, instead, the two counts are equal, that file structure might be part of an unreachable cycle. To determine whether that is the case, the kernel finds the set of all in-flight Unix-domain sockets for which all references are contained in SCM\_RIGHTS datagrams (for which f\_count and inflight are equal, in other words). It then counts how many references to each of those sockets come from SCM\_RIGHTS datagrams attached to sockets in this set. Any socket that has references coming from outside the set is reachable and can be removed from the set. If it is reachable, and if there are any SCM\_RIGHTS datagrams waiting to be consumed attached to it, the files contained within that datagram are also reachable and can be removed from the set.


At the end of an iterative process, the kernel may find itself with a set of in-flight Unix-domain sockets that are only referenced by unconsumed (and unconsumable) SCM\_RIGHTS datagrams; at this point, it has a cycle of file structures holding the only references to each other. Removing those datagrams from the queue, releasing the references they hold, and discarding them will break the cycle."


To be more specific, the SCM\_RIGHTS garbage collection system was developed in order to handle the unbreakable reference cycles. To identify which file descriptors are a part of unbreakable cycles:

1. Add any unix\_sock objects whose reference count equals its inflight count to the gc\_candidates list.
2. Determine if the socket is referenced by any sockets outside of the gc\_candidates list. If it is then it is reachable, remove it and any sockets it references from the gc\_candidates list. Repeat until no more reachable sockets are found.
3. After this iterative process, only sockets who are solely referenced by other sockets within the gc\_candidates list are left.


Let’s take a closer look at how this garbage collection process works. First, the kernel finds all the unix\_sock objects whose reference counts equals their inflight count and puts them into the gc\_candidates list ([garbage.c#L242)](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/garbage.c#L242):

| list\_for\_each\_entry\_safe(u, next, &gc\_inflight\_list, link) { long total\_refs; long inflight\_refs; total\_refs = file\_count(u->sk.sk\_socket->file); inflight\_refs = atomic\_long\_read(&u->inflight); BUG\_ON(inflight\_refs \< 1); BUG\_ON(total\_refs \< inflight\_refs); if (total\_refs == inflight\_refs) { list\_move\_tail(&u->link, &gc\_candidates); \_\_set\_bit(UNIX\_GC\_CANDIDATE, &u->gc\_flags); \_\_set\_bit(UNIX\_GC\_MAYBE\_CYCLE, &u->gc\_flags); } } | 


Next, the kernel removes any sockets that are referenced by other sockets outside of the current gc\_candidates list. To do this, the kernel invokes scan\_children ([garbage.c#138](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/garbage.c#L138)) along with the function pointer dec\_inflight to iterate through each candidate’s sk->receive\_queue. It decreases the inflight count for each of the passed file descriptors that are themselves candidates for garbage collection ([garbage.c#L261](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/garbage.c#L261)):

| /\* Now remove all internal in-flight reference to children of \* the candidates. \*/ list\_for\_each\_entry(u, &gc\_candidates, link) scan\_children(&u->sk, dec\_inflight, NULL); | 


After iterating through all the candidates, if a gc candidate still has a positive inflight count it means that it is referenced by objects outside of the gc\_candidates list and therefore is reachable. These candidates should not be included in the gc\_candidates list so the related inflight counts need to be restored.


To do this, the kernel will put the candidate to not\_cycle\_list instead and iterates through its receiver queue of each transmitted file in the gc\_candidates list ([garbage.c#L281](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/garbage.c#L281)) and increments the inflight count back. The entire process is done recursively, in order for the garbage collection to avoid purging reachable sockets:

| /\* Restore the references for children of all candidates, \* which have remaining references. Do this recursively, so \* only those remain, which form cyclic references. \* \* Use a "cursor" link, to make the list traversal safe, even \* though elements might be moved about. \*/ list\_add(&cursor, &gc\_candidates); while (cursor.next != &gc\_candidates) { u = list\_entry(cursor.next, struct unix\_sock, link); /\* Move cursor to after the current position. \*/ list\_move(&cursor, &u->link); if (atomic\_long\_read(&u->inflight) > 0) { list\_move\_tail(&u->link, ¬\_cycle\_list); \_\_clear\_bit(UNIX\_GC\_MAYBE\_CYCLE, &u->gc\_flags); scan\_children(&u->sk, inc\_inflight\_move\_tail, NULL); } } list\_del(&cursor); | 


Now gc\_candidates contains only “garbage”. The kernel restores original inflight counts from gc\_candidates, moves candidates from not\_cycle\_list back to gc\_inflight\_list and invokes \_\_skb\_queue\_purge for cleaning up garbage ([garbage.c#L306](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/garbage.c#L306)).

| /\* Now gc\_candidates contains only garbage. Restore original \* inflight counters for these as well, and remove the skbuffs \* which are creating the cycle(s). \*/ skb\_queue\_head\_init(&hitlist); list\_for\_each\_entry(u, &gc\_candidates, link) scan\_children(&u->sk, inc\_inflight, &hitlist); /\* not\_cycle\_list contains those sockets which do not make up a \* cycle. Restore these to the inflight list. \*/ while (!list\_empty(¬\_cycle\_list)) { u = list\_entry(not\_cycle\_list.next, struct unix\_sock, link); \_\_clear\_bit(UNIX\_GC\_CANDIDATE, &u->gc\_flags); list\_move\_tail(&u->link, &gc\_inflight\_list); } spin\_unlock(&unix\_gc\_lock); /\* Here we are. Hitlist is filled. Die. \*/ \_\_skb\_queue\_purge(&hitlist); spin\_lock(&unix\_gc\_lock); | 


\_\_skb\_queue\_purge clears every skb from the receiver queue:

| /\*\* \* \_\_skb\_queue\_purge - empty a list \* @list: list to empty \* \* Delete all buffers on an &sk\_buff list. Each buffer is removed from \* the list and one reference dropped. This function does not take the \* list lock and the caller must hold the relevant locks to use it. \*/ void skb\_queue\_purge(struct sk\_buff\_head \*list); static inline void \_\_skb\_queue\_purge(struct sk\_buff\_head \*list) { struct sk\_buff \*skb; while ((skb = \_\_skb\_dequeue(list)) != NULL) kfree\_skb(skb); } | 


There are two ways to trigger the garbage collection process:

1. wait\_for\_unix\_gc is invoked at the beginning of the sendmsg function if there are more than 16,000 inflight sockets
2. When a socket file is released by the kernel (i.e., a file descriptor is closed), the kernel will directly invoke unix\_gc.


Note that unix\_gc is not preemptive. If garbage collection is already in process, the kernel will not perform another unix\_gc invocation.


Now, let’s check this example (a breakable cycle) with a pair of sockets f00 and f01, and a single socket 𝛼:

1. Socket f 00 sends socket f 00 to socket f 01.
2. Socket f 01 sends socket f 01 to socket 𝛼.
3. Close f 00.
4. Close f 01.


Before starting the garbage collection process, the status of socket file descriptors are:

- f 00: ref = 1, inflight = 1
- f 01: ref = 1, inflight = 1
- 𝛼: ref = 1, inflight = 0

Breakable cycle by f 00, f 01 and 𝛼


During the garbage collection process, f 00 and f 01 are considered garbage candidates. The inflight count of f 00 is dropped to zero, but the count of f 01 is still 1 because 𝛼 is not a candidate. Thus, the kernel will restore the inflight count from f 01’s receive queue. As a result, f 00 and f 01 are not treated as garbage anymore.

# CVE-2021-0920 Root Cause Analysis

When a user receives SCM\_RIGHTS message from recvmsg without the MSG\_PEEK flag, the kernel will wait until the garbage collection process finishes if it is in progress. However, if the MSG\_PEEK flag is on, the kernel will increment the reference count of the transmitted file structures without synchronizing with any ongoing garbage collection process. This may lead to inconsistency of the internal garbage collection state, making the garbage collector mark a non-garbage sock object as garbage to purge.

## recvmsg without MSG\_PEEK flag

The kernel function unix\_stream\_read\_generic ([af\_unix.c#L2290](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/af_unix.c#L2290)) parses the SCM\_RIGHTS message and manages the file inflight count when the MSG\_PEEK flag is NOT set. Then, the function unix\_stream\_read\_generic calls unix\_detach\_fds to decrement the inflight count. Then, unix\_detach\_fds clears the list of passed file descriptors (scm\_fp\_list) from the skb:

| static void unix\_detach\_fds(struct scm\_cookie \*scm, struct sk\_buff \*skb) { int i; scm->fp = UNIXCB(skb).fp; UNIXCB(skb).fp = NULL; for (i = scm->fp->count-1; i >= 0; i--) unix\_notinflight(scm->fp->user, scm->fp->fp\[i\]); } | 


The unix\_notinflight from unix\_detach\_fds will reverse the effect of unix\_inflight by decrementing the inflight count:

| void unix\_notinflight(struct user\_struct \*user, struct file \*fp) { struct sock \*s = unix\_get\_socket(fp); spin\_lock(&unix\_gc\_lock); if (s) { struct unix\_sock \*u = unix\_sk(s); BUG\_ON(!atomic\_long\_read(&u->inflight)); BUG\_ON(list\_empty(&u->link)); if (atomic\_long\_dec\_and\_test(&u->inflight)) list\_del\_init(&u->link); unix\_tot\_inflight--; } user->unix\_inflight--; spin\_unlock(&unix\_gc\_lock); } | 


Later skb\_unlink and consume\_skb are invoked from unix\_stream\_read\_generic ([af\_unix.c#2451](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/af_unix.c#L2451)) to destroy the current skb. Following the call chain kfree(skb)->\_\_kfree\_skb, the kernel will invoke the function pointer skb->destructor ([code](https://elixir.bootlin.com/linux/v4.14.277/source/net/unix/af_unix.c#L1605)) which redirects to unix\_destruct\_scm:

| static void unix\_destruct\_scm(struct sk\_buff \*skb) { struct scm\_cookie scm; memset(&scm, 0, sizeof(scm)); scm.pid = UNIXCB(skb).pid; if (UNIXCB(skb).fp) unix\_detach\_fds(&scm, skb); /\* Alas, it calls VFS \*/ /\* So fscking what? fput() had been SMP-safe since the last Summer \*/ scm\_destroy(&scm); sock\_wfree(skb); } | 


In fact, the unix\_detach\_fds will not be invoked again here from unix\_destruct\_scm because UNIXCB(skb).fp is already cleared by unix\_detach\_fds. Finally, fd\_install(new\_fd, get\_file(fp\[i\])) from scm\_detach\_fds is invoked for installing a new file descriptor.

## recvmsg with MSG\_PEEK flag

The recvmsg process is different if the MSG\_PEEK flag is set. The MSG\_PEEK flag is used during receive to “peek” at the message, but the data is treated as unread. unix\_stream\_read\_generic will invoke scm\_fp\_dup instead of unix\_detach\_fds. This increases the reference count of the inflight file ([af\_unix.c#2149](https://android.googlesource.com/kernel/goldfish/+/eee65a1282369eedfcbb664d0c865a0ef3eb7017/net/unix/af_unix.c#2149)):

| /\* It is questionable, see note in unix\_dgram\_recvmsg. \*/ if (UNIXCB(skb).fp) scm.fp = scm\_fp\_dup(UNIXCB(skb).fp); sk\_peek\_offset\_fwd(sk, chunk); if (UNIXCB(skb).fp) break; | 


Because the data should be treated as unread, the skb is not unlinked and consumed when the MSG\_PEEK flag is set. However, the receiver will still get a new file descriptor for the inflight socket.

## recvmsg Examples

Let’s see a concrete example. Assume there are the following socket pairs:

- f 00, f 01
- f 10, f 11


Now, the program does the following operations:

- f 00 → \[f 00\] → f 01 (means f 00 sends \[f 00\] to f 01)
- f 10 → \[f 00\] → f 11
- Close(f 00)

Breakable cycle by f 00, f 01, f 10 and f 11


Here is the status:

- inflight(f 00) = 2, ref(f 00) = 2
- inflight(f 01) = 0, ref(f 01) = 1
- inflight(f 10) = 0, ref(f 10) = 1
- inflight(f 11) = 0, ref(f 11) = 1


If the garbage collection process happens now, before any recvmsg calls, the kernel will choose f 00 as the garbage candidate. However, f 00 will not have the inflight count altered and the kernel will not purge any garbage.


If f 01 then calls recvmsg with MSG\_PEEK flag, the receive queue doesn’t change and the inflight counts are not decremented. f 01 gets a new file descriptor f 00' which increments the reference count on f 00:

MSG\_PEEK increment the reference count of f 00 while the receive queue is not cleared


Status:

- inflight(f 00) = 2, ref(f 00) = 3
- inflight(f 01) = 0, ref(f 01) = 1
- inflight(f 10) = 0, ref(f 10) = 1
- inflight(f 11) = 0, ref(f 11) = 1


Then, f 01 calls recvmsg without MSG\_PEEK flag, f 01’s receive queue is removed. f 01 also fetches a new file descriptor f 00'':

The receive queue of f 01 is cleared and f 01'' is obtained from f 01


Status:

- inflight(f 00) = 1, ref(f 00) = 3
- inflight(f 01) = 0, ref(f 01) = 1
- inflight(f 10) = 0, ref(f 10) = 1
- inflight(f 11) = 0, ref(f 11) = 1

## UAF Scenario

From a very high level perspective, the internal state of Linux garbage collection can be non-deterministic because MSG\_PEEK is not synchronized with the garbage collector. There is a race condition where the garbage collector can treat an inflight socket as a garbage candidate while the file reference is incremented at the same time during the MSG\_PEEK receive. As a consequence, the garbage collector may purge the candidate, freeing the socket buffer, while a receiver may install the file descriptor, leading to a UAF on the skb object.


Let’s see how the captured 0-day sample triggers the bug step by step (simplified version, in reality you may need more threads working together, but it should demonstrate the core idea). First of all, the sample allocates the following socket pairs and single socket 𝛼:

- f 00, f 01
- f 10, f 11
- f 20, f 21
- f 30, f 31
- sock 𝛼 (actually there might be even thousands of 𝛼 for protracting the garbage collection process in order to evade a BUG\_ON check which will be introduced later).


Now, the program does the below operations:


Close the following file descriptors prior to any recvmsg calls:

- Close(f 00)
- Close(f 01)
- Close(f 11)
- Close(f 10)
- Close(f 30)
- Close(f 31)
- Close(𝛼)


Here is the status:

- inflight(f 00) = N + 1, ref(f 00) = N + 1
- inflight(f 01) = 2, ref(f 01) = 2
- inflight(f 10) = 3, ref(f 10) = 3
- inflight(f 11) = 1, ref(f 11) = 1
- inflight(f 20) = 0, ref(f 20) = 1
- inflight(f 21) = 0, ref(f 21) = 1
- inflight(f 31) = 1, ref(f 31) = 1
- inflight(𝛼) = 1, ref(𝛼) = 1


If the garbage collection process happens now, the kernel will do the following scrutiny:

- List f 00, f 01, f 10, f 11, f 31, 𝛼 as garbage candidates. Decrease inflight count for the candidate children in each receive queue.
- Since f 21 is not considered a candidate, f 11’s inflight count is still above zero.
- Recursively restore the inflight count.
- Nothing is considered garbage.


A potential skb UAF by race condition can be triggered by:

1. Call recvmsg with MSG\_PEEK flag from f 21 to get f 11’.
2. Call recvmsg with MSG\_PEEK flag from f 11 to get f 10’.
3. Concurrently do the following operations:

1. Call recvmsg without MSG\_PEEK flag from f 11 to get f 10’’.
2. Call recvmsg with MSG\_PEEK flag from f 10’


How is it possible? Let’s see a case where the race condition is not hit so there is no UAF:

| Thread 0 | Thread 1 | Thread 2 | 
| Call unix\_gc |  |  | 
| Stage0: List f 00, f 01, f 10, f 11, f 31, 𝛼 as garbage candidates. |  |  | 
|  | Call recvmsg with MSG\_PEEK flag from f 21 to get f 11’ |  | 
|  | Increase reference count: scm.fp = scm\_fp\_dup(UNIXCB(skb).fp); |  | 
| Stage0: decrease inflight count from the child of every garbage candidate |  |  | 
| Status after stage 0: inflight(f 00) = 0 inflight(f 01) = 0 inflight(f 10) = 0 inflight(f 11) = 1 inflight(f 31) = 0 inflight(𝛼) = 0 |  |  | 
| Stage1: Recursively restore inflight count if a candidate still has inflight count. |  |  | 
| Stage1: All inflight counts have been restored. |  |  | 
| Stage2: No garbage, return. |  |  | 
|  | Call recvmsg with MSG\_PEEK flag from f 11 to get f 10’ |  | 
|  |  | Call recvmsg without MSG\_PEEK flag from f 11 to get f 10’’ | 
|  | Call recvmsg with MSG\_PEEK flag from f 10’ |  | 
| Everyone is happy | Everyone is happy | Everyone is happy | 


However, if the second recvmsg occurs just after stage 1 of the garbage collection process, the UAF is triggered:

| Thread 0 | Thread 1 | Thread 2 | 
| Call unix\_gc |  |  | 
| Stage0: List f 00, f 01, f 10, f 11, f 31, 𝛼 as garbage candidates. |  |  | 
|  | Call recvmsg with MSG\_PEEK flag from f 21 to get f 11’ |  | 
|  | Increase reference count: scm.fp = scm\_fp\_dup(UNIXCB(skb).fp); |  | 
| Stage0: decrease inflight count from the child of every garbage candidates |  |  | 
| Status after stage 0: inflight(f 00) = 0 inflight(f 01) = 0 inflight(f 10) = 0 inflight(f 11) = 1 inflight(f 31) = 0 inflight(𝛼) = 0 |  |  | 
| Stage1: Start restoring inflight count. |  |  | 
|  | Call recvmsg with MSG\_PEEK flag from f 11 to get f 10’ |  | 
|  |  | Call recvmsg without MSG\_PEEK flag from f 11 to get f 10’’ | 
|  |  | unix\_detach\_fds: UNIXCB(skb).fp = NULL | 
|  |  | Blocked by spin\_lock(&unix\_gc\_lock) | 
| Stage1: scan\_inflight cannot find candidate children from f 11. Thus, the inflight count accidentally remains the same. |  |  | 
| Stage2: f 00, f 01, f 10, f 31, 𝛼 are garbage. |  |  | 
| Stage2: start purging garbage. |  |  | 
|  | Start calling recvmsg with MSG\_PEEK flag from f 10’, which would expect to receive f 00' |  | 
|  | Get skb = skb\_peek(&sk->sk\_receive\_queue), skb is going to be freed by thread 0. |  | 
| Stage2: for, calls \_\_skb\_unlink and kfree\_skb later. |  |  | 
|  | state->recv\_actor(skb, skip, chunk, state) UAF |  | 
| GC finished. |  |  | 
|  |  | Start garbage collection. | 
|  |  | Get f 10’’ | 


Therefore, the race condition causes a UAF of the skb object. At first glance, we should blame the second recvmsg syscall because it clears skb.fp, the passed file list. However, if the first recvmsg syscall doesn’t set the MSG\_PEEK flag, the UAF can be avoided because unix\_notinflight is serialized with the garbage collection. In other words, the kernel makes sure the garbage collection is either not processed or finished before decrementing the inflight count and removing the skb. After unix\_notinflight, the receiver obtains f11' and inflight sockets don't form an unbreakable cycle.


Since MSG\_PEEK is not serialized with the garbage collection, when recvmsg is called with MSG\_PEEK set, the kernel still considers f 11 as a garbage candidate. For this reason, the following next recvmsg will eventually trigger the bug due to the inconsistent state of the garbage collection process.


# Patch Analysis

## CVE-2021-0920 was found in 2016

The vulnerability was [initially reported to the Linux kernel community in 2016](https://patchwork.ozlabs.org/project/netdev/patch/CAOssrKcfncAYsQWkfLGFgoOxAQJVT2hYVWdBA6Cw7hhO8RJ_wQ@mail.gmail.com/). The researcher also provided the correct patch advice but it was not accepted by the Linux kernel community:

Patch was not applied in 2016


In theory, anyone who saw this patch might come up with an exploit against the faulty garbage collector.

## Patch in 2021

Let’s check the official [patch](https://lore.kernel.org/lkml/20210802134333.066918619@linuxfoundation.org/) for CVE-2021-0920. For the MSG\_PEEK branch, it requests the garbage collection lock unix\_gc\_lock before performing sensitive actions and immediately releases it afterwards:

| … + spin\_lock(&unix\_gc\_lock); + spin\_unlock(&unix\_gc\_lock); … | 


The patch is confusing - it’s rare to see such lock usage in software development. Regardless, the MSG\_PEEK flag now waits for the completion of the garbage collector, so the UAF issue is resolved.

## BUG\_ON Added in 2017

Andrey Ulanov from Google in 2017 found another issue in unix\_gc and provided a fix [commit](https://lore.kernel.org/lkml/20170315031642.19576-1-andreyu@google.com/). Additionally, the patch added a BUG\_ON for the inflight count:

| void unix\_notinflight(struct user\_struct \*user, struct file \*fp) if (s) { struct unix\_sock \*u = unix\_sk(s); + BUG\_ON(!atomic\_long\_read(&u->inflight)); BUG\_ON(list\_empty(&u->link)); if (atomic\_long\_dec\_and\_test(&u->inflight)) | 


At first glance, it seems that the BUG\_ON can prevent CVE-2021-0920 from being exploitable. However, if the exploit code can delay garbage collection by crafting a large amount of fake garbage, it can waive the BUG\_ON check by heap spray.

## New Garbage Collection Discovered in 2021

CVE-2021-4083 deserves an honorable mention: when I discussed CVE-2021-0920 with Jann Horn and Ben Hawkes, Jann found another [issue](https://bugs.chromium.org/p/project-zero/issues/detail?id=2247) in the garbage collection, described in the Project Zero blog post [Racing against the clock -- hitting a tiny kernel race window](/2022/03/racing-against-clock-hitting-tiny.html).

# Part I Conclusion

To recap, we have discussed the kernel internals of SCM\_RIGHTS and the designs and implementations of the Linux kernel garbage collector. Besides, we have analyzed the behavior of MSG\_PEEK flag with the recvmsg syscall and how it leads to a kernel UAF by a subtle and arcane race condition.


The bug was spotted in 2016 publicly, but unfortunately the Linux kernel community did not accept the patch at that time. Any threat actors who saw the public email thread may have a chance to develop an LPE exploit against the Linux kernel.


In part two, we'll look at how the vulnerability was exploited and the functionalities of the post compromise modules.
