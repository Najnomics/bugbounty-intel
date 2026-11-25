# Waymore

- **Source URL:** https://medium.com/@padhyepushkar/waymore-finding-what-the-website-forgot-bbbe205ba27d
- **Fetched from:** https://medium.com/@padhyepushkar/waymore-finding-what-the-website-forgot-bbbe205ba27d?source=rss-7f768e2cc329------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14925 (id 14925)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Pushkar Padhye / Sun, 27 Sep 2026 05:22:59 GMT

*The web has a memory. Waymore knows where to look.*

There’s a funny thing about the internet: deleting something doesn’t necessarily mean it disappears.

A JavaScript file gets replaced. An endpoint gets retired. A subdomain stops being used. A page vanishes.

But somewhere, an archive may still have a copy.

That’s where **Waymore** gets interesting.

Waymore is a reconnaissance tool designed to find URLs and archived responses from sources including the Wayback Machine, Common Crawl, URLScan, VirusTotal, AlienVault OTX, Ghost Archive, and Intelligence X. Its real party trick is that it can go beyond simply finding historical URLs and retrieve archived responses that you can inspect for additional links, parameters, comments, and other clues.

Instead of asking only:

*“What exists on this website right now?”*

Waymore lets you investigate a much more interesting question:

***“What has existed here before?”***

For this article, I’m using example.com as the demonstration target. The goal is to understand how Waymore works, how to control it, and what its output actually means not to blindly collect everything the internet has ever seen.

I’m running Waymore through **Kali Linux on WSL2**.

For this particular tool, the main advantage isn’t some magical performance boost. Waymore spends a lot of its time communicating with external services, so the network is going to matter more than squeezing every last bit of performance out of the machine.

The bigger advantage for me is having a Linux-native environment for the security tooling around it.

The installation is pretty painless:

pipx install git+https://github.com/xnl-h4ck3r/waymore.git

Then:

pipx ensurepath

After reloading the shell, I checked the installation:

waymore --help

And that’s where things get interesting.

The help output is long.

Not *“I’ll just glance at it for five minutes”* long.

More like:

*“Okay, this tool has opinions.”*

The good news is that you don’t need to memorize every flag. Once you understand the core workflow, the rest starts falling into place.

Waymore has three main modes:

That’s the first distinction worth understanding. **Finding a URL and retrieving what was archived at that URL are two separate jobs.**

If I only want URL discovery:

waymore -i example.com -mode U

This focuses on finding URLs from the available sources.

That can uncover historical paths, parameters, JavaScript files, old endpoints, and other URLs that may no longer be visible from the live application.

And sometimes the URL alone is the interesting part.

If I want to retrieve archived responses:

waymore -i example.com -mode R

Now we’re moving beyond *“this URL existed”* to:

*“What was actually returned when it was archived?”*

That can give you historical HTML, JavaScript, JSON, configuration files, and other resources, depending on what was captured.

And if you want both:

waymore -i example.com -mode B

That’s where Waymore becomes particularly useful for deeper historical reconnaissance.

Interestingly, when you provide only a domain, the current Waymore documentation says the default mode is B. If you provide a specific URL/path, the default behavior changes because there is no need to discover URLs for that exact path.

So you don’t always need to specify -mode manually but I still like doing it while learning because it makes the intention obvious.

This is where archive-based reconnaissance can get a little dangerous for your own sanity.

Point a tool at a large target and ask for everything, and you may get…

A lot.

Waymore’s own documentation makes the same point: the number of URLs and potentially archived responses can become huge, and the tool is designed around **coverage rather than speed**.

Which sounds great until your terminal starts producing output faster than your brain can process it.

So instead of thinking:

*“How do I get everything?”*

I prefer:

***“What do I actually need?”***

That’s where Waymore’s controls become useful.

One of the most useful options is:

-l / --limit

In response modes, it controls how many responses are retrieved.

For example:

waymore -i example.com -mode R -l 100

The current help documents positive values as the first N responses, negative values as the last N, and 0 as all responses. The default is 5000.

That’s a useful reminder that **scope matters**.

You don’t have to start with a massive collection.

Start small. Understand the output. Then expand.

Waymore also has:

-lr / --limit-requests

This is slightly different.

-l controls the number of responses.

-lr limits requests used to obtain links from a source.

Same general idea, different part of the workflow.

And this is one of those details that becomes important once you’re using Waymore as part of a larger reconnaissance process rather than simply experimenting with it.

One option I particularly like is:

waymore -i example.com -mode R -co

The -co / --check-only option makes a few minimal requests to estimate how many requests are involved and roughly how long URL retrieval and Wayback response downloads could take. It can't estimate URLScan response-download time.

In other words:

***Ask the tool how big the job is before starting the job.***

That’s a much better habit than launching a huge collection and discovering halfway through that you’ve created your own little archaeology project.

Waymore gives you several ways to narrow the results.

Some of the useful options include:

-fc    filter response status codes

-mc match status codes

-ft filter MIME types

-mt match MIME types

The important distinction is that some options **exclude** results while others **match** specific results.

This becomes useful when you know what kind of material you’re interested in.

Maybe you’re investigating JavaScript.

Maybe you’re interested in particular response codes.

Maybe you don’t want to download thousands of images that contribute very little to the investigation.

