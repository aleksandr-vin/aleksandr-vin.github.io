---
title:  "WebAssembly seems much more closer"
tags:   wasm js web fast performance dev browser optimization
---

I already heard about it but not really.

It appeared again as a post https://harshal.sheth.io/2022/01/31/webassembly.html
From where it took me to the https://developers.google.com/web/updates/2019/02/hotpath-with-wasm
Which is awesome and I have some quick notes:

1. Long running js parts, hot-paths, which are not good optimized by browsers, can be compiled in WebAssembly
2. Different browsers have different optimization strategies for js
3. You can write in TypeScript for WebAssembly using 
https://github.com/AssemblyScript/assemblyscript


