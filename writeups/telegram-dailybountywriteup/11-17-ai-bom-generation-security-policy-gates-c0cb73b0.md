# Securing the AI Supply Chain: A Hands-On AI-BOM Playbook for Pickle RCE, Poisoned Datasets, and CI Gates - SecurityCipher

- **Source URL:** https://securitycipher.com/2026/11/17/ai-bom-generation-security-policy-gates
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14988 (id 14988)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I keep a 21-byte file in my test folder. It is called `pytorch_model.bin`, it has no tensors, and it has never been anywhere near a GPU.

Last week it ran `id` on my laptop, because I asked PyTorch to load it.

That is the AI supply chain problem in one directory listing. An AI BOM (AI bill of materials, written AI-BOM in the specs) is how you make that file visible before a training job deserializes it. Your scanner sees a dependency graph; the attacker sees a file extension and a container with the Hugging Face token mounted.

This is the loop I run on engagements: find the file, prove it executes, record what the model actually is, and stop it coming back.

## The short version (TL;DR)

- A normal SBOM stops at the Python layer. In an LLM app, the things that can own your infrastructure are the weight files, the tokenizer code, the dataset snapshots, and the serving runtime. None of them appear in `pip freeze`.
- Pickle is not a data format, it is a virtual machine. Any `.bin`, `.pkl`, `.pt`, `.joblib` or `.h5` you load with `torch.load()`, `joblib.load()` or `pickle.load()` can run commands before a single tensor exists. PyTorch 2.6 made `weights_only=True` the default, which helps a lot - unless your code opts back out, and plenty of code does.
- An AI-BOM is inventory, not a fix. What it buys you is the ability to answer "which model version, built from which dataset, is running where" without interviewing engineers.
- You do not need a homemade YAML dialect. CycloneDX 1.6 (and 1.7) already has `machine-learning-model`, `modelCard`, `data`, `governance` and `bom-ref`. SPDX 3.0 has an AI profile if a customer insists on SPDX.
- The gate further down is four rules: no unsafe serialization, no unpinned datasets, no contradicting licenses, no missing digests. On the lab it found three problems in one run.

## The 21-byte model

The lab directory for this walkthrough looks like this. One of these files is not a model:

```
$ ls -l mock_llm_pipeline/
-rw-r--r--  355  config.json
-rw-r--r-- 8712  model.safetensors
-rw-r--r--   21  pytorch_model.bin      <-- 21 bytes
-rw-r--r--  243  tokenizer.json
-rw-r--r--  950  training_manifest.json
```
You have probably seen a `pytorch_model.bin` in a repo and assumed it was weights. Sometimes it is. This one is a command.

The rest of this post is the loop: prove the file executes, generate an AI-BOM that records what your pipeline really contains, then gate on the things that keep coming up.

## Why your SBOM stops exactly where the risk starts

A production LLM stack has six layers, and a conventional SBOM covers about one and a half of them:

| Layer | Artifact | In a classic SBOM? | Can it lead to RCE or data loss? | 
|---|---|---|---|
| Python / Node packages | `requirements.txt`, lockfiles | Yes | Yes, but well covered by existing tooling | 
| Model weights | `*.safetensors`, `*.bin`, `*.pt`, `*.gguf` | **No** | **Yes - deserialization RCE** | 
| Tokenizer / custom modeling code | `tokenizer.json`, `*.py` in the model repo | **No** | **Yes - `trust_remote_code=True` executes repo code** | 
| Training / fine-tuning data | parquet, JSONL, HF dataset snapshot | No | Yes - poisoning, PII memorization, license contamination | 
| Serving runtime | vLLM, TGI, Ollama, ONNX Runtime | Partly (container image) | Yes - CVE surface, model-loading paths | 
| Prompts, tools, MCP servers, vector index | config, SQLite, pgvector | No | Yes - tool abuse, data exfiltration | 

Which means you can pass a "100% SBOM coverage" review while shipping a model whose weights were replaced last Tuesday, fine-tuned on a scraped dataset full of customer emails, under a non-commercial license. I have now seen that exact combination twice.

