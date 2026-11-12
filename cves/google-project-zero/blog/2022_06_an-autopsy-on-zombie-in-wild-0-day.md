# An Autopsy on a Zombie In-the-Wild 0-day - Project Zero

Source: https://projectzero.google/2022/06/an-autopsy-on-zombie-in-wild-0-day.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Maddie Stone, Google Project Zero


Whenever there’s a new in-the-wild 0-day disclosed, I’m very interested in understanding the root cause of the bug. This allows us to then understand if it was fully fixed, look for variants, and brainstorm new mitigations. This blog is the story of a “zombie” Safari 0-day and how it came back from the dead to be disclosed as exploited in-the-wild in 2022. CVE-2022-22620 was initially fixed in 2013, reintroduced in 2016, and then disclosed as exploited in-the-wild in 2022. If you’re interested in the full root cause analysis for CVE-2022-22620, we’ve published it [here](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2022/CVE-2022-22620.html).


In the [2020 Year in Review of 0-days exploited in the wild](/2021/02/deja-vu-lnerability.html), I wrote how 25% of all 0-days detected and disclosed as exploited in-the-wild in 2020 were variants of previously disclosed vulnerabilities. Almost halfway through 2022 and it seems like we’re seeing a similar trend. Attackers don’t need novel bugs to effectively exploit users with 0-days, but instead can use vulnerabilities closely related to previously disclosed ones. This blog focuses on just one example from this year because it’s a little bit different from other variants that we’ve discussed before. Most variants we’ve discussed previously exist due to incomplete patching. But in this case, the variant was completely patched when the vulnerability was initially reported in 2013. However, the variant was reintroduced 3 years later during large refactoring efforts. The vulnerability then continued to exist for 5 years until it was fixed as an in-the-wild 0-day in January 2022.

# Getting Started

