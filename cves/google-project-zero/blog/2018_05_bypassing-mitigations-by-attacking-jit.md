# Bypassing Mitigations by Attacking JIT Server in Microsoft Edge - Project Zero

Source: https://projectzero.google/2018/05/bypassing-mitigations-by-attacking-jit.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ivan Fratric, Project Zero


With Windows 10 Creators Update, Microsoft introduced a new security mitigation in Microsoft Edge: [Arbitrary Code Guard (ACG)](https://blogs.windows.com/msedgedev/2017/02/23/mitigating-arbitrary-native-code-execution/). When ACG is applied to a Microsoft Edge Content Process, it makes it impossible to allocate new executable memory within a process or modify existing executable memory. The goal of this is to make it more difficult for an attacker who already gained some capabilities in the browser’s Content Process to execute arbitrary code.


Since modern web browsers rely on Just-In-Time (JIT) compilation of JavaScript to achieve better performance and the code compilation in JIT is incompatible with ACG, a custom solution was needed to enable ACG in Microsoft Edge: The JIT engine was separated from the Edge Content Process into a separate, JIT Process.


We analyzed ACG and tried to answer the question of how useful this mitigation is going to be in preventing an attacker from exploiting Microsoft Edge. Additionally, we examined the implementation of the JIT server and uncovered multiple issues in it (that have been fixed at the time of publishing this). While the paper focuses on Microsoft Edge, we believe that any other attempt to implement out-of-process JIT would encounter similar problems. Thus we hope that this work would be useful for other vendors who might consider employing similar mitigations.
