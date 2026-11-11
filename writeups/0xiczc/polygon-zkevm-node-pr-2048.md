# polygon-zkevm-node-pr-2048

- **Source URL:** https://github.com/0xPolygonHermez/zkevm-node/pull/2048
- **Fetched:** 2026-11-11
- **Researcher:** 0xiczc
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

This repository was archived by the owner on Feb 17, 2025. It is now read-only.

## Repository navigation

# Remove claim txs - #2048

Merged

Merged

## [Remove claim txs](#top)#2048

## Conversation


**[tclemos](/tclemos)**
    
              approved these changes

[Apr 25, 2023](#pullrequestreview-1400411931)
                  


**[ARR552](/ARR552)**
    
              approved these changes

[Apr 26, 2023](#pullrequestreview-1401672568)
                  

[Psykepro](/Psykepro)pushed a commit that referenced this pull request

[May 4, 2023](#ref-commit-5256c40)
    

\* remove claim txs
\* fix tests
\* fix tests
\* fix tests
\* remove deposit\_count
\* fix query
\* fix query
---------
Co-authored-by: Thiago Lemos \<thiago@polygon.technology>

[ARR552](/ARR552)added a commit that referenced this pull request

[May 25, 2023](#ref-commit-ac3664d)
    

\* build(deps): bump github.com/urfave/cli/v2 from 2.24.3 to 2.24.4 ([#1670](https://github.com/0xPolygon/zkevm-node/pull/1670))
Bumps \[github.com/urfave/cli/v2\]([https://github.com/urfave/cli](https://github.com/urfave/cli)) from 2.24.3 to 2.24.4.
- \[Release notes\]([https://github.com/urfave/cli/releases](https://github.com/urfave/cli/releases))
- \[Changelog\]([https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md](https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md))
- \[Commits\]([urfave/cli@`v2.24.3...v2.24.4`](https://github.com/urfave/cli/compare/v2.24.3...v2.24.4))
---
updated-dependencies:
- dependency-name: github.com/urfave/cli/v2
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/rubenv/sql-migrate ([#1694](https://github.com/0xPolygon/zkevm-node/pull/1694))
Bumps \[github.com/rubenv/sql-migrate\]([https://github.com/rubenv/sql-migrate](https://github.com/rubenv/sql-migrate)) from 0.0.0-20211023115951-9f02b1e13857 to 1.3.1.
- \[Release notes\]([https://github.com/rubenv/sql-migrate/releases](https://github.com/rubenv/sql-migrate/releases))
- \[Commits\]([https://github.com/rubenv/sql-migrate/commits/v1.3.1](https://github.com/rubenv/sql-migrate/commits/v1.3.1))
---
updated-dependencies:
- dependency-name: github.com/rubenv/sql-migrate
  dependency-type: direct:production
  update-type: version-update:semver-major
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* get nonce from state ([#1710](https://github.com/0xPolygon/zkevm-node/pull/1710))
\* get nonce from state
\* foce block number
\* foce block number and nonce
\* build(deps): bump github.com/stretchr/testify from 1.8.1 to 1.8.2 ([#1713](https://github.com/0xPolygon/zkevm-node/pull/1713))
Bumps \[github.com/stretchr/testify\]([https://github.com/stretchr/testify](https://github.com/stretchr/testify)) from 1.8.1 to 1.8.2.
- \[Release notes\]([https://github.com/stretchr/testify/releases](https://github.com/stretchr/testify/releases))
- \[Commits\]([stretchr/testify@`v1.8.1...v1.8.2`](https://github.com/stretchr/testify/compare/v1.8.1...v1.8.2))
---
updated-dependencies:
- dependency-name: github.com/stretchr/testify
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/prometheus/common from 0.40.0 to 0.41.0 ([#1716](https://github.com/0xPolygon/zkevm-node/pull/1716))
Bumps \[github.com/prometheus/common\]([https://github.com/prometheus/common](https://github.com/prometheus/common)) from 0.40.0 to 0.41.0.
- \[Release notes\]([https://github.com/prometheus/common/releases](https://github.com/prometheus/common/releases))
- \[Commits\]([prometheus/common@`v0.40.0...v0.41.0`](https://github.com/prometheus/common/compare/v0.40.0...v0.41.0))
---
updated-dependencies:
- dependency-name: github.com/prometheus/common
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* test: adding e2e forced batches test.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* test: adding check if the forced batch is also being consolidated/verified.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: lint errors and unit tests
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* new public data ([#1719](https://github.com/0xPolygon/zkevm-node/pull/1719))
\* fix pool add tx ([#1721](https://github.com/0xPolygon/zkevm-node/pull/1721))
\* fix pool add tx
\* fix
\* fix mining reverted txs ([#1712](https://github.com/0xPolygon/zkevm-node/pull/1712))
\* add e2e tests to validate reverted txs
\* fix unsigned tx error handling and test
\* fix test ip
\* finish test
\* finish test
\* fix reverted errors when calling eth\_call
\* commenting test reverting on constructor
\* fix jsonrpc tests error handling
\* fix state unit tests prover url
\* fix state revert tests
---------
Co-authored-by: ToniRamirezM \<toni@iden3.com>
\* sequencer fixes ([#1724](https://github.com/0xPolygon/zkevm-node/pull/1724))
\* sequencer fixes
\* comment test
\* fix test
\* remove default fork id ([#1728](https://github.com/0xPolygon/zkevm-node/pull/1728))
\* fix ([#1727](https://github.com/0xPolygon/zkevm-node/pull/1727))
\* fix
\* remove maxSequenceSize
\* linter
\* fix forkID ([#1729](https://github.com/0xPolygon/zkevm-node/pull/1729))
\* fix forkID
\* linter
\* fix test
\* fix error handling in sequencer ([#1730](https://github.com/0xPolygon/zkevm-node/pull/1730))
\* fix error handling in sequencer
\* fix error log
\* fix error log
\* fix error log
\* fix test
\* fix test
\* fix ([#1735](https://github.com/0xPolygon/zkevm-node/pull/1735))
\* add check stateroot in reprocessfull ([#1739](https://github.com/0xPolygon/zkevm-node/pull/1739))
\* fix stateroot on first run ([#1740](https://github.com/0xPolygon/zkevm-node/pull/1740))
\* fix stateroot on first run
\* add check stateroot in reprocessfull
\* fix
\* Feature/release run docs ([#1725](https://github.com/0xPolygon/zkevm-node/pull/1725))
\* Update running prod docs, and public testnet config
\* update gopackr
\* update gopackr, without go mod tidy
\* fix tests ([#1733](https://github.com/0xPolygon/zkevm-node/pull/1733))
\* fix tests
\* fix: fixing unit tests.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: configs
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
---------
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
Co-authored-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* build(deps): bump golang.org/x/crypto from 0.6.0 to 0.7.0 ([#1751](https://github.com/0xPolygon/zkevm-node/pull/1751))
Bumps \[golang.org/x/crypto\]([https://github.com/golang/crypto](https://github.com/golang/crypto)) from 0.6.0 to 0.7.0.
- \[Release notes\]([https://github.com/golang/crypto/releases](https://github.com/golang/crypto/releases))
- \[Commits\]([golang/crypto@`v0.6.0...v0.7.0`](https://github.com/golang/crypto/compare/v0.6.0...v0.7.0))
---
updated-dependencies:
- dependency-name: golang.org/x/crypto
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* allow reverted tx to be added to the pool ([#1744](https://github.com/0xPolygon/zkevm-node/pull/1744))
\* build(deps): bump github.com/urfave/cli/v2 from 2.24.4 to 2.25.0 ([#1750](https://github.com/0xPolygon/zkevm-node/pull/1750))
Bumps \[github.com/urfave/cli/v2\]([https://github.com/urfave/cli](https://github.com/urfave/cli)) from 2.24.4 to 2.25.0.
- \[Release notes\]([https://github.com/urfave/cli/releases](https://github.com/urfave/cli/releases))
- \[Changelog\]([https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md](https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md))
- \[Commits\]([urfave/cli@`v2.24.4...v2.25.0`](https://github.com/urfave/cli/compare/v2.24.4...v2.25.0))
---
updated-dependencies:
- dependency-name: github.com/urfave/cli/v2
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/go-git/go-git/v5 from 5.4.2 to 5.6.0 ([#1714](https://github.com/0xPolygon/zkevm-node/pull/1714))
\* build(deps): bump github.com/go-git/go-git/v5 from 5.4.2 to 5.6.0
Bumps \[github.com/go-git/go-git/v5\]([https://github.com/go-git/go-git](https://github.com/go-git/go-git)) from 5.4.2 to 5.6.0.
- \[Release notes\]([https://github.com/go-git/go-git/releases](https://github.com/go-git/go-git/releases))
- \[Commits\]([go-git/go-git@`v5.4.2...v5.6.0`](https://github.com/go-git/go-git/compare/v5.4.2...v5.6.0))
---
updated-dependencies:
- dependency-name: github.com/go-git/go-git/v5
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
\* remove deprecated code
---------
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
Co-authored-by: tclemos \<thiago@iden3.com>
\* Fix/reorg pool ([#1756](https://github.com/0xPolygon/zkevm-node/pull/1756))
\* fix
\* fix check if reorg
\* fix finalizer test
\* New executor error: Balance Mismatch ([#1720](https://github.com/0xPolygon/zkevm-node/pull/1720))
\* new executor error
\* fix test
\* build(deps): bump github.com/spf13/afero from 1.9.4 to 1.9.5 ([#1757](https://github.com/0xPolygon/zkevm-node/pull/1757))
Bumps \[github.com/spf13/afero\]([https://github.com/spf13/afero](https://github.com/spf13/afero)) from 1.9.4 to 1.9.5.
- \[Release notes\]([https://github.com/spf13/afero/releases](https://github.com/spf13/afero/releases))
- \[Commits\]([spf13/afero@`v1.9.4...v1.9.5`](https://github.com/spf13/afero/compare/v1.9.4...v1.9.5))
---
updated-dependencies:
- dependency-name: github.com/spf13/afero
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Broadcast URI ([#1722](https://github.com/0xPolygon/zkevm-node/pull/1722))
\* Broadcast URI
\* fix synchronizer test
\* fix
\* check if reorg in sequencer
\* JRPC - debug methods review ([#1650](https://github.com/0xPolygon/zkevm-node/pull/1650))
\* Fix revert message for sc deployment tx reverted on the constructor ([#1737](https://github.com/0xPolygon/zkevm-node/pull/1737))
\* Change %w to %v in logs ([#1764](https://github.com/0xPolygon/zkevm-node/pull/1764))
\* build(deps): bump github.com/rubenv/sql-migrate from 1.3.1 to 1.4.0 ([#1769](https://github.com/0xPolygon/zkevm-node/pull/1769))
Bumps \[github.com/rubenv/sql-migrate\]([https://github.com/rubenv/sql-migrate](https://github.com/rubenv/sql-migrate)) from 1.3.1 to 1.4.0.
- \[Release notes\]([https://github.com/rubenv/sql-migrate/releases](https://github.com/rubenv/sql-migrate/releases))
- \[Commits\]([rubenv/sql-migrate@`v1.3.1...v1.4.0`](https://github.com/rubenv/sql-migrate/compare/v1.3.1...v1.4.0))
---
updated-dependencies:
- dependency-name: github.com/rubenv/sql-migrate
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* \[Aggregator\]  More fine-grained logs in case of prover errors ([#1718](https://github.com/0xPolygon/zkevm-node/pull/1718))
Closes [#1717](https://github.com/0xPolygon/zkevm-node/issues/1717).
This PR adds logs in case of errors happening in the methods responsible to interact with the prover for proof generation.
This additional logs are necessary in order to print more information, in particular, the \`proofId\` and \`batches\` (or \`batch\`) fields, which is not available in the outer scope (the \`Channel\` method) where the main error log is printed.
\* Fix formatting in error logs ([#1768](https://github.com/0xPolygon/zkevm-node/pull/1768))
Closes [#1766](https://github.com/0xPolygon/zkevm-node/issues/1766) .
This PR adds an additional formatting to the error message template, to hold the additional argument that is appended for the stacktrace. This applies to \`Errorf\` and \`Fatalf\`.
Also the first argument of the 'w' functions (\`Infow\`, \`Debugw\`, ...) has been renamed \`msg\`, the previous \`template\` name was misleading because actually it is not treated as a template.
\* Expire transactions ([#1765](https://github.com/0xPolygon/zkevm-node/pull/1765))
\* expire too old txs in the efficiency list
\* refactor and new pool retrieval interval config parameter
\* reimplement
\* fix pool retrieval
\* fix config test
\* fix config test
\* update prover image ([#1772](https://github.com/0xPolygon/zkevm-node/pull/1772))
\* Fix/reorg ([#1771](https://github.com/0xPolygon/zkevm-node/pull/1771))
\* sequencer logs
\* logs
\* fix pool tx
\* fixes
\* fix + log
\* fix if
\* fix
\* Remove death code
\* fix
\* more logs
\* logs
\* log
\* log
\* log
\* remove not null for field topic0
\* fix topic0
\* full response log
\* remove some logs
\* linter
\* comment forced batches test
---------
Co-authored-by: Arnau \<arnaubennassar5@gmail.com>
Co-authored-by: ToniRamirezM \<toni@iden3.com>
\* add json rpc endpoints doc ([#1738](https://github.com/0xPolygon/zkevm-node/pull/1738))
\* build(deps): bump google.golang.org/protobuf from 1.28.1 to 1.29.0 ([#1775](https://github.com/0xPolygon/zkevm-node/pull/1775))
Bumps \[google.golang.org/protobuf\]([https://github.com/protocolbuffers/protobuf-go](https://github.com/protocolbuffers/protobuf-go)) from 1.28.1 to 1.29.0.
- \[Release notes\]([https://github.com/protocolbuffers/protobuf-go/releases](https://github.com/protocolbuffers/protobuf-go/releases))
- \[Changelog\]([https://github.com/protocolbuffers/protobuf-go/blob/master/release.bash](https://github.com/protocolbuffers/protobuf-go/blob/master/release.bash))
- \[Commits\]([protocolbuffers/protobuf-go@`v1.28.1...v1.29.0`](https://github.com/protocolbuffers/protobuf-go/compare/v1.28.1...v1.29.0))
---
updated-dependencies:
- dependency-name: google.golang.org/protobuf
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/prometheus/common from 0.41.0 to 0.42.0 ([#1774](https://github.com/0xPolygon/zkevm-node/pull/1774))
Bumps \[github.com/prometheus/common\]([https://github.com/prometheus/common](https://github.com/prometheus/common)) from 0.41.0 to 0.42.0.
- \[Release notes\]([https://github.com/prometheus/common/releases](https://github.com/prometheus/common/releases))
- \[Commits\]([prometheus/common@`v0.41.0...v0.42.0`](https://github.com/prometheus/common/compare/v0.41.0...v0.42.0))
---
updated-dependencies:
- dependency-name: github.com/prometheus/common
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/iden3/go-iden3-crypto ([#1773](https://github.com/0xPolygon/zkevm-node/pull/1773))
Bumps \[github.com/iden3/go-iden3-crypto\]([https://github.com/iden3/go-iden3-crypto](https://github.com/iden3/go-iden3-crypto)) from 0.0.14-0.20220413123345-edc36bfa5247 to 0.0.14.
- \[Release notes\]([https://github.com/iden3/go-iden3-crypto/releases](https://github.com/iden3/go-iden3-crypto/releases))
- \[Commits\]([https://github.com/iden3/go-iden3-crypto/commits/v0.0.14](https://github.com/iden3/go-iden3-crypto/commits/v0.0.14))
---
updated-dependencies:
- dependency-name: github.com/iden3/go-iden3-crypto
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* fix  log ([#1777](https://github.com/0xPolygon/zkevm-node/pull/1777))
\* fix claim pre execution ([#1786](https://github.com/0xPolygon/zkevm-node/pull/1786))
\* fix claim pre execution
\* fix
\* re fix
\* re fix
\* offset ([#1788](https://github.com/0xPolygon/zkevm-node/pull/1788))
\* Fix/run doc ([#1789](https://github.com/0xPolygon/zkevm-node/pull/1789))
Fix running production doc
\* add support to jrpc to accept short hashes and addresses strings like 0x00 ([#1792](https://github.com/0xPolygon/zkevm-node/pull/1792))
\* Add restart policy to main docker-compose ([#1797](https://github.com/0xPolygon/zkevm-node/pull/1797))
\* refactor deprecated things
\* log ([#1804](https://github.com/0xPolygon/zkevm-node/pull/1804))
\* close grpc connection ([#1816](https://github.com/0xPolygon/zkevm-node/pull/1816))
\* add support to jrpc to accept short hashes and addresses strings like 0x00 ([#1802](https://github.com/0xPolygon/zkevm-node/pull/1802))
\* add check for not found tx and block for trace endpoints ([#1811](https://github.com/0xPolygon/zkevm-node/pull/1811))
\* Create sonar-project.properties
\* Create sonarqube.yml
\* Log startup info as JSON in production ([#1799](https://github.com/0xPolygon/zkevm-node/pull/1799))
This commit changes the format of the startup info to be JSON when the
log \`Environment\` configuration is set to \`production\`.
\* build(deps): bump google.golang.org/protobuf from 1.29.0 to 1.29.1 ([#1828](https://github.com/0xPolygon/zkevm-node/pull/1828))
Bumps \[google.golang.org/protobuf\]([https://github.com/protocolbuffers/protobuf-go](https://github.com/protocolbuffers/protobuf-go)) from 1.29.0 to 1.29.1.
- \[Release notes\]([https://github.com/protocolbuffers/protobuf-go/releases](https://github.com/protocolbuffers/protobuf-go/releases))
- \[Changelog\]([https://github.com/protocolbuffers/protobuf-go/blob/master/release.bash](https://github.com/protocolbuffers/protobuf-go/blob/master/release.bash))
- \[Commits\]([protocolbuffers/protobuf-go@`v1.29.0...v1.29.1`](https://github.com/protocolbuffers/protobuf-go/compare/v1.29.0...v1.29.1))
---
updated-dependencies:
- dependency-name: google.golang.org/protobuf
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* fix: moving print for storing tx in finalizer.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Relay jRPC methods to TrustedSequencer if pool info is needed ([#1767](https://github.com/0xPolygon/zkevm-node/pull/1767))
\* Fix boot condition for GER signal being sent ([#1837](https://github.com/0xPolygon/zkevm-node/pull/1837))
\* Fix boot condition for GER signal being sent
\* Fix boot condition for GER signal being sent
\* Fix boot condition for GER signal being sent
\* Flush state db ([#1831](https://github.com/0xPolygon/zkevm-node/pull/1831))
\* flush state db
\* flush state db
\* update prover image
\* improve log message
\* improve: adding additional info for txs moved to not ready ([#1829](https://github.com/0xPolygon/zkevm-node/pull/1829))
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* ForkID logic for an old batch and fix error handling in execute batch ([#1803](https://github.com/0xPolygon/zkevm-node/pull/1803))
\* etherman forkID event
\* ForkID
\* linter
\* etherman tests
\* update forkID
\* Update forkIdIntervals
\* fix [#1830](https://github.com/0xPolygon/zkevm-node/issues/1830)
\* suggestion
\* Prevent sequencer from getting blocked by sync is trusted state is more advanced than virtual state ([#1836](https://github.com/0xPolygon/zkevm-node/pull/1836))
\* Fix/unsigned tx state root ([#1835](https://github.com/0xPolygon/zkevm-node/pull/1835))
\* fix unsigned tx to use the correct l2block state root
\* remove unused variables and logs
\* update mocks
\* fix unit tests
\* solve conflicts
---------
Co-authored-by: ToniRamirezM \<toni@iden3.com>
\* Add IP to Pool txs ([#1817](https://github.com/0xPolygon/zkevm-node/pull/1817))
\* Avoid changes on go.mod ([#1841](https://github.com/0xPolygon/zkevm-node/pull/1841))
\* fix pool ip ([#1842](https://github.com/0xPolygon/zkevm-node/pull/1842))
\* safer reorg ([#1844](https://github.com/0xPolygon/zkevm-node/pull/1844))
\* build(deps): bump github.com/go-git/go-git/v5 from 5.6.0 to 5.6.1 ([#1848](https://github.com/0xPolygon/zkevm-node/pull/1848))
Bumps \[github.com/go-git/go-git/v5\]([https://github.com/go-git/go-git](https://github.com/go-git/go-git)) from 5.6.0 to 5.6.1.
- \[Release notes\]([https://github.com/go-git/go-git/releases](https://github.com/go-git/go-git/releases))
- \[Commits\]([go-git/go-git@`v5.6.0...v5.6.1`](https://github.com/go-git/go-git/compare/v5.6.0...v5.6.1))
---
updated-dependencies:
- dependency-name: github.com/go-git/go-git/v5
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump google.golang.org/protobuf from 1.29.1 to 1.30.0 ([#1849](https://github.com/0xPolygon/zkevm-node/pull/1849))
Bumps \[google.golang.org/protobuf\]([https://github.com/protocolbuffers/protobuf-go](https://github.com/protocolbuffers/protobuf-go)) from 1.29.1 to 1.30.0.
- \[Release notes\]([https://github.com/protocolbuffers/protobuf-go/releases](https://github.com/protocolbuffers/protobuf-go/releases))
- \[Changelog\]([https://github.com/protocolbuffers/protobuf-go/blob/master/release.bash](https://github.com/protocolbuffers/protobuf-go/blob/master/release.bash))
- \[Commits\]([protocolbuffers/protobuf-go@`v1.29.1...v1.30.0`](https://github.com/protocolbuffers/protobuf-go/compare/v1.29.1...v1.30.0))
---
updated-dependencies:
- dependency-name: google.golang.org/protobuf
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* add fault tolerance when failed to get revert message ([#1846](https://github.com/0xPolygon/zkevm-node/pull/1846))
\* Sync Trusted State via jRPC instead of Broadcast ([#1840](https://github.com/0xPolygon/zkevm-node/pull/1840))
\* break down jrpc package to share objects
\* sync trusted state via jRPC instead of broadcast
---------
Co-authored-by: ToniRamirezM \<toni@iden3.com>
\* New Logs and fix to GER Closing Signal ([#1868](https://github.com/0xPolygon/zkevm-node/pull/1868))
\* fix log
\* add closing signals logs
\* fix new ger signal
\* fix log
\* fix and enable test
\* fix finalizer log
\* Add logs to follow sequencer flow ([#1866](https://github.com/0xPolygon/zkevm-node/pull/1866))
\* fix pool migration ([#1863](https://github.com/0xPolygon/zkevm-node/pull/1863))
\* fix pool migration
\* fix pool migration
\* fix pool migration
\* fix
\* keep the caller locked if an error happens when processing pending monitored txs ([#1865](https://github.com/0xPolygon/zkevm-node/pull/1865))
\* Log OOC on reprocess full batch ([#1876](https://github.com/0xPolygon/zkevm-node/pull/1876))
\* enable uncle tests and fix uncle enpoint parameters ([#1861](https://github.com/0xPolygon/zkevm-node/pull/1861))
\* Update batchresources.go ([#1880](https://github.com/0xPolygon/zkevm-node/pull/1880))
\* Halt finalizer in case of full execution error ([#1879](https://github.com/0xPolygon/zkevm-node/pull/1879))
\* panic if trusted reorg in synchronizer
\* fix ([#1878](https://github.com/0xPolygon/zkevm-node/pull/1878))
\* log
\* logs
\* fixes
\* sync test commented
\* fix finalizer
\* fix encodeTransaction
\* fix encodeTransaction
---------
Co-authored-by: Alonso \<ARR551@protonmail.com>
\* Test/broadcast ([#1850](https://github.com/0xPolygon/zkevm-node/pull/1850))
Add test for trusted state consumed through permissionless node
\* check response before checking internal responses ([#1882](https://github.com/0xPolygon/zkevm-node/pull/1882))
\* add debug endpoints to docs ([#1881](https://github.com/0xPolygon/zkevm-node/pull/1881))
\* fix get tx by block hash or number and index ([#1877](https://github.com/0xPolygon/zkevm-node/pull/1877))
\* Improve E2E test time ([#1860](https://github.com/0xPolygon/zkevm-node/pull/1860))
\* Update software requirements to Ubuntu 22.04 ([#1845](https://github.com/0xPolygon/zkevm-node/pull/1845))
The prover needs Ubuntu 22.04. Since this is run in Docker, the requirement for everything should be 22.04.
\* Fix/failed tx in pool ([#1895](https://github.com/0xPolygon/zkevm-node/pull/1895))
\* Ignore TxStatusFailed txs in pool during replacement
\* Ignore TxStatusFailed txs in pool during replacement
\* wip
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve: adding config params for MaxTxSize in pool and MaxTxSizeForL1 for sequence sender.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve: moving more hardcoded values to be config props. And adding unit testing of the 'oversized data error'.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Update prover config ([#1898](https://github.com/0xPolygon/zkevm-node/pull/1898))
\* Update prover config
\* Enable multiwrite
---------
Co-authored-by: Ubuntu \<ubuntu@ip-172-31-22-24.eu-west-1.compute.internal>
\* create group 7 and split e2e json rpc tests ([#1897](https://github.com/0xPolygon/zkevm-node/pull/1897))
\* feat: adding check gas price of tx to be greater that min gas price and min suggested gas price before adding to pool.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* docker contracts update ([#1903](https://github.com/0xPolygon/zkevm-node/pull/1903))
\* genesis + image
\* smc v1.0.0-fork.3
\* etherman + tests
\* update genblocknumber
\* linter
\* latest prover version
\* fix test
\* feat: adding check gas price of tx to be greater that min gas price and min suggested gas price before adding to pool.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Truncate value in follower ([#1890](https://github.com/0xPolygon/zkevm-node/pull/1890))
\* trucate value in follower
\* truncate gas price
\* add check to validate eth\_call params ([#1885](https://github.com/0xPolygon/zkevm-node/pull/1885))
\* improve: renaming 'ErrIntrinsicGasPrice' to 'ErrGasPrice'
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* build(deps): bump github.com/holiman/uint256 from 1.2.1 to 1.2.2 ([#1912](https://github.com/0xPolygon/zkevm-node/pull/1912))
Bumps \[github.com/holiman/uint256\]([https://github.com/holiman/uint256](https://github.com/holiman/uint256)) from 1.2.1 to 1.2.2.
- \[Release notes\]([https://github.com/holiman/uint256/releases](https://github.com/holiman/uint256/releases))
- \[Commits\]([holiman/uint256@`v1.2.1...v1.2.2`](https://github.com/holiman/uint256/compare/v1.2.1...v1.2.2))
---
updated-dependencies:
- dependency-name: github.com/holiman/uint256
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Feature/[#1833](https://github.com/0xPolygon/zkevm-node/issues/1833) execute batch ([#1834](https://github.com/0xPolygon/zkevm-node/pull/1834))
\* avoid execute batch twice
\* fix make run-rpc
\* linter
\* Revert "fix make run-rpc"
This reverts commit [`1b8bddd`](https://github.com/0xPolygon/zkevm-node/commit/1b8bddd1fb40a5ff29f3a4f5c4f71e3f7da604a2).
\* suggestion
\* remove log
\* fix eth\_call and eth\_estimateGas parameters ([#1891](https://github.com/0xPolygon/zkevm-node/pull/1891))
\* Log events ([#1905](https://github.com/0xPolygon/zkevm-node/pull/1905))
\* wip
\* WIP
\* log OOG on pool pre execution
\* log high zkcounters use
\* fix test
\* fix test
\* fix test
\* fix if
\* fix test
\* fix test
\* build(deps): bump google.golang.org/grpc from 1.53.0 to 1.54.0 ([#1901](https://github.com/0xPolygon/zkevm-node/pull/1901))
Bumps \[google.golang.org/grpc\]([https://github.com/grpc/grpc-go](https://github.com/grpc/grpc-go)) from 1.53.0 to 1.54.0.
- \[Release notes\]([https://github.com/grpc/grpc-go/releases](https://github.com/grpc/grpc-go/releases))
- \[Commits\]([grpc/grpc-go@`v1.53.0...v1.54.0`](https://github.com/grpc/grpc-go/compare/v1.53.0...v1.54.0))
---
updated-dependencies:
- dependency-name: google.golang.org/grpc
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
Co-authored-by: tclemos \<thiago@iden3.com>
\* fix: fixing comments. ([#1914](https://github.com/0xPolygon/zkevm-node/pull/1914))
\* fix: fixing comments.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve: improving
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: adding last fixes.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
---------
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Flush state db after setting genesis ([#1908](https://github.com/0xPolygon/zkevm-node/pull/1908))
\* Flush state db after setting genesis
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix tests
\* fix log L1 tx too big ([#1920](https://github.com/0xPolygon/zkevm-node/pull/1920))
\* fix missing return on ProcessUnsignedTransaction ([#1917](https://github.com/0xPolygon/zkevm-node/pull/1917))
\* fix missing return on ProcessUnsignedTransaction
\* refactor
\* fix unsigned tx revert response
\* fix unit tests
\* fix ProcessBatch err check before reading gas used
---------
Co-authored-by: tclemos \<thiago@iden3.com>
\* Reprocess empty batch to update state root before sanity check (full batch) ([#1921](https://github.com/0xPolygon/zkevm-node/pull/1921))
\* fix: removing check for low gas price for claims.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: removing check for low gas price for claims. ([#1922](https://github.com/0xPolygon/zkevm-node/pull/1922))
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve,test: adding test case for skipping gas price error if tx is claim.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix forkID ([#1925](https://github.com/0xPolygon/zkevm-node/pull/1925))
\* fix forkID
\* fix test
\* update docker prover forkid 4 +  pql cfg improvements ([#1929](https://github.com/0xPolygon/zkevm-node/pull/1929))
\* update docker prover forkid 4 +  pql cfg improvements
\* increase dbNumberOfPoolConnections
\* increase dbNumberOfPoolConnections again
\* update license
\* build(deps): bump github.com/urfave/cli/v2 from 2.25.0 to 2.25.1 ([#1931](https://github.com/0xPolygon/zkevm-node/pull/1931))
Bumps \[github.com/urfave/cli/v2\]([https://github.com/urfave/cli](https://github.com/urfave/cli)) from 2.25.0 to 2.25.1.
- \[Release notes\]([https://github.com/urfave/cli/releases](https://github.com/urfave/cli/releases))
- \[Changelog\]([https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md](https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md))
- \[Commits\]([urfave/cli@`v2.25.0...v2.25.1`](https://github.com/urfave/cli/compare/v2.25.0...v2.25.1))
---
updated-dependencies:
- dependency-name: github.com/urfave/cli/v2
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Prepare docs and action for mainnet release ([#1928](https://github.com/0xPolygon/zkevm-node/pull/1928))
\* Adds mainnet config ([#1941](https://github.com/0xPolygon/zkevm-node/pull/1941))
\* Fix mainnet config
\* Fix mainnet config
\* Add mising postgres config for mainnet
\* remove history limit, replace fatal to error ([#1940](https://github.com/0xPolygon/zkevm-node/pull/1940))
\* handle fea2scalar error ([#1942](https://github.com/0xPolygon/zkevm-node/pull/1942))
\* handle fea2scalar error
\* handle fea2scalar error
\* trusted reorg if it is not a trusted sequencer ([#1945](https://github.com/0xPolygon/zkevm-node/pull/1945))
\* trusted reorg if it is not a trusted sequencer
\* halt
\* trustedsequencer url as config param ([#1956](https://github.com/0xPolygon/zkevm-node/pull/1956))
\* add deposit\_counter to pool ([#1958](https://github.com/0xPolygon/zkevm-node/pull/1958))
\* add EIP-1898 support to eth\_call ([#1961](https://github.com/0xPolygon/zkevm-node/pull/1961))
\* tos32 error handling ([#1959](https://github.com/0xPolygon/zkevm-node/pull/1959))
\* fix log without topics response ([#1970](https://github.com/0xPolygon/zkevm-node/pull/1970))
\* add issue templates ([#1893](https://github.com/0xPolygon/zkevm-node/pull/1893))
\* fix BatchNumberByBlockNumber when batch is not found ([#1964](https://github.com/0xPolygon/zkevm-node/pull/1964))
\* fix claims ([#1977](https://github.com/0xPolygon/zkevm-node/pull/1977))
\* review jRPC endpoints doc ([#1968](https://github.com/0xPolygon/zkevm-node/pull/1968))
\* Update executor with forkID 4 support ([#1916](https://github.com/0xPolygon/zkevm-node/pull/1916))
Update executor and smart contracts for testing
---------
Co-authored-by: Alonso \<ARR551@protonmail.com>
Co-authored-by: tclemos \<thiago@iden3.com>
\* Stop release generation for RCs ([#1982](https://github.com/0xPolygon/zkevm-node/pull/1982))
\* create codeql scanning profile
\* mainnet and rollup exit roots ([#1975](https://github.com/0xPolygon/zkevm-node/pull/1975))
\* mainnet and rollup exit roots
\* linter
\* fix test e2e
\* doc
\* fix: adding support for eip-1898 in JSON-RPC for pending methods.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: fixing 'endpoints\_eth'.'GetTransactionCount'
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: parameters and return values of 'getBlockNumByArg' and 'getBlockByArg'.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* refactoring
\* remove javascript from codeql
\* add combined log to jRPC requests ([#1986](https://github.com/0xPolygon/zkevm-node/pull/1986))
\* web3\_clientVersion returns the node version ([#1985](https://github.com/0xPolygon/zkevm-node/pull/1985))
\* replace map by sync.Map for jRPC filters ([#1984](https://github.com/0xPolygon/zkevm-node/pull/1984))
\* add example to OPEN RPC doc for zkevm\_getBatchByNumber endpoint ([#1983](https://github.com/0xPolygon/zkevm-node/pull/1983))
\* event log ([#1989](https://github.com/0xPolygon/zkevm-node/pull/1989))
\* event log
\* event log
\* event log
\* event log
\* event log
\* fix config
\* reuse code
\* fix
\* fix
\* fix Makefile
\* remove default config
\* remove default config
\* remove default config
\* remove default config
\* replace the state debug tx to execute just the tx that needs the trace ([#1994](https://github.com/0xPolygon/zkevm-node/pull/1994))
\* remove broadcast service ([#1988](https://github.com/0xPolygon/zkevm-node/pull/1988))
\* allow pool to be blocked ([#1899](https://github.com/0xPolygon/zkevm-node/pull/1899))
\* improve: storing failed rx reason in db.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: regenerating mocks.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve: adding logs of tx efficiency
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: adding wait group for goroutines started in 'handleTransactionError' so we can await if needed in tests. And making other db deletions async as well.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* build(deps): bump golang.org/x/crypto from 0.7.0 to 0.8.0 ([#2001](https://github.com/0xPolygon/zkevm-node/pull/2001))
Bumps \[golang.org/x/crypto\]([https://github.com/golang/crypto](https://github.com/golang/crypto)) from 0.7.0 to 0.8.0.
- \[Release notes\]([https://github.com/golang/crypto/releases](https://github.com/golang/crypto/releases))
- \[Commits\]([golang/crypto@`v0.7.0...v0.8.0`](https://github.com/golang/crypto/compare/v0.7.0...v0.8.0))
---
updated-dependencies:
- dependency-name: golang.org/x/crypto
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Make stateTree and executor optional in the state. ([#1995](https://github.com/0xPolygon/zkevm-node/pull/1995))
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* make executor and statedb optional
\* fix eventlog
\* fix test
\* fix method name
\* move state SQL queries ([#2003](https://github.com/0xPolygon/zkevm-node/pull/2003))
\* improve: storing 'batch\_resources' and 'closing\_reason' in 'state.batch' on closing a batch.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Refactor sequencer state interfaces ([#2002](https://github.com/0xPolygon/zkevm-node/pull/2002))
\* improve: fixing worker todos.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve: fixing dbmanager todos.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* improve: fixing benchmark test scripts todos
\* build(deps): bump github.com/prometheus/client\_golang ([#2015](https://github.com/0xPolygon/zkevm-node/pull/2015))
Bumps \[github.com/prometheus/client\_golang\]([https://github.com/prometheus/client\_golang](https://github.com/prometheus/client_golang)) from 1.14.0 to 1.15.0.
- \[Release notes\]([https://github.com/prometheus/client\_golang/releases](https://github.com/prometheus/client_golang/releases))
- \[Changelog\]([https://github.com/prometheus/client\_golang/blob/main/CHANGELOG.md](https://github.com/prometheus/client_golang/blob/main/CHANGELOG.md))
- \[Commits\]([prometheus/client\_golang@`v1.14.0...v1.15.0`](https://github.com/prometheus/client_golang/compare/v1.14.0...v1.15.0))
---
updated-dependencies:
- dependency-name: github.com/prometheus/client\_golang
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Add more details on the compatibility of eth\_call ([#2018](https://github.com/0xPolygon/zkevm-node/pull/2018))
\* Add more details on the compatibility of eth\_call
\* Mention that effective gas price is not included for receipts
\* Improve timestamp resolution ([#2007](https://github.com/0xPolygon/zkevm-node/pull/2007))
\* timestamp resolution
\* fixes
\* fixes
\* fix
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* fix test
\* refactor code
\* refactor
\* refactor check
\* fix: fixing comments.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: fixing comments.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: fixing worker AddTxTracker to return drop error reason.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* check trusted state before L1 data ([#2022](https://github.com/0xPolygon/zkevm-node/pull/2022))
check trusted state before L1 data to avoid havan incomplete trusted state
\* improve: adding missing usages of TxStatus metric.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix: fixing sequencer metrics imports and host and port of event-db in debug config.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Improve GHA ([#2031](https://github.com/0xPolygon/zkevm-node/pull/2031))
Remove prover mock and ok-to-test
\* Merges v0.0.6 into Develop ([#2039](https://github.com/0xPolygon/zkevm-node/pull/2039))
\* fix eventlog config check
\* fix build version flags
\* fix optional trace config; update prover docker image
\* add callTracer ([#2010](https://github.com/0xPolygon/zkevm-node/pull/2010))
\* go 1.19
\* add callTracer, 4byte, noop and prestate tracers
\* workaround to fix linter problem related to the ruleguard, more details here: [golangci/golangci-lint#3107](https://github.com/golangci/golangci-lint/issues/3107)
\* fix eth\_estimateGas response for reverted txs
\* Improve claim checks ([#2027](https://github.com/0xPolygon/zkevm-node/pull/2027))
\* fix wrong state root when prevlastbatch & lastbatch are empty + restart ([#2028](https://github.com/0xPolygon/zkevm-node/pull/2028))
\* Update production config for prover
\* Update prover version
\* fix conflicts
\* fix conflicts
\* fix conflicts
\* Add ALL PRIVILEGES to prover\_user for prover\_db.state schema
\* update linter version
---------
Co-authored-by: tclemos \<thiago@iden3.com>
Co-authored-by: Thiago Coimbra Lemos \<tclemos@users.noreply.github.com>
Co-authored-by: Alonso Rodriguez \<ARR552@users.noreply.github.com>
Co-authored-by: bros \<arnaubennassar5@gmail.com>
Co-authored-by: agnusmor \<agnusmor@gmail.com>
Co-authored-by: agnusmor \<100322135+agnusmor@users.noreply.github.com>
Co-authored-by: Thiago Lemos \<thiago@polygon.technology>
\* Feature/split network config ([#1999](https://github.com/0xPolygon/zkevm-node/pull/1999))
\* Move network related config from config.toml to genesis.json
\* build(deps): bump github.com/iden3/go-iden3-crypto from 0.0.14 to 0.0.15 ([#2050](https://github.com/0xPolygon/zkevm-node/pull/2050))
Bumps \[github.com/iden3/go-iden3-crypto\]([https://github.com/iden3/go-iden3-crypto](https://github.com/iden3/go-iden3-crypto)) from 0.0.14 to 0.0.15.
- \[Release notes\]([https://github.com/iden3/go-iden3-crypto/releases](https://github.com/iden3/go-iden3-crypto/releases))
- \[Commits\]([iden3/go-iden3-crypto@`v0.0.14...v0.0.15`](https://github.com/iden3/go-iden3-crypto/compare/v0.0.14...v0.0.15))
---
updated-dependencies:
- dependency-name: github.com/iden3/go-iden3-crypto
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* wip
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Remove claim txs ([#2048](https://github.com/0xPolygon/zkevm-node/pull/2048))
\* remove claim txs
\* fix tests
\* fix tests
\* fix tests
\* remove deposit\_count
\* fix query
\* fix query
---------
Co-authored-by: Thiago Lemos \<thiago@polygon.technology>
\* wip#2
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* wip [#3](https://github.com/0xPolygon/zkevm-node/pull/3)
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Remove claim txs ([#2048](https://github.com/0xPolygon/zkevm-node/pull/2048))
\* remove claim txs
\* fix tests
\* fix tests
\* fix tests
\* remove deposit\_count
\* fix query
\* fix query
---------
Co-authored-by: Thiago Lemos \<thiago@polygon.technology>
\* build(deps): bump github.com/urfave/cli/v2 from 2.25.1 to 2.25.3 ([#2063](https://github.com/0xPolygon/zkevm-node/pull/2063))
Bumps \[github.com/urfave/cli/v2\]([https://github.com/urfave/cli](https://github.com/urfave/cli)) from 2.25.1 to 2.25.3.
- \[Release notes\]([https://github.com/urfave/cli/releases](https://github.com/urfave/cli/releases))
- \[Changelog\]([https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md](https://github.com/urfave/cli/blob/main/docs/CHANGELOG.md))
- \[Commits\]([urfave/cli@`v2.25.1...v2.25.3`](https://github.com/urfave/cli/compare/v2.25.1...v2.25.3))
---
updated-dependencies:
- dependency-name: github.com/urfave/cli/v2
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Do not use zkcounters on eth\_Call ([#2021](https://github.com/0xPolygon/zkevm-node/pull/2021))
\* not use zkcounters on eth\_Call
\* fix test
\* prover image
\* prover image
\* prover image
\* fix default trace values for custom tracers ([#2066](https://github.com/0xPolygon/zkevm-node/pull/2066))
\* add support to safe and finalized blocks for jRPC block parameters ([#2049](https://github.com/0xPolygon/zkevm-node/pull/2049))
\* cmd/approve: add new flag to set max-amount ([#2030](https://github.com/0xPolygon/zkevm-node/pull/2030))
\* build(deps): bump github.com/prometheus/client\_golang ([#2074](https://github.com/0xPolygon/zkevm-node/pull/2074))
Bumps \[github.com/prometheus/client\_golang\]([https://github.com/prometheus/client\_golang](https://github.com/prometheus/client_golang)) from 1.15.0 to 1.15.1.
- \[Release notes\]([https://github.com/prometheus/client\_golang/releases](https://github.com/prometheus/client_golang/releases))
- \[Changelog\]([https://github.com/prometheus/client\_golang/blob/main/CHANGELOG.md](https://github.com/prometheus/client_golang/blob/main/CHANGELOG.md))
- \[Commits\]([prometheus/client\_golang@`v1.15.0...v1.15.1`](https://github.com/prometheus/client_golang/compare/v1.15.0...v1.15.1))
---
updated-dependencies:
- dependency-name: github.com/prometheus/client\_golang
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/prometheus/client\_model from 0.3.0 to 0.4.0 ([#2073](https://github.com/0xPolygon/zkevm-node/pull/2073))
Bumps \[github.com/prometheus/client\_model\]([https://github.com/prometheus/client\_model](https://github.com/prometheus/client_model)) from 0.3.0 to 0.4.0.
- \[Release notes\]([https://github.com/prometheus/client\_model/releases](https://github.com/prometheus/client_model/releases))
- \[Commits\]([prometheus/client\_model@`v0.3.0...v0.4.0`](https://github.com/prometheus/client_model/compare/v0.3.0...v0.4.0))
---
updated-dependencies:
- dependency-name: github.com/prometheus/client\_model
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* fix sync\_info table ([#2055](https://github.com/0xPolygon/zkevm-node/pull/2055))
\* fix
\* linter
\* merge set last batch info seen methods
---------
Co-authored-by: Thiago Lemos \<thiago@polygon.technology>
\* remove unit suffix from duration config params ([#2068](https://github.com/0xPolygon/zkevm-node/pull/2068))
\* New sequence sender component ([#2051](https://github.com/0xPolygon/zkevm-node/pull/2051))
\* new sequence sender
\* fix config file
\* fix docker-compose
\* fix e2e tests
\* fix e2e tests
\* fix e2e tests
\* fix e2e tests
\* fixes
\* remove keys fron sequencer
\* fix sequence sender
\* remove todo
\* remove txPool dependency
\* Merge v0.0.8 into develop ([#2077](https://github.com/0xPolygon/zkevm-node/pull/2077))
\* wip [#4](https://github.com/0xPolygon/zkevm-node/pull/4)
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* fix
\* build(deps): bump github.com/prometheus/common from 0.42.0 to 0.43.0 ([#2081](https://github.com/0xPolygon/zkevm-node/pull/2081))
Bumps \[github.com/prometheus/common\]([https://github.com/prometheus/common](https://github.com/prometheus/common)) from 0.42.0 to 0.43.0.
- \[Release notes\]([https://github.com/prometheus/common/releases](https://github.com/prometheus/common/releases))
- \[Commits\]([prometheus/common@`v0.42.0...v0.43.0`](https://github.com/prometheus/common/compare/v0.42.0...v0.43.0))
---
updated-dependencies:
- dependency-name: github.com/prometheus/common
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump google.golang.org/grpc from 1.54.0 to 1.55.0 ([#2080](https://github.com/0xPolygon/zkevm-node/pull/2080))
Bumps \[google.golang.org/grpc\]([https://github.com/grpc/grpc-go](https://github.com/grpc/grpc-go)) from 1.54.0 to 1.55.0.
- \[Release notes\]([https://github.com/grpc/grpc-go/releases](https://github.com/grpc/grpc-go/releases))
- \[Commits\]([grpc/grpc-go@`v1.54.0...v1.55.0`](https://github.com/grpc/grpc-go/compare/v1.54.0...v1.55.0))
---
updated-dependencies:
- dependency-name: google.golang.org/grpc
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump golang.org/x/sync from 0.1.0 to 0.2.0 ([#2079](https://github.com/0xPolygon/zkevm-node/pull/2079))
Bumps \[golang.org/x/sync\]([https://github.com/golang/sync](https://github.com/golang/sync)) from 0.1.0 to 0.2.0.
- \[Commits\]([golang/sync@`v0.1.0...v0.2.0`](https://github.com/golang/sync/compare/v0.1.0...v0.2.0))
---
updated-dependencies:
- dependency-name: golang.org/x/sync
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
Co-authored-by: Toni Ramírez \<58293609+ToniRamirezM@users.noreply.github.com>
\* Fix/deployment ([#2076](https://github.com/0xPolygon/zkevm-node/pull/2076))
\* fix prover permissions
\* fix docker compose
\* fix doc
\* fix script
\* reduce interval to search forkID events
\* verify genesis block number check for full nodes
\* linter
\* improve: adding error handling for txs of forced batch
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Review jRPC default configuration ([#2083](https://github.com/0xPolygon/zkevm-node/pull/2083))
\* build(deps): bump golang.org/x/net from 0.9.0 to 0.10.0 ([#2084](https://github.com/0xPolygon/zkevm-node/pull/2084))
Bumps \[golang.org/x/net\]([https://github.com/golang/net](https://github.com/golang/net)) from 0.9.0 to 0.10.0.
- \[Commits\]([golang/net@`v0.9.0...v0.10.0`](https://github.com/golang/net/compare/v0.9.0...v0.10.0))
---
updated-dependencies:
- dependency-name: golang.org/x/net
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump golang.org/x/crypto from 0.8.0 to 0.9.0 ([#2087](https://github.com/0xPolygon/zkevm-node/pull/2087))
Bumps \[golang.org/x/crypto\]([https://github.com/golang/crypto](https://github.com/golang/crypto)) from 0.8.0 to 0.9.0.
- \[Commits\]([golang/crypto@`v0.8.0...v0.9.0`](https://github.com/golang/crypto/compare/v0.8.0...v0.9.0))
---
updated-dependencies:
- dependency-name: golang.org/x/crypto
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
Co-authored-by: Toni Ramírez \<58293609+ToniRamirezM@users.noreply.github.com>
\* config default values ([#2090](https://github.com/0xPolygon/zkevm-node/pull/2090))
\* config
\* unit test
\* MaxTxBytesSize and MaxTxDataBytesSize
\* fix decode txs ([#2091](https://github.com/0xPolygon/zkevm-node/pull/2091))
\* configuration fixes ([#2094](https://github.com/0xPolygon/zkevm-node/pull/2094))
\* improve: finishing implementation of the vector forced batch tests and updating e2e forced batch test to have 1 forced tx.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Update link to protocol specification
\* remove error logs when the error is related to the tx ([#2096](https://github.com/0xPolygon/zkevm-node/pull/2096))
\* fix: fixing forced batches error handling and normal batches transaction level error handling.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* rename isBatchProcessed
\* fix: forced batch rom OOC check.
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* rename isBatchProcessed
\* second fix
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
\* Refactor state errors ([#2105](https://github.com/0xPolygon/zkevm-node/pull/2105))
\* refactor state errors
\* refactor state errors
\* refactor state errors
\* refactor state errors
\* refactor state errors
\* refactor
\* fix
\* function rename
\* fix wg
\* fix wg
\* fix
\* Fix sequencer error ([#2108](https://github.com/0xPolygon/zkevm-node/pull/2108))
\* fix error not returned
\* avoid decoding batchl2data when there are no txs
\* fix
\* disable auto release on GHA ([#2107](https://github.com/0xPolygon/zkevm-node/pull/2107))
\* fix executor error handling ([#2109](https://github.com/0xPolygon/zkevm-node/pull/2109))
\* build(deps): bump github.com/stretchr/testify from 1.8.2 to 1.8.3 ([#2111](https://github.com/0xPolygon/zkevm-node/pull/2111))
Bumps \[github.com/stretchr/testify\]([https://github.com/stretchr/testify](https://github.com/stretchr/testify)) from 1.8.2 to 1.8.3.
- \[Release notes\]([https://github.com/stretchr/testify/releases](https://github.com/stretchr/testify/releases))
- \[Commits\]([stretchr/testify@`v1.8.2...v1.8.3`](https://github.com/stretchr/testify/compare/v1.8.2...v1.8.3))
---
updated-dependencies:
- dependency-name: github.com/stretchr/testify
  dependency-type: direct:production
  update-type: version-update:semver-patch
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* build(deps): bump github.com/prometheus/common from 0.43.0 to 0.44.0 ([#2116](https://github.com/0xPolygon/zkevm-node/pull/2116))
Bumps \[github.com/prometheus/common\]([https://github.com/prometheus/common](https://github.com/prometheus/common)) from 0.43.0 to 0.44.0.
- \[Release notes\]([https://github.com/prometheus/common/releases](https://github.com/prometheus/common/releases))
- \[Commits\]([prometheus/common@`v0.43.0...v0.44.0`](https://github.com/prometheus/common/compare/v0.43.0...v0.44.0))
---
updated-dependencies:
- dependency-name: github.com/prometheus/common
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* fix error returned during tx decoding ([#2117](https://github.com/0xPolygon/zkevm-node/pull/2117))
\* fix timestamp resolution to 10s ([#2112](https://github.com/0xPolygon/zkevm-node/pull/2112))
\* build(deps): bump github.com/go-git/go-git/v5 from 5.6.1 to 5.7.0 ([#2119](https://github.com/0xPolygon/zkevm-node/pull/2119))
Bumps \[github.com/go-git/go-git/v5\]([https://github.com/go-git/go-git](https://github.com/go-git/go-git)) from 5.6.1 to 5.7.0.
- \[Release notes\]([https://github.com/go-git/go-git/releases](https://github.com/go-git/go-git/releases))
- \[Commits\]([go-git/go-git@`v5.6.1...v5.7.0`](https://github.com/go-git/go-git/compare/v5.6.1...v5.7.0))
---
updated-dependencies:
- dependency-name: github.com/go-git/go-git/v5
  dependency-type: direct:production
  update-type: version-update:semver-minor
...
Signed-off-by: dependabot\[bot\] \<support@github.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
\* Fix/delegate call trace ([#2115](https://github.com/0xPolygon/zkevm-node/pull/2115))
\* WIP: fix delegatecall when trace is requested via custom tracer
\* changes to custom tracer for call, callcode, staticcall, delegatecall opcodes
\* fix custom tracer staticcall opcode
\* fix custom tracer subcalls with multi levels
\* comment test debug code
\* review error handling
\* fix custom call tracer for SC calls with precompiled code
\* fix get precompiled address and input for opcodes that have tx value
\* increase debug tracer e2e tests timeout
\* update prover image
\* change log to info ([#2121](https://github.com/0xPolygon/zkevm-node/pull/2121))
---------
Signed-off-by: dependabot\[bot\] \<support@github.com>
Signed-off-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
Co-authored-by: dependabot\[bot\] \<49699333+dependabot\[bot\]@users.noreply.github.com>
Co-authored-by: Toni Ramírez \<58293609+ToniRamirezM@users.noreply.github.com>
Co-authored-by: Nikolay Nedkov \<nikolai\_nedkov@yahoo.com>
Co-authored-by: Thiago Coimbra Lemos \<tclemos@users.noreply.github.com>
Co-authored-by: ToniRamirezM \<toni@iden3.com>
Co-authored-by: Arnau Bennassar \<arnaubennassar5@gmail.com>
Co-authored-by: tclemos \<thiago@iden3.com>
Co-authored-by: Paolo Grisoli \<paolo\_g84@icloud.com>
Co-authored-by: Cool Developer \<kevin@polygon.technology>
Co-authored-by: Cool Developer \<125276287+C001-developer@users.noreply.github.com>
Co-authored-by: CvH \<109217179+cvhpoly@users.noreply.github.com>
Co-authored-by: Jordi Baylina \<jordi@baylina.cat>
Co-authored-by: CG \<118215885+cg-polygon@users.noreply.github.com>
Co-authored-by: Ubuntu \<ubuntu@ip-172-31-22-24.eu-west-1.compute.internal>
Co-authored-by: agnusmor \<100322135+agnusmor@users.noreply.github.com>
Co-authored-by: zkronos73 \<94566827+zkronos73@users.noreply.github.com>
Co-authored-by: zkronos73 \<zkronos73@gmail.com>
Co-authored-by: pierce403 \<pierce403@gmail.com>
Co-authored-by: agnusmor \<agnusmor@gmail.com>
Co-authored-by: Thiago Lemos \<thiago@polygon.technology>
Co-authored-by: nathan haim \<nathan.haim@free.fr>
Co-authored-by: Toni Ramírez \<toni@polygon.technology>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Closes #2047

## What does this PR do?

Do not differentiate claim txs and handle them as regular ones.

## Reviewers

Main reviewers:
