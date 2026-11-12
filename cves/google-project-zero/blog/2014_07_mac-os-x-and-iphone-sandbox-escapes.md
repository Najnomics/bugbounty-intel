# Mac OS X and iPhone sandbox escapes - Project Zero

Source: https://projectzero.google/2014/07/mac-os-x-and-iphone-sandbox-escapes.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Chris Evans, Finder of None Of These


As part of our [launch manifesto](/2014/07/announcing-project-zero.html), we committed to openness and transparency, including sharing full details of our research.


About a month ago, Apple released two [security](http://support.apple.com/kb/HT6296) [advisories](http://support.apple.com/kb/HT6297) which fixed some Project Zero findings. Today, we’re releasing the technical details by making some bugs public. Why now? Generally, we’ll always wait a little while after a patch is available, to give users time to apply the patch.


We won’t be writing a blog post for every set of bugs we make public. The main reason for this particular blog post is to highlight our process for making bugs public. That said, there are some interesting bug details available as of today! To highlight a few:


- [This OS X bug](https://code.google.com/p/google-security-research/issues/detail?id=18) fully demonstrates the ability to read arbitrary kernel memory from within the sandbox. As you can see, the proof of concept C code is attached for you to study.
- [This OS X bug](https://code.google.com/p/google-security-research/issues/detail?id=22) covers a very interesting validation failure leading to an integer underflow, leading in turn to the kernel trying to read a kernel structure from a non-NULL userspace address. The kernel structure involved contains a function pointer so getting in-kernel code execution at a chosen address follows trivially. An annotated analysis of the faulty assembly instructions is included.
- [This OS X bug](https://code.google.com/p/google-security-research/issues/detail?id=20) covers NULL pointer dereferences in the kernel—four in fact. It goes into detail about which circumstances result in sandbox escapes and which are “only” privilege escalations. Two of the bugs are quite neat because they call an attacker-specified offset from a good vtable base. Because this situation does not involve knowing any absolute kernel addresses, the bug could be used to both defeat kernel ASLR and then gain kernel code execution.

If you want a single URL to enumerate all of our publicly viewable bugs,

[click here](https://code.google.com/p/google-security-research/issues/list?can=1). Enjoy! And thanks for following Project Zero.
