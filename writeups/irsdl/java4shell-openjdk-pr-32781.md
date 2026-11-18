# java4shell-openjdk-pr-32781

- **Source URL:** https://github.com/openjdk/jdk/pull/32781
- **Fetched:** 2026-11-18
- **Researcher:** irsdl
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

## Repository navigation

# 8392044: AVX-512 Base64 decoder overwrites output buffer on short padded tail - #32781

[albertnetymk](/albertnetymk)wants to merge 1 commit into

## [albertnetymk](/albertnetymk) wants to merge 1 commit into

## Conversation

| 👋 Welcome back ayang! A progress list of the required criteria for merging this PR into `master` will be added to the body of your pull request. There are additional [pull request commands](https://wiki.openjdk.java.net/display/SKARA/Pull+Request+Commands) available for use with this pull request. | 

| ❗ This change is not yet ready to be integrated. See the **Progress** checklist in the description for automated requirements. | 


[openjdk](/apps/openjdk)Bot changed the title

~~8392044~~8392044: AVX-512 Base64 decoder overwrites output buffer on short padded tail

[Sep 9, 2026](#event-30816762191)

| [@albertnetymk](https://github.com/albertnetymk) The following label will be automatically applied to this pull request: `hotspot-compiler` When this pull request is ready to be reviewed, an "RFR" email will be sent to the corresponding mailing list. If you would like to change these labels, use the [/label](https://wiki.openjdk.org/display/SKARA/Pull+Request+Commands#PullRequestCommands-/label) pull request command. | 

| The total number of required reviews for this PR has been set to 2 based on the presence of this label: `hotspot-compiler`. This can be overridden with the `/reviewers` command. | 

| [@albertnetymk](https://github.com/albertnetymk) This pull request has been inactive for more than 8 weeks and will be automatically closed if another 8 weeks passes without any activity. To avoid this, simply issue a `/touch` or `/keepalive` command to the pull request. Feel free to ask for assistance if you need help with progressing this pull request towards integration! | 

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

In

`StubGenerator::generate_base64_decodeBlock()`(x86\_64 AVX-512 VBMI path),`L_finalBit`handles 1-63 leftover bytes with a masked vector sequence that computes`output_size = (len/4)*3`. Valid inputs always have a length multiple of 4, so this bug triggers only on invalid inputs: with`length < 4`(e.g.`"A".repeat(64)+"="`leaves 1 byte after`L_process64Loop`),`output_size`starts at 0 and the padding path decrements it below zero, producing a wrong`output_mask`. The stub stores past the logical output length before returning to Java, corrupting the heap.
The suggested fix is to early-return to Java if

`length < 4`.
## Progress

## Integration blocker

`8392044`. Please make sure it exists and is accessible.
## Issue

`8392044`.
## Reviewing

## Using

`git`
Checkout this PR locally:



`$ git fetch https://git.openjdk.org/jdk.git pull/32781/head:pull/32781``$ git checkout pull/32781`
Update a local copy of the PR:



`$ git checkout pull/32781``$ git pull https://git.openjdk.org/jdk.git pull/32781/head`
## Using Skara CLI tools

Checkout this PR locally:


`$ git pr checkout 32781`
View PR using the GUI difftool:


`$ git pr show -t 32781`
## Using diff file

Download this PR as a diff file:

https://git.openjdk.org/jdk/pull/32781.diff
