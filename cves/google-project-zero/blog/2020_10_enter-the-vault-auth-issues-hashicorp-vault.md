# Enter the Vault: Authentication Issues in HashiCorp Vault - Project Zero

Source: https://projectzero.google/2020/10/enter-the-vault-auth-issues-hashicorp-vault.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Felix Wilhelm, Project Zero

## Introduction

In this blog post I'll discuss two vulnerabilities in HashiCorp Vault and its integration with Amazon Web Services (AWS) and Google Cloud Platform (GCP). These issues can lead to an authentication bypass in configurations that use the aws and gcp auth methods, and demonstrate the type of issues you can find in modern “cloud-native” software. Both vulnerabilities (CVE-2020-16250/16251) were addressed by HashiCorp and are fixed in Vault versions 1.2.5, 1.3.8, 1.4.4 and 1.5.1 released in [August](https://github.com/hashicorp/vault/blob/master/CHANGELOG.md#151).

Vault is a widely used tool for securely storing, generating and accessing secrets such as API keys, passwords or certificates. It can be used as a shared password manager for human users, but its feature set is optimized for API based access by other services. An example use case for Vault is to provide one of your services, such as your webserver, short lived credentials to your database or a third-party resource like an AWS S3 bucket.

Using a central secret storage like Vault offers security benefits such as centralized auditing, enforced credentials rotation or encrypted data storage. However, a central storage is also a very interesting target for an attacker. Exploiting a vulnerability in Vault could give an attacker full access to a wide range of important secrets and large parts of the target's infrastructure.

Before diving into the technical details of the vulnerabilities, the next section gives an overview about Vault’s authentication architecture and the way it integrates with cloud providers. Readers familiar with Vault can feel free to skip this section.

## Authenticating to Vault

