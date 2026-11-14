# October 2026 Patch Audit: PHP2Shell, GitLab, Node, LiteLLM - SecurityCipher

- **Source URL:** https://securitycipher.com/2026/10/26/october-2026-patch-audit-php2shell-gitlab-litellm
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14961 (id 14961)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Most teams patched PHP2Shell on 21 or 22 October and closed the ticket. A lot of those tickets are wrong. The package got upgraded but the FPM pool never restarted. The host got patched but the containers on it did not. GitLab went to 19.4.2 for the 12 October bug, and then a second CVSS 10 shipped on the 21st that 19.4.2 does not cover. And somewhere a CI job pulled `litellm:main-stable` during a two-hour window and nobody has looked since.

This is the audit for the October 2026 batch: PHP2Shell, both GitLab criticals, the Node.js security release, LiteLLM 1.107.0 and the eMudhra root removal. It does not tell you what to patch. It tells you how to prove the patch you already shipped actually took. Every command was run for real in a throwaway lab, one container on the old builds and one on the fixed ones. Start with the read-only script below for hosts and the SBOM hunt for images, and you will know which sections you can skip.

## The 15-minute audit

1. **LiteLLM first, if you run it anywhere.** Search for `cook.pth`, `litellm-1.107.0.dist-info` and the bad image digest. A hit means rotate every credential that host could read, then rebuild. Pin `1.106.2`.
2. **Internet-facing PHP.** Confirm **8.5.12, 8.4.27, 8.3.36 or 8.2.35** (or a backport that names both CVEs), then prove the running worker started after the upgrade. mod\_php hosts first.
3. **Self-managed GitLab. 19.5.1, 19.4.3 or 19.3.6** (backports: 19.2.9, 19.1.9, 19.0.10, 18.11.13). The 12 October release, 19.4.2, is not enough.
4. **Node.js. 22.23.4, 24.22.1 or 26.12.1**, inside the image your service actually starts. 18.x, 20.x, 23.x and 25.x get nothing.
5. **Certificates.** Chrome stops trusting the emSign ECC root from 27 October. Anything you serve that chains to eMudhra / emSign needs a new certificate. Update `ca-certificates` everywhere else.

## Run one script on every Linux host first

Version banners lie and people forget the second PHP. So the first step is a script that asks the box directly. It finds every PHP and Node binary in the usual places, flags mod\_php, compares the start time of each FPM or Apache master with the PHP files on disk, reads the Omnibus GitLab version, and sweeps for the LiteLLM payload files and markers. It changes nothing and it never starts Python, which matters because starting Python is what triggers the LiteLLM payload.

