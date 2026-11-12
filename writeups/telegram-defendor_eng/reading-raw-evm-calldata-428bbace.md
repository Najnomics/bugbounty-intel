# 🔐 EVM Calldata Decoded: Essential for DeFi Security

- **Source URL:** https://degatchi.com/articles/reading-raw-evm-calldata
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/81 (id 81)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reversing The EVM: Raw Calldata

8 min read

You may have have wondered how to decipher and read evm calldata, then attempted to read the transaction calldata of an Ethereum smart contract, only to become confused at a certain point. The EVM (and other L1 forks) encode and decode calldata in a specific way for static and dynamic types, which can be initially confusing. In this article, we will delve into the encoding sequence of calldata so that you can comprehend any verified or unverified smart contract transactions and understand the bytes. By doing so, I hope to empower you to create your own raw calldata.

## What Is Calldata?

Calldata is the encoded parameters that we send to functions, in this case to smart contracts on the Ethereum Virtual Machine (EVM). Each piece of calldata is 32 bytes long, or 64 characters. There are two types of calldata: static and dynamic.

Static variables are fairly straightforward to understand. Dynamic variables, on the other hand, are much more complex, and this is likely the reason why you may have difficulty reading raw calldata intuitively. However, once we go through how dynamic variables work, you will be able to read raw calldata with ease.

To begin, let’s understand how calldata is encoded and decoded to establish a foundation of how it all works.

## Encoding Calldata

