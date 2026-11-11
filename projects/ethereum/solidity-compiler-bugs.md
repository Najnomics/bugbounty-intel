# Solidity compiler bug list (canonical)

_67 known Solidity compiler bugs, verbatim from the canonical list the compiler team maintains: https://github.com/ethereum/solidity/blob/develop/docs/bugs.json (fetched 2026-11-11 WAT). Each entry: when it was introduced/fixed, severity, and the conditions that trigger it. A harness can map a contract's pragma/compiler version to the bugs that affect it. Data, not instructions._

| Name | Severity | Introduced | Fixed | Summary |
| --- | --- | --- | --- | --- |
| YulOptimizerKnowledgeBaseStaleBookkeeping | low | 0.8.19 | 0.8.38 | The Yul optimizer could consider two memory or storage locations distinct even though thei |
| MisorderedNamedParametersInRequireWithCustomErrors | very low | 0.8.26 | 0.8.37 | Custom error arguments passed to ``require`` using named-parameter syntax are ABI-encoded  |
| MemoryByteArrayElementDeleteClearsWholeWord | low/medium |  | 0.8.37 | Applying ``delete`` to a single element of a ``bytes`` array in memory clears not only tha |
| SpillSlotCollisionAcrossMutualRecursion | low/medium | 0.7.2 | 0.8.37 | Local variables of two simultaneously active functions moved to fixed memory offsets by th |
| InheritanceOrderReversalOnStorageEndWarning | medium | 0.8.29 | 0.8.36 | Emitting a warning about storage base location being too close to the storage end unintent |
| UnsoundSpillInMutualRecursion | medium | 0.7.2 | 0.8.36 | Local variables of a function involved in mutual recursion may spuriously be moved to fixe |
| TransientStorageClearingHelperCollision | high | 0.8.28 | 0.8.34 | Clearing both storage and transient storage variables in the same contract may result in o |
| LostStorageArrayWriteOnSlotOverflow | low | 0.1.0 | 0.8.32 | Operations that involve clearing or copying from arrays that straddle the end of storage c |
| VerbatimInvalidDeduplication | low | 0.8.5 | 0.8.23 | All ``verbatim`` blocks are considered identical by deduplicator and can incorrectly be un |
| FullInlinerNonExpressionSplitArgumentEvaluationOrder | low | 0.6.7 | 0.8.21 | Optimizer sequences containing FullInliner do not preserve the evaluation order of argumen |
| MissingSideEffectsOnSelectorAccess | low | 0.6.2 | 0.8.21 | Accessing the ``.selector`` member on complex expressions leaves the expression unevaluate |
| StorageWriteRemovalBeforeConditionalTermination | medium/high | 0.8.13 | 0.8.17 | Calling functions that conditionally terminate the external EVM call using the assembly st |
| AbiReencodingHeadOverflowWithStaticArrayCleanup | medium | 0.5.8 | 0.8.16 | ABI-encoding a tuple with a statically-sized calldata array in the last component would co |
| DirtyBytesArrayToStorage | low | 0.0.1 | 0.8.15 | Copying ``bytes`` arrays from memory or calldata to storage may result in dirty storage va |
| InlineAssemblyMemorySideEffects | medium | 0.8.13 | 0.8.15 | The Yul optimizer may incorrectly remove memory writes from inline assembly blocks, that d |
| DataLocationChangeInInternalOverride | very low | 0.6.9 | 0.8.14 | It was possible to change the data location of the parameters or return variables from ``c |
| NestedCalldataArrayAbiReencodingSizeValidation | very low | 0.5.8 | 0.8.14 | ABI-reencoding of nested dynamic calldata arrays did not always perform proper size checks |
| AbiEncodeCallLiteralAsFixedBytesBug | very low | 0.8.11 | 0.8.13 | Literals used for a fixed length bytes parameter in ``abi.encodeCall`` were encoded incorr |
| UserDefinedValueTypesBug | very low | 0.8.8 | 0.8.9 | User defined value types with underlying type shorter than 32 bytes used incorrect storage |
| SignedImmutables | very low | 0.6.5 | 0.8.9 | Immutable variables of signed integer type shorter than 256 bits can lead to values with i |
| ABIDecodeTwoDimensionalArrayMemory | very low | 0.4.16 | 0.8.4 | If used on memory byte arrays, result of the function ``abi.decode`` can depend on the con |
| KeccakCaching | medium |  | 0.8.3 | The bytecode optimizer incorrectly reused previously evaluated Keccak-256 hashes. You are  |
| EmptyByteArrayCopy | medium |  | 0.7.4 | Copying an empty byte array (or string) from memory or calldata to storage can result in d |
| DynamicArrayCleanup | medium |  | 0.7.3 | When assigning a dynamically-sized array with types of size at most 16 bytes in storage ca |
| FreeFunctionRedefinition | low | 0.7.1 | 0.7.2 | The compiler does not flag an error when two or more free functions with the same name and |
| UsingForCalldata | very low | 0.6.9 | 0.6.10 | Function calls to internal library functions with calldata parameters called via ``using f |
| MissingEscapingInFormatting | very low | 0.5.14 | 0.6.8 | String literals containing double backslash characters passed directly to external or enco |
| ArraySliceDynamicallyEncodedBaseType | very low | 0.6.0 | 0.6.8 | Accessing array slices of arrays with dynamically encoded base types (e.g. multi-dimension |
| ImplicitConstructorCallvalueCheck | very low | 0.4.5 | 0.6.8 | The creation code of a contract that does not define a constructor but has a base that doe |
| TupleAssignmentMultiStackSlotComponents | very low | 0.1.6 | 0.6.6 | Tuple assignments with components that occupy several stack slots, i.e. nested tuples, poi |
| MemoryArrayCreationOverflow | low | 0.2.0 | 0.6.5 | The creation of very large memory arrays can result in overlapping memory regions and thus |
| YulOptimizerRedundantAssignmentBreakContinue | medium | 0.6.0 | 0.6.1 | The Yul optimizer can remove essential assignments to variables declared inside for loops  |
| privateCanBeOverridden | low | 0.3.0 | 0.5.17 | Private methods can be overridden by inheriting contracts. |
| YulOptimizerRedundantAssignmentBreakContinue0.5 | low | 0.5.8 | 0.5.16 | The Yul optimizer can remove essential assignments to variables declared inside for loops  |
| ABIEncoderV2LoopYulOptimizer | low | 0.5.14 | 0.5.15 | If both the experimental ABIEncoderV2 and the experimental Yul optimizer are activated, on |
| ABIEncoderV2CalldataStructsWithStaticallySizedAndDynamicallyEncodedMembers | low | 0.5.6 | 0.5.11 | Reading from calldata structs that contain dynamically encoded, but statically-sized membe |
| SignedArrayStorageCopy | low/medium | 0.4.7 | 0.5.10 | Assigning an array of signed integers to a storage array of different type can lead to dat |
| ABIEncoderV2StorageArrayWithMultiSlotElement | low | 0.4.16 | 0.5.10 | Storage arrays containing structs or other statically-sized arrays are not read properly w |
| DynamicConstructorArgumentsClippedABIV2 | very low | 0.4.16 | 0.5.9 | A contract's constructor that takes structs or arrays that contain dynamically-sized array |
| UninitializedFunctionPointerInConstructor | very low | 0.5.0 | 0.5.8 | Calling uninitialized internal function pointers created in the constructor does not alway |
| UninitializedFunctionPointerInConstructor_0.4.x | very low | 0.4.5 | 0.4.26 | Calling uninitialized internal function pointers created in the constructor does not alway |
| IncorrectEventSignatureInLibraries | very low | 0.5.0 | 0.5.8 | Contract types used in events in libraries cause an incorrect event signature hash |
| IncorrectEventSignatureInLibraries_0.4.x | very low | 0.3.0 | 0.4.26 | Contract types used in events in libraries cause an incorrect event signature hash |
| ABIEncoderV2PackedStorage | low | 0.5.0 | 0.5.7 | Storage structs and arrays with types shorter than 32 bytes can cause data corruption if e |
| ABIEncoderV2PackedStorage_0.4.x | low | 0.4.19 | 0.4.26 | Storage structs and arrays with types shorter than 32 bytes can cause data corruption if e |
| IncorrectByteInstructionOptimization | very low | 0.5.5 | 0.5.7 | The optimizer incorrectly handles byte opcodes whose second argument is 31 or a constant e |
| DoubleShiftSizeOverflow | low | 0.5.5 | 0.5.6 | Double bitwise shifts by large constants whose sum overflows 256 bits can result in unexpe |
| ExpExponentCleanup | medium/high |  | 0.4.25 | Using the ** operator with an exponent of type shorter than 256 bits can result in unexpec |
| EventStructWrongData | very low | 0.4.17 | 0.4.25 | Using structs in events logged wrong data. |
| NestedArrayFunctionCallDecoder | medium | 0.1.4 | 0.4.22 | Calling functions that return multi-dimensional fixed-size arrays can result in memory cor |
| OneOfTwoConstructorsSkipped | very low | 0.4.22 | 0.4.23 | If a contract has both a new-style constructor (using the constructor keyword) and an old- |
| ZeroFunctionSelector | very low |  | 0.4.18 | It is possible to craft the name of a function such that it is executed instead of the fal |
| DelegateCallReturnValue | low | 0.3.0 | 0.4.15 | The low-level .delegatecall() does not return the execution outcome, but converts the valu |
| ECRecoverMalformedInput | medium |  | 0.4.14 | The ecrecover() builtin can return garbage for malformed input. |
| SkipEmptyStringLiteral | low |  | 0.4.12 | If "" is used in a function call, the following function arguments will not be correctly p |
| ConstantOptimizerSubtraction | low |  | 0.4.11 | In some situations, the optimizer replaces certain numbers in the code with routines that  |
| IdentityPrecompileReturnIgnored | low |  | 0.4.7 | Failure of the identity precompile was ignored. |
| OptimizerStateKnowledgeNotResetForJumpdest | medium | 0.4.5 | 0.4.6 | The optimizer did not properly reset its internal state at jump destinations, which could  |
| HighOrderByteCleanStorage | high | 0.1.6 | 0.4.4 | For short types, the high order bytes were not cleaned properly and could overwrite existi |
| OptimizerStaleKnowledgeAboutSHA3 | medium |  | 0.4.3 | The optimizer did not properly reset its knowledge about SHA3 operations resulting in some |
| LibrariesNotCallableFromPayableFunctions | low | 0.4.0 | 0.4.2 | Library functions threw an exception when called from a call that received Ether. |
| SendFailsForZeroEther | low |  | 0.4.0 | The send function did not provide enough gas to the recipient if no Ether was sent with it |
| DynamicAllocationInfiniteLoop | low |  | 0.3.6 | Dynamic allocation of an empty memory array caused an infinite loop and thus an exception. |
| OptimizerClearStateOnCodePathJoin | low |  | 0.3.6 | The optimizer did not properly reset its internal state at jump destinations, which could  |
| CleanBytesHigherOrderBits | medium/high |  | 0.3.3 | The higher order bits of short bytesNN types were not cleaned before comparison. |
| ArrayAccessCleanHigherOrderBits | medium/high |  | 0.3.1 | Access to array elements for arrays of types with less than 32 bytes did not correctly cle |
| AncientCompiler | high |  | 0.3.0 | This compiler version is ancient and might contain several undocumented or undiscovered bu |

---

## YulOptimizerKnowledgeBaseStaleBookkeeping

- **Severity:** low
- **Introduced:** 0.8.19  **Fixed:** 0.8.38

- **Trigger conditions:** {"yulOptimizer": true}
- **More info:** https://blog.soliditylang.org/2026/10/22/yul-optimizer-knowledge-base-stale-bookkeeping-bug/

**Summary:** The Yul optimizer could consider two memory or storage locations distinct even though their addresses were computed from different values of the same reassigned variable and coincided at runtime. This could lead to loads being replaced with outdated values and to needed stores being removed.

**Description:** The Yul optimizer steps ``LoadResolver`` and ``EqualStoreEliminator`` keep track of what was stored in memory and storage. ``LoadResolver`` uses this to replace loads and ``keccak256`` calls with known values, and ``EqualStoreEliminator`` uses it to remove stores of a value that the location already contains. Whenever a store is encountered whose exact location cannot be determined, the optimizer has to forget what it knows about every location the store might overwrite. To decide this, the optimizer represents an address symbolically as a constant offset either from zero or from another variable (its base variable). Two addresses with the same base can then be determined to be distinct if their offsets differ (for storage) or are at least 32 bytes apart (for memory). These representations were cached per variable. The base variable, however, may be reassigned afterwards. The optimizer did not always notice and then compared an address computed from the old value of the base with an address computed from the new value as if both used the same base. As a result, it could consider two locations distinct even though they coincided at runtime, keeping a stale entry for a location that had just been overwritten. A subsequent load from that location could then be replaced with an outdated value, a subsequent store of that value to the location could be removed, and ``keccak256`` over the location could be replaced with the hash of an outdated value. Whether the bug is triggered depends on the structure of the intermediate code these optimizer steps receive. It is therefore sensitive to the optimizer sequence and to the surrounding code, and the two locations additionally have to coincide at runtime. In optimized IR code generation, any code may be affected, including code without inline assembly. In optimized evmasm code generation, only inline assembly that does not refer to any Solidity variables or functions and compiler-generated Yul utility functions could be affected. Unoptimized code is unaffected.

## MisorderedNamedParametersInRequireWithCustomErrors

- **Severity:** very low
- **Introduced:** 0.8.26  **Fixed:** 0.8.37

- **Trigger conditions:** {"viaIR": true}
- **More info:** https://blog.soliditylang.org/2026/09/10/misordered-named-parameters-in-require-with-custom-errors-bug/

**Summary:** Custom error arguments passed to ``require`` using named-parameter syntax are ABI-encoded in call-site order instead of declaration order when compiling via IR.

**Description:** When a custom error was passed into the second argument of ``require`` and instantiated using named parameter syntax (e.g., ``require(condition, MyError({b: 1, a: 2}))``), the IR-based code generator would pass the arguments to the ABI encoder in the order they appeared at the call site, without reordering them to match the error definition. The arguments were type-checked against the parameters with matching names, not the ones they were actually passed into by the codegen, so the bug would not result in a compilation error. Instead, the encoder would produce a structurally valid encoding matching the error signature but not reflecting the values used to instantiate the error. The arguments on the stack would be reordered and possibly reinterpreted as different types by the encoder. In case of reference types, the reinterpretation would result in the content being obtained from wrong offsets in memory, storage or calldata. In some cases large values misinterpreted as offsets or lengths would make the encoder revert due to running out of gas. Types that occupy more than one slot on the stack would further complicate the behavior by leading to not only reordering but also misalignment of argument boundaries. The only unaffected types were string literals, which are not being passed to the encoder through the stack. The bug was specific to custom errors passed as the second argument of ``require``. Standalone ``revert ErrorName({...})`` statements, event emissions, function calls, struct constructor invocations and other constructs supporting named parameters were not affected. The evmasm pipeline was also unaffected.

## MemoryByteArrayElementDeleteClearsWholeWord

- **Severity:** low/medium
- **Introduced:** (unknown)  **Fixed:** 0.8.37

- **Trigger conditions:** {"viaIR": false}
- **More info:** https://blog.soliditylang.org/2026/09/10/memory-byte-array-element-delete-clears-whole-word-bug/

**Summary:** Applying ``delete`` to a single element of a ``bytes`` array in memory clears not only that element but the whole 32-byte word starting at the element's location, zeroing up to 31 bytes beyond the element.

**Description:** Elements of ``bytes`` arrays in memory are packed, each occupying a single byte. When a value is assigned to such an element, the evmasm code generator correctly stores it with a single-byte ``MSTORE8`` instruction. The code path in the evmasm pipeline implementing ``delete`` on such an element, however, wrote the zero value with a full-word ``MSTORE``, clearing the 32 bytes starting at the element's location. The bytes following the element within the array were silently zeroed. If the element was within the last 31 bytes of the array's allocation, the write also extended past it into the area where the allocator places the next memory object, clearing the most significant bytes of that object's first word. How many elements are in reach depends on the size of the allocation: arrays created with ``new bytes(n)`` or from literals occupy their length rounded up to a multiple of 32 bytes, so only elements falling within the last 31 bytes of that rounded-up area, if any, could be affected. The results of ``bytes.concat``, ``string.concat``, and the ``abi.encode*`` functions, on the other hand, are placed by the evmasm pipeline in an allocation of exactly the size of their data, so the next object starts immediately after their last element and each of their last 31 elements is in reach. Assigning zero to an element (``b[i] = 0``) was not affected, only the ``delete`` operator, and neither were byte arrays in transient storage, storage, or calldata. The bug exists only in the evmasm pipeline. Code compiled via IR is unaffected. Optimizer settings have no influence. The defective code predates the first released version of the compiler.

## SpillSlotCollisionAcrossMutualRecursion

- **Severity:** low/medium
- **Introduced:** 0.7.2  **Fixed:** 0.8.37

- **Trigger conditions:** {"viaIR": true}
- **More info:** https://blog.soliditylang.org/2026/09/10/spill-slot-collision-across-mutual-recursion-bug/

**Summary:** Local variables of two simultaneously active functions moved to fixed memory offsets by the stack limit evader may be assigned the same offset if the call graph contains mutual recursion, so that one variable is silently overwritten by the other.

**Description:** To work around the 16-slot stack access limit of the EVM, the IR-based code generator can, under some preconditions, move local variables to fixed memory offsets. Variables that can never be active at the same time may safely share an offset, so the reserved memory area is sized by a depth-first walk of the call graph that computes for every node the number of slots it and its callees need. To keep this walk from descending infinitely into recursive call chains, the slot count was initialized with zero upon entering it. This provisional zero was observable: a function reached again through a call graph cycle reported an empty footprint to its caller, the caller's count was finalized and cached on that basis, and the undercount propagated to every later caller, including functions outside the cycle. As a result, a function called by such a cycle and a function calling into it could be assigned the same memory slot even though both can be active at the same time. A relocated variable still needed after the call into the cycle returned had then been silently overwritten by the called function, producing wrong results. Triggering the bug requires the IR pipeline and a call graph in which a cycle of at least two mutually recursive functions both reaches a function needing relocation of variables to memory and is entered from a separate call chain whose own relocated variable is read again after the call towards the cycle returns. From 0.8.21 onward, it is independent of whether the optimizer is enabled.

## InheritanceOrderReversalOnStorageEndWarning

- **Severity:** medium
- **Introduced:** 0.8.29  **Fixed:** 0.8.36


- **More info:** https://blog.soliditylang.org/2026/07/09/inheritance-order-reversal-on-storage-end-warning-bug/

**Summary:** Emitting a warning about storage base location being too close to the storage end unintentionally reversed the ``linearizedBaseContracts`` annotation, possibly leading to miscompilation due to reversing the order in which inheritance is resolved.

**Description:** When the compiler detects that a custom layout specifier puts contract's static storage area too close to the end of the address space, it emits a warning. To make the warning more useful, the compiler tries to point at the last storage variable in that area. For this reason it walks the linearized inheritance hierarchy in reverse (from the least to the most derived). The list is calculated once and stored in an AST annotation called ``linearizedBaseContracts``. The direct cause of the bug was the fact that the code that reverses the list was doing it in place rather than on a copy, modifying the annotation. This effectively reversed the order of base contracts seen by any component that runs after layout checks: later phases of analysis, AST export, code generator, SMTChecker, etc. The observable effect was a reversed order of state variable initialization, constructor invocation, virtual function/modifier resolution, leading either to miscompilations or internal compiler errors, depending on the specific usage. Since the source of the bug was in the analysis stage, it was independent of the codegen pipeline or optimizer settings. The main condition necessary to trigger the bug was the presence of the warning in the output. The other is presence of language constructs whose evaluation depends on the inheritance order. While potential effects are very serious, this requirement excludes the vast majority of contracts as intentionally placing the storage variables in the last 2**64 slots is highly discouraged, which was actually the main reason for adding this warning.

## UnsoundSpillInMutualRecursion

- **Severity:** medium
- **Introduced:** 0.7.2  **Fixed:** 0.8.36

- **Trigger conditions:** {"viaIR": true}
- **More info:** https://blog.soliditylang.org/2026/07/09/unsound-spill-in-mutual-recursion-bug/

**Summary:** Local variables of a function involved in mutual recursion may spuriously be moved to fixed memory offsets and overwritten across recursive calls.

**Description:** To work around the 16-slot stack access limit of the EVM, the IR-based code generator can move local variables of stack-too-deep functions to fixed memory offsets. This relocation is unsound for recursive functions: a fixed offset would be shared by all activations of the function, so a recursive call would overwrite the caller's value. The stack limit evader therefore must not relocate variables of functions that are part of a recursive call chain. To this end, the call graph was searched for cycles using a path-based depth-first search that, once a function had been fully explored and popped from the search path, short-circuited on it on any later visit. As a result, a function shared between several intersecting cycles could be reached first through a path that did not yet close a cycle through it, get marked as finished, and then be skipped when a later path would have revealed that it does lie on a cycle. Such a function was misclassified as non-recursive. When a misclassified function was complex enough for the stack limit evader to relocate some of its variables, those variables were moved to fixed memory offsets and silently corrupted on recursion, producing wrong results rather than a compile-time error. Triggering the bug requires the IR pipeline, a set of mutually recursive functions whose call graph contains intersecting cycles, at least one of the functions in an undetected part of a cycle being complex enough to require relocation to memory, and an unfortunate processing order of the functions (which depends on the hashes of their Yul names). It is independent of whether the optimizer is enabled.

## TransientStorageClearingHelperCollision

- **Severity:** high
- **Introduced:** 0.8.28  **Fixed:** 0.8.34

- **Trigger conditions:** {"viaIR": true, "evmVersion": ">=cancun"}
- **More info:** https://blog.soliditylang.org/2026/02/18/transient-storage-clearing-helper-collision-bug/

**Summary:** Clearing both storage and transient storage variables in the same contract may result in only one of these locations being cleared.

**Description:** The IR-based code generator provides a set of Yul helper functions for basic operations, such as clearing, copying, encoding or type conversions. Not all functions are used by every contract. The codegen appends them to the generated sources individually, only when an operation that would invoke one of them is encountered. Utility functions are often specialized for different types and locations. Since Yul does not support generic functions, specialization is done by generating multiple versions of the same function, with the information distinguishing the variants embedded in their names. However, if not all the necessary bits of distinguishing information are properly accounted for, two helpers may end up with the same name, causing a collision. In this situation the codegen includes only one of them, with calls to both variants invoking it. This happened with the ``set_to_zero`` helper used when an area of transient or persistent storage needs to be cleared. The helper name was missing the location information, which resulted in a collision between the persistent and transient storage variants for the same type. This meant that contracts clearing both locations would actually clear only one, leaving the other untouched. Which location ended up being cleared depended on the order in which the code generator processed the input. The necessary condition to trigger the bug was the use of ``delete`` operator on a transient storage variable. This was due to value types being the only types supported in transient storage and ``delete`` being the only operation invoking the helper allowed on such types. The other necessary condition was clearing of persistent storage and in this case the range of affected operations was wider: operator ``delete``, array ``pop()`` or assignment that resulted in a longer array being overwritten with a shorter one. The cleared variable itself also did not necessarily have to be of the same type. It was enough that a matching value type was nested in it. It also did not always have to be the exact same value type - clearing operations on reference types are usually performed at slot granularity, treating every slot as ``uint256`` rather than clearing every value packed into it individually. To trigger the bug both operations had to be present within the same piece of bytecode. Independent contracts, not related through inheritance, would not affect each other this way. The presence of one operation only in creation code and the other only in deployed code would not trigger the bug either.

## LostStorageArrayWriteOnSlotOverflow

- **Severity:** low
- **Introduced:** 0.1.0  **Fixed:** 0.8.32


- **More info:** https://blog.soliditylang.org/2025/12/18/lost-storage-array-write-on-slot-overflow-bug/

**Summary:** Operations that involve clearing or copying from arrays that straddle the end of storage could result in silent data retention.

**Description:** Solidity makes it possible to define variables that extend past the last (2**256-th) slot of storage, which results in wrap-around back to slot zero. Since EVM uses 256-bit integer arithmetic, most operations on such variables just work. The only situation which requires special attention is iteration against absolute slot addresses: the invariant that the last slot belonging to a variable has the highest address does not hold. When implemented incorrectly, a loop over an array will immediately terminate if the container spans the end of storage - due to the initial position already being greater than the end position. This affected storage array clearing loops generated by both evmasm and IR pipelines. Additionally, (only in the evmasm pipeline) copying operations whose source was an array straddling the end of storage were also affected. At the language level, the buggy code would be generated for array assignment, array initialization, delete operator, <array>.pop() and <array>.push(). Note that a clearing loop is inserted by the compiler not only for invocations of the delete operator, but also to zero storage when overwriting a longer array with a shorter one, popping an element or even pushing an empty element to a dynamic array. Since clearing is a separate loop, it is possible for the bug to only affect it and not the copy operation it follows (which is always the case in the IR pipeline). The bug is extremely unlikely to be triggered accidentally due to the probabilistic impossibility of a short dynamic array being allocated right at the storage boundary. On the other hand, scenarios in which a user may place a static array there intentionally do not seem realistic and are limited to unusual layouts, in which a contract does not place any storage variables at slot zero (otherwise they would overlap the array).

## VerbatimInvalidDeduplication

- **Severity:** low
- **Introduced:** 0.8.5  **Fixed:** 0.8.23


- **More info:** https://blog.soliditylang.org/2023/11/08/verbatim-invalid-deduplication-bug/

**Summary:** All ``verbatim`` blocks are considered identical by deduplicator and can incorrectly be unified when surrounded by identical opcodes.

**Description:** The block deduplicator is a step of the opcode-based optimizer which identifies equivalent assembly blocks and merges them into a single one. However, when blocks contained ``verbatim``, their comparison was performed incorrectly, leading to the collapse of assembly blocks which are identical except for the contents of the ``verbatim`` items. Since ``verbatim`` is only available in Yul, compilation of Solidity sources is not affected.

## FullInlinerNonExpressionSplitArgumentEvaluationOrder

- **Severity:** low
- **Introduced:** 0.6.7  **Fixed:** 0.8.21

- **Trigger conditions:** {"yulOptimizer": true}
- **More info:** https://blog.soliditylang.org/2023/07/19/full-inliner-non-expression-split-argument-evaluation-order-bug/

**Summary:** Optimizer sequences containing FullInliner do not preserve the evaluation order of arguments of inlined function calls in code that is not in expression-split form.

**Description:** Function call arguments in Yul are evaluated right to left. This order matters when the argument expressions have side-effects, and changing it may change contract behavior. FullInliner is an optimizer step that can replace a function call with the body of that function. The transformation involves assigning argument expressions to temporary variables, which imposes an explicit evaluation order. FullInliner was written with the assumption that this order does not necessarily have to match usual argument evaluation order because the argument expressions have no side-effects. In most circumstances this assumption is true because the default optimization step sequence contains the ExpressionSplitter step. ExpressionSplitter ensures that the code is in *expression-split form*, which means that function calls cannot appear nested inside expressions, and all function call arguments have to be variables. The assumption is, however, not guaranteed to be true in general. Version 0.6.7 introduced a setting allowing users to specify an arbitrary optimization step sequence, making it possible for the FullInliner to actually encounter argument expressions with side-effects, which can result in behavior differences between optimized and unoptimized bytecode. Contracts compiled without optimization or with the default optimization sequence are not affected. To trigger the bug the user has to explicitly choose compiler settings that contain a sequence with FullInliner step not preceded by ExpressionSplitter.

## MissingSideEffectsOnSelectorAccess

- **Severity:** low
- **Introduced:** 0.6.2  **Fixed:** 0.8.21

- **Trigger conditions:** {"viaIR": false}
- **More info:** https://blog.soliditylang.org/2023/07/19/missing-side-effects-on-selector-access-bug/

**Summary:** Accessing the ``.selector`` member on complex expressions leaves the expression unevaluated in the legacy code generation.

**Description:** When accessing the ``.selector`` member on an expression with side-effects, like an assignment, a function call or a conditional, the expression would not be evaluated in the legacy code generation. This would happen in expressions where the functions used in the expression were all known at compilation time, regardless of whether the whole expression could be evaluated at compilation time or not. Note that the code generated by the IR pipeline was unaffected and would behave as expected.

## StorageWriteRemovalBeforeConditionalTermination

- **Severity:** medium/high
- **Introduced:** 0.8.13  **Fixed:** 0.8.17

- **Trigger conditions:** {"yulOptimizer": true}
- **More info:** https://blog.soliditylang.org/2022/09/08/storage-write-removal-before-conditional-termination/

**Summary:** Calling functions that conditionally terminate the external EVM call using the assembly statements ``return(...)`` or ``stop()`` may result in incorrect removals of prior storage writes.

**Description:** A call to a Yul function that conditionally terminates the external EVM call could result in prior storage writes being incorrectly removed by the Yul optimizer. This used to happen in cases in which it would have been valid to remove the store, if the Yul function in question never actually terminated the external call, and the control flow always returned back to the caller instead. Conditional termination within the same Yul block instead of within a called function was not affected. In Solidity with optimized via-IR code generation, any storage write before a function conditionally calling ``return(...)`` or ``stop()`` in inline assembly, may have been incorrectly removed, whenever it would have been valid to remove the write without the ``return(...)`` or ``stop()``. In optimized legacy code generation, only inline assembly that did not refer to any Solidity variables and that involved conditionally-terminating user-defined assembly functions could be affected.

## AbiReencodingHeadOverflowWithStaticArrayCleanup

- **Severity:** medium
- **Introduced:** 0.5.8  **Fixed:** 0.8.16

- **Trigger conditions:** {"ABIEncoderV2": true}
- **More info:** https://blog.soliditylang.org/2022/08/08/calldata-tuple-reencoding-head-overflow-bug/

**Summary:** ABI-encoding a tuple with a statically-sized calldata array in the last component would corrupt 32 leading bytes of its first dynamically encoded component.

**Description:** When ABI-encoding a statically-sized calldata array, the compiler always pads the data area to a multiple of 32-bytes and ensures that the padding bytes are zeroed. In some cases, this cleanup used to be performed by always writing exactly 32 bytes, regardless of how many needed to be zeroed. This was done with the assumption that the data that would eventually occupy the area past the end of the array had not yet been written, because the encoder processes tuple components in the order they were given. While this assumption is mostly true, there is an important corner case: dynamically encoded tuple components are stored separately from the statically-sized ones in an area called the *tail* of the encoding and the tail immediately follows the *head*, which is where the statically-sized components are placed. The aforementioned cleanup, if performed for the last component of the head would cross into the tail and overwrite up to 32 bytes of the first component stored there with zeros. The only array type for which the cleanup could actually result in an overwrite were arrays with ``uint256`` or ``bytes32`` as the base element type and in this case the size of the corrupted area was always exactly 32 bytes. The problem affected tuples at any nesting level. This included also structs, which are encoded as tuples in the ABI. Note also that lists of parameters and return values of functions, events and errors are encoded as tuples.

## DirtyBytesArrayToStorage

- **Severity:** low
- **Introduced:** 0.0.1  **Fixed:** 0.8.15


- **More info:** https://blog.soliditylang.org/2022/06/15/dirty-bytes-array-to-storage-bug/

**Summary:** Copying ``bytes`` arrays from memory or calldata to storage may result in dirty storage values.

**Description:** Copying ``bytes`` arrays from memory or calldata to storage is done in chunks of 32 bytes even if the length is not a multiple of 32. Thereby, extra bytes past the end of the array may be copied from calldata or memory to storage. These dirty bytes may then become observable after a ``.push()`` without arguments to the bytes array in storage, i.e. such a push will not result in a zero value at the end of the array as expected. This bug only affects the legacy code generation pipeline, the new code generation pipeline via IR is not affected.

## InlineAssemblyMemorySideEffects

- **Severity:** medium
- **Introduced:** 0.8.13  **Fixed:** 0.8.15

- **Trigger conditions:** {"yulOptimizer": true}
- **More info:** https://blog.soliditylang.org/2022/06/15/inline-assembly-memory-side-effects-bug/

**Summary:** The Yul optimizer may incorrectly remove memory writes from inline assembly blocks, that do not access solidity variables.

**Description:** The Yul optimizer considers all memory writes in the outermost Yul block that are never read from as unused and removes them. This is valid when that Yul block is the entire Yul program, which is always the case for the Yul code generated by the new via-IR pipeline. Inline assembly blocks are never optimized in isolation when using that pipeline. Instead they are optimized as a part of the whole Yul input. However, the legacy code generation pipeline (which is still the default) runs the Yul optimizer individually on an inline assembly block if the block does not refer to any local variables defined in the surrounding Solidity code. Consequently, memory writes in such inline assembly blocks are removed as well, if the written memory is never read from in the same assembly block, even if the written memory is accessed later, for example by a subsequent inline assembly block.

## DataLocationChangeInInternalOverride

- **Severity:** very low
- **Introduced:** 0.6.9  **Fixed:** 0.8.14


- **More info:** https://blog.soliditylang.org/2022/05/17/data-location-inheritance-bug/

**Summary:** It was possible to change the data location of the parameters or return variables from ``calldata`` to ``memory`` and vice-versa while overriding internal and public functions. This caused invalid code to be generated when calling such a function internally through virtual function calls.

**Description:** When calling external functions, it is irrelevant if the data location of the parameters is ``calldata`` or ``memory``, the encoding of the data does not change. Because of that, changing the data location when overriding external functions is allowed. The compiler incorrectly also allowed a change in the data location for overriding public and internal functions. Since public functions can be called internally as well as externally, this causes invalid code to be generated when such an incorrectly overridden function is called internally through the base contract. The caller provides a memory pointer, but the called function interprets it as a calldata pointer or vice-versa.

## NestedCalldataArrayAbiReencodingSizeValidation

- **Severity:** very low
- **Introduced:** 0.5.8  **Fixed:** 0.8.14


- **More info:** https://blog.soliditylang.org/2022/05/17/calldata-reencode-size-check-bug/

**Summary:** ABI-reencoding of nested dynamic calldata arrays did not always perform proper size checks against the size of calldata and could read beyond ``calldatasize()``.

**Description:** Calldata validation for nested dynamic types is deferred until the first access to the nested values. Such an access may for example be a copy to memory or an index or member access to the outer type. While in most such accesses calldata validation correctly checks that the data area of the nested array is completely contained in the passed calldata (i.e. in the range [0, calldatasize()]), this check may not be performed, when ABI encoding such nested types again directly from calldata. For instance, this can happen, if a value in calldata with a nested dynamic array is passed to an external call, used in ``abi.encode`` or emitted as event. In such cases, if the data area of the nested array extends beyond ``calldatasize()``, ABI encoding it did not revert, but continued reading values from beyond ``calldatasize()`` (i.e. zero values).

## AbiEncodeCallLiteralAsFixedBytesBug

- **Severity:** very low
- **Introduced:** 0.8.11  **Fixed:** 0.8.13


- **More info:** https://blog.soliditylang.org/2022/03/16/encodecall-bug/

**Summary:** Literals used for a fixed length bytes parameter in ``abi.encodeCall`` were encoded incorrectly.

**Description:** For the encoding, the compiler only considered the types of the expressions in the second argument of ``abi.encodeCall`` itself, but not the parameter types of the function given as first argument. In almost all cases the abi encoding of the type of the expression matches the abi encoding of the parameter type of the given function. This is because the type checker ensures the expression is implicitly convertible to the respective parameter type. However this is not true for number literals used for fixed bytes types shorter than 32 bytes, nor for string literals used for any fixed bytes type. Number literals were encoded as numbers instead of being shifted to become left-aligned. String literals were encoded as dynamically sized memory strings instead of being converted to a left-aligned bytes value.

## UserDefinedValueTypesBug

- **Severity:** very low
- **Introduced:** 0.8.8  **Fixed:** 0.8.9


- **More info:** https://blog.soliditylang.org/2021/09/29/user-defined-value-types-bug/

**Summary:** User defined value types with underlying type shorter than 32 bytes used incorrect storage layout and wasted storage

**Description:** The compiler did not correctly compute the storage layout of user defined value types based on types that are shorter than 32 bytes. It would always use a full storage slot for these types, even if the underlying type was shorter. This was wasteful and might have problems with tooling or contract upgrades.

## SignedImmutables

- **Severity:** very low
- **Introduced:** 0.6.5  **Fixed:** 0.8.9


- **More info:** https://blog.soliditylang.org/2021/09/29/signed-immutables-bug/

**Summary:** Immutable variables of signed integer type shorter than 256 bits can lead to values with invalid higher order bits if inline assembly is used.

**Description:** When immutable variables of signed integer type shorter than 256 bits are read, their higher order bits were unconditionally set to zero. The correct operation would be to sign-extend the value, i.e. set the higher order bits to one if the sign bit is one. This sign-extension is performed by Solidity just prior to when it matters, i.e. when a value is stored in memory, when it is compared or when a division is performed. Because of that, to our knowledge, the only way to access the value in its unclean state is by reading it through inline assembly.

## ABIDecodeTwoDimensionalArrayMemory

- **Severity:** very low
- **Introduced:** 0.4.16  **Fixed:** 0.8.4

- **Trigger conditions:** {"ABIEncoderV2": true}
- **More info:** https://blog.soliditylang.org/2021/04/21/decoding-from-memory-bug/

**Summary:** If used on memory byte arrays, result of the function ``abi.decode`` can depend on the contents of memory outside of the actual byte array that is decoded.

**Description:** The ABI specification uses pointers to data areas for everything that is dynamically-sized. When decoding data from memory (instead of calldata), the ABI decoder did not properly validate some of these pointers. More specifically, it was possible to use large values for the pointers inside arrays such that computing the offset resulted in an undetected overflow. This could lead to these pointers targeting areas in memory outside of the actual area to be decoded. This way, it was possible for ``abi.decode`` to return different values for the same encoded byte array.

## KeccakCaching

- **Severity:** medium
- **Introduced:** (unknown)  **Fixed:** 0.8.3

- **Trigger conditions:** {"optimizer": true}
- **More info:** https://blog.soliditylang.org/2021/03/23/keccak-optimizer-bug/

**Summary:** The bytecode optimizer incorrectly reused previously evaluated Keccak-256 hashes. You are unlikely to be affected if you do not compute Keccak-256 hashes in inline assembly.

**Description:** Solidity's bytecode optimizer has a step that can compute Keccak-256 hashes, if the contents of the memory are known during compilation time. This step also has a mechanism to determine that two Keccak-256 hashes are equal even if the values in memory are not known during compile time. This mechanism had a bug where Keccak-256 of the same memory content, but different sizes were considered equal. More specifically, ``keccak256(mpos1, length1)`` and ``keccak256(mpos2, length2)`` in some cases were considered equal if ``length1`` and ``length2``, when rounded up to nearest multiple of 32 were the same, and when the memory contents at ``mpos1`` and ``mpos2`` can be deduced to be equal. You maybe affected if you compute multiple Keccak-256 hashes of the same content, but with different lengths inside inline assembly. You are unaffected if your code uses ``keccak256`` with a length that is not a compile-time constant or if it is always a multiple of 32.

## EmptyByteArrayCopy

- **Severity:** medium
- **Introduced:** (unknown)  **Fixed:** 0.7.4


- **More info:** https://blog.soliditylang.org/2020/10/19/empty-byte-array-copy-bug/

**Summary:** Copying an empty byte array (or string) from memory or calldata to storage can result in data corruption if the target array's length is increased subsequently without storing new data.

**Description:** The routine that copies byte arrays from memory or calldata to storage stores unrelated data from after the source array in the storage slot if the source array is empty. If the storage array's length is subsequently increased either by using ``.push()`` or by assigning to its ``.length`` attribute (only before 0.6.0), the newly created byte array elements will not be zero-initialized, but contain the unrelated data. You are not affected if you do not assign to ``.length`` and do not use ``.push()`` on byte arrays, or only use ``.push(<arg>)`` or manually initialize the new elements.

## DynamicArrayCleanup

- **Severity:** medium
- **Introduced:** (unknown)  **Fixed:** 0.7.3


- **More info:** https://blog.soliditylang.org/2020/10/07/solidity-dynamic-array-cleanup-bug/

**Summary:** When assigning a dynamically-sized array with types of size at most 16 bytes in storage causing the assigned array to shrink, some parts of deleted slots were not zeroed out.

**Description:** Consider a dynamically-sized array in storage whose base-type is small enough such that multiple values can be packed into a single slot, such as `uint128[]`. Let us define its length to be `l`. When this array gets assigned from another array with a smaller length, say `m`, the slots between elements `m` and `l` have to be cleaned by zeroing them out. However, this cleaning was not performed properly. Specifically, after the slot corresponding to `m`, only the first packed value was cleaned up. If this array gets resized to a length larger than `m`, the indices corresponding to the unclean parts of the slot contained the original value, instead of 0. The resizing here is performed by assigning to the array `length`, by a `push()` or via inline assembly. You are not affected if you are only using `.push(<arg>)` or if you assign a value (even zero) to the new elements after increasing the length of the array.

## FreeFunctionRedefinition

- **Severity:** low
- **Introduced:** 0.7.1  **Fixed:** 0.7.2




**Summary:** The compiler does not flag an error when two or more free functions with the same name and parameter types are defined in a source unit or when an imported free function alias shadows another free function with a different name but identical parameter types.

**Description:** In contrast to functions defined inside contracts, free functions with identical names and parameter types did not create an error. Both definition of free functions with identical name and parameter types and an imported free function with an alias that shadows another function with a different name but identical parameter types were permitted due to which a call to either the multiply defined free function or the imported free function alias within a contract led to the execution of that free function which was defined first within the source unit. Subsequently defined identical free function definitions were silently ignored and their code generation was skipped.

## UsingForCalldata

- **Severity:** very low
- **Introduced:** 0.6.9  **Fixed:** 0.6.10




**Summary:** Function calls to internal library functions with calldata parameters called via ``using for`` can result in invalid data being read.

**Description:** Function calls to internal library functions using the ``using for`` mechanism copied all calldata parameters to memory first and passed them on like that, regardless of whether it was an internal or an external call. Due to that, the called function would receive a memory pointer that is interpreted as a calldata pointer. Since dynamically sized arrays are passed using two stack slots for calldata, but only one for memory, this can lead to stack corruption. An affected library call will consider the JUMPDEST to which it is supposed to return as part of its arguments and will instead jump out to whatever was on the stack before the call.

## MissingEscapingInFormatting

- **Severity:** very low
- **Introduced:** 0.5.14  **Fixed:** 0.6.8

- **Trigger conditions:** {"ABIEncoderV2": true}


**Summary:** String literals containing double backslash characters passed directly to external or encoding function calls can lead to a different string being used when ABIEncoderV2 is enabled.

**Description:** When ABIEncoderV2 is enabled, string literals passed directly to encoding functions or external function calls are stored as strings in the intermediate code. Characters outside the printable range are handled correctly, but backslashes are not escaped in this procedure. This leads to double backslashes being reduced to single backslashes and consequently re-interpreted as escapes potentially resulting in a different string being encoded.

## ArraySliceDynamicallyEncodedBaseType

- **Severity:** very low
- **Introduced:** 0.6.0  **Fixed:** 0.6.8

- **Trigger conditions:** {"ABIEncoderV2": true}


**Summary:** Accessing array slices of arrays with dynamically encoded base types (e.g. multi-dimensional arrays) can result in invalid data being read.

**Description:** For arrays with dynamically sized base types, index range accesses that use a start expression that is non-zero will result in invalid array slices. Any index access to such array slices will result in data being read from incorrect calldata offsets. Array slices are only supported for dynamic calldata types and all problematic type require ABIEncoderV2 to be enabled.

## ImplicitConstructorCallvalueCheck

- **Severity:** very low
- **Introduced:** 0.4.5  **Fixed:** 0.6.8




**Summary:** The creation code of a contract that does not define a constructor but has a base that does define a constructor did not revert for calls with non-zero value.

**Description:** Starting from Solidity 0.4.5 the creation code of contracts without explicit payable constructor is supposed to contain a callvalue check that results in contract creation reverting, if non-zero value is passed. However, this check was missing in case no explicit constructor was defined in a contract at all, but the contract has a base that does define a constructor. In these cases it is possible to send value in a contract creation transaction or using inline assembly without revert, even though the creation code is supposed to be non-payable.

## TupleAssignmentMultiStackSlotComponents

- **Severity:** very low
- **Introduced:** 0.1.6  **Fixed:** 0.6.6




**Summary:** Tuple assignments with components that occupy several stack slots, i.e. nested tuples, pointers to external functions or references to dynamically sized calldata arrays, can result in invalid values.

**Description:** Tuple assignments did not correctly account for tuple components that occupy multiple stack slots in case the number of stack slots differs between left-hand-side and right-hand-side. This can either happen in the presence of nested tuples or if the right-hand-side contains external function pointers or references to dynamic calldata arrays, while the left-hand-side contains an omission.

## MemoryArrayCreationOverflow

- **Severity:** low
- **Introduced:** 0.2.0  **Fixed:** 0.6.5


- **More info:** https://blog.soliditylang.org/2020/04/06/memory-creation-overflow-bug/

**Summary:** The creation of very large memory arrays can result in overlapping memory regions and thus memory corruption.

**Description:** No runtime overflow checks were performed for the length of memory arrays during creation. In cases for which the memory size of an array in bytes, i.e. the array length times 32, is larger than 2^256-1, the memory allocation will overflow, potentially resulting in overlapping memory areas. The length of the array is still stored correctly, so copying or iterating over such an array will result in out-of-gas.

## YulOptimizerRedundantAssignmentBreakContinue

- **Severity:** medium
- **Introduced:** 0.6.0  **Fixed:** 0.6.1

- **Trigger conditions:** {"yulOptimizer": true}


**Summary:** The Yul optimizer can remove essential assignments to variables declared inside for loops when Yul's continue or break statement is used. You are unlikely to be affected if you do not use inline assembly with for loops and continue and break statements.

**Description:** The Yul optimizer has a stage that removes assignments to variables that are overwritten again or are not used in all following control-flow branches. This logic incorrectly removes such assignments to variables declared inside a for loop if they can be removed in a control-flow branch that ends with ``break`` or ``continue`` even though they cannot be removed in other control-flow branches. Variables declared outside of the respective for loop are not affected.

## privateCanBeOverridden

- **Severity:** low
- **Introduced:** 0.3.0  **Fixed:** 0.5.17




**Summary:** Private methods can be overridden by inheriting contracts.

**Description:** While private methods of base contracts are not visible and cannot be called directly from the derived contract, it is still possible to declare a function of the same name and type and thus change the behaviour of the base contract's function.

## YulOptimizerRedundantAssignmentBreakContinue0.5

- **Severity:** low
- **Introduced:** 0.5.8  **Fixed:** 0.5.16

- **Trigger conditions:** {"yulOptimizer": true}


**Summary:** The Yul optimizer can remove essential assignments to variables declared inside for loops when Yul's continue or break statement is used. You are unlikely to be affected if you do not use inline assembly with for loops and continue and break statements.

**Description:** The Yul optimizer has a stage that removes assignments to variables that are overwritten again or are not used in all following control-flow branches. This logic incorrectly removes such assignments to variables declared inside a for loop if they can be removed in a control-flow branch that ends with ``break`` or ``continue`` even though they cannot be removed in other control-flow branches. Variables declared outside of the respective for loop are not affected.

## ABIEncoderV2LoopYulOptimizer

- **Severity:** low
- **Introduced:** 0.5.14  **Fixed:** 0.5.15

- **Trigger conditions:** {"ABIEncoderV2": true, "optimizer": true, "yulOptimizer": true}


**Summary:** If both the experimental ABIEncoderV2 and the experimental Yul optimizer are activated, one component of the Yul optimizer may reuse data in memory that has been changed in the meantime.

**Description:** The Yul optimizer incorrectly replaces ``mload`` and ``sload`` calls with values that have been previously written to the load location (and potentially changed in the meantime) if all of the following conditions are met: (1) there is a matching ``mstore`` or ``sstore`` call before; (2) the contents of memory or storage is only changed in a function that is called (directly or indirectly) in between the first store and the load call; (3) called function contains a for loop where the same memory location is changed in the condition or the post or body block. When used in Solidity mode, this can only happen if the experimental ABIEncoderV2 is activated and the experimental Yul optimizer has been activated manually in addition to the regular optimizer in the compiler settings.

## ABIEncoderV2CalldataStructsWithStaticallySizedAndDynamicallyEncodedMembers

- **Severity:** low
- **Introduced:** 0.5.6  **Fixed:** 0.5.11

- **Trigger conditions:** {"ABIEncoderV2": true}


**Summary:** Reading from calldata structs that contain dynamically encoded, but statically-sized members can result in incorrect values.

**Description:** When a calldata struct contains a dynamically encoded, but statically-sized member, the offsets for all subsequent struct members are calculated incorrectly. All reads from such members will result in invalid values. Only calldata structs are affected, i.e. this occurs in external functions with such structs as argument. Using affected structs in storage or memory or as arguments to public functions on the other hand works correctly.

## SignedArrayStorageCopy

- **Severity:** low/medium
- **Introduced:** 0.4.7  **Fixed:** 0.5.10


- **More info:** https://blog.soliditylang.org/2019/06/25/solidity-storage-array-bugs/

**Summary:** Assigning an array of signed integers to a storage array of different type can lead to data corruption in that array.

**Description:** In two's complement, negative integers have their higher order bits set. In order to fit into a shared storage slot, these have to be set to zero. When a conversion is done at the same time, the bits to set to zero were incorrectly determined from the source and not the target type. This means that such copy operations can lead to incorrect values being stored.

## ABIEncoderV2StorageArrayWithMultiSlotElement

- **Severity:** low
- **Introduced:** 0.4.16  **Fixed:** 0.5.10

- **Trigger conditions:** {"ABIEncoderV2": true}
- **More info:** https://blog.soliditylang.org/2019/06/25/solidity-storage-array-bugs/

**Summary:** Storage arrays containing structs or other statically-sized arrays are not read properly when directly encoded in external function calls or in abi.encode*.

**Description:** When storage arrays whose elements occupy more than a single storage slot are directly encoded in external function calls or using abi.encode*, their elements are read in an overlapping manner, i.e. the element pointer is not properly advanced between reads. This is not a problem when the storage data is first copied to a memory variable or if the storage array only contains value types or dynamically-sized arrays.

## DynamicConstructorArgumentsClippedABIV2

- **Severity:** very low
- **Introduced:** 0.4.16  **Fixed:** 0.5.9

- **Trigger conditions:** {"ABIEncoderV2": true}


**Summary:** A contract's constructor that takes structs or arrays that contain dynamically-sized arrays reverts or decodes to invalid data.

**Description:** During construction of a contract, constructor parameters are copied from the code section to memory for decoding. The amount of bytes to copy was calculated incorrectly in case all parameters are statically-sized but contain dynamically-sized arrays as struct members or inner arrays. Such types are only available if ABIEncoderV2 is activated.

## UninitializedFunctionPointerInConstructor

- **Severity:** very low
- **Introduced:** 0.5.0  **Fixed:** 0.5.8




**Summary:** Calling uninitialized internal function pointers created in the constructor does not always revert and can cause unexpected behaviour.

**Description:** Uninitialized internal function pointers point to a special piece of code that causes a revert when called. Jump target positions are different during construction and after deployment, but the code for setting this special jump target only considered the situation after deployment.

## UninitializedFunctionPointerInConstructor_0.4.x

- **Severity:** very low
- **Introduced:** 0.4.5  **Fixed:** 0.4.26




**Summary:** Calling uninitialized internal function pointers created in the constructor does not always revert and can cause unexpected behaviour.

**Description:** Uninitialized internal function pointers point to a special piece of code that causes a revert when called. Jump target positions are different during construction and after deployment, but the code for setting this special jump target only considered the situation after deployment.

## IncorrectEventSignatureInLibraries

- **Severity:** very low
- **Introduced:** 0.5.0  **Fixed:** 0.5.8




**Summary:** Contract types used in events in libraries cause an incorrect event signature hash

**Description:** Instead of using the type `address` in the hashed signature, the actual contract name was used, leading to a wrong hash in the logs.

## IncorrectEventSignatureInLibraries_0.4.x

- **Severity:** very low
- **Introduced:** 0.3.0  **Fixed:** 0.4.26




**Summary:** Contract types used in events in libraries cause an incorrect event signature hash

**Description:** Instead of using the type `address` in the hashed signature, the actual contract name was used, leading to a wrong hash in the logs.

## ABIEncoderV2PackedStorage

- **Severity:** low
- **Introduced:** 0.5.0  **Fixed:** 0.5.7

- **Trigger conditions:** {"ABIEncoderV2": true}
- **More info:** https://blog.soliditylang.org/2019/03/26/solidity-optimizer-and-abiencoderv2-bug/

**Summary:** Storage structs and arrays with types shorter than 32 bytes can cause data corruption if encoded directly from storage using the experimental ABIEncoderV2.

**Description:** Elements of structs and arrays that are shorter than 32 bytes are not properly decoded from storage when encoded directly (i.e. not via a memory type) using ABIEncoderV2. This can cause corruption in the values themselves but can also overwrite other parts of the encoded data.

## ABIEncoderV2PackedStorage_0.4.x

- **Severity:** low
- **Introduced:** 0.4.19  **Fixed:** 0.4.26

- **Trigger conditions:** {"ABIEncoderV2": true}
- **More info:** https://blog.soliditylang.org/2019/03/26/solidity-optimizer-and-abiencoderv2-bug/

**Summary:** Storage structs and arrays with types shorter than 32 bytes can cause data corruption if encoded directly from storage using the experimental ABIEncoderV2.

**Description:** Elements of structs and arrays that are shorter than 32 bytes are not properly decoded from storage when encoded directly (i.e. not via a memory type) using ABIEncoderV2. This can cause corruption in the values themselves but can also overwrite other parts of the encoded data.

## IncorrectByteInstructionOptimization

- **Severity:** very low
- **Introduced:** 0.5.5  **Fixed:** 0.5.7

- **Trigger conditions:** {"optimizer": true}
- **More info:** https://blog.soliditylang.org/2019/03/26/solidity-optimizer-and-abiencoderv2-bug/

**Summary:** The optimizer incorrectly handles byte opcodes whose second argument is 31 or a constant expression that evaluates to 31. This can result in unexpected values.

**Description:** The optimizer incorrectly handles byte opcodes that use the constant 31 as second argument. This can happen when performing index access on bytesNN types with a compile-time constant value (not index) of 31 or when using the byte opcode in inline assembly.

## DoubleShiftSizeOverflow

- **Severity:** low
- **Introduced:** 0.5.5  **Fixed:** 0.5.6

- **Trigger conditions:** {"optimizer": true, "evmVersion": ">=constantinople"}
- **More info:** https://blog.soliditylang.org/2019/03/26/solidity-optimizer-and-abiencoderv2-bug/

**Summary:** Double bitwise shifts by large constants whose sum overflows 256 bits can result in unexpected values.

**Description:** Nested logical shift operations whose total shift size is 2**256 or more are incorrectly optimized. This only applies to shifts by numbers of bits that are compile-time constant expressions.

## ExpExponentCleanup

- **Severity:** medium/high
- **Introduced:** (unknown)  **Fixed:** 0.4.25


- **More info:** https://blog.soliditylang.org/2018/09/13/solidity-bugfix-release/

**Summary:** Using the ** operator with an exponent of type shorter than 256 bits can result in unexpected values.

**Description:** Higher order bits in the exponent are not properly cleaned before the EXP opcode is applied if the type of the exponent expression is smaller than 256 bits and not smaller than the type of the base. In that case, the result might be larger than expected if the exponent is assumed to lie within the value range of the type. Literal numbers as exponents are unaffected as are exponents or bases of type uint256.

## EventStructWrongData

- **Severity:** very low
- **Introduced:** 0.4.17  **Fixed:** 0.4.25


- **More info:** https://blog.soliditylang.org/2018/09/13/solidity-bugfix-release/

**Summary:** Using structs in events logged wrong data.

**Description:** If a struct is used in an event, the address of the struct is logged instead of the actual data.

## NestedArrayFunctionCallDecoder

- **Severity:** medium
- **Introduced:** 0.1.4  **Fixed:** 0.4.22


- **More info:** https://blog.soliditylang.org/2018/09/13/solidity-bugfix-release/

**Summary:** Calling functions that return multi-dimensional fixed-size arrays can result in memory corruption.

**Description:** If Solidity code calls a function that returns a multi-dimensional fixed-size array, array elements are incorrectly interpreted as memory pointers and thus can cause memory corruption if the return values are accessed. Calling functions with multi-dimensional fixed-size arrays is unaffected as is returning fixed-size arrays from function calls. The regular expression only checks if such functions are present, not if they are called, which is required for the contract to be affected.

## OneOfTwoConstructorsSkipped

- **Severity:** very low
- **Introduced:** 0.4.22  **Fixed:** 0.4.23




**Summary:** If a contract has both a new-style constructor (using the constructor keyword) and an old-style constructor (a function with the same name as the contract) at the same time, one of them will be ignored.

**Description:** If a contract has both a new-style constructor (using the constructor keyword) and an old-style constructor (a function with the same name as the contract) at the same time, one of them will be ignored. There will be a compiler warning about the old-style constructor, so contracts only using new-style constructors are fine.

## ZeroFunctionSelector

- **Severity:** very low
- **Introduced:** (unknown)  **Fixed:** 0.4.18




**Summary:** It is possible to craft the name of a function such that it is executed instead of the fallback function in very specific circumstances.

**Description:** If a function has a selector consisting only of zeros, is payable and part of a contract that does not have a fallback function and at most five external functions in total, this function is called instead of the fallback function if Ether is sent to the contract without data.

## DelegateCallReturnValue

- **Severity:** low
- **Introduced:** 0.3.0  **Fixed:** 0.4.15




**Summary:** The low-level .delegatecall() does not return the execution outcome, but converts the value returned by the functioned called to a boolean instead.

**Description:** The return value of the low-level .delegatecall() function is taken from a position in memory, where the call data or the return data resides. This value is interpreted as a boolean and put onto the stack. This means if the called function returns at least 32 zero bytes, .delegatecall() returns false even if the call was successful.

## ECRecoverMalformedInput

- **Severity:** medium
- **Introduced:** (unknown)  **Fixed:** 0.4.14




**Summary:** The ecrecover() builtin can return garbage for malformed input.

**Description:** The ecrecover precompile does not properly signal failure for malformed input (especially in the 'v' argument) and thus the Solidity function can return data that was previously present in the return area in memory.

## SkipEmptyStringLiteral

- **Severity:** low
- **Introduced:** (unknown)  **Fixed:** 0.4.12




**Summary:** If "" is used in a function call, the following function arguments will not be correctly passed to the function.

**Description:** If the empty string literal "" is used as an argument in a function call, it is skipped by the encoder. This has the effect that the encoding of all arguments following this is shifted left by 32 bytes and thus the function call data is corrupted.

## ConstantOptimizerSubtraction

- **Severity:** low
- **Introduced:** (unknown)  **Fixed:** 0.4.11

- **Trigger conditions:** {"optimizer": true}
- **More info:** https://blog.soliditylang.org/2017/05/03/solidity-optimizer-bug/

**Summary:** In some situations, the optimizer replaces certain numbers in the code with routines that compute different numbers.

**Description:** The optimizer tries to represent any number in the bytecode by routines that compute them with less gas. For some special numbers, an incorrect routine is generated. This could allow an attacker to e.g. trick victims about a specific amount of ether, or function calls to call different functions (or none at all).

## IdentityPrecompileReturnIgnored

- **Severity:** low
- **Introduced:** (unknown)  **Fixed:** 0.4.7




**Summary:** Failure of the identity precompile was ignored.

**Description:** Calls to the identity contract, which is used for copying memory, ignored its return value. On the public chain, calls to the identity precompile can be made in a way that they never fail, but this might be different on private chains.

## OptimizerStateKnowledgeNotResetForJumpdest

- **Severity:** medium
- **Introduced:** 0.4.5  **Fixed:** 0.4.6

- **Trigger conditions:** {"optimizer": true}


**Summary:** The optimizer did not properly reset its internal state at jump destinations, which could lead to data corruption.

**Description:** The optimizer performs symbolic execution at certain stages. At jump destinations, multiple code paths join and thus it has to compute a common state from the incoming edges. Computing this common state was simplified to just use the empty state, but this implementation was not done properly. This bug can cause data corruption.

## HighOrderByteCleanStorage

- **Severity:** high
- **Introduced:** 0.1.6  **Fixed:** 0.4.4


- **More info:** https://blog.soliditylang.org/2016/11/01/security-alert-solidity-variables-can-overwritten-storage/

**Summary:** For short types, the high order bytes were not cleaned properly and could overwrite existing data.

**Description:** Types shorter than 32 bytes are packed together into the same 32 byte storage slot, but storage writes always write 32 bytes. For some types, the higher order bytes were not cleaned properly, which made it sometimes possible to overwrite a variable in storage when writing to another one.

## OptimizerStaleKnowledgeAboutSHA3

- **Severity:** medium
- **Introduced:** (unknown)  **Fixed:** 0.4.3

- **Trigger conditions:** {"optimizer": true}


**Summary:** The optimizer did not properly reset its knowledge about SHA3 operations resulting in some hashes (also used for storage variable positions) not being calculated correctly.

**Description:** The optimizer performs symbolic execution in order to save re-evaluating expressions whose value is already known. This knowledge was not properly reset across control flow paths and thus the optimizer sometimes thought that the result of a SHA3 operation is already present on the stack. This could result in data corruption by accessing the wrong storage slot.

## LibrariesNotCallableFromPayableFunctions

- **Severity:** low
- **Introduced:** 0.4.0  **Fixed:** 0.4.2




**Summary:** Library functions threw an exception when called from a call that received Ether.

**Description:** Library functions are protected against sending them Ether through a call. Since the DELEGATECALL opcode forwards the information about how much Ether was sent with a call, the library function incorrectly assumed that Ether was sent to the library and threw an exception.

## SendFailsForZeroEther

- **Severity:** low
- **Introduced:** (unknown)  **Fixed:** 0.4.0




**Summary:** The send function did not provide enough gas to the recipient if no Ether was sent with it.

**Description:** The recipient of an Ether transfer automatically receives a certain amount of gas from the EVM to handle the transfer. In the case of a zero-transfer, this gas is not provided which causes the recipient to throw an exception.

## DynamicAllocationInfiniteLoop

- **Severity:** low
- **Introduced:** (unknown)  **Fixed:** 0.3.6




**Summary:** Dynamic allocation of an empty memory array caused an infinite loop and thus an exception.

**Description:** Memory arrays can be created provided a length. If this length is zero, code was generated that did not terminate and thus consumed all gas.

## OptimizerClearStateOnCodePathJoin

- **Severity:** low
- **Introduced:** (unknown)  **Fixed:** 0.3.6

- **Trigger conditions:** {"optimizer": true}


**Summary:** The optimizer did not properly reset its internal state at jump destinations, which could lead to data corruption.

**Description:** The optimizer performs symbolic execution at certain stages. At jump destinations, multiple code paths join and thus it has to compute a common state from the incoming edges. Computing this common state was not done correctly. This bug can cause data corruption, but it is probably quite hard to use for targeted attacks.

## CleanBytesHigherOrderBits

- **Severity:** medium/high
- **Introduced:** (unknown)  **Fixed:** 0.3.3




**Summary:** The higher order bits of short bytesNN types were not cleaned before comparison.

**Description:** Two variables of type bytesNN were considered different if their higher order bits, which are not part of the actual value, were different. An attacker might use this to reach seemingly unreachable code paths by providing incorrectly formatted input data.

## ArrayAccessCleanHigherOrderBits

- **Severity:** medium/high
- **Introduced:** (unknown)  **Fixed:** 0.3.1




**Summary:** Access to array elements for arrays of types with less than 32 bytes did not correctly clean the higher order bits, causing corruption in other array elements.

**Description:** Multiple elements of an array of values that are shorter than 17 bytes are packed into the same storage slot. Writing to a single element of such an array did not properly clean the higher order bytes and thus could lead to data corruption.

## AncientCompiler

- **Severity:** high
- **Introduced:** (unknown)  **Fixed:** 0.3.0




**Summary:** This compiler version is ancient and might contain several undocumented or undiscovered bugs.

**Description:** The list of bugs is only kept for compiler versions starting from 0.3.0, so older versions might contain undocumented bugs.