```
#!/usr/bin/env bash
# patch-week-check.sh - read-only audit of the October 2026 fixes
# PHP2Shell, GitLab CVE-2026-110264, Node.js 21 Oct release, LiteLLM 1.107.0.
# Changes nothing. Never starts Python. Run as root to see every process.
set -u
RED=$'\033[91m'; GRN=$'\033[92m'; YEL=$'\033[93m'; DIM=$'\033[90m'; BLD=$'\033[1m'; RST=$'\033[0m'
FAILS=0; CHECKS=0
bad()  { printf '  %sFAIL%s   %s\n' "$RED" "$RST" "$*"; FAILS=$((FAILS+1)); }
ok()   { printf '  %sOK%s     %s\n' "$GRN" "$RST" "$*"; }
chk()  { printf '  %sCHECK%s  %s\n' "$YEL" "$RST" "$*"; CHECKS=$((CHECKS+1)); }
hdr()  { printf '\n%s%s%s\n' "$BLD" "$*" "$RST"; }
# ver_lt A B: true when A is older than B
ver_lt() { [ "$1" != "$2" ] && [ "$(printf '%s\n%s\n' "$1" "$2" | sort -V | head -1)" = "$1" ]; }
SCAN_ROOTS="${SCAN_ROOTS:-/usr /opt /srv /home /root /var/lib /app}"
# ---------------------------------------------------------------- PHP
hdr "PHP2Shell  CVE-2026-109618 / CVE-2026-109619"
php_fixed() {
  case "$1" in
    8.5.*) echo 8.5.12 ;; 8.4.*) echo 8.4.27 ;;
    8.3.*) echo 8.3.36 ;; 8.2.*) echo 8.2.35 ;; *) echo EOL ;;
  esac
}
found_php=0
for bin in $(ls -1 /usr/bin/php* /usr/sbin/php-fpm* /usr/local/bin/php /usr/local/sbin/php-fpm \
             /opt/cpanel/ea-php*/root/usr/bin/php /opt/alt/php*/usr/bin/php 2>/dev/null \
             | grep -E '/php([0-9.]+)?$|/php-fpm([0-9.]+)?$' | sort -u); do
  v=$("$bin" -v 2>/dev/null | awk 'NR==1{print $2}' | sed 's/[-+~].*//')
  [ -z "$v" ] && continue
  found_php=1
  f=$(php_fixed "$v")
  if [ "$f" = EOL ]; then
    bad "$bin $v is end of life. Needs a vendor backport naming both CVEs, or 8.2.35+"
  elif ver_lt "$v" "$f"; then
    bad "$bin $v  ->  upgrade to $f"
  else
    ok "$bin $v"
  fi
done
[ "$found_php" = 0 ] && ok "no PHP binary found in the usual paths"
for mod in /usr/lib/apache2/modules/libphp*.so /etc/httpd/modules/libphp*.so /usr/lib64/httpd/modules/libphp*.so; do
  [ -e "$mod" ] && chk "mod_php present at $mod. Highest-risk SAPI: patch these hosts first"
done
# Workers that started before the binary was replaced still run the old code.
for p in /proc/[0-9]*; do
  pid=${p#/proc/}
  cmd=$(tr '\0' ' ' < "$p/cmdline" 2>/dev/null)
  case "$cmd" in
    "php-fpm: master"*|*apache2\ -*|*httpd\ -*|apache2|httpd) ;;
    *) continue ;;
  esac
  ppid=$(awk '{print $4}' "$p/stat" 2>/dev/null)
  pcmd=$( { tr '\0' ' ' < "/proc/$ppid/cmdline"; } 2>/dev/null)
  case "$pcmd" in *apache2*|*httpd*) continue ;; esac
  exe=$(readlink "$p/exe" 2>/dev/null) || continue
  started=$(stat -c %Y "$p" 2>/dev/null) || continue
  newest=$(stat -c %Y "$exe" /usr/lib/apache2/modules/libphp*.so /usr/local/sbin/php-fpm 2>/dev/null | sort -n | tail -1)
  if [ -n "$newest" ] && [ "$started" -lt "$newest" ]; then
    bad "pid $pid ($(basename "$exe")) started before PHP was updated. Restart it."
  else
    ok "pid $pid ($(basename "$exe")) started after the current PHP files"
  fi
done
if command -v php >/dev/null 2>&1; then
  up=$(php -r 'echo ini_get("session.upload_progress.enabled") ? "On" : "Off";' 2>/dev/null)
  [ "$up" = "On" ] && chk "session.upload_progress.enabled=On (CLI view). Set Off in php.ini / FPM pool until the next PHP release (CVE-2026-115560)"
fi
# ---------------------------------------------------------------- GitLab
hdr "GitLab  CVE-2026-110264 (21 Oct)  +  CVE-2026-97229 (12 Oct)"
gl_fixed() {
  case "$1" in
    19.5.*) echo 19.5.1 ;; 19.4.*) echo 19.4.3 ;; 19.3.*) echo 19.3.6 ;;
    19.2.*) echo 19.2.9 ;; 19.1.*) echo 19.1.9 ;; 19.0.*) echo 19.0.10 ;;
    18.11.*) echo 18.11.13 ;; *) echo UPGRADE-PATH ;;
  esac
}
if [ -r /opt/gitlab/version-manifest.txt ]; then
  line=$(head -1 /opt/gitlab/version-manifest.txt)
  v=$(echo "$line" | awk '{print $2}')
  f=$(gl_fixed "$v")
  if [ "$f" = UPGRADE-PATH ]; then
    bad "$line has no backport. Follow the upgrade path to 18.11.13 or newer"
  elif ver_lt "$v" "$f"; then
    bad "$line  ->  upgrade to $f (the 12 Oct 19.4.2 / 19.3.5 fixes are NOT enough)"
  else
    ok "$line"
  fi
else
  ok "no Omnibus GitLab on this host"
fi
# ---------------------------------------------------------------- Node.js
hdr "Node.js  CVE-2026-111497 Brotli + 9 more (21 Oct)"
node_fixed() {
  case "$1" in
    26.*) echo 26.12.1 ;; 24.*) echo 24.22.1 ;; 22.*) echo 22.23.4 ;; *) echo EOL ;;
  esac
}
found_node=0
for bin in $(ls -1 /usr/bin/node /usr/local/bin/node /opt/*/bin/node /root/.nvm/versions/node/*/bin/node \
             /home/*/.nvm/versions/node/*/bin/node 2>/dev/null | sort -u); do
  v=$("$bin" -v 2>/dev/null | tr -d v)
  [ -z "$v" ] && continue
  found_node=1
  f=$(node_fixed "$v")
  if [ "$f" = EOL ]; then
    bad "$bin $v is end of life. Move to 22.23.4, 24.22.1 or 26.12.1"
  elif ver_lt "$v" "$f"; then
    bad "$bin $v  ->  upgrade to $f"
  else
    ok "$bin $v"
  fi
done
[ "$found_node" = 0 ] && ok "no Node.js binary found in the usual paths"
# ---------------------------------------------------------------- LiteLLM
hdr "LiteLLM 1.107.0  (PyPI 11:39-13:23 UTC, Docker until 14:20 UTC, 21 Oct)"
hits=$(find $SCAN_ROOTS -xdev \( -name 'cook.pth' -o -name 'cook.py' -o -name 'litellm-1.107.0.dist-info' \) 2>/dev/null)
if [ -n "$hits" ]; then
  while IFS= read -r h; do bad "payload file: $h"; done <<< "$hits"
else
  ok "no cook.pth / cook.py / litellm-1.107.0.dist-info under $SCAN_ROOTS"
fi
while IFS= read -r s; do
  [ -n "$s" ] && chk "sitecustomize.py at $s (some distros ship one; compare against the IOC hashes)"
done <<< "$(find $SCAN_ROOTS -xdev -path '*site-packages/sitecustomize.py' 2>/dev/null)"
for m in /tmp/remote_code_loader.lock /tmp/.pc_once_72129118c59f5636c0bb; do
  [ -e "$m" ] && bad "marker present: $m (treat host as compromised)"
done
if command -v docker >/dev/null 2>&1; then
  if docker images --digests 2>/dev/null | grep -q '1bbcb1443bc962e45f5aad53fe3d2c30600e0379715fb6c664cdd3ac126c339e'; then
    bad "malicious LiteLLM image digest sha256:1bbcb144... is on this host"
  fi
fi
# ---------------------------------------------------------------- summary
printf '\n%s%d FAIL%s, %s%d CHECK%s on %s\n' "$RED" "$FAILS" "$RST" "$YEL" "$CHECKS" "$RST" "$(hostname)"
[ "$FAILS" -eq 0 ]
```
Save it as `patch-week-check.sh`, then run it locally, over SSH, or inside containers:

