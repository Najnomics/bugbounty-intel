# Unveiling the Secrets

- **Source URL:** https://medium.com/@soufianehabti/unveiling-the-secrets-ssrf-adventures-in-microsofts-ai-playground-26c7872b32fc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240310131956/https://medium.com/@soufianehabti/unveiling-the-secrets-ssrf-adventures-in-microsofts-ai-playground-26c7872b32fc
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5452 (id 5452)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Unveiling the Secrets: SSRF Adventures in Microsoft’s AI Playground

As-salamu alaykum everyone,

I will discuss a comprehensive SSRF (Server-Side Request Forgery) exploit that [5h3rl0ck](https://medium.com/u/5014f5b262d3?source=post_page-----26c7872b32fc--------------------------------) and I discovered and successfully exploited within one of Microsoft’s AI products, namely Microsoft Designer.

Microsoft Designer is an AI-powered graphic design app that helps you create stunning social media posts, invitations, digital postcards, graphics, and more, all in a flash.

While we were trying to find some IDORs on the application we encountered an endpoint which take some parameters including a parameter called nextlink and retrieve an image from it, and then it generates from it a thumbnail and hosts it on onedrive, seeing that triggered the spidey sense for SSRFs and changed the original url to burp collaborator url, and all we go is a 500 response error with a little header showing a parsing error as it is shown bellow:

After several unsuccessful attempts to reproduce a blind SSRF to the metadata URL from this juncture, we began to feel that we were merely wasting time. Thus, we decided to take a step back and examine the output of the original value for the next URL. It appeared to be a JSON object representing the [drive object](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/resources/drive?view=odsp-graph-online) , and the JSON resembled the following structure:

```
{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('elhabtiesoufiane%40gmail.com')/drive/special('approot')/children",
    "@odata.count": 33,
    "@odata.nextLink": "https://graph.microsoft.com/v1.0/me/drive/special/approot:/My%20stuff:/children?expand=thumbnails(select%3dmedium)&top=9&orderby=lastModifiedDateTime+desc&select=id%2cname%2ccreatedDateTime%2clastModifiedDateTime%2cthumbnails%2cfile%2cimage%2c%40microsoft.graph.downloadUrl&$skiptoken=Mjg",
    "value": [{
        "@microsoft.graph.downloadUrl": "https://public.am.files.1drv.com/y4mKouM8V3c8qPmNuxA6Xuar9ZLAjp5mc_nmElgmPbykqyEx6fA2fIOqOt9JmGK9T7wrPrpGIFl6thL91UYUXJeYAjkoJ29DLcrxIJtjk3XjCK8XSi2rkNL_MN9gSl8jgukYpYIR7H2tPIbSWswzXmxbxgo6dOg3q5FfTbPFAMvlvzNuUzfyIp8aVBL0e4PkG5Z7NXkOJ3S0_3wzzvo2UBH90XlTf5n97OBLcTNLz5fTjo",
        "id": null,
        "name": "check 9.jpg",
        "createdDateTime": "2023-08-29T17:44:24.92Z",
        "lastModifiedDateTime": "2023-08-29T18:07:58.943Z",
        "file": {
            "mimeType": "image/jpeg",
            "hashes": {
                "quickXorHash": "htg9DiY+4UVg4Utg7VVVLudD968=",
                "sha1Hash": "77C14952BFA9BBC809B6267C88385B6C428EFABA",
                "sha256Hash": "7225D72CBB652B45E5883BEB794BC5BB3F7B024CF5E6BAED24F243EEAB988918"
            }
        },
        "image": {
            "height": 800,
            "width": 800
        },
        "thumbnails@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users('elhabtiesoufiane%40gmail.com')/drive/special('approot')/children('FE1AD29AF25F99C0%2119434')/thumbnails",
        "thumbnails": [{
            "medium": {
                "height": 176,
                "url": "SOME ONEDRIVE URL"
            }
        }]
    }
]
}
```
With some debugging we understood that the backend was retrieving value of thumbnails.medium.url, what we did is hosting a similar json object on a server of our own and make the backend send a request to it, so we built the exploit and sent the request, but guess what! no error but an empty response as shown bellow:

But on the bright side we got a call back on our burp collab from a microsoft IP:

At this point seem like we can only retrieve pictures’ thumbnails using our exploit, until suddenly we noticed a request header called Responsetype which was originally set to json, so we tried to set it to html and we got the full response of our burp collaborator:

Then finally we played with this and we accessed the local image of the microsoft designer from an internal IP, and also we request the instance information from the metadata url (we cannot retrieve tokens as it requires some headers):

Thanks everyone for getting this far,

And please pray for Palestine ❤ .
