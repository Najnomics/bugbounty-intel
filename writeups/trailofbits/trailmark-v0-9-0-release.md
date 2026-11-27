# trailmark-v0-9-0-release

- **Source URL:** https://github.com/trailofbits/trailmark/releases/tag/v0.9.0
- **Fetched:** 2026-11-27
- **Researcher:** trailofbits
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

## Repository navigation

# Trailmark v0.9.0

[tob-scott-a](/tob-scott-a)released this

·
          
            [14 commits](/trailofbits/trailmark/compare/v0.9.0...main)
          
          to main
          since this release

Immutable
            release. Only release title and notes can be modified.

This release adds eight language frontends for verification and specification

analysis, extends reference traversal, and improves call binding and source ownership

across existing frontends.

### Added

- **Lean 4:** declarations, namespaces, structures, classes, inductive types,
inspected imports, conservative calls, and located references in signatures,
bodies, typed projections, and immutable record updates.
- **Dafny:** modules, classes, datatypes, functions, methods, lemmas, contracts,
scoped computational calls, ghost/proof references, and callback invocation sites.
- **F*:*\* declarations, interface/implementation correspondence, refinements,
scoped imports and exports, computation effects, and conservative applications.
- **Rocq/Coq:** Gallina declarations, modules, sections, assumptions, theorem
statements, project load paths, and explicit source references.
- **WhyML:** programs and modules, arrays, records, ghost code, contracts,
inspected imports, and explicit references, with diagnostics for syntax gaps.
- **TLA+:** modules, state variables, operators, lexical LET definitions,
EXTENDS/INSTANCE dependencies, and proof-step source references.
- **Tamarin:** rules, function/fact symbols, roles, persistence, macros,
predicates, includes, conditionals, and specification references.
- **ProVerif:** typed pi-calculus declarations, processes, events, queries,
destructor equations, macros, tables, and inspected library dependencies.
- Opt-in `edge_kinds` filters for `reachable_from`, `ancestors_of`, and
`paths_between`. Graph JSON can include locations for `references` edges
within schema version 1; traversal defaults remain calls only.

### Changed

- Separate computational applications from proof, type, ghost, and erased uses
in verification-language graphs. Preserve lexical binders, declaration order,
visibility, source locations, and uncertain application evidence where supported.
These graphs describe source syntax rather than verifier results or runtime dispatch.
- Resolve literal JavaScript/TypeScript named imports only through selected source
exports, and bind imported constructions to inspected constructor bodies. Retain
every construction site, including uncertain proxies for unresolved constructors;
these sites can change resolution counts and graph diffs.
Reuse export discovery and constructor indexes during directory analysis to
avoid repeated parsing and whole-graph scans. Share formal import lookup indexes.
- Retain Rust `macro_rules!` arms as template nodes with non-call references for
source navigation, without treating templates as runtime execution.
- Include `.h` files in C++ directory analysis. In mixed C/C++ trees, C++ owns
shared headers unless Objective-C is selected; headers are inspected once.

### Fixed

- Preserve Python assignment-expression bindings and nested generator ownership;
retain Swift defer/self calls, dominated Bash helpers, Lua local-table methods,
Ruby inline visibility and literal aliases, and Julia inbounds-wrapped calls.
- Preserve C++ class, namespace, constructor, and out-of-line method ownership
through supported export markers, templates, casts, and block macros. Bound
template-marker recovery to avoid exponential backtracking.
- Retain Objective-C declarations inside conditional implementations, nullability
regions, and standard enum typedefs; link messages through inspected ivar types.
- Resolve inspected Java anonymous-class helpers and retain enclosing-method
fallback with conservative confidence. Preserve C# construction sites and
cross-file static calls; keep attributed overloads conservative and handle
equivalent optional defaults.
- Bind supported Kotlin fixed-arity overloads and Dart named/factory constructors,
explicit`this` methods, and final locals with declared factory return types.
- Preserve Cairo generic impls and supported qualified/self calls, VB.NET
inheritance declarations, Rego compound indices and clause dependencies,
Solidity member/modifier calls, Zig typed-local calls, and SQL routine recovery.
- Retain Thrift service inheritance, GraphQL interface implementations, and Tact
trait relationships. Preserve complete Dafny generic type identifiers and
source offsets during bounded formal syntax recovery.
- Name the grammar, original error, and build requirements when a missing compiler
or read-only installation prevents native grammar compilation.

### Upgrade notes

- Auto mode now detects `.lean`, `.dfy`, `.fst`/`.fsti`, `.mlw`/`.why`, `.tla`,
`.spthy`, and `.pv`/`.pvl` files that v0.8.0 ignored. To preserve an existing
language selection, pass an explicit list such as`--language python,javascript`.
- Cairo, VB.NET, and Rego now use bundled grammars, as do the new Dafny, F\*,
Rocq, WhyML, Tamarin, and ProVerif frontends. First use requires a C compiler
(`cc`), Python development headers, and write access to the installed grammar
directories. A required grammar failure stops the analysis, including auto mode.
Precompile bindings before making an installation read-only. See
[installation requirements](https://github.com/trailofbits/trailmark/blob/v0.9.0/docs/installation.md#bundled-grammars).
- Require `tree-sitter-language-pack` 1.25.2 or newer. Support tree-sitter 0.25.2
or newer below 0.27, excluding 0.26.0 because of its native Point lifetime
regression. Require`tree-sitter-sql` 0.3.13 or newer below 0.4.
Python 3.12 remains the minimum; CI tests Python 3.12 through 3.15.
- Select `--language rocq` explicitly for `.v` files. For F\* paths that cross an
interface into its implementation, use`edge_kinds=("calls", "corresponds_to")`.
Proof/specification dependencies require the appropriate reference edge filters;
default call-only traversal does not establish proof dependencies.
- Rebuild source graphs to pick up corrected bindings and ownership. Graph schema
version 1 and the existing call-only query defaults remain supported. Per-language
syntax and inference limits are documented in[language notes](https://github.com/trailofbits/trailmark/blob/v0.9.0/docs/languages.md).

**Full changelog:** `v0.8.0...v0.9.0`