Interfacing with Vault requires authentication and Vault supports role-based access control to govern access to stored secrets. For authentication, it supports pluggable [auth methods](https://www.vaultproject.io/api-docs/auth) ranging from static credentials, LDAP or Radius, to full integration into third-party OpenID Connect (OIDC) providers or Cloud Identity Access Management (IAM) platforms. For infrastructure that runs on a supported cloud provider, using the provider's IAM platform for authentication is a logical choice.

Take AWS as an example: Almost every workload you can run in AWS executes in the context of a specific AWS IAM user. By enabling and configuring the [aws auth method](https://www.vaultproject.io/docs/auth/aws), you can create a mapping between certain IAM users or roles to Vault roles.

Imagine that you have an AWS Lambda function and want to give it access to a database password stored in Vault. Instead of storing hard coded credentials in the function code, a Vault administrator can assign a vault role to the Lambda function [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) using the [vault CLI](https://www.vaultproject.io/docs/commands):

This will create a mapping between a vault role named dbclient and the AWS IAM role lambda-role. A vault [policy](https://www.vaultproject.io/docs/concepts/policies) can now be used to grant the dbclient role access to the database secret.

When the lambda function executes, it authenticates to Vault by sending a request to the /v1/auth/aws/login API endpoint. I’ll go into the exact layout of this request later in the post, but for now just assume that the request allows Vault to verify the AWS IAM role of the caller. If authentication succeeds, Vault returns a short-lived API token for the dbclient role back to the lambda function. This token can now be used to fetch the database secret from Vault. Depending on the database backend, this secret could be a static user-password combination, a short lived client certificate or even a [dynamically created credential pair](https://www.vaultproject.io/docs/secrets/databases).

Using Vault in this way has some nice security benefits: The lambda function itself does not need to contain bootstrap credentials and every access to the database credentials is auditable. Rotating old or compromised database credentials is straightforward and can be centrally enforced.

However, this operational simplicity is only possible because of hidden complexity in the AWS iam auth method. How does the /v1/auth/aws/login API endpoint actually work and is there a way a unauthenticated attacker can impersonate a random AWS IAM role? Let’s take a look.

## sts:GetCallerIdentity

Vault’s aws auth method supports two different authentication mechanisms internally: iam and ec2. We are interested in the iam mechanism, which is the recommended variant and also used in our previous Lambda example. iam auth is built on top of an AWS API method called [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html), part of the AWS Security Token Service (STS).

As its name implies, GetCallerIdentity returns details about the IAM role or user whose credentials were used to call the API. To understand how Vault uses this method to authenticate clients we need to understand how AWS APIs perform authentication:

Instead of attaching some form of authentication token or credential to API requests, AWS requires clients to [calculate an HMAC signature](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) for the (canonicalized) request using the caller's secret access key and attach this signature to the request. This mechanism makes it possible to pre-sign a request and forward it to another party to allow a limited form of impersonation. A popular example use case is to give clients the ability to upload a file to S3 without giving them access to credentials with write permissions.

The Vault aws authentication mechanism is a simple variant of this technique.


The client pre-signs an HTTP request to the STS GetCallerIdentity method and sends a serialized version of it to the Vault server. The Vault server sends the pre-signed requests to the STS host and extracts the AWS IAM information out of the result. The server-side part of this flow is implemented in pathLoginUpdate in builtin/credential/aws/path\_login.go:

The function extracts HTTP method, URL, body and headers out of the supplied request body which is stored in data. It then calls submitCallerIdentity to forward the request to the STS server and to fetch and parse the result in parseGetCallerIdentityResponse:


buildHttpRequest creates a http.Request object based on the user supplied parameters, but uses the hardcoded constant [https://sts.amazonaws.com](https://sts.amazonaws.com) to build the target URL.

Without this restriction, we could simply trigger a request to a server under our control and return a fake caller identity.

However, the complete lack of validation for URL path, query, POST body and HTTP headers still looks like a promising attack surface. The next section describes how we can turn this gap into a full authentication bypass.

## STS (Caller) Identity Theft

Our goal is to trick Vault’s submitCallerIdentityRequest function into returning an attacker controlled caller identity. One way to achieve this is to manipulate the Vault server into sending a request to a host we control, bypassing the hardcoded endpoint host. Looking at the buildHttpRequest method, two approaches come to mind:

- The code for calculating targetUrl targetUrl := fmt.Sprintf("%s/%s", endpoint, parsedUrl.RequestURI()) doesn't look very robust against URL parsing issues. However, tricks like embedding a fake userinfo ([https://sts.amazonaws.com/:foo@example.com/test](https://sts.amazonaws.com/:foo@example.com/test)) and similar ideas do not work against the robust Go URL parser.
- Even though Vault will always create a HTTPS request pointing at the hardcoded endpoint, the attacker has full control over the Host http header (request.Host = parsedUrl.Host). This could be a problem if a load balancer in front of the STS API makes routing decisions based on the Host header, but blind testing against the STS host did not lead to any success.

After ruling out the easy way forward, we still have another approach available: Vault does not restrict our URL query parameters. This means we are not limited to pre-signing requests to GetCallerIdentity and can create requests to any action of the [STS API](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html). STS supports 8 different actions, but none gives us the ability to completely control the response. At this point I was slowly getting frustrated and decided to take a look at Vault’s response parsing code:

parseGetCallerIdentityResponse is called on every response received from STS as long as the status code is 200. The function uses the Golang standard XML library to decode an XML response into a GetCallerIdentityResponse structure and returns an error if decoding fails.

There is an easy to miss problem with this code: Vault never enforces or verifies that the STS response is actually XML encoded. While STS responses are XML encoded by default, it also supports JSON encoding for clients that send an Accept: application/json HTTP header.

For Vault, this turns into a security issue due to a somewhat surprising feature of the Go XML decoder: The decoder silently ignores non XML content before and after the expected XML root. This means that calling parseGetCallerIdentityResponse with a (JSON encoded) server response such as ‘{“abc” : “xzy\<GetCallerIdentityResponse>\</GetCallerIdentityResponse>}’ will succeed and return an (empty) CallerIdentityResponse structure.

This brings us really close to our goal of spoofing an arbitrary caller identity: We just need to find a STS action that reflects attacker controlled text as part of its API response. Serialize a request to it while including an Accept: application/json header and put an arbitrary GetCallerIdentityResponse XML blob into the reflected payload.

Finding a reflected parameter that is not constrained to alpha-numeric characters turns out to be tricky. After some trial and error, I decided to target the [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) action and its SubjectFromWebIdentityToken response element. AssumeRoleWithWebIdentity is used to translate JSON Web Tokens (JWT) signed by an OpenID Connect (OIDC)  provider into AWS IAM identities.

Sending a request to this action with a valid signed JWT will return the sub field of the token in the SubjectFromWebIdentityToken field.

Of course, a normal OIDC provider won’t sign a JWT with an XML payload in the subject field. Still, an attacker can just create their own OIDC Identity Provider (IdP), [register it](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) on an AWS account they own and sign arbitrary tokens with their own keys.

Let's put all of this together and walk through the full attack step-by-step.

1. Create a minimal OIDC IdP. This boils down to generating a RSA key pair, creating an OIDC discovery.json and key.json document and hosting the json files on a web server (see [here](https://github.com/aws/amazon-eks-pod-identity-webhook/blob/master/SELF_HOSTED_SETUP.md), for an example setup using S3).
2. Use your own AWS account to [register an OID IdP -> AWS IAM role mapping](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html). It is important to note that the AWS account used for this does not need to have any relationship with our target.
3. We can now use our OIDP to sign a JWT that contains an arbitrary GetCallerIdentityResponse as part of its subject claim. A decoded example token could look like this: iss, azp and aud match the details specified in the step 2. sub contains our spoofed response, identifying us as the AWS IAM account arn:aws:iam::superprivileged-aws-account

1. We can test if everything is setup correctly by sending a direct request to the STS AssumeRoleWithWebIdentity action using the (signed) token from step 3 and the RoleArn used in step 2:

If everything goes as planned STS will reflect the token subject as part of its JSON encoded response. As discussed above, the Go XML decoder will skip all of the content before and after the GetCallerIdentityResponse object leading Vault to consider this a valid STS CallerIdentity response.

1. The final step is to convert this request into the form expected by Vault (e.g base64 encoding all required headers, the url and an empty post body) and to send it to the target Vault server as a login request on /v1/auth/aws/login. Vault will deserialize the request, send it to STS and misinterpret the response. If the AWS ARN/UserID in our fake GetCallerIdentityResponse has privileges on the Vault server we get a valid session token back, which we can use to interact with the Vault server to fetch some secrets.

I wrote a [proof-of-concept exploit](https://bugs.chromium.org/p/project-zero/issues/attachmentText?aid=455263) that takes care of most of the busy work around JWT creation and serialization. While the OIDC provider setup adds some complexity, we end up with a nice authentication bypass for arbitrary AWS enabled roles. The only requirement is that the attacker knows the name of an privileged AWS role in the target Vault server.

What went wrong here? Looking at it from an attacker perspective, the whole authentication mechanism seems clever but error-prone. Putting HTTP request forwarding into the unauthenticated external attack surface of a security product requires strong confidence in the implementation and the underlying HTTP libraries. This becomes even more difficult as the security depends on implementation details of the Security Token Service, which might change at any point in the future. For example, AWS might decide to put STS behind a load balancing frontend, which uses the Host header for routing decisions. Without any change to the Vault codebase, this could severely degrade the security of this authentication mechanism from one moment to another.

Of course, there is a reason why the authentication works as described: AWS IAM doesn’t have a straightforward way of proving a service’s identity to other non-AWS services. Third-party services can’t easily verify pre-signed requests and AWS IAM doesn’t offer any standard signing primitives that could be used to implement certificate based authentication or JWTs.

In the end, Hashicorp fixed the vulnerability by enforcing an allowlist of HTTP headers, restricting requests to the GetCallerIdentity action and stronger validation of the STS response, which is hopefully enough to protect against unexpected changes to the STS implementation or HTTP parser differences between STS and Golang.

After finding this issue in the AWS authentication module, I decided to review its GCP equivalent. The next section describes how GCP authentication for Vault is implemented and how a simple logic flaw can lead to an authentication bypass in many configurations.

## Exploiting Vault-on-GCP

Vault supports the [gcp](https://www.vaultproject.io/docs/auth/gcp) auth method for deployments on Google Cloud. Similar to its AWS counterpart, the auth method supports two different authentication mechanisms: iam and gce. Whereas the iam mechanism supports arbitrary service accounts and can be used from services such as App Engine or Cloud Functions, gce can only be used to authenticate virtual machines running on Google Compute Engine. Still, it has some interesting advantages. Instead of only making authentication decisions based on a service account identity, gce can also grant access based on a number of [VM attributes](https://www.vaultproject.io/api/auth/gcp#gce-only-parameters). For example, a configuration could give only VMs in a specific region (europe-west-6) access to certain secrets, allow all VMs in the xyz-prod GCP project access or restrict it even further using [instance-groups](https://cloud.google.com/compute/docs/instance-groups).

Both iam and gce are built on top of JWT. A vault client that wants to

authenticate, creates a signed token to prove its identity and sends it to the vault

server to get a session token back. For the iam mechanism, the client signs the token directly

using a service account private key under their control or with the [projects.serviceAccounts.signJwt](https://cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt) IAM API method.

For gce, the client is expected to run on an authorized GCE VM. It fetches a signed token by sending a request to the [instance identity endpoint](https://cloud.google.com/compute/docs/instances/verifying-instance-identity) of the GCP metadata server. In contrast to service account tokens, this token is signed by an [official Google certificate](https://www.googleapis.com/oauth2/v1/certs). In addition to the normal JWT claims (sub, aud, iat, exp), the tokens returned from the metadata server also contains a special compute\_engine claim that lists details about the instance, which are processed as part of the auth process:

JWT has a number of design choices that make it very prone to implementation errors (see [this blog post](https://research.securitum.com/jwt-json-web-token-security/) by securitum for an overview about typical issues), so I decided to spend a day on reviewing Vault’s token processing.

The function [parseAndValidateJwt](https://github.com/hashicorp/vault-plugin-auth-gcp/blob/8450f263d8d262b6c4871ff2576373c17dbe1687/plugin/path_login.go#L145) is responsible for processing both gce and iam tokens.

It first parses the token without verifying the signature and passes the decoded token into the getSigningKey helper method:

getSigningKey extracts the key id claim (kid) out of the token header and tries to find a google-wide oAuth key with the same identifier. This will work for GCE metadata tokens, but not for tokens signed by a service account:

If this approach fails, the Vault server extracts the Subject (sub) claim from the supplied token. For valid tokens, this claim contains the email address of the signing service account. Knowing the key id and subject of the token, Vault fetches the public key used for signing using the service account GCP API:

In both cases, the Vault server now has access to a public key that can verify the signature of the JWT:

If verification succeeds, Vault fills out the loginInfo struct that is later used to grant or deny access. If the token contains a compute\_engine claim it is copied into the loginInfo.GceMetada field:

As mentioned above, all of this code is shared between the iam and gce auth methods. The issue here is that no check enforces that a token signed by an arbitrary service account doesn’t contain GCE compute\_engine claims. While the content in a GCE metadata token is trustworthy and controlled by Google, service account tokens are completely controlled by the owner of the service account and can therefore contain arbitrary claims.

If we follow the control flow of the gce method to the end we can see that Vault uses loginInfo.GceMetadata as part of its auth decision in [pathGceLogin](https://github.com/hashicorp/vault-plugin-auth-gcp/blob/8450f263d8d262b6c4871ff2576373c17dbe1687/plugin/path_login.go#L438) if two conditions are met:

- The VM described in the metadata section needs to exist. This is verified using the GCE API and requires an attacker to impersonate an actively running VM. In practice, only project\_id, zone and instance\_name are verified and need to be set to valid values.
- The service account in subject claim of the JWT token needs to exist. This is verified using the ServiceAccount GCP API which requires the iam.serviceAccounts.get permission in the project hosting the service account. As the attacker can just use a service account in their own project, it is straightforward to just grant this permission to the GCP identity Vault is running under or even allUsers.

Finally, [AuthorizeGCE](https://github.com/hashicorp/vault-plugin-auth-gcp/blob/8450f263d8d262b6c4871ff2576373c17dbe1687/plugin/authorizer_gce.go#L36) is called to grant or deny access. If the attacker impersonated

a GCE instance with the right attributes (project, label, zones..) everything works out well and

the attacker gets a valid session token back. The only auth restriction that can’t be bypassed is a hardcoded service account name, as this value will be equal to the attacker account and not the expected VM account name.

An end-to-end attack against a vulnerable configuration will look like this:

1. Create a service account in a GCP project you control and generate a private key using gcloud: gcloud iam service-accounts keys create key.json --iam-account [sa-name@project-id.iam.gserviceaccount.com](mailto:sa-name@project-id.iam.gserviceaccount.com)
2. Sign a JWT with a fake compute\_engine claim describing an existing and privileged VM. See [here](https://bugs.chromium.org/p/project-zero/issues/attachmentText?aid=456240) for a simple proof-of-concept script that takes care of most of the details.
3. Now simply use the token to sign-in to Vault: curl --request POST --data '{"role": "my-gce-role", "jwt" : "...."}' [http://vault:8200/v1/auth/gcp/login](http://vault:8200/v1/auth/gcp/login)

This is an interesting bug that requires some knowledge of GCP IAM to spot. The root cause seems to be the merging of two separate authentication flows into a single code path in the parseAndValidateJwt function, which makes it difficult to reason about all security requirements when writing or reviewing the code. At the same time, GCP makes it easy to shoot yourself in the foot by offering two types of JWT tokens with completely different security properties.

## Conclusion

This blog post describes two authentication vulnerabilities in HashiCorp Vault, a “cloud-native” software for secret management. While Vault was clearly developed with security in mind and profits from the memory safety and high quality standard library of its implementation language Go, I was still able to identify two critical vulnerabilities in its unauthenticated attack surface.

In my experience, tricky vulnerabilities like this often exist where developers have to interact with external systems and services. A strong developer might be able to reason about all security boundaries, requirements and pitfalls of their own software, but it becomes very difficult once a complex external service comes into play. Modern cloud IAM solutions are powerful and often more secure than comparable on-premise solutions, but they come with their own security pitfalls and a high implementation complexity. As more and more companies move to the big cloud providers, familiarity with these technology stacks will become a key skill for security engineers and researchers and it is safe to assume that there will be a lot of similar issues in the next few years.

Finally, both discussed vulnerabilities demonstrate how difficult it is to write secure software. Even with memory-safe languages, strong cryptography primitives, static analysis and large fuzzing infrastructure, some issues can only be discovered by manual code review and an attacker mindset.
