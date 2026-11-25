# JEB MCP 설치 가이드

- **Source URL:** https://medium.com/@2jw2534/jeb-mcp-%EC%84%A4%EC%B9%98-%EA%B0%80%EC%9D%B4%EB%93%9C-64e9aeb96bb2
- **Fetched from:** https://medium.com/@2jw2534/jeb-mcp-%EC%84%A4%EC%B9%98-%EA%B0%80%EC%9D%B4%EB%93%9C-64e9aeb96bb2?source=rss-8ca7df4b7832------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14950 (id 14950)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** roronoa / Fri, 16 Oct 2026 13:00:23 GMT

**1. 저장소 받기**

git clone https://github.com/flankerhqd/jebmcp.git

**2. 플러그인 복사**:

jeb-mcp/src/jeb\_mcp/MCP.py 파일 경로를 확인합니다.

해당 파일을 $JEB\_INSTALLATION\_DIR/scripts에 복사합니다.

**3. JEB에서 스크립트 실행**:

JEB GUI에서 File → Scripts → Scripts selector...로 MCP.py를 선택해 실행합니다.

Logger 창에 아래처럼 나오면 성공입니다.

**4. MCP 클라이언트에 등록**:

\~/.claude.json 파일에 아래 설정을 추가합니다.

```
{
  "mcpServers": {
    "jeb": {
      "type": "stdio",
      "command": "C:\\Users\\holyshit\\.local\\bin\\uv.exe",
      "args": [
        "--directory",
        "C:\\apphackingtool\\jeb-pro\\jeb-mcp",
        "run",
        "src/jeb_mcp/server.py"
      ],
      "env": {}
    }
  }
}
```
5\. Claude Code 실행 후 /mcp에서 jeb 확인