```
# this host
sudo bash patch-week-check.sh
# a list of hosts, one per line in hosts.txt
while read -r host; do
  echo "== $host"
  ssh -o BatchMode=yes "$host" 'sudo bash -s' < patch-week-check.sh
done < hosts.txt | tee patch-week-report.txt
# every running container
for c in $(docker ps --format '{{.Names}}'); do
  echo "== $c"; docker exec -i "$c" bash -s < patch-week-check.sh
done
```
Read it top to bottom. **FAIL** means a version below the fix, a worker older than the files on disk, or a LiteLLM payload file. **CHECK** means a human should look: mod\_php in use, upload progress still on, or a `sitecustomize.py` that may be your distro's own. The exit code is non-zero when anything failed, so you can wire it into Ansible or a CI job.

## Use SBOMs to find every image that ships it

The script covers boxes you can SSH into. It does not cover the few hundred images in your registry, the build that ran at noon UTC on 21 October and is still deployed, or the base image another team owns. That is what SBOMs are for, and honestly a month like October is where they earn their keep. If you already keep one SBOM per image digest, "where do we run PHP 8.3.35?" is a query over files you have. If you do not, the first one you generate will answer it anyway.

### Generate one per image, from the image

Build the SBOM from the image you ship, not from the source repo. A lockfile does not know that your Dockerfile copies a `node` binary from another stage, or that the base image brought mod\_php with it. `syft` reads the image layers and catches both.

```
# one image
syft docker:shop-web:2026.10.20 -o cyclonedx-json=shop-web.cdx.json
# everything running on this Docker host, one file per image
mkdir -p sboms
for i in $(docker ps --format '{{.Image}}' | sort -u); do
  syft -q "docker:$i" -o cyclonedx-json="sboms/$(echo "$i" | tr '/:' '__').cdx.json"
done
# alternatives: trivy for images, cdxgen for source repos with lockfiles
trivy image --format cyclonedx --output shop-web.cdx.json shop-web:2026.10.20
cdxgen -t php -o composer.cdx.json .
```
Look at what it found in the lab. `libphp` at the Apache module path, which tells you this image runs mod\_php. A `node` binary that no package manager installed, so `dpkg -l` and `npm ls` would both miss it. And `litellm 1.107.0` from the pip metadata. The `ai-gateway` image here is a stub with only the package metadata, no LiteLLM code and no payload.

To make this the default, generate the SBOM in CI right after the push and attach it to the digest:

```
# GitHub Actions, after the image push step (needs permissions: id-token: write, packages: write)
- uses: anchore/sbom-action@v0
  with:
    image: ghcr.io/acme/shop-web@${{ steps.push.outputs.digest }}
    format: cyclonedx-json
    output-file: sbom.cdx.json
- run: cosign attest --yes --type cyclonedx --predicate sbom.cdx.json \
        ghcr.io/acme/shop-web@${{ steps.push.outputs.digest }}
# later, pull the SBOM for any deployed digest
cosign download attestation ghcr.io/acme/shop-web@sha256:... \
  | jq -r .payload | base64 -d | jq .predicate > shop-web.cdx.json
```
### Hunt by version on day one

On the day of a disclosure your scanner's feed may not know the CVE yet, or may map it to the wrong package. You do not need it to. You know the fixed versions, so match on versions. This script reads a folder of CycloneDX files and flags every PHP, Node and LiteLLM component below the October fix, with the path inside the image so whoever owns it knows what to rebuild.

```
#!/usr/bin/env bash
# sbom-hunt.sh - find October 2026 patch gaps in a folder of CycloneDX SBOMs.
# Usage: sbom-hunt.sh [dir-with-*.cdx.json]   (needs jq)
# Matches by version, so it works before your scanner's feed knows the CVE IDs.
set -u
dir="${1:-sboms}"
fails=0
ver_lt() { [ "$1" != "$2" ] && [ "$(printf '%s\n%s\n' "$1" "$2" | sort -V | head -1)" = "$1" ]; }
fixed_for() {
  local name="$1" v="$2"
  case "$name" in
    php|php-cli|php-fpm|libphp)
      case "$v" in
        8.5.*) echo "8.5.12 PHP2Shell" ;; 8.4.*) echo "8.4.27 PHP2Shell" ;;
        8.3.*) echo "8.3.36 PHP2Shell" ;; 8.2.*) echo "8.2.35 PHP2Shell" ;;
        *)     echo "EOL PHP2Shell: no upstream fix, vendor backport or 8.2+" ;;
      esac ;;
    node)
      case "$v" in
        22.*) echo "22.23.4 Node-Oct" ;; 24.*) echo "24.22.1 Node-Oct" ;;
        26.*) echo "26.12.1 Node-Oct" ;;
        *)    echo "EOL Node-Oct: branch gets no fix, move to 22/24/26" ;;
      esac ;;
  esac
}
for f in "$dir"/*.json; do
  img=$(jq -r '.metadata.component | "\(.name // "unknown"):\(.version // "?")"' "$f")
  while IFS=$'\t' read -r name v path; do
    [ -z "$name" ] && continue
    if [ "$name" = "litellm" ]; then
      if [ "$v" = "1.107.0" ]; then
        dist="${path%/METADATA}"
        printf 'FAIL  %-24s litellm %-9s -> 1.106.2 (backdoor)  [site-packages/%s]\n' "$img" "$v" "${dist##*/}"
        fails=$((fails+1))
      fi
      continue
    fi
    read -r fix why <<<"$(fixed_for "$name" "$v")"
    [ -z "${fix:-}" ] && continue
    if [ "$fix" = "EOL" ]; then
      printf 'FAIL  %-24s %-7s %-9s %s  [%s]\n' "$img" "$name" "$v" "$why" "$path"; fails=$((fails+1))
    elif ver_lt "$v" "$fix"; then
      printf 'FAIL  %-24s %-7s %-9s -> %s (%s)  [%s]\n' "$img" "$name" "$v" "$fix" "$why" "$path"; fails=$((fails+1))
    else
      printf 'ok    %-24s %-7s %s\n' "$img" "$name" "$v"
    fi
  done < <(jq -r '.components[]?
      | select(.name | test("^(php|php-cli|php-fpm|libphp|node|litellm)$"))
      | [.name, .version,
         ([.properties[]? | select(.name == "syft:location:0:path") | .value][0] // "-")]
      | @tsv' "$f")
done
echo
echo "$fails finding(s) across $(ls "$dir"/*.json | wc -l | tr -d ' ') SBOM(s)"
[ "$fails" -eq 0 ]
```
It exits non-zero on any finding, so it can gate a deploy. For the next incident, edit `fixed_for` and the component list. That takes five minutes, and it works before any vendor feed does.

