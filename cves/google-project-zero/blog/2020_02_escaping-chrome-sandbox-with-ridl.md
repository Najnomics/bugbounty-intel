# Escaping the Chrome Sandbox with RIDL - Project Zero

Source: https://projectzero.google/2020/02/escaping-chrome-sandbox-with-ridl.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Guest blog post by Stephen Röttger

tl;dr: Vulnerabilities that leak cross process memory can be exploited to escape the Chrome sandbox. An attacker is still required to compromise the renderer prior to mounting this attack. To protect against attacks on affected CPUs make sure your microcode is up to date and disable hyper-threading (HT).


In my last guest blog post [“Trashing the Flow of Data”](/2019/05/trashing-flow-of-data.html) I described how to exploit a bug in Chrome’s JavaScript engine V8 to gain code execution in the renderer. For such an exploit to be useful, you will usually need to chain it with a second vulnerability since Chrome’s sandbox will limit your access to the OS and [site isolation](https://www.chromium.org/Home/chromium-security/site-isolation) moved cross-site renderers into separate processes to prevent you from bypassing restrictions of the web platform.


In this post, we will take a look at the sandbox and in particular at the impact of [RIDL](https://mdsattacks.com/) and similar hardware vulnerabilities when used from a compromised renderer. Chrome’s IPC mechanism Mojo is based on secrets for message routing and leaking these secrets allows us to send messages to privileged interfaces and perform actions that the renderer shouldn’t be allowed to do. We will use this to read arbitrary local files as well as execute a .bat file outside of the sandbox on Windows. At the time of writing, both Apple and Microsoft are actively working on a fix to prevent this attack in collaboration with the Chrome security team.

# Background

Here’s a simplified overview of what the Chrome process model looks like:


The renderer processes are in separate sandboxes and the access to the kernel is limited, e.g. via a seccomp filter on Linux or  [win32k lockdown](/2016/11/breaking-chain.html) on Windows. But for the renderer to do anything useful, it needs to talk to other processes to perform various actions. For example, to load an image it will need to ask the network service to fetch it on its behalf.


The default mechanism for inter process communication in Chrome is called Mojo. Under the hood it supports message/data pipes and shared memory but you would usually use one of the higher level language bindings in C++, Java or JavaScript. That is, you create an interface with methods in a custom interface definition language (IDL), Mojo generates stubs for you in your language of choice and you just implement the functionality. To see what this looks like in practice, you can check out the URLLoaderFactory in [.mojom IDL](https://cs.chromium.org/chromium/src/services/network/public/mojom/url_loader_factory.mojom?l=32&rcl=85c4d882d30b93f615011b036176cd0ce5b791df), [C++ implementation](https://cs.chromium.org/chromium/src/services/network/url_loader_factory.h?l=43&rcl=5fa80058135430d5253d4f2912a3bb11c6ecbfa9) and [usage in the renderer](https://cs.chromium.org/chromium/src/services/network/cors/cors_url_loader.cc?l=513&rcl=5fa80058135430d5253d4f2912a3bb11c6ecbfa9).


One notable feature is that Mojo allows you to forward IPC endpoints over an existing channel. This is used extensively in the Chrome codebase, i.e. whenever you see a pending\_receiver or pending\_remote parameter in a .mojom file.




Under the hood, Mojo uses a platform specific message pipe between processes, or more specifically between nodes in Mojo. Two nodes can be connected directly with each other but they don’t have to since Mojo supports message routing. One node in the network is called the broker node which has some additional responsibilities to set up node channels and perform some actions restricted by the sandbox.


The IPC endpoints themselves are called ports. In the URLLoaderFactory example above, both the client and the implementation side are identified by a port. In code, a port looks like [this](https://cs.chromium.org/chromium/src/mojo/core/ports/port.h?l=64&rcl=20c48eee7403759d676e5d3a125657aaba1a03ca):


The peer\_node\_name and peer\_port\_name above are both 128bit random integers used for addressing. If you send a message to a port, it will first forward it to the right node and the receiving node will look up the port name in a map of local ports and put the message into the right message queue.


Of course this means that if you have an info leak vulnerability in the browser process, you can leak port names and use them to inject messages into privileged IPC channels. And in fact, this is called out in the [security section](https://chromium.googlesource.com/chromium/src/+/master/mojo/core/README.md#security) of the Mojo core documentation:

“\[...\] any Node can send any Message to any Port of any other Node so long as it has knowledge of the Port and Node names. \[...\] It is therefore important not to leak Port names into Nodes that shouldn't be granted the corresponding Capability.”

A good example of a bug that can be easily exploited to leak port numbers was [crbug.com/779314](https://crbug.com/779314) by [@NedWilliamson](https://twitter.com/NedWilliamson). It was an integer overflow in the [blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) implementation which allowed you to read an arbitrary amount of heap memory in front of a blob in the browser process. The exploit would then look roughly as follows:

1. Compromise the renderer.
2. Use the blob bug to leak heap memory.
3. Search through the memory for ports (a valid state + 16 high entropy bytes).
4. Use the leaked ports to inject a message into a privileged IPC connection.

Next, we’ll look at two things. How to replace step 2. and 3. above with a CPU bug and what kind of primitives we can gain via privileged IPC connections.

# RIDL

To exploit this behavior with a hardware vulnerability I was looking for a bug that allows you to leak memory across process boundaries. RIDL from the [MDS attacks](http://mdsattacks.com/) seems like the perfect candidate since it promises exactly this: it allows you to leak data from various internal buffers on affected CPUs. For details on how it works, check out the [paper](https://mdsattacks.com/files/ridl.pdf) or the [slides](https://mdsattacks.com/slides/slides.html) since they explain it much better than I could.


There were microcode and OS updates released to address the MDS attacks. However, if you read [Intel’s deep dive](https://software.intel.com/security-software-guidance/insights/deep-dive-intel-analysis-microarchitectural-data-sampling) on the topic you will note that the mitigations clear the affected buffers when switching to a less privileged execution context. If your CPU supports hyper threading, you will still be able to leak data from the second thread running on your physical core. The [recommendation](https://software.intel.com/security-software-guidance/insights/deep-dive-intel-analysis-microarchitectural-data-sampling#SMT-mitigations) to address this is to either disable hyper threading or implement a group scheduler.


You can find [multiple](https://github.com/pietroborrello/RIDL-and-ZombieLoad) [PoCs](https://github.com/vusec/ridl/) [for](https://github.com/IAIK/ZombieLoad) [the](https://gamozolabs.github.io/metrology/2019/12/30/load-port-monitor.html#multi-architectural-load-port-data-sampling-mlpds) [MDS](https://twitter.com/dsredford/status/1191920315724713985) [vulnerabilities](https://twitter.com/Oranav/status/1191133009677869063) online, some of them already public since May 2019. The PoCs for the variants come with different properties:


- They target either loads or stores.
- Some require the secret to be flushed from the L1 cache.
- You can either control the index in the 64 byte cache line to leak from or leak a 64 bit value from a previous access.
- The speed varies a lot depending on both the variant and the exploit. The highest report I’ve seen is for Brandon Falk’s[MLPDS exploit](https://gamozolabs.github.io/metrology/2019/12/30/load-port-monitor.html#an-mlpds-exploit) with 228kB/s. For comparison, a naive exploit on my machine only reaches 25kB/s.


The one property all variants share is that they are probabilistic in what gets leaked. While the [RIDL paper](https://mdsattacks.com/files/ridl.pdf) describes some synchronization primitives to target certain values, you usually need to trigger a repeated access to the secret in order to leak it fully.


I ended up writing two exploits for Chrome using different MDS variants, one targeting a linux build on an Xeon Gold 6154 and one for Windows on a Core i7-7600U. I will describe both since they ended up posing different challenges when applying them in practice.

## Microarchitectural Fill Buffer Data Sampling (MFBDS)

My first exploit was using MFBDS which targets the line fill buffer of the CPU. The PoC is very simple:

After this, you will time the access to the probe array to see which index got cached.

You can change the 0 in the beginning to control the offset in the cache line for your leak. In addition, you want to implement a prefix or suffix filter on the leaked value as described in the [paper](https://mdsattacks.com/files/ridl.pdf) as well. Note that this only leaks values that are not in the L1 cache, so you want to have a way to evict the secret from cache in between accesses.


For my first leak target, I picked a privileged [URLLoaderFactory](https://cs.chromium.org/chromium/src/services/network/public/mojom/url_loader_factory.mojom?l=32&rcl=0296cd840a0cc3983db8e4d7c0577ee7845a1493). As mentioned above, the URLLoaderFactory is used by the renderer to fetch network resources. It will enforce the same-origin policy (actually same-site) for your renderer to make sure you can’t break restrictions of the web platform. However, the browser process is also using URLLoaderFactories for different purposes and those have additional privileges. Besides ignoring the same-origin policy, they are also allowed to upload local files. Thus, if we can leak one of their port names we can use it to upload /etc/passwd to [https://evil.website](https://evil.website/).


The next step will be to trigger a repeated access to the port name of a privileged loader. Getting the browser process to make network requests could be an option but seems to have too much overhead. I decided to target the port lookup in the node instead.

Every node has a hash map that stores all [local ports](https://cs.chromium.org/chromium/src/mojo/core/ports/node.h?l=298&rcl=3fa5edd2bbabbc33627dffd5f0d1c99f9e18d109). If we send a message to a non-existent port, the target node will [look it up](https://cs.chromium.org/chromium/src/mojo/core/ports/node.cc?l=156&rcl=3d901c43e94344919690ef36c843fa58e182ad50) in the map, see that it doesn’t exist and drop the message. If our port name lands in the same hash bucket as another port name, it will [read the full hash](https://cs.chromium.org/chromium/src/buildtools/third_party/libc%2B%2B/trunk/include/__hash_table?l=2465&rcl=78d6a7767ed57b50122a161b91f59f19c9bd0d19) of the unknown port to compare it with. This will also load the port name itself into the cache since it’s usually stored in the same cache line as the hash. MFBDS allows us to leak the whole cache line, even if a value didn’t get accessed directly.


The map starts with a bucket size of roughly 700 on a fresh Chrome instance and it grows mainly with the number of renderers. This makes the attack infeasible since we will have to brute force both the bucket index and the cache line offset (1 in 4 thanks to alignment). However, I noticed a code path that allows you to create a large amount of privileged URLLoaderFactories using service workers. If you create a service worker with [navigation preload](https://developers.google.com/web/updates/2017/02/navigation-preload) enabled, every top-level navigation would [create such a loader](https://cs.chromium.org/chromium/src/content/browser/service_worker/service_worker_fetch_dispatcher.cc?l=334&rcl=a129610c20b22dd77f65f137d88fc37dd1eb064f). By simply creating a number of iframes and stalling the requests on the server side, you can keep a few thousand loaders alive at the same time and make the brute force much easier.


The only thing missing is to evict the target value from L1 cache. Simply padding our messages with 32KB of data seems to do the trick in practice since I assume the data will get loaded into the L1 cache in the victim and evict everything else.

To summarize the full exploit:


1. Compromise the renderer.
2. Run the RIDL exploit in $NUM\_CPU-1 processes with varying cache line offsets.
3. Install a service worker with navigation preload.
4. Create lots of iframes and stall their requests.
5. Send messages to the network process with random port names.
6. If we collide on the bucket index, the process in 2. can leak the port name.

## TSX Asynchronous Abort (TAA)

In November 2019 new variants of the MDS attacks were released and as the TAA PoC seemed to be faster than my MFBDS exploit, I decided to adapt it to the Chrome exploit. In addition, VUSec released an exploit that [targets store operations](https://github.com/vusec/ridl/blob/master/pocs/taa_basic.c) which should allow us to get rid of the cache flushing requirement if we can get the secret to be written to different addresses in memory. This should happen if we can trigger the browser to send a message to a privileged port. In this scenario, the secret port name will also be prefixed by the node name and we can use the techniques from the RIDL paper to filter on it easily.


I also started looking for a better primitive and found that if I can talk to the [NetworkService](https://cs.chromium.org/chromium/src/services/network/public/mojom/network_service.mojom?l=197&rcl=d688b8ccdea936abf6d8f48ea58488c74827056b), it will allow me to create a new [NetworkContext](https://cs.chromium.org/chromium/src/services/network/public/mojom/network_context.mojom?l=807&rcl=d688b8ccdea936abf6d8f48ea58488c74827056b) and thereby choose the [file path](https://cs.chromium.org/chromium/src/services/network/public/mojom/network_context.mojom?l=233&rcl=d688b8ccdea936abf6d8f48ea58488c74827056b) of the sqlite3 database in which cookies are stored.


To find out how to trigger messages from the browser process to the NetworkService, I looked at the IPC methods in the interface to find one that looks like I might be able to influence it from a renderer. [NetworkService.OnPeerToPeerConnectionsCountChange](https://cs.chromium.org/chromium/src/services/network/public/mojom/network_service.mojom?l=318&rcl=d688b8ccdea936abf6d8f48ea58488c74827056b) caught my eye and in fact, this method gets called every time when a WebRTC connection gets updated. You just have to create a fake WebRTC connection and everytime you mark it as connected/disconnected it will trigger a new message to the NetworkService.




Once we leak the port name from a compromised renderer, we gain the primitive to write a sqlite3 database with a fully controlled path.


While this didn’t sound very useful at first, you can actually abuse it to gain code execution. I noticed that Windows batch files are a very forgiving file format. If you have garbage at the beginning of the file, it will skip over it until the next “\r\n” and execute the next command from there. In my exploit, I use it to create a cookies.bat file in the user’s autorun directory, add a cookie with “\r\n” and a command in it and it will get executed on the next login.


In the end, this exploit ended up working in 1-2 minutes on average and consistently worked in under 5 minutes on my machine. And I’m sure that this can be vastly improved since I’ve seen lots of speed ups from small changes and different techniques. For example, MLPDS seems to be even faster in practice than the variant I am using.


Exploit summary:


1. Compromise the renderer.
2. Run the RIDL exploit in $NUM\_CPU-1 processes with varying cache line offsets.
3. Create a fake WebRTC connection and alternate between connected and disconnected.
4. Leak the NetworkService port name.
5. Create a new NetworkContext with a cookie file at c:\path\to\user\autorun\cookies.bat
6. Insert the cookie “\r\ncalc.exe\r\n”.
7. Wait for the next log in.

# Summary

When I started working on this I was surprised that it’s still exploitable even though the vulnerabilities have been public for a while. If you read guidance on the topic, they will usually talk about how these vulnerabilities have been mitigated if your OS is up to date with a note that you should disable hyper threading to protect yourself fully. The focus on mitigations certainly gave me a false sense that the vulnerabilities have been addressed and I think these articles could be more clear on the impact of leaving hyper threading enabled.


That being said, I would like you to take away two things from this post. First, info leak bugs can be more than just an ASLR bypass. Even if it wasn’t for the reliance on secret port names, there would be other interesting data to leak, e.g. Chrome’s UnguessableTokens, Gmail cookies or sensitive data in other processes on the machine. If you have an idea how to find info leaks at scale, Chrome might be a good target.

Second, I ignored hardware vulnerabilities for the longest time since they are way out of my comfort zone. However, I hope that I can give you another data point on their impact with this blog post to help you make a decision if you should disable hyper-threading. There’s lots of room for exploration on what other software can be broken in similar ways and I would love to see more examples of applying hardware bugs to break software security boundaries.
