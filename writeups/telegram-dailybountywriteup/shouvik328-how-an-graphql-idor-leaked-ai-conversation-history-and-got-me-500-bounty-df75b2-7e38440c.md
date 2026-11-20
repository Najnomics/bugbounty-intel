# How an GraphQL IDOR leaked AI conversation History and Got me $500 bounty

- **Source URL:** https://medium.com/@shouvik328/how-an-graphql-idor-leaked-ai-conversation-history-and-got-me-500-bounty-df75b24a08f7
- **Fetched from:** https://medium.com/feed/@shouvik328
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14992 (id 14992)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### What is IDOR ??

IDOR common web security vulnerability that happens when an application exposes an internal object — such as a user ID, order number, or file path — directly in a URL or request parameter without checking if the logged-in user is actually authorized to view or edit it

### How Malicious Graphql query can leads to IDOR :-

So while Hunting on a target I came up on a AI chat assistant which is designed to help user’s plan their vacation all over the world.

What the assistant primarily does is fetched information of available Flights, best hotels and resorts and plan a nice vacation within your budget.

While playing with the AI bot by Looking at the request & response I got to know the application is using a Graphql endpoint in the backed for fetching data.

**Which gave me an idea**

### Can Graphql query Injection possible ?

To find out I looked at the endpoint [https://api.example.com/umbrella/v2/graphql?featureName=PapayaItinerariesQuery](https://api.example.com/umbrella/v2/graphql?featureName=PapayaItinerariesQuery)

I observed that feature-name PapayaItenerariesQuery is been used for fetching data thought graphql query.

It also contains a field papayaConversationHistory which obviously shows user's coversation with the AI assistant.

**Spoting the IDOR — ->**

To fetch the conversation history of any user an important thing is needed which is the “conversationID” of a particular session.

In the target’s web app whenever a User initiates a conversation with the AI assistant it generates a url with a uuid for each session like this ->

[https://www.example.com/en/search/results?conversation=594b89bb-2c6d-4ac3-a67e-35b61fd0a5a6](https://www.example.com/en/search/results?conversation=594b89bb-2c6d-4ac3-a67e-35b61fd0a5a6)

Here The UUID is present in the url parameter “594b89bb-2c6d-4ac3-a67e-35b61fd0a5a6”

Here I got an Idea

I intercepted the POST request of the GraphQL api in Burpsuite and injected a query with Another user’s ‘conversationID’

```
query {
 papayaConversationHistory(
   conversationID: "<victim's-ID>"
 ) {
   __typename
   ... on PapayaConversation {
     conversationID
     conversation {
       prompt
       promptID
       __typename
     }
   }
   ... on AppError {
     code
     message
     __typename
   }
 }
}
```
by putting the victims’s ‘conversationID’ in the \<victim’s-iD> field throws me all the conversation Other user had with the AI assistant.

And hell yeah without even being authenticated as a user and Attacker can view anyone’s conversation History.

**Conslusion :**

Some times diving Deep into the Target get’s you bugs that automated scanners and other Hunters miss…. So stay Sharp , Stay Curious

**Happy Hacking!**
