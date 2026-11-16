# 🕵️‍♂️ Malicious Chrome Extensions Steal ChatGPT and DeepSeek Conversations

- **Source URL:** https://www.ox.security/blog/malicious-chrome-extensions-steal-chatgpt-deepseek-conversations
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1062 (id 1062)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### **OX Security discovered two malicious extensions – impersonating the legitimate AITOPIA extension. The malicious extensions exfiltrate ChatGPT and DeepSeek conversations alongside browsing data to attacker-controlled servers. Despite containing data-stealing malware, one of them received Google’s “Featured” badge**

## TL;DR

The OX Research team detected a new malware campaign stealing ChatGPT and DeepSeek conversations – from over 900,000 Chrome extension downloads. Two malicious extensions were found exfiltrating user conversations and all Chrome tab URLs to a remote C2 server every 30 minutes.

The malware deceives users by impersonating a legitimate extension by a company called AITOPIA, which adds a sidebar on top of any website, with the ability to chat with the most popular LLMs in the market.

The malware adds malicious capabilities by requesting consent for “anonymous, non-identifiable analytics data” while actually exfiltrating complete conversation content from ChatGPT and DeepSeek sessions.

The threat actors are abusing Lovable, an AI-powered web development platform, to host their privacy policies and other infrastructure components, anonymizing their activities and preventing researchers from tracing back to the original actors.

