# 0day &quot;In the Wild&quot; - Project Zero

Source: https://projectzero.google/0day.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Project Zero’s team mission is to “make zero-day hard”, i.e. to make it more costly to discover and exploit security vulnerabilities. We primarily achieve this by performing our own security research, but at times we also study external instances of zero-day exploits that were discovered “in the wild”. These cases provide an interesting glimpse into real-world attacker behavior and capabilities, in a way that nicely augments the insights we gain from our own research.

Today, we’re sharing our tracking spreadsheet for publicly known cases of detected zero-day exploits, in the hope that this can be a useful community resource:

Spreadsheet link: [0day “In the Wild”](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/view)

This data is collected from a range of public sources. We include relevant links to third-party analysis and attribution, but we do this only for your information; their inclusion does not mean we endorse or validate the content there. The data described in the spreadsheet is nothing new, but we think that collecting it together in one place is useful. For example, it shows that:

- On average, a new “in the wild” exploit is discovered every 17 days (but in practice these often clump together in exploit chains that are all discovered on the same date);
- Across all vendors, it takes 15 days on average to patch a vulnerability that is being used in active attacks;
- A detailed technical analysis on the root-cause of the vulnerability is published for 86% of listed CVEs;
- Memory corruption issues are the root-cause of 68% of listed CVEs.

We also think that this data poses an interesting question: what is the detection rate of 0day exploits? In other words, at what rate are 0day exploits being used in attacks without being detected? This is a key “unknown parameter” in security, and how you model it will greatly inform your views, plans, and priorities as a defender.

It’s also important that we interpret this data as a failure-case for an attacker, and so it doesn’t make sense to draw overarching conclusions about attacker behavior based on a limited data set like this – we see a brief glimpse, but not the whole story. Additionally, the rate of detection is likely to differ substantially between platforms (e.g. mobile vs desktop), so it’s not useful for direct comparisons between platforms either.

Finally, if you spot something in the spreadsheet that looks incorrect, let us know! We hope to maintain and improve this spreadsheet over time, and welcome suggestions for additions or corrections based on publicly available data.
