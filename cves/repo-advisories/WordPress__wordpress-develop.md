# Repository security advisories: WordPress/wordpress-develop (54 published)

Verbatim from GitHub API `repos/WordPress/wordpress-develop/security-advisories` on 2026-11-12.

## GHSA-x3wp-h3qx-9w94 — Stored cross-site scripting (XSS) in WordPress block editor
- CVE: CVE-2019-16780 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2019-12-20T23:12:22Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-x3wp-h3qx-9w94
- Affected /: vulnerable 5.0.7, 5.1.3, 5.2.4, and 5.3.0 patched 5.3.1

### Impact
WordPress users with lower privileges (like contributors) can inject JavaScript code in the block editor using a specific payload, which is executed within the dashboard. This can lead to XSS if an admin opens the post in the editor. Execution of this attack does require an authenticated user.

### Patches
This has been patched in WordPress 5.3.1, along with all the previous affected WordPress versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### References
* https://wordpress.org/news/2019/12/wordpress-5-3-1-security-and-maintenance-release/
* https://hackerone.com/reports/738644

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-pg4x-64rh-3c9v — Authenticated cross-site scripting (XSS) in WordPress block editor (within dashboard)
- CVE: CVE-2019-16781 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2019-12-20T23:12:56Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-pg4x-64rh-3c9v
- Affected /: vulnerable 5.0.7, 5.1.3, 5.2.4, and 5.3.0 patched 5.3.1

### Impact
Authenticated users with lower privileges (like contributors) can inject JavaScript code in the block editor, which is executed within the dashboard. It can lead to an admin opening the affected post in the editor leading to XSS.

### Patches
This has been patched in WordPress 5.3.1, along with all the previous affected WordPress versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### References
* https://wordpress.org/news/2019/12/wordpress-5-3-1-security-and-maintenance-release/
* https://hackerone.com/reports/731301

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-xvg2-m2f4-83m7 — Stored cross-site scripting (XSS) through 'wp_targeted_link_rel'
- CVE: CVE-2019-16773 | Severity: high | CVSS: None `None` | CWE: 
- Published: 2020-01-08T16:11:05Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-xvg2-m2f4-83m7
- Affected /: vulnerable 5.0.7, 5.1.3, 5.2.4, and 5.3.0 patched 5.3.1

### Impact
The function `wp_targeted_link_rel()` can be used in a particular way to result in a stored cross-site scripting (XSS) vulnerability. 

### Patches
This has been patched in WordPress 5.3.1, along with all the previous affected WordPress versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### References
* https://hackerone.com/reports/509930

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)


## GHSA-g7rg-hchx-c2gw — Users without "publish_posts" rights can mark sticky/unsticky a post via REST API
- CVE: CVE-2019-16788 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-01-08T17:15:37Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-g7rg-hchx-c2gw
- Affected /: vulnerable 4.7.15, 4.8.11, 4.9.12, 5.0.7, 5.1.3, 5.2.4, 5.3.0 patched 4.7.16, 4.8.12, 4.9.13, 5.0.8, 5.1.4, 5.2.5, 5.3.1

### Impact
Authenticated users who do not have the rights to publish a post are able to mark posts as sticky or unsticky via the REST API. For example, the contributor role does not have such rights, but this allowed them to bypass that.

### Patches
This has been patched in WordPress 5.3.1, along with all the previous WordPress versions from 3.7 to 5.3 via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### References

* https://wordpress.org/news/2019/12/wordpress-5-3-1-security-and-maintenance-release/
* https://wordpress.org/support/wordpress-version/version-5-3-1/

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)


## GHSA-vccm-6gmc-qhjh — Cross-site scripting (XSS) in Search block - WordPress
- CVE: CVE-2020-11030 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-04-30T00:06:20Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-vccm-6gmc-qhjh
- Affected /: vulnerable 5.2 - 5.4 patched 5.4.1, 5.3.3, 5.2.6

### Impact
A special payload can be crafted that can lead to scripts getting executed within the RSS and search block of the block editor. This requires an authenticated user with the ability to add content.

### Patches
This has been patched in WordPress 5.4.1, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-568w-8m88-8g2c — WordPress: Cross-site scripting in stats method (object cache)
- CVE: CVE-2020-11029 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-04-30T00:06:28Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-568w-8m88-8g2c
- Affected /: vulnerable 3.7 - 5.4 patched 5.4.1

### Impact
A vulnerability in the stats() method of class-wp-object-cache.php can be exploited to execute cross-site scripting (XSS) attacks.

### Patches
This has been patched in WordPress 5.4.1, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-xhx9-759f-6p2w — WordPress: Unauthenticated disclosure of certain private posts
- CVE: CVE-2020-11028 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-04-30T00:06:41Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-xhx9-759f-6p2w
- Affected /: vulnerable 3.7 - 5.4 patched 5.4.1

### Impact
Some private posts, which were previously public, can result in unauthenticated disclosure under a specific set of conditions.

### Patches
This has been patched in WordPress 5.4.1, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-ww7v-jg8c-q6jw — Password reset links invalidation issue in WordPress
- CVE: CVE-2020-11027 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-04-30T00:06:57Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-ww7v-jg8c-q6jw
- Affected /: vulnerable 3.7 - 5.4 patched 5.4.1

### Impact
Password reset link emailed to a user do not expire upon changing the user password. Access would be needed to the email account of the user by a malicious party for successful execution.

### Patches
This has been patched in WordPress 5.4.1, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-3gw2-4656-pfr2 — Specially crafted filenames in WordPress leading to XSS
- CVE: CVE-2020-11026 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-04-30T00:07:10Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-3gw2-4656-pfr2
- Affected /: vulnerable 3.7 - 5.4 patched 5.4.1

### Impact
Files with a specially crafted name when uploaded to the Media section can lead to script execution upon accessing the file. This requires an authenticated user with privileges to upload files.

### Patches
This has been patched in WordPress 5.4.1, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)


## GHSA-4mhg-j6fx-5g3c — Authenticated cross-site scripting (XSS) in WordPress Customizer
- CVE: CVE-2020-11025 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-04-30T00:07:33Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-4mhg-j6fx-5g3c
- Affected /: vulnerable 4.7 - 5.4 patched 5.4.1

### Impact
A cross-site scripting (XSS) vulnerability in the navigation section of Customizer allows JavaScript code to be executed. Exploitation requires an authenticated user.

### Patches
This has been patched in WordPress 5.4.1, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)


## GHSA-4vpv-fgg2-gcqc — WordPress: 'set-screen-option' filter misuse by plugins leading to privilege escalation
- CVE: CVE-2020-4050 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-06-12T05:31:18Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-4vpv-fgg2-gcqc
- Affected /: vulnerable 3.7 - 5.4.1 patched 5.4.2

