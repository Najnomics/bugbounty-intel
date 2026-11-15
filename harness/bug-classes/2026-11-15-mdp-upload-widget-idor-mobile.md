# Harness checks — 2026-11-15 (mdp_sec)

## 1. Guest upload → RCE
- Enumerate guest/anonymous upload endpoints.
- Polyglot / magic-byte-only bypass corpus (benign header + attacker body; double-ext; CT mismatch).
- Look for config files (YAML/JSON/INI/.htaccess/web.config) written beside uploads and reloaded.
- After upload, request returned + sibling paths; assert no execution.

## 2. Third-party widget config XSS
- Inventory embeds; capture config/bootstrap URLs.
- Unauthenticated CRUD on vendor config; inject script payloads.
- Confirm execution in first-party origin.

## 3. Masking asymmetry IDOR
- For sequential ids, diff GET vs PUT/PATCH/POST bodies.
- Brute ±id without auth; flag fields that unmask on write echo.

## 4. Mobile hardcoded crypto
- Unpack APK/IPA; extract keys; decrypt startup config downloads.
- Fail if production private keys / master secrets appear.

## 5. AI harness ops
- Scope enforcement at egress proxy, not prompt.
- Direct provider API; RAG + helpers; human-only report review.