The goal isn’t to collect less for the sake of collecting less.

It’s to spend your time on the results that can actually tell you something.

One of my favorite options is:

-ko / --keywords-only

waymore -i example.com -mode U -ko admin

You can also use a regular expression, such as:

\.js(\?.\*|$)

Waymore applies keyword filtering during the source lookup and then performs exact local regex filtering. The matching is case-insensitive.

This changes the workflow from:

*“Give me the entire history.”*

to:

***“Show me the parts of the history that match what I’m investigating.”***

That is a much more manageable way to work.

Waymore also lets you put boundaries around the timeline.

You can use:

-from

-to

to define a date range.

There’s also:

-ci / --capture-interval

which controls the capture interval used for Wayback responses.

This is useful because sometimes the question isn’t:

*“What has this domain ever had?”*

It’s:

*“What was around during this particular period?”*

That can make historical reconnaissance much more focused.

This is another reason the tool is interesting.

Waymore isn’t tied to one archive.

The current project lists sources including:

You can exclude individual sources or explicitly choose providers.

Different sources can contain different pieces of history, so having multiple sources available can increase the amount of historical context you can discover.

Of course, more sources can also mean more results.

Which brings us neatly back to the previous rule:

**Control your scope.**

Some providers require authentication, so Waymore supports configuration through its config.yml.

The current project keeps configuration under the platform’s standard configuration location; on Linux, that is typically:

\~/.config/waymore/

Recent releases also improved automatic creation of config.yml for installations such as pipx.

API credentials are about **access to provider functionality**.

They’re separate from the options that control how Waymore behaves when making requests.

-p

-r

-wrlr

-urlr

deal with processes, retries, and rate-limit waiting.

So don’t think:

*“I added an API key, therefore I can just turn everything up.”*

Your API key doesn’t magically make external services infinite.

Waymore provides controls for dealing with the reality that external services have limits.

-p      processes / basic multithreading

-r retries

-wrlr Wayback rate-limit retry

-urlr URLScan rate-limit retry

The current help output lists defaults for these settings, including two processes, one retry, a three-minute Wayback rate-limit wait, and a one-minute URLScan rate-limit wait.

The project itself also recommends being sensible with concurrency because these requests affect external services.

There is also a memory threshold:

-m / --memory-threshold

with a default of 95%, allowing Waymore to stop gracefully before memory usage becomes critical.

For my WSL2 setup, I don’t need to turn this into a performance-engineering exercise.

Start reasonably.

Watch what the tool does.

Increase the scope when you actually need to.

Waymore can save URL results with:

-oU

and archived responses with:

-oR

If you don’t specify them, it uses the configured default output directory.

There are also options for overwriting existing URL output, creating a .new file for the latest URL run, and streaming URLs to standard output.

One small detail I like is that response files can use hash-based filenames.

That allows identical responses to be deduplicated instead of filling your filesystem with five copies of the same thing wearing different names.

Because apparently even archived websites need housekeeping.

This is probably the most important distinction in the article:

**Waymore is a reconnaissance tool, not a vulnerability scanner.**

It doesn’t look at an archived response and announce:

*“Congratulations. Critical vulnerability found.”*

Instead, it helps you reconstruct a target’s historical attack surface.

A simple workflow might look like this:

Target

↓

Historical URL discovery

↓

Interesting paths / files / parameters

↓

Archived responses

↓

Manual analysis

↓

Further reconnaissance and testing

The value is in the information it uncovers.

The next step is figuring out whether any of that information matters.

When I first looked at the help output, Waymore seemed like one of those tools with approximately 47 switches for doing what sounds like one job.

But once you break it down, the workflow is fairly simple.

Ask four questions:

URLs, responses, or both?

Which providers make sense for the investigation?

Use limits, dates, filters, and request controls.

Look for URLs, files, parameters, responses, and historical behavior that can actually inform the next step.

That’s it.

The flags are just how you communicate those decisions to the tool.

A modern website is constantly changing.

Endpoints disappear.

Applications get rewritten.

JavaScript bundles are replaced.

Subdomains are retired.

Developers clean things up.

But the historical record doesn’t necessarily move at the same speed.

That’s what makes tools like Waymore interesting.

An old JavaScript file might reveal a path that isn’t linked anymore.

An archived page might expose an old application structure.

A historical response might contain clues about how the application worked at an earlier point in time.

And suddenly, something that looked like a completely ordinary website has a much longer story.

Waymore isn’t really about finding *old URLs*.

It’s about finding **context**.

A live target shows you what exists now.

Historical data can show you what existed before.

And sometimes, understanding the past makes the present much easier to understand.

That’s the part I find most interesting about reconnaissance in general.

You’re not just collecting URLs.

You’re building a timeline.

You’re looking for patterns.

You’re figuring out what changed, what disappeared, and what might still be relevant.

The internet has a habit of keeping receipts.

**Waymore is one way of reading them.**

Only run reconnaissance against systems you own or are explicitly authorized to assess.

Historical data can surface information that is no longer linked from a live application, but that doesn’t automatically make it yours to access, test, or disclose.

The interesting part of Waymore is learning how historical data can change your understanding of a target.

The responsible part is knowing where you’re allowed to look.

Good luck and happy recon.