### Impact
Misuse of the `set-screen-option` filter's return value allows arbitrary user meta fields to be saved. It does require an admin to install a plugin that would misuse the filter. Once installed, it can be leveraged by low privileged users.

### Patches
This has been patched in WordPress 5.4.2, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-87h4-phjv-rm6p — WordPress: Authenticated self-XSS via theme uploads
- CVE: CVE-2020-4049 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-06-12T05:31:25Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-87h4-phjv-rm6p
- Affected /: vulnerable 3.7 - 5.4.1 patched 5.4.2

### Impact
When uploading themes, the name of the theme folder can be crafted in a way that could lead to JavaScript execution in /wp-admin on the themes page. This does require an admin to upload the theme, and is low severity self-XSS.

### Patches
This has been patched in WordPress 5.4.2, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-q6pw-gvf4-5fj5 — WordPress: Open redirect in wp_validate_redirect()
- CVE: CVE-2020-4048 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-06-12T05:31:29Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-q6pw-gvf4-5fj5
- Affected /: vulnerable 3.7 - 5.4.1 patched 5.4.2

### Impact
Due to an issue in wp_validate_redirect() and URL sanitization, an arbitrary external link can be crafted leading to unintended/open redirect when clicked.

### Patches
This has been patched in WordPress 5.4.2, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-8q2w-5m27-wm27 — WordPress: Authenticated XSS via media attachment page
- CVE: CVE-2020-4047 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-06-12T05:31:34Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-8q2w-5m27-wm27
- Affected /: vulnerable 3.7 - 5.4.1 patched 5.4.2

### Impact
Authenticated users with upload permissions (like authors) are able to inject JavaScript into some media file attachment pages in a certain way. This can lead to script execution in the context of a higher privileged user when the file is viewed by them.

### Patches
This has been patched in WordPress 5.4.2, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-rpwf-hrh2-39jf — WordPress: Authenticated XSS through embed block
- CVE: CVE-2020-4046 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-06-12T05:31:41Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-rpwf-hrh2-39jf
- Affected /: vulnerable 5.1 - 5.4.1 patched 5.4.2

### Impact
Users with low privileges (like contributors and authors) can use the embed block in a certain way to inject unfiltered HTML in the block editor. When affected posts are viewed by a higher privileged user, this could lead to script execution in the editor/wp-admin.

### Patches
This has been patched in WordPress 5.4.2, along with all the previously affected versions via a minor release. Automatic updates are enabled by default for minor releases and we strongly recommend that you keep them enabled.

### For more information
If you have any questions or comments about this advisory:
* Open an issue on [HackerOne](https://hackerone.com/wordpress)

## GHSA-pmmh-2f36-wvhq — WordPress: Authenticated disclosure of password-protected posts and pages 
- CVE: CVE-2021-29450 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2021-04-15T10:14:22Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-pmmh-2f36-wvhq
- Affected /: vulnerable 4.7 - 5.7 patched 5.7.1

### Impact
One of the blocks in the WordPress editor can be exploited in a way that exposes password-protected posts and pages. This requires at least contributor privileges.

### Patches
This has been patched in WordPress 5.7.1, along with the older affected versions via minor releases. It's strongly recommended that you keep auto-updates enabled to receive the fix.

### References
https://wordpress.org/news/category/security/

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)


## GHSA-rv47-pc52-qrhh — WordPress: Authenticated XXE attack when installation is running PHP 8
- CVE: CVE-2021-29447 | Severity: medium | CVSS: None `None` | CWE: CWE-611
- Published: 2021-04-15T10:14:33Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-rv47-pc52-qrhh
- Affected /: vulnerable 5.6 - 5.7 patched 5.7.1

### Impact
A user with the ability to upload files (like an Author) can exploit an XML parsing issue in the Media Library leading to XXE attacks. This requires WordPress installation to be using PHP 8. Access to internal files is possible in a successful XXE attack.

### Patches
This has been patched in WordPress version 5.7.1, along with the older affected versions via a minor release. We strongly recommend you keep auto-updates enabled.

### References
https://wordpress.org/news/category/security/

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)


## GHSA-fr6h-3855-j297 — WordPress 5.8 beta: Stored Cross-Site Scripting (XSS) vulnerability in widget editor
- CVE: CVE-2021-39202 | Severity: low | CVSS: 3.8 `CVSS:3.0/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:N` | CWE: CWE-80
- Published: 2021-09-09T17:01:42Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-fr6h-3855-j297
- Affected wordpress/: vulnerable 5.8 beta 1 - 5.8 beta 2 patched 5.8

### Impact
The widgets editor introduced in WordPress 5.8 beta 1 has improper handling of HTML input in the Custom HTML feature. This leads to stored XSS in the custom HTML widget.

### Patches
This has been patched in WordPress 5.8. It was only present during the testing/beta phase of WordPress 5.8.

### References
https://hackerone.com/reports/1222797
https://wordpress.org/news/category/releases/

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)

## GHSA-m9hc-7v5q-x8q5 — WordPress: Information Disclosure in wp_die() via JSONP, leading to CSRF
- CVE: CVE-2021-39200 | Severity: medium | CVSS: None `None` | CWE: CWE-200, CWE-352
- Published: 2021-09-09T17:02:08Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-m9hc-7v5q-x8q5
- Affected wordpress/: vulnerable 5.2 - 5.8 patched 5.8.1

### Impact
Output data of the function wp_die() can be leaked under certain conditions, which can include data like nonces. It can then be used to perform actions on your behalf.

### Patches
This has been patched in WordPress 5.8.1, along with any older affected versions via minor releases. It's strongly recommended that you keep auto-updates enabled to receive the fix.

### References
https://wordpress.org/news/category/releases/
https://hackerone.com/reports/1142140

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)

## GHSA-qxvw-qxm9-qvg6 — WordPress 5.8 beta: Private data disclosure/privilege escalation through the block editor
- CVE: CVE-2021-39203 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2021-09-09T17:02:24Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-qxvw-qxm9-qvg6
- Affected wordpress/: vulnerable 5.8 beta 1 patched 5.8

### Impact
Authenticated users who don't have permission to view private post types/data can bypass restrictions in the block editor under certain conditions.

### Patches
This affected WordPress 5.8 beta during the testing period. It's fixed in the final 5.8 release.

### References
https://wordpress.org/news/category/releases/
https://hackerone.com/reports/1225282

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)

