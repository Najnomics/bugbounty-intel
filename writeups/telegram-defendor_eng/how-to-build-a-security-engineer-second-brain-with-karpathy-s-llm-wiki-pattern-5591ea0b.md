# 💡 Security Tip: Build a Security Engineer Second Brain

- **Source URL:** https://labs.secengai.com/p/how-to-build-a-security-engineer-second-brain-with-karpathy-s-llm-wiki-pattern
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1797 (id 1797)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**TL;DR:** Andrej Karpathy published a pattern for building personal knowledge bases with LLMs instead of RAG This guide adapts it for security engineering Ingest pentest reports, incident logs, bug writeups, and terminal output with one command Query everything you ever learned from any project directory

Knowledge base in Graph view

## The Problem Every Security Engineer Has

You open 50 browser tabs researching a CVE, close the browser, and one week later, you can't find a single note

Documentation end up spread across five different projects. A month passes, the doc exists somewhere, but where? And then there's the deja vu: solving the same attack pattern for the third time across three separate projects, starting from scratch each time

Every knowledge base tool either needs a vector database, a RAG pipeline, or difficult to setup

Skill flow

## Why Karpathy's LLM Wiki Pattern Is Different

Andrej Karpathy described this pattern in his LLM Wiki project Instead of RAG, the approach is direct context loading: the LLM reads the relevant wiki pages at query time

Benefits for security engineers:

- Easier to add notes and knowledge without complex setup
- Easier to find and query any information you've saved
- Easier to read and access your notes from anywhere

## Security Engineer Use Cases

These are the use cases that matter for security engineers:

- Pull IoCs, attack patterns, and remediation steps straight from pentest reports and CVE advisories
- Query incident timelines and root causes months later without digging through Slack threads
- Extract exploitation patterns from bug bounty writeups and tag them by technique
- Find that one-liner command you ran 1 week ago from indexed terminal logs and command history
- Search across every project you ever worked on from a single query

## Prerequisites

