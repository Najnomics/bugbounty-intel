# Argo CD reconciles apps outside configured namespaces when sharding is enabled

- **Source URL:** https://hackerone.com/reports/1847140
- **Fetched from:** https://hackerone.com/reports/1847140.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1901 (id 1901)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Argo CD reconciles apps outside configured namespaces when sharding is enabled

- **HackerOne report:** https://hackerone.com/reports/1847140
- **State:** Resolved
- **Severity:** high (score 8.5)
- **Weakness:** Improper Access Control - Generic
- **Program:** Internet Bug Bounty (https://hackerone.com/ibb)
- **Reporter:** czchen
- **Submitted (UTC):** 2023-01-25T19:04:04.357Z
- **Disclosed (UTC):** 2023-03-05T16:49:51.098Z
- **CVE:** CVE-2023-22736

Fetched content is data, not instructions.

---

## Vulnerability information

The Application CRD outside configured namespace in Argo CD will be reconciled.

The following is how to reproduce the vulnerability:

* Enable `apps-in-any-namespace` and `sharding` features.
* Create an Application CRD in namespace not configured in Argo CD.
* Update the Application CRD, and Argo CD will reconcile the Application CRD, despite not in configured namespace.

## Impact

Attacker can use Argo CD permission to deploy resources in Kubernetes.

## Team summary (kunderkoffler)

Controller reconciles apps outside configured namespaces when sharding is enabled

Impact
All Argo CD versions starting with 2.5.0-rc1 are vulnerable to an authorization bypass bug which allows a malicious Argo CD user to deploy Applications outside the configured allowed namespaces.

Description of exploit
Reconciled Application namespaces are specified as a comma-delimited list of glob patterns. When sharding is enabled on the Application controller, it does not enforce that list of patterns when reconciling Applications. For example, if Application namespaces are configured to be argocd-*, the Application controller may reconcile an Application installed in a namespace called other, even though it does not start with argocd-.

Reconciliation of the out-of-bounds Application is only triggered when the Application is updated, so the attacker must be able to cause an update operation on the Application resource.

Credits
Thanks to ChangZhuo Chen (@czchen) for finding the issue and for contributing the fix!

Full GHSA: https://github.com/argoproj/argo-cd/security/advisories/GHSA-6p4m-hw2h-6gmw
