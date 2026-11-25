# Meet Acurist

- **Source URL:** https://imapurbo.medium.com/meet-acurist-a-terminal-native-ai-agent-built-for-offensive-security-cc4b6eb09376
- **Fetched from:** https://imapurbo.medium.com/meet-acurist-a-terminal-native-ai-agent-built-for-offensive-security-cc4b6eb09376?source=rss-93abe504dc38------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14936 (id 14936)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** IMApurbo / Mon, 05 Oct 2026 18:13:19 GMT

*An open-source, vendor-agnostic agent for bug bounty hunters, red teamers, and security researchers*

If you’ve spent any time in offensive security, you know the rhythm: run a scan, wait, parse the output, pivot, repeat. Most of that loop is mechanical. The interesting part, the thinking, gets buried under tool juggling and terminal tabs.

[*Acurist*](https://github.com/IMApurbo/acurist) is an open-source project that tries to fix that. It’s a terminal-native, autonomous AI agent designed specifically for offensive security workflows: reconnaissance, exploit development, and security auditing. If you’ve used Claude Code, the interface will feel familiar. The difference is that Acurist is built for the pentester’s toolbox and isn’t tied to any single model vendor.

What Is [Acurist](https://github.com/IMApurbo/acurist)?

[*Acurist*](https://github.com/IMApurbo/acurist) gives you a scrolling transcript, live tool-execution tracking, automatic process backgrounding, and human-in-the-loop controls, all inside your terminal. You describe what you want in plain language, and the agent plans the steps, runs the security binaries, and processes the output.

It connects to any OpenAI- or Anthropic-compatible endpoint. That includes local setups like Ollama, LM Studio, and vLLM, hosted providers like DeepSeek, and custom proxies. Point it at a local model and you can run assessments fully offline.

Key Capabilities

Getting Started

[*Acurist*](https://github.com/IMApurbo/acurist) needs Node.js v22 or higher and an inference backend. By default it looks for an endpoint at [http://localhost:8765](http://localhost:8765). Installation is a single command:

npm install -g acurist@latest

Then launch it with a local model. For example, with Ollama running a coding model:

ACURIST\_PROXY=http://localhost:11434 \

ACURIST\_MODEL=qwen2.5-coder:32b acurist

Prefer to approve every shell command before it runs? Start in manual mode. You can also begin with a specific persona:

acurist --mode manual

acurist --agent bug-hunter

[*Acurist*](https://github.com/IMApurbo/acurist) also documents an integration with deeptunnel for routing requests to DeepSeek V3 or R1 through its web chat, with flags like — ds-model expert and — ds-think for deeper reasoning. If you go that route, check the terms of the service you’re connecting to and make sure the setup fits your own risk tolerance and engagement rules.

Watching It Work

The part I find most useful is how [*Acurist*](https://github.com/IMApurbo/acurist) handles long-running jobs. When you kick off a full-port nmap scan, it doesn’t freeze your session. It detaches the process, gives you a job ID, PID, and log path, and shows the first few seconds of output so you know it started correctly.

You stay in control with a few simple calls: force backgrounding with a settle delay, tail a job’s log, or kill it outright. That means you can keep recon running while you analyze results from an earlier scan.

Slash Commands for Fast Control

You can adjust the environment mid-session without restarting. Here are the commands you’ll use most:

The per-tool permission control is a thoughtful touch. You might let read-only recon tools run freely while requiring manual approval for anything that writes, exploits, or touches the network in a noisy way.

Under the Hood

The interface is built with Ink and React for terminal rendering, with real-time tool execution cards, a non-blocking process manager, and an input handler for slash commands and @mentions. It talks to your backend over the OpenAI or Anthropic protocol, so any server exposing /v1/models and /v1/messages will work.

A Note on Responsible Use

Tools like this are powerful, and the project is clear about its purpose: authorized penetration testing, vulnerability assessment, and education. Only test systems you own or have explicit written permission to assess. Keep a human in the loop for anything consequential, and use manual mode when the scope is tight. An autonomous agent will happily do exactly what you ask, so scope and authorization are your responsibility.

Final Thoughts

AI agents are quickly becoming part of the security researcher’s toolkit, and the ability to run them locally and swap models freely is a real advantage for privacy-sensitive work. [*Acurist*](https://github.com/IMApurbo/acurist) is a young project, but its focus on backgrounding, per-tool permissions, and offline operation shows it was designed around how pentesters actually work.

If you try it out, I’d love to hear how it fits into your workflow. The project is open source under the MIT License, and contributions are welcome on GitHub.

Repository: [github.com/IMApurbo/acurist](https://github.com/IMApurbo/acurist) | [Install](https://www.npmjs.com/package/acurist): npm install -g acurist