### Then run a scanner, and filter hard

Once the feeds catch up, point a scanner at the same files. Scanning an SBOM is fast because nothing gets pulled or unpacked:

```
grype db update
grype sbom:sboms/shop-web_2026.10.20.cdx.json --only-fixed
osv-scanner --sbom=sboms/shop-web_2026.10.20.cdx.json
# or keep every SBOM in Dependency-Track, which re-checks them when new advisories land
curl -X POST "$DT_URL/api/v1/bom" -H "X-Api-Key: $DT_API_KEY" \
  -F autoCreate=true -F projectName=shop-web -F projectVersion=2026.10.20 \
  -F bom=@sboms/shop-web_2026.10.20.cdx.json
```
Two things to notice. The patched image still has 978 findings, nearly all from the Debian base layer, so a raw count tells you nothing about this incident. Filter to the CVE IDs and advisories you are chasing. And the LiteLLM hit is a GitHub malicious-package advisory, not a CVE, so a filter on `CVE-` alone would have dropped it.

This is the gap that matters. With a database built on 26 October, grype maps CVE-2026-111497 to distro `brotli` packages only. Node bundles its own Brotli, zlib, OpenSSL and undici inside one binary, so the SBOM shows a single `node` component, and nothing matches it. The version rule in `sbom-hunt.sh` catches it. For runtimes, match the runtime version against the runtime's own advisory. Do not wait for a library match.

### Where SBOMs will not save you

- **Restarts.** An SBOM describes the image, not the process. A host on 8.3.36 with an FPM master from before the upgrade looks clean. Keep the host script.
- **GitLab Omnibus.** syft has no cataloger for the Omnibus version manifest. Use `/api/v4/version` or `version-manifest.txt` as shown below.
- **History.** An SBOM of today's rebuild says nothing about what ran on 21 October. Keep SBOMs per digest. CycloneDX stores the generation time, in local time unless you run syft with `TZ=UTC` (CI runners already are). With UTC stamps you can list builds from the LiteLLM window: `jq -r 'select(.metadata.timestamp >= "2026-10-21T11:39" and .metadata.timestamp <= "2026-10-21T14:20") | .metadata.component.name' sboms/*.json`
- **Vendors.** Appliances and SaaS do not hand you their images. Ask for an SBOM or a VEX statement covering these CVE IDs, and write the answer down.
- **Repeat triage.** When you decide a finding does not apply, for example `php-cli` in an image that only runs cron jobs, record it as OpenVEX and pass it with `grype --vex` so the next scan does not reopen it.

## PHP2Shell: patch, restart, prove it

CVE-2026-109618 and CVE-2026-109619 are two memory bugs in code nearly every PHP request touches: out-of-memory handling and error cleanup. No login, CVSS 4.0 score 9.2. PHP calls mod\_php the highest risk, because a request can trigger the bug before your application code runs. Every web SAPI is affected: PHP-FPM, mod\_php, php-cgi, FrankenPHP and LiteSpeed.

Where it stood on 25 October: AWS saw a first attempt in its honeypots on 17 October, four days before the fix. Cloudflare counted millions of blocked attempts in the first days. Unit 42 described one successful intrusion at a European government body. CISA had not added either CVE to KEV as of the 23 October catalog. Rapid7 and Sansec both say the public exploits only work under narrow conditions. That last part is not a reason to wait. It is a reason to expect a better exploit.

| Branch | Vulnerable | Install | 
|---|---|---|
| 8.5 | 8.5.0 to 8.5.11 | **8.5.12** | 
| 8.4 | 8.4.0 to 8.4.26 | **8.4.27** | 
| 8.3 | 8.3.0 to 8.3.35 | **8.3.36** | 
| 8.2 | 8.2.0 to 8.2.34 | **8.2.35** | 
| 8.1, 8.0, 7.4 | all | Vendor backport naming both CVEs, php.net source backport, or move to 8.2+ | 

### Find every PHP that serves traffic

`php -v` answers for the CLI. Your visitors hit FPM pools or an Apache module, and old servers often have a second branch installed that one forgotten vhost still uses.

