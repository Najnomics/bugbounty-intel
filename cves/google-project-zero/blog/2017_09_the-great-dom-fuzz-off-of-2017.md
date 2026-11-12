# The Great DOM Fuzz-off of 2017 - Project Zero

Source: https://projectzero.google/2017/09/the-great-dom-fuzz-off-of-2017.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ivan Fratric, Project Zero

## Introduction

Historically, DOM engines have been one of the largest sources of web browser bugs. And while in the recent years the popularity of those kinds of bugs in targeted attacks has somewhat fallen in favor of Flash (which allows for cross-browser exploits) and JavaScript engine bugs (which often result in very powerful exploitation primitives), they are far from gone. For example, [CVE-2016-9079](https://bugzilla.mozilla.org/show_bug.cgi?id=1321066) (a bug that was used in November 2016 against Tor Browser users) was a bug in Firefox’s DOM implementation, specifically the part that handles SVG elements in a web page. It is also a rare case that a vendor will publish a security update that doesn’t contain fixes for at least several DOM engine bugs.

An interesting property of many of those bugs is that they are more or less easy to find by fuzzing. This is why a lot of security researchers as well as browser vendors who care about security invest into building DOM fuzzers and associated infrastructure.

As a result, after joining Project Zero, one of my first projects was to test the current state of resilience of major web browsers against DOM fuzzing.

## The fuzzer

For this project I wanted to write a new fuzzer which takes some of the ideas from my previous DOM fuzzing projects, but also improves on them and implements new features. Starting from scratch also allowed me to end up with cleaner code that I’m open-sourcing together with this blog post. The goal was not to create anything groundbreaking - as already noted by security researchers, many DOM fuzzers have begun to look like each other over time. Instead the goal was to create a fuzzer that has decent initial coverage, is easily understandable and extendible and can be reused by myself as well as other researchers for fuzzing other targets besides just DOM fuzzing.

We named this new fuzzer Domato (credits to Tavis for suggesting the name). Like most DOM fuzzers, Domato is generative, meaning that the fuzzer generates a sample from scratch given a set of grammars that describes HTML/CSS structure as well as various JavaScript objects, properties and functions.

The fuzzer consists of several parts:

- The base engine that can generate a sample given an input grammar. This part is intentionally fairly generic and can be applied to other problems besides just DOM fuzzing.
- The main script that parses the arguments and uses the base engine to create samples. Most logic that is DOM specific is captured in this part.
- A set of grammars for generating HTML, CSS and JavaScript code.

One of the most difficult aspects in the generation-based fuzzing is creating a grammar or another structure that describes the samples that are going to be created. In the past I experimented with manually created grammars as well as grammars extracted automatically from web browser code. Each of these approaches has advantages and drawbacks, so for this fuzzer I decided to use a hybrid approach:

1. I initially extracted DOM API declarations from .idl files in Google Chrome Source. Similarly, I parsed Chrome’s layout tests to extract common (and not so common) names and values of various HTML and CSS properties.
2. Afterwards, this automatically extracted data was heavily manually edited to make the generated samples more likely to trigger interesting behavior. One example of this are functions and properties that take strings as input: Just because a DOM property takes a string as an input does not mean that any string would have a meaning in the context of that property.

Otherwise, Domato supports features that you’d expect from a DOM fuzzer such as:

- Generating multiple JavaScript functions that can be used as targets for various DOM callbacks and event handlers

- Implicit (through grammar definitions) support for “interesting” APIs (e.g. the Range API) that have historically been prone to bugs.

Instead of going into much technical details here, the reader is referred to the fuzzer code and documentation at [https://github.com/google/domato](https://github.com/google/domato). It is my hope that by open-sourcing the fuzzer I would invite community contributions that would cover the areas I might have missed in the fuzzer or grammar creation.

## Setup

We tested 5 browsers with the highest market share: Google Chrome, Mozilla Firefox, Internet Explorer, Microsoft Edge and Apple Safari. We gave each browser approximately 100.000.000 iterations with the fuzzer and recorded the crashes. (If we fuzzed some browsers for longer than 100.000.000 iterations, only the bugs found within this number of iterations were counted in the results.) Running this number of iterations would take too long on a single machine and thus requires fuzzing at scale, but it is still well within the pay range of a determined attacker. For reference, it can be done for about $1k on [Google Compute Engine](https://cloud.google.com/compute/) given the smallest possible VM size, preemptable VMs (which I think work well for fuzzing jobs as they don’t need to be up all the time) and 10 seconds per run.

Here are additional details of the fuzzing setup for each browser:

- Google Chrome was fuzzed on an internal Chrome Security fuzzing cluster called[ClusterFuzz](http://dev.chromium.org/Home/chromium-security/bugs/using-clusterfuzz). To fuzz Google Chrome on ClusterFuzz we simply needed to upload the fuzzer and it was run automatically against various Chrome builds.

- Mozilla Firefox was fuzzed on internal Google infrastructure (linux based). Since Mozilla already offers Firefox ASAN builds for download, we used that as a fuzzing target. Each crash was additionally verified against a release build.

- Internet Explorer 11 was fuzzed on Google Compute Engine running Windows Server 2012 R2 64-bit. Given the lack of ASAN build, page heap was applied to iexplore.exe process to make it easier to catch some types of issues.

- Microsoft Edge was the only browser we couldn’t easily fuzz on Google infrastructure since Google Compute Engine doesn’t support Windows 10 at this time and Windows Server 2016 does not include Microsoft Edge. That’s why for fuzzing it we created a virtual cluster of Windows 10 VMs on Microsoft Azure. Same as with Internet Explorer, page heap was applied to MicrosoftEdgeCP.exe process before fuzzing.

- Instead of fuzzing Safari directly, which would require Apple hardware, we instead used WebKitGTK+ which we could run on internal (Linux-based) infrastructure. We created an ASAN build of the release version of WebKitGTK+. Additionally, each crash was verified against a nightly ASAN WebKit build running on a Mac.

## Results

Without further ado, the number of security bugs found in each browsers are captured in the table below.

Only security bugs were counted in the results (doing anything else is tricky as some browser vendors fix non-security crashes while some don’t) and only bugs affecting the currently released version of the browser at the time of fuzzing were counted (as we don’t know if bugs in development version would be caught by internal review and fuzzing process before release).

| Vendor | Browser | Engine | Number of Bugs | Project Zero Bug IDs | 
| Google | Chrome | Blink | 2 | 994, 1024 | 
| Mozilla | Firefox | Gecko | 4\*\* | 1130, 1155, 1160, 1185 | 
| Microsoft | Internet Explorer | Trident | 4 | 1011, 1076, 1118, 1233 | 
| Microsoft | Edge | EdgeHtml | 6 | 1011, 1254, 1255, 1264, 1301, 1309 | 
| Apple | Safari | WebKit | 17 | 999, 1038, 1044, 1080, 1082, 1087, 1090, 1097, 1105, 1114, 1241, 1242, 1243, 1244, 1246, 1249, 1250 | 
| Total |  |  | 31\* |  | 

\*While adding the number of bugs results in 33, 2 of the bugs affected multiple browsers

\*\*The root cause of one of the bugs found in Mozilla Firefox was in the Skia graphics library and not in Mozilla source. However, since the relevant code was contributed by Mozilla engineers, I consider it fair to count here.

All of the bugs listed here have been fixed in the current shipping versions of the browsers. As can be seen in the table most browsers did relatively well in the experiment with only a couple of security relevant crashes found. Since using the same methodology used to result in significantly higher number of issues just several years ago, this shows clear progress for most of the web browsers. For most of the browsers the differences are not sufficiently statistically significant to justify saying that one browser’s DOM engine is better or worse than another.

However, Apple Safari is a clear outlier in the experiment with significantly higher number of bugs found. This is especially worrying given attackers’ interest in the platform as evidenced by the exploit prices and recent targeted attacks. It is also interesting to compare Safari’s results to Chrome’s, as until a couple of years ago, they were using the same DOM engine (WebKit). It appears that after the Blink/Webkit split either the number of bugs in Blink got significantly reduced or a significant number of bugs got introduced in the new WebKit code (or both). To attempt to address this discrepancy, I reached out to Apple Security proposing to share the tools and methodology. When one of the Project Zero members decided to transfer to Apple, he contacted me and asked if the offer was still valid. So Apple received a copy of the fuzzer and will hopefully use it to improve WebKit.

It is also interesting to observe the effect of MemGC, a use-after-free mitigation in Internet Explorer and Microsoft Edge. When this mitigation is disabled using the registry flag OverrideMemoryProtectionSetting, a lot more bugs appear. However, Microsoft considers these bugs strongly mitigated by MemGC and I agree with that assessment. Given that IE used to be plagued with use-after-free issues, MemGC is an example of a useful mitigation that results in a clear positive real-world impact. Kudos to Microsoft’s team behind it!

When interpreting the results, it is very important to note that they don’t necessarily reflect the security of the whole browser and instead focus on just a single component (DOM engine), but one that has historically been a source of many security issues. This experiment does not take into account other aspects such as presence and security of a sandbox, bugs in other components such as scripting engines etc. I can also not disregard the possibility that, within DOM, my fuzzer is more capable at finding certain types of issues than other, which might have an effect on the overall stats.

## Experimenting with coverage-guided DOM fuzzing

Since coverage-guided fuzzing seems to produce very good results in other areas we wanted to combine it with the DOM fuzzing. We built an experimental coverage-guided DOM fuzzer and ran it against Internet Explorer. IE was selected as a target both because of the author's familiarity with it and because it is very easy to limit coverage collection to just the DOM component (mshtml.dll). The experimental fuzzer used a modified Domato engine to generate mutations and used a modified WinAFL's DynamoRIO client to measure coverage. The fuzzing flow worked roughly as follows:

1. The fuzzer generates a new set of samples by mutating existing samples in the corpus.
2. The fuzzer spawns IE process which opens a harness HTML page.
3. The harness HTML page instructs the fuzzer to start measuring coverage and loads one of the samples in an iframe
4. After the sample executes, it notifies the harness which notifies the fuzzer to stop collecting coverage.
5. Coverage map is examined and if it contains unseen coverage, the corresponding sample is added to the corpus.
6. Go to step 3 until all samples are executed or the IE process crashes
7. Periodically minimize the corpus using the AFL’s cmin algorithm.
8. Go to step 1.

The following set of mutations was used to produce new samples from the existing ones:

- Adding new CSS rules
- Adding new properties to the existing CSS rules
- Adding new HTML elements
- Adding new properties to the existing HTML elements
- Adding new JavaScript lines. The new lines would be aware of the existing JavaScript variables and could thus reuse them.

Unfortunately, while we did see a steady increase in the collected coverage over time while running the fuzzer, it did not result in any new crashes (i.e. crashes that would not be discovered using dumb fuzzing). It would appear more investigation is required in order to combine coverage information with DOM fuzzing in a meaningful way.

## Conclusion

As stated before, DOM engines have been one of the largest sources of web browser bugs. While this type of bug are far from gone, most browsers show clear progress in this area. The results also highlight the importance of doing continuous security testing as bugs get introduced with new code and a relatively short period of development can significantly deteriorate a product’s security posture.

The big question at the end is: Are we now at a stage where it is more worthwhile to look for security bugs manually than via fuzzing? Or do more targeted fuzzers need to be created instead of using generic DOM fuzzers to achieve better results? And if we are not there yet - will we be there soon (hopefully)? The answer certainly depends on the browser and the person in question. Instead of attempting to answer these questions myself, I would like to invite the security community to let us know their thoughts.