[Watch the Webinar](https://www.ox.security/webinar/lessons-for-security-leaders-from-anthropics-mcp-failure?ref=in-content-cta-mcp-webinar)

## About the Malicious Extensions

We identified two malicious extensions inside this malware campaign, both un-elegantly named:

1. **Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI**  – with over 600,000 users and a Google Chrome Featured badge

2\. **AI Sidebar with Deepseek, ChatGPT, Claude and more** –  with over 300,000 users.

## Potential Damage

The scope of information compromise is significant. Stolen data sent to the threat actor’s C2 server includes:

**AI Conversation Data –** which could include:

- Proprietary source code and development queries shared with ChatGPT or DeepSeek
- Business strategies, competitive intelligence, and strategic planning discussions

- Personal identifiable information (PII) disclosed during conversations
- Confidential research, legal matters, and sensitive corporate communications

**Browsing Activity:** 

- Complete URLs from all Chrome tabs, exposing the user’s browsing profile
- Search queries containing sensitive keywords and research topics
- URL parameters that may contain session tokens, user IDs, and authentication data
- Internal corporate URLs revealing organizational structure and tools

This data can be weaponized for corporate espionage, identity theft, targeted phishing campaigns, or sold on underground forums. Organizations whose employees installed these extensions may have unknowingly exposed intellectual property, customer data, and confidential business information.

## Recommendations

- If you have downloaded one of the affected Chrome extensions, immediately remove them from your browser.
  - Go to either of the extension pages, and check if you have the “Remove from Chrome” button
  - Another way to remove the extensions is to copy paste “chrome://extensions” into your browser, and remove them directly from there.
- Do not install extensions from unknown sources, even if they have the “Featured” tag on them.

### Disclosure & Response From Google

We reported both malicious extensions to Google on 29-Dec-2025. As of Dec 30, Google team reached out in response saying the issue is in review.

Both extensions remain live and actively downloadable on the Chrome Web Store, with the first extension still carrying its ‘Featured’ badge.

## Attack Analysis

### Method: Impersonating a Legitimate Chrome Extension

The original AITOPIA extension adds a sidebar on top of any website, with the ability to chat with the most popular LLMs in the market. AITOPIA details in its privacy policy that users’ chats through the company’s sidebar “will be saved on AITOPIA.ai servers in Amazon US Data server” – **this is legitimate behavior with proper disclosure.**

**The Impersonation Strategy:** The threat actors copied the functionality of AITOPIA’s legitimate AI sidebar extension, then added malicious data exfiltration capabilities on top. While the extensions provide the same AI chat sidebar interface that users expect, they contain hidden malware that steals ChatGPT and DeepSeek conversations directly from the browser – functionality absent from the legitimate AITOPIA extension.

This approach serves two purposes: it makes the malicious extensions appear functional and useful (increasing download rates), while the familiar AITOPIA interface masks the malicious activity occurring in the background.

This is how the **LEGITIMATE AITOPIA** extension looks in the Chrome extensions store:

## How it Works

The malware leverages broad “read all website content” permissions to monitor user browsing activity. When a user visits ChatGPT or DeepSeek, the extension identifies active conversation pages and extracts both user prompts and AI responses in real-time. This stolen data is stored in a local database on the victim’s machine, then exfiltrated in batches to a remote command-and-control (C2) server every 30 minutes.

[Watch Now](https://www.ox.security/webinar/threat-intelligence-update-whats-been-working-for-hackers-and-what-have-the-good-guys-been-doing?ref=in-content-threat-intelligence-update-webinar)

### Legitimate AITOPIA extension behavior

### Malicious extensions behavior

### Malware Analysis

When the malware is installed, it asks the user for permission to collect anonymized browser behavior. If the user clicks yes, the extension automatically starts to listen to events such as visited URLs, ChatGPT and DeepSeek chats.

After clicking yes, the malware automatically starts to collect user data, it first generates a unique user ID in order to track each user’s behavior – “gptChatId”, then it reads the previous and the current URL the user is visiting and saves them to the local storage, later to be sent to the remote C2 server

Visited URLs collection via the chrome.tabs.onUpdated API:

When sending the visited URLs to the remote server – you can see that information such as google search queries can be part of the information collected and sent to the remote server.

Please note that before sending the information, it is encoded via base64, in this report we show you the decoded information sent to the remote C2 server.

In order to read the ChatGPT and DeepSeek information, it checks if the current website URL contains either “chatgpt” or “deepseek”, then it looks for specific DOM elements inside the page that point to the chat conversation, if found, it extracts the chat messages and stores them, in order to later send them to the remote server.

Chat conversation sent to the remote server, this includes the ChatGPT session ID collected from the ChatGPT URL:

All information is sent to the C2 server deepaichats\[.\]com, in 30 minutes intervals:

### Threat Intelligence

This malware campaign has two Chrome extensions:

- Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI
- AI Sidebar with Deepseek, ChatGPT, Claude and more.

When one of the extensions is uninstalled it opens the other malicious extension inside a new tab, in order to trick users into installing the other extension instead.

In order to hide their activities, the threat actors setup the privacy policy and uninstall redirection websites using the vibe coding tool Lovable, making it hard to traceback the creators of the websites:

The first extension – “Chat GPT for Chrome …” is seen as a “Featured” extension, meaning it is presented first in searches, and shown above other extensions in the store. The Chrome store states that it “Follows recommended practices for Chrome extensions”.

### AITOPIA Chrome Extension Similarities

Inside the malicious extensions codebase, we can see multiple indications that this extension is a modified version of the AITOPIA Chrome Extension, providing the same AI Sidebar functionality, but without sending private user information to a remote C2 server, this include both the malicious extension’s description, the codebase, and the behavior – showing the AITOPIA screen when opened –

From the malicious extension’s description:

### Privacy Policy

Inside the privacy policy of “Chat GPT for Chrome with GPT-5” the developer states that they “do not collect personal information”, and also state that all of the information is being saved locally, offline inside the browser. In no place there’s a statement about sending browsing content and history to a remote server.

The malicious extensions reference AITOPIA in their privacy policies, further reinforcing the impersonation and potentially confusing users who might search for AITOPIA to verify legitimacy.

Inside the “AI Sidebar with Deepseek” privacy policy, they state that they collect anonymized data,

They also state they use AITOPIA and that they collect saved chat history – which is also saved and sent even if the user doesn’t create an account with AITOPIA.

### IoC

| Name | Extension ID | Version | Hash | 
| Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI | fnmihdojmnkclgjpcoonokmkhjpjechg | 1.9.6 | 98d1f151872c27d0abae3887f7d6cb6e4ce29e99ad827cb077e1232bc4a69c00 | 
| AI Sidebar with Deepseek, ChatGPT, Claude and more. | inhcgfpbfdjbjogdfjbclgolkmhnooop | 1.6.1 | 20ba72e91d7685926c8c1c5b4646616fa9d769e32c1bc4e9f15dddaf3429cea7 | 

##### C2 Servers

- Lovable Servers
  - chataigpt\[.\]pro
  - chatgptsidebar\[.\]pro
- C2 Endpoints
  - deepaichats\[.\]com
  - chatsaigpt\[.\]com
- Websites
  - deepseek\[.\]ai
  - chatgptbuddy\[.\]com