```
systemctl list-units --all 'php*' 'apache2*' 'httpd*'
php-fpm8.3 -v            # Debian/Ubuntu naming, use your branch
php-fpm -v               # RHEL family
apachectl -M 2>/dev/null | grep -i php
# hosting panels run several builds side by side
ls -d /opt/cpanel/ea-php*/ /opt/alt/php*/ 2>/dev/null
```
Containers carry their own PHP. Ask each one:

```
for c in $(docker ps --format '{{.Names}}'); do
  printf '%-24s ' "$c"; docker exec "$c" php -v 2>&1 | head -1
done
```
### Patch by platform

```
# Debian / Ubuntu
sudo apt-get update
sudo apt-get install --only-upgrade 'php8.3-*'
apt changelog php8.3-fpm | grep -E 'CVE-2026-10961[89]'
# RHEL / Alma / Rocky (AppStream or Remi)
sudo dnf upgrade 'php*'
rpm -q --changelog php-fpm | grep -E 'CVE-2026-10961[89]'
# Docker: rebuild from a fixed base, then replace the container
docker compose build --pull && docker compose up -d
```
Ubuntu LTS, Debian stable and CloudLinux backport the fix without bumping the version, so `8.1.2` on Ubuntu 22.04 can be patched and a plain version check will call it vulnerable. The changelog grep is the tiebreaker. If neither CVE ID shows up, you are not patched, whatever the version says.

Managed hosting and PaaS each have a different answer. Laravel Cloud patched running apps without a redeploy. Laravel Vapor needs a redeploy. Forge has no update path on Ubuntu 20.04 and older. On shared hosting, ask support which PHP build serves your site and when the workers restarted, and get the answer in writing.

### Restart, then prove the worker is new

This is the trap that keeps biting. The package manager replaces the files, the old master process keeps the old code mapped, and the ticket closes on a green `php -v`. Use a full restart, not a reload, then compare start time with upgrade time:

```
sudo systemctl restart php8.3-fpm      # or: apache2 / httpd for mod_php
ps -eo pid,lstart,cmd | grep -E '[p]hp-fpm: master|[a]pache2 -k|[h]ttpd -k'
grep ' upgrade .*php' /var/log/dpkg.log | tail -3   # Debian/Ubuntu
rpm -q --last php-fpm                               # RHEL family
```
### If a host still cannot be patched

These come from PHP's own advisory. They block specific attack paths and nothing more. Set them where they apply before request parsing: `php.ini`, the FPM pool, or the Apache vhost. `ini_set()` and `.user.ini` are too late.

```
; /etc/php/8.3/fpm/conf.d/zz-php2shell.ini  (path varies)
session.upload_progress.enabled = 0   ; blocks the confirmed CVE-2026-109619 paths
fatal_error_backtraces = 0            ; PHP 8.5 only
post_max_size = 8M                    ; 32M if you need uploads
upload_max_filesize = 6M              ; keep below post_max_size
; then: sudo systemctl restart php8.3-fpm
```
PHP also suggests `memory_limit=-1` for CVE-2026-109618. I would only do that with a container or cgroup memory cap behind it, or one bad request takes the whole box. If the host is on 8.1 or older and you have no backport, CISA's advice is blunt: take it offline. Use `systemctl disable --now php8.1-fpm`, not `stop`, so a reboot does not quietly bring it back.

Keep `session.upload_progress.enabled=0` even after you patch. On 23 October PHP published CVE-2026-115560, a follow-up that only matters if an app switches `session.serialize_handler` at runtime. The fix comes in the next regular release, and the setting is the stopgap until then.

### Scan your own hosts, carefully

The current Nuclei template for CVE-2026-109618 (templates v10.5.1, 23 October) is not a banner check. It sends up to three multipart probes per URL, 1, 8 and 20 MiB, and looks for a PHP memory-exhaustion error or an empty 500 from a crashed FPM worker. That is why it catches backported-but-unpatched and patched-but-old-banner cases. It is also why you only point it at hosts you own, rate limited.

```
nuclei -update-templates
nuclei -id CVE-2026-109618 -l my-php-hosts.txt -rl 5 -c 5 -o php2shell-hits.txt
```
Assetnote's open-source `php2shell-scanner` uses the same logic and lets you force `--sapi mod_php` or `--sapi fpm`. After you patch and restart, rerun the scan. A host that still matches has a pool you did not restart.

### If workers exit with code 137 after the update

The fix changed how PHP handles running out of memory and added a `memory_hard_limit_percent` setting. Past the hard limit the process now exits with code 137 instead of throwing a catchable error. Several regressions against 8.5.12 and 8.4.27 are open in the PHP tracker (issues 24492, 24493, 24497, 24631). If a batch job started dying on Wednesday night, look at its memory limits before you call it an attack.

### Hunt back to 17 October

If a host was reachable and unpatched at any point after the 17th, spend twenty minutes on these before you close it. They are leads, not verdicts. Missing logs are a gap, not a clean result.

