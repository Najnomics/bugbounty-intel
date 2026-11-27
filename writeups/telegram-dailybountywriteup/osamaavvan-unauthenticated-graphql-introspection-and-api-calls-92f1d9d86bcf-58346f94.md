# Unauthenticated GraphQL Introspection and API calls

- **Source URL:** https://medium.com/@osamaavvan/unauthenticated-graphql-introspection-and-api-calls-92f1d9d86bcf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260609091417/https://medium.com/@osamaavvan/unauthenticated-graphql-introspection-and-api-calls-92f1d9d86bcf
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1826 (id 1826)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Unauthenticated GraphQL Introspection and API calls**

Assalam u Alikum Everyone, it’s been a while since my last writeup. So here I am with another interesting finding.

GraphQL Introspection is a feature of the GraphQL specification that allows clients to query information about a GraphQL API’s schema. This can be useful for various purposes, such as generating documentation, building GraphQL clients, and performing validations.

Unauthenticated GraphQL Introspection refers to the ability of anyone, including unauthenticated users, to access the GraphQL Introspection functionality without any restrictions. This means that anyone can query the API’s schema and retrieve all its types, fields, and relationships.

So while hunting on a Bugcrowd Public Program there was a subdomain that doesn’t have any login or signup page or anything interesting so after fuzzing I came across a Graphql endpoint that was allowing Unauthenticated GraphQL Introspection and I was able to make API calls to all the Graphql queries being unauthenticated. To test for the Introspection we will send a POST request with a query.

`{"query": "query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}`
Now copy the whole JSON in the response which is the schema and save it in a file with the .json extension. Now we will use the Burp InQL Scanner Extension, In your Burp Suite click on the InQL scanner tab and click on Load and load the .json file

After the schema is loaded it will create a nice-looking directory structure separating Queries and Mutations.


GraphQL queries are used to fetch data, and they typically take the form of a JSON-like object with a set of fields that define the data to be returned. For example, a query might request a user’s name, email address, and profile picture.

GraphQL mutations, on the other hand, are used to modify data on the server. They allow clients to specify the exact changes they want to make, and they can be used to create, update, or delete data. Mutations are similar to queries in structure, but they are typically used to change data on the server rather than retrieve it.

Now we will use the isEmailAvailable query to see which email is taken meaning if the user has an account or not. Select the **isEmailAvailable.query** and click on the Raw Tab on the top.

The **“code\*”** in the query indicates that it is expecting a string datatype, which is obvious, Now copy the Raw query and send a POST request at the /graphql endpoint with the JSON query.

As I have already created an account with my email so in the Response we can see it says **“is\_email\_available: false”** which means the email is already taken.

Now let’s move to the Mutations, as we now know we can use the mutation query to create/modify data on the server, so now we will be using the **createCustomer.query** to create an account, copy the RAW query and fill the values according to their fields as we know the **“code\*”** will be replaced with the string values but the **gender:** field is without quotes so it means that it will be an integer value.

Sending the POST request with fields filled with their respective data.

The account was created and an access token was returned in the HTTP Response.

Now after creating the account, there was no login page on that subdomain, but after some analysis, it was found that there was another subdomain which was a service portal of the company where these credentials were working and I got access to that portal. That portal had the same Graphql Queries that I had access to before but without any authentication.

Thank you for reading.
