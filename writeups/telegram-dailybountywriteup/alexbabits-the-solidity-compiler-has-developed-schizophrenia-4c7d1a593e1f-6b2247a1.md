# The Solidity Compiler has Developed Schizophrenia

- **Source URL:** https://medium.com/@alexbabits/the-solidity-compiler-has-developed-schizophrenia-4c7d1a593e1f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821173906/https://medium.com/@alexbabits/the-solidity-compiler-has-developed-schizophrenia-4c7d1a593e1f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10387 (id 10387)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Solidity Compiler has Developed Schizophrenia

Please take a seat, anon. We need to have a discussion about the health of your solidity compiler.

Disclaimer: 90% shitpost, 10% education

## Part 1 — Arithmetic

One of the illnesses found in the solidiy compiler relates directly to the concepts in [“Fixed point and real arithmetic are more different than you think”](https://100proof.org/eighteen-decimals-not-approx-real-arith.html), written by the legend [100Proof](https://immunefi.com/profile/IAm100proof/) himself.

I highly recommend reading it, especially if you’d like a detailed look at the technical differences between **integer** and **rational** arithmetic before continuing.

Briefly,

- **integer arithmetic** truncates results during division because non-integer decimal outputs are forbidden. For example, when calculating `34 * (100 / 34)`, we first calcualte `100/34` which is `2.94`. Because decimals are not allowed, this gets truncated down to `2`. Then we proceed with `34 * 2 = 68`. A surprising result, but this is how integer maths is done.
- **rational arithmetic** allows for any numeric output we want. This is your normal math. `34 * (100 / 34) = 100`. A pure result due to a lack of truncation during divison.

The Solidity Compiler (SOLC) is flexible enough to perform both integer and rational arithmetic, acknowledged in the solidity docs [here](https://docs.soliditylang.org/en/v0.8.30/types.html#rational-and-integer-literals).

From my understanding,

- The compiler uses **rational arithmetic** anytime a mathematical expression is deemed to be **literal** and can be precomputed before runtime.
- The compiler uses **integer arithmetic** anytime a mathematical expression is deemed **not a literal** and cannot be precomputed before runtime.

The following arithmetic related problems arise because the compiler fails to gracefully maintain consistent harmony with it’s duality of arithmetic. It gets confused about when to use integer or rational arithmetic.

Let:

```
    uint256 constant CONSTANT_IN = 34e34;
    uint256 constant CONSTANT_E18 = 1e18;
    uint256 constant CONSTANT_E36 = 1e36;
    uint256 immutable immutable_in; // 34e34
    uint256 immutable immutable_e18; // 1e18
    uint256 immutable immutable_e36; // 1e36
    uint256 public state_in; // 34e34
    uint256 public state_e18; // 1e18
    uint256 public state_e36; // 1e36
```
1. Argument assignment (literal vs non-literal):

```
// let input = 34e16
functoin foo(uint256 input) public view returns (uint256, uint256) {
  uint256 out1 = 34e16 * (1e18 / 34e16); // 1e18
  uint256 out2 = input * (1e18 / input); // 0.68e18
}
```
Notice how both mathematically equivalent expressions have two drastically different results. This result is technically “expected” but unnerving.

2\. Substitution

```
    function substitution(uint256 inputParam) public view returns (uint256, uint256, uint256, uint256) {
        uint256 out1 = uint256(immutable_in * (immutable_e36 / immutable_in) / immutable_e18); // 0.68e18
        uint256 out2 = uint256(CONSTANT_IN * (CONSTANT_E36 / CONSTANT_IN) / CONSTANT_E18); // 0.68e18
        uint256 out3 = uint256(34e34 * (CONSTANT_E36 / 34e34) / 1e18); // 0.68e18
        uint256 out4 = uint256(34e34 * (1e36 / 34e34) / CONSTANT_E18); // 1e18
        // Note: If you substitute the first term with a constant/immutable, it doesn't compile
        //uint256 out5 = uint256(CONSTANT_IN * (1e36 / 34e34) / 1e18);
        //uint256 out6 = uint256(IMMUTABLE_IN * (1e36 / 34e34) / 1e18);
        return (out1, out2, out3, out4);
    }
```
We see all mathematical expressions are equivalent, but output three different results: 1e18, 0.68e18, and does not compile. Just like substitute teachers, you have no clue if you’re getting the hot chick, the angry 63 year old with bags sagging to the floor, or the one that doesn’t even show up.

3\. Casting

```
    function casting() public pure returns (uint256, uint256, uint256, uint256, uint256, uint256, uint256) {
        uint256 out1 = uint256(34e16 * (1e18 / 34e16)); // 1e18
        uint256 out2 = uint256(34e16 * (uint256(1e18) / 34e16)); // 0.68e18
        uint256 out3 = uint256(34e16 * (1e18 / uint256(34e16))); // 0.68e18
        // Note: If you cast the first term in the following expression, it doesn't compile
        //uint256 out4 = uint256(uint256(34e16) * (1e18 / 34e16));
        uint256 out4 = uint256(34e34 * (1e36 / 34e34) / 1e18); // 1e18
        uint256 out5 = uint256(34e34 * (1e36 / 34e34) / uint256(1e18)); // 1e18
        uint256 out6 = uint256(34e34 * (1e36 / uint256(34e34)) / 1e18); // 0.68e18
        uint256 out7 = uint256(34e34 * (uint256(1e36) / 34e34) / 1e18); // 0.68e18
        // Note: If you cast the first term in the following expression, it doesn't compile
        //uint256 out8 = uint256(uint256(34e34) * (1e36 / 34e34) / 1e18);
        return (out1, out2, out3, out4, out5, out6, out7);
    }
```
We see again three different results from mathematically equivalent expressions. Notice that by changing the casting location in an expression, we can change the type of arithmetic the compiler is performing, or whether it compiles at all. It’s kinda like a box of chocolates, or russian roulette.

4\. State substitution

```
    function stateWithoutCasting() public view returns (uint256, uint256, uint256) {
        uint256 out1 = (34e34 * (1e36 / 34e34) / state_e18); // 1e18
        uint256 out2 = (34e34 * (1e36 / state_in) / 1e18); // 0.68e18
        uint256 out3 = (34e34 * (state_e36 / 34e34) / 1e18); // 0.68e18
        // Note: If you substitute the first term with state, it doesn't compile
        // uint256 out4 = (state_in * (1e36 / 34e34) / 1e18);
        return (out1, out2, out3);
    }
```
Notice even when state becomes involved, three mathematically equivalent expressions yield three different outcomes.

5\. Assembly

```
    function literalSolidityVsAssembly() public pure returns (uint256, uint256, uint256, uint256) {
        uint256 out1;
        uint256 out2;
        
        // assembly literal
        assembly {
            // (34e18 * (1e20 / 34e18)) / 100
            out1 := div(mul(34000000000000000000, div(100000000000000000000, 34000000000000000000)), 100) // 0.68e18
            // 34e34 * (1e36 / 34e34)
            out2 := mul(340000000000000000, div(1000000000000000000, 340000000000000000)) // 0.68e18 
        }
        // solidity literal
        uint256 out3 = (34e18 * (1e20 / 34e18)) / 100; // 1e18
        uint256 out4 = 34e16 * (1e18 / 34e16); // 1e18
        return (out1, out2, out3, out4);
    }
```
Perhaps the most stark example is shown above. Identical assembly and solidity literal expressions output different results. In my understanding, the absolute equivalence between assembly and higher level expressions must always be a maintained invariant.

Enough blackpills, let’s switch gears and check out the red-headed step child of EVM compilers — Vyper, and see how it handles this shit.

Turns out, Vyper handles integer and rational arithmetic in a surprisingly elegant fashion.

Vyper disallows rational arithmetic unless all are satisfied:

1. `--enable-decimals` flag is used.
2. Numbers are declared as `decimal` type.
3. literal number expressions have at least one value after the decimal.

Developers are required to explicitly “request” rational arithmetic through the checklist above, efficiently separating any unintended mixing of integer and rational arithmetic.

The developer must “invite” rational arithmetic into his domain. He knows when he’s working with rational arithmetic, and knows when he is not. There’s no way to stumble into one type of arithmetic or accidentally confuse the compiler.

Furthermore, even if he wants to mix integer and rational types, he cannot, as the compiler stops him from performing arithmetic between `decimal` and `uint256` types without an explicit `convert()` from one type to the other.

## Part 1 — Conclusion

In the SOLC compiler, none of these illnesses appear to be immediately exploitable at a critical level, but it is just kinda gross.

Like shitting your pants in public, or learning how McDonalds is made. And yet we still eat McDonalds while shitting our pants.

Note: Bug report was submitted but unsuccessful.

A meme is usually more efficient when trying to get the point accross to autists:

Gist for all Part 1 examples: [SOLC Problems](https://gist.github.com/alexbabits/0e56e0c91a124bddc59b01af4d9c9ef9)

## Part 2 — Constructor Inheritance with Legacy vs Via-IR

There is another illness discussed by [Danipopes](https://x.com/danipopes) and [Philogy](https://x.com/real_philogy) that relates to via-ir vs legacy compilation with respect to constructor outputs during inheritance.

The problem:

Full example code:


// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.29;


contract A {

uint public constructorArg;


constructor(uint _arg) {

constructorArg = _arg;

}

}


contract B is A {

uint x = 69;

constructor() A(x) {}

}



// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.29;


import {Test, console} from "forge-std/Test.sol";

import {A, B} from "../src/Example.sol";


contract ExampleTest is Test {


// Legacy: forge test --mt test_ConstructorBehavior -vv

// via-ir: FOUNDRY_PROFILE=via-ir forge test --mt test_ConstructorBehavior -vv

function test_ConstructorBehavior() public {

B b = new B();

console.log(b.constructorArg()); // legacy mode outputs 69, via-ir outputs 0

}

}




// Add this to foundry.toml:

via_ir = false


[profile.via-ir]

src = "src"

out = "out"

libs = ["lib"]

via_ir = true
Notice that there’s a schism between when a state variable is initialized:

- **Legacy** mode initializes ALL state vars in inheritance chain first (x=69), then runs constructors from base → derived, so A(x) gets x=69.
- **Via-IR** mode (intermediate representation compilation which goes through Yul before bytecode) operates as follows: For each contract base → derived it initializes that contract’s state variables, and then runs the contract’s constructor. So when A(x) runs, state variables from Contract B haven’t been initialized, meaning x=0

The silent runtime behavior documentation can be found [here](https://docs.soliditylang.org/en/latest/ir-breaking-changes.html).

## Final Conclusion

If anyone has any other greivous examples or bad quirks that compilers shouldn’t do, but SOLC does, share them!

In my understanding, none of this should be acceptable for a solidity compiler at version 1, but as long as the illness doesn’t immediately cause millions or billions of dollars to be lost, nobody cares.

Overall, neither of these schizophrenic tendencies of SOLC are critically severe. But it does beg the question, how many more illnesses are hidden in the solidity compiler, and are any of them a ticking time bomb?
