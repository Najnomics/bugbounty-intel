# Wordpress users Disclosure [ /wp-json/wp/v2/users/ ]

- **Source URL:** https://hackerone.com/reports/1735586
- **Fetched from:** https://hackerone.com/reports/1735586.json
- **Fetched:** 2026-11-15
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/917 (id 917)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Wordpress users Disclosure [ /wp-json/wp/v2/users/ ]

- **HackerOne report:** https://hackerone.com/reports/1735586
- **State:** Resolved
- **Severity:** critical
- **Weakness:** Information Disclosure
- **Program:** MTN Group (https://hackerone.com/mtn_group)
- **Reporter:** shubham_srt
- **Submitted (UTC):** 2022-10-14T13:29:56.108Z
- **Disclosed (UTC):** 2022-11-27T03:25:02.082Z
- **Attachments (filenames only; expiring CDN URLs omitted):** image.png (image/png)

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
Using REST API, we can see all the WordPress users/author with some of their information. Which can even be Personal information of employees/author. The file v2/users at:  https://www.mtn.com/wp-json/wp/v2/users/   is enabled and this give the attacker many users names like:  `Amogelang Maluleka` `Greg Davies` `karenbyamugisha` `Marc Ilunga` `mitchprinsloo`

## Steps To Reproduce:

  1.  Go to https://www.mtn.com/wp-json/wp/v2/users/  [ Allows anyone to view active usernames ]

{F1985941}

## Supporting Material/References:
https://hackerone.com/reports/356047
https://hackerone.com/reports/370777

###Fix:
Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.
```javascript
add_filter( 'rest_endpoints', function( $endpoints ){
    if ( isset( $endpoints['/wp/v2/users'] ) ) {
        unset( $endpoints['/wp/v2/users'] );
    }
    if ( isset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] ) ) {
        unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    }
    return $endpoints;
});
```

## Impact

Malicious counterpart could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known), making it less harder to penetrate the data.gov systems.
