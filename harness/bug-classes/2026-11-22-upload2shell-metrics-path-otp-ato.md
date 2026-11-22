# 2026-11-22 bug-class check-specs

Source posts: PaulosYibelo Upload2Shell (CVE-2026-125396), mdp_sec `/./metrics` edge bypass + OTP ATO.

## 1. upload_triggers_ghostscript

- **Signal:** Any upload/preview/thumbnail/crop/print path that can hand attacker bytes to ImageMagick, Imagick, Pillow `load()/crop()`, imageio, libvips `magickload`, Qt EPS plugin, or CUPS `gstopdf`.
- **Probe:** Upload EPS/PostScript content under a trusted extension (`.jpg`/`.png`/`.pdf`); watch for `gs` process spawn or ImageMagick PostScript delegate.
- **Escalate if:** Ghostscript < 10.08.0 (CVE-2026-125396 Type1 font UAF → `-dSAFER` bypass → `%pipe%` RCE).
- **Known remote chains:** Roundcube email thumbnail (external sender), WordPress PDF preview + Forminator/Essential Addons public upload fields, Debian 13 CUPS anonymous IPP Print-Job.
- **Refs:** `writeups/PaulosYibelo/upload2shell-research-CVE-2026-125396.md`, posts/PaulosYibelo/2026-11-21-2124203995329933441.md

## 2. edge_path_denylist_normalization_bypass

- **Signal:** Edge/WAF exact-path denylist (e.g. `/metrics`, `/actuator`, `/debug`) returns 403 on the canonical path but 200 on `/./path`, `/path/.`, percent-encoding of any single character, or Unicode NFKC variants.
- **Probe corpus:** `/./metrics`, `/metrics/.`, `/././metrics`, `%6detrics`, `%6Detrics`, double-encode, trailing slash, mixed case.
- **Escalate if:** Response body contains tokens/secrets (Prometheus labels with request paths often leak bearer/applicant tokens). Replay leaked tokens against app CRUD.
- **Refs:** posts/mdp_sec/2026-11-21-2124233889270939950.md

## 3. otp_verify_finalize_identity_mismatch (ATO)

- **Signal:** OTP/MFA verify step binds to account A, but finalize/login response issues a session for account B.
- **Probe (two owned accounts):** Start login as victim; complete OTP under attacker session (or swap user_id/email/phone between verify and finalize); assert identity in finalize response equals identity committed at verify.
- **Also test:** OTP issued for A submitted for B; race verify+finalize; reuse pre-MFA cookie on post-MFA endpoints.
- **Refs:** posts/mdp_sec/2026-11-21-2124052695359381521.md ($5k ATO, details undisclosed)

## 4. huntdeck_pay_per_hour_prioritization

- **Signal:** Public paid disclosures ranked by $/hour put access-control (IDOR/BAC/ATO/open-redirect) in S-tier; open redirect median ~$280.
- **Harness weight:** Prefer IDOR/BAC/ATO/open-redirect fuzzers when optimizing $/hour; keep SQLi/XSS but don't starve access-control coverage.
- **Refs:** posts/mdp_sec/2026-11-21-2124022496446017575.md; huntdeck.io/disclosed (403 to crawler 2026-11-22)

## 5. fhe_privacy_walkaway_test (pcaversaccio / Zama)

- **Signal:** Vendor-dependent FHE/"privacy" stacks whose license grants no patent rights and require vendor permission for commercial use fail walkaway/CROPS.
- **Checklist:** independent reimplementability; patent/license walkaway; who maintains if vendor disappears; attestation/measurement binding independent of vendor keys.
- **Refs:** posts/pcaversaccio/2026-11-21-2124077434697846817.md
