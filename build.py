#!/usr/bin/env python3
"""Static site generator for fighttowinmarriages (Netlify). Run: python3 build.py"""
import json, os, html

SITE = "https://fight-to-win-marriages.netlify.app"  # TODO: swap to custom domain when purchased
OUT = os.path.join(os.path.dirname(__file__), "site")
NAME = "Fight to Win Marriages"
IG = "https://www.instagram.com/fighttowinmarriages/"
YT = "https://www.youtube.com/watch?v=5Sk_Hm1As2k"
EMAIL = "fighttowinmarriages@gmail.com"
ZOOM = "https://us02web.zoom.us/j/84083347510"
ZOOM_ID = "840 8334 7510"
TUE_TIME = "6:00 PM CT"
TT = ""  # [PLACEHOLDER: TikTok profile URL] - footer link and sameAs appear once set
SAME_AS = [u for u in (IG, TT, YT) if u]

NAV = [
    ("/", "Home"),
    ("/about/", "About Terrie"),
    ("/marriage-coaching/", "Coaching"),
    ("/tuesday-prayer-call/", "Tuesday Prayer Call"),
    ("/events/", "Events & Speaking"),
    ("/blog/", "Blog"),
]

def ph(text):
    """Visible placeholder for facts Terrie still needs to supply."""
    return f'<mark class="ph" title="Placeholder: replace before launch">[{html.escape(text)}]</mark>'

ORG = {
    "@type": "Organization",
    "@id": f"{SITE}/#org",
    "name": NAME,
    "url": SITE + "/",
    "logo": f"{SITE}/assets/logo.png",
    "description": "Faith-based marriage ministry founded on 2 Corinthians 10:4 and Ephesians 6:12 that equips husbands and wives with spiritual warfare, biblical principles, prayer and practical tools to build healed, healthy, God-centered marriages.",
    "email": EMAIL,
    "founder": {"@id": f"{SITE}/#terrie"},
    "sameAs": SAME_AS,
}
PERSON = {
    "@type": "Person",
    "@id": f"{SITE}/#terrie",
    "name": "Terrie Beeman",
    "jobTitle": "Certified Christian Counselor and Marriage Coach",
    "description": "Terrie Beeman is a Certified Christian Counselor, Spiritual Life Coach, Marriage Coach, Motivator and Prayer Warrior, and the founder of Fight to Win Marriages.",
    "email": EMAIL,
    "image": f"{SITE}/assets/terrie-beeman.jpg",
    "url": f"{SITE}/about/",
    "worksFor": {"@id": f"{SITE}/#org"},
    "sameAs": SAME_AS,
    "knowsAbout": ["Christian marriage coaching", "Marriage restoration", "Prayer and fasting for marriage", "Biblical marriage", "Spiritual warfare prayer", "Christian counseling", "Premarital coaching"],
}
WEBSITE = {"@type": "WebSite", "@id": f"{SITE}/#website", "url": SITE + "/", "name": NAME, "publisher": {"@id": f"{SITE}/#org"}}

def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (u, n) in enumerate(items)]}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs, heading="Frequently Asked Questions"):
    items = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faqs)
    return f'<section class="section"><div class="wrap narrow"><h2>{heading}</h2><div class="faq">{items}</div></div></section>'

def cta_band(title="Your marriage is worth fighting for.", text="Book a coaching session, join the Tuesday prayer call, or invite Terrie to speak.", primary=("/contact/", "Book Terrie"), secondary=("/tuesday-prayer-call/", "Join Tuesday Prayer")):
    return f'''<section class="cta-band"><div class="wrap">
<h2>{title}</h2><p>{text}</p>
<div class="btns"><a class="btn gold" href="{primary[0]}">{primary[1]}</a><a class="btn ghost-light" href="{secondary[0]}">{secondary[1]}</a></div>
</div></section>'''

