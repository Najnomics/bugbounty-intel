# The Problems and Promise of WebAssembly - Project Zero

Source: https://projectzero.google/2018/08/the-problems-and-promise-of-webassembly.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Natalie Silvanovich, Project Zero


WebAssembly is a format that allows code written in assembly-like instructions to be run from JavaScript. It has recently been implemented in all four major browsers. We reviewed each browser’s WebAssembly implementation and found three vulnerabilities. This blog post gives an overview of the features and attack surface of WebAssembly, as well as the vulnerabilities we found.

### Building WebAssembly


A number of tools can be used to write WebAssembly code. An important [goal](http://webassembly.org/docs/high-level-goals/) of the designers of the format is to be able to compile C and C++ into WebAssembly, and compilers exist to do so. It is likely that other languages will compile into WebAssembly in the future. It is also possible to write WebAssembly in [WebAssembly text format](https://webassembly.github.io/spec/core/text/index.html) which is a direct text representation of [WebAssembly binary format](https://webassembly.github.io/spec/core/binary/index.html), the final format of all WebAssembly code.

### WebAssembly Modules


Code in WebAssembly binary format starts off in an ArrayBuffer or TypedArray in JavaScript. It is then loaded into a WebAssembly Module.


var code = new ArrayBuffer(len);

… // write code into ArrayBuffer

var m = new WebAssembly.Module(code);


A module is an object that contains the code and initialization information specified by the bytes in binary format. When a module is created, it parses the binary, loads needed information into the module, and then translates the WebAssembly instructions into an intermediate bytecode. Verification of the WebAssembly instructions is performed during this translation.


WebAssembly binaries consist of a series of sections (binary blobs) with different lengths and types. The sections supported by WebAssembly binary format are as follows.


| Section | Code | Description | 
| Type | 1 | Contains a list of function signatures used by functions defined and called by the module. Each signature has an index, and can be used by multiple functions by specifying that index. | 
| Imports | 2 | Contains the names and types of objects to be imported. More on this later. | 
| Functions | 3 | The declarations (including the index of a signature specified in the Type Section) of the functions defined in this module. | 
| Table | 4 | Contains details about function tables. More on this later. | 
| Memory | 5 | Contains details about memory. More on this later. | 
| Global | 6 | Global declarations. | 
| Exports | 7 | Contains the names and types of objects and functions that will be exported. | 
| Start | 8 | Specifies a function that will be called on Module start-up. | 
| Elements | 9 | Table initialization information. | 
| Code | 10 | The WebAssembly instructions that make up the body of each function. | 
| Data | 11 | Memory initialization information. | 


If a section has a code that is not specified in the above table, it is called a custom section. Some browsers use custom sections to implement upcoming or experimental features. Unrecognized custom sections are skipped when loading a Module, and can be accessed as TypedArrays in JavaScript.


Module loading starts off by parsing the module. This involves going through each section, verifying its format and then loading the needed information into a native structure inside the WebAssembly engine. Most of the bugs that Project Zero found in WebAssembly occured in this phase.


To start, [CVE-2018-4222](https://bugs.chromium.org/p/project-zero/issues/detail?id=1545) occurs when the WebAssembly binary is read out of the buffer containing it. TypedArray objects in JavaScript can contain offsets at which their underlying ArrayBuffers are accessed. The WebKit implementation of this added the offset to the ArrayBuffer data pointer twice. So the following code:


var b2 = new ArrayBuffer(1000);

var view = new Int8Array(b2, 700); // offset

var mod = new WebAssembly.Module(view);


Will read memory out-of-bounds in an unfixed version of WebKit. Note that this is also a functional error, as it prevents any TypedArray with an offset from being processed correctly by WebAssembly.


[CVE-2018-6092](https://bugs.chromium.org/p/project-zero/issues/detail?id=1546)in Chrome is an example of an issue that occurs when parsing a WebAssembly buffer.

[Similar](https://bugs.chromium.org/p/chromium/issues/detail?id=737069)

[issues](https://bugs.chromium.org/p/chromium/issues/detail?id=647329)

[have](https://bugs.chromium.org/p/chromium/issues/detail?id=789952)been fixed in the past. In this vulnerability, there is an integer overflow when parsing the locals of a function specified in the code section of the binary. The number of locals of each type are added together, and the size\_t that contains this number can wrap on a 32-bit platform.


It is also evident from the section table above (and specified in the WebAssembly standard) that sections must be unique and in the correct order. For example, the function section can’t load unless the type section containing the signatures it needs has been loaded already.

[CVE-2018-4121](https://bugs.chromium.org/p/project-zero/issues/detail?id=1546)is an error in section order checking in WebKit. In unfixed versions of WebKit, the order check gets reset after a custom section is processed, basically allowing sections to occur any number of times in any order. This leads to an overflow in several vectors in WebKit, as its parsing implementation allocates memory based on the assumption that there is only one of each section, and then adds elements to the memory without checking. Even without this implementation detail, though, this bug would likely lead to many subtle memory corruption issues in the WebAssembly engine, as the order and non-duplicate nature of WebAssembly binary sections is very fundamental to the functionality of WebAssembly.


This vulnerability was independently discovered by Alex Plaskett, Fabian Beterke and Georgi Geshev of MWR Labs, and they describe their exploit [here](https://labs.mwrinfosecurity.com/assets/BlogFiles/apple-safari-wasm-section-vuln-write-up-2018-04-16.pdf).

### WebAssembly Instances


After a binary is loaded into a Module, an Instance of the module needs to be created to run the code. An Instance binds the code to imported objects it needs to run, and does some final initialization.


var code = new ArrayBuffer(len);

… // write code into ArrayBuffer

var m = new WebAssembly.Module(code);

var i = new WebAssembly.Instance(m, imports);


Each module has an Import Section it loaded from the WebAssembly binary. This section contains the names and types of objects that must be imported from JavaScript for the code in the module to run. There are four types of object that can be imported. Functions (JavaScript or WebAssembly) can be imported and called from WebAssembly. Numeric types can also be imported from JavaScript to populate globals.


Memory and Table objects are the final two types that can be imported. These are new object types added to JavaScript engines for use in WebAssembly. Memory objects contain the memory used by the WebAssembly code. This memory can be accessed in JavaScript via an ArrayBuffer, and in WebAssembly via load and store instructions. When creating a Memory object, the WebAssembly developer specifies the initial and optional maximum size of the memory. The Memory object is then created with the initial memory size allocated, and the allocated memory size can be increased in JavaScript by calling the grow method, and in WebAssembly using the grow instruction. Memory size can never decrease (at least according to the standard).


Table objects are function tables for WebAssembly. They contain function objects at specific indexes in the table, and these functions can be called from WebAssembly using the call\_indirect instruction. Like memory, tables have an initial and optional maximum size, and their size can be expanded by calling the grow method in JavaScript. Table objects cannot be expanded in WebAssembly.  Table objects can only contain WebAssembly functions, not JavaScript functions, and an exception is thrown if the wrong type of function is added to a Table object. Currently, WebAssembly only supports one Memory object and one Table object per Instance object. This is likely to change in the future though.


More than one Instance object can share the same Memory object and Table object. If two or more Instance objects share both of these objects, they are referred to as being in the same compartment. It is possible to create Instance objects that share a Table object, but not a Memory object, or vice versa, but no compiler should ever create Instances with this property. No compiler ever changes the values in a table after it is initialized, and this is likely to remain true in the future, but it is still possible for JavaScript callers to change them at any time.


There are two ways to add Memory and Table objects to an Instance object. The first is through the Import Section as mentioned above. The second way is to include a Memory or Table Section in the binary. Including these sections causes the WebAssembly engine to create the needed Memory or Table object for the module, with parameters provided in the binary. It is not valid to specify these objects in both the Import Section and the Table or Memory Section, as this would mean there is more than one of each object, which is not currently allowed. Memory and Table objects are not mandatory, and it is fairly common for code in WebAssembly not to have a Table object. It is also possible to create WebAssembly code that does not have a Memory object, for example a function that averages the parameters that are passed in, but this is rare in practice.


One feature of these objects that has led to several vulnerabilities is the ability to increase the size of the allocated Memory or Table object. For example, [CVE-2018-5093](https://www.mozilla.org/en-US/security/advisories/mfsa2018-02/#), a series of integer overflow vulnerabilities in increasing the size of Memory and Table objects was recently found by [OSS-Fuzz](https://opensource.google.com/projects/oss-fuzz). A similar [issue](https://bugs.chromium.org/p/chromium/issues/detail?id=772056) was found in Chrome by OSS-Fuzz.


Another question that immediately comes to mind about Memory objects is whether the internal ArrayBuffer can be detached, as many vulnerabilities have occured in ArrayBuffer detachment. According to the specification, Memory object ArrayBuffers cannot be detached by script, and this is true in all browsers except for Microsoft Edge (Chakra does not allow this, but Edge does). The Memory object ArrayBuffer also do not change size when the Memory object is expanded. Instead, they are detached as soon as the grow method is called. This prevents any bugs that could occur due to ArrayBuffers changing size.


Out of bounds access is always a concern when allowing script to use memory, but these types of issues are fairly uncommon in WebAssembly. One likely reason for this is that a limited number of WebAssembly instructions can access memory, and WebAssembly currently only supports a single page of memory, so the code that accesses memory is a WebAssembly engine is actually quite small. Also, on 64-bit systems, WebAssembly implements memory as safe buffers (also called signal buffers). To understand how safe buffers work, it is important to understand how loads and stores work in WebAssembly. These instructions have two operands, an address and an offset. When memory is accessed, these two operands are added to the pointer to the start of the internal memory of the Memory object, and the resulting location is where the memory access happens. Since both of these operands are 32-bit integers (note that this is likely to change in future versions of WebAssembly), and required to be above zero, a memory access can be at most 0xfffffffe (4GB) outside of the allocated buffer.


Safe buffers work by mapping 4GB into memory space, and then allocating the portion of memory that is actually needed by WebAssembly code as RW memory at the start of the mapped address space. Memory accesses can be at most 4GB from the start of the memory buffer, so all accesses should be in this range. Then, if memory is accessed outside of the allocated memory, it will cause a signal (or equivalent OS error), which is then handled by the WebAssembly engine, and an appropriate out of bounds exception is then thrown in JavaScript. Safe buffers eliminate the need for bounds checks in code, making vulnerabilities due to out-of-bounds access less likely on 64-bit systems. Explicit bounds checking is still required on 32-bit systems, but these are becoming less common.


After the imported objects are loaded, the WebAssembly engine goes through a few more steps to create the Instance Object. The Elements Section of the WebAssembly binary is used to initialize the Table object, if both of these exist, and then the Data Section of the WebAssembly binary is used to initialize the Memory object, if both exist. Then, the code in the Module is used to create functions, and these functions are exported (attached to a JavaScript object, so they are accessible in JavaScript). Finally, if a start function is specified in the Start Section, it is executed, and then the WebAssembly is ready to run!


var b2 = new ArrayBuffer(1000);

var view = new Int8Array(b2, 700); // offset

var mod = new WebAssembly.Module(a);

var i = new WebAssembly.Instance(m, imports);

i.exports.call\_me(); //WebAssembly happens!


The final [issue](https://bugs.chromium.org/p/chromium/issues/detail?id=826434#c1) we found involves a number of these components. It was discovered and fixed by the Chrome team before we found it, so it doesn’t have a CVE, but it’s still an interesting bug.


This issue is related to the call\_indirect instruction which calls a function in the Table object. When the function in the Table object is called, the function can remove itself from the Table object during the call. Before this issue was fixed, Chrome relied on the reference to the function in the Table object to prevent it from being freed during garbage collection. So removing the function from the Table object during a call has the potential to cause the call to use freed memory when it unwinds.


This bug was originally fixed by preventing a Table object from being changed in JavaScript when a WebAssembly call was in progress. Unfortunately, this fix did not completely resolve the issue. Since it is possible to create a WebAssembly Instance in any function, it was still possible to change the Table object by creating an Instance that imports the Table object and has an underlying module with an Elements Section. When the new Instance is created, the Elements Section is used to initialize the Table, allowing the table to be changed without calling the JavaScript function to change a Table object. The issue was ultimately resolved by holding an extra reference to all needed objects for the duration of the call.

### Execution


WebAssembly is executed by calling an exported function. Depending on the engine, the intermediate bytecode generated when the Module was parsed is either interpreted or used to generate native code via JIT. It’s not uncommon for WebAssembly engines to have bugs where the wrong code is generated for certain sequences of instructions; many such issues have been reported in the bugs trackers for the different engines. We didn’t see any such bugs that had a clear security impact though.

### The Future


Overall, the majority of the bugs we found in WebAssembly were related to the parsing of WebAssembly binaries, and this has been mirrored in vulnerabilities reported by other parties. Also, compared to other recent browser features, surprisingly few vulnerabilities have been reported in it. This is likely due to the simplicity of the current design, especially with regards to memory management.


There are two emerging features of WebAssembly that are likely to have a security impact. One is [threading](https://github.com/WebAssembly/threads). Currently, WebAssembly only supports concurrency via JavaScript workers, but this is likely to change. Since JavaScript is designed assuming that this is the only concurrency model, WebAssembly threading has the potential to require a lot of code to be thread safe that did not previously need to be, and this could lead to security problems.

WebAssembly [GC](https://github.com/WebAssembly/gc) is another potential feature of WebAssembly that could lead to security problems. Currently, some uses of WebAssembly have performance problems due to the lack of higher-level memory management in WebAssembly. For example, it is difficult to implement a performant Java Virtual Machine in WebAssembly. If WebAssembly GC is implemented, it will increase the number of applications that WebAssembly can be used for, but it will also make it more likely that vulnerabilities related to memory management will occur in both WebAssembly engines and applications written in WebAssembly.
