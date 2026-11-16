# http://iojs.org/

- **Source URL:** http://iojs.org/
- **Fetched from:** https://nodejs.org/en
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9 (id 9)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Run JavaScript Everywhere

Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.

[Get Node.js®](https://nodejs.org/en/download)

[Get Node.js®](https://nodejs.org/en/download)

[Get security support
for EOL Node.js versions](https://nodejs.org/en/about/eol)Node.js is proudly supported by the partners above

[and more](https://nodejs.org/en/about/partners).

```
// server.mjs
import {  } from 'node:http';
const  = ((, ) => {
  .(200, { 'Content-Type': 'text/plain' });
  .('Hello World!\n');
});
// starts a simple http server locally on port 3000
.(3000, '127.0.0.1', () => {
  .('Listening on 127.0.0.1:3000');
});
// run with `node server.mjs`
```
```
// tests.mjs
import  from 'node:assert';
import  from 'node:test';
('that 1 is equal 1', () => {
  .(1, 1);
});
('that throws as 1 is not equal 2', () => {
  // throws an exception because 1 != 2
  .(1, 2);
});
// run with `node tests.mjs`
```
```
// crypto.mjs
import {  } from 'node:crypto';
import {  } from 'node:fs/promises';
const  = ('sha1');
.('hex');
// ensure you have a `package.json` file for this test!
.(await ('package.json'));
.();
const  = .();
// run with `node crypto.mjs`
```
```
// streams.mjs
import { ,  } from 'node:fs';
import {  } from 'node:stream/promises';
import {  } from 'node:zlib';
// ensure you have a `package.json` file for this test!
await (
  ('package.json'),
  (),
  ('package.json.gz')
);
// run with `node streams.mjs`
```
```
// threads.mjs
import { , ,
  ,  } from 'node:worker_threads';
if () {
  const  = 'some data';
  const  = new (import.meta., { :  });
  .('message',  => .('Reply from Thread:', ));
} else {
  const  = ;
  .((.toUpperCase()));
}
// run with `node threads.mjs`
```
Learn more what Node.js is able to offer with our [Learning materials](https://nodejs.org/en/learn).