- [Obsidian](https://obsidian.md) installed (any recent version)
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured
- [obsidian-wiki skills](https://github.com/Ar9av/obsidian-wiki) repository
- Optional: [Defuddle](https://github.com/kepano/defuddle) for better website content extraction

## Full Setup Guide

### Step 1: Clone and Install

**Command:** Send below command to terminal

```
git clone https://github.com/Ar9av/obsidian-wiki.git
cd obsidian-wiki
bash setup.sh
```
### Step 2: Configure the Vault

**Command:** Send below command to terminal

```
cp .env.example .env
mkdir ~/llm-wiki
```
Open `.env` and set the vault path:

`OBSIDIAN_VAULT_PATH=/path/to/your/llm-wiki`
Replace `/path/to/your/` with the actual path

### Step 3: Initialize the Wiki

Open Claude Code inside the repository directory

**Prompt:** Send below prompt to Claude Code

`Set up my wiki`
This reads the repository configuration and creates the initial wiki structure: index pages, category folders, and cross-link templates

### Step 4: Symlink Skills to Global

**Command:** Send below command to terminal

```
ln -s "$PWD/.skills/wiki-ingest" ~/.claude/skills/wiki-ingest
ln -s "$PWD/.skills/ingest-url" ~/.claude/skills/ingest-url
ln -s "$PWD/.skills/wiki-query" ~/.claude/skills/wiki-query
ln -s "$PWD/.skills/daily-update" ~/.claude/skills/daily-update
```
Without symlinks, the skills only function inside the `obsidian-wiki` repo folder

## The Core Skills

| Skill | Command | What it does | 
|---|---|---|
| **Ingest anything** | `/wiki-ingest "<prompt>"` | Takes any document, distills knowledge into wiki pages, cross-links related content | 
| **Ingest URL** | `/ingest-url <url>` | Pulls any article, advisory, or writeup directly into the wiki | 
| **Query everything** | `/wiki-query "<question>"` | Answers questions using everything ever ingested | 
| **Daily maintenance** | `/daily-update` | Runs freshness checks, cross-linking, index updates | 

## Demo: Ingestion

### Ingest a CVE Advisory from the Web

**Prompt:** Send below prompt to Claude Code

`/ingest-url https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854`
Ingesting a url

The skill fetches the page, extracts the vulnerability details, affected versions, and remediation steps The skill creates wiki pages for the CVE, the attack technique, and links them to existing entries if any exist

### Ingest a PDF Incident Report

**Prompt:** Send below prompt to Claude Code

`/wiki-ingest "@Bybit Incident Investigation - Preliminary Report v1.0.pdf"`
Ingesting pdf

The skill ingests the PDF and extracts the incident timeline, root cause, and attack chain Each piece gets its own wiki page

Source: [Verichains Public Audit Reports](https://github.com/verichains/public-audit-reports/tree/main)

### Add Inline Knowledge

**Prompt:** Send below prompt to Claude Code

`/wiki-ingest Create a note about production-web-01 server. It's at 10.0.1.50, runs Ubuntu 22.04, owned by the Platform team, admin contact is` [\[email protected\]](https://labs.secengai.com/cdn-cgi/l/email-protection), and it hosts the customer portal
No file needed Type the knowledge directly The skill structures it into a wiki page with frontmatter and links

## Demo: Querying

### Query for CVE Details

**Prompt:** Send below prompt to Claude Code

`/wiki-query What do I know about the GitHub RCE vulnerability?`
Returns: CVE number, affected versions, attack vector, remediation steps (pulled from the advisory ingested earlier)

### Query for Incident Patterns

**Prompt:** Send below prompt to Claude Code

`/wiki-query get the ioc from bybit incident`
Querying information from Knowledge base

Returns: The attack chain, compromised keys, and timeline from the PDF report ingested earlier

### Query for Service Owner Mapping

**Prompt:** Send below prompt to Claude Code

`/wiki-query Show me service owner and infrastructure mapping of production-web-01`
Returns: Server names, IP addresses, owning teams, and admin contacts added via the inline knowledge entry

## Follow-Up Prompts

### Save a Conversation

**Prompt:** Send below prompt to Claude Code

`/wiki-capture`
This stores the current Claude Code conversation into the knowledge base Useful when a debugging session or analysis produced insights worth keeping

## Further Improvements

- **QMD semantic search** — Adds semantic search on top of the wiki Useful when the vault grows past 200+ pages [Setup guide](https://github.com/Ar9av/obsidian-wiki/tree/main#optional-qmd-semantic-search)
- **MarkItDown for PDF parsing** — Better PDF extraction than the default Microsoft's library handles tables and formatted content well [GitHub](https://github.com/microsoft/markitdown)
- **Graph colorize** — Colors the Obsidian graph view by category Helps visualize knowledge clusters Run `/graph-colorize` inside Claude Code

Note: Swap any tools or adjust skills to match your setup The system is plain markdown with no lock-in

## Conclusion

Adding knowledge to your second brain is now as easy as typing a sentence or dropping a file No more wrestling with RAG pipelines, vector databases, or complex setups Just ingest and query, the knowledge stays and grows with every use

## Further Reading

**MCP Servers:**

- [Tavily MCP](https://github.com/tavily-ai/tavily-mcp) — Web search and research
- [DeepWiki MCP](https://docs.devin.ai/work-with-devin/deepwiki-mcp) — GitHub repository documentation
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) — Browser automation
- [Burp Suite MCP](https://github.com/PortSwigger/mcp-server) — Security testing integration
- [Basic Memory](https://github.com/basicmachines-co/basic-memory) — Alternative knowledge management

**Skills & Agents:**

- [security-code-audit-skills](https://github.com/mfakbar127/security-code-audit-skills) — Code review use cases
- [Trail of Bits Skills](https://github.com/trailofbits/skills) — Security review skills
- [General Purpose Agents](https://github.com/wshobson/agents) — Agent templates

**Config Management:**

- [Claude Samurai](https://github.com/mfakbar127/Claude-Samurai) — Visual configuration manager for Claude Code

**Ready to apply AI to your Security Engineering ?**

[Subscribe to Secengai Newsletter](https://labs.secengai.com/) for weekly actionable content on AI for security engineers

### Disclaimer

*This content reflects personal views, experiments, and use cases in AI and security engineering. It does not represent any employer's positions, policies, or practices.*