```
# memory exhaustion bursts (the bug's trigger) in PHP and web server logs
sudo grep -h 'Allowed memory size of' /var/log/php*-fpm.log /var/log/apache2/error.log* 2>/dev/null | wc -l
# empty-bodied 500s (combined log format: $9 status, $10 bytes)
sudo awk '$9==500 && ($10==0 || $10=="-")' /var/log/nginx/access.log* /var/log/apache2/access.log* 2>/dev/null | head
# PHP files written in web roots since the 17th
sudo find /var/www /srv -name '*.php' -newermt 2026-10-17 -printf '%TY-%Tm-%Td %TH:%TM  %p\n' 2>/dev/null | sort
# shells or downloaders spawned by the web user (needs auditd)
sudo ausearch -ui www-data -sc execve --start 10/17/2026 2>/dev/null | grep -E 'exe="/(usr/)?bin/(sh|bash|curl|wget)' | head
# live outbound connections from PHP workers
sudo ss -tnp | grep -E 'php-fpm|apache2|httpd' | grep -v ':80 \|:443 '
```
CISA added a Sigma rule to its alert on 23 October for PHP workers launching shells. If you run a SIEM, import that instead of rebuilding it. If anything above looks wrong, rotate what the PHP user could read (`wp-config.php`, `.env`, database passwords) after you patch, not before.

## GitLab: two CVSS 10s in nine days

Both bugs are integer overflows in GitLab's regular-expression compiler, and both came from the same HackerOne researcher. CVE-2026-97229 was fixed on 12 October in 19.4.2, 19.3.5 and 19.2.8. CVE-2026-110264 was fixed on 21 October and reaches back to **GitLab 7.0**, so GitLab backported it beyond its normal window. GitLab lists no workaround. No exploitation reported yet. A public instance still on 19.4.2 is the first thing I would fix from this list.

| You run | Land on | Notes | 
|---|---|---|
| 19.5.x | **19.5.1** | All 12 fixes in the release | 
| 19.4.x | **19.4.3** | 19.4.2 only fixes the 12 Oct bug | 
| 19.3.x | **19.3.6** | Skip 19.3.4 (merge request bug with Ona) | 
| 19.2 / 19.1 / 19.0 | **19.2.9 / 19.1.9 / 19.0.10** | Critical fix backported | 
| 18.11.x | **18.11.13** | Critical fix backported | 
| 18.10 and older | Upgrade path | No backport. Follow the official upgrade path | 

Check what is actually running:

```
# Omnibus
sudo head -1 /opt/gitlab/version-manifest.txt
# Docker
docker exec gitlab head -1 /opt/gitlab/version-manifest.txt
# from anywhere, with a read_api token
curl -s -H "PRIVATE-TOKEN: $GITLAB_TOKEN" https://gitlab.example.com/api/v4/version
```
Upgrade within your minor line. Take a backup and confirm background migrations are finished first:

```
sudo gitlab-backup create STRATEGY=copy
sudo gitlab-rails runner -e production \
  'puts Gitlab::Database::BackgroundMigration::BatchedMigration.queued.count'   # want 0
# Omnibus (Debian/Ubuntu), CE users swap gitlab-ee for gitlab-ce
sudo apt-get update && sudo apt-get install gitlab-ee=19.4.3-ee.0
# Docker: pin the exact tag, never :latest
#   image: gitlab/gitlab-ee:19.4.3-ee.0
docker compose pull gitlab && docker compose up -d gitlab
```
While you wait for a window, at least stop strangers from creating accounts. It does not fix CVE-2026-110264, but it removes the cheapest way in on public instances:

`sudo gitlab-rails runner 'ApplicationSetting.current.update!(signup_enabled: false)'`
GitLab published detections with the release for native Onigmo worker crashes and bursts of Org-mode rendering errors. A quick look before you upgrade, plus a list of accounts created since the first fix:

```
sudo grep -ciE 'onigmo|SIGSEGV' /var/log/gitlab/puma/puma_stderr.log /var/log/gitlab/sidekiq/current
sudo gitlab-rails runner \
  'User.where("created_at > ?", "2026-10-12").pluck(:username, :created_at).each { |u| p u }'
```
## Node.js: upgrade the runtime the container actually starts

The 21 October release fixes ten issues across 22.x, 24.x and 26.x. The headline is CVE-2026-111497, an out-of-bounds write in the bundled Brotli decoder: a process that decompresses attacker-supplied Brotli can crash, leak memory, or run code. That includes fetching a Brotli-encoded response from somewhere you do not control, not only parsing request bodies.

- **CVE-2026-106069, CVE-2026-105483** (high): TLS hostname checks that accept the wrong certificate for non-canonical IPs.
- **CVE-2026-105482** (high): `dns.resolve` truncates at a NUL byte.
- **CVE-2026-106074** (medium): `crypto.randomUUID()` caches baked into startup snapshots and single-executable builds. Rebuild SEA binaries after upgrading.
- Root store update that drops the compromised eMudhra intermediates. One upgrade, two problems.

| Line | Install | Status | 
|---|---|---|
| 26.x | **26.12.1** | Current | 
| 24.x | **24.22.1** | LTS | 
| 22.x | **22.23.4** | LTS | 
| 25.x, 23.x, 20.x, 18.x | none | End of life. Move to a supported line | 

Find the code paths that matter, then check the version where it runs:

```
grep -rnE "brotliDecompress|createBrotliDecompress|Accept-Encoding.*br" src/ node_modules/ --include=*.js | head
# what each running pod's image is
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}/{.metadata.name}{"\t"}{.spec.containers[*].image}{"\n"}{end}' | grep -i node
# inside an image, not on your laptop
docker run --rm --entrypoint node your-registry/api:prod -v
```
Then upgrade and pin. Floating tags like `node:22` are whatever your build cache had:

```
nvm install 22.23.4 && nvm alias default 22.23.4
# Dockerfile: pin the version and the digest
docker buildx imagetools inspect node:22.23.4-slim | grep Digest
#   FROM node:22.23.4-slim@sha256:<digest from above>
docker build --pull -t your-registry/api:prod . && docker push your-registry/api:prod
```
`docker restart` on last month's image changes nothing. Roll the deployment so new pods pull the new image.

