# Release of a Technical Report into Intel Trust Domain Extensions - Project Zero

Source: https://projectzero.google/2023/04/technical-report-into-intel-tdx.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Today, members of Google Project Zero and Google Cloud are releasing a report on a security review of Intel's [Trust Domain Extensions](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-trust-domain-extensions.html) (TDX). TDX is a feature introduced to support [Confidential Computing](https://cloud.google.com/confidential-computing) by providing hardware isolation of virtual machine guests at runtime. This isolation is achieved by securing sensitive resources, such as guest physical memory. This restricts what information is exposed to the hosting environment.


The security review was performed in cooperation with Intel engineers on pre-release source code for version 1.0 of the TDX feature. This code is the basis for the TDX implementation which will be shipping in limited SKUs of the 4th Generation Intel Xeon Scalable CPUs.


The result of the review was the discovery of 10 confirmed security vulnerabilities which were fixed before the final release of products with the TDX feature. The final report highlights the most interesting of these issues and provides an overview of the feature's architecture. 5 additional areas were identified for defense-in-depth changes to subsequent versions of TDX.


You can read more details about the review on the [Google Cloud security blog](https://cloud.google.com/blog/products/identity-security/rsa-google-intel-confidential-computing-more-secure) and the [final report](https://services.google.com/fh/files/misc/intel_tdx_-_full_report_041423.pdf). If you would like to review the source code yourself, Intel has made it available on the [TDX website](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-trust-domain-extensions.html#inpage-nav-5).