In the case of CVE-2022-22620 I had two pieces of information to help me figure out the vulnerability: [the patch](https://github.com/WebKit/WebKit/commit/486816dc355c19f1de1b8056f85d0bbf7084dd6e) (thanks to Apple for sharing with me!) and [the description from the security bulletin](https://support.apple.com/en-us/HT213093) stating that the vulnerability is a use-after-free. The primary change in the patch was to change the type of the second argument (stateObject) to the function FrameLoader::loadInSameDocument from a raw pointer, SerializedScriptValue\* to a reference-counted pointer, RefPtr\<SerializedScriptValue>.


[trunk/Source/WebCore/loader/FrameLoader.cpp](https://trac.webkit.org/changeset/288539/webkit/trunk/Source/WebCore/loader/FrameLoader.cpp)

|  |  |  | 
| 1094 | 1094 | // This does the same kind of work that didOpenURL does, except it relies on the fact | 
| 1095 | 1095 | // that a higher level already checked that the URLs match and the scrolling is the right thing to do. | 
| 1096 |  | void FrameLoader::loadInSameDocument(const URL& url, SerializedScriptValue\* stateObject, bool isNewNavigation) | 
|  | 1096 | void FrameLoader::loadInSameDocument(URL url, RefPtr\<SerializedScriptValue> stateObject, bool isNewNavigation) | 



Whenever I’m doing a root cause analysis on a browser in-the-wild 0-day, along with studying the code, I also usually search through commit history and bug trackers to see if I can find anything related. I do this to try and understand when the bug was introduced, but also to try and save time. (There’s a lot of 0-days to be studied! 😀)

# The Previous Life

In the case of CVE-2022-22620, I was scrolling through the [git](https://git-scm.com/docs/git-blame) [blame](https://git-scm.com/docs/git-blame) view of FrameLoader.cpp. Specifically I was looking at the [definition of](https://github.com/WebKit/WebKit/blame/7b23cae2a1b1ffd026288f15261f8ba272c3b24b/Source/WebCore/loader/FrameLoader.cpp#L1096) [loadInSameDocument](https://github.com/WebKit/WebKit/blame/7b23cae2a1b1ffd026288f15261f8ba272c3b24b/Source/WebCore/loader/FrameLoader.cpp#L1096). When looking at the git blame for this line prior to our patch, it’s a very [interesting commit](https://github.com/WebKit/WebKit/commit/aa31b6b4d09b09acdf1cec11f2f7f35bd362dd0e). The commit was actually changing the stateObject argument from a reference-counted pointer, PassRefPtr\<SerializedScriptValue>, to a raw pointer, SerializedScriptValue\*. This change from December 2016 introduced CVE-2022-22620. The [Changelog even states](https://github.com/WebKit/WebKit/commit/aa31b6b4d09b09acdf1cec11f2f7f35bd362dd0e#diff-9fb71b6fa7156160059b0216d05933e621d422df2b20f72ad7399eb946b8ba04):


(WebCore::FrameLoader::loadInSameDocument): Take a raw pointer for the

serialized script value state object. No one was passing ownership.

But pass it along to statePopped as a Ref since we need to pass ownership

of the null value, at least for now.


Now I was intrigued and wanted to track down the previous commit that had changed the stateObject argument to PassRefPtr\<SerializedScriptValue>. I was in luck and only had to go back in the history two more steps. There was a [commit from 2013](https://github.com/WebKit/WebKit/commit/4b3be1d3a8d22cb2b2f5ddb8299f7cd25a21cebf) that changed the stateObject argument from the raw pointer, SerializedScriptValue\*, to a reference-counted pointer, PassRefPtr\<SerializedScriptValue>. This commit from February 2013 was doing the same thing that our commit in 2022 was doing. The commit was titled “Use-after-free in SerializedScriptValue::deserialize” and included a good description of how that use-after-free worked.


The commit also included a test:


Added a test that demonstrated a crash due to use-after-free

of SerializedScriptValue.


Test: fast/history/replacestate-nocrash.html


The trigger from this test is:

| Object.prototype.\_\_defineSetter\_\_("foo",function(){history.replaceState("", "")}); history.replaceState({foo:1,zzz:"a".repeat(1\<\<22)}, ""); history.state.length; | 


My hope was that the test would crash the vulnerable version of WebKit and I’d be done with my root cause analysis and could move on to the next bug. Unfortunately, it didn’t crash.


The commit description included the comment to check out a Chromium bug. (During this time Chromium still used the WebKit rendering engine. Chromium forked [the Blink rendering engine in April 2013](https://blog.chromium.org/2013/04/blink-rendering-engine-for-chromium.html).) I saw that my now Project Zero teammate, Sergei Glazunov, originally reported the [Chromium bug](https://bugs.chromium.org/p/chromium/issues/detail?id=171839) back in 2013, so I asked him for the details.


The use-after-free from 2013 (no CVE was assigned) was a bug in the implementation of the History API. This API allows access to (and modification of) a stack of the pages visited in the current frame, and these page states are stored as a SerializedScriptValue. The History API exposes a getter for state, and a method replaceState which allows overwriting the "most recent" history entry. 

The bug was that in the implementation of the getter for state, SerializedScriptValue::deserialize was called on the current "most recent" history entry value without increasing its reference count. As SerializedScriptValue::deserialize could trigger a callback into user JavaScript, the callback could call replaceState to drop the only reference to the history entry value by replacing it with a new value. When the callback returned, the rest of SerializedScriptValue::deserialize ran with a free'd this pointer.


In order to fix this bug, it appears that the developers decided to change every caller of SerializedScriptValue::deserialize to increase the reference count on the stateObject by changing the argument types from a raw pointer to PassRefPtr\<SerializedScriptValue>. While the originally reported trigger called deserialize on the stateObject through the V8History::stateAccessorGetter function, the developers’ fix also caught and patched the path to deserialize through loadInSameDocument.


The timeline of the changes impacting the stateObject is:


- HistoryItem.m\_stateObject is type RefPtr\<SerializedScriptValue>
- HistoryItem::stateObject() returns SerializedScriptValue\*
- FrameLoader::loadInSameDocument takes stateObject argument as SerializedScriptValue\*

- HistoryItem::stateObject returns a PassRefPtr\<SerializedScriptValue>
- FrameLoader::loadInSameDocument takes stateObject argument as PassRefPtr\<SerializedScriptValue>

- HistoryItem::stateObject returns RefPtr instead of PassRefPtr

- HistoryItem::stateObject() is changed to return raw pointer instead of RefPtr

- FrameLoader::loadInSameDocument changed to take stateObject as a raw pointer instead of PassRefPtr\<SerializedScriptValue>

- FrameLoader::loadInSameDocument changed to take stateObject as a RefPtr\<SerializedScriptValue>

# The Autopsy

When we look at the timeline of changes for FrameLoader::loadInSameDocument it seems that the bug was re-introduced in December 2016 due to refactoring. The question is, why did the patch author think that loadInSameDocument would not need to hold a reference. From the [December 2016 commit ChangeLog](https://github.com/WebKit/WebKit/commit/aa31b6b4d09b09acdf1cec11f2f7f35bd362dd0e): Take a raw pointer for the serialized script value state object. No one was passing ownership.


My assessment is that it’s due to the October 2016 changes in HistoryItem:stateObject. When the author was evaluating the refactoring changes needed in the dom directory in December 2016, it would have appeared that the only calls to loadInSameDocument passed in either a null value or the result of stateObject() which as of October 2016 now passed a raw SerializedScriptValue\* pointer. When looking at those two options for the type of an argument, then it’s potentially understandable that the developer thought that loadInSameDocument did not need to share ownership of stateObject.


So why then was HistoryItem::stateObject’s return value changed from a RefPtr to a raw pointer in October 2016? That I’m struggling to find an explanation for.


According to the description, the patch in October 2016 was intended to “Replace all uses of ExceptionCodeWithMessage with WebCore::Exception”. However when we look at the ChangeLog it seems that the author decided to also do some (seemingly unrelated) refactoring to HistoryItem. These are some of the only changes in the commit whose descriptions aren’t related to exceptions. As an outsider looking at the commits, it seems that the developer by chance thought they’d do a little “clean-up” while working through the required refactoring on the exceptions. If this was simply an additional ad-hoc step while in the code, rather than the goal of the commit, it seems plausible that the developer and reviewers may not have further traced the full lifetime of HistoryItem::stateObject.


While the change to HistoryItem in October 2016 was not sufficient to introduce the bug, it seems that that change likely contributed to the developer in December 2016 thinking that loadInSameDocument didn’t need to increase the reference count on the stateObject.


Both the October 2016 and the December 2016 commits were very large. The commit in October changed 40 files with 900 additions and 1225 deletions. The commit in December changed 95 files with 1336 additions and 1325 deletions. It seems untenable for any developers or reviewers to understand the security implications of each change in those commits in detail, especially since they’re related to lifetime semantics.

# The Zombie

We’ve now tracked down the evolution of changes to fix the 2013 vulnerability…and then revert those fixes… so I got back to identifying the 2022 bug. It’s the same bug, but triggered through a different path. That’s why the 2013 test case wasn’t crashing the version of WebKit that should have been vulnerable to CVE-2022-22620:

1. The 2013 test case triggers the bug through the V8History::stateAccessorAndGetter path instead of FrameLoader::loadInSameDocument, and
2. As a part of Sergei’s 2013 bug report there were additional hardening measures put into place that prevented user-code callbacks being processed during deserialization.

Therefore we needed to figure out how to call loadInSameDocument and instead of using the deserialization to trigger a JavaScript callback, we needed to find another event in the loadInSameDocument function that would trigger the callback to user JavaScript.


To quickly figure out how to call loadInSameDocument, I modified the WebKit source code to trigger a test failure if loadInSameDocument was ever called and then ran all the tests in the fast/history directory. There were 5 out of the 80 tests that called loadInSameDocument:


The tests history-back-forward-within-subframe-hash.html and fast/history/history-traversal-is-asynchronous.html were the most helpful. We can trigger the call to loadInSameDocument by setting the history stack with an object whose location is the same page, but includes a hash. We then call history.back() to go back to that state that includes the URL with the hash. loadInSamePage is responsible for scrolling to that location.

| history.pushState("state1", "", location + "#foo"); history.pushState("state2", ""); // current state history.back(); //goes back to state1, triggering loadInSameDocument | 




Now that I knew how to call loadInSameDocument, I teamed up with Sergei to identify how we could get user code execution sometime during the loadInSameDocument function, but prior to the call to statePopped ([FrameLoader.cpp#1158](https://github.com/WebKit/WebKit/blob/7b23cae2a1b1ffd026288f15261f8ba272c3b24b/Source/WebCore/loader/FrameLoader.cpp#L1158)):

| m\_frame.document()->statePopped(stateObject ? Ref\<SerializedScriptValue> { \*stateObject } : SerializedScriptValue::nullValue()); | 


The callback to user code would have to occur prior to the call to statePopped because stateObject was cast to a reference there and thus would now be reference-counted. We assumed that this would be the place where the “freed” object was “used”.


If you go down the rabbit hole of the calls made in loadInSameDocument, we find that there is a path to the blur event being dispatched. We could have also used a tool like [CodeQL](https://codeql.github.com/) to see if there was a path from loadInSameDocument to dispatchEvent, but in this case we just used manual auditing. The call tree to the blur event is:

| FrameLoader::loadInSameDocument FrameLoader::scrollToFragmentWithParentBoundary FrameView::scrollToFragment FrameView::scrollToFragmentInternal FocusController::setFocusedElement FocusController::setFocusedFrame dispatchWindowEvent(Event::create(eventNames().blurEvent, Event::CanBubble::No, Event::IsCancelable::No)); | 


The blur event fires on an element whenever focus is moved from that element to another element. In our case loadInSameDocument is triggered when we need to scroll to a new location within the current page. If we’re scrolling and therefore changing focus to a new element, the blur event is fired on the element that previously had the focus.


The last piece for our trigger is to free the stateObject in the onblur event handler. To do that we call replaceState, which overwrites the current history state with a new object. This causes the final reference to be dropped on the stateObject and it’s therefore free’d. loadInSameDocument still uses the free’d stateObject in its call to statePopped.

| input = document.body.appendChild(document.createElement("input")); a = document.body.appendChild(document.createElement("a")); a.id = "foo"; history.pushState("state1", "", location + "#foo"); history.pushState("state2", ""); setTimeout(() => { input.focus(); input.onblur = () => history.replaceState("state3", ""); setTimeout(() => history.back(), 1000); }, 1000); | 


In both the 2013 and 2022 cases, the root vulnerability is that the stateObject is not correctly reference-counted. In 2013, the developers did a great job of patching all the different paths to trigger the vulnerability, not just the one in the submitted proof-of-concept. This meant that they had also killed the vulnerability in loadInSameDocument. The refactoring in December 2016 then revived the vulnerability to enable it to be exploited in-the-wild and re-patched in 2022.

# Conclusion

Usually when we talk about variants, they exist due to incomplete patches: the vendor doesn’t correctly and completely fix the reported vulnerability. However, for CVE-2022-22620 the vulnerability was correctly and completely fixed in 2013. Its fix was just regressed in 2016 during refactoring. We don’t know how long an attacker was exploiting this vulnerability in-the-wild, but we do know that the vulnerability existed (again) for 5 years: December 2016 until January 2022.


There’s no easy answer for what should have been done differently. The developers responding to the initial bug report in 2013 followed a lot of best-practices:

- Patched all paths to trigger the vulnerability, not just the one in the proof-of-concept. This meant that they patched the variant that would become CVE-2022-22620.
- Submitted a test case with the patch.
- Detailed commit messages explaining the vulnerability and how they were fixing it.
- Additional hardening measures during deserialization.


As an offensive security research team, we can make assumptions about what we believe to be the core challenges facing modern software development teams: legacy code, short reviewer turn-around expectations, refactoring and security efforts are generally under-appreciated and under-rewarded, and lack of memory safety mitigations. Developers and security teams need time to review patches, especially for security issues, and rewarding these efforts, will make a difference. It also will save the vendor resources in the long run. In this case, 9 years after a vulnerability was initially triaged, patched, tested, and released, the whole process had to be duplicated again, but this time under the pressure of in-the-wild exploitation.


While this case study was a 0-day in Safari/WebKit, this is not an issue unique to Safari. Already in 2022, we’ve seen in-the-wild 0-days that are variants of previously disclosed bugs targeting Chromium, Windows, Pixel, and iOS as well. It’s a good reminder that as defenders we all need to stay vigilant in reviewing and auditing code and patches.