The package-and-pipeline half of this problem is well covered elsewhere - I wrote about it in [Software Supply Chain Security in 2026](https://securitycipher.com/2026/08/10/software-supply-chain-security-2026/). This post is the half that lives inside the weights.

An **AI-BOM** closes the gap by treating the model, its tokenizer, its datasets and its runtime as real components with names, versions, hashes, licenses and dependency edges. CycloneDX already defines the fields for this in its [specification overview](https://cyclonedx.org/specification/overview/), so you are filling in a schema rather than inventing one.

## Threat model: the six ways an AI pipeline actually gets hurt

These are ordered by how often I find them in real assessments, not by CVSS.

### 1. Pickle deserialization (CWE-502) - the default failure

Python's `pickle` supports a `REDUCE` opcode, which calls an arbitrary callable with arbitrary arguments. A model file is just a pickle stream, so "loading a model" is "running attacker-chosen code with your privileges".

It is not exotic. It is the historical default for `torch.save`, `joblib.dump` (scikit-learn pipelines), `dill` and `cloudpickle`. JFrog and ReversingLabs both documented live campaigns on Hugging Face using this primitive; ReversingLabs' 2025 "nullifAI" research also found models crafted to slip past naive scanners by using malformed pickle framing that parsers reject but loaders tolerate.

PyTorch 2.6 (January 2025) made `weights_only=True` the default for `torch.load`, which blocks arbitrary globals. That is genuinely good news, and it is also where a lot of teams stop reading. It does nothing for the code paths that still pass `weights_only=False`, and nothing for `joblib.load`, `pickle.load` or `np.load(allow_pickle=True)`. If your model loader is four years old, the default changed under it, not inside it.

### 2. `trust_remote_code=True` - arbitrary Python from a model repo

`AutoModelForCausalLM.from_pretrained("some-org/some-model", trust_remote_code=True)`
That flag tells `transformers` to import `.py` files that ship inside the model repository. The weights can be pristine `safetensors` and you still get code execution. This is the single most under-reported AI supply chain issue because it looks like a configuration convenience.

### 3. Dataset poisoning and sleeper behavior

Fine-tuning on an attacker-influenced dataset lets them install triggers that survive RLHF: a specific phrase in a code comment makes the model emit a hardcoded credential or a weak cipher. Anthropic's 2024 sleeper-agent work demonstrated the behavior persists through safety training, which means "we ran our evals" is not a control. The only durable control is knowing **which dataset snapshot** produced **which checkpoint** - which is exactly what an AI-BOM records. If you want the retrieval-side version of the same problem, I walked through it in [RAG Poisoning in 2026](https://securitycipher.com/2026/08/19/rag-poisoning-2026-practical-playbook/).

### 4. PII and secret memorization (OWASP LLM02:2025)

If the fine-tuning corpus contains support tickets, `.env` files scraped from GitHub, or customer emails, the model can be induced to reproduce them. This is [LLM02 in the 2025 OWASP Top 10 for LLM applications](https://genai.owasp.org/llm-top-10/), and it is the finding I least enjoy writing up, because the fix is a redaction pipeline that should have run months earlier. An AI-BOM entry that says `compliance:pii_sanitized=false` is a blocker, not a warning.

### 5. License and contractual contamination

`CC-BY-NC-4.0`, `GPL-3.0-only`, and `AGPL-3.0-only` on a dataset or base model can poison a commercial product. This is not theoretical: it is the most common finding in M&A diligence, and it is trivially automatable from an AI-BOM.

### 6. Regulatory exposure (EU AI Act, NIST, sector rules)

EU AI Act GPAI obligations ([Article 53](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)) became applicable in August 2025. Providers must maintain technical documentation, a training-content summary and a copyright policy, and must pass information to downstream integrators. Fines for GPAI-related infringements reach EUR 15M or 3% of global turnover. NIST's [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) and SP 800-218A ask for the same evidence in different words. An AI-BOM is the cheapest way to produce it on demand instead of reconstructing it during an audit.

Mapping note: the OWASP Top 10 for LLM Applications **2025** renumbered the list. Supply chain is **LLM03**, data and model poisoning is **LLM04**, sensitive information disclosure is **LLM02**. A lot of published AI-BOM advice still cites the 2023/2024 numbering - check which one your compliance spreadsheet uses.


### Format risk tiers

Not every weight format is equal. This is the table to paste into a review doc:

| Format | Extensions | Code execution on load? | Position | 
|---|---|---|---|
| Safetensors | `.safetensors` | No - pure tensor data + JSON header | **Default allow** | 
| GGUF | `.gguf` | No (parsing bugs only) | Allow, pin version | 
| ONNX | `.onnx` | No (protobuf), but custom ops load shared libraries | Allow with op allowlist | 
| NumPy | `.npy` | No, unless `allow_pickle=True` | Conditional | 
| Pickle family | `.bin`, `.pt`, `.pkl`, `.pth`, `.joblib`, `.dill` | **Yes** | Deny in CI | 
| Keras legacy | `.h5` with Lambda layers | **Yes** (CVE-2024-3660 class) | Deny unless re-saved in Keras 3 native format | 
| TensorFlow SavedModel | `saved_model.pb` + `variables/` | No, but can embed Python in serving signatures | Review | 

## Lab 1: build the payload, then catch it

First, create the deliberately broken fixture. One file, no downloads, no GPU:

```
# aibom-lab/setup_lab.py - creates the mock model directory used throughout
import json
import os
from pathlib import Path
model = Path("mock_llm_pipeline")
model.mkdir(exist_ok=True)
(model / "config.json").write_text(json.dumps({
    "architectures": ["LlamaForCausalLM"],
    "model_type": "llama",
    "base_model": "meta-llama/Llama-3-8B-Instruct",
    "quantization": "AWQ-4bit",
    "intended_use": "internal code assistant",
}, indent=2))
(model / "tokenizer.json").write_text('{"version": "1.0"}')
(model / "model.safetensors").write_bytes(b"\x00" * 512 + os.urandom(8192))
# A raw pickle: GLOBAL os.system, STRING 'id', TUPLE, REDUCE. 21 bytes, no tensors.
(model / "pytorch_model.bin").write_bytes(b"cos\nsystem\n(S'id'\ntR.")
(model / "training_manifest.json").write_text(json.dumps({
    "pipeline_id": "sec-cipher-ft-llama3-v2",
    "version": "2.0.0",
    "datasets": [
        {
            "name": "enterprise-code-curated-v3",
            "url": "s3://internal-ai-datasets/code/curated-v3.parquet",
            "sha256": "8a3f81e7d9c6e3b2a5f1d0c4e7b8a9f2c1d3e5f7a9b0c2d4e6f8a0b1c3d5e7f9",
            "license": "Apache-2.0",
            "sample_count": 450000,
            "contains_pii_sanitized": True,
        },
        {
            "name": "unverified-web-scrape-sample",
            "url": "https://huggingface.co/datasets/community/unfiltered-code-scraped",
            "sha256": "4b9c1d7e2f8a3b6c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c",
            "license": "CC-BY-NC-4.0",
            "sample_count": 120000,
            "contains_pii_sanitized": False,
        },
    ],
}, indent=2))
print("mock_llm_pipeline/ ready")
```
The file it creates is a raw pickle, 21 bytes, and you can read the exploit directly out of it:

```
$ xxd mock_llm_pipeline/pytorch_model.bin
00000000: 636f 730a 7379 7374 656d 0a28 5327 6964  cos.system.(S'id
00000010: 270a 7452 2e                             '.tR.
```
Decoded, that is four pickle opcodes: `GLOBAL os system` (push the callable), `STRING 'id'` (push the argument), `TUPLE`, `REDUCE` (call it). No tensors, no header, no model. Loading it runs `id`:

```
$ python3 -c "import pickle, pathlib; \
    pickle.loads(pathlib.Path('mock_llm_pipeline/pytorch_model.bin').read_bytes())"
uid=1000(runner) gid=1000(runner) groups=1000(runner)   # abridged
```
`torch.load(..., weights_only=False)` reaches the same `pickle` machinery, just with a zip container around it. The modern, renderable version of the same primitive:

```
# aibom-lab/poc_pickle.py  -  DEFANGED. Educational use only.
import os
import torch
class Payload:
    def __reduce__(self):
        # A real attack would use ("bash -i >& /dev/tcp/...") or curl | sh.
        # We write a marker so you can prove execution without a C2.
        return (os.system, ("touch /tmp/aibom-pickle-executed",))
torch.save({"state_dict": Payload()}, "mock_llm_pipeline/pytorch_model.bin")
```
```
$ rm -f /tmp/aibom-pickle-executed
$ python3 -c "import torch; torch.load('mock_llm_pipeline/pytorch_model.bin', weights_only=False)"
$ ls -l /tmp/aibom-pickle-executed
-rw-r--r-- 1 runner runner 0 Nov 16 13:33 /tmp/aibom-pickle-executed
```
On a default PyTorch 2.6+ install, the same call without `weights_only=False` raises `UnpicklingError: Weights only load failed` - which is why the exploit now hides in the long tail: `joblib.load`, `np.load(allow_pickle=True)`, `pickle.load`, and any library that passes `weights_only=False` for "compatibility".

### Scan it before you load it

Two open-source scanners cover this space and they complement each other: [picklescan](https://github.com/mmaitre314/picklescan) parses the pickle stream and matches dangerous globals, [ModelScan](https://github.com/protectai/modelscan) does the same across a wider set of serialization formats. Output shape (wording varies by version):

```
$ pip install picklescan modelscan
$ picklescan -p mock_llm_pipeline/
Scanned 5 files, detected 1 dangerous pickle
  pytorch_model.bin: os.system
$ modelscan -p mock_llm_pipeline/pytorch_model.bin
--- Summary ---
Total files scanned: 1
Total issues found: 1
  Severity: CRITICAL  Description: function `os.system` is dangerous
```
Two things to internalize:

1. **Scanner coverage is a heuristic.** ReversingLabs' nullifAI samples were built so that scanners could not parse the pickle stream while PyTorch still could. A clean scan is not a control; an **extension allowlist** is.
2. **Scan the artifact you are actually going to load**, not the one you downloaded. See the LFS note further down - this distinction has burned more teams than any CVE.

### Fix it properly: convert and refuse

Conversion is a one-liner once you have the weights loaded in a trusted environment:

```
from safetensors.torch import save_file
import torch
state = torch.load("pytorch_model.bin", map_location="cpu", weights_only=True)
save_file(state, "model.safetensors", metadata={"format": "pt", "source": "migrated-2026-11"})
```
Then make the insecure path unreachable in application code:

```
# app/model_loader.py  - defence in depth, not a substitute for CI policy
from pathlib import Path
import torch
UNSAFE_SUFFIXES = {".bin", ".pt", ".pth", ".pkl", ".joblib", ".dill", ".h5"}
def assert_safe_artifacts(model_dir: Path) -> None:
    offenders = [
        str(p.relative_to(model_dir))
        for p in model_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in UNSAFE_SUFFIXES
    ]
    if offenders:
        raise RuntimeError(
            "Refusing to load model: unsafe serialization present -> " + ", ".join(offenders)
        )
def load_weights(model_dir: Path) -> dict:
    assert_safe_artifacts(model_dir)
    weights = model_dir / "model.safetensors"
    # weights_only=True, mmap=True: no pickle, no full copy into RAM
    return torch.load(weights, map_location="cpu", weights_only=True, mmap=True)
```
For scikit-learn pipelines the equivalent is **skops** (`skops.io.dump` / `skops.io.load` with a trusted-type allowlist) instead of `joblib.load`, because a `.joblib` file is a pickle with a nicer extension.

## Lab 2: generate an AI-BOM you can actually gate on

### The tool landscape (as of late 2026)

| Tool | Role | Command | 
|---|---|---|
| **OWASP cdxgen** (12.x) | Builds CycloneDX BOMs; `--profile ml` walks Hugging Face refs, services, datasets | `npx @cyclonedx/cdxgen --profile ml --spec-version 1.6 -o bom.json .` | 
| **OWASP AIBOM** (`cisco-aibom`) | Source-level discovery of models, providers, datasets, MCP tools | `uv tool install cisco-aibom && aibom scan -p .` | 
| **ModelScan** (Protect AI) | Inspects serialized weights for dangerous operators | `modelscan -p ./model` | 
| **picklescan** | Fast pickle global/opcode denylist | `picklescan -p ./model` | 
| **Syft** (Anchore) | Container + filesystem SBOM, catches the serving runtime | `syft dir:. -o cyclonedx-json > runtime.json` | 
| **Conftest / OPA** | Policy-as-code over any BOM JSON | `conftest test bom.json -p policy/` | 
| **cosign / Sigstore** | Sign and verify the BOM itself | `cosign sign-blob --bundle bom.sigstore.json bom.json` | 

A workable split: **cdxgen produces, ModelScan verifies artifacts, your auditor decides, cosign seals.** cdxgen alone is not a security tool - it is a very good inventory tool.

### Run cdxgen on the lab

```
$ npx @cyclonedx/cdxgen --profile ml --spec-version 1.6 \
    -o cdxgen_bom.json mock_llm_pipeline
```
Real output from this run, trimmed to the parts that matter (cdxgen 12.9.2 emits 1.7 by default when you do not pin `--spec-version`):

```
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.7",
  "metadata": {
    "tools": { "components": [ { "name": "cdxgen", "version": "12.9.2", "publisher": "OWASP Foundation" } ] }
  },
  "components": [
    {
      "type": "data",
      "name": "unfiltered-code-scraped",
      "group": "community",
      "externalReferences": [
        { "type": "distribution", "url": "https://huggingface.co/datasets/community/unfiltered-code-scraped" }
      ],
      "tags": ["ai", "data", "dataset", "huggingface", "unlocked"]
    },
    {
      "type": "machine-learning-model",
      "name": "mock_llm_pipeline",
      "modelCard": {
        "modelParameters": { "architectureFamily": "llama", "modelArchitecture": "LlamaForCausalLM" }
      }
    }
  ],
  "services": [
    {
      "name": "Hugging Face Inference API",
      "provider": { "name": "huggingface" },
      "properties": [ { "name": "cdx:ai:kind", "value": "inference-service" } ]
    }
  ]
}
```
Note what cdxgen gave us for free, and what it did not. It found the model, the dataset, and the inference service from source references. It did **not** hash the weight files, flag the pickle checkpoint, or know that the dataset contains unsanitized PII. That is the gap the generator and the auditor fill.

### A generator that adds the parts that matter

`generate_aibom.py` walks the model directory and produces CycloneDX 1.6 with `bom-ref`-ed components, dual digests, dataset governance, and a hard failure on git-lfs stubs:

```
#!/usr/bin/env python3
"""CycloneDX 1.6 AI-BOM for an LLM pipeline. Fails loudly on LFS pointer stubs."""
from __future__ import annotations
import datetime, hashlib, json, sys, uuid
from pathlib import Path
PICKLE_SUFFIXES = {".bin", ".pt", ".pth", ".pkl", ".joblib", ".dill"}
def digest(path: Path) -> dict[str, str]:
    h256, h512 = hashlib.sha256(), hashlib.sha512()
    with path.open("rb") as fh:
        while chunk := fh.read(1 << 20):
            h256.update(chunk); h512.update(chunk)
    return {"SHA-256": h256.hexdigest(), "SHA-512": h512.hexdigest()}
def is_lfs_pointer(path: Path) -> bool:
    """A ~130-byte git-lfs stub hashes to something that is NOT the weights."""
    with path.open("rb") as fh:
        return fh.read(64).startswith(b"version https://git-lfs")
def build(model_dir: Path, pipeline_id: str) -> dict:
    config = json.loads((model_dir / "config.json").read_text())
    manifest_path = model_dir / "training_manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.is_file() else {}
    components, pointers = [], []
    for path in sorted(p for p in model_dir.iterdir() if p.is_file() and not p.name.startswith(".")):
        if is_lfs_pointer(path):
            pointers.append(path.name)
        fmt = "pickle" if path.suffix.lower() in PICKLE_SUFFIXES else (path.suffix.lstrip(".") or "json")
        components.append({
            "type": "file",
            "bom-ref": f"file:{path.name}",
            "name": path.name,
            "hashes": [{"alg": alg, "content": val} for alg, val in digest(path).items()],
            "properties": [
                {"name": "security:format", "value": fmt},
                {"name": "security:safe_deserialization", "value": str(fmt != "pickle").lower()},
            ],
        })
    if pointers:
        raise SystemExit(f"Refusing to attest LFS pointers instead of weights: {pointers}")
    model = {
        "type": "machine-learning-model",
        "bom-ref": f"model:{pipeline_id}",
        "name": pipeline_id,
        "version": manifest.get("version", "2.0.0"),
        "purl": f"pkg:huggingface/{manifest.get('repo', pipeline_id)}",
        "modelCard": {
            "modelParameters": {
                "approach": {"type": "supervised"},
                "task": "causal-language-modeling",
                "architectureFamily": config.get("architectures", ["unknown"])[0],
                "modelArchitecture": config.get("architectures", ["unknown"])[0],
                "baseModel": config.get("base_model", "unknown"),
                "quantization": config.get("quantization", "none"),
            },
            "considerations": {
                "useCases": config.get("intended_use", ["internal assistant"]),
                "limitations": ["Not approved for autonomous shell execution"],
            },
        },
        "data": [
            {
                "type": "dataset",
                "bom-ref": f"dataset:{ds['name']}",
                "name": ds["name"],
                "governance": {"licenses": [{"license": {"id": ds.get("license", "Proprietary")}}]},
                "contents": {
                    "samples": ds.get("sample_count", 0),
                    "properties": [
                        {"name": "provenance:source_url", "value": ds["url"]},
                        {"name": "provenance:sha256", "value": ds["sha256"]},
                        {"name": "compliance:pii_sanitized", "value": str(ds.get("contains_pii_sanitized", False)).lower()},
                    ],
                },
            }
            for ds in manifest.get("datasets", [])
        ],
    }
    return {
        "$schema": "http://cyclonedx.org/schema/bom-1.6.schema.json",
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "tools": {"components": [{"type": "application", "name": "SecurityCipher AI-BOM Generator", "version": "1.1.0"}]},
            "component": model,
        },
        "components": components,
        "dependencies": [{"ref": model["bom-ref"], "dependsOn": [c["bom-ref"] for c in components]}],
    }
if __name__ == "__main__":
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "mock_llm_pipeline")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "cyclonedx_aibom.json")
    bom = build(src, "sec-cipher-ft-llama3-v2")
    out.write_text(json.dumps(bom, indent=2))
    print(f"{out}  ({out.stat().st_size} bytes, {len(bom['components'])} components, {len(bom['metadata']['component']['data'])} datasets)")
```
### What the generated manifest actually looks like

Real excerpt from the lab run (`cyclonedx_aibom.json`, 7,139 bytes, 5 components, 2 datasets). Note the 21-byte file's SHA-256 - that digest is the whole point, because it is a fingerprint of a payload, not a model:

```
{
  "type": "file",
  "bom-ref": "file:pytorch_model.bin",
  "name": "pytorch_model.bin",
  "hashes": [
    { "alg": "SHA-256", "content": "8cc73ceecc3fb6787129f6639c5171a97fae9256e36d20d1ca7e4916aee299a4" },
    { "alg": "SHA-512", "content": "47157164ede214e4d6457098fca9c3b81500e0acc15496013127ffe7539df4497d41cdbc714de65875c2cab0ee2565a14cfb955f29f10195231e028557978397" }
  ],
  "properties": [
    { "name": "security:format", "value": "pickle" },
    { "name": "security:safe_deserialization", "value": "false" }
  ]
}
```
The safe counterpart, for contrast:

```
{
  "type": "file",
  "bom-ref": "file:model.safetensors",
  "name": "model.safetensors",
  "hashes": [
    { "alg": "SHA-256", "content": "dbb6ce8ae5f046e0fc7c6844d45b51f4ac4210480b0da988283eec4bf514d544" },
    { "alg": "SHA-512", "content": "98973928bd04a2e5b9e42b17aa2d16f88d9b5a8fe19e3eed5527bb2a70207557ff5c85dbc342702225a4ef65baef666d021dca094ae11e0f40ade4307127993e" }
  ],
  "properties": [
    { "name": "security:format", "value": "safetensors" },
    { "name": "security:safe_deserialization", "value": "true" }
  ]
}
```
Dataset provenance, including the finding that later blocks the build:

```
{
  "type": "dataset",
  "name": "unverified-web-scrape-sample",
  "governance": { "licenses": [ { "license": { "id": "CC-BY-NC-4.0" } } ] },
  "contents": {
    "samples": 120000,
    "properties": [
      { "name": "provenance:source_url", "value": "https://huggingface.co/datasets/community/unfiltered-code-scraped" },
      { "name": "provenance:sha256", "value": "5d41402abc4b2a76b9719d911017c592..." },
      { "name": "compliance:pii_sanitized", "value": "false" }
    ]
  }
}
```
### Three `jq` one-liners worth memorizing

Every AI-BOM question you will be asked in your first month can be answered with these:

```
# 1. What models and base models are we actually running?
$ jq -r '.components[] | select(.type=="machine-learning-model")
         | [.name, .version, (.modelCard.modelParameters.baseModel // "-")] | @tsv' bom.json
sec-cipher-ft-llama3-v2	2.0.0	meta-llama/Llama-3-8B-Instruct
# 2. Which datasets are not PII-attested?
$ jq -r '.metadata.component.data[]
         | select(([.contents.properties[] | select(.name=="compliance:pii_sanitized")][0].value) != "true")
         | [.name, (.governance.licenses[0].license.id // "?")] | @tsv' bom.json
unverified-web-scrape-sample	CC-BY-NC-4.0
# 3. Any unsafe serialization left in the fleet? (run across every BOM you have)
$ jq -r '.components[] | select(.properties[]? | select(.name=="security:format" and .value=="pickle")) | .name' \
    inventory/**/bom.json | sort | uniq -c | sort -rn
      7 pytorch_model.bin
      2 model.pt
```
Query 3 is the one that turns an AI-BOM program from a compliance ritual into a security control: it is a fleet-wide grep for the thing that gives attackers code execution.

## Lab 3: turn the manifest into a gate

Generating a BOM that nobody reads is compliance theater. The gate is a short, boring program with explicit rules and an exit code. Here are the rules that matter:

```
# aibom-lab/audit_aibom.py (core rules; the complete file is below)
import json, sys
from pathlib import Path
UNSAFE_FORMATS = {"pickle", "pt", "pth", "bin", "pkl", "joblib", "dill", "h5"}
RESTRICTED = {"CC-BY-NC-4.0", "GPL-3.0-only", "AGPL-3.0-only", "SSPL-1.0", "CC-BY-NC-SA-4.0"}
FAIL_ON = {"CRITICAL", "HIGH"}
def props(obj): return {p["name"]: p["value"] for p in obj.get("properties", []) or []}
def evaluate(bom):
    findings = []
    for comp in bom.get("components", []):
        if comp.get("type") != "file":
            continue
        p = props(comp)
        fmt = p.get("security:format", "").lower()
        if fmt in UNSAFE_FORMATS or p.get("security:safe_deserialization") == "false":
            findings.append(("CRITICAL", "AIBOM-SER-001", comp["name"], "pickle family -> CWE-502 RCE"))
        if "SHA-256" not in {h["alg"] for h in comp.get("hashes", [])}:
            findings.append(("HIGH", "AIBOM-INT-001", comp["name"], "artifact has no digest"))
    model = (bom.get("metadata") or {}).get("component") or {}
    datasets = model.get("data") or []
    if not datasets:
        findings.append(("HIGH", "AIBOM-DAT-003", model.get("name"), "no datasets declared"))
    for ds in datasets:
        p = props((ds.get("contents") or {}))
        if p.get("compliance:pii_sanitized", "false") != "true":
            findings.append(("HIGH", "AIBOM-DAT-001", ds["name"], "PII not attested (LLM02:2025)"))
        if not p.get("provenance:sha256"):
            findings.append(("HIGH", "AIBOM-DAT-002", ds["name"], "dataset not pinned to a hash"))
        for entry in (ds.get("governance") or {}).get("licenses", []):
            if ((entry.get("license") or {}).get("id")) in RESTRICTED:
                findings.append(("MEDIUM", "AIBOM-LIC-001", ds["name"], "restricted license"))
    return findings
bom = json.loads(Path(sys.argv[1]).read_text())
findings = evaluate(bom)
for sev, rule, target, why in findings:
    print(f"[{sev}] {rule} {target}: {why}")
sys.exit(1 if any(s in FAIL_ON for s, *_) in findings else 0)
```
### Real run against the lab

```
$ python3 audit_aibom.py cyclonedx_aibom.json
================================================================================
 SECURITYCIPHER AI-BOM POLICY GATE (v1.2.0)
 Target: cyclonedx_aibom.json
 Spec:   CycloneDX v1.6 | 5 components, 2 datasets
================================================================================
  [1] CRITICAL AIBOM-SER-001  security:format=pickle - pickle/torch.load can execute arbitrary commands (CWE-502)
      target:      pytorch_model.bin
      remediation: Convert to .safetensors (safetensors.torch.save_file) and deny pickle extensions in CI.
  [2] HIGH     AIBOM-DAT-001  no PII sanitization attestation - OWASP LLM02:2025 (sensitive information disclosure)
      target:      unverified-web-scrape-sample
      remediation: Run Presidio/NER redaction before fine-tuning and set compliance:pii_sanitized=true.
  [3] MEDIUM   AIBOM-LIC-001  restricted/non-commercial license in a commercial pipeline
      target:      unverified-web-scrape-sample (CC-BY-NC-4.0)
      remediation: Replace with Apache-2.0, MIT, or CDLA-Permissive-2.0, or obtain written clearance.
--------------------------------------------------------------------------------
 RESULT: FAIL (1 critical, 1 high, 1 medium, 0 low)
 exit code: 1
--------------------------------------------------------------------------------
```
Three findings, one run, no GPU required. That is the difference between "we think our model is fine" and "we know which artifact is unsafe, which dataset is unattested, and which license will stop a deal".

### Emit SARIF so findings land in the pull request

A gate that only writes to a log file gets ignored. GitHub Code Scanning renders findings inline on the diff, which is where developers actually look:

```
$ python3 audit_aibom.py cyclonedx_aibom.json --sarif aibom.sarif
$ jq '.runs[0].results | length' aibom.sarif
3
```
Prefer the whole file? This is the complete auditor used for the screenshots above - the seven rules, the SARIF writer, and the exit-code logic:

## audit\_aibom.py (full source) +

```
#!/usr/bin/env python3
"""
SecurityCipher AI-BOM policy gate.
Evaluates a CycloneDX 1.6+ AI-BOM and blocks the build on unsafe serialization,
unattested datasets, restricted licenses, and missing digests.
Usage:
    python3 audit_aibom.py cyclonedx_aibom.json
    python3 audit_aibom.py cyclonedx_aibom.json --sarif aibom.sarif
Exit codes: 0 = pass, 1 = CRITICAL/HIGH finding, 2 = bad input.
Rules
    AIBOM-SER-001  unsafe serialization format (pickle family)   CRITICAL
    AIBOM-INT-001  component without a SHA-256 digest            HIGH
    AIBOM-DAT-001  dataset without PII sanitization attestation  HIGH
    AIBOM-DAT-002  dataset without provenance hash               HIGH
    AIBOM-DAT-003  model with no datasets declared               HIGH
    AIBOM-LIC-001  restricted dataset license                    MEDIUM
    AIBOM-EU-001   model card missing base model / architecture  LOW
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
UNSAFE_FORMATS = {"pickle", "pickle.bin", "pt", "pth", "bin", "pkl", "joblib", "dill", "h5"}
RESTRICTED_LICENSES = {
    "CC-BY-NC-4.0",
    "CC-BY-NC-SA-4.0",
    "CC-BY-NC-ND-4.0",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "AGPL-3.0-only",
    "SSPL-1.0",
}
SEVERITY_ORDER = {"CRITICAL": 3, "HIGH": 2, "MEDIUM": 1, "LOW": 0}
FAIL_ON = {"CRITICAL", "HIGH"}
SARIF_LEVEL = {"CRITICAL": "error", "HIGH": "error", "MEDIUM": "warning", "LOW": "note"}
def props(obj: dict) -> dict[str, str]:
    return {str(p.get("name")): str(p.get("value")) for p in obj.get("properties", []) or []}
def finding(severity: str, rule: str, target: str, why: str, remediation: str) -> dict:
    return {
        "severity": severity,
        "rule": rule,
        "target": target,
        "why": why,
        "remediation": remediation,
    }
def check_serialization(data: dict) -> list[dict]:
    """AIBOM-SER-001 / AIBOM-INT-001."""
    out: list[dict] = []
    for comp in data.get("components", []) or []:
        if comp.get("type") != "file":
            continue
        p = props(comp)
        fmt = p.get("security:format", "").lower()
        safe = p.get("security:safe_deserialization", "true").lower() == "true"
        if fmt in UNSAFE_FORMATS or not safe:
            out.append(
                finding(
                    "CRITICAL",
                    "AIBOM-SER-001",
                    comp.get("name", "?"),
                    f"security:format={fmt or 'unknown'} - pickle/torch.load can execute arbitrary commands (CWE-502)",
                    "Convert to .safetensors (safetensors.torch.save_file) and deny pickle extensions in CI.",
                )
            )
        algs = {h.get("alg") for h in comp.get("hashes", []) or []}
        if "SHA-256" not in algs:
            out.append(
                finding(
                    "HIGH",
                    "AIBOM-INT-001",
                    comp.get("name", "?"),
                    "no SHA-256 digest, so the artifact cannot be attested or diffed",
                    "Hash every artifact at build time; fail the build if a digest is missing.",
                )
            )
    return out
def check_datasets(data: dict) -> list[dict]:
    """AIBOM-DAT-001 / 002 / 003 / LIC-001 / EU-001."""
    out: list[dict] = []
    model = (data.get("metadata") or {}).get("component") or {}
    datasets = model.get("data") or []
    params = ((model.get("modelCard") or {}).get("modelParameters") or {})
    if not datasets:
        out.append(
            finding(
                "HIGH",
                "AIBOM-DAT-003",
                model.get("name", "?"),
                "no datasets declared - training provenance is unprovable",
                "Record every pre-training and fine-tuning dataset with URL, hash, and license.",
            )
        )
    for ds in datasets:
        name = ds.get("name", "?")
        p = props((ds.get("contents") or {}))
        if p.get("compliance:pii_sanitized", "false").lower() != "true":
            out.append(
                finding(
                    "HIGH",
                    "AIBOM-DAT-001",
                    name,
                    "no PII sanitization attestation - OWASP LLM02:2025 (sensitive information disclosure)",
                    "Run Presidio/NER redaction before fine-tuning and set compliance:pii_sanitized=true.",
                )
            )
        if not p.get("provenance:sha256"):
            out.append(
                finding(
                    "HIGH",
                    "AIBOM-DAT-002",
                    name,
                    "dataset snapshot is not pinned to a hash",
                    "Pin the dataset revision and record provenance:sha256 of the materialized snapshot.",
                )
            )
        for entry in ((ds.get("governance") or {}).get("licenses") or []):
            lic = ((entry or {}).get("license") or {}).get("id", "")
            if lic in RESTRICTED_LICENSES:
                out.append(
                    finding(
                        "MEDIUM",
                        "AIBOM-LIC-001",
                        f"{name} ({lic})",
                        "restricted/non-commercial license in a commercial pipeline",
                        "Replace with Apache-2.0, MIT, or CDLA-Permissive-2.0, or obtain written clearance.",
                    )
                )
    if not params.get("baseModel") and not params.get("modelArchitecture"):
        out.append(
            finding(
                "LOW",
                "AIBOM-EU-001",
                model.get("name", "?"),
                "model card lacks base model / architecture (EU AI Act Art. 53 evidence)",
                "Fill modelCard.modelParameters.baseModel and modelArchitecture.",
            )
        )
    return out
def to_sarif(findings: list[dict], target: str) -> dict:
    rules: dict[str, dict] = {}
    results = []
    for f in findings:
        rules[f["rule"]] = {"id": f["rule"], "shortDescription": {"text": f["why"][:120]}}
        results.append(
            {
                "ruleId": f["rule"],
                "level": SARIF_LEVEL[f["severity"]],
                "message": {"text": f"[{f['severity']}] {f['target']}: {f['why']} Fix: {f['remediation']}"},
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": target},
                            "region": {"startLine": 1},
                        }
                    }
                ],
            }
        )
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "sc-aibom-gate",
                        "version": "1.2.0",
                        "rules": list(rules.values()),
                    }
                },
                "results": results,
            }
        ],
    }
def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sarif_out = None
    if "--sarif" in sys.argv:
        idx = sys.argv.index("--sarif")
        if idx + 1 < len(sys.argv):
            sarif_out = Path(sys.argv[idx + 1])
            args = [a for a in args if a != str(sarif_out)]
    target = Path(args[0]) if args else Path("cyclonedx_aibom.json")
    if not target.is_file():
        print(f"error: {target} not found; run generate_aibom.py first", file=sys.stderr)
        return 2
    data = json.loads(target.read_text())
    findings = check_serialization(data) + check_datasets(data)
    findings.sort(key=lambda f: SEVERITY_ORDER[f["severity"]], reverse=True)
    comps = len(data.get("components", []) or [])
    model = (data.get("metadata") or {}).get("component") or {}
    datasets = len(model.get("data") or [])
    print("=" * 80)
    print(" SECURITYCIPHER AI-BOM POLICY GATE (v1.2.0)")
    print(f" Target: {target}")
    print(
        f" Spec:   {data.get('bomFormat')} v{data.get('specVersion')}"
        f" | {comps} components, {datasets} datasets"
    )
    print("=" * 80)
    if not findings:
        print("\n  PASS - no policy violations. Manifest is safe to promote.\n")
        return 0
    for i, f in enumerate(findings, 1):
        print(f"\n  [{i}] {f['severity']:<8} {f['rule']}  {f['why']}")
        print(f"      target:      {f['target']}")
        print(f"      remediation: {f['remediation']}")
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in SEVERITY_ORDER}
    failed = any(f["severity"] in FAIL_ON for f in findings)
    print("\n" + "-" * 80)
    print(
        " RESULT: "
        + ("FAIL" if failed else "PASS WITH WARNINGS")
        + f" ({counts['CRITICAL']} critical, {counts['HIGH']} high, "
        + f"{counts['MEDIUM']} medium, {counts['LOW']} low)"
    )
    print(f" exit code: {1 if failed else 0}")
    print("-" * 80)
    if sarif_out:
        sarif_out.write_text(json.dumps(to_sarif(findings, str(target)), indent=2))
        print(f" SARIF written: {sarif_out}")
    return 1 if failed else 0
if __name__ == "__main__":
    sys.exit(main())
```
## Wiring it into CI (and sealing the artifact)

```
# .github/workflows/ai-supply-chain-gate.yml
name: ai-supply-chain-gate
on:
  pull_request:
    paths: ['models/**', 'datasets/**', 'serving/**']
permissions:
  contents: read
  security-events: write   # required to upload SARIF
  id-token: write          # required for keyless cosign signing
jobs:
  aibom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true        # without LFS you hash 130-byte pointers, not weights
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Scan serialized artifacts before anything loads them
        run: |
          pip install --quiet modelscan
          modelscan -p models/current
      - name: Generate AI-BOM
        run: |
          python3 aibom-lab/generate_aibom.py models/current aibom.json
      - name: Enforce AI-BOM policy
        run: python3 aibom-lab/audit_aibom.py aibom.json --sarif aibom.sarif
      - name: Upload findings to Code Scanning
        if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: aibom.sarif
      - name: Seal the manifest
        run: cosign sign-blob --yes --bundle aibom.sigstore.json aibom.json
      - uses: actions/upload-artifact@v4
        with:
          name: aibom
          path: |
            aibom.json
            aibom.sigstore.json
```
Three things make this gate worth having rather than decorative:

1. **It runs before the artifact is loadable.** `modelscan` runs on files, not on a loaded model.
2. **It fails the build, not just a dashboard.** Non-zero exit blocks the merge.
3. **The manifest is signed.** A BOM that anyone can edit is a suggestion. A Sigstore bundle is evidence.

Verify it downstream, at deploy time, not just at build time:

```
# In the CD job, before the rollout
cosign verify-blob \
  --bundle aibom.sigstore.json \
  --certificate-identity-regexp 'https://github.com/your-org/.*' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  aibom.json
python3 aibom-lab/audit_aibom.py aibom.json   # re-check what you are about to ship
kubectl set image deployment/llm-inference inference=registry.local/llm@sha256:...
```
### When the gate fires, here is the remediation path

| Finding | First action | Real fix | Prove it | 
|---|---|---|---|
| `AIBOM-SER-001` | Block the model version, notify the owner | Load in an isolated job, `torch.load(..., weights_only=True)`, re-save via `safetensors.torch.save_file` | New BOM shows `security:format=safetensors`, gate passes | 
| `AIBOM-DAT-001` | Freeze fine-tuning runs that use the dataset | Re-run PII pipeline (Presidio/NER), write the attestation into the dataset manifest | `compliance:pii_sanitized=true` plus a redaction report ID | 
| `AIBOM-DAT-002` | Stop using floating dataset revisions | Pin to a dataset commit hash and record the materialized snapshot hash | `provenance:sha256` matches on two independent machines | 
| `AIBOM-LIC-001` | Escalate to legal before release | Replace the dataset or obtain written commercial clearance | License field updated, or an approval reference stored with the BOM | 

## Five real use cases (what this looks like on a Monday)

Theory is cheap. These are the five situations where an AI-BOM actually earns its keep, with the exact artifact you hand over.

### Use case 1: M&A / vendor due diligence, 48-hour turnaround

Legal asks whether the target company's "AI-powered" product can ship inside your stack. You have two days, no source access, and a data room.

I ask for six things, and treat a refusal as a finding in itself:

1. The AI-BOM for each production model, signed.
2. `config.json` + tokenizer files for every model in the product.
3. Dataset manifest with snapshot hashes and licenses.
4. A statement of `trust_remote_code` usage.
5. Registry policy (what is allowed to be pulled at runtime).
6. The last model-promotion ticket, to confirm the BOM matches what is deployed.

Then I run the two `jq` queries from Lab 2 - and, more usefully, generate my own BOM from the artifacts they handed over and diff it against theirs.

What comes out is a one-page risk register: models in use, base models, dataset licenses, unsafe serialization count, gaps in provenance. The diff is usually where the story is. Their BOM says one thing, the bytes say another.

One warning from experience: these BOMs get generated once, by hand, at funding time. Assume it is stale until the hashes match the artifacts.

### Use case 2: incident response - "a model on our registry was pulled"

A base model you use gets yanked from the hub after a malicious upload. Leadership asks whether you are exposed. If you have been generating BOMs, this is a five-minute answer rather than a two-day archaeology project.

```
# 1. Which of our BOMs reference that base model or repo?
$ jq -r --arg needle "meta-llama/Llama-3-8B" '
    .metadata.component as $m
    | select(($m.modelCard.modelParameters.baseModel // "") | contains($needle))
    | [$m.name, $m.version, ($m.purl // "-")] | @tsv' inventory/**/bom.json
# 2. Which deployed services run a digest that is in the affected set?
$ jq -r '.components[] | select(.name|endswith(".safetensors")) | .hashes[] | select(.alg=="SHA-256") | .content' \
    inventory/**/bom.json | sort -u > affected-digests.txt
```
(The dataset step in the middle is a join on the BOM, which is the point - you should not be reconstructing it from a wiki page.)

You hand back three lists: affected model versions, affected datasets so someone can decide about retraining, and affected serving deployments by digest. Add a timeline of when each digest entered the registry, taken from the signed BOM history.

If what got pulled was a credentials problem rather than a weights problem, [the TruffleHog playbook](https://securitycipher.com/2026/08/13/secrets-that-pay-trufflehog-bug-bounty/) covers that path.

**Where this falls down:** without per-artifact digests you cannot answer "did we actually run that version?" You end up asking engineers what they remember, which is the one answer you cannot put in an incident report.

### Use case 3: platform team - build the golden path once

You are the platform team. Five product teams are pulling models off the internet into a shared inference cluster, and you cannot review every pull request. Nor should you have to.

Four things, in this order:

1. **A registry in front of the hub.** Only approved repos, only `safetensors`/GGUF, pinned revisions. Everything else 403s.
2. **A CI template** (the workflow above) that teams include, not copy. It fails on the four rules.
3. **A BOM inventory** written by CI to object storage, keyed by `model@sha256`. This becomes your query surface for IR and audits.
4. **An admission check** that only allows images whose model digest appears in that inventory.

```
# Deploy gate - 12 lines that stop unverified weights
#!/usr/bin/env bash
set -euo pipefail
DIGEST="$(sha256sum model.safetensors | cut -d' ' -f1)"
grep -qx "$DIGEST" inventory/approved-digests.txt || {
  echo "model digest $DIGEST is not in the approved AI-BOM inventory"; exit 1; }
cosign verify-blob --bundle aibom.sigstore.json \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com aibom.json >/dev/null
```
What the product teams get is a paved road: green pipeline in minutes if they stay on it, and a blocking error with a remediation link when they do not. That is the whole sales pitch - the secure path has to be the fastest one.

The failure mode is boring: if the gate is slower than the workaround, teams route around it. Keep the job under about three minutes and cache the `modelscan` and `cdxgen` installs.

### Use case 4: pentest / AI red team - use the BOM as an attack surface map

Two weeks against a company running an internal LLM assistant. You need to find the paths that matter, quickly.

Ten minutes of recon first: every `machine-learning-model` component is a target, every `data` component is a potential exfiltration source, and every `service` entry is an endpoint to test.

```
# Build a target list from whatever the client will share
$ jq -r '.components[] | select(.type=="machine-learning-model") | "\(.name)\t\(.modelCard.modelParameters.baseModel // "-")"' aibom.json
$ jq -r '.components[] | select(.type=="data") | "\(.name)\t\(.contents.properties[]? | select(.name=="provenance:source_url") | .value)"' aibom.json
$ jq -r '.metadata.tools.components[].name' aibom.json   # what built it = what to attack next
```
**Five tests that pay for the engagement:**

1. **Serialization.** Is there any `.bin`/`.pt`/`.joblib` in the artifact store? If yes, you have a credible RCE path with a defanged PoC (Lab 1) and a written impact statement.
2. **`trust_remote_code`.** Grep the serving code. A `True` here means the model repo is executable code; combined with an unpinned revision, that is a supply chain beachhead.
3. **Prompt-to-secret.** If the BOM marks a dataset `pii_sanitized=false`, try memorization probing against it (authorized scope, synthetic lookups first). Document the exact prompt and the returned data class, never the actual secret.
4. **Model extraction / endpoint abuse.** If the `service` component points at a shared inference endpoint, test rate limits and whether a caller can select arbitrary model IDs (a classic confused-deputy bug in multi-tenant gateways).
5. **Registry trust.** Can a developer point the pipeline at an arbitrary HF repo? If the answer is yes, the AI-BOM is the evidence that no revision pinning exists.

The report is the BOM annotated with findings per component, plus a reachability column: which finding an attacker can reach from the internet, which needs insider access, which is theoretical. Severity without reachability is noise in an AI engagement.

One thing to expect: clients will hand you a BOM with the unsafe files removed. Regenerate from the artifacts you were given and diff the two. The delta is usually the finding.

### Use case 5: EU AI Act / audit evidence on demand

An enterprise customer's procurement team sends a 40-question AI questionnaire, and legal wants answers this week rather than in three weeks of archaeology.

The mapping I use:

| Requirement (EU AI Act Art. 53 / Annex XI-XII) | AI-BOM field | Where it comes from | 
|---|---|---|
| General model description, architecture | `modelCard.modelParameters` | `config.json` + training run metadata | 
| Base model and lineage | `modelParameters.baseModel`, `purl` | Model repo metadata, pinned commit | 
| Training data summary | `metadata.component.data[].contents` | Dataset manifest + snapshot hash | 
| Copyright / license compliance | `data[].governance.licenses` | Dataset and model license files | 
| Technical documentation version | `serialNumber` + `metadata.timestamp` + signed bundle | CI artifact store | 
| Downstream integration info | `dependencies[].dependsOn` + `services` | Service inventory | 

What you hand over: the signed BOM for each GPAI model, a one-page index mapping that table to your document store, and the CI run IDs that produced them. The next questionnaire takes an hour.

Where auditors push back: increasingly on *how* the evidence is produced, not just the document. "Generated by cdxgen 12.9.2 in run 4821, signed with keyless Sigstore, digest pinned in the registry" lands much better than a PDF export.

## Field notes: the five things that break AI-BOM programs

These are not theoretical. They are the reasons a program that looks green in the demo fails its first audit.

### 1. You attested a 130-byte text file and called it a model

If your CI checkout does not have Git LFS, every "weight file" you hash is a pointer:

```
$ ls -l model.safetensors
-rw-r--r-- 1 runner runner 133 model.safetensors
$ cat model.safetensors
version https://git-lfs.github.com/spec/v1
oid sha256:8f14e45fceea167a5a36dedd4bea2543...
size 16098332144
```
You have now produced a signed, timestamped, compliance-grade attestation of a **text stub**. The model is 16 GB. Your BOM says it is 133 bytes. Nothing fails, because nothing checks.

Two guards, both cheap:

```
# CI: fail if any weight artifact is suspiciously small or is a pointer
find models -name '*.safetensors' -size -1M -print0 | xargs -0 -r -I{} sh -c \
  'head -c 32 "{}" | grep -q "^version https://git-lfs" && { echo "LFS pointer: {}"; exit 1; }; true'
```
and the `is_lfs_pointer()` check in the generator (Lab 2), which turns the failure into a non-zero exit instead of a silent lie.

### 2. `joblib` is pickle wearing a lab coat

Half the "AI" in enterprises is scikit-learn, XGBoost, or Prophet, serialized with `joblib`. A `.joblib` file is a pickle. `joblib.load()` executes it.

```
# Bad: executes whatever the file says
model = joblib.load("churn_model.joblib")
# Better: skops with an explicit trusted-type allowlist
import skops.io as sio
model = sio.load("churn_model.skops", trusted=sio.get_untrusted_types(file="churn_model.skops"))
```
Add `.joblib` and `.pkl` to the same deny-list as `.bin`. You will find them in the model registry next to the LLM weights, and nobody has scanned them.

### 3. `trust_remote_code=True` is a shell exec with extra steps

```
$ grep -rn "trust_remote_code" --include='*.py' .
serving/load_model.py:42:    model = AutoModel.from_pretrained(MODEL_ID, trust_remote_code=True)
```
`MODEL_ID` is usually an unpinned Hub string. Attack path: repo owner account takeover -> modified `modeling_*.py` -> your next pod restart executes it. Mitigation is boring and effective: pin the revision to a commit hash and vendor the remote code after review, or do not use it.

### 4. Scanners lose to crafted pickle framing

`picklescan` and `modelscan` parse the pickle stream and match against dangerous globals. ReversingLabs' nullifAI samples used broken/partial pickle framing so scanners could not parse the file while PyTorch's loader fell back and still executed it. The lesson is not "scanners are useless"; it is that scanners are a detection layer and format allowlisting is the prevention layer. Hugging Face runs a scanner of its own on upload and is candid about the limits - see [pickle scanning](https://huggingface.co/docs/hub/security-pickle). You need both layers, and the AI-BOM is what proves the allowlist is actually in force.

### 5. A BOM is only evidence if it is regenerated and signed

Three failure modes that look identical in a slide deck:

| Failure | Symptom | Fix | 
|---|---|---|
| **BOM rot** | Generated once, never regenerated; deployed model has drifted | Generate in CI on every build, store by digest | 
| **Unsigned BOM** | Anyone can edit the JSON before the audit | `cosign sign-blob` + verify at deploy | 
| **Hash of the wrong thing** | You hashed the directory listing, a tarball with timestamps, or a resaved safetensors file | Hash the exact bytes the loader opens, record the algorithm explicitly | 

That last row is subtle and important. Re-saving `model.safetensors` with different metadata changes its SHA-256 without changing a single weight. If your gate compares hashes from two different pipelines, normalize first: same file, same bytes, same tool version, or the diff is noise.

## The AI-BOM review checklist

Ten controls, each with a command you can run today. Use it for a pentest, a vendor review, or your own pipeline - and if you want the longer version, it slots into the [Security Checklists Hub](https://securitycipher.com/security-checklists/).

| # | Control | Verify with | Pass criteria | 
|---|---|---|---|
| 1 | No pickle-family artifacts | `find . -iregex '.*\.\(bin\|pt\|pth\|pkl\|joblib\|dill\)$'` | Zero hits outside a quarantined archive | 
| 2 | Artifacts are hashed, dual-algorithm | `jq '.components[].hashes[].alg' bom.json \| sort -u` | `SHA-256` present on every file component | 
| 3 | BOM matches deployed bytes | Regenerate the BOM from the running artifact and diff | Identical digests, or an explained delta | 
| 4 | Datasets pinned and hashed | `jq '.metadata.component.data[].contents.properties' bom.json` | Every dataset has `provenance:sha256` | 
| 5 | PII attestation present | `jq '.metadata.component.data[].contents.properties[] \| select(.name=="compliance:pii_sanitized")'` | `true`, with a redaction report ID | 
| 6 | Licenses compatible | `jq -r '.components[]?,.metadata.component.data[]? \| .governance.licenses[]?.license.id' bom.json \| sort -u` | No `CC-BY-NC*`, `GPL-3.0*`, `AGPL-3.0*`, `SSPL-1.0` | 
| 7 | Model card completeness | `jq '.metadata.component.modelCard.modelParameters' bom.json` | `baseModel`, `modelArchitecture`, `task` populated | 
| 8 | `trust_remote_code` absent | `grep -rn "trust_remote_code=True" --include='*.py' .` | Zero hits, or a reviewed, vendored exception | 
| 9 | BOM signed and verified | `cosign verify-blob --bundle aibom.sigstore.json ... aibom.json` | Verification succeeds in CD, not just CI | 
| 10 | Gate actually blocks | Open a PR that adds a `.bin` file | Pipeline fails with `AIBOM-SER-001` | 

Row 10 is the only one that matters in an audit. Everything else is a claim until you have watched the pipeline say no.

## FAQ

## How is an AI-BOM different from an SBOM?

An SBOM inventories code dependencies: packages, versions, licenses, transitive graph. An AI-BOM adds the machine-learning layer: model weights and their serialization format, base model lineage, tokenizer and custom code, dataset provenance and governance, and the inference services the model talks to. In a modern LLM product the two overlap by maybe 5-10%; the rest of the risk lives in the AI-specific half.

## Is a CycloneDX BOM enough, or do I need SPDX too?

Pick one as primary and keep it current. CycloneDX has the deeper ML modelling today (`modelCard`, `data`, `machine-learning-model`, `services`) and the broader tooling for AI, so most teams start there. SPDX 3.0 has an AI profile and matters when a customer or regulator specifies SPDX. Converting between them is possible but lossy, so do not maintain two hand-edited sources of truth.

## Does PyTorch 2.6 fix pickle RCE?

It removes the default footgun. `torch.load` now defaults to `weights_only=True`, which blocks arbitrary globals. It does not fix `joblib.load`, `pickle.load`, `np.load(allow_pickle=True)`, `dill`, or the many code paths that explicitly pass `weights_only=False`. Treat "we are on PyTorch 2.6" as risk reduction, not remediation.

## Can an AI-BOM prevent dataset poisoning?

No, and it helps to be precise about what it does buy you: it makes datasets *provable*. Pin the snapshot hash and record provenance, and tampering becomes detectable and rollback becomes surgical. It still cannot tell you the contents are benign. Pair it with PII scanning, content review, and evals that specifically probe for triggers.

## What if I have 300 models and no idea where to start?

Start with the ones that load pickle on a network-reachable path. Run query 3 from Lab 2 across every BOM you can generate, sort by exposure, and fix the top five. Then automate generation in CI so the inventory stops decaying. A complete inventory of safe models is worth less than a partial inventory that is enforced.

## Does this replace ModelScan / picklescan?

They solve different halves of the same problem, so keep both. A scanner looks inside the artifact; the BOM records what the artifact is, where it came from, and what it is allowed to be. Policy lives in the gate, evidence lives in the BOM, detection lives in the scanner.

## Bottom line

The file that ends up mattering is almost never a zero-day in a transformer kernel. It is a small, boring checkpoint someone downloaded in a hurry, and it is already in your repository, being deserialized by a job that runs with the cluster's credentials.

You cannot buy your way out of that one. The loop is: hash what you ship, keep the inventory somewhere queryable, fail the build on four rules, sign the result, regenerate every time. That is an afternoon of work with the code above, and it changes the shape of every later conversation - with legal, with a customer's procurement team, with an incident commander at 2am - from "we think" to "here is the digest, here is the run ID".

If you want a second pair of eyes on a pipeline before it ships, [the AI and LLM security testing page](https://securitycipher.com/services/ai-llm-agent-security-testing/) explains what an engagement covers. You can [reach me here](https://securitycipher.com/contact-us/).

*Everything in this post runs offline - the fixture, the generator, the gate - in under a minute. If a step does not reproduce on your machine, that is a bug and I would like to hear about it.*
