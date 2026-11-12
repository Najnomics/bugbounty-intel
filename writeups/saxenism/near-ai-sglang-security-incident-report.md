# near-ai-sglang-security-incident-report

- **Source URL:** https://near.ai/blog/security-incident-report-sglang-vulnerability
- **Fetched:** 2026-11-12
- **Researcher:** saxenism
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

[← All articles](/blog)

# Security Incident Report

NEAR AI recently identified and contained unauthorized access to part of its infrastructure. The access has been closed, affected credentials have been replaced, the vulnerability that allowed it has been fixed, and access to NEAR AI Cloud has been restored.

## What was affected

The unauthorized party exploited a remote code execution vulnerability in SGLang, the open-source inference engine running on our servers. This gave them code execution on one inference server and, from there, access to our infrastructure.

Our investigation to date has confirmed that they then reached an internal system behind previously deprecated Private Chat and downloaded account details (email addresses, name, and for some accounts, plan and balance information) for approximately 100 users. Additionally, there was access to 18 agents on a legacy deployment of NEAR AI Agents which were not running in NEAR AI's confidential computing (TEE) environment. On November 8, they could also have observed user requests being processed on the accessed server, including requests running in confidential mode. We have found no indication that stored Private Chat conversation or uploaded files were accessed. For the 18 agents, the data retrieved included chat history, settings and logs. Two Cloud customers had NEAR AI Cloud API keys exposed in logs. Those keys have been revoked.

## What we did

On detection, we revoked all active sessions and administrative credentials, replaced all agent tokens, took Private Chat offline, and deployed a fix for the SGLang vulnerability across all inference servers. We've completed the rotation of all remaining credentials and a full forensic review. We have notified users whose account details or agents we have confirmed were accessed and will make any regulatory notifications that are required.

## Confidential inference

Confidential computing protects data from the operator and the host. It does not protect against a vulnerability in the software running inside the environment, and that is what happened here: the SGLang vulnerability let the party run code inside one inference server and access requests in processing on that server, including confidential ones. We have deployed a fix across all servers and reported the vulnerability to the SGLang project. We are now treating the inference software and the services around the enclave with the same rigor as the enclave itself when running security analysis, and the code, dependencies and deployment configurations for our confidential inference stack remain public so that anyone can verify what is running.

Affected users have been contacted directly from [security@near.ai](mailto:security@near.ai) with the steps that apply to them. As a precaution, treat unsolicited messages referencing your account or balance with caution. The 18 agent owners have been contacted individually with the steps that apply to them.

Questions: [security@near.ai](mailto:security@near.ai).
