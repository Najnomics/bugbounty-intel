# How I Use the DeFi Watchdog Unified Security API to Secure Smart Contracts (Part 1)

- **Source URL:** https://medium.com/@charingane/how-i-use-the-defi-watchdog-unified-security-api-to-secure-smart-contracts-part-1-357f424efe98?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821171748/https://medium.com/@charingane/how-i-use-the-defi-watchdog-unified-security-api-to-secure-smart-contracts-part-1-357f424efe98
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10242 (id 10242)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Use the DeFi Watchdog Unified Security API to Secure Smart Contracts (Part 1)

# Introduction

If you’ve shipped smart contracts, you know security isn’t optional. One overlooked bug or unchecked edge case, and you might lose funds or your project’s reputation. As someone who’s worked with a lot of security tools, I wanted something better: a unified API that lets me scan contracts with multiple industry-standard analyzers, without juggling five different UIs or scripts.

That’s exactly what [DeFi Watchdog Unified Security API](https://defi-watchdog.com/) delivers. In this two-part guide, I’ll show how I use this API in real-world audits — covering everything from the first cURL call to integrating it into my dev workflow. In **Part 1** (this post), we’ll focus on setup, main endpoints, and practical code samples.

# Why a Unified Security API?

I’ve lost track of how many times I’ve bounced between **Slither**, **Mythril**, **Semgrep**, and others — sometimes just to double-check a finding or compare outputs. The DeFi Watchdog Unified Security API puts all these under one REST interface, letting you scan Solidity code with as many tools as you want, and get normalized results in a single response.

For solo devs, auditors, or even teams building continuous integration pipelines, this API is a big time-saver.

# Quick Look: What’s Supported

**Tools available (run any or all):**

- Slither
- Mythril
- Manticore
- Semgrep
- Oyente

API Base URL: [http://api.defi-watchdog.com:5001](http://89.147.103.119:5001)**No API key required** (for now — this might change in future versions).

# The Endpoints You’ll Actually Use

I like docs that get straight to the point. Here are the endpoints I use most:

```
+-----------+--------------------+-------------------------------------------------------+
|        Endpoint       |   Method    |                    What it does                  |
+-----------+--------------------+-------------------------------------------------------+
| /health               |    GET      | See if the API is live and which tools are up    |
| /api/tools            |    GET      | Get details about each analysis tool             |
| /api/analyze          |    POST     | Analyze a contract with several tools            |
| /api/analyze/{tool}   |    POST     | Analyze a contract with just one tool            |
+-----------+--------------------+-------------------------------------------------------+
```
# Step 1: Check If the API Is Online

Before running anything serious, I always ping the health endpoint:

`curl -X GET http://api.defi-watchdog.com:5001/health`
You’ll get a JSON like:

```
{
  "status": "healthy",
  "service": "DeFi Watchdog Unified Security API",
  "version": "2.0.0",
  "available_tools": ["slither", "mythril", "manticore", "semgrep", "oyente"],
  "timestamp": "2025-07-17T15:37:00Z"
}
```
If any tool is down, it’ll drop from `available_tools`.

# Step 2: See Which Tools Are Available (and Fastest)

The `/api/tools` endpoint gives me a breakdown of versions, features, and expected runtime for each tool.

`curl -X GET http://api.defi-watchdog.com:5001/api/tools`
This is useful if I want a quick scan (Slither/Semgrep take 2–15s), or if I’m okay with waiting longer for deep analysis (Mythril/Manticore can take a few minutes).

# Step 3: Analyzing a Smart Contract

**This is where the magic happens.**I send my Solidity source code as a JSON payload. You can ask the API to run all tools, or just a subset.

Example: Analyze With Slither and Semgrep (Fast!)


```
curl -X POST http://api.defi-watchdog.com:5001/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "sourceCode": "pragma solidity ^0.8.0;\ncontract Test { uint value; }",
    "tools": ["slither", "semgrep"]
  }'
```
Example: Full Analysis (All Tools)


Just leave out the `"tools"` field:

```
curl -X POST http://api.defi-watchdog.com:5001/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"sourceCode": "pragma solidity ^0.8.0;\ncontract Test { ... }"}'
```
The response contains a summary, unified findings, and per-tool details. Here’s a real excerpt:

```
{
    "findings": [
        {
            "confidence": "Medium",
            "description": "VulnerableVault.emergencyWithdraw() (Contract.sol#22-25) sends eth to arbitrary user\n\tDangerous calls:\n\t- address(owner).transfer(address(this).balance) (Contract.sol#24)\n",
            "detector_id": "arbitrary-send-eth",
            "elements": [
                "emergencyWithdraw at lines 22-25",
                "address(owner).transfer(address(this).balance) at lines 24-24"
            ],
            "severity": "HIGH",
            "title": "arbitrary-send-eth",
            "tool": "Slither"
        },
        {
            "confidence": "Medium",
            "description": "Reentrancy in VulnerableVault.withdraw(uint256) (Contract.sol#15-20):\n\tExternal calls:\n\t- (success,None) = msg.sender.call{value: amount}() (Contract.sol#17)\n\tState variables written after the call(s):\n\t- balances[msg.sender] -= amount (Contract.sol#19)\n\tVulnerableVault.balances (Contract.sol#4) can be used in cross function reentrancies:\n\t- VulnerableVault.balances (Contract.sol#4)\n\t- VulnerableVault.deposit() (Contract.sol#11-13)\n\t- VulnerableVault.withdraw(uint256) (Contract.sol#15-20)\n",
            "detector_id": "reentrancy-eth",
            "elements": [
                "withdraw at lines 15-20",
                "(success,None) = msg.sender.call{value: amount}() at lines 17-17",
                "balances[msg.sender] -= amount at lines 19-19"
            ],
            "severity": "HIGH",
            "title": "reentrancy-eth",
            "tool": "Slither"
        },
        {
            "confidence": "Medium",
            "description": "VulnerableVault.emergencyWithdraw() (Contract.sol#22-25) uses tx.origin for authorization: require(bool)(tx.origin == owner) (Contract.sol#23)\n",
            "detector_id": "tx-origin",
            "elements": [
                "emergencyWithdraw at lines 22-25",
                "require(bool)(tx.origin == owner) at lines 23-23"
            ],
            "severity": "MEDIUM",
            "title": "tx-origin",
            "tool": "Slither"
        },
        {
            "confidence": "High",
            "description": "Version constraint ^0.8.0 contains known severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)\n\t- FullInlinerNonExpressionSplitArgumentEvaluationOrder\n\t- MissingSideEffectsOnSelectorAccess\n\t- AbiReencodingHeadOverflowWithStaticArrayCleanup\n\t- DirtyBytesArrayToStorage\n\t- DataLocationChangeInInternalOverride\n\t- NestedCalldataArrayAbiReencodingSizeValidation\n\t- SignedImmutables\n\t- ABIDecodeTwoDimensionalArrayMemory\n\t- KeccakCaching.\nIt is used by:\n\t- ^0.8.0 (Contract.sol#1)\n",
            "detector_id": "solc-version",
            "elements": [
                "^0.8.0 at lines 1-1"
            ],
            "severity": "INFO",
            "title": "solc-version",
            "tool": "Slither"
        },
        {
            "confidence": "High",
            "description": "Low level call in VulnerableVault.withdraw(uint256) (Contract.sol#15-20):\n\t- (success,None) = msg.sender.call{value: amount}() (Contract.sol#17)\n",
            "detector_id": "low-level-calls",
            "elements": [
                "withdraw at lines 15-20",
                "(success,None) = msg.sender.call{value: amount}() at lines 17-17"
            ],
            "severity": "INFO",
            "title": "low-level-calls",
            "tool": "Slither"
        },
        {
            "confidence": "High",
            "description": "VulnerableVault.owner (Contract.sol#5) should be immutable \n",
            "detector_id": "immutable-states",
            "elements": [
                "owner at lines 5-5"
            ],
            "severity": "MEDIUM",
            "title": "immutable-states",
            "tool": "Slither"
        }
    ],
    "success": true,
    "summary": {
        "critical": 0,
        "execution_time": "2025-07-17T17:26:01.232640",
        "high": 2,
        "info": 2,
        "low": 0,
        "medium": 2,
        "security_score": 60,
        "tools_run": [
            "slither",
            "mythril"
        ],
        "total_findings": 6
    },
    "tools_results": {
        "mythril": {
            "findings": [],
            "metadata": {
                "execution_time": "2025-07-17T17:26:01.231790",
                "version": ""
            },
            "success": true
        },
        "slither": {
            "findings": [
                {
                    "confidence": "Medium",
                    "description": "VulnerableVault.emergencyWithdraw() (Contract.sol#22-25) sends eth to arbitrary user\n\tDangerous calls:\n\t- address(owner).transfer(address(this).balance) (Contract.sol#24)\n",
                    "detector_id": "arbitrary-send-eth",
                    "elements": [
                        "emergencyWithdraw at lines 22-25",
                        "address(owner).transfer(address(this).balance) at lines 24-24"
                    ],
                    "severity": "HIGH",
                    "title": "arbitrary-send-eth",
                    "tool": "Slither"
                },
                {
                    "confidence": "Medium",
                    "description": "Reentrancy in VulnerableVault.withdraw(uint256) (Contract.sol#15-20):\n\tExternal calls:\n\t- (success,None) = msg.sender.call{value: amount}() (Contract.sol#17)\n\tState variables written after the call(s):\n\t- balances[msg.sender] -= amount (Contract.sol#19)\n\tVulnerableVault.balances (Contract.sol#4) can be used in cross function reentrancies:\n\t- VulnerableVault.balances (Contract.sol#4)\n\t- VulnerableVault.deposit() (Contract.sol#11-13)\n\t- VulnerableVault.withdraw(uint256) (Contract.sol#15-20)\n",
                    "detector_id": "reentrancy-eth",
                    "elements": [
                        "withdraw at lines 15-20",
                        "(success,None) = msg.sender.call{value: amount}() at lines 17-17",
                        "balances[msg.sender] -= amount at lines 19-19"
                    ],
                    "severity": "HIGH",
                    "title": "reentrancy-eth",
                    "tool": "Slither"
                },
                {
                    "confidence": "Medium",
                    "description": "VulnerableVault.emergencyWithdraw() (Contract.sol#22-25) uses tx.origin for authorization: require(bool)(tx.origin == owner) (Contract.sol#23)\n",
                    "detector_id": "tx-origin",
                    "elements": [
                        "emergencyWithdraw at lines 22-25",
                        "require(bool)(tx.origin == owner) at lines 23-23"
                    ],
                    "severity": "MEDIUM",
                    "title": "tx-origin",
                    "tool": "Slither"
                },
                {
                    "confidence": "High",
                    "description": "Version constraint ^0.8.0 contains known severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)\n\t- FullInlinerNonExpressionSplitArgumentEvaluationOrder\n\t- MissingSideEffectsOnSelectorAccess\n\t- AbiReencodingHeadOverflowWithStaticArrayCleanup\n\t- DirtyBytesArrayToStorage\n\t- DataLocationChangeInInternalOverride\n\t- NestedCalldataArrayAbiReencodingSizeValidation\n\t- SignedImmutables\n\t- ABIDecodeTwoDimensionalArrayMemory\n\t- KeccakCaching.\nIt is used by:\n\t- ^0.8.0 (Contract.sol#1)\n",
                    "detector_id": "solc-version",
                    "elements": [
                        "^0.8.0 at lines 1-1"
                    ],
                    "severity": "INFO",
                    "title": "solc-version",
                    "tool": "Slither"
                },
                {
                    "confidence": "High",
                    "description": "Low level call in VulnerableVault.withdraw(uint256) (Contract.sol#15-20):\n\t- (success,None) = msg.sender.call{value: amount}() (Contract.sol#17)\n",
                    "detector_id": "low-level-calls",
                    "elements": [
                        "withdraw at lines 15-20",
                        "(success,None) = msg.sender.call{value: amount}() at lines 17-17"
                    ],
                    "severity": "INFO",
                    "title": "low-level-calls",
                    "tool": "Slither"
                },
                {
                    "confidence": "High",
                    "description": "VulnerableVault.owner (Contract.sol#5) should be immutable \n",
                    "detector_id": "immutable-states",
                    "elements": [
                        "owner at lines 5-5"
                    ],
                    "severity": "MEDIUM",
                    "title": "immutable-states",
                    "tool": "Slither"
                }
            ],
            "metadata": {
                "execution_time": "2025-07-17T17:25:57.468471",
                "version": "0.11.3"
            },
            "success": true
        }
    }
}
```
# How I Integrate This in My Workflow

You can call the API from any language. Here are Python and Node.js examples I actually use:

```
# Python
import requests
contract = """
pragma solidity ^0.8.0;
contract Example {
    mapping(address => uint256) public balances;
    function withdraw() public {
        uint256 amount = balances[msg.sender];
        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
        balances[msg.sender] = 0;
    }
}
"""
res = requests.post(
    "http://api.defi-watchdog.com:5001/api/analyze",
    json={"sourceCode": contract, "tools": ["slither", "semgrep"]}
)
print(res.json())
```
```
const axios = require('axios');
const contract = `
pragma solidity ^0.8.0;
contract Example {
    mapping(address => uint256) public balances;
    function withdraw() public {
        uint256 amount = balances[msg.sender];
        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
        balances[msg.sender] = 0;
    }
}
`;
axios.post('http://api.defi-watchdog.com:5001/api/analyze', {
    sourceCode: contract,
    tools: ['slither', 'semgrep']
}).then(res => {
    console.log(res.data);
});
```
# Pro Tips for Fast, Useful Results

- For most contract updates, I use just Slither + Semgrep for a sub-20-second check.
- For production releases, I run all tools (expect up to 5 minutes).
- If you hit a timeout or a tool is down, retry with fewer tools or check `/health`.
- If you get lots of findings, prioritize **HIGH** and **CRITICAL** first.

# What’s Next

In **Part 2**, I’ll dive deep into each analysis tool, show how severity and security scores work, and share my approach to optimizing analysis time and interpreting tricky findings.

You like? leave claps 👏

Have questions or want to see specific integrations? Leave a comment!👇

# Links :

⛓️Website: [https://defi-watchdog.com/](https://defi-watchdog.com/)

⛓️Twitter: [https://x.com/watchdog\_defi](https://x.com/watchdog_defi)
