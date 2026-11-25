# I Owned the S3 Buckets Behind 79 Million NASA Satellite Files

- **Source URL:** https://obaskly.medium.com/i-owned-the-s3-buckets-behind-79-million-nasa-satellite-files-1d22fb0a0629
- **Fetched from:** https://obaskly.medium.com/i-owned-the-s3-buckets-behind-79-million-nasa-satellite-files-1d22fb0a0629?source=rss-5638f1c49663------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14960 (id 14960)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Obaskly / Tue, 27 Oct 2026 05:52:03 GMT

NASA’s own catalog pointed scientists at two buckets nobody owned, so I registered them.

Here’s a curl command and what it returned:

$ curl -L https://asf-cumulus-prod-opera-product.s3.amazonaws.com/poc.txt


NASA VDP PoC by obaskly - Bugcrowd

That bucket name appears in NASA’s official data catalog. It’s where NASA tells researchers to fetch OPERA satellite data, about 79.5 million files’ worth. But that bucket was in my AWS account.

**WHERE IT STARTED**

I’d already spent a while on NASA’s Common Metadata Repository (CMR), the search backend for Earthdata. (I found an RCE and a Zip Slip in it, and wrote both up separately.) This time I wasn’t looking at the code. I was looking at what CMR returns.

Every cloud-hosted collection in CMR has a block called DirectDistributionInformation. It tells tools which S3 bucket the data lives in:

GET https://cmr.earthdata.nasa.gov/search/collections.umm\_json?concept\_id=C3294057315-ASF

"DirectDistributionInformation": {

"Region": "us-west-2",

"S3BucketAndObjectPrefixNames": \[

"asf-cumulus-prod-opera-product/OPERA\_L3\_DISP-S1/"

\],

"S3CredentialsAPIEndpoint": "https://cumulus.asf.alaska.edu/s3credentials"

}

S3 bucket names are global. If a bucket gets deleted, or was never created, anyone can register that name. So I pulled every collection from ASF (Alaska Satellite Facility, one of NASA’s data centers) and checked each bucket in that field.

**Two of them came back as NoSuchBucket:**

**TAKING THEM**

There isn’t much to it. I created both buckets in my own AWS account in us-west-2 and uploaded a poc.txt to each:

$ curl -L https://asf-cumulus-prod-browse.s3.amazonaws.com/poc.txt

NASA VDP PoC by obaskly - Bugcrowd

$ curl -L https://asf-cumulus-prod-opera-product.s3.amazonaws.com/poc.txt

NASA VDP PoC by obaskly - Bugcrowd

Both returned 200 from AmazonS3.

**HOW BIG WAS IT**

This is the part that turned a “bucket takeover” into something serious. I counted how many collections and granules (individual data files) referenced each bucket. CMR returns the count in a CMR-Hits header, so you can ask for page\_size=0 and get the number back instantly:

r = requests.get(

"https://cmr.earthdata.nasa.gov/search/granules.json",

params={"collection\_concept\_id": concept\_id, "page\_size": 0},

)

hits = int(r.headers.get("CMR-Hits", 0))

The affected data covered ARIA Sentinel-1 interferograms and the OPERA products: surface displacement, radar backscatter, tropospheric corrections and so on. People use this data for earthquake and landslide monitoring, disaster response and climate research.

**WHO ACTUALLY READS THIS FIELD**

A bucket name sitting in metadata is only dangerous if something follows it. So I checked earthaccess, NASA’s official Python library for Earthdata. In earthaccess/results.py:

def s3\_bucket(self) -> Dict\[str, Any\]:

return self\["umm"\].get("DirectDistributionInformation", {})

That’s the exact field I’d taken over. The usual cloud workflow is: look up the collection in CMR, read the bucket name, get temporary credentials from the S3CredentialsAPIEndpoint, then download from the bucket. That last step would land in my bucket, and since the name matches what NASA’s metadata says, nobody would notice.

To show the chain end to end, my PoC read the bucket names live from CMR and then fetched from them, the same way a tool would:

Collection : C3294057315-ASF - OPERA\_L3\_DISP-S1\_V1

CMR bucket : \['asf-cumulus-prod-opera-product/OPERA\_L3\_DISP-S1/'\]

→ https://asf-cumulus-prod-opera-product.s3.amazonaws.com/poc.txt

HTTP 200 - NASA VDP PoC by obaskly - Bugcrowd

**WHAT AN ATTACKER COULD DO**

I only ever uploaded a text file. Someone with worse intentions could have:

\- Put fake .nc, .h5 or .tif files at the paths NASA’s granules reference. Scientists would download altered satellite data and might never find out. Picture a fake ground displacement map going into someone’s earthquake analysis.

- Hide malware in files people treat as plain data. Nobody runs antivirus on NetCDF files.

- Log every request and see who’s downloading what, from where, and when.

Most subdomain or bucket takeovers end with defacing a page nobody visits. This one sat in the middle of a scientific data pipeline.

**THE FIX**

NASA’s side was straightforward:

\- Get the bucket names back under NASA’s AWS account, which meant I had to delete mine first.

- Audit every DirectDistributionInformation entry in CMR for other dead buckets.

- Longer term, sign or checksum the data so clients can verify files no matter where they came from.

The issue has been triaged, fixed and resolved.

**TAKEAWAYS**

\- Metadata is attack surface. Any bucket name, hostname or URL a system hands out is worth checking to see if it still exists.

- Count the blast radius. “I took over a bucket” sounds like a P3. “I took over a bucket referenced by 79 million files that NASA’s SDK reads” doesn’t. Get the numbers and put them in the report.

- Follow the reference all the way through. Showing that earthaccess reads that field is what made the impact real.

Thanks to the NASA and ASF teams for fixing it.

\- obaskly
