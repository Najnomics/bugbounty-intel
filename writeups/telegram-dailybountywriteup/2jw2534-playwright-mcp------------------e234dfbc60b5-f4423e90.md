# playwright mcp 설치 가이드

- **Source URL:** https://medium.com/@2jw2534/playwright-mcp-%EC%84%A4%EC%B9%98-%EA%B0%80%EC%9D%B4%EB%93%9C-e234dfbc60b5
- **Fetched from:** https://medium.com/@2jw2534/playwright-mcp-%EC%84%A4%EC%B9%98-%EA%B0%80%EC%9D%B4%EB%93%9C-e234dfbc60b5?source=rss-8ca7df4b7832------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14952 (id 14952)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** roronoa / Sun, 18 Oct 2026 11:08:06 GMT

현재 프로젝트에서 playwright mcp 설치 명령어는 다음과 같습니다.

claude mcp add playwright -- npx @playwright/mcp@latest

모든 프로젝트에서 쓰려면 --scope user를 붙입니다.

claude mcp add --scope user playwright -- npx @playwright/mcp@latest

옵션을 줄 때는 -- 뒤에 이어서 씁니다. 예를 들어 브라우저 창 없이 실행하려면 이렇게 합니다.

claude mcp add playwright -- npx @playwright/mcp@latest --headless

설정 파일을 열어 아래 내용을 추가합니다. Claude Desktop 앱에서 Settings → Developer → Edit Config로도 열 수 있습니다.

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```