def page(path, title, desc, body, schema=None, og_type="website", crumb=None):
    url = SITE + path
    graph = [ORG, WEBSITE]
    if crumb:
        graph.append(crumbs(crumb))
    if schema:
        graph.extend(schema if isinstance(schema, list) else [schema])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1)
    cur = ' aria-current="page"'
    nav = "".join(f'<li><a href="{u}"{cur if (u == path or (u != "/" and path.startswith(u))) else ""}>{n}</a></li>' for u, n in NAV)
    bc = ""
    if crumb and len(crumb) > 1:
        bc = '<nav class="crumbs wrap" aria-label="Breadcrumb">' + " / ".join(
            (f'<a href="{u}">{html.escape(n)}</a>' if i < len(crumb) - 1 else f'<span aria-current="page">{html.escape(n)}</span>') for i, (u, n) in enumerate(crumb)) + "</nav>"
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{'noindex, follow' if path in ('/thank-you/', '/404.html') else 'index, follow, max-image-preview:large'}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#4a1d3a">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
<!-- [PLACEHOLDER: GA4 / GTM snippet goes here once property is created] -->
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap bar">
<a class="brand" href="/" aria-label="{NAME} home"><span class="mark" aria-hidden="true">&#10084;</span><span>Fight to Win <em>Marriages</em></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Main"><ul>{nav}</ul><a class="btn gold small" href="/contact/">Book Terrie</a></nav>
</div>
</header>
{bc}
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="wrap cols">
<div><p class="brand foot"><span class="mark" aria-hidden="true">&#10084;</span> Fight to Win Marriages</p>
<p>We don't give up on marriage. We fight in prayer, love &amp; faith. A God-filled space for healing, restoration, and standing on God's promises together.</p>
<p class="social"><a href="{IG}" rel="noopener" target="_blank">Instagram</a> · {f'<a href="{TT}" rel="noopener" target="_blank">TikTok</a> · ' if TT else ''}<a href="{YT}" rel="noopener" target="_blank">YouTube</a></p></div>
<div><h3>Ministry</h3><ul><li><a href="/marriage-coaching/">Christian Marriage Coaching</a></li><li><a href="/tuesday-prayer-call/">Tuesday Prayer &amp; Fasting Call</a></li><li><a href="/events/">Marriage Events &amp; Speaking</a></li><li><a href="/blog/">Marriage Blog</a></li></ul></div>
<div><h3>Connect</h3><ul><li><a href="/about/">About Terrie Beeman</a></li><li><a href="/contact/">Book or Contact</a></li><li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Phone: {ph("phone, optional")}</li></ul></div>
</div>
<div class="wrap legal"><p>&copy; 2026 Fight to Win Marriages. Coaching and Christian counseling are faith-based and are not a substitute for licensed clinical or mental health care. If you are in danger, call 911 or the National Domestic Violence Hotline at 1-800-799-7233.</p><p><a href="/privacy/">Privacy Policy</a></p></div>
</footer>
<script>
const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
b.addEventListener('click',()=>{{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>
'''
    if path.endswith(".html"):
        fp = os.path.join(OUT, path.strip("/"))
    else:
        d = os.path.join(OUT, path.strip("/"))
        os.makedirs(d, exist_ok=True)
        fp = os.path.join(d, "index.html")
    with open(fp, "w") as f:
        f.write(doc)
    return url

PORTRAIT = '<picture><source srcset="/assets/terrie-beeman.webp" type="image/webp"><img src="/assets/terrie-beeman.jpg" alt="Terrie Beeman, founder of Fight to Win Marriages, smiling outdoors" width="480" height="480" {extra}></picture>'

# ---------------------------------------------------------------- HOME
home_faq = [
    ("What is Fight to Win Marriages?", "Fight to Win Marriages is a faith-based marriage ministry led by Terrie Beeman. It encourages couples not to give up on their marriage and focuses on healing, restoration, and standing on God's promises through prayer, love and faith."),
    ("Who is marriage coaching for?", "Coaching is for married couples, engaged couples, and individual spouses standing for their marriage, whether you are newlyweds or have been married for decades."),
    ("When is the Tuesday prayer call?", "Terrie hosts an online marriage prayer and fasting call on Zoom every Tuesday. Couples young and old are welcome to join for prayer, encouragement and biblical guidance."),
    ("Can I book Terrie to speak at my church or event?", "Yes. Terrie speaks at church marriage ministries, couples retreats, women's conferences and marriage events. Use the booking form to share your date, location and audience."),
]
home = f'''
<section class="hero">
<div class="wrap hero-grid">
<div>
<p class="eyebrow">Christian marriage coaching &middot; Prayer &middot; Restoration</p>
<h1>We don't give up on marriage. We fight in <em>prayer, love &amp; faith.</em></h1>
<p class="lead">A God-filled space for healing, restoration, and standing on God's promises together. Terrie Beeman offers Christian marriage coaching, a weekly Tuesday prayer and fasting call, and marriage events for couples young and old.</p>
<div class="btns"><a class="btn gold" href="/marriage-coaching/">Book Marriage Coaching</a><a class="btn ghost" href="/tuesday-prayer-call/">Join Tuesday Prayer Call</a></div>
<p class="micro">Serving couples online nationwide. Newlyweds, empty nesters and every season between.</p>
</div>
<div class="portrait">{PORTRAIT.format(extra='fetchpriority="high"')}<p class="caption">Terrie Beeman, Founder</p></div>
</div>
</section>

<section class="section">
<div class="wrap">
<h2 class="center">Three ways to get help for your marriage</h2>
<div class="cards three">
<article class="card"><h3>Christian Marriage Coaching</h3><p>One-on-one or couples sessions rooted in Scripture. Work through conflict, broken trust, communication and separation with a coach who believes your marriage can be restored.</p><a class="link" href="/marriage-coaching/">Explore coaching &rarr;</a></article>
<article class="card featured"><h3>Tuesday Prayer &amp; Fasting Call</h3><p>Every Tuesday at {TUE_TIME}, Terrie prays, fasts and offers biblical guidance to couples on Zoom. Bring your marriage before God alongside others who are standing too.</p><a class="link" href="/tuesday-prayer-call/">Join the call &rarr;</a></article>
<article class="card"><h3>Events &amp; Speaking</h3><p>Invite Terrie to your church, couples retreat, women's conference or marriage ministry for a message of hope, healing and covenant love.</p><a class="link" href="/events/">Book Terrie to speak &rarr;</a></article>
</div>
</div>
</section>

<section class="section alt">
<div class="wrap split">
<div>
<p class="eyebrow">Our mission</p>
<h2>Putting marriages back on the map</h2>
<p>Marriage is one of God's greatest institutions, and we believe it is worth fighting for. Founded on 2 Corinthians 10:4 and Ephesians 6:12, Fight to Win Marriages partners with God to equip husbands and wives with spiritual warfare weapons, biblical principles, prayer, encouragement and practical tools to build strong, healthy, God-centered marriages.</p>
<p><strong>Our vision</strong> is to see marriages healed, healthy and whole, and to decrease the divorce rate in the body of believers.</p>
<h3>Who we serve</h3>
<ul class="checks">
<li>Married couples, newlyweds to decades in</li>
<li>Engaged couples and individuals preparing for marriage</li>
<li>Spouses seeking healing, restoration, wisdom and biblical guidance</li>
</ul>
<p>Whether your marriage needs healing, strengthening, encouragement or prayer, you are welcome here.</p>
</div>
<div>
<blockquote class="verse">"The weapons we fight with are not the weapons of the world. On the contrary, they have divine power to demolish strongholds."<cite>2 Corinthians 10:4</cite></blockquote>
<blockquote class="verse" style="margin-top:20px">"For our struggle is not against flesh and blood, but against the rulers, against the authorities, against the powers of this dark world and against the spiritual forces of evil in the heavenly realms."<cite>Ephesians 6:12</cite></blockquote>
</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div>
<h2>Winning means winning as a team</h2>
<p>In a marriage, your spouse is not the enemy. Most conflict is a battle against stress, exhaustion, old wounds and spiritual opposition. Fighting to win means you team up against the problem and stand together in prayer.</p>
<ul class="checks">
<li><strong>Shift your perspective.</strong> See the real battle behind the argument.</li>
<li><strong>Attack the problem, not the person.</strong> Trade "street fighting" for healthy, honoring boundaries.</li>
<li><strong>Seek the win-win.</strong> If one spouse wins and the other loses, the marriage loses.</li>
<li><strong>Stand on the Word.</strong> Pray God's promises over your home, even when feelings fade.</li>
</ul>
<a class="btn" href="/blog/how-to-fight-for-your-marriage/">Read: How to Fight for Your Marriage</a>
</div>
<blockquote class="verse">"Therefore what God has joined together, let no one separate."<cite>Mark 10:9</cite></blockquote>
</div>
</section>

<section class="section">
<div class="wrap">
<h2 class="center">What couples are saying</h2>
<div class="cards three">
<figure class="card quote"><blockquote>{ph("Couple testimonial #1, with permission")}</blockquote><figcaption>{ph("First names, years married")}</figcaption></figure>
<figure class="card quote"><blockquote>{ph("Couple testimonial #2, with permission")}</blockquote><figcaption>{ph("First names, years married")}</figcaption></figure>
<figure class="card quote"><blockquote>{ph("Event host or pastor testimonial")}</blockquote><figcaption>{ph("Name, church or organization")}</figcaption></figure>
</div>
</div>
</section>

<section class="section alt">
<div class="wrap split">
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/5Sk_Hm1As2k" title="Fight to Win Marriages on YouTube" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
<div><h2>Encouragement for your marriage, every week</h2><p>Follow Fight to Win Marriages on Instagram, TikTok and YouTube for prayers, teaching and real-talk encouragement for husbands and wives who are still believing.</p>
<div class="btns"><a class="btn" href="{IG}" target="_blank" rel="noopener">Follow on Instagram</a><a class="btn ghost" href="{YT}" target="_blank" rel="noopener">Watch on YouTube</a></div></div>
</div>
</section>
{faq_html(home_faq)}
{cta_band()}
'''
page("/", "Christian Marriage Coaching & Prayer | Fight to Win Marriages",
     "Faith-based marriage coaching with Terrie Beeman. Book a session, join the weekly Tuesday prayer and fasting call on Zoom, or invite Terrie to speak.",
     home, schema=[PERSON, faq_schema(home_faq)])

# ---------------------------------------------------------------- ABOUT
about = f'''
<section class="page-hero"><div class="wrap split">
<div><p class="eyebrow">About the founder</p><h1>Meet Terrie Beeman</h1>
<p class="lead">Certified Christian Counselor, Spiritual Life Coach, Marriage Coach, Motivator and Prayer Warrior, and founder of Fight to Win Marriages.</p></div>
<div class="portrait sm">{PORTRAIT.format(extra='')}</div>
</div></section>
<section class="section"><div class="wrap narrow prose">
<h2>Why Fight to Win Marriages exists</h2>
<p>Terrie Beeman started Fight to Win Marriages with one message: don't give up. Marriage is one of God's greatest institutions, and it is worth fighting for. Too many couples walk away from a covenant God can still heal. Through coaching, prayer and teaching, Terrie helps husbands and wives stop fighting each other and start fighting for each other.</p>
<p>The ministry is founded on 2 Corinthians 10:4 and Ephesians 6:12. Our battle is not against our spouse but against spiritual forces, and God has given us weapons with divine power to pull down strongholds. Fight to Win Marriages partners with God to equip husbands and wives with those weapons, along with biblical principles, prayer, encouragement and practical tools to build strong, healthy, God-centered marriages.</p>
<h2>Our vision</h2>
<p>To see marriages healed, healthy and whole, and to decrease the divorce rate in the body of believers. Terrie is committed to inspiring faith, restoring hope and putting marriages back on the map.</p>
<h2>Who we serve</h2>
<p>Married and engaged couples, individuals preparing for marriage, and anyone seeking healing, restoration, wisdom and biblical guidance for their marriage.</p>
<p>{ph("Terrie's story in her own words: how God led her into marriage ministry, her own marriage journey, years in ministry")}</p>
<h2>What Terrie believes about marriage</h2>
<ul class="checks">
<li>Marriage is a covenant, and God is in the business of restoration.</li>
<li>Your spouse is not your enemy. The battle is spiritual, and it is won in prayer.</li>
<li>Healing comes through honesty, forgiveness, faith and practical change.</li>
<li>No season is too late, whether you are newlyweds or married 40 years.</li>
</ul>
<h2>Credentials and ministry background</h2>
<ul class="checks">
<li>Certified Christian Counselor</li>
<li>Spiritual Life Coach</li>
<li>Marriage Coach</li>
<li>Motivator and speaker</li>
<li>Prayer Warrior and intercessor</li>
</ul>
<p>{ph("Certifying organization, years in ministry, church affiliation, media appearances")}</p>
<h2>A growing online community</h2>
<p>Fight to Win Marriages has become a faith-based relationship community across <a href="{IG}" target="_blank" rel="noopener">Instagram</a>, TikTok and <a href="{YT}" target="_blank" rel="noopener">YouTube</a>, where couples find daily encouragement to keep standing.</p>
</div></section>
{cta_band(title="Work with Terrie", text="Coaching, prayer and speaking for couples and churches.", primary=("/marriage-coaching/", "See Coaching Options"), secondary=("/events/", "Invite Terrie to Speak"))}
'''
page("/about/", "About Terrie Beeman, Christian Counselor & Marriage Coach | Fight to Win Marriages",
     "Meet Terrie Beeman, Certified Christian Counselor, marriage coach and prayer warrior who founded Fight to Win Marriages to help couples heal and fight for their marriage.",
     about, schema=[PERSON, {"@type": "AboutPage", "url": SITE + "/about/", "mainEntity": {"@id": f"{SITE}/#terrie"}}],
     og_type="profile", crumb=[("/", "Home"), ("/about/", "About Terrie Beeman")])

# ---------------------------------------------------------------- COACHING
coach_faq = [
    ("Is this Christian marriage counseling?", "Terrie is a Certified Christian Counselor and Marriage Coach. Sessions are faith-based coaching and Christian counseling, not licensed clinical therapy. Coaching uses biblical principles, prayer and practical tools to help you move forward. If you need clinical or crisis care, Terrie will encourage you to seek a licensed professional alongside coaching."),
    ("Can I do coaching if my spouse won't join?", "Yes. Many people begin coaching alone while standing for their marriage. Individual sessions focus on your heart, your prayer life and the changes you can make."),
    ("Are sessions online?", "Yes. Sessions are held online by video so couples anywhere can participate."),
    ("How much does marriage coaching cost?", "Pricing depends on the package. See the options on this page or request a free consultation to find the right fit."),
    ("Is what I share confidential?", "Yes. What you share in coaching stays private, except where safety or the law requires otherwise."),
]
coaching = f'''
<section class="page-hero"><div class="wrap">
<p class="eyebrow">Online &middot; Faith-based &middot; Couples and individuals</p>
<h1>Christian Marriage Coaching</h1>
<p class="lead">Biblical marriage coaching with Terrie Beeman for couples who want to heal, rebuild trust and grow closer to God and each other. Sessions are online, so you can join from anywhere.</p>
<div class="btns"><a class="btn gold" href="/contact/?type=coaching">Request a Free Consultation</a><a class="btn ghost" href="#packages">View Packages</a></div>
</div></section>

<section class="section"><div class="wrap">
<h2>Coaching that meets you where you are</h2>
<div class="cards three">
<div class="card"><h3>Marriage in crisis</h3><p>Infidelity, separation, talk of divorce, or a spouse who has checked out. Get a steady, prayer-covered plan for the next step.</p></div>
<div class="card"><h3>Stuck in conflict</h3><p>Same argument, different day. Learn to fight fair, listen well and attack the problem instead of each other.</p></div>
<div class="card"><h3>Standing alone</h3><p>When only one spouse is ready, individual coaching helps you stand in faith, guard your heart and keep your home covered in prayer.</p></div>
<div class="card"><h3>Newlyweds &amp; engaged</h3><p>Build on a biblical foundation from the start, with honest conversations about roles, money, intimacy and expectations.</p></div>
<div class="card"><h3>Long-married couples</h3><p>Empty nest, retirement or just drifting. Rekindle friendship and purpose for the years ahead.</p></div>
<div class="card"><h3>Blended families</h3><p>Navigate new roles, old wounds and co-parenting with grace and wisdom.</p></div>
</div></div></section>

<section class="section alt"><div class="wrap">
<h2>How coaching works</h2>
<ol class="steps">
<li><strong>Request a consultation.</strong> Tell Terrie a little about your marriage through the booking form.</li>
<li><strong>Free discovery call.</strong> A short call to pray, listen and recommend a path. {ph("confirm length, e.g. 20 minutes")}</li>
<li><strong>Coaching sessions.</strong> Scripture-based guidance, prayer and practical homework between sessions.</li>
<li><strong>Ongoing support.</strong> Join the Tuesday prayer call for weekly encouragement as you grow.</li>
</ol>
</div></section>

<section class="section" id="packages"><div class="wrap">
<h2 class="center">Coaching packages</h2>
<div class="cards three pricing">
<div class="card"><h3>Single Session</h3><p class="price">{ph("$ price")}</p><p>{ph("Session length")} online session for an individual or couple. Good for a specific issue or a first step.</p><a class="btn" href="/contact/?type=coaching">Book a Session</a></div>
<div class="card featured"><h3>Restoration Package</h3><p class="price">{ph("$ price")}</p><p>{ph("Number of sessions")} sessions for couples committed to rebuilding, with prayer support between sessions.</p><a class="btn gold" href="/contact/?type=coaching">Start Restoration</a></div>
<div class="card"><h3>Standing Spouse Package</h3><p class="price">{ph("$ price")}</p><p>{ph("Number of sessions")} individual sessions for the spouse standing for their marriage.</p><a class="btn" href="/contact/?type=coaching">Get Support</a></div>
</div>
<p class="center micro">{ph("Confirm package names, pricing, payment method and scheduling link (Calendly, Acuity, etc.)")}</p>
</div></section>
{faq_html(coach_faq, "Marriage Coaching FAQ")}
{cta_band(title="Your marriage can be restored.", text="Take the first step today. A free consultation is the easiest place to start.", primary=("/contact/?type=coaching", "Request a Free Consultation"))}
'''
coach_service = {"@type": "Service", "name": "Christian Marriage Coaching", "serviceType": "Marriage coaching",
                 "provider": {"@id": f"{SITE}/#org"}, "areaServed": {"@type": "Country", "name": "United States"},
                 "availableChannel": {"@type": "ServiceChannel", "serviceUrl": SITE + "/marriage-coaching/"},
                 "description": "Online biblical marriage coaching for couples and individuals with Terrie Beeman."}
page("/marriage-coaching/", "Christian Marriage Coaching Online | Fight to Win Marriages",
     "Online Christian marriage coaching with Terrie Beeman. Faith-based help for conflict, broken trust, separation and couples who want to grow. Book a free consult.",
     coaching, schema=[coach_service, faq_schema(coach_faq)], crumb=[("/", "Home"), ("/marriage-coaching/", "Marriage Coaching")])

# ---------------------------------------------------------------- TUESDAY CALL
tue_faq = [
    ("Is the Tuesday prayer call free?", f"The call is open to couples and individuals who want prayer for their marriage. Join on Zoom every Tuesday at {TUE_TIME} using the link on this page, meeting ID {ZOOM_ID}."),
    ("Do both spouses need to attend?", "No. Come together or come alone. Many people join while standing in prayer for a spouse who is not ready yet."),
    ("Do I have to fast to join?", "No. Terrie prays and fasts for the marriages on the call. You are welcome to fast with her as you feel led, but it is not required to attend."),
    ("Do I have to be on camera or speak?", "No. You can listen, pray along and type requests privately if you prefer."),
    ("Can I submit a prayer request if I can't attend?", "Yes. Use the prayer request form on this page and Terrie will lift your marriage up in prayer."),
]
tuesday = f'''
<section class="page-hero"><div class="wrap">
<p class="eyebrow">Every Tuesday &middot; Live on Zoom &middot; All couples welcome</p>
<h1>Tuesday Marriage Prayer &amp; Fasting Call</h1>
<p class="lead">Each Tuesday, Terrie Beeman prays and fasts for marriages and hosts a live online Zoom call offering biblical guidance to couples, young and old. Come pray, be encouraged and stand with others who are believing God for their marriage.</p>
<div class="when"><div><span>Day</span><strong>Every Tuesday</strong></div><div><span>Time</span><strong>{TUE_TIME}</strong></div><div><span>Where</span><strong>Zoom &middot; ID {ZOOM_ID}</strong></div><div><span>Cost</span><strong>{ph("Free / love offering")}</strong></div></div>
<div class="btns"><a class="btn gold" href="{ZOOM}" target="_blank" rel="noopener">Join on Zoom</a><a class="btn ghost" href="#register">Get Weekly Reminders</a><a class="btn ghost" href="#prayer-request">Send a Prayer Request</a></div>
</div></section>

<section class="section"><div class="wrap split">
<div class="prose">
<h2>What happens on the call</h2>
<ul class="checks">
<li><strong>Corporate prayer</strong> over marriages, homes and families.</li>
<li><strong>A word of encouragement</strong> from Scripture for the week ahead.</li>
<li><strong>Biblical guidance</strong> for real questions couples are facing.</li>
<li><strong>Prayer requests</strong> lifted up by name, as you are comfortable.</li>
</ul>
<h2>Why prayer and fasting?</h2>
<p>Some battles are only won on our knees. Fasting humbles the heart and sharpens our focus on God. Terrie fasts each Tuesday for the couples on the call, so you never have to stand alone.</p>
</div>
<blockquote class="verse">"Again, truly I tell you that if two of you on earth agree about anything they ask for, it will be done for them by my Father in heaven."<cite>Matthew 18:19</cite></blockquote>
</div></section>

<section class="section alt" id="register"><div class="wrap narrow">
<h2>Get weekly reminders</h2>
<p>Join anytime with the <a href="{ZOOM}" target="_blank" rel="noopener">Zoom link</a> (meeting ID {ZOOM_ID}) every Tuesday at {TUE_TIME}. Add your name below and we'll send you a reminder each week.</p>
<form name="tuesday-registration" method="POST" data-netlify="true" netlify-honeypot="company" action="/thank-you/" class="form">
<input type="hidden" name="form-name" value="tuesday-registration">
<p class="hp"><label>Leave blank <input name="company"></label></p>
<div class="row"><label>First and last name<input name="name" required autocomplete="name"></label><label>Email<input type="email" name="email" required autocomplete="email"></label></div>
<label>Joining as<select name="joining_as"><option>A couple</option><option>A wife</option><option>A husband</option><option>Engaged</option></select></label>
<label class="check"><input type="checkbox" name="reminders" value="yes" checked> Send me weekly reminders</label>
<button class="btn gold" type="submit">Send Me Reminders</button>
</form>
</div></section>

<section class="section" id="prayer-request"><div class="wrap narrow">
<h2>Can't make it? Send a prayer request</h2>
<form name="prayer-request" method="POST" data-netlify="true" netlify-honeypot="company" action="/thank-you/" class="form">
<input type="hidden" name="form-name" value="prayer-request">
<p class="hp"><label>Leave blank <input name="company"></label></p>
<div class="row"><label>First name<input name="name" autocomplete="given-name"></label><label>Email (optional)<input type="email" name="email" autocomplete="email"></label></div>
<label>Your prayer request<textarea name="request" rows="5" required></textarea></label>
<button class="btn" type="submit">Send Prayer Request</button>
</form>
</div></section>
{faq_html(tue_faq, "Tuesday Prayer Call FAQ")}
{cta_band(title="Want more than one night a week?", text="Personal coaching gives you a plan and a coach in your corner.", primary=("/marriage-coaching/", "Explore Coaching"), secondary=("/contact/", "Contact Terrie"))}
'''
tue_service = {"@type": "Service", "name": "Tuesday Marriage Prayer and Fasting Call", "serviceType": "Online marriage prayer meeting",
               "provider": {"@id": f"{SITE}/#org"}, "availableChannel": {"@type": "ServiceChannel", "serviceUrl": SITE + "/tuesday-prayer-call/"},
               "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": "https://schema.org/Tuesday", "opens": "18:00"},
               "description": "Weekly online Zoom call where Terrie Beeman prays, fasts and offers biblical guidance to couples."}
tue_event = {"@type": "Event", "name": "Fight to Win Marriages Tuesday Prayer & Fasting Call",
             "description": "Weekly online marriage prayer and fasting call on Zoom with Terrie Beeman, offering prayer, Scripture and biblical guidance to couples young and old.",
             "startDate": "2026-10-20T18:00:00-05:00",
             "eventSchedule": {"@type": "Schedule", "repeatFrequency": "P1W", "byDay": "https://schema.org/Tuesday",
                               "startTime": "18:00", "scheduleTimezone": "America/Chicago"},
             "eventStatus": "https://schema.org/EventScheduled",
             "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
             "location": {"@type": "VirtualLocation", "url": ZOOM},
             "image": f"{SITE}/assets/og-image.jpg",
             "organizer": {"@id": f"{SITE}/#org"}, "performer": {"@id": f"{SITE}/#terrie"}}
page("/tuesday-prayer-call/", "Online Marriage Prayer Call Every Tuesday | Fight to Win Marriages",
     "Join Terrie Beeman's marriage prayer and fasting call on Zoom every Tuesday at 6 PM CT. Prayer, Scripture and biblical guidance for couples young and old.",
     tuesday, schema=[tue_service, tue_event, faq_schema(tue_faq)], crumb=[("/", "Home"), ("/tuesday-prayer-call/", "Tuesday Prayer Call")])

# ---------------------------------------------------------------- EVENTS
ev_faq = [
    ("What topics does Terrie speak on?", "Topics include fighting for your marriage, restoration after betrayal, praying for your spouse, covenant marriage, and strengthening marriages in the church."),
    ("Does Terrie travel for events?", "Yes. Terrie speaks in person and virtually. Share your location and date in the booking form for availability and travel details."),
    ("What size events does Terrie speak at?", "From small church couples' nights to conferences and retreats. Each message is tailored to the audience."),
]
events = f'''
<section class="page-hero"><div class="wrap">
<p class="eyebrow">Upcoming events &middot; Church &amp; conference speaking</p>
<h1>Marriage Events &amp; Speaking</h1>
<p class="lead">Join Terrie Beeman at an upcoming marriage event, or invite her to bring a message of hope, healing and covenant love to your church, couples retreat or conference.</p>
<div class="btns"><a class="btn gold" href="/contact/?type=speaking">Invite Terrie to Speak</a><a class="btn ghost" href="#upcoming">See Upcoming Events</a></div>
</div></section>

<section class="section" id="upcoming"><div class="wrap">
<h2>Upcoming events</h2>
<div class="events">
<article class="event"><div class="date"><span>{ph("Mon")}</span><strong>{ph("DD")}</strong></div><div><h3>{ph("Event name, e.g. Fight to Win Couples Night")}</h3><p>{ph("City, venue or Online")} &middot; {ph("Time")}</p><p>{ph("One-sentence description")}</p></div><a class="btn small" href="/contact/">Register</a></article>
<article class="event"><div class="date"><span>Every</span><strong>Tue</strong></div><div><h3>Tuesday Marriage Prayer &amp; Fasting Call</h3><p>Online via Zoom &middot; {TUE_TIME}</p><p>Weekly prayer, Scripture and biblical guidance for couples.</p></div><a class="btn small" href="/tuesday-prayer-call/">Details</a></article>
</div>
<p class="micro">{ph("Add each confirmed event with date, location and registration link. Event schema will be added per event once dates are confirmed.")}</p>
</div></section>

<section class="section alt"><div class="wrap">
<h2>Book Terrie to speak</h2>
<p>Terrie brings warmth, honesty and a deep prayer life to every stage. Messages are rooted in Scripture and practical enough for couples to use the same night.</p>
<div class="cards three">
<div class="card"><h3>Fight to Win</h3><p>Your spouse is not the enemy. How couples team up against the real battle and win together.</p></div>
<div class="card"><h3>Restoration Is Possible</h3><p>Hope and next steps for marriages facing betrayal, separation or years of distance.</p></div>
<div class="card"><h3>Praying for Your Marriage</h3><p>How prayer and fasting change hearts, homes and generations.</p></div>
</div>
<h3>Great fit for</h3>
<ul class="tags"><li>Church marriage ministries</li><li>Couples retreats</li><li>Women's conferences</li><li>Valentine's &amp; anniversary events</li><li>Marriage enrichment weekends</li><li>Virtual events &amp; podcasts</li></ul>
<p>{ph("Speaker one-sheet PDF, past venues, honorarium range")}</p>
<a class="btn gold" href="/contact/?type=speaking">Request Terrie for Your Event</a>
</div></section>
{faq_html(ev_faq, "Speaking FAQ")}
{cta_band(title="Bring Fight to Win to your church.", text="Share your date and audience, and Terrie's team will follow up.", primary=("/contact/?type=speaking", "Book Terrie to Speak"))}
'''
page("/events/", "Christian Marriage Events & Speaker Booking | Fight to Win Marriages",
     "See upcoming Fight to Win Marriages events and book Terrie Beeman to speak at your church, couples retreat, women's conference or marriage ministry event.",
     events, schema=[faq_schema(ev_faq)], crumb=[("/", "Home"), ("/events/", "Events & Speaking")])

# ---------------------------------------------------------------- CONTACT
contact = f'''
<section class="page-hero"><div class="wrap">
<h1>Book Terrie or Get in Touch</h1>
<p class="lead">Request marriage coaching, invite Terrie to speak, or ask about the Tuesday prayer call. You'll hear back within {ph("response time, e.g. 2 business days")}.</p>
</div></section>
<section class="section"><div class="wrap split">
<form name="booking" method="POST" data-netlify="true" netlify-honeypot="company" action="/thank-you/" class="form">
<input type="hidden" name="form-name" value="booking">
<p class="hp"><label>Leave blank <input name="company"></label></p>
<label>I'm interested in<select name="type" id="type"><option value="coaching">Marriage coaching</option><option value="speaking">Booking Terrie for an event or speaking</option><option value="tuesday">Tuesday prayer call</option><option value="other">Something else</option></select></label>
<div class="row"><label>Name<input name="name" required autocomplete="name"></label><label>Email<input type="email" name="email" required autocomplete="email"></label></div>
<div class="row"><label>Phone (optional)<input type="tel" name="phone" autocomplete="tel"></label><label>Event date (if speaking)<input type="date" name="event_date"></label></div>
<label>Church, organization or event location (if speaking)<input name="organization"></label>
<label>How can Terrie help?<textarea name="message" rows="6" required></textarea></label>
<button class="btn gold" type="submit">Send Request</button>
</form>
<aside class="card">
<h2>Other ways to connect</h2>
<p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><strong>Scheduling:</strong> {ph("Calendly or booking link")}</p>
<p><strong>Instagram:</strong> <a href="{IG}" target="_blank" rel="noopener">@fighttowinmarriages</a></p>
<p><strong>YouTube:</strong> <a href="{YT}" target="_blank" rel="noopener">Fight to Win Marriages</a></p>
<p class="micro">If you or your children are in danger, call 911 or the National Domestic Violence Hotline at 1-800-799-7233.</p>
</aside>
</div></section>
<script>const t=new URLSearchParams(location.search).get('type');if(t)document.getElementById('type').value=t;</script>
'''
page("/contact/", "Book Marriage Coaching or Speaking | Fight to Win Marriages",
     "Contact Terrie Beeman to book Christian marriage coaching, schedule a speaking engagement, or join the Tuesday marriage prayer call.",
     contact, schema=[{"@type": "ContactPage", "url": SITE + "/contact/"}], crumb=[("/", "Home"), ("/contact/", "Contact")])

# ---------------------------------------------------------------- BLOG
POSTS = [
    {
        "slug": "how-to-fight-for-your-marriage",
        "title": "How to Fight for Your Marriage (Without Fighting Your Spouse)",
        "seo_title": "How to Fight for Your Marriage: 5 Biblical Steps | Fight to Win Marriages",
        "desc": "Fighting for your marriage means fighting the problem, not your spouse. Five biblical steps to stand together, pray and rebuild when your marriage is hurting.",
        "date": "2026-10-19",
        "excerpt": "Your spouse is not the enemy. Here's how to team up against the real battle and fight for your marriage God's way.",
        "body": """
<p>When a marriage is hurting, it is easy to start keeping score. Who said what. Who started it. Who is more wrong. But winning an argument and winning your marriage are two very different things. Fighting for your marriage means you stop fighting each other and start fighting <em>for</em> each other.</p>
<h2>1. Remember who the real enemy is</h2>
<p>"For our struggle is not against flesh and blood" (Ephesians 6:12). Stress, exhaustion, old wounds and spiritual opposition all show up in the kitchen as an argument about the dishes. Name the real battle, and you can face it together.</p>
<h2>2. Attack the problem, not the person</h2>
<p>Street fighting has no rules: name-calling, bringing up the past, threatening divorce. Set ground rules together. Use "I feel" statements, keep conflict away from the children, and agree that either spouse can call a cool-off break when tempers rise.</p>
<h2>3. Look for the win-win</h2>
<p>If one of you wins and the other loses, the marriage loses. Ask, "What would a good outcome look like for both of us?" Real resolution takes listening, yielding and humility from both sides.</p>
<h2>4. Pray for your spouse, not just about them</h2>
<p>It is hard to stay bitter toward someone you are praying blessing over. Pray for your spouse's heart, health, purpose and walk with God. Then pray for your own heart to soften.</p>
<h2>5. Don't fight alone</h2>
<p>Couples who make it through hard seasons rarely do it in isolation. Invite prayer partners, a coach or a trusted pastor into the battle. That is exactly why Terrie hosts the <a href="/tuesday-prayer-call/">Tuesday marriage prayer and fasting call</a>.</p>
<h2>Ready for help?</h2>
<p>If your marriage needs more than a few tips, <a href="/marriage-coaching/">Christian marriage coaching</a> gives you a plan and a coach in your corner.</p>
""",
    },
    {
        "slug": "praying-and-fasting-for-your-marriage",
        "title": "Praying and Fasting for Your Marriage: A Simple Guide",
        "seo_title": "Praying and Fasting for Your Marriage: A Simple Guide | Fight to Win Marriages",
        "desc": "A practical guide to praying and fasting for your marriage: how to start, what to pray, Scriptures to stand on, and how to fast safely and with purpose.",
        "date": "2026-10-19",
        "excerpt": "Some breakthroughs only come through prayer and fasting. Here's how to start, what to pray, and Scriptures to stand on.",
        "body": """
<p>Prayer invites God into your marriage. Fasting quiets everything else so you can hear Him. Together they are one of the most powerful things a spouse can do when a marriage needs a breakthrough.</p>
<h2>Why fast for your marriage?</h2>
<p>Fasting is not a way to earn God's favor or force your spouse to change. It humbles your heart, sharpens your focus and says, "Lord, this matters more to me than food." Jesus said some things come out "only by prayer and fasting."</p>
<h2>How to start</h2>
<ul>
<li><strong>Choose a simple fast.</strong> Skip one meal, fast from sunup to sundown, or give up something like social media or TV for the day.</li>
<li><strong>Set a clear focus.</strong> Write down what you are believing God for in your marriage.</li>
<li><strong>Replace the meal with prayer.</strong> Use the time you would spend eating to pray and read Scripture.</li>
<li><strong>Be wise.</strong> If you are pregnant, nursing, diabetic or on medication, talk to your doctor first and choose a non-food fast.</li>
</ul>
<h2>What to pray</h2>
<ul>
<li>For unity and a soft heart in both of you.</li>
<li>For healing of past wounds and broken trust.</li>
<li>For protection over your home, children and covenant.</li>
<li>For wisdom to know your part, and grace to do it.</li>
</ul>
<h2>Scriptures to stand on</h2>
<p>Mark 10:9. Ecclesiastes 4:12. Ephesians 4:31-32. 1 Corinthians 13:4-7. Matthew 18:19.</p>
<h2>You don't have to fast alone</h2>
<p>Every Tuesday, Terrie Beeman prays and fasts for marriages and leads a live <a href="/tuesday-prayer-call/">marriage prayer call on Zoom</a>. Join her and stand with other couples who are believing God.</p>
""",
    },
    {
        "slug": "signs-your-marriage-needs-a-coach",
        "title": "7 Signs Your Marriage Could Use a Christian Marriage Coach",
        "seo_title": "7 Signs You Need a Christian Marriage Coach | Fight to Win Marriages",
        "desc": "Same fight on repeat? Feeling like roommates? Seven signs your marriage could benefit from Christian marriage coaching, and what coaching looks like.",
        "date": "2026-10-19",
        "excerpt": "Same fight on repeat? Feeling more like roommates than partners? These are signs it may be time to bring in a coach.",
        "body": """
<p>Asking for help is not a sign your marriage is failing. It is a sign you are serious about winning. Here are seven signs a Christian marriage coach could help.</p>
<h2>1. You keep having the same argument</h2><p>The topic changes, but the pattern doesn't. A coach helps you see the cycle and break it.</p>
<h2>2. You feel more like roommates than partners</h2><p>Busy schedules, kids and careers can slowly push intimacy and friendship aside.</p>
<h2>3. Trust has been broken</h2><p>Infidelity, secrets, or financial betrayal need a guided path to rebuild, not just time.</p>
<h2>4. One of you has mentioned divorce</h2><p>That word changes the atmosphere of a home. Get support before decisions are made in pain.</p>
<h2>5. You're standing alone</h2><p>If your spouse isn't ready, you can still get coaching for yourself and keep your marriage covered in prayer.</p>
<h2>6. You're entering a new season</h2><p>Newlyweds, new babies, empty nests and blended families all bring new pressures.</p>
<h2>7. You've stopped praying together</h2><p>Spiritual distance often comes before emotional distance.</p>
<h2>What coaching with Terrie looks like</h2>
<p><a href="/marriage-coaching/">Fight to Win marriage coaching</a> is online, rooted in Scripture and practical. It is not a replacement for licensed counseling, but it gives couples prayer, perspective and a plan. <a href="/contact/?type=coaching">Request a free consultation</a> to get started.</p>
""",
    },
]

def author_box():
    return f'''<aside class="author card"><div class="portrait xs">{PORTRAIT.format(extra='loading="lazy"')}</div><div><p class="eyebrow">Written by</p><h2><a href="/about/">Terrie Beeman</a></h2><p>Certified Christian Counselor, marriage coach, prayer warrior and founder of Fight to Win Marriages. Terrie hosts a weekly Tuesday prayer and fasting call for couples.</p></div></aside>'''

cards = ""
for p in POSTS:
    u = f"/blog/{p['slug']}/"
    cards += f'<article class="card post"><p class="micro"><time datetime="{p["date"]}">October 19, 2026</time></p><h2><a href="{u}">{html.escape(p["title"])}</a></h2><p>{html.escape(p["excerpt"])}</p><a class="link" href="{u}">Read more &rarr;</a></article>'
    others = "".join(f'<li><a href="/blog/{o["slug"]}/">{html.escape(o["title"])}</a></li>' for o in POSTS if o is not p)
    body = f'''
<article class="section"><div class="wrap narrow prose">
<p class="eyebrow">Marriage Blog</p>
<h1>{html.escape(p["title"])}</h1>
<p class="meta">By <a href="/about/">Terrie Beeman</a> &middot; <time datetime="{p["date"]}">October 19, 2026</time></p>
{p["body"]}
{author_box()}
<h2>Keep reading</h2><ul>{others}</ul>
</div></article>
{cta_band()}
'''
    page(u, p["seo_title"], p["desc"], body, og_type="article",
         schema=[{"@type": "BlogPosting", "headline": p["title"], "description": p["desc"], "datePublished": p["date"], "dateModified": p["date"],
                  "author": {"@id": f"{SITE}/#terrie"}, "publisher": {"@id": f"{SITE}/#org"}, "image": f"{SITE}/assets/og-image.jpg",
                  "mainEntityOfPage": SITE + u}, PERSON],
         crumb=[("/", "Home"), ("/blog/", "Blog"), (u, p["title"])])

blog = f'''
<section class="page-hero"><div class="wrap">
<h1>Marriage Blog: Faith, Prayer &amp; Restoration</h1>
<p class="lead">Biblical encouragement and practical help for couples who are fighting for their marriage, from Terrie Beeman.</p>
</div></section>
<section class="section"><div class="wrap"><div class="cards three">{cards}</div></div></section>
{cta_band()}
'''
page("/blog/", "Christian Marriage Blog | Fight to Win Marriages",
     "Biblical marriage advice from Terrie Beeman: how to fight for your marriage, praying and fasting for your spouse, rebuilding trust and restoration.",
     blog, schema=[{"@type": "Blog", "name": "Fight to Win Marriages Blog", "url": SITE + "/blog/", "publisher": {"@id": f"{SITE}/#org"}}],
     crumb=[("/", "Home"), ("/blog/", "Blog")])

# ---------------------------------------------------------------- UTILITY PAGES
page("/thank-you/", "Thank You | Fight to Win Marriages", "Thank you for reaching out to Fight to Win Marriages.",
     '<section class="page-hero"><div class="wrap narrow"><h1>Thank you. We received your message.</h1><p class="lead">Terrie or a member of her team will follow up soon. In the meantime, join the <a href="/tuesday-prayer-call/">Tuesday prayer call</a> or read the <a href="/blog/">marriage blog</a>.</p></div></section>')
page("/privacy/", "Privacy Policy | Fight to Win Marriages", "Privacy policy for Fight to Win Marriages.",
     f'<section class="section"><div class="wrap narrow prose"><h1>Privacy Policy</h1><p>Fight to Win Marriages collects the information you submit through forms on this site (such as your name, email and message) only to respond to you and provide the services you request. We do not sell your information.</p><p>Questions about your information? Email <a href="mailto:{EMAIL}">{EMAIL}</a>. {ph("Full privacy policy text and analytics disclosure")}</p></div></section>',
     crumb=[("/", "Home"), ("/privacy/", "Privacy Policy")])

# 404
page("/404.html", "Page Not Found | Fight to Win Marriages", "Page not found.",
     '<section class="page-hero"><div class="wrap narrow"><h1>Page not found</h1><p class="lead">Don\'t give up. Try the <a href="/">home page</a>, <a href="/marriage-coaching/">coaching</a> or the <a href="/blog/">blog</a>.</p></div></section>')

# sitemap + robots
urls = ["/", "/about/", "/marriage-coaching/", "/tuesday-prayer-call/", "/events/", "/blog/", "/contact/", "/privacy/"] + [f"/blog/{p['slug']}/" for p in POSTS]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{SITE}{u}</loc><lastmod>2026-10-19</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nDisallow: /thank-you/\n\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(urls), "indexable urls")