To encode types, you can pass them into the \`abi.encode(parameters)“ method to generate raw calldata.

If you want to encode calldata for a specific interfaced function, you can use abi.encodeWithSelector(selector, parameters). This will be the same as passing in the function and it’s parameters directly.

For example:

The method `.selector` generates the 4-bytes that represents that method on the interface. We use it
to tell the EVM that we’re sending our calldata to that function. This is how UniswapV2 enables
flashswaps!

There is also `abi.encodePacked(...)` which is efficiently put all dynamic variables with eachother,
removing the 0 padding. The problem with it is that it doens’t prevent collisions and should only be
used when you know for certain the types and lengths of the parameters.

## Decoding calldata

So you have your calldata, how do you decode it?

If the calldata was created with `abi.encode(...)` then we can decode the parameters with
`abi.decode(...)` by passing in the parameters we want to decode the calldata into.

For example:

Where `data` represents the calldata being passed in.

Now that we understand how to encode and decode parameters, we can move onto the different variable types and how they are reflected in the calldata output.

## Static Variables

Static variables are simply the encoded representation of the following types: `uint`s, `int`s,
`address`, `bool`, `bytes1` to `bytes32` (including function selector), and `tuple`s (however they
can have dynamic variables in them).

For example, lets say we’re interacting with the following contract:

With the input parameters:

We would generate the calldata:
`0x000000000000000000000000000000000000000000000000000000004d866d9200000000000000000000000068b3465833fb72a70ecdf485e0e4c7bd8665fc45`

But… how tf do we read this?

Well, lets chop it up into readable pieces, by first removing the prefix `0x` and then breaking each
line into 64 character (or 32 byte) parts

Cool, now we know the first 32-bytes is the `uint256 amount` variable and the 2nd 32-bytes is the
`address to` one.

## Functions

But what if we wanted to call the `transfer` function directly?

We would need to know what parameters types takes in order and use a hashing mechanism called
`keccak256` which turns the inputted data into a 32-byte hash.

In this case, to hash:

We would do:

Which would return the following 32-byte hash:

To get the function signature we only need the first 4-bytes (or 8 characters, excluding the `0x`
prefix), `b7760c8f`.

This 4-byte signature, `b7760c8f`, is how we tell the EVM that we’re interacting with that function
and the following calldata is being passed in as parameters.

For example, if we were to call `transfer` with the same parameters as before in # Static Variables
we would grab the existing calldata:

And add `b7760c8f` to the start of the first 4 bytes of the first 32-bytes:

or

You may be wondering, how is the calldata parameter actually inputted into the function with the embedded signature?

The answer is, the contract’s bytecode reads it by targetting the function `b7760c8f`, then
replacing it with `00000000` padding then passing in the parameter.

## Dynamic Variables

Dynamic variables are non-fixed-size types, including `bytes`, `string`, and dynamic arrays `<T>[]`,
as well as fixed arrays `<T>[N]`.

The structure of dynamic types always starts with an offset, which is the hexadecimal representation
of where the dynamic type begins. For example, a hex of `20` represents `32-bytes`. Once we reach
the offset, there is a smaller number that represents the length of the type.

Tldr; 1st 32-bytes = offset, 2nd 32-bytes = length, the rest are elements.

For arrays, this length represents the number of elements contained in the array. For bytes and
string types, it represents the length of the type. For example, the string `"Hello World!"` is
12-bytes long, with each character being 1-byte. Keep in mind that these types start on the
left-hand side of the calldata, rather than the right-hand side like everything else.

For example, here’s the `string` `"Hello World!"` encoded:

Observe how the first 32-bytes represents the hexadecimal offset of `20`, which is `32` in decimal.
So we skip 32-bytes from the start of
`0000000000000000000000000000000000000000000000000000000000000020`, bringing us to the next line
with a hex of `0c`, a decimal of `12`, representing length of our `string` in bytes. Now when we
convert `48656c6c6f20576f726c6421` to a `string` type it returns our original value.

Congrats! Now you know how to read dynamic types.

## Decoding Static And Dynamic Parameters

Lets say we’re interacting with the following contract:

With the following parameters for `transfer`:

We would generate the calldata:
`0x8229ffb60000000000000000000000000000000000000000000000000000000000000040000000000000000000000000f8e81d47203a594245e36c48e151709f0c19fbe8000000000000000000000000000000000000000000000000000000000000000300000000000000000000000000000000000000000000000000000000000004d200000000000000000000000000000000000000000000000000000000000011d700000000000000000000000000000000000000000000000000000000000022ce`

We can chop this up into a more readable form:

Notice how the array parameter is represented by an offset to where the array begins. Then we move
onto the second param, the `address` type, then finishing off the array type.

Now that we know how to read both static + dynamic parameters, let’s dissect a more complex example!

## Decoding A Multicall’s Calldata

We’re going to be a UniswapV3 multicall’s input calldata from
[this](https://etherscan.io/tx/0x31a45e8893f0cc7de009da5546539f703ed725d076ccdf73d307df5caa8c72b3)
transaction. Here the user calls 3 different functions from the multicall function.

Etherscan is nice enough to give us a simple decoded version:

We will modify this a bit and expand upon this line-by-line to make it even more readable. Keep in
mind, each value is in hexadecimal format and `20 hex == 32-bytes` for quick reference.

Now you’re able to read raw embedded dynamic types!

## Final

I hope this information has helped you understand how calldata is encoded, decoded, and read. It took me some time to research and experiment with it all in order to learn, but it was worth it. The next step from here is to learn how to read bytecode in order to understand the EVM at its lowest level (Then everything becomes open-source >:D).

I appreciate you for taking the time to read this article. I hope you found value in this, anon!

Share this Article

## Recent Articles

-  Overcoming Mental Warfare When does pain stop? This constant back and forth of two titans colliding conscious never seens to let up...Will I ever escape? I must confront them, even if it means I will lose myself in the process. Fear not death but to live a life with undecisiveness.
-  Numbing Persistance There is nothing you can do but endure and persist to grasp those dreams from many moons ago. It feels mind numbing, all this effort. Maybe one day you'll reach it but at what cost? Was it worth it? All that pain and suffering, for what cause? Are you fighting to survive or is this thought play for you? For me, it's survival. Without it I would have nothing, but to rot in my mind as time drifts by.
-  A Warrior's Journey Deciding to become who you want to be is no easy feat. You are destined to battle the strongest of enemies on that path, sometimes with friends but majority of the time alone. What does the mind of one that is walking this path for the second time look like?
