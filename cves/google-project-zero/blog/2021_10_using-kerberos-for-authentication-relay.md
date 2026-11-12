# Using Kerberos for Authentication Relay Attacks - Project Zero

Source: https://projectzero.google/2021/10/using-kerberos-for-authentication-relay.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Project Zero


This blog post is a summary of some research I've been doing into relaying Kerberos authentication in Windows domain environments. To keep this blog shorter I am going to assume you have a working knowledge of Windows network authentication, and specifically Kerberos and NTLM. For a quick primer on Kerberos see [this page](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/b4af186e-b2ff-43f9-b18e-eedb366abf13) which is part of Microsoft's Kerberos extension documentation or you can always read [RFC4120](https://www.rfc-editor.org/rfc/rfc4120.txt).

## Background

Windows based enterprise networks rely on network authentication protocols, such as [NT Lan Manager (NTLM)](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nlmp/b38c36ed-2804-4868-a9ff-8dd3182128e4) and Kerberos to implement single sign on. These protocols allow domain users to seamlessly connect to corporate resources without having to repeatedly enter their passwords. This works by the computer's Local Security Authority (LSA) process storing the user's credentials when the user first authenticates. The LSA can then reuse those credentials for network authentication without requiring user interaction.


However, the convenience of not prompting the user for their credentials when performing network authentication has a downside. To be most useful, common clients for network protocols such as HTTP or SMB must automatically perform the authentication without user interaction otherwise it defeats the purpose of avoiding asking the user for their credentials.


This automatic authentication can be a problem if an attacker can trick a user into connecting to a server they control. The attacker could induce the user's network client to start an authentication process and use that information to authenticate to an unrelated service allowing the attacker to access that service's resources as the user. When the authentication protocol is captured and forwarded to another system in this way it's referred to as an Authentication Relay attack.



Authentication relay attacks using the NTLM protocol were [f](https://web.archive.org/web/20030706050349/http://www.xfocus.net/articles/200305/smbrelay.html)[irst published](https://web.archive.org/web/20030706050349/http://www.xfocus.net/articles/200305/smbrelay.html) all the way back in 2001 by Josh Buchbinder (Sir Dystic) of the Cult of the Dead Cow. However, even in 2021 NTLM relay attacks still represent a threat in default configurations of Windows domain networks. The most recent major abuse of NTLM relay was through the [Active Directory Certificate Services web enrollment service](https://specterops.io/assets/resources/Certified_Pre-Owned.pdf). This combined with the [PetitPotam](https://github.com/topotam/PetitPotam) technique to induce a Domain Controller to perform NTLM authentication allows for a Windows domain to be compromised by an unauthenticated attacker.


Over the years Microsoft has made many efforts to mitigate authentication relay attacks. The best mitigations rely on the fact that the attacker does not have knowledge of the user's password or control over the authentication process. This includes signing and encryption (sealing) of network traffic using a session key which is protected by the user's password or channel binding as part of [Extended Protection for Authentication (EPA)](https://msrc-blog.microsoft.com/2009/12/08/extended-protection-for-authentication/) which prevents relay of authentication to a network protocol under TLS.


Another mitigation regularly proposed is to disable NTLM authentication either for particular services or network wide using [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-ntlm-authentication-in-this-domain). While this has potential compatibility issues, restricting authentication to only Kerberos should be more secure. That got me thinking, is disabling NTLM sufficient to eliminate authentication relay attacks on Windows domains?

## Why are there no Kerberos Relay Attacks?

The obvious question is, if NTLM is disabled could you relay Kerberos authentication instead? Searching for Kerberos Relay attacks doesn't yield much public research that I could find. There is the [krbrelayx](https://github.com/dirkjanm/krbrelayx) tool written by [Dirk-jan](https://twitter.com/_dirkjan) which is similar in concept to the [ntlmrelayx](https://github.com/SecureAuthCorp/impacket/tree/master/impacket/examples/ntlmrelayx) tool in [impacket](https://github.com/SecureAuthCorp/impacket), a common tool for performing NTLM authentication relay attacks. However as the accompanying [blog post](https://dirkjanm.io/krbrelayx-unconstrained-delegation-abuse-toolkit/) makes clear this is a tool to abuse [unconstrained delegation](https://docs.microsoft.com/en-us/defender-for-identity/cas-isp-unconstrained-kerberos) rather than relay the authentication.


I did find a [recent presentation](https://media.defcon.org/DEF%20CON%2029/DEF%20CON%2029%20presentations/Sagi%20Sheinfeld%20Eyal%20Karni%20Yaron%20Zinar%20-%20Using%20Machine-in-the-Middle%20to%20Attack%20Active%20Directory%20Authentication%20Schemes.pdf) by Sagi Sheinfeld, [Eyal Karni](https://twitter.com/eyal_karni), [Yaron Zinar](https://twitter.com/YaronZi) from Crowdstrike at Defcon 29 (and also coming up at Blackhat EU 2021) which relayed Kerberos authentication. The presentation discussed MitM network traffic to specific servers, then relaying the Kerberos authentication. A MitM attack relies on being able to spoof an existing server through some mechanism, which is a well known risk.  The last line in the presentation is "Microsoft Recommendation: Avoid being MITM’d…" which seems a reasonable approach to take if possible.


However a MitM attack is slightly different to the common NTLM relay attack scenario where you can induce a domain joined system to authenticate to a server an attacker controls and then forward that authentication to an unrelated service. NTLM is easy to relay as it wasn't designed to distinguish authentication to a particular service from any other. The only unique aspect was the server (and later client) challenge but that value wasn't specific to the service and so authentication for say SMB could be forwarded to HTTP and the victim service couldn't tell the difference. Subsequently EPA has been retrofitted onto NTLM to make the authentication specific to a service, but due to backwards compatibility these mitigations aren't always used.


On the other hand Kerberos has always required the target of the authentication to be specified beforehand through a principal name, typically this is a [Service Principal Name (SPN)](https://docs.microsoft.com/en-us/windows/win32/ad/service-principal-names) although in certain circumstances it can be a User Principal Name (UPN). The SPN is usually represented as a string of the form CLASS/INSTANCE:PORT/NAME, where CLASS is the class of service, such as HTTP or CIFS, INSTANCE is typically the DNS name of the server hosting the service and PORT and NAME are optional.


The SPN is used by the Kerberos Ticket Granting Server (TGS) to select the shared encryption key for a Kerberos service ticket generated for the authentication. This ticket contains the details of the authenticating user based on the contents of the Ticket Granting Ticket (TGT) that was requested during the user's initial Kerberos authentication process. The client can then package the service's ticket into an Authentication Protocol Request (AP\_REQ) authentication token to send to the server.


Without knowledge of the shared encryption key the Kerberos service ticket can't be decrypted by the service and the authentication fails. Therefore if Kerberos authentication is attempted to an SMB service with the SPN CIFS/fileserver.domain.com, then that ticket shouldn't be usable if the relay target is a HTTP service with the SPN HTTP/fileserver.domain.com, as the shared key should be different.


In practice that's rarely the case in Windows domain networks. The Domain Controller associates the SPN with a user account, most commonly the computer account of the domain joined server and the key is derived from the account's password. The CIFS/fileserver.domain.com and HTTP/fileserver.domain.com SPNs would likely be assigned to the FILESERVER$ computer account, therefore the shared encryption key will be the same for both SPNs and in theory the authentication could be relayed from one service to the other. The receiving service could query for the authenticated SPN string from the authentication APIs and then compare it to its expected value, but this check is typically optional.


The selection of the SPN to use for the Kerberos authentication is typically defined by the target server's host name. In a relay attack the attacker's server will not be the same as the target. For example, the SMB connection might be targeting the attacker's server, and will assign the SPN CIFS/evil.com. Assuming this SPN is even registered it would in all probability have a different shared encryption key to the CIFS/fileserver.domain.com SPN due to the different computer accounts. Therefore relaying the authentication to the target SMB service will fail as the ticket can't be decrypted.


The requirement that the SPN is associated with the target service's shared encryption key is why I assume few consider Kerberos relay attacks to be a major risk, if not impossible. There's an assumption that an attacker cannot induce a client into generating a service ticket for an SPN which differs from the host the client is connecting to.


However, there's nothing inherently stopping Kerberos authentication being relayed if the attacker can control the SPN. The only way to stop relayed Kerberos authentication is for the service to protect itself through the use of signing/sealing or channel binding which rely on the shared knowledge between the client and server, but crucially not the attacker relaying the authentication. However, even now these service protections aren't the default even on critical protocols such as LDAP.


As the only limit on basic Kerberos relay (in the absence of service protections) is the selection of the SPN, this research focuses on how common protocols select the SPN and whether it can be influenced by the attacker to achieve Kerberos authentication relay.

## Kerberos Relay Requirements

It's easy to demonstrate in a controlled environment that Kerberos relay is possible. We can write a simple client which uses the [Security Support Provider Interface (SSPI)](https://en.wikipedia.org/wiki/Security_Support_Provider_Interface) APIs to communicate with the LSA and implement the network authentication. This client calls the [InitializeSecurityContext](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-initializesecuritycontextw) API which will generate an AP\_REQ authentication token containing a Kerberos Service Ticket for an arbitrary SPN. This AP\_REQ can be forwarded to an intermediate server and then relayed to the service the SPN represents. You'll find this will work, again to reiterate, assuming that no service protections are in place.


However, there are some caveats in the way a client calls InitializeSecurityContext which will impact how useful the generated AP\_REQ is even if the attacker can influence the SPN. If the client specifies any one of the following request flags, ISC\_REQ\_CONFIDENTIALITY, ISC\_REQ\_INTEGRITY, ISC\_REQ\_REPLAY\_DETECT or ISC\_REQ\_SEQUENCE\_DETECT then the generated AP\_REQ will enable encryption and/or integrity checking. When the AP\_REQ is received by the server using the [AcceptSecurityContext](https://docs.microsoft.com/en-us/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) API it will return a set of flags which indicate if the client enabled encryption or integrity checking. Some services use these [returned flags](https://docs.microsoft.com/en-us/windows/win32/secauthn/context-requirements) to opportunistically enable service protections.


For example LDAP's default setting is to enable signing/encryption if the client supports it. Therefore you shouldn't be able to relay Kerberos authentication to LDAP if the client enabled any of these protections. However, other services such as HTTP don't typically support signing and sealing and so will happily accept authentication tokens which specify the request flags.


Another caveat is the client could specify channel binding information, typically derived from the certificate used by the TLS channel used in the communication. The channel binding information can be controlled by the attacker, but not set to arbitrary values without a bug in the TLS implementation or the code which determines the channel binding information itself.


While services have an option to only enable channel binding if it's supported by the client, all Windows Kerberos AP\_REQ tokens indicate support through the [KERB\_AP\_OPTIONS\_CBT](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/b15648e2-439a-4d04-b8a2-2f34c45690f9) options flag in the authenticator. Sagi Sheinfeld et al did demonstrate (see slide 22 in [their presentation](https://media.defcon.org/DEF%20CON%2029/DEF%20CON%2029%20presentations/Sagi%20Sheinfeld%20Eyal%20Karni%20Yaron%20Zinar%20-%20Using%20Machine-in-the-Middle%20to%20Attack%20Active%20Directory%20Authentication%20Schemes.pdf)) that if you can get the AP\_REQ from a non-Windows source it will not set the options flag and so no channel binding is enforced, but that was apparently not something Microsoft will fix. It is also possible that a Windows client disables channel binding through a [registry configuration option](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/authentication-fails-non-windows-ntlm-kerberos-server), although that seems to be unlikely in real world networks.


If the client specifies the ISC\_REQ\_MUTUAL\_AUTH request flag when generating the initial AP\_REQ it will enable mutual authentication between the client and server. The client expects to receive an Authentication Protocol Response (AP\_REP) token from the server after sending the AP\_REQ to prove it has possession of the shared encryption key. If the server doesn't return a valid AP\_REP the client can assume it's a spoofed server and refuse to continue the communication.


From a relay perspective, mutual authentication doesn't really matter as the server is the target of the relay attack, not the client. The target server will assume the authentication has completed once it's accepted the AP\_REQ, so that's all the attacker needs to forward. While the server will generate the AP\_REP and return it to the attacker they can just drop it unless they need the relayed client to continue to participate in the communication for some reason.


One final consideration is that the SSPI APIs have two security packages which can be used to implement Kerberos authentication, Negotiate and Kerberos. The Negotiate protocol wraps the AP\_REQ (and other authentication tokens) in the [SPNEGO protocol](https://datatracker.ietf.org/doc/html/rfc4178) whereas Kerberos sends the authentication tokens using a simple GSS-API wrapper (see [RFC4121](https://datatracker.ietf.org/doc/html/rfc4121)).


The first potential issue is Negotiate is by far the most likely package in use as it allows a network protocol the flexibility to use the most appropriate authentication protocol that the client and server both support. However, what happens if the client uses the raw Kerberos package but the server uses Negotiate?


This isn't a problem as the server implementation of Negotiate will pass the input token to the function NegpDetermineTokenPackage in lsasrv.dll during the first call to AcceptSecurityContext. This function detects if the client has passed a GSS-API Kerberos token (or NTLM) and enables a pass through mode where Negotiate gets out of the way. Therefore even if the client uses the Kerberos package you can still authenticate to the server and keep the client happy without having to extract the inner authentication token or wrap up response tokens.


One actual issue for relaying is the Negotiate protocol enables integrity protection (equivalent to passing ISC\_REQ\_INTEGRITY to the underlying package) so that it can generate a Message Integrity Code (MIC) for the authentication exchange to prevent tampering. Using the Kerberos package directly won't add integrity protection automatically. Therefore relaying Kerberos AP\_REQs from Negotiate will likely hit issues related to automatic enabling of signing on the server. It is possible for a client to explicitly disable automatic integrity checking by passing the ISC\_REQ\_NO\_INTEGRITY request attribute, but that's not a common case.


It's possible to disable Negotiate from the relay if the client passes an arbitrary authentication token to the first call of the InitializeSecurityContext API. On the first call the Negotiate implementation will call the NegpDetermineTokenPackage function to determine whether to enable authentication pass through. If the initial token is NTLM or looks like a Kerberos token then it'll pass through directly to the underlying security package and it won't set ISC\_REQ\_INTEGRITY, unless the client explicitly requested it. The byte sequence \[0x00, 0x01, 0x40\] is sufficient to get Negotiate to detect Kerberos, and the token is then discarded so it doesn't have to contain any further valid data.

## Sniffing and Proxying Traffic

Before going into individual protocols that I've researched, it's worth discussing some more obvious ways of getting access to Kerberos authentication targeted at other services. First is sniffing network traffic sent from client to the server. For example, if the Kerberos AP\_REQ is sent to a service over an unencrypted network protocol and the attacker can view that traffic the AP\_REQ could be extracted and relayed. The selection of the SPN will be based on the expected traffic so the attacker doesn't need to do anything to influence it.


The Kerberos authentication protocol has protections against this attack vector. The Kerberos AP\_REQ doesn't just contain the service ticket, it's also accompanied by an Authenticator which is encrypted using the ticket's session key. This key is accessible by both the legitimate client and the service. The authenticator contains a timestamp of when it was generated, and the service can check if this authenticator is within an allowable time range and whether it has seen the timestamp already. This allows the service to reject replayed authenticators by caching recently received values, and the allowable time window prevents the attacker waiting for any cache to expire before replaying.


What this means is that while an attacker could sniff the Kerberos authentication on the wire and relay it, if the service has already received the authenticator it would be rejected as being a replay. The only way to exploit it would be to somehow prevent the legitimate authentication request from reaching the service, or race the request so that the attacker's packet is processed first.


Note, [RFC4120](https://datatracker.ietf.org/doc/html/rfc4120#section-3.2.3) mentions the possibility of embedding the client's network address in the authenticator so that the service could reject authentication coming from the wrong host. This isn't used by the Windows Kerberos implementation as far as I can tell. No doubt it would cause too many false positives for the replay protection in anything but the simplest enterprise networks.


Therefore the only reliable way to exploit this scenario would be to actively interpose on the network communications between the client and service. This is of course practical and has been demonstrated many times assuming the traffic isn't protected using something like TLS with server verification. Various attacks would be possible such as ARP or DNS spoofing attacks or HTTP proxy redirection to perform the interposition of the traffic.


However, active MitM of protocols is a known risk and therefore an enterprise might have technical defenses in place to mitigate the issue. Of course, if such enterprises have enabled all the recommended relay protections,it's a moot point. Regardless, we'll assume that MitM is impractical for existing services due to protections in place and consider how individual protocols handle SPN selection.

## IPSec and AuthIP

My research into Kerberos authentication relay came about in part because I was looking into the implementation of IPSec on Windows as part of my firewall research. Specifically I was researching the [AuthIP ISAKMP](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-aips/eee3de64-3847-4451-978e-9513ff187d30) which allows for Windows authentication protocols to be used to establish IPsec Security Associations.


I noticed that the AuthIP protocol has a [GSS-ID payload](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-aips/9ab1ccc0-d92e-4ca4-bae9-1c93871399ac) which can be sent from the server to the client. This payload contains the textual SPN to use for the Kerberos authentication during the AuthIP process. This SPN is passed verbatim to the SSPI InitializeSecurityContext call by the AuthIP client.


As no verification is done on the format of the SPN in the GSS-ID payload, it allows the attacker to fully control the values including the service class and instance name. Therefore if an attacker can induce a domain joined machine to connect to an attacker controlled service and negotiate AuthIP then a Kerberos AP\_REQ for an arbitrary SPN can be captured for relay use. As this AP\_REQ is never sent to the target of the SPN it will not be detected as a replay.


Inducing authentication isn't necessarily difficult. Any IP traffic which is covered by the domain [configured security connection rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/configure-the-rules-to-require-encryption) will attempt to perform AuthIP. For example it's possible that a UDP response for a DNS request from the domain controller might be sufficient. AuthIP supports two authenticated users, the machine and the calling user. By default it seems the machine authenticates first, so if you convinced a Domain Controller to authenticate you'd get the DC computer account which could be fairly exploitable.


For interest's sake, the SPN is also used to determine the computer account associated with the server. This computer account is then used with [Service For User (S4U)](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-sfu/3bff5864-8135-400e-bdd9-33b552051d94) to generate a local access token allowing the client to determine the identity of the server. However I don't think this is that useful as the fake server can't complete the authentication and the connection will be discarded.


The security connection rules use IP address ranges to determine what hosts need IPsec authentication. If these address ranges are too broad it's also possible that ISAKMP AuthIP traffic might leak to external networks. For example if the rules don't limit the network ranges to the enterprise's addresses, then even a connection out to a public service could be accompanied by the ISAKMP AuthIP packet. This can be then exploited by an attacker who is not co-located on the enterprise network just by getting a client to connect to their server, such as through a web URL.



To summarize the attack process from the diagram:

1. Induce a client computer to send some network traffic to EVILHOST. It doesn't really matter what the traffic is, only that the IP address, type and port must match an IP security connection rule to use AuthIP. EVILHOST does not need to be domain joined to perform the attack.
2. The network traffic will get the Windows IPsec client to try and establish a security association with the target host.
3. A fake AuthIP server on the target host receives the request to establish a security association and returns a GSS-ID payload. This payload contains the target SPN, for example CIFS/FILESERVER.
4. The IPsec client uses the SPN to create an AP\_REQ token and sends it to EVILHOST.
5. EVILHOST relays the Kerberos AP\_REQ to the target service on FILESERVER.


Relaying this AuthIP authentication isn't ideal from an attacker's perspective. As the authentication will be used to sign and seal the network traffic, the request context flags for the call to InitializeSecurityContext will require integrity and confidentiality protection. For network protocols such as LDAP which default to requiring signing and sealing if the client supports it, this would prevent the relay attack from working. However if the service ignores the protection and doesn't have any further checks in place this would be sufficient.


This issue was [reported to MSRC](https://bugs.chromium.org/p/project-zero/issues/detail?id=2213) and assigned case number 66900. However Microsoft have indicated that it will not be fixed with a security bulletin. I've described Microsoft's rationale for not fixing this issue later in the blog post. If you want to reproduce this issue there's details on Project Zero's [issue tracker](https://bugs.chromium.org/p/project-zero/issues/detail?id=2213).

## MSRPC

After discovering that AuthIP could allow for authentication relay the next protocol I looked at is [MSRPC](https://docs.microsoft.com/en-us/windows/win32/rpc/rpc-start-page). The protocol supports NTLM, Kerberos or Negotiate authentication protocols over connected network transports such as named pipes or TCP. These authentication protocols need to be opted into by the server using the [RpcServerRegisterAuthInfo](https://docs.microsoft.com/en-us/windows/win32/api/rpcdce/nf-rpcdce-rpcserverregisterauthinfo) API by specifying the authentication service constants of RPC\_C\_AUTHN\_WINNT, RPC\_C\_AUTHN\_GSS\_KERBEROS or RPC\_C\_AUTHN\_GSS\_NEGOTIATE respectively. When registering the authentication information the server can optionally specify the SPN that needs to be used by the client.


However, this SPN isn't actually used by the RPC server itself. Instead it's registered with the runtime, and a client can query the server's SPN using the [RpcMgmtInqServerPrincName](https://docs.microsoft.com/en-us/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtinqserverprincname) management API. Once the SPN is queried the client can configure its authentication for the connection using the [RpcBindingSetAuthInfo](https://docs.microsoft.com/en-us/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfo) API. However, this isn't required; the client could just generate the SPN manually and set it. If the client doesn't call RpcBindingSetAuthInfo then it will not perform any authentication on the RPC connection.


Aside, curiously when a connection is made to the server it can query the client's authentication information using the [RpcBindingInqAuthClient](https://docs.microsoft.com/en-us/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthclient) API. However, the SPN that this API returns is the one registered by RpcServerRegisterAuthInfo and NOT the one which was used by the client to authenticate. Also Microsoft does mention the call to RpcMgmtInqServerPrincName in the "[Writing a secure RPC client or server](https://docs.microsoft.com/en-us/windows/win32/rpc/choosing-security-qos-options)" section on MSDN. However they frame it in the context of mutual authentication and not to protect against a relay attack.


If a client queries for the SPN from a malicious RPC server it will authenticate using a Kerberos AP\_REQ for an SPN fully under the attacker's control. Whether the AP\_REQ has integrity or confidentiality enabled depends on the authentication level set during the call to RpcBindingSetAuthInfo. If this is set to RPC\_C\_AUTHN\_LEVEL\_CONNECT and the client uses RPC\_C\_AUTHN\_GSS\_KERBEROS then the AP\_REQ won't have integrity enabled. However, if Negotiate is used or anything above RPC\_C\_AUTHN\_LEVEL\_CONNECT as a level is used then it will have the integrity/confidentiality flags set.


Doing a quick scan in system32 the following DLLs call the RpcMgmtInqServerPrincName API: certcli.dll, dot3api.dll, dusmsvc.dll, FrameServerClient.dll, L2SecHC.dll, luiapi.dll, msdtcprx.dll, nlaapi.dll, ntfrsapi.dll, w32time.dll, WcnApi.dll, WcnEapAuthProxy.dll, WcnEapPeerProxy.dll, witnesswmiv2provider.dll, wlanapi.dll, wlanext.exe, WLanHC.dll, wlanmsm.dll, wlansvc.dll, wwansvc.dll, wwapi.dll. Some basic analysis shows that none of these clients check the value of the SPN and use it verbatim with RpcBindingSetAuthInfo. That said, they all seem to use RPC\_C\_AUTHN\_GSS\_NEGOTIATE and set the authentication level to RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY which makes them less useful as an attack vector.


If the client specifies RPC\_C\_AUTHN\_GSS\_NEGOTIATE but does not specify an SPN then the runtime generates one automatically. This is based on the target hostname with the RestrictedKrbHost service class. The runtime doesn't process the hostname, it just concatenates strings and for some reason the runtime doesn't support generating the SPN for RPC\_C\_AUTHN\_GSS\_KERBEROS.


One additional quirk of the RPC runtime is that the request attribute flag ISC\_REQ\_USE\_DCE\_STYLE is used when calling InitializeSecurityContext. This enables a [special three-leg authentication mode](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-kile/190ab8de-dc42-49cf-bf1b-ea5705b7a087) which results in the server sending back an AP\_RET and then receiving another AP\_RET from the client. Until that third AP\_RET has been provided to the server it won't consider the authentication complete so it's not sufficient to just forward the initial AP\_REQ token and close the connection to the client. This just makes the relay code slightly more complex but not impossible.


A second change that ISC\_REQ\_USE\_DCE\_STYLE introduces is that the Kerberos AP\_REQ token does not have an GSS-API wrapper. This causes the call to NegpDetermineTokenPackage to fail to detect the package in use, making it impossible to directly forward the traffic to a server using the Negotiate package. However, this prefix is not protected against modification so the relay code can append the appropriate value before forwarding to the server. For example the following C# code can be used to convert a DCE style AP\_REQ to a GSS-API format which Negotiate will accept.

| public static byte\[\] EncodeLength(int length) { if (length \< 0x80) return new byte\[\] { (byte)length }; if (length \< 0x100) return new byte\[\] { 0x81, (byte)length }; if (length \< 0x10000) return new byte\[\] { 0x82, (byte)(length >> 8), (byte)(length & 0xFF) }; throw new ArgumentException("Invalid length", nameof(length)); } public static byte\[\] ConvertApReq(byte\[\] token) { if (token.Length == 0 \|\| token\[0\] != 0x6E) return token; MemoryStream stm = new MemoryStream(); BinaryWriter writer = new BinaryWriter(stm); Console.WriteLine("Converting DCE AP\_REQ to GSS-API format."); byte\[\] header = new byte\[\] { 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x12, 0x01, 0x02, 0x02, 0x01, 0x00 }; writer.Write((byte)0x60); writer.Write(EncodeLength(header.Length + token.Length)); writer.Write(header); writer.Write(token); return stm.ToArray(); } | 


Subsequent tokens in the authentication process don't need to be wrapped; in fact, wrapping them with their GSS-API headers will cause the authentication to fail. Relaying MSRPC requests would probably be difficult just due to the relative lack of clients which request the server's SPN. Also when the SPN is requested it tends to be a conscious act of securing the client and so best practice tends to require the developer to set the maximum authentication level, making the Kerberos AP\_REQ less useful.

## DCOM

The DCOM protocol uses MSRPC under the hood to access remote COM objects, therefore it should have the same behavior as MSRPC. The big difference is DCOM is designed to automatically handle the authentication requirements of a remote COM object through binding information contained in the [DUALSTRINGARRAY](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dcom/7fe8200b-dccd-48cf-a2fa-681e3e0a23f4) returned during Object Exporter ID (OXID) resolving. Therefore the client doesn't need to explicitly call RpcBindingSetAuthInfo to configure the authentication.


The binding information contains the protocol sequence and endpoint to use (such as TCP on port 30000) as well as the security bindings. Each security binding contains the RPC authentication service (wAuthnSvc in the below screenshot) to use as well as an optional SPN (aPrincName) for the authentication. Therefore a malicious DCOM server can force the client to use the RPC\_C\_AUTHN\_GSS\_KERBEROS authentication service with a completely arbitrary SPN by returning an appropriate security binding.



The authentication level chosen by the client depends on the value of the dwAuthnLevel parameter specified if the COM client calls the [CoInitializeSecurity](https://docs.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) API. If the client doesn't explicitly call CoInitializeSecurity then a default will be used which is currently RPC\_C\_AUTHN\_LEVEL\_CONNECT. This means neither integrity or confidentiality will be enforced on the Kerberos AP\_REQ by default.


One limitation is that without a call to CoInitializeSecurity, the default impersonation level for the client is set to RPC\_C\_IMP\_LEVEL\_IDENTIFY. This means the access token generated by the DCOM RPC authentication can only be used for identification and not for impersonation. For some services this isn't an issue, for example LDAP doesn't need an impersonation level token. However for others such as SMB this would prevent access to files. It's possible that you could find a COM client which sets both RPC\_C\_AUTHN\_LEVEL\_CONNECT and RPC\_C\_IMP\_LEVEL\_IMPERSONATE though there's no trivial process to assess that.


Getting a client to connect to the server isn't trivial as DCOM isn't a widely used protocol on modern Windows networks due to high authentication requirements. However, one use case for this is local privilege escalation. For example you could get a privileged service to connect to the malicious COM server and relay the computer account Kerberos AP\_REQ which is generated. I have a working PoC for this which allows a local non-admin user to connect to the domain's LDAP server using the local computer's credentials.


This attack is somewhat similar to the [RemotePotato](https://github.com/antonioCoco/RemotePotato0) attack (which uses NTLM rather than Kerberos) which again Microsoft have refused to fix. I'll describe this in more detail in a separate blog post after this one.

## HTTP

HTTP has supported NTLM and Negotiate authentication for a long time (see [this draft](https://datatracker.ietf.org/doc/html/draft-brezak-spnego-http-04) from 2002 although the most recent RFC is [4559](https://datatracker.ietf.org/doc/html/rfc4559) from 2006). To initiate a Windows authentication session the server can respond to a request with the status code 401 and specify a WWW-Authenticate header with the value Negotiate. If the client supports Windows authentication it can use InitializeSecurityContext to generate a token, convert the binary token into a Base64 string and send it in the next request to the server with the Authorization header. This process is repeated until the client errors or the authentication succeeds.


In theory only NTLM and Negotiate are defined but a HTTP implementation could use other Windows authentication packages such as Kerberos if it so chose to. Whether the HTTP client will automatically use the user's credentials is up to the user agent or the developer using it as a library.


All the major browsers support both authentication types as well as many non browser HTTP user agents such as those in .NET and WinHTTP. I looked at the following implementations, all running on Windows 10 21H1:

- WinINET (Internet Explorer 11)
- WinHTTP (WebClient)
- Chromium M93 (Chrome and Edge)
- Firefox 91
- .NET Framework 4.8
- .NET 5.0 and 6.0


This is of course not an exhaustive list, and there's likely to be many different HTTP clients in Windows which might have different behaviors. I've also not looked at how non-Windows clients work in this regard.


There's two important behaviors that I wanted to assess with HTTP. First is how the user agent determines when to perform automatic Windows authentication using the current user's credentials. In order to relay the authentication it can't ask the user for their credentials. And second we want to know how the SPN is selected by the user agent when calling InitializeSecurityContext.

### WinINET (Internet Explorer 11)

[WinINET](https://docs.microsoft.com/en-us/windows/win32/wininet/portal) can be used as a generic library to handle HTTP connections and authentication. There's likely many different users of WinINET but we'll just look at Internet Explorer 11 as that is what it's most known for. WinINET is also the originator of HTTP Negotiate authentication, so it's good to get a baseline of what WinINET does in case other libraries just copied its behavior.


First, how does WinINET determine when it should handle Windows authentication automatically? By default this is based on whether the target host is considered to be in the Intranet Zone. This means any host which bypasses the configured HTTP proxy or uses an undotted name will be considered Intranet zone and WinINET will automatically authenticate using the current user's credentials.


It's possible to disable this behavior by changing the security options for the Intranet Zone to "Prompt for user name and password", as shown below:



Next, how does WinINET determine the SPN to use for Negotiate authentication? RFC4559 says the following:


'When the Kerberos Version 5 GSSAPI mechanism \[RFC4121\] is being used, the HTTP server will be using a principal name of the form of "HTTP/hostname"'


You might assume therefore that the HTTP URL that WinINET is connecting to would be sufficient to build the SPN: just use the hostname as provided and combine with the HTTP service class. However it turns out that's not entirely the case. I found a rough description of how IE and WinINET actually generate the SPN in [this blog](https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/internet-explorer-behaviors-with-kerberos-authentication/ba-p/396428). This blog post is over 10 years old so it was possible that things have changed, however it turns out to not be the case.


The basic approach is that WinINET doesn't necessarily trust the hostname specified in the HTTP URL. Instead it requests the canonical name of the server via DNS. It doesn't seem to explicitly request a CNAME record from the DNS server. Instead it calls [getaddrinfo](https://docs.microsoft.com/en-us/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfo) and specifies the AI\_CANONNAME hint. Then it uses the returned value of ai\_canonname and prefixes it with the HTTP service class. In general ai\_canonname is the name provided by the DNS server in the returned A/AAAA record.


For example, if the HTTP URL is http://fileserver.domain.com, but the DNS A record contains the canonical name example.domain.com the generated SPN is HTTP/example.domain.com and not HTTP/fileserver.domain.com. Therefore to provide an arbitrary SPN you need to get the name in the DNS address record to differ from the IP address in that record so that IE will connect to a server we control while generating Kerberos authentication for a different target name.


The most obvious technique would be to specify a DNS CNAME record which redirects to another hostname. However, at least if the client is using a Microsoft DNS server (which is likely for a domain environment) then the CNAME record is not directly returned to the client. Instead the DNS server will perform a recursive lookup, and then return the CNAME along with the validated address record to the client.


Therefore, if an attacker sets up a CNAME record for www.evil.com, which redirects to fileserver.domain.com the DNS server will return the CNAME record and an address record for the real IP address of fileserver.domain.com. WinINET will try to connect to the HTTP service on fileserver.domain.com rather than www.evil.com which is what is needed for the attack to function.


I tried various ways of tricking the DNS client into making a direct request to a DNS server I controlled but I couldn't seem to get it to work. However, it turns out there is a way to get the DNS resolver to accept arbitrary DNS responses, via local DNS resolution protocols such as [Multicast DNS (MDNS)](https://datatracker.ietf.org/doc/html/rfc6762) and [Link-Local Multicast Name Resolution (LLMNR)](https://datatracker.ietf.org/doc/html/rfc4795).


These two protocols use a lightly modified DNS packet structure, so you can return a response to the name resolution request with an address record with the IP address of the malicious web server, but the canonical name of any server. WinINET will then make the HTTP connection to the malicious web server but construct the SPN for the spoofed canonical name. I've verified this with LLMNR and in theory MDNS should work as well.


Is spoofing the canonical name a bug in the Windows DNS client resolver? I don't believe any DNS protocol requires the query name to exactly match the answer name. If the DNS server has a CNAME record for the queried host then there's no obvious requirement for it to return that record when it could just return the address record. Of course if a public DNS server could spoof a host for a DNS zone which it didn't control, that'd be a [serious security issue](https://www.cs.cornell.edu/~shmat/shmat_securecomm10.pdf). It's also worth noting that this doesn't spoof the name generally. As the cached DNS entry on Windows is based on the query name, if the client now resolves fileserver.domain.com a new DNS request will be made and the DNS server would return the real address.


Attacking local name resolution protocols is a well known weakness abused for MitM attacks, so it's likely that some security conscious networks will disable the protocols. However, the advantage of using LLMNR this way over its use for MitM is that the resolved name can be anything. As in, normally you'd want to spoof the DNS name of an existing host, in our example you'd spoof the request for the fileserver name. But for registered computers on the network the DNS client will usually satisfy the name resolution via the network's DNS server before ever trying local DNS resolution. Therefore local DNS resolution would never be triggered and it wouldn't be possible to spoof it. For relaying Kerberos authentication we don't care, you can induce a client to connect to an unregistered host name which will fallback to local DNS resolution.


The big problem with the local DNS resolution attack vector is that the attacker must be in the same multicast domain as the victim computer. However, the attacker can still start the process by getting a user to connect to an external domain which looks legitimate then redirect to an undotted name to both force automatic authentication and local DNS resolving.



To summarize the attack process as shown in the above diagram:

1. The attacker sets up an LLMNR service on a machine in the same multicast domain at the victim computer. The attacker listens for a target name request such as EVILHOST.
2. Trick the victim to use IE (or another WinINET client, such as via a document format like DOCX) to connect to the attacker's server on http://EVILHOST.
3. The LLMNR server receives the lookup request and responds by setting the address record's hostname to the SPN target host to spoof and the IP address to the attacker-controlled server.
4. The WinINET client extracts the spoofed canonical name, appends the HTTP service class to the SPN and requests the Kerberos service ticket. This Kerberos ticket is then sent to the attacker's HTTP service.
5. The attacker receives the Negotiate/Kerberos authentication for the spoofed SPN and relays it to the real target server.


An example LLMNR response decoded by Wireshark for the name evilhost (with IP address 10.0.0.80), spoofing fileserver.domain.com (which is not address 10.0.0.80) is shown below:

| Link-local Multicast Name Resolution (response) Transaction ID: 0x910f Flags: 0x8000 Standard query response, No error Questions: 1 Answer RRs: 1 Authority RRs: 0 Additional RRs: 0 Queries evilhost: type A, class IN Name: evilhost \[Name Length: 8\] \[Label Count: 1\] Type: A (Host Address) (1) Class: IN (0x0001) Answers fileserver.domain.com: type A, class IN, addr 10.0.0.80 Name: fileserver.domain.com Type: A (Host Address) (1) Class: IN (0x0001) Time to live: 1 (1 second) Data length: 4 Address: 10.0.0.80 | 


You might assume that the SPN always having the HTTP service class would be a problem. However, the Active Directory default SPN mapping will map HTTP to the HOST service class which is always registered. Therefore you can target any domain joined system without needing to register an explicit SPN. As long as the receiving service doesn't then verify the SPN it will work to authenticate to the computer account, which is used by privileged services. You can use the following PowerShell script to list all the configured SPN mappings in a domain.

| PS> $base\_dn = (Get-ADRootDSE).configurationNamingContext PS> $dn = "CN=Directory Service,CN=Windows NT,CN=Services,$base\_dn" PS> (Get-ADObject $dn -Properties sPNMappings).sPNMappings | 


One interesting behavior of WinINET is that it always requests Kerberos delegation, although that will only be useful if the SPN's target account is registered for delegation. I couldn't convince WinINET to default to a Kerberos only mode; sending back a WWW-Authenticate: Kerberos header causes the authentication process to stop. This means the Kerberos AP\_REQ will always have Integrity enabled even though the user agent doesn't explicitly request it.


Another user of WinINET is Office. For example you can set a template located on an HTTP URL which will generate local Windows authentication if in the Intranet zone just by opening a Word document. This is probably a good vector for getting the authentication started rather than relying on Internet Explorer being available.


WinINET does have some [feature controls](<https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537164(v=vs.85)>) which can be enabled on a per-executable basis which affect the behavior of the SPN lookup process, specifically FEATURE\_USE\_CNAME\_FOR\_SPN\_KB911149 and

FEATURE\_ALWAYS\_USE\_DNS\_FOR\_SPN\_KB3022771. However these only seem to come into play if the HTTP connection is being proxied, which we're assuming isn't the case.

### WinHTTP (WebDAV WebClient)

The [WinHTTP library](https://docs.microsoft.com/en-us/windows/win32/winhttp/about-winhttp) is an alternative to using WinINET in a client application. It's a cleaner API and doesn't have the baggage of being used in Internet Explorer. As an example client I chose to use the built-in WebDAV WebClient service because it gives the interesting property that it converts a UNC file name request into a potentially exploitable HTTP request. If the WebClient service is installed and running then opening a file of the form \\EVIL\abc will cause an HTTP request to be sent out to a server under the attacker's control.


From what I can tell the behavior of WinHTTP when used with the WebClient service is almost exactly the same as for WinINET. I could exploit the SPN generation through local DNS resolution, but not from a public DNS name record. WebDAV seems to consider undotted names to be Intranet zone, however the default for WinHTTP seems to depend on whether the connection would bypass the proxy. The automatic authentication decision is based on the value of the WINHTTP\_OPTION\_AUTOLOGON\_POLICY policy.


At least as used with WebDAV WinHTTP handles a WWW-Authenticate header of Kerberos, however it ends up using the Negotiate package regardless and so Integrity will always be enabled. It also enables Kerberos delegation automatically like WinINET.

### Chromium M93

Chromium based browsers such as Chrome and Edge are open source so it's a bit easier to check the implementation. By default Chromium will automatically authenticate to intranet zone sites, it uses the same Internet Security Manager used by WinINET to make the zone determination in [URLSecurityManagerWin::CanUseDefaultCredentials](https://source.chromium.org/chromium/chromium/src/+/main:net/http/url_security_manager_win.cc;drc=739ccc21289257112c667e04a40d9a5a2db466bf;l=50). An administrator can set GPOs to change this behavior to only allow automatic authentication to a set of hosts.


The SPN is generated in [HttpAuthHandlerNegotiate::CreateSPN](https://source.chromium.org/chromium/chromium/src/+/main:net/http/http_auth_handler_negotiate.cc;drc=78c0778431c6fdd3dead532b1774270486829251;l=248) which is called from [HttpAuthHandlerNegotiate::DoResolveCanonicalNameComplete](https://source.chromium.org/chromium/chromium/src/+/main:net/http/http_auth_handler_negotiate.cc;drc=a412d0ef42cd54ca75e76023a8ccf13d6f58bf06;l=356). While the documentation for CreateSPN mentions it's basically a copy of the behavior in IE, it technically isn't. Instead of taking the canonical name from the initial DNS request it does a second DNS request, and the result of that is used to generate the SPN.


This second DNS request is important as it means that we now have a way of exploiting this from a public DNS name. If you set the TTL of the initial host DNS record to a very low value, then it's possible to change the DNS response between the lookup for the host to connect to and the lookup for the canonical name to use for the SPN.


This will also work with local DNS resolution as well, though in that case the response doesn't need to be switched as one response is sufficient. This second DNS lookup behavior can be disabled with a [GPO](https://admx.help/?Category=Chrome&Policy=Google.Policies.Chrome::DisableAuthNegotiateCnameLookup). If this is disabled then neither local DNS resolution nor public DNS will work as Chromium will use the host specified in the URL for the SPN.


In a domain environment where the Chromium browser is configured to only authenticate to Intranet sites we can abuse the fact that by default authenticated users can add new DNS records to the Microsoft DNS server through LDAP (see [this blog post](https://www.netspi.com/blog/technical/network-penetration-testing/exploiting-adidns/) by [Kevin Robertson](https://twitter.com/kevin_robertson)). Using the domain's DNS server is useful as the DNS record could be looked up using a short Intranet name rather than a public DNS name meaning it's likely to be considered a target for automatic authentication.


One problem with using LDAP to add the DNS record is the time before the DNS server will refresh its records is at least 180 seconds. This would make it difficult to switch the response from a normal address record to a CNAME record in a short enough time frame to be useful. Instead we can add an NS record to the DNS server which forwards the lookup to our own DNS server. As long as the TTL for the DNS response is short the domain's DNS server will rerequest the record and we can return different responses without any waiting for the DNS server to update from LDAP. This is very similar to [DNS rebinding attack](https://en.wikipedia.org/wiki/DNS_rebinding), except instead of swapping the IP address, we're swapping the canonical name.



Therefore a working exploit as shown in the diagram would be the following:

1. Register an NS record with the DNS server for evilhost.domain.com using existing authenticated credentials via LDAP. Wait for the DNS server to pick up the record.
2. Direct the browser to connect to http://evilhost. This allows Chromium to automatically authenticate as it's an undotted Intranet host. The browser will lookup evilhost.domain.com by adding its primary DNS suffix.
3. This request goes to the client's DNS server, which then follows the NS record and performs a recursive query to the attacker's DNS server.
4. The attacker's DNS server returns a normal address record for their HTTP server with a very short TTL.
5. The browser makes a request to the HTTP server, at this point the attacker delays the response long enough for the cached DNS request to expire. It can then return a 401 to get the browser to authenticate.
6. The browser makes a second DNS lookup for the canonical name. As the original request has expired, another will be made for evilhost.domain.com. For this lookup the attacker returns a CNAME record for the fileserver.domain.com target. The client's DNS server will look up the IP address for the CNAME host and return that.
7. The browser will generate the SPN based on the CNAME record and that'll be used to generate the AP\_REQ, sending it to the attacker's HTTP server.
8. The attacker can relay the AP\_REQ to the target server.


It's possible that we can combine the local and public DNS attack mechanisms to only need one DNS request. In this case we could set up an NS record to our own DNS server and get the client to resolve the hostname. The client's DNS server would do a recursive query, and at this point our DNS server shouldn't respond immediately. We could then start a classic DNS spoofing attack to return a DNS response packet directly to the client with the spoofed address record.


In general DNS spoofing is limited by requiring the source IP address, transaction ID and the UDP source port to match before the DNS client will accept the response packet. The source IP address should be spoofable on a local network and the client's IP address can be known ahead of time through an initial HTTP connection, so the only problems are the transaction ID and port.


As most clients have a relatively long timeout of 3-5 seconds, that might be enough time to try the majority of the combinations for the ID and port. Of course there isn't really a penalty for trying multiple times. If this attack was practical then you could do the attack on a local network even if local DNS resolution was disabled and enable the attack for libraries which only do a single lookup such as WinINET and WinHTTP. The response could have a long TTL, so that when the access is successful it doesn't need to be repeated for every request.


I couldn't get Chromium to downgrade Negotiate to Kerberos only so Integrity will be enabled. Also since Delegation is not enabled by default, an administrator needs to configure an [allow list GPO](https://admx.help/?Category=Chrome&Policy=Google.Policies.Chrome::AuthNegotiateDelegateWhitelist) to specify what targets are allowed to receive delegated credentials.


A bonus quirk for Chromium: It seems to be the only browser which still supports URL based user credentials. If you pass user credentials in the request and get the server to return a request for Negotiate authentication then it'll authenticate automatically regardless of the zone of the site. You can also pass credentials using XMLHttpRequest::open.


While not very practical, this can be used to test a user's password from an arbitrary host. If the username/password is correct and the SPN is spoofed then Chromium will send a validated Kerberos AP\_REQ, otherwise either NTLM or no authentication will be sent.


NTLM can be always generated as it doesn't require any proof the password is valid, whereas Kerberos requires the password to be correct to allow the authentication to succeed. You need to specify the domain name when authenticating so you use a URL of the form http://DOMAIN%5CUSER:PASSWORD@host.com.


One other quirk of this is you can specify a fully qualified domain name (FQDN) and user name and the Windows Kerberos implementation will try and authenticate using that server based on the DNS SRV records. For example http://EVIL.COM%5CUSER:PASSWORD@host.com will try to authenticate to the Kerberos service specified through the \_kerberos.\_tcp.evil.com SRV record. This trick works even on non-domain joined systems to generate Kerberos authentication, however it's not clear if this trick has any practical use.


It's worth noting that I did discuss the implications of the Chromium HTTP vector with team members internally and the general conclusion that this behavior is by design as it's trying to copy the behavior expected of existing user agents such as IE. Therefore there was no expectation it would be fixed.

### Firefox 91

As with Chromium, Firefox is open source so we can find the [implementation](https://searchfox.org/mozilla-central/source/extensions/auth/nsHttpNegotiateAuth.cpp#170). Unlike the other HTTP implementations researched up to this point, Firefox doesn't perform Windows authentication by default. An administrator needs to configure either a list of hosts that are allowed to automatically authenticate, or the network.negotiate-auth.allow-non-fqdn setting can be enabled to authenticate to non-dotted host names.


If authentication is enabled it works with both local DNS resolving and public DNS as it does a second DNS lookup when constructing the SPN for Negotiate in [nsAuthSSPI::MakeSN](https://searchfox.org/mozilla-central/source/extensions/auth/nsAuthSSPI.cpp#93). Unlike Chromium there doesn't seem to be a setting to disable this behavior.


Once again I couldn't get Firefox to use raw Kerberos, so Integrity is enabled. Also Delegation is not enabled unless an administrator configures the network.negotiate-auth.delegation-uris setting.

### .NET Framework 4.8

The .NET Framework 4.8 officially has two HTTP libraries, the original [System.Net.HttpWebRequest](https://docs.microsoft.com/en-us/dotnet/api/system.net.webrequest) and derived APIs and the newer [System.Net.Http.HttpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) API. However in the .NET framework the newer API uses the older one under the hood, so we'll only consider the older of the two.


Windows authentication is only generated automatically if the [UseDefaultCredentials](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest.usedefaultcredentials) property is set to true on the HttpWebRequest object as shown below (technically this sets the [CredentialCache.DefaultCredentials](https://docs.microsoft.com/en-us/dotnet/api/system.net.credentialcache.defaultcredentials) object, but it's easier to use the boolean property). Once the default credentials are set the client will automatically authenticate using Windows authentication to any host, it doesn't seem to care if that host is in the Intranet zone.

| var request = WebRequest.CreateHttp("http://www.evil.com"); request.UseDefaultCredentials = true; var response = (HttpWebResponse)request.GetResponse(); | 


The SPN is generated in the [System.Net.AuthenticationState.GetComputeSpn](https://referencesource.microsoft.com/#System/net/System/Net/_AuthenticationState.cs,114) function which we can find in the .NET reference source. The SPN is built from the canonical name returned by the initial DNS lookup, which means it supports the local but not public DNS resolution. If you follow the code it does support doing a second DNS lookup if the host is undotted, however this is only if the client code sets an explicit Host header as far as I can tell. Note that the code here is slightly different in .NET 2.0 which might support looking up the canonical name as long as the host name is undotted, but I've not verified that.


The .NET Framework supports specifying Kerberos directly as the authentication type in the WWW-Authentication header. As the client code doesn't explicitly request integrity, this allows the Kerberos AP\_REQ to not have Integrity enabled.


The code also supports the WWW-Authentication header having an initial token, so even if Kerberos wasn't directly supported, you could use Negotiate and specify the stub token I described at the start to force Kerberos authentication. For example returning the following header with the initial 401 status response will force Kerberos through auto-detection:

| WWW-Authenticate: Negotiate AAFA | 


Finally, the authentication code always enables delegation regardless of the target host.

### .NET 5.0

The .NET 5.0 runtime has deprecated the HttpWebRequest API in favor of the HttpClient API. It uses a new backend class called the [SocketsHttpHandler](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.socketshttphandler). As it's all open source we can find the [implementation](https://github.com/dotnet/runtime/blob/791a0d896052f61161aff4c1ccb5f3425328f9a8/src/libraries/System.Net.Http/src/System/Net/Http/SocketsHttpHandler/AuthenticationHelper.NtAuth.cs), specifically the AuthenticationHelper class which is a complete rewrite from the .NET Framework version.


To automatically authenticate, the client code must either use the HttpClientHandler class and set the UseDefaultCredentials property as shown below. Or if using SocketsHttpHandler, set the Credentials property to the default credentials. This handler must then be specified when creating the HttpClient object.

| var handler = new HttpClientHandler(); handler.UseDefaultCredentials = true; var client = new HttpClient(handler); await client.GetStringAsync("http://www.evil.com"); | 


Unless the client specified an explicit Host header in the request the authentication will do a DNS lookup for the canonical name. This is separate from the DNS lookup for the HTTP connection so it supports both local and public DNS attacks.


While the implementation doesn't support Kerberos directly like the .NET Framework, it does support passing an initial token so it's still possible to force raw Kerberos which will disable the Integrity requirement.

### .NET 6.0

The .NET 6.0 runtime is basically the same as .NET 5.0, except that Integrity is specified explicitly when creating the client authentication context. This means that rolling back to Kerberos no longer has any advantage. [This change](https://github.com/dotnet/runtime/commit/17481fef502ee6aed6f9e8fc76e45bb5863c68b5) seems to be down to a broken implementation of NTLM on macOS and not as some anti-NTLM relay measure.

### HTTP Overview

The following table summarizes the results of the HTTP protocol research:

- The LLMNR column indicates it's possible to influence the SPN using a local DNS resolver attack
- DNS CNAME indicates a public DNS resolving attack
- Delegation indicates the HTTP user agent enables Kerberos delegation
- Integrity indicates that integrity protection is requested which reduces the usefulness of the relayed authentication if the target server automatically detects the setting.

| User Agent | LLMNR | DNS CNAME | Delegation | Integrity | 
| Internet Explorer 11 (WinINET) | Yes | No | Yes | Yes | 
| WebDAV (WinHTTP) | Yes | No | Yes | Yes | 
| Chromium (M93) | Yes | Yes | No† | Yes | 
| Firefox 91 | Yes | Yes | No† | Yes | 
| .NET Framework 4.8 | Yes | No‡ | Yes | No | 
| .NET 5.0 | Yes | Yes | No | No | 
| .NET 6.0 | Yes | Yes | No | Yes | 


† Chromium and Firefox can enable delegation only on a per-site basis through a GPO.

‡ .NET Framework supports DNS resolving in special circumstances for non-dotted hostnames.


By far the most permissive client is .NET 5.0. It supports authenticating to any host as long as it has been configured to authenticate automatically. It also supports arbitrary SPN spoofing from a public DNS name as well as disabling integrity through Kerberos fallback. However, as .NET 5.0 is designed to be something usable cross platform, it's possible that few libraries written with it in mind will ever enable automatic authentication.

## LDAP

Windows has a built-in general purpose LDAP library in [wldap32.dll](https://docs.microsoft.com/en-us/windows/win32/api/_ldap/). This is used by the majority of OS components when accessing Active Directory and is also used by the .NET [LdapConnection](https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.protocols.ldapconnection) class. There doesn't seem to be a way of specifying the SPN manually for the LDAP connection using the API. Instead it's built manually based on the canonical name based on the DNS lookup. Therefore it's exploitable in a similar manner to WinINET via local DNS resolution.


The name of the LDAP server can also be found by querying for a SRV record for the hostname. This is used to support accessing the LDAP server from the top-level Windows domain name. This will usually return an address record alongside, all this does is change the server resolution process which doesn't seem to give any advantages to exploitation.


Whether the LDAP client enables integrity checking is based on the value of the LDAP\_OPT\_SIGN flag. As the connection only supports Negotiate authentication the client passes the ISC\_REQ\_NO\_INTEGRITY flag if signing is disabled so that the server won't accidentally auto-detect the signing capability enabled for the Negotiate MIC and accidentally enable signing protection.


As part of [recent changes](https://support.microsoft.com/en-us/topic/2020-ldap-channel-binding-and-ldap-signing-requirements-for-windows-ef185fb8-00f7-167d-744c-f299a66fc00a) to LDAP signing the client is forced to enable Integrity by the [LdapClientIntegrity policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-ldap-client-signing-requirements). This means that regardless of whether the LDAP server needs integrity protection it'll be enabled on the client which in turn will automatically enable it on the server. Changing the value of LDAP\_OPT\_SIGN in the client has no effect once this policy is enabled.

## SMB

SMB is one of the most commonly exploited protocols for NTLM relay, as it's easy to convert access to a file into authentication. It would be convenient if it was also exploitable for Kerberos relay. While SMBv1 is deprecated and not even installed on newer installs of Windows, it's still worth looking at the implementation of v1 and v2 to determine if either are exploitable.


The client implementations of SMB 1 and 2 are in mrxsmb10.sys and mrxsmb20.sys respectively with some common code in mrxsmb.sys. Both protocols support specifying a name for the SPN which is related to DFS. The SPN name needs to be specified through the GUID\_ECP\_DOMAIN\_SERVICE\_NAME\_CONTEXT ECP and is only enabled if the NETWORK\_OPEN\_ECP\_OUT\_FLAG\_RET\_MUTUAL\_AUTH flag in the GUID\_ECP\_NETWORK\_OPEN\_CONTEXT ECP (set by MUP) is specified. This is related to UNC hardening which was added to protect things like group policies.


It's easy enough to trigger the conditions to set the NETWORK\_OPEN\_ECP\_OUT\_FLAG\_RET\_MUTUAL\_AUTH flag. The default UNC hardening rules always add SYSVOL and NETLOGON UNC paths with a wildcard hostname. Therefore a request to \\evil.com\SYSVOL will cause the flag to be set and the SPN potentially overridable. The server should be a DFS server for this to work, however even with the flag set I've not found a way of setting an arbitrary SPN value remotely.


Even if you could spoof the SPN, the SMB clients always enable Integrity protection. Like LDAP, SMB will enable signing and encryption opportunistically if available from the client, unless UNC hardening measures are in place.

## Marshaled Target Information SPN

While investigating the SMB implementation I noticed something interesting. The SMB clients use the function [SecMakeSPNEx2](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-secmakespnex2) to build the SPN value from the service class and name. You might assume this would just return the SPN as-is, however that's not the case. Instead for the hostname of fileserver with the service class cifs you get back an SPN which looks like the following:

| cifs/fileserver1UWhRCAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAfileserversBAAAA | 


Looking at the implementation of SecMakeSPNEx2 it makes a call to the API function [CredMarshalTargetInfo](https://docs.microsoft.com/en-us/windows/win32/api/ntsecpkg/nf-ntsecpkg-credmarshaltargetinfo). This API takes a list of target information in a [CREDENTIAL\_TARGET\_INFORMATION](https://docs.microsoft.com/en-us/windows/win32/api/wincred/ns-wincred-credential_target_informationw) structure and marshals it using a base64 string encoding. This marshaled string is then appended to the end of the real SPN.


The code is therefore just appending some additional target information to the end of the SPN, presumably so it's easier to pass around. My initial assumption would be this information is stripped off before passing to the SSPI APIs by the SMB client. However, passing this SPN value to InitializeSecurityContext as the target name succeeds and gets a Kerberos service ticket for cifs/fileserver. How does that work?


Inside the function SspiExProcessSecurityContext in lsasrv.dll, which is the main entrypoint of InitializeSecurityContext, there's a call to the CredUnmarshalTargetInfo API, which parses the marshaled target information. However SspiExProcessSecurityContext doesn't care about the unmarshalled results, instead it just gets the length of the marshaled data and removes that from the end of the target SPN string. Therefore before the Kerberos package gets the target name it has already been restored to the original SPN.


The encoded SPN shown earlier, minus the service class, is a valid DNS component name and therefore could be used as the hostname in a public or local DNS resolution request. This is interesting as this potentially gives a way of spoofing a hostname which is distinct from the real target service, but when processed by the SSPI API requests the spoofed service ticket. As in if you use the string fileserver1UWhRCAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAfileserversBAAAA as the DNS name, and if the client appends a service class to the name and passes it to SSPI it will get a service ticket for fileserver, however the DNS resolving can trivially return an unrelated IP address.


There are some big limitations to abusing this behavior. The marshaled target information must be valid, the last 6 characters is an encoded length of the entire marshaled buffer and the buffer is prefixed with a 28 byte header with a magic value of 0x91856535 in the first 4 bytes. If this length is invalid (e.g. larger than the buffer or not a multiple of 2) or the magic isn't present then the CredUnmarshalTargetInfo call fails and SspiExProcessSecurityContext leaves the SPN as is which will subsequently fail to query a Kerberos ticket for the SPN.


The easiest way that the name could be invalid is by it being converted to lowercase. DNS is case insensitive, however generally the servers are case preserving. Therefore you could lookup the case sensitive name and the DNS server would return that unmodified. However the HTTP clients tested all seem to lowercase the hostname before use, therefore by the time it's used to build an SPN it's now a different string. When unmarshalling 'a' and 'A' represent different binary values and so parsing of the marshaled information will fail.


Another issue is that the size limit of a single name in DNS is 63 characters. The minimum valid marshaled buffer is 44 characters long leaving only 19 characters for the SPN part. This is at least larger than the minimum NetBIOS name limit of 15 characters so as long as there's an SPN for that shorter name registered it should be sufficient. However if there's no short SPN name registered then it's going to be more difficult to exploit.


In theory you could specify the SPN using its FQDN. However it's hard to construct such a name. The length value must be at the end of the string and needs to be a valid marshaled value so you can't have any dots within its 6 characters. It's possible to have a TLD which is 6 characters or longer and as the embedded marshaled values are not escaped this can be used to construct a valid FQDN which would then resolve to another SPN target. For example:

| fileserver1UWhRCAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA.domain.oBAAAA | 


is a valid DNS name which would resolve to an SPN for fileserver. Except that oBAAAA is not a valid public TLD. Pulling the list of [valid TLDs](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) from ICANN's website and converting all values which are 6 characters or longer into the expected length value, the smallest length which is a multiple of 2 is from WEBCAM which results in a DNS name at least 264331 characters long, which is somewhat above the 255 character limit usually considered valid for a FQDN in DNS.


Therefore this would still be limited to more local attacks and only for limited sets of protocols. For example an authenticated user could register a DNS entry for the local domain using this value and trick an RPC client to connect to it using its undotted hostname. As long as the client doesn't modify the name other than putting the service class on it (or it gets automatically generated by the RPC runtime) then this spoofs the SPN for the request.

## Microsoft's Response to the Research

I didn't initially start looking at Kerberos authentication relay, as mentioned I found it inadvertently when looking at IPsec and AuthIP which I subsequently reported to Microsoft. After doing more research into other network protocols I decided to use the AuthIP issue as a bellwether on Microsoft's views on whether relaying Kerberos authentication and spoofing SPNs would cross a security boundary.


As I mentioned earlier the AuthIP issue was classed as "vNext", which denotes it might be fixed in a future version of Windows, but not as a security update for any currently shipping version of Windows. This was because Microsoft determined it to be a Moderate severity issue (see [this](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2A3xt) for the explanation of the severities). Only Important or above will be serviced.


It seems that the general rule is that any network protocol where the SPN can be spoofed to generate Kerberos authentication which can be relayed, is not sufficient to meet the severity level for a fix. However, any network facing service which can be used to induce authentication where the attacker does not have existing network authentication credentials is considered an Important severity spoofing issue and will be fixed. This is why PetitPotam was fixed as [CVE-2021-36942](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-36942), as it could be exploited from an unauthenticated user.


As my research focused entirely on the network protocols themselves and not the ways of inducing authentication, they will all be covered under the same Moderate severity. This means that if they were to be fixed at all, it'd be in unspecified future versions of Windows.

## Available Mitigations

How can you defend yourself against authentication relay attacks presented in this blog post? While I think I've made the case that it's possible to relay Kerberos authentication, it's somewhat more limited in scope than NTLM relay. This means that disabling NTLM is still an invaluable option for mitigating authentication relay issues on a Windows enterprise network.


Also, except for disabling NTLM, all the mitigations for NTLM relay apply to Kerberos relay. Requiring signing or sealing on the protocol if possible is sufficient to prevent the majority of attack vectors, especially on important network services such as LDAP.


For TLS encapsulated protocols, channel binding prevents the authentication being relayed as I didn't find any way of spoofing the TLS certificate at the same time. If the network service supports EPA, such as HTTPS or LDAPS it should be enabled. Even if the protocol doesn't support EPA, enabling TLS protection if possible is still valuable. This not only provides more robust server authentication, which Kerberos mutual authentication doesn't really provide, it'll also hide Kerberos authentication tokens from sniffing or MitM attacks.


Some libraries, such as WinHTTP and .NET set the undocumented ISC\_REQ\_UNVERIFIED\_TARGET\_NAME request attribute when calling InitializeSecurityContext in certain circumstances. This affects the behavior of the server when querying for the SPN used during authentication. Some servers such as SMB and IIS with EPA can be configured to validate the SPN. If this request attribute flag is set then while the authentication will succeed when the server goes to check the SPN, it gets an empty string which will not match the server's expectations. If you're a developer you should use this flag if the SPN has been provided from an untrustworthy source, although this will only be beneficial if the server is checking the received SPN.


A common thread through the research is abusing local DNS resolution to spoof the SPN. Disabling LLMNR and MDNS should always be best practice, and this just highlights the dangers of leaving them enabled. While it might be possible to perform the same attacks through DNS spoofing attacks, these are likely to be much less reliable than local DNS spoofing attacks.


If Windows authentication isn't needed from a network client, it'd be wise to disable it if supported. For example, some HTTP user agents support disabling automatic Windows authentication entirely, while others such as Firefox don't enable it by default. Chromium also supports disabling the DNS lookup process for generating the SPN through group policy.


Finally, blocking untrusted devices on the network such as through 802.1X or requiring authenticated IPsec/IKEv2 for all network communications to high value services would go some way to limiting the impact of all authentication relay attacks. Although of course, an attacker could still compromise a trusted host and use that to mount the attack.

## Conclusions

I hope that this blog post has demonstrated that Kerberos relay attacks are feasible and just disabling NTLM is not a sufficient mitigation strategy in an enterprise environment. While DNS is a common thread and is the root cause of the majority of these protocol issues, it's still possible to spoof SPNs using other protocols such as AuthIP and MSRPC without needing to play DNS tricks.


While I wrote my own tooling to perform the LLMNR attack there are various public tools which can mount an LLMNR and MDNS spoofing attack such as the venerable [Python Responder](https://github.com/SpiderLabs/Responder). It shouldn't be hard to modify one of the tools to verify my findings.


I've also not investigated every possible network protocol which might perform Kerberos authentication. I've also not looked at non-Windows systems which might support Kerberos such as Linux and macOS. It's possible that in more heterogeneous networks the impact might be more pronounced as some of the security changes in Microsoft's Kerberos implementation might not be present.


If you're doing your own research into this area, you should look at how the SPN is specified by the protocol, but also how the implementation builds it. For example the HTTP Negotiate RFC states how to build the SPN for Kerberos, but then each implementation does it slightly differently and not to the RFC specification.


You should be especially wary of any protocol where an untrusted server can specify an arbitrary SPN. This is the case in AuthIP, MSRPC and DCOM. It's almost certain that when these protocols were originally designed many years ago, that no thought was given to the possible abuse of this design for relaying the Kerberos network authentication.