## LiteLLM 1.107.0: hunt from outside, rebuild, rotate

On 21 October someone used stolen GitHub CLI OAuth tokens from LiteLLM engineers to run the release workflow against a lookalike repo. All seven `litellm==1.107.0` wheels on PyPI were bad from 11:39 to 13:23 UTC. The Docker tags `v1.107.0`, `latest`, `main-latest` and `main-stable` pointed at the bad image until 14:20 UTC. The git tag was clean, so reviewing source would not have caught it. Enterprise private releases, 1.106.2 and the 1.107.0 release candidates were not affected.

The wheels drop three files into site-packages: `cook.pth`, `cook.py` and `sitecustomize.py`. Python runs them on every interpreter start, so you never have to import litellm, and running `pip` inside that environment runs them again. The stealer takes cloud metadata credentials (and validates AWS ones with STS), SSH keys, browser passwords, `.env` files, CI and kube tokens, AI tool configs, and if `DATABASE_URL` is set, every provider key in the LiteLLM proxy database. It posts an encrypted archive to `www.litellm.dev/healthcheck`.

### Step 1. Find exposure without starting Python

```
# payload files and markers
sudo find / -xdev \( -name cook.pth -o -name cook.py -o -name 'litellm-1.107.0.dist-info' \) 2>/dev/null
ls -la /tmp/remote_code_loader.lock /tmp/.pc_once_72129118c59f5636c0bb 2>/dev/null
# pins, lockfiles, Dockerfiles and compose files that could have pulled it
grep -rnE 'litellm' . --include='requirements*.txt' --include='*.lock' --include='pyproject.toml' \
  --include='Dockerfile*' --include='compose*.y*ml' --include='*.yaml'
# pip and uv caches from the 21st
find ~/.cache/pip ~/.cache/uv -iname '*litellm-1.107.0*' 2>/dev/null
# the known-bad image digest on hosts and in clusters
docker images --digests | grep -i 1bbcb1443bc962e45f5aad53fe3d2c30600e0379715fb6c664cdd3ac126c339e
kubectl get pods -A -o jsonpath='{range .items[*]}{.status.containerStatuses[*].imageID}{"\n"}{end}' | grep 1bbcb1443bc9
```
One caveat from LiteLLM's own note: finding a file proves exposure, not finding one proves nothing. Containers that were recreated and `/tmp` cleanups erase the evidence. If something pulled during the window, treat it as exposed.

### Step 2. Contain and rebuild

```
# from a shell, never from Python
sudo fuser -v /tmp/remote_code_loader.lock     # the loader daemon holds this lock
sudo fuser -k /tmp/remote_code_loader.lock
SP=/path/to/venv/lib/python3.12/site-packages
sudo rm -f $SP/cook.pth $SP/cook.py $SP/sitecustomize.py $SP/__pycache__/cook*.pyc $SP/__pycache__/sitecustomize*.pyc
```
Then throw the environment away. New virtualenv, new image, new CI runner. A half-cleaned site-packages is how this comes back on the next cron job, and a runner hosted every job's secrets, not only the LiteLLM one.

### Step 3. Check whether it phoned home

```
# DNS / proxy logs (adjust paths to your resolver)
sudo grep -hE 'litellm\.dev|letters9813/pythonclient-test' /var/log/syslog* /var/log/squid/access.log* 2>/dev/null | head
# AWS: the stealer calls GetCallerIdentity with the instance role
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=GetCallerIdentity \
  --start-time 2026-10-21T11:30:00Z --end-time 2026-10-21T16:00:00Z \
  --query 'Events[].[EventTime,Username]' --output table
```
On Defender XDR, Microsoft's write-up has hunting queries for the collector domain and the file hashes. The short one:

```
DeviceNetworkEvents
| where Timestamp > datetime(2026-10-21)
| where RemoteUrl has "litellm.dev"
| project Timestamp, DeviceName, RemoteUrl, RemoteIP, InitiatingProcessCommandLine
```
### Step 4. Rotate, in this order

Create the new credential, move the service to it, confirm it works, then revoke the old one at the issuer. If you see evidence of misuse, revoke first and accept the outage.

### Step 5. Pin so the next one cannot walk in

```
# requirements.in
litellm==1.106.2
uv pip compile requirements.in --generate-hashes -o requirements.txt
pip install --require-hashes -r requirements.txt
# images: pin by digest, not by tag
#   FROM ghcr.io/berriai/litellm@sha256:<digest of the 1.106.2 image>
```
## eMudhra: Chrome drops emSign ECC Root CA - G3 on 27 October

Eight eMudhra intermediate keys turned out to be recoverable in milliseconds. Browsers blocked them, eMudhra is leaving public TLS, and Google says the removal of **emSign ECC Root CA - G3** from the Chrome Root Store reaches devices on the morning of 27 October, Pacific time. Two different jobs:

**What you serve.** If your issuer says eMudhra or emSign, replace the certificate with one from another CA.

```
for h in www.example.com api.example.com; do
  printf '%-24s ' "$h"
  echo | openssl s_client -connect "$h:443" -servername "$h" 2>/dev/null | openssl x509 -noout -issuer
done
```
**What you trust.** Update the trust store on servers and in images, then restart long-lived processes that cached the old bundle. The Node.js releases above carry the change. Java has its own store, and Oracle shipped a separate Security Alert, CVE-2026-91403, on 21 October.