## GHSA-wh69-25hr-h94v — Authenticated cross-site scripting (XSS) in WordPress editor
- CVE: CVE-2021-39201 | Severity: medium | CVSS: None `None` | CWE: CWE-79
- Published: 2021-09-09T17:03:09Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-wh69-25hr-h94v
- Affected wordpress/: vulnerable 5.0 - 5.7.2 patched 5.8

### Impact
The issue allows an authenticated but low-privileged user (like contributor/author) to execute XSS in the editor. This bypasses the restrictions imposed on users who do not have the permission to post `unfiltered_html`.

### Patches
This has been patched in WordPress 5.8, and will be pushed to older versions via minor releases (automatic updates). It's strongly recommended that you keep auto-updates enabled to receive the fix.

### References
https://wordpress.org/news/category/releases/
https://hackerone.com/reports/1142140

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)

## GHSA-jp3p-gw8h-6x86 — WordPress: SQL injection due to improper sanitization in WP_Meta_Query
- CVE: CVE-2022-21664 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2022-01-06T21:11:52Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-jp3p-gw8h-6x86
- Affected wordpress/: vulnerable 4.1.33 - 5.8.2 patched 5.8.3

### Impact
Due to lack of proper sanitization in `WP_Meta_Query`, there's potential for blind SQL Injection.

### Patches
This has been patched in WordPress version 5.8.3. Older affected versions are also fixed via security release, that go back till 4.1.34. We strongly recommend that you keep auto-updates enabled.

### References
https://wordpress.org/news/category/releases/

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)

## GHSA-jmmq-m8p8-332h — WordPress: Authenticated Object Injection in Multisites
- CVE: CVE-2022-21663 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2022-01-06T21:12:14Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-jmmq-m8p8-332h
- Affected wordpress/: vulnerable < 5.8.3 patched 5.8.3

### Impact
On a multisite, users with Super Admin role can bypass explicit/additional hardening under certain conditions through object injection.

### Patches
This has been patched in WordPress version 5.8.3. Older affected versions are also fixed via security release, that go back till 3.7.37. We strongly recommend that you keep auto-updates enabled.

### References
https://wordpress.org/news/category/releases/
https://hackerone.com/reports/541469

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)


## GHSA-699q-3hj9-889w — WordPress: Stored XSS through authenticated users
- CVE: CVE-2022-21662 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2022-01-06T21:12:28Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-699q-3hj9-889w
- Affected wordpress/: vulnerable < 5.8.3 patched 5.8.3

### Impact
Low-privileged authenticated users (like author) in WordPress core are able to execute JavaScript/perform stored XSS attack, which can affect high-privileged users. 

### Patches
This has been patched in WordPress version 5.8.3. Older affected versions are also fixed via security release, that go back till 3.7.37. We strongly recommend that you keep auto-updates enabled.

### References
https://wordpress.org/news/category/releases/
https://hackerone.com/reports/425342

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)


## GHSA-6676-cqfm-gw84 — WordPress: SQL Injection through WP_Query
- CVE: CVE-2022-21661 | Severity: high | CVSS: None `None` | CWE: 
- Published: 2022-01-06T21:12:48Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-6676-cqfm-gw84
- Affected wordpress/: vulnerable < 5.8.3 patched 5.8.3

### Impact
Due to improper sanitization in WP_Query, there can be cases where SQL injection is possible through plugins or themes that use it in a certain way.
 
### Patches
This has been patched in WordPress version 5.8.3. Older affected versions are also fixed via security release, that go back till 3.7.37. We strongly recommend that you keep auto-updates enabled.

### References
https://wordpress.org/news/category/releases/
https://hackerone.com/reports/1378209

