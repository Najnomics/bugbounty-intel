# How to perform dynamic analysis of a smart contract with Myth

- **Source URL:** https://medium.com/@bugbountydegen/how-to-perform-dynamic-analysis-of-a-smart-contract-with-myth-e80fb9351c85?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126144042/https://medium.com/@bugbountydegen/how-to-perform-dynamic-analysis-of-a-smart-contract-with-myth-e80fb9351c85
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3753 (id 3753)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to perform dynamic analysis of a smart contract with Myth

Myth is a powerful tool to find vulnerabilities in smart contracts, learn how to use it.

**Myth** is a tool developed by **Consensys** that does dynamic analysis of a Solidity smart contract. It has a paid version called **MythX** and a free version called **Mythril**. We will check out how to use the latter in this post.

If you just want to scan on-chain contracts online without installing mythril in your system, you can try my [free on-chain scanner](https://securitydegen.com/)

A prerequisite is that you have already installed in your system **solc** (the Solidity compiler).

After that, we already can install **Myth** in our system:

`# pip3 install mythril`
After the install, just check version to validate that everything is fine:

```
# myth version
Mythril version v0.23.10
```
## Basic usage:

## Local directory analysis:

`myth analyze <file_path>`
## On-chain analysis:

`myth analyze -v 5 -a <ETHEREUM ADDRESS> --infura-id <INFURA API KEY>`
Advanced help options:

```
# myth help
usage: myth [-h] [-v LOG_LEVEL] {safe-functions,analyze,a,disassemble,d,list-detectors,read-storage,function-to-hash,hash-to-address,version,help} ...
Security analysis of Ethereum smart contracts
positional arguments:
  {safe-functions,analyze,a,disassemble,d,list-detectors,read-storage,function-to-hash,hash-to-address,version,help}
                        Commands
    safe-functions      Check functions which are completely safe using symbolic execution
    analyze (a)         Triggers the analysis of the smart contract
    disassemble (d)     Disassembles the smart contract
    list-detectors      Lists available detection modules
    read-storage        Retrieves storage slots from a given address through rpc
    function-to-hash    Returns the hash signature of the function
    hash-to-address     converts the hashes in the blockchain to ethereum address
    version             Outputs the version
optional arguments:
  -h, --help            show this help message and exit
  -v LOG_LEVEL          log level (0-5)
```
Command line options to analyse a smart contract:

```
# myth analyze --help
usage: myth analyze [-h] [--rpc HOST:PORT / ganache / infura-[network_name]] [--rpctls RPCTLS] [--infura-id INFURA_ID] [--solc-json SOLC_JSON] [--solv SOLV] [-c BYTECODE] [-f BYTECODEFILE]
                    [-a CONTRACT_ADDRESS] [--bin-runtime] [-o <text/markdown/json/jsonv2>] [-g GRAPH] [-j OUTPUT_FILE] [-m MODULES] [--max-depth MAX_DEPTH] [--call-depth-limit CALL_DEPTH_LIMIT]
                    [--strategy {dfs,bfs,naive-random,weighted-random}] [--transaction-sequences TRANSACTION_SEQUENCES] [--beam-search BEAM_SEARCH] [-b N] [-t TRANSACTION_COUNT]
                    [--execution-timeout EXECUTION_TIMEOUT] [--solver-timeout SOLVER_TIMEOUT] [--create-timeout CREATE_TIMEOUT] [--parallel-solving] [--solver-log SOLVER_LOG] [--no-onchain-data]
                    [--pruning-factor PRUNING_FACTOR] [--unconstrained-storage] [--phrack] [--enable-physics] [-q] [--enable-iprof] [--disable-dependency-pruning] [--enable-coverage-strategy]
                    [--custom-modules-directory CUSTOM_MODULES_DIRECTORY] [--attacker-address ATTACKER_ADDRESS] [--creator-address CREATOR_ADDRESS]
                    [solidity_files ...]
positional arguments:
  solidity_files        Inputs file name and contract name.
                        usage: file1.sol:OptionalContractName file2.sol file3.sol:OptionalContractName
optional arguments:
  -h, --help            show this help message and exit
  --rpc HOST:PORT / ganache / infura-[network_name]
                        custom RPC settings
  --rpctls RPCTLS       RPC connection over TLS
  --infura-id INFURA_ID
                        set infura id for onchain analysis
  --solc-json SOLC_JSON
                        Json for the optional 'settings' parameter of solc's standard-json input
  --solv SOLV           specify solidity compiler version. If not present, will try to install it (Experimental)
  -c BYTECODE, --code BYTECODE
                        hex-encoded bytecode string ("6060604052...")
  -f BYTECODEFILE, --codefile BYTECODEFILE
                        file containing hex-encoded bytecode string
  -a CONTRACT_ADDRESS, --address CONTRACT_ADDRESS
                        pull contract from the blockchain
  --bin-runtime         Only when -c or -f is used. Consider the input bytecode as binary runtime code, default being the contract creation bytecode.
  -o <text/markdown/json/jsonv2>, --outform <text/markdown/json/jsonv2>
                        report output format
commands:
  -g GRAPH, --graph GRAPH
                        generate a control flow graph
  -j OUTPUT_FILE, --statespace-json OUTPUT_FILE
                        dumps the statespace json
options:
  -m MODULES, --modules MODULES
                        Comma-separated list of security analysis modules
  --max-depth MAX_DEPTH
                        Maximum recursion depth for symbolic execution
  --call-depth-limit CALL_DEPTH_LIMIT
                        Maximum call depth limit for symbolic execution
  --strategy {dfs,bfs,naive-random,weighted-random}
                        Symbolic execution strategy
  --transaction-sequences TRANSACTION_SEQUENCES
                        The possible transaction sequences to be executed. Like [[func_hash1, func_hash2], [func_hash2, func_hash3]] where for the first transaction is constrained with func_hash1 and func_hash2, and the second tx is constrained with func_hash2 and func_hash3
  --beam-search BEAM_SEARCH
                        Beam search with with
  -b N, --loop-bound N  Bound loops at n iterations
  -t TRANSACTION_COUNT, --transaction-count TRANSACTION_COUNT
                        Maximum number of transactions issued by laser
  --execution-timeout EXECUTION_TIMEOUT
                        The amount of seconds to spend on symbolic execution
  --solver-timeout SOLVER_TIMEOUT
                        The maximum amount of time(in milli seconds) the solver spends for queries from analysis modules
  --create-timeout CREATE_TIMEOUT
                        The amount of seconds to spend on the initial contract creation
  --parallel-solving    Enable solving z3 queries in parallel
  --solver-log SOLVER_LOG
                        Path to the directory for solver log
  --no-onchain-data     Don't attempt to retrieve contract code, variables and balances from the blockchain
  --pruning-factor PRUNING_FACTOR
                        Checks for reachability at the rate of <pruning-factor> (range 0-1.0). Where 1.0 would mean checking for every execution
  --unconstrained-storage
                        Default storage value is symbolic, turns off the on-chain storage loading
  --phrack              Phrack-style call graph
  --enable-physics      enable graph physics simulation
  -q, --query-signature
                        Lookup function signatures through www.4byte.directory
  --enable-iprof        enable the instruction profiler
  --disable-dependency-pruning
                        Deactivate dependency-based pruning
  --enable-coverage-strategy
                        enable coverage based search strategy
  --custom-modules-directory CUSTOM_MODULES_DIRECTORY
                        designates a separate directory to search for custom analysis modules
  --attacker-address ATTACKER_ADDRESS
                        Designates a specific attacker address to use during analysis
  --creator-address CREATOR_ADDRESS
                        Designates a specific creator address to use during analysis
```
## Bonus track: How to resolve the @openzeppelin dependency error

If you experience some problems with the @openzeppelin dependencies like this:

```
mythril.interfaces.cli [ERROR]: Solc experienced a fatal error.
ParserError: Source "@openzeppelin/contracts/token/PRC20/PRC20.sol" not found: File not found. Searched the following locations: "".
--> <file_path>:1:1:
|
1 | import "@openzeppelin/contracts/token/PRC20/PRC20.sol";
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
Use the following file **remappings.json** to fix the problem:

```
{
"remappings": [ "@openzeppelin/contracts/token/PRC20/=node_modules/PRC20" ],
}
```
With the following command line to resolve the dependency:

`myth analyze {file_path} --solc-json remappings.json`
More info:

Follow me on Twitter: [@bugbountydegen](https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fmedium.com%2F%40bugbountydegen%2F&screen_name=bugbountydegen)

Boost your Web3 security alpha, try my [SecurityDegen](https://securitydegen.com/) on-chain scanner!