```
sudo apt-get update && sudo apt-get install --only-upgrade ca-certificates   # Debian/Ubuntu
sudo dnf upgrade ca-certificates && sudo update-ca-trust                      # RHEL family
```
## Other October fixes still worth checking

| Product | Issue | Do this | 
|---|---|---|
| Arista VeloCloud Orchestrator (on-prem) | CVE-2026-114625, SQLi to operator, **exploited** | 5.2.3.18 / 6.1.3.10 / 6.4.2.12. Block 74.82.197.86 and 38.54.50.151, search logs for both | 
| Plex Media Server | Plex2Shell chain CVE-2026-96652/54/55/56, in KEV | 1.43.3.10861. Look for unknown .so files in Codecs. Stop forwarding 32400 | 
| SiteGuard Server Edition | CVE-2026-106931, root command injection, in KEV | 8.00 Update 5. Collect vendor diagnostics before patching, the update erases traces | 
| Laravel | CVE-2026-114509, TokenGuard auth bypass on MySQL/MariaDB | laravel/framework 12.68.0 or 13.29.0 ( `composer show laravel/framework`) | 
| Cisco Expressway (clustered) | CVE-2026-76466, unauthenticated root | X15.5.20. No workaround | 
| Oracle | October CPU: WebLogic CVE-2026-91323, EBS CVE-2026-101809 | Internet-facing WebLogic and EBS first. Block T3/IIOP at the edge | 
| Still open from KEV | Ivanti Connect Secure CVE-2026-104935, AhsayCBS CVE-2026-105133/105134, Windows CVE-2026-96951 | Patch or pull off the internet | 
| Railway, TiDB Cloud, OpenCode Console | Customer secrets or API keys exposed | Rotate the keys stored there and check provider billing | 

## The audit checklist

Give each line an owner and a piece of evidence. "Done" without evidence is not done.

- **LiteLLM:** sweep hosts, caches, lockfiles and image digests. Hits get rebuilt and every reachable credential rotated. *Evidence: sweep output plus revoked key IDs.*
- **PHP:** every internet-facing host on 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35 or a backport with both CVEs in the changelog, workers restarted, upload progress off. *Evidence: checker exit 0, Nuclei quiet.*
- **PHP hunt:** logs reviewed back to 17 October on anything that was exposed. *Evidence: the five commands above, saved to the ticket.*
- **GitLab:** 19.5.1 / 19.4.3 / 19.3.6 or the backport for your line. Sign-up off until then. *Evidence: /api/v4/version.*
- **Node.js:** 22.23.4 / 24.22.1 / 26.12.1 in every image that runs, digests pinned, SEA binaries rebuilt. *Evidence: node -v inside the deployed image.*
- **Images:** an SBOM for every deployed digest, `sbom-hunt.sh` clean, scanner output filtered to the October IDs. *Evidence: hunt output plus the SBOM files.*
- **Certificates:** nothing you serve chains to emSign, `ca-certificates` current. *Evidence: issuer loop output.*
- **Appliances:** VeloCloud, Plex, SiteGuard, Expressway, Ivanti, Ahsay patched or unplugged.

The rest of October's CVE flood can wait until those lines have evidence next to them.

## Sources

## FAQ

## We upgraded GitLab to 19.4.2 on 12 October. Are we done?

No. 19.4.2 fixed CVE-2026-97229 (12 October). CVE-2026-110264 landed on 21 October and needs **19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10 or 18.11.13**. Every version back to 7.0 is affected. GitLab.com and Dedicated are already patched.

## Does a WAF rule or a php.ini change fix PHP2Shell?

No. PHP says only the update is a complete fix. Turning off `session.upload_progress.enabled`, lowering `post_max_size` and the other settings in this post cut specific attack paths. A WAF buys time. Neither makes an old build safe.

## Is the Nuclei CVE-2026-109618 template safe to run in production?

It is an active check. It sends up to three multipart probes per URL (1, 8 and 20 MiB) and tries to make PHP run out of memory. Most workers recover in a second, but run it against hosts you own, rate limited, ideally in a maintenance window. Never against other people's servers.

## We are on PHP 8.1 or 7.4. What now?

php.net shipped minimal source backports for 7.4, 8.0 and 8.1, and some vendors (CloudLinux, Ubuntu Pro, Remi) ship patched packages that keep the old version number. Check the changelog for both CVE IDs. If you cannot prove a backport, CISA's advice is to take the system offline until it moves to 8.2.35 or newer.

## We never typed litellm==1.107.0. Are we clear?

Not if anything installed an unpinned `litellm` between 11:39 and 13:23 UTC on 21 October, or pulled `latest`, `main-latest`, `main-stable` or `v1.107.0` before 14:20 UTC. Search lockfiles, caches and image digests. Do not run pip inside the suspect environment to check.

## PHP workers exit with code 137 after the upgrade. Is that an attack?

Probably not. The 21 October fix changed out-of-memory handling and added `memory_hard_limit_percent`. Going over the hard limit now ends the process with exit 137. Several regressions are open in the PHP tracker. Look at your memory limits before you open an incident.

## Can our SBOMs tell us which images are affected?

Yes, if they were generated from the images and not only from source lockfiles. Match on the fixed versions first, because scanner feeds lag. On 26 October grype matched PHP2Shell and the LiteLLM advisory but not the Node.js Brotli CVE on the `node` binary. An SBOM will not tell you whether a worker restarted, so keep the host check too.

## Does updating WordPress fix PHP2Shell?

No. The bug is in the PHP interpreter under WordPress. Core and plugin updates do not touch it. Ask your host which PHP build serves your site and when the workers last restarted.
