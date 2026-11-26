# Two Bypasses for Chrome's Sanitizer API

- Author: Searchlight Cyber / Assetnote research (@hash_kitten), published May 22, 2026
- Source: https://www.slcyber.io/research/two-bypasses-for-chromes-sanitizer-api
- Linked from: https://x.com/garethheyes/status/2125629582015611281 (2026-11-25)
- Fetched 2026-11-26 (readable extraction; code blocks partially flattened by the extractor — consult source for exact formatting)

Share on social

May 22, 2026

Lorem ipsum

The Sanitizer API arrived [with much fanfare](https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/) in both Chrome 146 and Firefox 148 just a few months ago. The API provides two new ways to set HTML safely from within javascript; the default mode:

``node.setHTML(`<b>Hello, world!</b>`)``

And the more customizable mode:

`const config = {`

"elements": \["p", "span", "b"\],

"attributes": \["class"\]

};

const sanitizer = new Sanitizer(config);

node.setHTML(\`\<b>Hello, world!\</b>\`, {sanitizer: sanitizer});

The most permissive mode for this new API is the empty config `{}`, which means 'allow anything, except scripts':

`const sanitizer = new Sanitizer({});`

node.setHTML(\`\<b>Hello, world!\</b>\`, {sanitizer: sanitizer});

The specification is clear: no matter how you configure the sanitizer, you should not be able to pass through HTML that results in XSS.

The sanitizer API is a strong security boundary and solves the biggest issue plaguing the industry-standard DOMPurify today - mutation XSS. The standard use of DOMPurify is something like this:

``const clean = DOMPurify.sanitize(`<b>Hello, world!</b>`);``

node.innerHTML = clean;

This approach seems clean but has a very significant issue; the code involves a serialization from HTML to string (since `DOMPurify.sanitize` returns a string) and then the HTML is reparsed when it is assigned to `innerHTML`. Due to the complexity of the HTML parsing and serialization rules, this can result in a parsing differential between what DOMPurify sees and what ends up in the DOM tree, leading to XSS. This has been exploited [again](https://www.securitum.com/mutation-xss-via-mathml-mutation-dompurify-2-0-17-bypass.html) and [again](https://portswigger.net/research/bypassing-dompurify-again-with-mutation-xss) and [again](https://mizu.re/post/exploring-the-dompurify-library-bypasses-and-fixes). Significant hardening, such as the [mXSS protections in browsers](https://developer.chrome.com/blog/escape-attributes) and DOMPurify's namespace sanitizer, has left the library safe for now, but there is no theoretical obstacle to another bypass.

The sanitizer API, on the other hand, returns the DOM tree directly. There is no serialization/reparsing round trip, and thus a lot of these issues are directly eliminated. (For what it's worth, DOMPurify offers this as `RETURN_DOM`, but adoption in the wild is low). Therefore, bypassing this new API requires new ideas from the security community and new approaches. In this blog post, I present two bypasses for the Sanitizer API in Chrome 146; one of which was discovered and reported by myself, and one which I reverse engineered from a Chrome commit. These two bypasses use novel, disparate ideas and can hopefully inspire future security research on the Sanitizer API.

The main file that handles most of the sanitization is [`third_party/blink/renderer/core/sanitizer/sanitizer.cc`](https://source.chromium.org/chromium/chromium/src/+/075796a0e7faad0baefcda33a792ffd0e26d4354:third_party/blink/renderer/core/sanitizer/sanitizer.cc). After reading the file from top to bottom and the [associated specification from WICG](https://wicg.github.io/sanitizer-api/), one thing that stood out to me was this direct string comparison:

`void RemoveAttributeIfValueIsHref(Element* element,`

const QualifiedName& attribute) {

const AtomicString& value = element->getAttribute(attribute);

if (value == "href" or value == "xlink:href") {

element->removeAttribute(attribute);

}

}

Direct string comparisons rarely work in HTML-world for sanitization. But what is this meant to protect?

As is well known by now, SVG can not only handle static images but dynamic ones too. One of the ways of achieving animation is the `<animate>` tag, which looks something like this:

`<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">`

\<rect id="foo" x="10" y="10" width="50" height="50" fill="tomato"/>

\<animate href="#foo" attributeName="x" from="10" to="140" dur="2s" repeatCount="indefinite"/>

\</svg>

There are a couple of components here. We first define a `<rect>` with an ID of `foo`. Then, using the `<animate>` tag, we specify via the `attributeName` parameter that we are going to vary `x` over the values `10` to `140`. The effect of this is that we animate the square to move from left to right. If you were to query the `foo.x` property via Javascript, you would see that the value does indeed actually change over time.

Not every attribute can be animated. However, when these features were introduced, it was [quickly noticed](https://portswigger.net/research/svg-animate-xss-vector) that the `href` and `xlink:href` attributes are animatable. This means things like this are possible:

`<svg>`

\<a id="foo">\<text x=20 y=20>click me\</text>\</a>

\<animate href="#foo" attributeName="href" values="javascript:alert(1)"/>

\</svg>

This is the purpose of the sanitization routine above. This routine is called for all tags that can take an `attributeName`:

`void Sanitizer::SanitizeJavascriptNavigationAttributes(Element* element,`

Mode safe) const {

// ... SNIP ...

if (...) {

// ... SNIP ...

} else if (qname == svg\_names::kAnimateTag ||

qname == svg\_names::kAnimateMotionTag ||

qname == svg\_names::kAnimateTransformTag ||

qname == svg\_names::kSetTag) {

RemoveAttributeIfValueIsHref(element, svg\_names::kAttributeNameAttr);

}

}

Recall that the attribute comparison is done strictly and case sensitively - the attribute to animate must be exactly `href` or `xlink:href`. Those of you with hacker sense might already be scheming bypasses, and I had the same thought. I tried several variations, including:

`HREF`

hReF

href (leading space)

href�

But nothing like this worked. Turns out, SVG is pretty strict about exact casing and spacing when it comes to attribute names!

I turned my attention to the other blocked attribute: `xlink:href` . This is a namespaced element, and it's parsed by splitting the attribute on `:` - the first element is the namespace, and the second is the attribute name. I quickly hypothesized that this might be implemented by splitting on `:` and taking the first two elements. Thus, I tried `xlink:href:x`, and it worked! This achieves an XSS while bypassing the sanitizer. The final payload:

`<svg xmlns:xlink="http://www.w3.org/1999/xlink">`

\<a id="foo">\<text x=20 y=20>click me\</text>\</a>

\<animate href="#foo" attributeName="xlink:href:x" values="javascript:alert(1)"/>

\</svg>

Chrome fixed this in two ways:

`RemoveAttributeIfValueIsHref`
Two days after the patch landed for my sanitizer bypass, I noticed a suspicious commit which touched the `sanitizer.cc` file - [c7d115c0](https://source.chromium.org/chromium/chromium/src/+/c7d115c0878465398b7aa3ceea3841484010a25e). The commit has a few changes but the relevant one is this single line:

`void RemoveAttributeIfProtocolIsJavaScript(Element* element,`

const QualifiedName& attribute) {

const AtomicString& value = element->getAttribute(attribute);

-  if (value && KURL(value.GetString()).ProtocolIsJavaScript()) {

+  if (value && ProtocolIsJavaScript(value)) {

element->removeAttribute(attribute);

}

}

The commit description gives us a hint as to what it's doing:


For checking the scheme there's a fast-path scheme parser, so we don't need to parse the entire URL.

Let's understand what the change does. Firstly, `RemoveAttributeIfProtocolIsJavaScript` is used in this way:

`void Sanitizer::SanitizeJavascriptNavigationAttributes(Element* element,`

Mode safe) const {

// ... SNIP ...

const QualifiedName& qname = element->TagQName();

if (qname == html\_names::kATag || qname == html\_names::kAreaTag ||

qname == html\_names::kBaseTag) {

RemoveAttributeIfProtocolIsJavaScript(element, html\_names::kHrefAttr);

} else if (qname == svg\_names::kATag ||

element->namespaceURI() == mathml\_names::kNamespaceURI) {

RemoveAttributeIfProtocolIsJavaScript(element, html\_names::kHrefAttr);

RemoveAttributeIfProtocolIsJavaScript(element, xlink\_names::kHrefAttr);

} else if (qname == html\_names::kButtonTag ||

qname == html\_names::kInputTag) {

RemoveAttributeIfProtocolIsJavaScript(element, html\_names::kFormactionAttr);

} else if (qname == html\_names::kFormTag) {

RemoveAttributeIfProtocolIsJavaScript(element, html\_names::kActionAttr);

} else if (qname == html\_names::kIFrameTag) {

RemoveAttributeIfProtocolIsJavaScript(element, html\_names::kSrcAttr);

}

// ... SNIP ...

}

This is the function responsible for stripping the `javascript:` protocol from navigations. This protects against simple vectors like:

`<a href="javascript:alert(1)">click me</a>`

\<form>\<button type="submit" formaction="javascript:alert(1)"/>\</form>

\<form action="javascript:alert(1)">\<button type="submit"/>\</form>

Anyone who has spent any time looking at XSS knows that simply checking that a navigation attribute starts with `javascript:` is not sufficient; the URL has complex parsing rules which means that URLs like `jAvA
script:alert(1)` still work. To combat this, the old Chrome code used its own URL parser called `KURL` (the same one that handles constructing the navigation) to parse the URL, and strips the attribute if the protocol is `javascript`.

On the other hand, the patched code uses a special `ProtocolIsJavaScript` function. This function does not construct a full `KURL` object, but instead emulates the parsing of *just the protocol* part of `KURL` and uses that as a shortcut, resulting in a large efficiency gain over thousands of URLs; after all, the `KURL` object is only being used for checking the protocol and is then immediately discarded.

At first glance, you might guess there is some subtle difference in how the protocol is parsed between the browser on a navigation, `KURL`, and the free form `ProtocolIsJavaScript` function. But indeed, after checking the implementations carefully, the protocol parsing in all of them is the exact same. There is, however, one difference: if `KURL` thinks the URL is not valid, `KURL::ProtocolIsJavaScript` will always return false, but the free form version `ProtocolIsJavaScript` will return true.

Is there such a thing as an 'invalid' Javascript URL? Turns out, there is!

`new URL('javascript://://aaa')`

// Uncaught TypeError: URL constructor: javascript://://aaa is not a valid URL.

This is because the `//:/` is treated as a `hostname:port` combo. Since you can't have an empty host or port, the URL is considered invalid. Thus in Chrome 146, if you sanitize `<a href="javascript://://aaa">click me</a>` using the Sanitizer API, it will actually leave the URL untouched. This is because the `KURL` constructor sees that the URL is invalid, and so `ProtocolIsJavaScript` returns false.

There is one problem with this 'bypass' - even though the `javascript` URL makes it to the DOM untouched, when you click on it, nothing happens. You may initially think this is because the `//` forms a comment, but you can verify this isn't the case. Using a payload like `javascript://:// alert(1)` (where ` ` is a valid line separator) still doesn't result in XSS on click. The real reason is that the URL is invalid, so the browser will refuse to navigate to it or execute. This makes sense; the browser is using the same construction under the hood to handle navigation, and so an invalid URL will result in no execution. You can doubly verify this by trying to navigate to the URL manually:

`document.location = 'javascript://://aaa'`

// Uncaught SyntaxError: Failed to set the 'href' property on 'Location'

// 'javascript:///.//aaa' is not a valid URL.

The question then becomes; is there some HTML construction where the URL is *mutated* before click, in such a way that the invalid URL could become valid? As it turns out, there is indeed such a mechanism in HTML - forms. Consider the following HTML:

`<form action="https://example.com/path">`

\<input name="foo" value="bar"/>

\<button type="submit">click me\</button>

\</form>

This is a GET-based form. When you click the `click me` button, you get sent to `https://example.com/path?foo=bar`. What happens is roughly as follows:

`action``foo=bar`

We are lucky. In Chrome, if the URL is reserialized after having an invalid host, Chrome will treat the URL as if it had no host (just a path and query). This gives us the differential we need to conjure a working Javascript XSS out of the invalid URL.

After a bit of tweaking, I landed on this payload:

`<form action="javascript://://-alert(1)//">`

\<button type="submit">click me\</button>

\</form>

Pre-patch, this would pass through the Sanitizer API untouched - but when you click on it, you get an alert. Let's trace what happens:

`javascript://://-alert(1)//``KURL``click me``?``//-alert(1)//``//``/.//``javascript:/.//-alert(1)//?``/./``/``-``alert(1)``//?`
Phew!

While this is patched now for the sanitizer, it could be useful in other situations. I posted a challenge on X that looked like this:

`<html>`

\<body>

\<form id="targetForm">\</form>

Please enter a url, like as follows: \<a href="?url=https://example.com">?url=https://example.com\</a>

\</body>

\<script defer="true">

const url = new URLSearchParams(window.location.search).get('url');

if (url && URL.parse(url)?.protocol != 'javascript:') {

targetForm.action = url;

targetForm.submit();

}

\</script>

\</html>

Here, it's checking that if the URL is valid, that its protocol must not be `javascript:`. At first, this condition seems impossible to bypass for XSS. But using the invalid URL trick, we can indeed get XSS with `javascript://://-alert(1)//`! In general, any sanitizer that

`javascript``URL`
Could be fooled by this technique.

The Sanitizer API has opened up a brand new surface for client side research. While the techniques described are patched now, I am sure there are other techniques waiting to be discovered. I am excited to see what the security research community comes up with!

Timeline:

`xlink:href``ProtocolIsJavaScript`
Customers of Searchlight Cyber’s ASM solution, [Assetnote](https://slcyber.io/products/attack-surface-management-tool/), are always first to receive checks for the novel vulnerabilities we discover – often weeks or months before public disclosure. Our Security Research Team continues to dig beyond public PoCs to deliver high-signal detections to our platform. [Learn more](https://slcyber.io/products/attack-surface-management-tool/).