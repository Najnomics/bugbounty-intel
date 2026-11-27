# Introducing Goctopus

- **Source URL:** https://medium.com/@tristan.kalos/introducing-goctopus-open-source-graphql-endpoint-discovery-tool-written-in-go-bb7f5c228fdf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142716/https://medium.com/@tristan.kalos/introducing-goctopus-open-source-graphql-endpoint-discovery-tool-written-in-go-bb7f5c228fdf
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3571 (id 3571)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Introducing Goctopus: Open-Source GraphQL endpoint discovery tool written in go

In the fast-evolving domain of APIs, GraphQL has emerged as a powerful, data-oriented language. As its adoption soars, so does the need for robust tools to discover and fingerprint these APIs. Enter Goctopus, a Golang-based solution we developed at Escape to provide comprehensive, fast, and interoperable endpoint discovery and fingerprinting for GraphQL APIs. Engineered to overcome the limitations of existing tools, Goctopus extends its arms into realms of subdomain enumeration, route brute-force, authentication detection, schema introspection, and more, all while maintaining optimum speed and resource management. In this article, we dive into why we created Goctopus, what it does, and how it’s pushing the boundaries of API security.

*TL;DR: We built an open-source GraphQL endpoint discovery & fingerprinting tool: check out Goctopus on Github. This article is best read on Escape’s blog.*

## Unmasking APIs: The Importance of API Discovery & Fingerprinting

In the expansive realm of APIs, two practices stand out in their ability to shed light on the intricacies of your online presence: API Discovery and Fingerprinting.

API Discovery is the process of finding all the APIs an organization has in its ecosystem. The aim here is to unveil the totality of the digital surface that can be interacted with. In the era of microservices and distributed systems, discovering all your API endpoints is crucial for both maintaining service interoperability and ensuring security.

API Fingerprinting, on the other hand, takes this a step further. Once the endpoints are discovered, they’re scanned to find specific information about them: technologies used, configuration, authentication details…

Endpoint discovery & fingerprinting are crucial tools in offensive and defensive security to:

1. **Detecting Attack Surface**: By understanding what endpoints exist and how they operate, you get an accurate view of your potential attack surface. This gives you the upper hand in securing your system, as you can preemptively locate and address vulnerabilities.
2. **Internet-wide Research**: If you’re a security researcher or an organization keen on understanding the landscape of what’s exposed on the internet, fingerprinting can give you a macro view. It helps to gather data about technologies, configurations, and security practices being used across various domains.
3. **Classifying endpoints**: Being able to determine which technologies and configurations are used on APIs is usually the first step in any security process (offensive or defensive).

For REST APIs there are lots of tools to perform those tasks. However, for GraphQL this is not the same story, as you will see in the next paragraph.

## Identifying the Void: Why We Needed Goctopus

