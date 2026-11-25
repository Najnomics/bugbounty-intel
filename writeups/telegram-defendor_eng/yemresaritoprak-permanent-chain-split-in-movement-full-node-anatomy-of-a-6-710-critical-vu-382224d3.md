# 🔐 The First ZK Exploits To Hit Live Protocols

- **Source URL:** https://medium.com/@yemresaritoprak/permanent-chain-split-in-movement-full-node-anatomy-of-a-6-710-critical-vulnerability-that-fa75fe66a0c7
- **Fetched from:** https://web.archive.org/web/20260726071019/https://medium.com/@yemresaritoprak/permanent-chain-split-in-movement-full-node-anatomy-of-a-6-710-critical-vulnerability-that-fa75fe66a0c7
- **Fetched:** 2026-11-25
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1680 (id 1680)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Permanent Chain Split in Movement Full Node: Anatomy of a $6,710 Critical Vulnerability That Required a Hard Fork

Hello, I’m Yunus Emre Sarıtoprak. As a cybersecurity researcher, my goal is to contribute to the security of the Web3 ecosystem. In this article, I will share the story and technical details of a critical vulnerability I responsibly disclosed to Movement Labs through the Immunefi platform, for which I was rewarded **$6,710**.

This vulnerability was a critical logic flaw in the “full node” software — one of the most fundamental components of a blockchain network. It was capable of causing a **permanent chain split** and required a **hard fork** (a mandatory protocol upgrade) to resolve.

## Summary of the Vulnerability: How Were Two Blocks at the Same Height Possible?

The most fundamental rule of a blockchain is that there can only be one canonical (official) block at each block `height`. If a network dispute or a malicious act leads to the production of multiple blocks at the same height, nodes must use a "fork-choice logic" to select only one and reject the others.

However, the **Movement Full Node** software was missing this mechanism. This flaw could lead to a permanent chain split, double-spend attacks, and a complete loss of network consensus.

Let’s break down how this vulnerability manifested at the code level, step by step.

## Technical Analysis: A Deep Dive into the Code

The root cause of the vulnerability lay within the `process_block_from_da` function in the `execute_settle.rs` file.

### Step 1: The Full Vulnerable Function

First, let’s look at the entire function where the error was found. This function is responsible for processing blocks coming from the Data Availability (DA) layer.

```
// networks/movement/movement-full-node/src/node/tasks/execute_settle.rs
async fn process_block_from_da(
    &mut self,
    response: StreamReadFromHeightResponse,
) -> anyhow::Result<()> {
    // Extracts block data, timestamp, ID, and height from the blob response.
    let (block_bytes, block_timestamp, block_id, da_height) = match response
        .blob
        .ok_or(anyhow::anyhow!("No blob in response"))?
        .blob_type
        .ok_or(anyhow::anyhow!("No blob type in response"))?
    {
        blob_response::BlobType::SequencedBlobBlock(blob) => {
            (blob.data, blob.timestamp, blob.blob_id, blob.height)
        }
        // ... other blob types
        _ => anyhow::bail!("Invalid blob type"),
    };
    info!(
        block_id = %hex::encode(block_id.clone()),
        da_height = da_height,
        time = block_timestamp,
        "Processing block from DA"
    );
    // Checks if the block has been executed before.
    if self.da_db.has_executed_block(block_id.clone()).await? {
        info!("Block already executed: {:#?}. It will be skipped", block_id);
        return Ok(());
    }
    if da_height < 2 {
        anyhow::bail!("Invalid DA height: {:?}", da_height);
    }
    // Deserializes the block bytes into a Block struct.
    let block: Block = bcs::from_bytes(&block_bytes[..])?;
    // Executes the block with retries.
    let span = info_span!(target: "movement_timing", "execute_block", id = ?block_id);
    let commitment =
        self.execute_block_with_retries(block, block_timestamp).instrument(span).await?;
    // Sets the synced height.
    self.da_db.set_synced_height(da_height - 1).await?;
    // Adds the executed block ID to the database.
    self.da_db.add_executed_block(block_id.clone()).await?;
    info!(block_id = ?block_id, "Skipping settlement or proceeding...");
    Ok(())
}
```
### Step 2: How the Code is Supposed to Work (The Expected Behavior)

Looking at the function above, we can see a standard workflow:

1. **Receive Data:** The function gets block data (`response`) from the DA layer.
2. **Extract Information:** It extracts the block’s content (`block_bytes`), its unique identifier (`block_id`), and its height (`da_height`).
3. **Prevent Re-processing:** It uses the `has_executed_block` function to check if the block's **identifier** (`block_id`) has been previously saved to the database. If the same `block_id` has been processed before, the function stops. This is a standard check to prevent processing the exact same block multiple times.
4. **Process and Save:** If the block is new, the code executes it (applies its transactions) and finally saves the block’s ID to the database as “executed” using the `add_executed_block` function.