### For more information
If you have any questions or comments about this advisory:
* Open an issue in [HackerOne](https://hackerone.com/wordpress)


## GHSA-x79f-xrjv-jx5r — PHP file upload bypass via Plugin installer
- CVE: CVE-2024-31210 | Severity: high | CVSS: 7.6 `CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:H` | CWE: 
- Published: 2024-04-03T22:25:47Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-x79f-xrjv-jx5r
- Affected wordpress/WordPress: vulnerable >= 6.4.0 <6.4.3 patched 6.4.3
- Affected wordpress/WordPress: vulnerable >= 6.3.0 <6.3.3 patched 6.3.3
- Affected wordpress/WordPress: vulnerable >= 6.2.0 <6.2.4 patched 6.2.4
- Affected wordpress/WordPress: vulnerable >= 6.1.0 <6.1.5 patched 6.1.5
- Affected wordpress/WordPress: vulnerable >= 6.0.0 <6.0.7 patched 6.0.7
- Affected wordpress/WordPress: vulnerable >= 5.9.0 <5.9.9 patched 5.9.9
- Affected wordpress/WordPress: vulnerable >= 5.8.0 <5.8.9 patched 5.8.9
- Affected wordpress/WordPress: vulnerable >= 5.7.0 <5.7.11 patched 5.7.11
- Affected wordpress/WordPress: vulnerable >= 5.6.0 <5.6.13 patched 5.6.13
- Affected wordpress/WordPress: vulnerable >= 5.5.0 <5.5.14 patched 5.5.14
- Affected wordpress/WordPress: vulnerable >= 5.4.0 <5.4.15 patched 5.4.15
- Affected wordpress/WordPress: vulnerable >= 5.3.0 <5.3.17 patched 5.3.17
- Affected wordpress/WordPress: vulnerable >= 5.2.0 <5.2.20 patched 5.2.20
- Affected wordpress/WordPress: vulnerable >= 5.1.0 <5.1.18 patched 5.1.18
- Affected wordpress/WordPress: vulnerable >= 5.0.0 <5.0.21 patched 5.0.21
- Affected wordpress/WordPress: vulnerable >= 4.9.0 <4.9.25 patched 4.9.25
- Affected wordpress/WordPress: vulnerable >= 4.8.0 <4.8.24 patched 4.8.24
- Affected wordpress/WordPress: vulnerable >= 4.7.0 <4.7.28 patched 4.7.28
- Affected wordpress/WordPress: vulnerable >= 4.6.0 <4.6.28 patched 4.6.28
- Affected wordpress/WordPress: vulnerable >= 4.5.0 <4.5.31 patched 4.5.31
- Affected wordpress/WordPress: vulnerable >= 4.4.0 <4.4.32 patched 4.4.32
- Affected wordpress/WordPress: vulnerable >= 4.3.0 <4.3.33 patched 4.3.33
- Affected wordpress/WordPress: vulnerable >= 4.2.0 <4.2.37 patched 4.2.37
- Affected wordpress/WordPress: vulnerable <4.1.40 patched 4.1.40

### Impact

It's possible for a file of a type other than a zip file to be submitted as a new plugin by an administrative user on the Plugins -> Add New -> Upload Plugin screen in WordPress. If FTP credentials are requested for installation (in order to move the file into place outside of the `uploads` directory) then the uploaded file remains temporary available in the Media Library despite it not being allowed.

If the `DISALLOW_FILE_EDIT` constant is set to `true` on the site _and_ FTP credentials are required when uploading a new theme or plugin, then this technically allows an RCE when the user would otherwise have no means of executing arbitrary PHP code. This issue _only_ affects Administrator level users on single site installations, and Super Admin level users on Multisite installations where it's otherwise expected that the user does not have permission to upload or execute arbitrary PHP code.

* Lower level users are not affected
* Sites where the `DISALLOW_FILE_MODS` constant is set to `true` are not affected
* Sites where an administrative user either does not need to enter FTP credentials or they have access to the valid FTP credentials, are not affected

### Patches

The issue was fixed in WordPress 6.4.3 on January 30, 2024 and backported to branches back to 4.1.

### Workarounds

If the `DISALLOW_FILE_MODS` constant is defined as `true` then it will not be possible for any user to upload a plugin and therefore this issue will not be exploitable.


## GHSA-m257-q4m5-j653 — Remote Code Execution in `WP_HTML_Token`
- CVE: CVE-2024-31211 | Severity: medium | CVSS: 5.5 `CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:L/I:L/A:N` | CWE: 
- Published: 2024-04-03T22:49:48Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-m257-q4m5-j653
- Affected wordpress/WordPress: vulnerable >= 6.4.0 <6.4.2 patched 6.4.2

### Impact

Unserialization of instances of the `WP_HTML_Token` class allows for code execution via its `__destruct()` magic method.

### Patches

This issue was fixed in WordPress 6.4.2 on December 6th, 2023. Versions prior to 6.4.0 are not affected.

### References

This vulnerability was not responsibly disclosed to the WordPress security team and was published publicly as a zero-day vulnerability. [Find out more about responsibly reporting security vulnerabilities](https://make.wordpress.org/core/handbook/testing/reporting-security-vulnerabilities/).

## GHSA-ff9f-jf42-662q — REST API batch-route confusion and SQL injection issue leading to Remote Code Execution
- CVE: CVE-2026-63030 | Severity: critical | CVSS: None `None` | CWE: 
- Published: 2026-07-17T19:00:46Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-ff9f-jf42-662q
- Affected wordpress/WordPress: vulnerable 6.9.0 - 6.9.4 patched 6.9.5
- Affected wordpress/WordPress: vulnerable 7.0.0 - 7.0.1 patched 7.0.2

WordPress versions 6.9 and higher are vulnerable to a REST API batch-route confusion weakness, which combined with an SQL injection issue ([GHSA-fpp7-x2x2-2mjf](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-fpp7-x2x2-2mjf)) leads to Remote Code Execution.

WordPress versions 7.0.2, 6.9.5, and 7.1 beta2 have been released, containing fixes for the vulnerability.

Due to the severity of the vulnerability it is recommended that you update your sites immediately.

Discovered and responsibly disclosed by Adam Kues at Assetnote / Searchlight Cyber.

## GHSA-fpp7-x2x2-2mjf — Facilitated SQL injection vulnerability in the `author__not_in` parameter of `WP_Query`
- CVE: CVE-2026-60137 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-07-17T19:00:52Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-fpp7-x2x2-2mjf
- Affected wordpress/WordPress: vulnerable 6.8.0 - 6.8.5 patched 6.8.6
- Affected wordpress/WordPress: vulnerable 6.9.0 - 6.9.4 patched 6.9.5
- Affected wordpress/WordPress: vulnerable 7.0.0 - 7.0.1 patched 7.0.2

WordPress versions 6.8 and higher are vulnerable to an SQL injection issue.

In WordPress versions 6.9 and higher, this combined with a REST API batch-route confusion issue (GHSA-ff9f-jf42-662q) leads to Remote Code Execution.

WordPress versions 7.0.2, 6.9.5, 6.8.6, and 7.1 beta2 have been released, containing fixes for the vulnerability.

Due to the severity of the vulnerability it is recommended that you update your sites immediately.

Discovered and responsibly disclosed as a team by TF1T, dtro, and haongo.

## GHSA-52p2-r8wf-jcrf — Pre-auth reflected XSS on login screen with potential to lead to PHP code execution
- CVE: CVE-2026-64638 | Severity: high | CVSS: None `None` | CWE: 
- Published: 2026-08-06T18:54:17Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-52p2-r8wf-jcrf
- Affected wordpress/WordPress: vulnerable 7.0.0 - 7.0.2 patched 7.0.3
- Affected wordpress/WordPress: vulnerable 6.9.0 - 6.9.5 patched 6.9.6
- Affected wordpress/WordPress: vulnerable 6.8.0 - 6.8.6 patched 6.8.7
- Affected wordpress/WordPress: vulnerable 6.7.0 - 6.7.5 patched 6.7.6
- Affected wordpress/WordPress: vulnerable 6.6.0 - 6.6.5 patched 6.6.6
- Affected wordpress/WordPress: vulnerable 6.5.0 - 6.5.8 patched 6.5.9
- Affected wordpress/WordPress: vulnerable 6.4.0 - 6.4.8 patched 6.4.9
- Affected wordpress/WordPress: vulnerable 6.3.0 - 6.3.8 patched 6.3.9
- Affected wordpress/WordPress: vulnerable 6.2.0 - 6.2.9 patched 6.2.10
- Affected wordpress/WordPress: vulnerable 6.1.0 - 6.1.10 patched 6.1.11
- Affected wordpress/WordPress: vulnerable 6.0.0 - 6.0.12 patched 6.0.13
- Affected wordpress/WordPress: vulnerable 5.9.0 - 5.9.13 patched 5.9.14
- Affected wordpress/WordPress: vulnerable 5.8.0 - 5.8.13 patched 5.8.14
- Affected wordpress/WordPress: vulnerable 5.7.0 - 5.7.15 patched 5.7.16
- Affected wordpress/WordPress: vulnerable 5.6.0 - 5.6.17 patched 5.6.18
- Affected wordpress/WordPress: vulnerable 5.5.0 - 5.5.18 patched 5.5.19
- Affected wordpress/WordPress: vulnerable 5.4.0 - 5.4.19 patched 5.4.20
- Affected wordpress/WordPress: vulnerable 5.3.0 - 5.3.21 patched 5.3.22
- Affected wordpress/WordPress: vulnerable 5.2.0 - 5.2.24 patched 5.2.25
- Affected wordpress/WordPress: vulnerable 5.1.0 - 5.1.22 patched 5.1.23
- Affected wordpress/WordPress: vulnerable 5.0.0 - 5.0.25 patched 5.0.26
- Affected wordpress/WordPress: vulnerable 4.9.0 - 4.9.29 patched 4.9.30
- Affected wordpress/WordPress: vulnerable 4.8.0 - 4.8.28 patched 4.8.29
- Affected wordpress/WordPress: vulnerable 4.7.0 - 4.7.33 patched 4.7.34

WordPress is vulnerable to a pre-auth reflected XSS vulnerability on the login screen.

Via a specially crafted malicious third-party website hosted by an attacker, it is possible for this to be escalated to an RCE vulnerability with conditions outside of the attackers control. This requires successful social engineering of and explicit interaction by the target victim.

This issue affects all versions of WordPress. Version 7.0.3 has been released, containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by [the team at pwn.ai](https://pwn.ai/).

Full information about the WordPress 7.0.3 release can be found here: https://wordpress.org/news/2026/08/wordpress-7-0-3-release/.

## GHSA-8vr3-7mxf-gx8w — Remote code execution vulnerability via malicious file upload by an Author level user or higher
- CVE: CVE-2026-65640 | Severity: high | CVSS: 8.8 `CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` | CWE: CWE-434
- Published: 2026-08-12T14:44:42Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-8vr3-7mxf-gx8w
- Affected wordpress/WordPress: vulnerable 7.0.0 - 7.0.3 patched 7.0.4
- Affected wordpress/WordPress: vulnerable 6.9.0 - 6.9.6 patched 6.9.7
- Affected wordpress/WordPress: vulnerable 6.8.0 - 6.8.7 patched 6.8.8
- Affected wordpress/WordPress: vulnerable 6.7.0 - 6.7.6 patched 6.7.7
- Affected wordpress/WordPress: vulnerable 6.6.0 - 6.6.6 patched 6.6.7
- Affected wordpress/WordPress: vulnerable 6.5.0 - 6.5.9 patched 6.5.10
- Affected wordpress/WordPress: vulnerable 6.4.0 - 6.4.9 patched 6.4.10
- Affected wordpress/WordPress: vulnerable 6.3.0 - 6.3.9 patched 6.3.10
- Affected wordpress/WordPress: vulnerable 6.2.0 - 6.2.10 patched 6.2.11
- Affected wordpress/WordPress: vulnerable 6.1.0 - 6.1.11 patched 6.1.12
- Affected wordpress/WordPress: vulnerable 6.0.0 - 6.0.13 patched 6.0.14
- Affected wordpress/WordPress: vulnerable 5.9.0 - 5.9.15 patched 5.9.16
- Affected wordpress/WordPress: vulnerable 5.8.0 - 5.8.14 patched 5.8.15
- Affected wordpress/WordPress: vulnerable 5.7.0 - 5.7.16 patched 5.7.17
- Affected wordpress/WordPress: vulnerable 5.6.0 - 5.6.18 patched 5.6.19
- Affected wordpress/WordPress: vulnerable 5.5.0 - 5.5.19 patched 5.5.20
- Affected wordpress/WordPress: vulnerable 5.4.0 - 5.4.20 patched 5.4.21
- Affected wordpress/WordPress: vulnerable 5.3.0 - 5.3.22 patched 5.3.23
- Affected wordpress/WordPress: vulnerable 5.2.0 - 5.2.25 patched 5.2.26
- Affected wordpress/WordPress: vulnerable 5.1.0 - 5.1.23 patched 5.1.24
- Affected wordpress/WordPress: vulnerable 5.0.0 - 5.0.26 patched 5.0.27
- Affected wordpress/WordPress: vulnerable 4.9.0 - 4.9.30 patched 4.9.31
- Affected wordpress/WordPress: vulnerable 4.8.0 - 4.8.29 patched 4.8.30
- Affected wordpress/WordPress: vulnerable 4.7.0 - 4.7.34 patched 4.7.35

Certain installations of WordPress are vulnerable to a remote code execution vulnerability via malicious Postscript file upload by an Author level user or higher.

Prerequisites:

* Imagick and Ghostscript in use on the server (the weakness is in Ghostscript's handling of certain embedded files)
* A malicious user with the `upload_files` capability

WordPress version 7.0.4 has been released, containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by [the team at pwn.ai](https://pwn.ai/).

## GHSA-32m5-wc28-ghrr — Comments, including notes, can be reparented by any authenticated user
- CVE: None | Severity: medium | CVSS: 4.3 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N` | CWE: 
- Published: 2026-09-18T17:56:14Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-32m5-wc28-ghrr
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24

An authenticated user (Author role suffices) who created a comment on their own post can send a request that reparents it onto a post they cannot edit.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 5.3.

Discovered and responsibly disclosed by Justin Hart, Viridis Security.

## GHSA-33wf-p63q-w25f — Contributor+ Arbitrary Post Overwrite
- CVE: None | Severity: medium | CVSS: 6.5 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N` | CWE: 
- Published: 2026-09-18T17:57:08Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-33wf-p63q-w25f
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.35 patched 4.7.36

A Contributor can overwrite the title, content, and author of a published post by sending a specially crafted request to `wp-admin/post.php`

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by Anthropic.

## GHSA-cjfg-q57r-mq45 — Missing `read_post` check in `attachment_submitbox_metadata()` leaks a private parent-post title
- CVE: None | Severity: medium | CVSS: 5.3 `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` | CWE: CWE-862
- Published: 2026-09-18T17:57:32Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-cjfg-q57r-mq45
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20

The attachment edit screen renders the parent post's title without a `read_post` check, so a
low-privilege Author can be shown the title of a private or draft parent post that they cannot otherwise read.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 5.6.

Discovered and responsibly disclosed by [HDWSec](https://hdwsec.fr).

## GHSA-f522-h982-63mg — Missing Authorization leads to Draft/Pending Post Slug Disclosure by Contributor+
- CVE: None | Severity: low | CVSS: None `None` | CWE: 
- Published: 2026-09-18T17:58:47Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-f522-h982-63mg
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.35 patched 4.7.36

A Contributor-level user can discover the URL slugs of draft and pending posts from other users.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by Jakub Herman.

## GHSA-qg7r-fjh2-wvx8 — Stored cross-site scripting in `wpautop()` allows an unauthenticated visitor to inject script
- CVE: None | Severity: high | CVSS: None `None` | CWE: 
- Published: 2026-09-18T17:58:59Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-qg7r-fjh2-wvx8
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.35 patched 4.7.36

An unauthenticated visitor can post a comment containing a KSES-legal element whose attribute value holds a newline. `wpautop()` treats that newline as a paragraph boundary and rewrites a `<p>` inside the element, ultimately resulting in a live event-handler attribute being rendered on the page.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 5.9.

Discovered and responsibly disclosed by [Rafie Muhammad](https://www.linkedin.com/in/rafiemuhammad/) (Awesome Motive, Inc.)

## GHSA-w57f-v787-qhpf — Authenticated Path Traversal in WP REST Templates Controller
- CVE: None | Severity: medium | CVSS: 4.3 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N` | CWE: 
- Published: 2026-09-18T17:59:19Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-w57f-v787-qhpf
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17

The REST templates endpoint accepts template IDs whose slug regex can result in an unbound filesystem path. An authenticated Author can read any .html file on the server.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 5.9.

Discovered and responsibly disclosed by Anthropic.

## GHSA-xhp5-863h-rhfr — XML-RPC can be used to publish `customize_changeset` posts that bypass checks for `edit_css`
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-09-18T17:59:30Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-xhp5-863h-rhfr
- Affected other/WordPress: vulnerable 7.1.0 - 7.1 patched 7.1.1
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.35 patched 4.7.36

The generic XML-RPC `wp.newPost` path accepts caller-selected registered post types. A non-Super-Admin site administrator can therefore publish a raw `customize_changeset` post through XML-RPC that contains custom CSS that bypasses the expected check that usually ensures a user can `edit_css`.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by Alex Concha of the WordPress Security Team.

## GHSA-mgvw-845h-9qgq — A theme that supports custom-header and does not register an admin-preview-callback is vulnerable to stored XSS
- CVE: None | Severity: low | CVSS: None `None` | CWE: 
- Published: 2026-09-18T17:59:36Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-mgvw-845h-9qgq
- Affected /WordPress: vulnerable 7.1.0 patched 7.1.1
- Affected /WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected /WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected /WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected /WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected /WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected /WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected /WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected /WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected /WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected /WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected /WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected /WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected /WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected /WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected /WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected /WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected /WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected /WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected /WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected /WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected /WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected /WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected /WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31
- Affected /WordPress: vulnerable 4.7.0 - 4.7.35 patched 4.7.36

A user with `edit_theme_options` can store information about a custom header which on some themes can be used to create a stored XSS. 

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by Jeremy Felt of the WordPress Security Team.

## GHSA-5qf7-2r5p-ppj8 — Specially crafted URLs can automatically install and preview an inactive theme from WordPress.org
- CVE: None | Severity: medium | CVSS: 5.3 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:H/A:N` | CWE: 
- Published: 2026-09-18T17:59:48Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-5qf7-2r5p-ppj8
- Affected /WordPress: vulnerable 7.1.0 patched 7.1.1
- Affected /WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected /WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected /WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected /WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected /WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected /WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected /WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected /WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected /WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected /WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected /WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected /WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected /WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected /WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected /WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected /WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected /WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected /WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected /WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected /WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected /WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected /WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected /WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31

If an Administrator opens a specially crafted link and, when prompted, logs in, WordPress can automatically install and preview a theme from WordPress.org without the Administrator having to click the Install button. The theme gets written to disk, it remains inactive, and the Administrator immediately sees its preview. This does not change the live site but it does result in the previewed theme being fully loaded.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.8.

Discovered and responsibly disclosed by Paulos Yibelo and [pwn.ai](https://pwn.ai/)

## GHSA-76jg-r2qr-v77f — Site Administrator can network-activate an installed Network-only plugin
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-09-18T17:59:57Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-76jg-r2qr-v77f
- Affected /WordPress: vulnerable 7.1.0 patched 7.1.1
- Affected /WordPress: vulnerable 7.0.0 - 7.0.4 patched 7.0.5
- Affected /WordPress: vulnerable 6.9.0 - 6.9.7 patched 6.9.8
- Affected /WordPress: vulnerable 6.8.0 - 6.8.8 patched 6.8.9
- Affected /WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8
- Affected /WordPress: vulnerable 6.6.0 - 6.6.7 patched 6.6.8
- Affected /WordPress: vulnerable 6.5.0 - 6.5.10 patched 6.5.11
- Affected /WordPress: vulnerable 6.4.0 - 6.4.10 patched 6.4.11
- Affected /WordPress: vulnerable 6.3.0 - 6.3.10 patched 6.3.11
- Affected /WordPress: vulnerable 6.2.0 - 6.2.11 patched 6.2.12
- Affected /WordPress: vulnerable 6.1.0 - 6.1.12 patched 6.1.13
- Affected /WordPress: vulnerable 6.0.0 - 6.0.14 patched 6.0.15
- Affected /WordPress: vulnerable 5.9.0 - 5.9.16 patched 5.9.17
- Affected /WordPress: vulnerable 5.8.0 - 5.8.15 patched 5.8.16
- Affected /WordPress: vulnerable 5.7.0 - 5.7.17 patched 5.7.18
- Affected /WordPress: vulnerable 5.6.0 - 5.6.19 patched 5.6.20
- Affected /WordPress: vulnerable 5.5.0 - 5.5.20 patched 5.5.21
- Affected /WordPress: vulnerable 5.4.0 - 5.4.21 patched 5.4.22
- Affected /WordPress: vulnerable 5.3.0 - 5.3.23 patched 5.3.24
- Affected /WordPress: vulnerable 5.2.0 - 5.2.26 patched 5.2.27
- Affected /WordPress: vulnerable 5.1.0 - 5.1.24 patched 5.1.25
- Affected /WordPress: vulnerable 5.0.0 - 5.0.27 patched 5.0.28
- Affected /WordPress: vulnerable 4.9.0 - 4.9.31 patched 4.9.32
- Affected /WordPress: vulnerable 4.8.0 - 4.8.30 patched 4.8.31
- Affected /WordPress: vulnerable 4.7.0 - 4.7.35 patched 4.7.36

On Multisite networks where the Network Administrator exposes the Plugins menu to site Administrators, a plugin that has the `network: true` header can be network-activated by a site Administrator.

WordPress 7.1.1 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by Jesse McNeil.

## GHSA-rmpv-w5v9-rqh5 — HTML API: `set_modifiable_text()` allows breaking out of a comment via abrupt-closing sequences
- CVE: None | Severity: low | CVSS: 1.8 `CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:U/C:N/I:L/A:N` | CWE: 
- Published: 2026-09-18T18:12:46Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-rmpv-w5v9-rqh5
- Affected /WordPress: vulnerable 7.1.0 patched 7.1.1 
- Affected /WordPress: vulnerable  7.0.0 - 7.0.4  patched 7.0.5 
- Affected /WordPress: vulnerable 6.9.0 - 6.9.7 patched  6.9.8
- Affected /WordPress: vulnerable  6.8.0 - 6.8.8 patched 6.8.9
- Affected /WordPress: vulnerable 6.7.0 - 6.7.7 patched 6.7.8

If specific strings are passed to `WP_HTML_Tag_Processor`'s `set_modifiable_text()` method, the tag processor can break out of an HTML comment and inject markup.

There is no direct WordPress core or Gutenberg vulnerability as a result of this but the issue is being fixed as a hardening measure.

WordPress 7.1.1 has been released containing hardening, and as a courtesy to users on older branches this has been backported to all branches back to 6.7.

Discovered and responsibly disclosed by Jeremy Felt of the WordPress Security Team

## GHSA-7hp8-65ch-5whp — Unauthenticated path traversal in page-template resolution leading to conditional RCE
- CVE: CVE-2026-87902 | Severity: critical | CVSS: None `None` | CWE: CWE-98
- Published: 2026-09-22T13:57:27Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.1 patched 7.1.2
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.5 patched 7.0.6
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.8 patched 6.9.9
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.9 patched 6.8.10
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.8 patched 6.7.9
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.8 patched 6.6.9
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.11 patched 6.5.12
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.11 patched 6.4.12
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.11 patched 6.3.12
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.12 patched 6.2.13
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.13 patched 6.1.14
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.15 patched 6.0.16
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.17 patched 5.9.18
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.16 patched 5.8.17
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.18 patched 5.7.19
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.20 patched 5.6.21
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.21 patched 5.5.22
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.22 patched 5.4.23
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.24 patched 5.3.25
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.27 patched 5.2.28
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.25 patched 5.1.26
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.28 patched 5.0.29
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.32 patched 4.9.33
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.31 patched 4.8.32
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.36 patched 4.7.37
- Credits: ressl

An unauthenticated attacker can make `get_page_template()` page-template resolution include a chosen readable local `.php` file outside the active theme directories. If relevant pre-conditions for both the server environment and the active theme are met, this can lead to RCE.

The pre-conditions are:

* The active child or parent theme contains a top-level directory whose name starts with `page-` (e.g. `page-templates`). This affects the legacy Twenty Twelve and Twenty Fourteen themes, as well as some popular third party themes such as Neve, Hestia, and Sydney.
* A chosen local `.php` target file exists on the server and is readable by the web server account. The well known `pearcmd.php` PEAR→RCE transition can be used for this when `register_argc_argv` is set to `On`. The official `php` image for Docker is affected, and the default cPanel configuration is affected when PHP prior to 8.5 is in use.

WordPress 7.1.2 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by [Robert Ressl](https://ressl.ch/).

## GHSA-83c2-c4pc-wmp3 — Contributor+ stored cross-site scripting (XSS) and denial of service issues in Interactivity API bindings
- CVE: None | Severity: high | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:00:39Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-83c2-c4pc-wmp3
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Credits: marcelhacks, rekter0, anas-cherni

Several Interactivity API binding issues let a user with the Contributor role or above store cross-site scripting or a denial of service in post content: inherited property lookups that reach `innerHTML`, `__proto__` as a directive name, bindings to internal props or inherited methods, and `data-wp-style` writing into any resolved object.

WordPress 7.1.4 has been released containing fixes for these vulnerabilities, and as a courtesy to users on older branches the fixes have been backported to all branches back to 6.4.

Discovered and responsibly disclosed by rekter0, Marcel Karlsson (whoismarcel), Jon Surrell and Alex Concha of the WordPress Security Team.

## GHSA-2p22-wv7j-cvfv — A hardening fix for unsafe preg_replace() replacements in the Image and Playlist blocks
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:02:35Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-2p22-wv7j-cvfv
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14

The Image and Playlist blocks built markup with `preg_replace()` using replacement strings that include block attributes, so backreferences such as `$1` in those values were expanded into the output. The blocks now use `preg_replace_callback()`.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 6.4.

Discovered and responsibly disclosed by Ben Bidner of the WordPress Security Team.

## GHSA-7q86-3j97-744j — A cross-site scripting (XSS) issue in the Categories block via format string injection
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:02:55Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7q86-3j97-744j
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11

The Categories block passes a user-controlled string to `sprintf()` as its format string, which allows cross-site scripting.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 6.7.

Discovered and responsibly disclosed by Ben Bidner.

## GHSA-wjwj-p342-9fq7 — An issue allowing post content to shadow Script Module data with a matching element ID
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:03:31Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-wjwj-p342-9fq7
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11

Post content can include an element whose ID matches a Script Module's data script, so a post author can replace the data that the module reads.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 6.6.

Discovered and responsibly disclosed by Weston Ruter.

## GHSA-j255-3x8q-7q7g — A Contributor+ stored cross-site scripting (XSS) issue in the labels of the Comments Pagination and Post Navigation Link blocks
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:03:53Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-j255-3x8q-7q7g
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.13 patched 6.3.14
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.14 patched 6.2.15
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.15 patched 6.1.16
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.17 patched 6.0.18
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.19 patched 5.9.20

The Comments Pagination Next, Comments Pagination Previous and Post Navigation Link blocks output their label without escaping, so a user with the Contributor role or above can store script in post content.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 5.9.

Discovered and responsibly disclosed by Alex Concha of the WordPress Security Team.

## GHSA-9vrg-x932-q57q — A Contributor+ stored cross-site scripting (XSS) issue in Customizer selective refresh
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:05:06Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-9vrg-x932-q57q
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.13 patched 6.3.14
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.14 patched 6.2.15
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.15 patched 6.1.16
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.17 patched 6.0.18
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.19 patched 5.9.20
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.18 patched 5.8.19
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.20 patched 5.7.21
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.22 patched 5.6.23
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.23 patched 5.5.24
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.24 patched 5.4.25
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.26 patched 5.3.27
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.29 patched 5.2.30
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.27 patched 5.1.28
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.30 patched 5.0.31

A user with the Contributor role or above can store markup in post content that Customizer selective refresh treats as HTML, which runs a script in an Administrator's Customizer preview.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 5.0.

Discovered and responsibly disclosed by [Rafie Muhammad](https://www.linkedin.com/in/rafiemuhammad/) (Awesome Motive, Inc.)

## GHSA-j3rg-rwgx-7wx7 — Unescaped usernames on the multisite Network Users screens, fixed as a hardening measure
- CVE: None | Severity: low | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:08:09Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-j3rg-rwgx-7wx7
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.13 patched 6.3.14
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.14 patched 6.2.15
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.15 patched 6.1.16
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.17 patched 6.0.18
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.19 patched 5.9.20
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.18 patched 5.8.19
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.20 patched 5.7.21
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.22 patched 5.6.23
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.23 patched 5.5.24
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.24 patched 5.4.25
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.26 patched 5.3.27
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.29 patched 5.2.30
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.27 patched 5.1.28
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.30 patched 5.0.31
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.34 patched 4.9.35
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.33 patched 4.8.34
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.38 patched 4.7.39

Usernames were output without escaping on the multisite Network Users screens. Normal WordPress flows can't store an unsafe username, so exploiting this needs direct database access. There is no direct vulnerability as a result of this, but the issue is being fixed as a hardening measure.

WordPress 7.1.4 has been released containing hardening, and as a courtesy to users on older branches the hardening has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by Anthropic.

## GHSA-mqjw-vvgg-xfvf — An Editor+ stored cross-site scripting (XSS) issue in the personal data erasure requests screen
- CVE: None | Severity: low | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:08:30Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-mqjw-vvgg-xfvf
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.13 patched 6.3.14
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.14 patched 6.2.15
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.15 patched 6.1.16
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.17 patched 6.0.18
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.19 patched 5.9.20
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.18 patched 5.8.19
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.20 patched 5.7.21
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.22 patched 5.6.23
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.23 patched 5.5.24
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.24 patched 5.4.25
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.26 patched 5.3.27
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.29 patched 5.2.30
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.27 patched 5.1.28
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.30 patched 5.0.31
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.34 patched 4.9.35

A user with the Editor role or above can create a personal data erasure request through XML-RPC whose email field contains a script, which runs when an Administrator views the Erase Personal Data screen.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.9.

Discovered and responsibly disclosed by Anthropic.

## GHSA-vchg-92fx-636p — A permissions issue letting custom roles that moderate comments read, edit and delete notes on posts they can't edit
- CVE: None | Severity: low | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:08:53Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-vchg-92fx-636p
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11

A custom role that holds `moderate_comments` but can't edit a post can read, modify and delete the notes on that post through the update and delete endpoints. No default role is affected.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 6.9.

Discovered and responsibly disclosed by Ramon of the WordPress Security Team.

## GHSA-p2r6-rwjp-phv3 — An information disclosure issue exposing unpublished Customizer changes to unauthenticated visitors
- CVE: None | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:10:17Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-p2r6-rwjp-phv3
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.13 patched 6.3.14
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.14 patched 6.2.15
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.15 patched 6.1.16
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.17 patched 6.0.18
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.19 patched 5.9.20
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.18 patched 5.8.19
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.20 patched 5.7.21
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.22 patched 5.6.23
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.23 patched 5.5.24
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.24 patched 5.4.25
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.26 patched 5.3.27
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.29 patched 5.2.30
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.27 patched 5.1.28
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.30 patched 5.0.31
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.34 patched 4.9.35

An unauthenticated visitor can load the newest unpublished Customizer changeset in a front-end preview without knowing its UUID, which exposes unpublished changes.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.9.

Discovered and responsibly disclosed by [Antonio Lorensius Silaban](https://www.linkedin.com/in/antoniolorensius/).

## GHSA-4w3m-c66w-69mg — A race condition during core updates that could lead to remote code execution
- CVE: None | Severity: low | CVSS: None `None` | CWE: 
- Published: 2026-10-29T19:12:01Z | URL: https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-4w3m-c66w-69mg
- Affected other/WordPress: vulnerable 7.1.0 - 7.1.3 patched 7.1.4
- Affected other/WordPress: vulnerable 7.0.0 - 7.0.7 patched 7.0.8
- Affected other/WordPress: vulnerable 6.9.0 - 6.9.10 patched 6.9.11
- Affected other/WordPress: vulnerable 6.8.0 - 6.8.11 patched 6.8.12
- Affected other/WordPress: vulnerable 6.7.0 - 6.7.10 patched 6.7.11
- Affected other/WordPress: vulnerable 6.6.0 - 6.6.10 patched 6.6.11
- Affected other/WordPress: vulnerable 6.5.0 - 6.5.13 patched 6.5.14
- Affected other/WordPress: vulnerable 6.4.0 - 6.4.13 patched 6.4.14
- Affected other/WordPress: vulnerable 6.3.0 - 6.3.13 patched 6.3.14
- Affected other/WordPress: vulnerable 6.2.0 - 6.2.14 patched 6.2.15
- Affected other/WordPress: vulnerable 6.1.0 - 6.1.15 patched 6.1.16
- Affected other/WordPress: vulnerable 6.0.0 - 6.0.17 patched 6.0.18
- Affected other/WordPress: vulnerable 5.9.0 - 5.9.19 patched 5.9.20
- Affected other/WordPress: vulnerable 5.8.0 - 5.8.18 patched 5.8.19
- Affected other/WordPress: vulnerable 5.7.0 - 5.7.20 patched 5.7.21
- Affected other/WordPress: vulnerable 5.6.0 - 5.6.22 patched 5.6.23
- Affected other/WordPress: vulnerable 5.5.0 - 5.5.23 patched 5.5.24
- Affected other/WordPress: vulnerable 5.4.0 - 5.4.24 patched 5.4.25
- Affected other/WordPress: vulnerable 5.3.0 - 5.3.26 patched 5.3.27
- Affected other/WordPress: vulnerable 5.2.0 - 5.2.29 patched 5.2.30
- Affected other/WordPress: vulnerable 5.1.0 - 5.1.27 patched 5.1.28
- Affected other/WordPress: vulnerable 5.0.0 - 5.0.30 patched 5.0.31
- Affected other/WordPress: vulnerable 4.9.0 - 4.9.34 patched 4.9.35
- Affected other/WordPress: vulnerable 4.8.0 - 4.8.33 patched 4.8.34
- Affected other/WordPress: vulnerable 4.7.0 - 4.7.38 patched 4.7.39

During a core update that uses a complete package, WordPress extracted the new files to a predictable directory inside the web-served upgrade folder. An unauthenticated attacker who wins a race against that extraction could reach remote code execution.

WordPress 7.1.4 has been released containing a fix for the vulnerability, and as a courtesy to users on older branches the fix has been backported to all branches back to 4.7.

Discovered and responsibly disclosed by [Umut Bayram](https://www.picussecurity.com/resource/author/umut-bayram).
