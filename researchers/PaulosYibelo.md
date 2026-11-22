# @PaulosYibelo

PwnEscape / pwn.ai. Prior: Vercel sandbox KVM escape (CVE-2026-99999). Consistent public technical disclosures on memory-corruption → RCE chains in widely deployed interpreters.

## Finds indexed here

### 2026-11-21 — Upload2Shell / CVE-2026-125396 (Ghostscript Type1 font UAF → RCE)
- **Bug / class:** Use-after-free in Ghostscript `.putgstringcopy` / `.forceput` Type1 font loader; write-what-where → disable `-dSAFER` `path_control_active` → `%pipe%` RCE. CVSS 4.0 8.5 (local AV in CVE); remote chains demonstrated.
- **Root cause:** Font helper uses `.forceput` without type checks; attacker Type1 font traps `typecheck` during `copy`, resumes into `.forceput` with chosen (dict,key,value), plants global→local dangling ref, after `restore` overwrites native refs.
- **How found:** GPT 5.6 Sol + PaulosYibelo source audit of Ghostscript; dependency tracing through ImageMagick/Pillow/Imagick/libvips/Qt EPS/CUPS.
- **Remote entry points demonstrated:** Roundcube email thumbnail (external sender, no click), WordPress PDF preview + Forminator/Essential Addons public uploads, Debian 13 CUPS anonymous IPP Print-Job as `uid=7(lp)`.
- **Takeaways / harness:** Inventory every upload→renderer path; flag Ghostscript < 10.08.0; probe EPS under trusted extensions; CUPS shared queues without auth.
- **Local verbatim:** [posts/PaulosYibelo/2026-11-21-2124203995329933441.md](../posts/PaulosYibelo/2026-11-21-2124203995329933441.md) (tease: [2124181046484979915](../posts/PaulosYibelo/2026-11-21-2124181046484979915.md))
- **Full writeup:** [upload2shell research](../writeups/PaulosYibelo/upload2shell-research-CVE-2026-125396.md) · [landing](../writeups/PaulosYibelo/upload2shell-landing-2026-11-21.md)