We built [Graphinder](https://github.com/Escape-Technologies/graphinder?ref=escape.tech) a while ago to discover GraphQL endpoints, and it’s been serving us well for a few years. However, when we decided to implement our [API Catalog](https://escape.tech/blog/graphql-api-catalog/), we needed a more robust, faster, all-in-one, and more interoperable solution.

Graphinder had some shortcomings that were hard to ignore. It was slow, hard to use programmatically, often missed inputs, lacked options, and its Python basis wasn’t our preferred choice for this specific task. Moreover, we found ourselves needing a tool that could offer more comprehensive and efficient discovery and fingerprinting capabilities:

- Broad and efficient discovery capabilities: Subdomain enumeration, brute-force, script analysis.
- Precise, fast and complete fingerprinting of GraphQL APIs: Technology, authentication, schema, field suggestion attack.
- Easy to use and enjoyable CLI.
- Complete Package for programmatic usage.
- Service interoperability: communicate with external services via webhooks.
- Portability: run easily anywhere at any scale.
- Versatile inputs: take a variety of inputs, domains, URLs, and IP addresses.
- Speed: scan thousands of domains in minutes.
- Scale: run on larger machines or scale horizontally.
- Network resources: send a minimum amount of necessary requests and maximize throughput.

So, with those constraints in mind, we realized we needed a solution that could go beyond what was already there. A more holistic tool. A faster tool. A…well, better tool. We needed Goctopus.

## Unleashing the Beast: Meet Goctopus

Born out of the needs above, Goctopus is our answer to the comprehensive, fast, and interoperable tool we need. Created with [Golang](https://go.dev/?ref=escape.tech) for its superior speed and efficiency in networking, this octopus has its arms reaching everywhere. Let’s dive into its various facets:

**Discovery**:

- **Subdomain Enumeration**: Goctopus uses DNS records APIs via [subfinder](https://github.com/projectdiscovery/subfinder?ref=escape.tech) to enumerate subdomains.
- **Bruteforce**: We built a custom list of popular GraphQL routes so that Goctopus has the best odds of finding endpoints on every domain it tests.
- **Script Analysis (Work-In-Progress)**: With this in the pipeline, Goctopus will soon be able to sniff out hidden GraphQL endpoints from Javascript & HTML files across the web.

**Fingerprinting**:

- **Authentication**: It quickly identifies which endpoints require authentication and which are publicly exposed.
- **GraphQL Schema/Introspection**: Goctopus checks if the schema is available or not.
- **Field Suggestions for Bruteforcing**: If the schema is unavailable, this clever cephalopod can even figure out if the schema can be brute-forced using field suggestions attacks.
- **Engine Fingerprinting (Work-In-Progress)**: Once this feature is added, Goctopus will be capable of understanding the tech stack behind an endpoint.

**Dx & usage**:

- **CLI**: Goctopus is easily usable as a CLI for manual operations.
- **Go package**: It can be used as a Golang package programmatically to integrate into other tools.
- **Webhook**: With this feature, Goctopus can forward its results via a webhook so that other services can retrieve them.
- **Variety of inputs**: The tool accepts a wide variety of inputs: domains, URLs, and IP addresses.

**Performance**:

- **Speed**: Designed for speed, Goctopus can scan thousands of domains in minutes.
- **Scale**: This tool has no fear of the deep; it’s built to scale on larger machines or spread horizontally across a cluster.
- **Network resources**: Goctopus is mindful of its requests, only sending what’s necessary.
- **Rate limiting**: It also ensures not sending too many requests to a single endpoint concurrently to avoid rate limiting.

In a nutshell, Goctopus is what we envisioned when we realized the limitations of existing tools. It’s comprehensive, fast, flexible, and extensible.

## Quick Hands-On: Meet Goctopus

Interested in trying out Goctopus? Here’s how to get started.

**Installation**: You have two options here. If Go is installed on your machine, just run `go install -v github.com/Escape-Technologies/goctopus/cmd/goctopus@latest` in your terminal. Prefer Docker? No problem, use `docker run --rm -it escapetech/goctopus:latest <options>` to run the latest version of Goctopus in a docker container.

**Usage Example**: Once installed, take Goctopus for a spin with this simple command `goctopus -a example.com`. This will start the discovery process on the specified domain with all features enabled (\`-a\` flag stands for "all").

For instance, running Goctopus on `rickandmortyapi.com` will result in the following:

`goctopus -a rickandmortyapi.com``````
                    .-'   `'.
                   /         \
                   |         ;
                   |         |           ___.--,
          _.._     |0) ~ (0) |    _.---'`__.-( (_.
   __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
  ( ,.--'`   ',__ /./;   ;, '.__.'`    __
  _`) )  .---.__.' / |   |\   \__..--""  """--.,_
 `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
       | |  .' _.-' |  |  \  \  '.               `~---`
        \ \/ .'     \  \   '. '-._)
         \/ /        \  \    `=.__`~-.
     jgs / /\         `) )    / / `"".`\
   , _.-'.'\ \        / /    ( (     / /
    `--~`   ) )    .-'.'      '.'.  | (
           (/`    ( (`          ) )  '-;
            `      '-;         (-'
                  _
  __ _  ___   ___| |_ ___  _ __  _   _ ___
 / _` |/ _ \ / __| __/ _ \| '_ \| | | / __|
| (_| | (_) | (__| || (_) | |_) | |_| \__ \
 \__, |\___/ \___|\__\___/| .__/ \__,_|___/ v0.0.14
 |___/                    |_|
[INF] Enumerating subdomains for 'rickandmortyapi.com'
[INF] Found 5 subdomains for 'rickandmortyapi.com' in 15 seconds 276 milliseconds
INFO[0016] Done fingerprinting rickandmortyapi.com
INFO[0016] Found: {"authenticated":false,"domain":"rickandmortyapi.com","schema_status":"OPEN","source":"rickandmortyapi.com","url":"https://rickandmortyapi.com/graphql"}
INFO[0016] Done. Found 1 graphql endpoints
`````
Visit our [GitHub repo](https://github.com/Escape-Technologies/goctopus?ref=escape.tech) for detailed documentation and the latest release notes.

## The Future of Goctopus: Contributing and Roadmap

We’re actively looking for ways to enhance Goctopus, and we welcome contributions. Feel free to raise issues or PRs on our [GitHub repo](https://github.com/Escape-Technologies/goctopus?ref=escape.tech). We’re excited to see where the community can take this project.

Looking ahead, we’ve got big plans. Improved subdomain enumeration, more intelligent endpoint discovery, engine fingerprinting — the roadmap for Goctopus is packed with exciting updates.

## Goctopus at Escape: Providing Top-Notch Security for Our Users

Here at Escape, we’re using Goctopus to provide enhanced security for our users.

**API Catalog**: We’re using Goctopus to provide users with detailed information about their attack surface. By continuously scanning for new APIs and updating our records, we can ensure an up-to-date vision and alert our users whenever they expose an unprotected API.

**Suggestions**: Goctopus is also integrated into our application creation process to automatically suggest our user’s endpoints to secure to make our platform as smooth to use as possible.

**Kraken**: We built an internal tool around Goctopus called Kraken to scale Goctopus to another level. It consists of an API, a database, and dozens of Goctopus instances managed by a Kubernetes cluster that [allowed us to scan](https://escape.tech/resources/state-of-graphql-security-2023/?utm_source=blog_goctopus) millions of domains to gather data on +150k GraphQL endpoints. Stay tuned for an upcoming article on the topic!

We invite you to join us in exploring what Goctopus can do. Try it out, contribute, and together, let’s push the boundaries of API security! And don’t forget to star the [Goctopus repo](https://github.com/YourOrganization/goctopus?ref=escape.tech) on GitHub.

Need a complete and automated security solution for your GraphQL APIs? You can easily try Escape by [signing up to a free account](https://app.escape.tech/register/?ref=escape.tech) to test your endpoints before committing.