This flow works perfectly in the ideal scenario where every block has a unique `block_id`. The problem, however, arises in non-ideal scenarios.

### Step 3: Where the Vulnerability Was Hiding (The Unexpected Behavior)

The vulnerability stems from a single, critical omission: **the lack of a height check.**

The following code block is the first and most crucial part of the vulnerability:

```
// Vulnerable Part 1: Only the block ID is checked.
if self.da_db.has_executed_block(block_id.clone()).await? {
    info!("Block already executed: {:#?}. It will be skipped", block_id);
    return Ok(());
}
```
*The Problem: This check only and exclusively considers the block\_id. There is no corresponding "has this height been used before?" check for the da\_height.*


What does this mean?

If, due to an attacker or a network partition, two blocks (Block A and Block B) are produced with the same `da_height = H` but different `block_id`s:

- When Block A arrives, it passes the `has_executed_block` check because its ID is new. The block is processed, and its ID is added to the database.
- Immediately after, when Block B arrives, it also **successfully passes** the `has_executed_block` check because its `block_id` is different from Block A's!

The code is unable to realize that Block B is attempting to occupy a height that should already be considered filled.

And the following code block makes this situation irreversible:

```
// Vulnerable Part 2: The invalid block is saved as if it were valid.
self.da_db.add_executed_block(block_id.clone()).await?;
```
This line adds the ID of the second block at the same height to the “executed” database. Now, the ledger has both Block A and Block B recorded at the same height `H`. **The chain has been permanently split.**

## Impact and Severity

**The final assessment by Immunefi’s Triage team clarified the severity of the vulnerability even further: *Unintended permanent chain split requiring a hard fork*.**

This is one of the most destructive scenarios for a blockchain project. It means that once the network is split in this way, it can never heal on its own through an automatic process. The only solution to merge the split chains is a hard fork — a manual software upgrade that all network participants (validators, node operators, developers) must agree upon and apply. This process is extremely costly, difficult to coordinate, and highly damaging to a project’s reputation.

In light of this final assessment, the impacts of the vulnerability are:

- **Double-Spending & Conflicting Transactions:** It becomes possible to send the same assets to different people on the split chains.
- **Network Halt and Mandatory Hard Fork:** The network can no longer proceed in a consistent state. Developers would need to halt the network, issue a patch, and ensure all operators upgrade to the new version.
- **Loss of Trust:** The “finality” promise of a blockchain — the guarantee that a transaction is irreversible — is completely broken. This fundamentally undermines the trust of users and investors in the project.

For these reasons, the vulnerability was classified at the highest level: **Critical**.

## Proof of Concept

Triggering this vulnerability did not require any code modification. A test environment with a multi-validator setup and a brief network partition was sufficient:

1. **Prepare the Environment:** Two different Celestia validators were run, connected to a single Movement Full Node.
2. **Simulate a Network Partition:** The network connection of one of the validators was briefly disconnected and then reconnected.
3. **The Fork:** During this brief separation, both validators produced blocks at the same height (`H`) but with different identifiers (`block_id=A` and `block_id=B`).
4. **Observation:** Once the network connection was restored, the logs of the Movement Full Node were examined. It was observed that the node first processed Block A and then, without any error, processed Block B at the exact same height `H`.

This simple test clearly proved that the chain was permanently forked and that the node had no mechanism to correct this state.

## Recommendations

I provided the following solutions to the Movement Labs team:

- **Fork-Choice Logic:** The most robust solution is to implement a fork-choice rule (e.g., a BFT-based mechanism). This allows the node to decide which block is canonical when faced with multiple blocks at the same height.
- **Height-Based Blocking:** A simpler, more immediate fix is to mark a height `H` as "filled" once a block is processed for it, and reject all subsequent blocks claiming the same height.
- **Expanded Testing:** Increase test coverage, especially for scenarios involving network partitions and multi-validator setups.

## Conclusion and Acknowledgments

In complex systems like blockchains, sometimes the simplest logic flaws can lead to the most devastating consequences, **even to the point of requiring the entire network to halt and be upgraded via a hard fork**. This case underscores that the definition of a “unique block” must be based not only on its `block_id` but also on its `height`.

I want to thank the **Movement Labs** team for their professional and prompt handling of this report and the **Immunefi** platform for managing the responsible disclosure process transparently. The collaboration between whitehats and projects is vital for building a more secure future for Web3.

Thank you for reading. You can follow me on Medium and [Twitter @yemresaritoprak](https://web.archive.org/web/20260726071019/https://twitter.com/yemresaritoprak) for future write-ups.
