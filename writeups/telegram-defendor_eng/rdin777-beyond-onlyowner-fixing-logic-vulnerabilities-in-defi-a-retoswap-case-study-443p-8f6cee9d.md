# ⚠️ Logic Flaw Could Have Drained DeFi Vault

- **Source URL:** https://dev.to/rdin777/beyond-onlyowner-fixing-logic-vulnerabilities-in-defi-a-retoswap-case-study-443p
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1684 (id 1684)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Logic vulnerabilities are often the most dangerous bugs in DeFi. Unlike reentrancy or overflow errors, they don't always trigger standard static analysis tools. They hide in plain sight, disguised as "intended functionality."

In this article, I want to share a recent security assessment I performed, where a critical logic flaw could have allowed an attacker to drain the entire vault.

1. The Anatomy of the Bug: The "Arbiter" Flaw In the original implementation of the RetoSwap vault, the logic for registering an "Arbiter" (a trusted entity authorized to move funds) was flawed:

Solidity

function registerArbiter(address \_newArbiter) external {

// Missing access control! 

// Anyone could call this and assign themselves as the arbiter.

arbiter = \_newArbiter;

isAuthorized\[\_newArbiter\] = true;

}

Because there was no onlyOwner modifier, any user could invoke this function to hijack the administrative role and gain immediate withdrawal rights.

1. Proof of Concept (PoC) To prove this, I used Foundry to simulate an attack. By using vm.prank, I could impersonate a malicious actor and execute the unauthorized registration:

Solidity

function testExploitArbiterRegistration() public {

// Malicious actor registers themselves

vm.prank(hacker);

vault.registerArbiter(hacker);

```
// Malicious actor drains the vault
vm.prank(hacker);
vault.withdraw(10 ether);
assertEq(address(vault).balance, 0);
```
}

The test confirmed: the vault was drained in a single transaction.

1. The Solution: Defense in Depth To fix this, we didn't just add a modifier; we implemented a multi-layered security approach:

Access Control: We added the onlyOwner modifier to ensure only the deployer can manage administrative roles.

Whitelist (Allowed Addresses): Even if an Arbiter is compromised, they can now only withdraw funds to a pre-approved treasury address.

Solidity

function withdraw(address to, uint256 amount) external {

require(isAuthorized\[msg.sender\], "Not an arbiter");

require(allowedWithdrawalAddresses\[to\], "Address not allowed"); // Whitelist check

```
payable(to).transfer(amount);
```
}

1. Key Takeaways for Auditors Negative Testing is Crucial: Don't just test that your code works; use vm.expectRevert to prove it fails when it's supposed to.

Restrict the Blast Radius: Even if one part of your system (like the Arbiter role) is compromised, your whitelist acts as a secondary shield.

Cleanliness Matters: Always use git correctly, maintain a clean .gitignore, and document your fixes clearly.

Final Results

After applying these fixes, all tests pass, and the exploit is successfully mitigated.

You can find the full code, documentation, and the PoC exploit in my repository:

👉 [https://github.com/rdin777/RetoSwap-Audit](https://github.com/rdin777/RetoSwap-Audit)

Have you encountered similar logic flaws in your audits? Let's discuss in the comments!

## Top comments (0)
