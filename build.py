#!/usr/bin/env python3
"""Static site generator for fighttowinmarriages (Netlify). Run: python3 build.py"""
import json, os, html

SITE = "https://fight-to-win-marriages.netlify.app"  # TODO: swap to custom domain when purchased
OUT = os.path.join(os.path.dirname(__file__), "site")
NAME = "Fight to Win Marriages"
IG = "https://www.instagram.com/fighttowinmarriages/"
YT = "https://www.youtube.com/@FIGHTTOWINMARRIAGES"
YT_STORY = "https://www.youtube.com/watch?v=5Sk_Hm1As2k"
VIDEO_TESTIMONY_ONE = "https://drive.google.com/file/d/14QjXP1ye4KxoWnmos3_v8D8_fVchgCz-/view"
VIDEO_TESTIMONY_TWO = "https://drive.google.com/file/d/1FLaKGGMrJsxTYR0NFuTxW_iGpyC1CmQ5/view"
CALENDLY = "https://calendly.com/fighttowinmarriages/30min"
NOTES_PDF = "/assets/notes/fight-to-win-marriages-2026-10-20-spiritual-heart-check.pdf"
EMAIL = "fighttowinmarriages@gmail.com"
ZOOM = "https://us02web.zoom.us/j/84083347510"
ZOOM_ID = "840 8334 7510"
TUE_TIME = "6:00 PM CT"
TT = "https://www.tiktok.com/@fight.to.win.marr"
SOCIAL_ICONS = f'<div class="social-icons"><a href="{YT}" target="_blank" rel="noopener" aria-label="Fight to Win Marriages on YouTube" title="YouTube"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a><a href="{IG}" target="_blank" rel="noopener" aria-label="Fight to Win Marriages on Instagram" title="Instagram"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"/></svg></a><a href="{TT}" target="_blank" rel="noopener" aria-label="Fight to Win Marriages on TikTok" title="TikTok"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg></a></div>'
SAME_AS = [u for u in (IG, TT, YT) if u]

NAV = [
    ("/", "Home"),
    ("/about/", "About Terrie"),
    ("/marriage-coaching/", "Coaching"),
    ("/tuesday-prayer-call/", "Tuesday Prayer Call"),
    ("/events/", "Events & Speaking"),
    ("/testimonials/", "Testimonials"),
    ("/blog/", "Blog"),
]

RELATED = {
    "/": [
        ("/marriage-coaching/", "Christian marriage coaching", "Get faith-based support for conflict, trust, communication and restoration."),
        ("/tuesday-prayer-call/", "Tuesday prayer call", "Join couples online each Tuesday for free prayer, Scripture and encouragement."),
        ("/blog/", "Marriage encouragement", "Read practical, biblical guidance for fighting for your marriage."),
    ],
    "/about/": [
        ("/marriage-coaching/", "Work with Terrie", "Explore online coaching for couples and individuals."),
        ("/events/", "Invite Terrie to speak", "Bring a message of marriage restoration to your church or event."),
        ("/testimonials/", "Read marriage testimonies", "Hear from couples and individuals strengthened by prayer, teaching and community."),
    ],
    "/marriage-coaching/": [
        ("/about/#story", "Read Terrie's restoration story", "See how a 365-day spiritual battle became a marriage ministry."),
        ("/tuesday-prayer-call/", "Join the free prayer call", "Find weekly encouragement while you work on your marriage."),
        ("/contact/?type=coaching", "Request a consultation", "Tell Terrie what your marriage needs and take the next step."),
    ],
    "/tuesday-prayer-call/": [
        ("/prayer-call-notes/", "Download weekly call notes", "Review and download edited recaps from Tuesday prayer and teaching calls."),
        ("/blog/praying-and-fasting-for-your-marriage/", "Learn to pray and fast", "Prepare for the call with a practical biblical guide."),
        ("/marriage-coaching/", "Explore marriage coaching", "Get personal support beyond the weekly group call."),
    ],
    "/prayer-call-notes/": [
        ("/tuesday-prayer-call/", "Join the Tuesday prayer call", "Join the free weekly Zoom gathering for prayer, Scripture and encouragement."),
        ("/blog/", "Read marriage resources", "Explore more biblical encouragement and practical guidance for your marriage."),
        ("/contact/", "Send a prayer request", "Share what you want Terrie and the ministry to pray over."),
    ],
    "/events/": [
        ("/about/", "Meet Terrie Beeman", "Learn about her testimony, credentials and ministry."),
        ("/contact/?type=speaking", "Request Terrie for an event", "Share your church, retreat or conference details."),
        ("/marriage-coaching/", "Marriage coaching", "Discover another way Fight to Win serves couples."),
    ],
    "/testimonials/": [
        ("/about/", "Meet Terrie Beeman", "Learn about the testimony and calling behind Fight to Win Marriages."),
        ("/tuesday-prayer-call/", "Join the Tuesday prayer call", "Pray and stand with other couples in a free weekly online gathering."),
        ("/marriage-coaching/", "Explore marriage coaching", "Get faith-based support for your marriage and your next step."),
    ],
    "/contact/": [
        ("/marriage-coaching/", "Review coaching options", "See who coaching helps and what to expect."),
        ("/tuesday-prayer-call/", "Join Tuesday prayer", "Attend the free weekly Zoom call for couples and individuals."),
        ("/events/", "Speaking and events", "Learn about Terrie's marriage ministry messages and gatherings."),
    ],
    "/blog/": [
        ("/blog/how-to-fight-for-your-marriage/", "How to fight for your marriage", "Learn to face the problem as a team."),
        ("/blog/praying-and-fasting-for-your-marriage/", "Praying and fasting for marriage", "Build a focused prayer practice for your home."),
        ("/marriage-coaching/", "Get personal support", "Pair biblical encouragement with one-on-one marriage coaching."),
    ],
}

def related_links(path):
    """Contextual internal links for visitors and search engines."""
    if path in ("/thank-you/", "/privacy/", "/404.html"):
        return ""
    links = RELATED.get(path)
    if links is None and path.startswith("/blog/"):
        links = [
            ("/blog/", "More marriage resources", "Explore biblical articles about prayer, conflict, trust and restoration."),
            ("/tuesday-prayer-call/", "Pray with us on Tuesday", "Join the free weekly marriage prayer and fasting call."),
            ("/marriage-coaching/", "Explore marriage coaching", "Get faith-based guidance for your specific season."),
        ]
    if not links:
        return ""
    cards = "".join(
        f'<article class="related-card"><h3><a href="{url}">{html.escape(label)}</a></h3><p>{html.escape(text)}</p></article>'
        for url, label, text in links
    )
    return f'''<section class="section related" aria-labelledby="related-heading"><div class="wrap">
<p class="eyebrow">Keep exploring</p><h2 id="related-heading">Marriage help and encouragement</h2>
<div class="related-grid">{cards}</div>
</div></section>'''

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
    "areaServed": [{"@type": "City", "name": "Houston, TX"}, {"@type": "Country", "name": "United States"}],
    "image": [f"{SITE}/assets/photos/kingdom-kouples-small-group-houston.jpg", f"{SITE}/assets/photos/terrie-beeman-teaching-marriage-small-group.jpg"],
    "sameAs": SAME_AS,
}
PERSON = {
    "@type": "Person",
    "@id": f"{SITE}/#terrie",
    "name": "Terrie Beeman",
    "jobTitle": "Certified Christian Counselor and Marriage Coach",
    "description": "Terrie Beeman is a Certified Christian Counselor, Spiritual Life Coach, Marriage Coach, Motivator and Prayer Warrior. She is the founder of TBee Ministries Inc. and Fight to Win Marriages, the creator of Power Talks with Terrie, and the owner of Blessed Income Tax Service Inc.",
    "email": EMAIL,
    "image": f"{SITE}/assets/terrie-beeman.jpg",
    "url": f"{SITE}/about/",
    "worksFor": {"@id": f"{SITE}/#org"},
    "sameAs": SAME_AS,
    "knowsAbout": ["Christian marriage coaching", "Marriage restoration", "Prayer and fasting for marriage", "Biblical marriage", "Spiritual warfare prayer", "Christian counseling", "Spiritual life coaching", "Women's empowerment", "Premarital coaching"],
}
TOMEKA = {
    "@type": "Person",
    "@id": f"{SITE}/about/#tomeka-jones",
    "name": "Tomeka Jones",
    "jobTitle": "Personal Assistant, Prayer Warrior and Intercessor",
    "description": "Tomeka Jones serves Fight to Win Marriages as Terrie Beeman's personal assistant, a prayer warrior and an intercessor standing for wives, marriages and covenant restoration.",
    "url": f"{SITE}/about/#tomeka-jones",
    "worksFor": {"@id": f"{SITE}/#org"},
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
    primary_attrs = ' target="_blank" rel="noopener"' if primary[0].startswith("http") else ""
    secondary_attrs = ' target="_blank" rel="noopener"' if secondary[0].startswith("http") else ""
    return f'''<section class="cta-band"><div class="wrap">
<h2>{title}</h2><p>{text}</p>
<div class="btns"><a class="btn gold" href="{primary[0]}"{primary_attrs}>{primary[1]}</a><a class="btn ghost-light" href="{secondary[0]}"{secondary_attrs}>{secondary[1]}</a></div>
</div></section>'''

def page(path, title, desc, body, schema=None, og_type="website", crumb=None):
    url = SITE + path
    graph = [ORG, WEBSITE]
    share_image = f"{SITE}/assets/photos/happy-black-couple-hero-og.jpg" if path == "/" else f"{SITE}/assets/og-image.jpg"
    share_alt = "A joyful Black married couple relaxing together at home" if path == "/" else "Fight to Win Marriages"
    graph.append({
        "@type": "CollectionPage" if path == "/blog/" else "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        "name": title,
        "description": desc,
        "inLanguage": "en-US",
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": {"@id": f"{SITE}/#org"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": share_image},
    })
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
<meta name="author" content="Terrie Beeman">
<meta name="application-name" content="{NAME}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<link rel="canonical" href="{url}">
<meta name="robots" content="{'noindex, follow' if path in ('/thank-you/', '/404.html') else 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{share_image}">
<meta property="og:image:secure_url" content="{share_image}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="{html.escape(share_alt)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{share_image}">
<meta name="twitter:image:alt" content="{html.escape(share_alt)}">
<meta name="theme-color" content="#4a1d3a">
<meta name="color-scheme" content="light">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css?v=20261023-mobile-fit-2">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap bar">
<a class="brand" href="/" aria-label="{NAME} home"><span>Fight to Win <em>Marriages</em></span></a>
{SOCIAL_ICONS}
<button class="menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span class="menu-icon" aria-hidden="true">&#9776;</span><span class="menu-label"> Menu</span></button>
<nav id="nav" aria-label="Main"><ul>{nav}</ul><a class="btn gold small" href="{CALENDLY}" target="_blank" rel="noopener">Book a Meeting</a></nav>
</div>
</header>
{bc}
<main id="main">
{body}
{related_links(path)}
</main>
<footer class="site-footer">
<div class="wrap cols">
<div><p class="brand foot"><span class="mark" aria-hidden="true">&#10084;</span> Fight to Win Marriages</p>
<p>We don't give up on marriage. We fight in prayer, love &amp; faith. A God-filled space for healing, restoration, and standing on God's promises together.</p>
<p class="social"><a href="{IG}" rel="noopener" target="_blank">Instagram</a> · {f'<a href="{TT}" rel="noopener" target="_blank">TikTok</a> · ' if TT else ''}<a href="{YT}" rel="noopener" target="_blank">YouTube</a></p></div>
<div><h3>Ministry</h3><ul><li><a href="/marriage-coaching/">Christian Marriage Coaching</a></li><li><a href="/tuesday-prayer-call/">Tuesday Prayer &amp; Fasting Call</a></li><li><a href="/prayer-call-notes/">Tuesday Call Notes</a></li><li><a href="/events/">Marriage Events &amp; Speaking</a></li><li><a href="/blog/">Marriage Blog</a></li></ul></div>
<div><h3>Connect</h3><ul><li><a href="/about/">About Terrie Beeman</a></li><li><a href="/contact/">Book or Contact</a></li><li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
</div>
<div class="wrap legal"><p>&copy; 2026 Fight to Win Marriages. Coaching and Christian counseling are faith-based and are not a substitute for licensed clinical or mental health care. If you are in danger, call 911 or the National Domestic Violence Hotline at 1-800-799-7233.</p><p><a href="/privacy/">Privacy Policy</a></p></div>
</footer>
<nav class="mobile-cta" aria-label="Quick actions"><a class="btn gold" href="{CALENDLY}" target="_blank" rel="noopener">Book a Meeting</a><a class="btn" href="/tuesday-prayer-call/">Join Tuesday Call</a></nav>
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
    with open(fp, "w", encoding="utf-8") as f:
        f.write(doc)
    return url

PORTRAIT = '<picture><source srcset="/assets/terrie-beeman.webp" type="image/webp"><img src="/assets/terrie-beeman.jpg" alt="Terrie Beeman, founder of Fight to Win Marriages, smiling outdoors" width="480" height="480" {extra}></picture>'

PHOTOS = {
    "kingdom-kouples-fellowship-dinner-houston": ((960, 719), "Kingdom Kouples Ministries couples gathered around a restaurant table in Houston, several in purple Kingdom Kouples shirts"),
    "marriage-small-group-women-houston": ((900, 1200), "Women from a Kingdom Kouples marriage small group in Houston smiling together in name tags"),
    "terrie-beeman-teaching-marriage-small-group": ((900, 1200), "Terrie Beeman teaching a Kingdom Kouples marriage small group in a Houston home"),
    "terrie-beeman-leading-couples-group": ((900, 1200), "Terrie Beeman leading a couples small group discussion in a living room"),
    "kingdom-kouples-small-group-houston": ((968, 1200), "Terrie Beeman with couples and families from a Kingdom Kouples small group in Houston"),
    "couples-small-group-discussion": ((900, 1200), "Couples talking around a dining table during a marriage small group"),
    "marriage-small-group-living-room": ((900, 1200), "Husbands and wives seated together during a Houston marriage small group meeting"),
    "couples-fellowship-dinner": ((900, 1200), "Couples and families sharing a meal at a Kingdom Kouples fellowship dinner"),
    "marriage-ministry-group-church": ((1024, 768), "Couples from the marriage ministry gathered together at a church event"),
    "terrie-beeman-certified-christian-counselor": ((1200, 1797), "Terrie Beeman smiling while holding her Board Certified Christian Counselor certificate"),
}

def photo(name, cls="", sizes="(max-width: 820px) 100vw, 50vw"):
    """Responsive, lazy-loaded photo from site/assets/photos (webp with jpg fallback)."""
    (w, h), alt = PHOTOS[name]
    b = f"/assets/photos/{name}"
    return (f'<picture class="photo {cls}"><source type="image/webp" srcset="{b}-640.webp 640w, {b}.webp {w}w" sizes="{sizes}">'
            f'<img src="{b}.jpg" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></picture>')

def gallery(names):
    return '<div class="gallery">' + "".join(photo(n, sizes="(max-width: 700px) 50vw, 25vw") for n in names) + "</div>"

# ---------------------------------------------------------------- HOME
home_faq = [
    ("What is Fight to Win Marriages?", "Fight to Win Marriages is a faith-based marriage ministry led by Terrie Beeman. It encourages couples not to give up on their marriage and focuses on healing, restoration, and standing on God's promises through prayer, love and faith."),
    ("Who is marriage coaching for?", "Coaching is for married couples, engaged couples, and individual spouses standing for their marriage, whether you are newlyweds or have been married for decades."),
    ("When is the Tuesday prayer call?", "Terrie hosts a free online marriage prayer and fasting call on Zoom every Tuesday at 6:00 PM CT. Couples young and old are welcome to join for prayer, encouragement and biblical guidance."),
    ("Can I book Terrie to speak at my church or event?", "Yes. Terrie speaks at church marriage ministries, couples retreats, women's conferences and marriage events. Use the booking form to share your date, location and audience."),
]

TESTIMONIALS = [
    {
        "author": "The Kellys",
        "meta": "Married 29 years",
        "excerpt": "We learned that fighting for our marriage does not mean fighting against each other. It means recognizing that we are on the same team and taking our battles to God in prayer.",
        "paragraphs": [
            "One of the blessings God placed on our 29-year marriage journey is Fight to Win Marriages Ministry. The weekly Tuesday Zoom meetings and our commitment to fasting until 3:00 p.m. have demonstrated the dedication and spiritual discipline it takes to fight for a marriage.",
            "We learned that fighting for our marriage does not mean fighting against each other—it means recognizing that we are on the same team and taking our battles to God in prayer. Ephesians 6:12 reminds us, ‘For our struggle is not against flesh and blood,’ and Ephesians 6:16 teaches us to take up the shield of faith so that we can extinguish the fiery darts of the enemy.",
            "Hearing Terrie and Donald share their testimony about the deliverance and restoration of their marriage especially blessed us and gave us hope to continue fighting. Their testimony reminded us that situations may look impossible to us, but nothing is impossible with God. This ministry reminds us that some things are worth fighting for.",
        ],
    },
    {
        "author": "Donna A.",
        "meta": "Standing for restoration",
        "excerpt": "Thanks to Fight to Win Marriages, I am further along than I was when I filed for divorce. My faith has been restored in God coming through for me and my family.",
        "paragraphs": [
            "This ministry has blessed me tremendously. I filed for divorce two times, but through this ministry I have learned what it means to be a woman of God who fights for her marriage. My eyes have been opened to the truth of what my marriage means for the Kingdom of God, and that my pain has purpose. Despite the way I feel, I have learned there is more to this story than the pain it has caused me.",
            "It is about God using me to break generational curses off my life, my husband's life and our children's lives. The ministry has taught me what to pray, what to seek God about, and has ignited a thirst for God as I believe for my marriage to be completely reconciled and my husband's heart turned to God.",
            "I am not where I would love to be yet, but thanks to Fight to Win Marriages, I am further along than I was when I filed for divorce. My faith has been restored in God coming through for me and my family. I have always believed in what God can do for me in other situations, but I used to doubt Him with my marriage based on what I saw and felt. Thanks to this ministry, that is not the case anymore. God is doing it, He has been working on it, and I cannot wait to share my reconciliation testimony in the future. He who started a good work is faithful to complete it. I am forever grateful for God using Mrs. Terrie and her ministry.",
        ],
    },
    {
        "author": "Prayer-call participant",
        "meta": "Tuesday marriage prayer call",
        "excerpt": "The weekly marriage prayer calls have strengthened my faith, taught me to trust God more in my marriage, and helped me go deeper in prayer.",
        "paragraphs": [
            "Fight to Win Marriages Ministry and God have blessed me through the weekly marriage prayer calls by strengthening my faith and teaching me to trust God more in my marriage. It has helped me go deeper in my prayers and grow in patience and understanding as a wife. I appreciate Terrie and Donald's passion and dedication to help us fight for our marriages.",
        ],
    },
    {
        "author": "S.W.",
        "meta": "Fight to Win Marriages community member",
        "excerpt": "Strong, Christ-centered marriages do not happen by accident, and this ministry is helping couples fight for what God intended.",
        "paragraphs": [
            "My husband and I are so grateful for Fight to Win Marriages. It is such a blessing to be in a space with like-minded couples and believers who are intentional about strengthening their marriages and putting God at the center.",
            "Satan has definitely been served several notices in our home, and we are believing our marriage will continue to reflect God's love to others. We are just getting started, and we are excited for all that God has in store.",
            "We absolutely love this community and wholeheartedly support what Donald and Terrie Beeman are doing. Their assignment is needed. Strong, Christ-centered marriages do not happen by accident, and this ministry is helping couples fight for what God intended.",
            "If you are married and want to see your marriage thrive, invite your spouse and join us. The more couples walking in God's purpose for their marriage, the stronger our families and communities will be. In Jesus' name.",
        ],
    },
    {
        "author": "The Cowans",
        "meta": "Fight to Win Marriages community members",
        "excerpt": "Your dedication, faithfulness and commitment to bringing God's people together in prayer do not go unnoticed.",
        "paragraphs": [
            "We want to thank you and Donald for the wonderful work you both continue to do in bringing God's people together in prayer. Your dedication, faithfulness and commitment to the work of the Lord do not go unnoticed, and we are truly grateful for you both. We love and appreciate you both, and we pray that God continues to strengthen, bless and use you mightily for His glory.",
        ],
    },
    {
        "author": "The Hendersons",
        "meta": "Married 4 years",
        "excerpt": "Terrie challenges you to trust God through the highs, lows and in-between. She is kind and inviting and made us feel comfortable opening up.",
        "paragraphs": [
            "Terrie was an amazing leader who challenges you to trust God through the highs, lows and in-between. She is so kind and inviting and really made us feel comfortable opening up. We really enjoyed meeting with her for Kingdom Kouples and her Zoom prayer calls.",
        ],
    },
    {
        "author": "The Randolphs",
        "meta": "Kingdom Wives participant",
        "excerpt": "Kingdom Wives really provided a lot of peace for me and my family. I am looking forward to Kingdom Couples.",
        "paragraphs": [
            "Good morning, Ms. Terri. I just wanted to thank you again for last semester's Kingdom Wives. It really provided a lot of peace for me and my family. I am looking forward to Kingdom Couples. Have a wonderful day.",
        ],
    },
]

def testimonial_card(item, compact=False):
    paragraphs = [item["excerpt"]] if compact else item["paragraphs"]
    rendered = []
    for index, paragraph in enumerate(paragraphs):
        text = html.escape(paragraph)
        if index == 0:
            text = "&ldquo;" + text
        if index == len(paragraphs) - 1:
            text += "&rdquo;"
        rendered.append(f"<p>{text}</p>")
    meta = f'<span class="testimonial-meta">{html.escape(item["meta"])}</span>' if item.get("meta") else ""
    return (f'<figure class="card testimonial"><blockquote>{"".join(rendered)}</blockquote>'
            f'<figcaption><strong>{html.escape(item["author"])}</strong>{meta}</figcaption></figure>')

def testimonial_grid(items, compact=False, modifier="full"):
    cards = "".join(testimonial_card(item, compact=compact) for item in items)
    return f'<div class="testimonials-grid {modifier}">{cards}</div>'

home = f'''
<section class="hero">
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">Christian marriage coaching &middot; Prayer &middot; Restoration</p>
<h1>We don't give up on marriage. We fight in <em>prayer, love &amp; faith.</em></h1>
<p class="lead">A God-filled space for healing, restoration, and standing on God's promises together. Terrie Beeman offers Christian marriage coaching, a weekly Tuesday prayer and fasting call, and marriage events for couples young and old.</p>
<div class="btns"><a class="btn gold" href="{CALENDLY}" target="_blank" rel="noopener">Book a 30-Minute Meeting</a><a class="btn ghost" href="/tuesday-prayer-call/">Join Tuesday Prayer Call</a></div>
<p class="micro">Serving couples online nationwide. Newlyweds, empty nesters and every season between.</p>
</div>
<picture class="hero-media"><source srcset="/assets/photos/happy-black-couple-hero.webp" type="image/webp"><img src="/assets/photos/happy-black-couple-hero.jpg" alt="A joyful Black married couple relaxing together at home" width="1983" height="793" fetchpriority="high" decoding="async"></picture>
</div>
</section>

<section class="section">
<div class="wrap">
<h2 class="center">Three ways to get help for your marriage</h2>
<div class="cards three">
<article class="card"><h3>Christian Marriage Coaching</h3><p>One-on-one or couples sessions rooted in Scripture. Work through conflict, broken trust, communication and separation with a coach who believes your marriage can be restored.</p><a class="link" href="/marriage-coaching/">Explore coaching &rarr;</a></article>
<article class="card featured"><h3>Tuesday Prayer &amp; Fasting Call</h3><p>Every Tuesday at {TUE_TIME}, Terrie hosts a free Zoom call where she prays, fasts and offers biblical guidance to couples. Bring your marriage before God alongside others who are standing too.</p><a class="link" href="/tuesday-prayer-call/">Join the call &rarr;</a></article>
<article class="card"><h3>Events &amp; Speaking</h3><p>Invite Terrie to your church, couples retreat, women's conference or marriage ministry for a message of hope, healing and covenant love.</p><a class="link" href="/events/">Book Terrie to speak &rarr;</a></article>
</div>
</div>
</section>

<section class="section founder-intro">
<div class="wrap split">
<div>
<p class="eyebrow">Meet the founder</p>
<h2>Terrie Beeman knows restoration is possible</h2>
<p>After a 365-day spiritual battle helped restore her own marriage, Terrie built Fight to Win Marriages to help couples pray, heal and fight for one another. She brings the compassion of someone who has lived the hard season and the practical guidance of a Certified Christian Counselor and Marriage Coach.</p>
<div class="btns"><a class="btn" href="/about/">Meet Terrie</a><a class="btn ghost" href="{CALENDLY}" target="_blank" rel="noopener">Schedule with Terrie</a></div>
</div>
<div class="portrait sm">{PORTRAIT.format(extra='loading="lazy" decoding="async"')}<p class="caption">Terrie Beeman, Founder</p></div>
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

<section class="section alt">
<div class="wrap">
<p class="eyebrow center">Ministry in action</p>
<h2 class="center">Marriage small groups in Houston and online</h2>
<p class="center narrow" style="margin:0 auto 8px">Terrie leads marriage small groups with Kingdom Kouples Ministries in Houston, where couples pray, learn and grow together around the table. The same heart for marriage carries into her online coaching and Tuesday prayer call.</p>
{gallery(["terrie-beeman-teaching-marriage-small-group", "kingdom-kouples-small-group-houston", "couples-small-group-discussion", "kingdom-kouples-fellowship-dinner-houston"])}
<p class="center"><a class="btn" href="/events/">See Events &amp; Gatherings</a></p>
</div>
</section>

<section class="section" id="testimonials">
<div class="wrap">
<p class="eyebrow center">Real stories of faith and restoration</p>
<h2 class="center">What couples are saying</h2>
<p class="center narrow testimonials-intro">A few words from couples and individuals whose faith and marriages have been strengthened through prayer, biblical teaching and community.</p>
{testimonial_grid([TESTIMONIALS[0], TESTIMONIALS[1], TESTIMONIALS[3]], compact=True, modifier="highlights")}
<p class="center testimonials-link"><a class="btn" href="/testimonials/">Read All Testimonials</a></p>
</div>
</section>

<section class="section alt">
<div class="wrap">
<p class="eyebrow center">Words to fight by</p>
<h2 class="center">Marriage grows when love stays in action</h2>
<div class="cards three quote-cards">
<figure class="card quote"><blockquote>"Remember&mdash;as a husband and wife, you have vowed to be each other's partner, lover, best friend, encourager, accountability and person to lean on when the other is weak. Marriage is a beautiful, lifelong partnership when we allow it to be, but we can't give up when it gets hard. We must press on. Let's not wonder how things could have been."</blockquote><figcaption>Terrie Beeman</figcaption></figure>
<figure class="card quote"><blockquote>"When you and your spouse reach the end of your time on earth, what will matter most will be the moments you served each other and the moments you served alongside each other. When we remove selfishness from our marriages, love will be all that remains. That's the kind of love that can change your marriage and change the world through your marriage."</blockquote><figcaption>Terrie Beeman</figcaption></figure>
<figure class="card quote"><blockquote>"Marriage should grow stronger with time. A couple should continue pursuing, encouraging and adoring each other through all the seasons of the relationship."</blockquote><figcaption>Terrie Beeman</figcaption></figure>
</div>
</div>
</section>

<section class="section">
<div class="wrap split">
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/5Sk_Hm1As2k" title="Terrie Beeman shares how she fought to win her marriage" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
<div><p class="eyebrow">Watch Terrie's story</p><h2>Born from a fight to win her own marriage</h2><p>Several years ago, Terrie's husband told her he wanted out. What followed was a 365-day battle of spiritual warfare, a still, small voice asking, "What about Me?", and a marriage fully restored. Today they stand 34 years strong, and everything they learned became Fight to Win Marriages.</p>
<p>Follow along on <a href="{IG}" target="_blank" rel="noopener">Instagram</a>, <a href="{TT}" target="_blank" rel="noopener">TikTok</a> and <a href="{YT}" target="_blank" rel="noopener">YouTube</a> for prayers, tips, tools and weapons to help you fight to win your marriage.</p>
<div class="btns"><a class="btn" href="/about/#story">Read Terrie's Story</a><a class="btn ghost" href="{YT_STORY}" target="_blank" rel="noopener">Watch on YouTube</a></div></div>
</div>
</section>
{faq_html(home_faq)}
{cta_band()}
'''
page("/", "Christian Marriage Coaching & Prayer | Fight to Win Marriages",
     "Faith-based Christian marriage coaching, prayer and restoration support with Terrie Beeman. Book coaching or join the free Tuesday prayer call online.",
     home, schema=[PERSON, faq_schema(home_faq)])

# ---------------------------------------------------------------- ABOUT
about = f'''
<section class="page-hero"><div class="wrap split">
<div><p class="eyebrow">About the founder</p><h1>Meet Terrie Beeman</h1>
<p class="lead">Certified Christian Counselor, Spiritual Life Coach, Marriage Coach, Motivator, Prayer Warrior and purpose-driven community leader.</p>
<div class="btns"><a class="btn gold" href="#bio">Read Terrie's Bio</a><a class="btn ghost" href="{CALENDLY}" target="_blank" rel="noopener">Book a 30-Minute Meeting</a></div></div>
<div class="portrait sm">{PORTRAIT.format(extra='')}</div>
</div></section>
<section class="section" id="bio"><div class="wrap split bio-profile">
<div>{photo("terrie-beeman-certified-christian-counselor", "bio-photo")}</div>
<div class="prose">
<p class="eyebrow">Her calling and her work</p>
<h2 style="margin-top:0">Faith, purpose and service in action</h2>
<p>Terrie Beeman is a Certified Christian Counselor, Spiritual Life Coach, Marriage Coach, motivator and prayer warrior&mdash;and the indomitable force behind TBee Ministries Inc. Hailing from the soulful streets of Motown, Detroit, she has found her vibrant home in H-Town, Houston.</p>
<p>Terrie is the visionary creator of <strong>Power Talks with Terrie</strong>, a platform where she weaves spiritual insight and life coaching into powerful, purpose-filled conversations. As founder of <strong>TBee Ministries Inc.</strong>, she guides people toward their God-given purpose. She also wears the entrepreneurial hat as owner of <strong>Blessed Income Tax Service Inc.</strong>, bringing the same heart for service to the financial lives of families.</p>
<p>A leader devoted to the sacred institution of marriage, Terrie spearheads <strong>Fight to Win Marriages</strong>, a movement dedicated to <em>Putting Marriages Back on the Map</em>. Her commitment to love extends beyond marriage. In 2020, she launched <strong>Put a Smile on a Child&mdash;Christmas Blessings</strong> to bring warmth and joy to children in need. In fall 2024, she expanded that work with <strong>Put a Smile on a Child&mdash;Back to School</strong>, equipping underprivileged children with essentials for a brighter academic journey.</p>
<p>Also in 2024, Terrie unveiled another facet of her purpose through <strong>Daughters Rise Up</strong>, a project created to empower women of all ages. Her vision is to illuminate their inherent worth, guide them from the shadows to the forefront, and ignite the spark within them to fulfill their divine destinies.</p>
<p>Terrie is an atmospheric shifter who casts light and positivity wherever she goes. Her infectious energy transforms every room and leaves an indelible mark on those fortunate enough to encounter her. A designer's original and a true game-changer, Terrie stands in her God-given uniqueness&mdash;the one and only, incomparable Terrie Beeman.</p>
</div>
</div></section>
<section class="section alt" id="tomeka-jones"><div class="wrap narrow">
<article class="card team-bio">
<div class="team-monogram" aria-hidden="true">TJ</div>
<div class="prose">
<p class="eyebrow">Meet the team</p>
<h2 style="margin-top:0">Tomeka Jones</h2>
<p class="team-role">Personal Assistant &middot; Prayer Warrior &middot; Intercessor</p>
<p>Once a timid, people-pleasing little girl carrying rejection and father wounds, Tomeka is now a <strong>bold, set-apart woman of God</strong>&mdash;healed by His love, refined by His fire and transformed by His presence. Peculiar by design and unapologetic in her faith, she no longer seeks man's approval. She loves what God loves, hates what He hates and bows to no one but Him.</p>
<p>As Terrie's personal assistant, Tomeka has led wives' groups back to Christ and served in marriage ministry as a prayer warrior and intercessor. She stands in the gap for wives, marriages and covenant restoration.</p>
<blockquote class="team-declaration">I am chosen. Called. Consecrated. And His!</blockquote>
</div>
</article>
</div></section>
<section class="section" id="story"><div class="wrap narrow prose">
<p class="eyebrow">Terrie's story</p>
<h2 style="margin-top:0">How a 365-day fight gave birth to a ministry</h2>
<p>"Several years ago, my husband came to me and said he no longer wanted to be married. He wanted out.</p>
<p>Those words catapulted me into a 365-day battle of spiritual warfare. Through many dark days, endless tears, and what felt like an emotional roller coaster, I was angry, I was sad, and many, many times I was mad. I have to admit it: there were days I didn't want to fight for my marriage.</p>
<p>Then one day the ride took a drastic, unexpected turn. I began to come to myself and count the cost. This wasn't just about me and my husband. What about our kids, our grandkids, and the generations to come? I realized he was a good man, and he was worth fighting for. Our marriage was worth fighting for.</p>
<p>So I went searching for answers, running to anybody who would listen, even strangers. I looked back at all the prayers, the fasting, the energy and the sweat I had poured into our marriage. And one day I heard a still, small voice say to me:</p>
<blockquote class="verse">"Terrie, what about Me? You haven't asked Me how to win your marriage back."</blockquote>
<p>That's when the Holy Spirit revealed to me that what we were facing was a spiritual battle. This was warfare. I took heed to God's voice and His instructions. The first thing I had to do was silence the outside voices and tune in to the voice of the Holy Spirit. He taught me how to be a kingdom wife, a wife according to His blueprint, and step by step He walked with me and showed me how to win our marriage back.</p>
<p>What we didn't know was that through the heartache, the storms and the chaos, we were giving birth to a marriage ministry.</p>
<p>Today our marriage is fully restored, healthy, and made new. We stand 34 years strong. Everything we learned through the good, the bad and the ugly, we now teach to husbands and wives all over the map: how to have a happy, healthy marriage that pleases God. A kingdom marriage."</p>
<p class="meta">Terrie Beeman, founder of Fight to Win Marriages &middot; <a href="{YT_STORY}" target="_blank" rel="noopener">Watch Terrie tell her story on YouTube</a></p>
</div></section>
<section class="section alt"><div class="wrap narrow prose">
<h2 style="margin-top:0">Why Fight to Win Marriages exists</h2>
<p>Terrie Beeman started Fight to Win Marriages with one message: don't give up. Marriage is one of God's greatest institutions, and it is worth fighting for. Too many couples walk away from a covenant God can still heal. Through coaching, prayer and teaching, Terrie helps husbands and wives stop fighting each other and start fighting for each other.</p>
<p>The ministry is founded on 2 Corinthians 10:4 and Ephesians 6:12. Our battle is not against our spouse but against spiritual forces, and God has given us weapons with divine power to pull down strongholds. Fight to Win Marriages partners with God to equip husbands and wives with those weapons, along with biblical principles, prayer, encouragement and practical tools to build strong, healthy, God-centered marriages.</p>
<h2>Our vision</h2>
<p>To see marriages healed, healthy and whole, and to decrease the divorce rate in the body of believers. Terrie is committed to inspiring faith, restoring hope and putting marriages back on the map.</p>
<h2>Who we serve</h2>
<p>Married and engaged couples, individuals preparing for marriage, and anyone seeking healing, restoration, wisdom and biblical guidance for their marriage.</p>
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
<li>Founder, TBee Ministries Inc. and Fight to Win Marriages</li>
<li>Creator, Power Talks with Terrie</li>
<li>Owner, Blessed Income Tax Service Inc.</li>
<li>Founder, Put a Smile on a Child and Daughters Rise Up community projects</li>
</ul>
<h2>Leading marriage small groups in Houston</h2>
<p>Terrie leads marriage small groups with Kingdom Kouples Ministries in Houston, Texas. Couples gather in homes and around the dinner table to pray, study God's Word and build friendships with other couples who are fighting for their marriages.</p>
<div class="photo-pair">{photo("terrie-beeman-teaching-marriage-small-group")}{photo("kingdom-kouples-small-group-houston")}</div>
<h2>A growing online community</h2>
<p>Fight to Win Marriages has become a faith-based relationship community across <a href="{IG}" target="_blank" rel="noopener">Instagram</a>, <a href="{TT}" target="_blank" rel="noopener">TikTok</a> and <a href="{YT}" target="_blank" rel="noopener">YouTube</a>, where couples find daily encouragement to keep standing.</p>
</div></section>
{cta_band(title="Work with Terrie", text="Coaching, prayer and speaking for couples and churches.", primary=("/marriage-coaching/", "See Coaching Options"), secondary=("/events/", "Invite Terrie to Speak"))}
'''
page("/about/", "About Terrie Beeman & the Ministry Team | Fight to Win Marriages",
     "Meet Terrie Beeman, founder of Fight to Win Marriages, and Tomeka Jones, her personal assistant, prayer warrior and intercessor.",
     about, schema=[PERSON, TOMEKA, {"@type": "AboutPage", "url": SITE + "/about/", "mainEntity": {"@id": f"{SITE}/#terrie"}}],
     og_type="profile", crumb=[("/", "Home"), ("/about/", "About Terrie Beeman")])

# ---------------------------------------------------------------- TESTIMONIALS
testimonials = f'''
<section class="page-hero"><div class="wrap narrow">
<p class="eyebrow">Stories from the community</p>
<h1>Marriage &amp; Ministry Testimonials</h1>
<p class="lead">Real words from couples and individuals who have found prayer, encouragement, peace and renewed faith through Fight to Win Marriages and Terrie Beeman's ministry.</p>
<div class="btns"><a class="btn gold" href="/tuesday-prayer-call/">Join Tuesday Prayer</a><a class="btn ghost" href="/marriage-coaching/">Explore Marriage Coaching</a></div>
</div></section>

<section class="section"><div class="wrap">
<p class="eyebrow center">Testimonies of faith and restoration</p>
<h2 class="center">Why couples keep fighting</h2>
<p class="center narrow testimonials-intro">Every testimony is presented in the same text format so each person's words remain the focus.</p>
{testimonial_grid(TESTIMONIALS)}
</div></section>

<section class="section alt" id="video-testimonies"><div class="wrap narrow video-testimonies center">
<p class="eyebrow">Hear their stories</p>
<h2>Video testimonies</h2>
<p>Hear directly from members of the Fight to Win Marriages community about the difference prayer, encouragement and standing together have made in their lives.</p>
<div class="btns"><a class="btn" href="{VIDEO_TESTIMONY_ONE}" target="_blank" rel="noopener">Watch Video Testimony</a><a class="btn ghost" href="{VIDEO_TESTIMONY_TWO}" target="_blank" rel="noopener">Watch Another Testimony</a></div>
</div></section>
{cta_band(title="Your story is still being written.", text="Stand with a community that believes prayer, faith and practical support can strengthen a marriage.", primary=("/tuesday-prayer-call/", "Join Tuesday Prayer"), secondary=("/contact/", "Contact Terrie"))}
'''
page("/testimonials/", "Marriage & Ministry Testimonials | Fight to Win Marriages",
     "Read testimonies from couples and individuals strengthened through Fight to Win Marriages, Terrie Beeman's teaching, prayer calls and community.",
     testimonials, crumb=[("/", "Home"), ("/testimonials/", "Testimonials")])

# ---------------------------------------------------------------- COACHING
coach_faq = [
    ("Is this Christian marriage counseling?", "Terrie is a Certified Christian Counselor and Marriage Coach. Sessions are faith-based coaching and Christian counseling, not licensed clinical therapy. Coaching uses biblical principles, prayer and practical tools to help you move forward. If you need clinical or crisis care, Terrie will encourage you to seek a licensed professional alongside coaching."),
    ("Can I do coaching if my spouse won't join?", "Yes. Many people begin coaching alone while standing for their marriage. Individual sessions focus on your heart, your prayer life and the changes you can make."),
    ("Are sessions online?", "Yes. Sessions are held online by video so couples anywhere can participate."),
    ("How much does marriage coaching cost?", "Pricing depends on the package. Terrie shares pricing on your free consultation call so you can choose the right fit."),
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
<div class="split" style="margin-bottom:36px"><div><h2>Real couples, real growth</h2><p>Terrie has been where you are. Her own marriage was restored after a 365-day spiritual battle, and she and her husband now stand 34 years strong. She has since walked alongside couples in Houston small groups and one-on-one, and coaching brings that same prayerful, practical approach to building a kingdom marriage, wherever you live. <a href="/about/#story">Read Terrie's story</a>.</p></div>{photo("couples-small-group-discussion", "rounded")}</div>
<h2>How coaching works</h2>
<ol class="steps">
<li><strong>Request a consultation.</strong> Tell Terrie a little about your marriage through the booking form.</li>
<li><strong>Free discovery call.</strong> A short call to pray, listen and recommend a path.</li>
<li><strong>Coaching sessions.</strong> Scripture-based guidance, prayer and practical homework between sessions.</li>
<li><strong>Ongoing support.</strong> Join the Tuesday prayer call for weekly encouragement as you grow.</li>
</ol>
</div></section>

<section class="section" id="packages"><div class="wrap">
<h2 class="center">Coaching packages</h2>
<div class="cards three pricing">
<div class="card"><h3>Single Session</h3><p>One online session for an individual or couple. Good for a specific issue or a first step.</p><a class="btn" href="/contact/?type=coaching">Book a Session</a></div>
<div class="card featured"><h3>Restoration Package</h3><p>A series of sessions for couples committed to rebuilding, with prayer support between sessions.</p><a class="btn gold" href="/contact/?type=coaching">Start Restoration</a></div>
<div class="card"><h3>Standing Spouse Package</h3><p>Individual sessions for the spouse standing for their marriage.</p><a class="btn" href="/contact/?type=coaching">Get Support</a></div>
</div>
<p class="center micro" style="margin-top:20px">Pricing and scheduling are shared on your free consultation call, so you can choose the package that fits your marriage.</p>
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
    ("Is the Tuesday prayer call free?", f"Yes. The call is free and open to couples and individuals who want prayer for their marriage. Join on Zoom every Tuesday at {TUE_TIME} using the link on this page, meeting ID {ZOOM_ID}."),
    ("Do both spouses need to attend?", "No. Come together or come alone. Many people join while standing in prayer for a spouse who is not ready yet."),
    ("Do I have to fast to join?", "No. Terrie prays and fasts for the marriages on the call. You are welcome to fast with her as you feel led, but it is not required to attend."),
    ("Do I have to be on camera or speak?", "No. You can listen, pray along and type requests privately if you prefer."),
    ("Can I submit a prayer request if I can't attend?", "Yes. Use the prayer request form on this page and Terrie will lift your marriage up in prayer."),
]
tuesday = f'''
<section class="page-hero"><div class="wrap">
<p class="eyebrow">Every Tuesday &middot; Live on Zoom &middot; Free &middot; All couples welcome</p>
<h1>Tuesday Marriage Prayer &amp; Fasting Call</h1>
<p class="lead">Each Tuesday, Terrie Beeman prays and fasts for marriages and hosts a free, live online Zoom call offering biblical guidance to couples, young and old. Come pray, be encouraged and stand with others who are believing God for their marriage.</p>
<div class="when"><div><span>Day</span><strong>Every Tuesday</strong></div><div><span>Time</span><strong>{TUE_TIME}</strong></div><div><span>Where</span><strong>Zoom &middot; ID {ZOOM_ID}</strong></div><div><span>Cost</span><strong>Free</strong></div></div>
<div class="btns prayer-call-actions"><a class="btn gold" href="{ZOOM}" target="_blank" rel="noopener">Join on Zoom</a><a class="btn ghost" href="#register">Get Weekly Reminders</a><a class="btn ghost" href="#prayer-request">Send a Prayer Request</a></div>
<p class="call-notes-inline"><span>Weekly resource</span><a href="/prayer-call-notes/">View and download Tuesday call notes <span aria-hidden="true">&rarr;</span></a></p>
</div></section>

<section class="section"><div class="wrap"><div class="split">
<div class="prose">
<h2>What happens on the call</h2>
<ul class="checks">
<li><strong>Corporate prayer</strong> over marriages, homes and families.</li>
<li><strong>A word of encouragement</strong> from Scripture for the week ahead.</li>
<li><strong>Biblical guidance</strong> for real questions couples are facing.</li>
<li><strong>Prayer requests</strong> lifted up by name, as you are comfortable.</li>
</ul>
<h2>Why prayer and fasting?</h2>
<p>Some battles are only won on our knees. Terrie learned that firsthand during her own 365-day fight for her marriage, when prayer, fasting and the voice of the Holy Spirit carried her through. Fasting humbles the heart and sharpens our focus on God. Terrie fasts each Tuesday for the couples on the call, so you never have to stand alone.</p>
</div>
<div>{photo("terrie-beeman-leading-couples-group", "rounded")}
<blockquote class="verse" style="margin-top:20px">"Again, truly I tell you that if two of you on earth agree about anything they ask for, it will be done for them by my Father in heaven."<cite>Matthew 18:19</cite></blockquote></div>
</div>
<article class="card call-notes-promo">
<div><p class="eyebrow">Keep the teaching close</p><h2>Weekly call notes</h2><p>Review the key Scriptures, teachings, reflection questions and next steps from Tuesday gatherings. Each recap is available to view or download.</p></div>
<div class="btns"><a class="btn" href="/prayer-call-notes/">Browse the Notes Archive</a><a class="btn ghost" href="{NOTES_PDF}" download>Download the Latest Recap</a></div>
</article>
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
             "isAccessibleForFree": True,
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": SITE + "/tuesday-prayer-call/", "validFrom": "2026-10-01"},
             "organizer": {"@id": f"{SITE}/#org"}, "performer": {"@id": f"{SITE}/#terrie"}}
page("/tuesday-prayer-call/", "Free Online Marriage Prayer Call Every Tuesday | Fight to Win Marriages",
     "Join Terrie Beeman's free marriage prayer and fasting call on Zoom every Tuesday at 6 PM CT. Prayer, Scripture and biblical guidance for couples young and old.",
     tuesday, schema=[tue_service, tue_event, faq_schema(tue_faq)], crumb=[("/", "Home"), ("/tuesday-prayer-call/", "Tuesday Prayer Call")])

# ---------------------------------------------------------------- CALL NOTES ARCHIVE
notes = f'''
<section class="page-hero"><div class="wrap narrow">
<p class="eyebrow">Tuesday prayer call resource library</p>
<h1>Weekly Call Notes</h1>
<p class="lead">Return to the Scriptures, teachings, reflection questions and prayer focus from Fight to Win Marriages' weekly Tuesday calls. View each edited recap online or download it to keep and share.</p>
<div class="btns"><a class="btn gold" href="{NOTES_PDF}" download>Download the Latest Notes</a><a class="btn ghost" href="/tuesday-prayer-call/">Join the Tuesday Call</a></div>
</div></section>

<section class="section"><div class="wrap">
<div class="archive-heading"><div><p class="eyebrow">Notes archive</p><h2>Tuesday call recaps</h2></div><p>New notes will be added here as they become available.</p></div>
<div class="resource-list">
<article class="card resource-card">
<div class="resource-date"><span>Oct</span><strong>20</strong><small>2026</small></div>
<div class="resource-copy">
<p class="resource-meta"><time datetime="2026-10-20">October 20, 2026</time> &middot; 2 pages &middot; PDF</p>
<h3>Spiritual Heart Check</h3>
<p>This recap invites husbands and wives to keep God at the center, begin with their own hearts, identify inner obstacles, receive correction as an opportunity to grow, and practice forgiveness with healthy boundaries. It also includes a marriage examination, personal reflection questions, a prayer focus and next steps.</p>
<p class="micro">Edited recap prepared from the weekly call summary and transcript; not a verbatim transcript.</p>
<div class="btns"><a class="btn" href="{NOTES_PDF}" target="_blank" rel="noopener">View PDF</a><a class="btn ghost" href="{NOTES_PDF}" download>Download PDF</a></div>
</div>
</article>
</div>
</div></section>
{cta_band(title="Join us for the next Tuesday call.", text="Come for prayer, Scripture and encouragement, then return here for downloadable notes.", primary=("/tuesday-prayer-call/", "Join Tuesday Prayer"), secondary=(CALENDLY, "Book a Meeting"))}
'''
notes_document = {
    "@type": "DigitalDocument",
    "name": "Tuesday Prayer Call Recap: Spiritual Heart Check",
    "description": "Edited recap of the October 20, 2026 Fight to Win Marriages Tuesday prayer call.",
    "datePublished": "2026-10-20",
    "encodingFormat": "application/pdf",
    "contentUrl": SITE + NOTES_PDF,
    "publisher": {"@id": f"{SITE}/#org"},
}
page("/prayer-call-notes/", "Weekly Tuesday Prayer Call Notes | Fight to Win Marriages",
     "View and download edited recaps, Scriptures, reflection questions and prayer notes from Fight to Win Marriages' weekly Tuesday calls.",
     notes, schema=[notes_document], crumb=[("/", "Home"), ("/prayer-call-notes/", "Weekly Call Notes")])

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
<article class="event"><div class="date"><span>Every</span><strong>Tue</strong></div><div><h3>Tuesday Marriage Prayer &amp; Fasting Call</h3><p>Online via Zoom &middot; {TUE_TIME}</p><p>Free weekly prayer, Scripture and biblical guidance for couples.</p></div><a class="btn small" href="/tuesday-prayer-call/">Details</a></article>
</div>
<p>New events are announced on <a href="{IG}" target="_blank" rel="noopener">Instagram</a> and <a href="{YT}" target="_blank" rel="noopener">YouTube</a>. Want Terrie at your church or retreat? <a href="/contact/?type=speaking">Send a speaking request</a>.</p>
</div></section>

<section class="section"><div class="wrap">
<h2>Past gatherings</h2>
<p>From Kingdom Kouples small groups and fellowship dinners in Houston to church marriage events, Terrie creates space for couples to connect, pray and grow.</p>
{gallery(["kingdom-kouples-fellowship-dinner-houston", "marriage-ministry-group-church", "couples-fellowship-dinner", "marriage-small-group-women-houston", "marriage-small-group-living-room", "kingdom-kouples-small-group-houston", "terrie-beeman-teaching-marriage-small-group", "couples-small-group-discussion"])}
</div></section>

<section class="section alt"><div class="wrap">
<h2>Book Terrie to speak</h2>
<p>Terrie brings warmth, honesty and a deep prayer life to every stage. Messages are rooted in Scripture and practical enough for couples to use the same night.</p>
<div class="cards three">
<div class="card"><h3>My 365-Day Fight</h3><p>Terrie's testimony of a husband who wanted out, a year of spiritual warfare, and a marriage restored and now 34 years strong.</p></div>
<div class="card"><h3>Restoration Is Possible</h3><p>Hope and next steps for marriages facing betrayal, separation or years of distance.</p></div>
<div class="card"><h3>Praying for Your Marriage</h3><p>How prayer and fasting change hearts, homes and generations.</p></div>
</div>
<h3>Great fit for</h3>
<ul class="tags"><li>Church marriage ministries</li><li>Couples retreats</li><li>Women's conferences</li><li>Valentine's &amp; anniversary events</li><li>Marriage enrichment weekends</li><li>Virtual events &amp; podcasts</li></ul>
<a class="btn gold" href="/contact/?type=speaking">Request Terrie for Your Event</a>
</div></section>
{faq_html(ev_faq, "Speaking FAQ")}
{cta_band(title="Bring Fight to Win to your church.", text="Share your date and audience, and Terrie's team will follow up.", primary=("/contact/?type=speaking", "Book Terrie to Speak"))}
'''
page("/events/", "Christian Marriage Events & Speaker Booking | Fight to Win Marriages",
     "Fight to Win Marriages events, Houston marriage small groups and speaker booking. Invite Terrie Beeman to your church, couples retreat or marriage ministry event.",
     events, schema=[faq_schema(ev_faq)], crumb=[("/", "Home"), ("/events/", "Events & Speaking")])

# ---------------------------------------------------------------- CONTACT
contact = f'''
<section class="page-hero"><div class="wrap">
<h1>Book Terrie or Get in Touch</h1>
<p class="lead">Request marriage coaching, invite Terrie to speak, or ask about the Tuesday prayer call. Terrie or her team will follow up by email.</p>
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
<p><a class="btn gold" href="{CALENDLY}" target="_blank" rel="noopener">Book a 30-Minute Meeting with Terrie</a></p>
<p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><strong>Instagram:</strong> <a href="{IG}" target="_blank" rel="noopener">@fighttowinmarriages</a></p>
<p><strong>YouTube:</strong> <a href="{YT}" target="_blank" rel="noopener">@FIGHTTOWINMARRIAGES</a></p>
<p><strong>TikTok:</strong> <a href="{TT}" target="_blank" rel="noopener">@fight.to.win.marr</a></p>
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
        "slug": "break-generational-curses-marriage-prayer",
        "title": "Break the Curse: 20 Declarations to Break Generational Curses Off Your Marriage",
        "seo_title": "Prayer to Break Generational Curses in Marriage | Fight to Win Marriages",
        "desc": "Pray along with Terrie Beeman: 20 declarations to break generational curses of divorce, infidelity, anger, addiction and more off your marriage, in Jesus' name.",
        "date": "2026-10-19",
        "excerpt": "Divorce, infidelity, anger and addiction can be passed down. Pray these 20 declarations with Terrie and declare a new legacy over your marriage.",
        "video": "kBKfw4CKGF4",
        "body": '\n<p>Some of the battles in your marriage didn\'t start with you. Patterns like divorce, infidelity, anger, addiction and silence can be passed down from one generation to the next until someone stands up and says, "It ends with us." In this prayer, Terrie Beeman leads husbands and wives in breaking generational curses off their marriage by the power of the almighty God and in the name of Jesus.</p>\n<div class="video" style="margin:28px 0"><iframe src="https://www.youtube-nocookie.com/embed/kBKfw4CKGF4" title="Break the Curse: generational curse declarations for your marriage with Terrie Beeman" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>\n<p class="meta"><a href="https://www.youtube.com/watch?v=kBKfw4CKGF4" target="_blank" rel="noopener">Watch "Break the Curse" on YouTube</a> and pray along with Terrie.</p>\n<h2>The message: Christ has already broken the curse</h2>\n<p>"Christ redeemed us from the curse of the law by becoming a curse for us" (Galatians 3:13). You are not bound to repeat what you saw growing up. In Christ, you and your spouse are a new creation (2 Corinthians 5:17), and your marriage can be transformed by the renewing of your mind (Romans 12:2). These declarations put that truth into words over your home.</p>\n<h2>How to pray these declarations</h2>\n<ul>\n<li><strong>Pray out loud,</strong> together if you can. If your spouse isn\'t ready, stand in the gap and declare them over your marriage yourself.</li>\n<li><strong>Pray them all, then linger on the ones that hit home.</strong> Repeat a declaration until your faith rises to meet it.</li>\n<li><strong>Pair them with action.</strong> Breaking a curse in prayer and building new habits go together. Forgive, set boundaries, get help for addiction, and learn to communicate.</li>\n</ul>\n<h2>20 declarations to break generational curses off your marriage</h2>\n<ol class="declarations">\n<li><strong>Divorce and broken marriages.</strong> By the power of the almighty God, i break the generational curse of divorce, broken marriages and unhealthy relationships in my family. In the mighty name of Jesus.</li>\n<li><strong>Infidelity.</strong> By the power of the almighty God, i break the generational curse of infidelity, adultery and unfaithfulness in my family bloodline. In the mighty name of Jesus.</li>\n<li><strong>Abandonment.</strong> By the power of the almighty God, i break the generational curse of abandonment. Fathers and mothers will not leave their spouses and children. In the mighty name of Jesus.</li>\n<li><strong>Abuse.</strong> By the power of the almighty God, i break the generational curse of domestic violence, whether physical, verbal, emotional or sexual abuse. These evil behaviors will not be normalized in our marriage or our family. In the mighty name of Jesus.</li>\n<li><strong>Addiction.</strong> By the power of the almighty God, i break the generational curse of addiction to alcohol, drugs, gambling, pornography or anything else damaging the marriages in my family. In the mighty name of Jesus.</li>\n<li><strong>Anger.</strong> By the power of the almighty God, i break the generational curse of chronic anger, explosive tempers, harsh words and unresolved conflict in our marriage. In the mighty name of Jesus.</li>\n<li><strong>Unforgiveness.</strong> By the power of the almighty God, i break the generational curse of unforgiveness. We will no longer hold grudges in our family. Instead, we will pursue reconciliation. In the mighty name of Jesus.</li>\n<li><strong>Control and manipulation.</strong> By the power of the almighty God, i break the generational curse of control and manipulation in our family. We will serve one another in love. In the mighty name of Jesus.</li>\n<li><strong>Pride.</strong> By the power of the almighty God, i break the generational curse of pride in our family. In the mighty name of Jesus.</li>\n<li><strong>Financial dysfunction.</strong> By the power of the almighty God, i break the generational curse of financial dysfunction in our family. No more debt and no more greed. In the mighty name of Jesus.</li>\n<li><strong>Sexual sin.</strong> By the power of the almighty God, i break the generational curse of sexual immorality, promiscuity, pornography or any other sexual sin affecting marital intimacy in our family. In the mighty name of Jesus.</li>\n<li><strong>Poor communication.</strong> By the power of the almighty God, i break the generational curse of poor communication in our family. In the mighty name of Jesus.</li>\n<li><strong>Emotional neglect.</strong> By the power of the almighty God, i break the generational curse of emotional neglect. We will no longer withhold love, affection, encouragement or support from one another. In the mighty name of Jesus.</li>\n<li><strong>Fear of commitment.</strong> By the power of the almighty God, i break the generational curse of fear of commitment in my family. In the mighty name of Jesus.</li>\n<li><strong>Distrust and jealousy.</strong> By the power of the almighty God, i break the generational curse of distrust, dishonesty and jealousy. In the mighty name of Jesus.</li>\n<li><strong>Codependency.</strong> By the power of the almighty God, i break the generational curse of codependency and unhealthy emotional dependence in our family. In the mighty name of Jesus.</li>\n<li><strong>Unhealthy family boundaries.</strong> By the power of the almighty God, i break the generational curse of unhealthy family boundaries. We will no longer allow our parents, siblings, relatives or even friends to interfere with our marriage relationship. In the mighty name of Jesus.</li>\n<li><strong>Spiritual apathy.</strong> By the power of the almighty God, i break the generational curse of spiritual apathy. We will no longer neglect prayer, worship or the Word of God in our marriage, leaving it spiritually vulnerable. In the mighty name of Jesus.</li>\n<li><strong>Idolatry.</strong> By the power of the almighty God, i break the generational curse of occult involvement and idolatry. In the mighty name of Jesus.</li>\n<li><strong>Victim mentality.</strong> By the power of the almighty God, i break the generational curse of a victim mentality. In the mighty name of Jesus.</li>\n</ol>\n<p class="micro">If you or your children are experiencing abuse, please get safe first. Call 911 or the National Domestic Violence Hotline at 1-800-799-7233. Prayer and safety go together.</p>\n<h2>Declare a new legacy</h2>\n<blockquote class="verse">I declare and I decree that my spouse and I are in Christ, and we are a new creation. We are transformed by the renewing of our minds. Lord Jesus, thank You that You redeemed us from every curse by becoming a curse for us, so we are no longer bound by generational curses or curses we have brought on ourselves. As for me and my house, we will serve the Lord. In Jesus\' mighty name, amen.<cite>Galatians 3:13 &middot; 2 Corinthians 5:17 &middot; Romans 12:2 &middot; Joshua 24:15</cite></blockquote>\n<h2>Keep standing for your marriage</h2>\n<p>Breaking generational curses is spiritual warfare, and it is exactly the battle Terrie fought for her own marriage. <a href="/about/#story">Read Terrie\'s story</a> of a 365-day fight and a marriage restored.</p>\n<ul>\n<li><a href="/tuesday-prayer-call/">Join the free Tuesday marriage prayer and fasting call</a> on Zoom every Tuesday at 6:00 PM CT and pray these declarations with other couples.</li>\n<li><a href="/blog/praying-and-fasting-for-your-marriage/">Learn how to pray and fast for your marriage</a>.</li>\n<li><a href="/marriage-coaching/">Book Christian marriage coaching</a> for help breaking old patterns and building new ones.</li>\n</ul>\n',
    },
    {
        "slug": "good-bad-ugly-seasons-of-marriage",
        "title": "The Good, the Bad and the Ugly Seasons of Marriage: God Is Still Writing Your Story",
        "seo_title": "The Good, the Bad & the Ugly in Marriage (Romans 8:28) | Fight to Win Marriages",
        "desc": "Every marriage has good, bad and ugly seasons. Terrie Beeman shares how Romans 8:28 means none of them is wasted, and why God is still writing your story.",
        "date": "2026-10-19",
        "excerpt": "Every marriage has good, bad and ugly seasons. None of them has to be wasted. Don't judge your marriage by the middle of the story. God is still writing.",
        "video": "evRtY6DnDXg",
        "body": """
<p>Every marriage has its seasons: the good, the bad and the ugly. There are blissful days full of laughter and long walks. There are hard days of heartache and broken promises. And there are ugly days when trust is shattered and the dream you started with seems out of reach. In this message, Terrie Beeman reminds husbands and wives that none of those seasons has to be wasted, because God is able to work all of it together for good.</p>
<div class="video" style="margin:28px 0"><iframe src="https://www.youtube-nocookie.com/embed/evRtY6DnDXg" title="The Good, the Bad and the Ugly parts of marriage with Terrie Beeman" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
<p class="meta"><a href="https://www.youtube.com/watch?v=evRtY6DnDXg" target="_blank" rel="noopener">Watch "The Good, the Bad &amp; the Ugly" on YouTube</a></p>
<blockquote class="verse">"And we know that all things work together for good to those who love God, to those who are the called according to His purpose."<cite>Romans 8:28 (NKJV)</cite></blockquote>
<h2>The message: God is still writing your story</h2>
<p>Don't judge your marriage by what it looks like in the middle of the story. The enemy wants the bad and the ugly seasons to destroy your marriage, but God can use every one of them for His purpose. Don't rip out the pages, and don't toss the book aside because the story isn't turning out the way you thought it would. There is so much more to your story.</p>
<h2>God is like a master chef</h2>
<p>A master chef can take ingredients that seem like they don't belong together and turn them into something good. God does the same with your marriage. He takes the beautiful seasons, the laughter, the joy and the romance, and mixes them with the heartbreaks, the broken trust, the disappointments and the shattered dreams. Somehow, some way, only God can make it all work together for your good.</p>
<h2>The good, the bad and the ugly</h2>
<ul class="checks">
<li><strong>The good seasons.</strong> Thank God for them. The joy, the friendship and the closeness are gifts worth celebrating and remembering.</li>
<li><strong>The bad seasons.</strong> They don't have to be wasted. God can teach you a whole lot through the difficult times: patience, humility and how to depend on Him together.</li>
<li><strong>The ugly seasons.</strong> Even the painful, ugly experiences in your marriage don't have to be wasted. God can bring healing, wisdom, maturity and a powerful testimony out of them.</li>
</ul>
<h2>Change the question you're asking God</h2>
<p>When marriage gets rough, tough and challenging, it's natural to pray, "God, make this turn out the way I want it to." Terrie invites couples to make a powerful shift and ask a different question:</p>
<blockquote class="verse" style="margin-bottom:20px">"Lord, how can You use this situation, this ugly situation, for Your purpose?"</blockquote>
<p>That one change moves you from demanding an outcome to trusting the One who is working behind the scenes, even when you just don't see it yet.</p>
<h2>What to do when you're in a bad or ugly season</h2>
<ol>
<li><strong>Don't give up and don't throw in the towel.</strong> The story isn't over, and starting over with someone else won't heal what God wants to heal in you.</li>
<li><strong>Spend time with God.</strong> Ask Him, "What is the purpose of this season we're in?"</li>
<li><strong>Sit still long enough to hear Him.</strong> He'll give you hope, and He may even give you a glimpse of what's on the other side of the trouble.</li>
<li><strong>Listen for His voice.</strong> The same still, small voice that guided Terrie through her own marriage battle will speak to you.</li>
</ol>
<h2>Terrie knows the ugly seasons, too</h2>
<p>Terrie's own marriage went through the good, the bad and the ugly, including the day her husband said he no longer wanted to be married. Through a 365-day battle of prayer and spiritual warfare, God restored their marriage, now 34 years strong. <a href="/about/#story">Read Terrie's story</a>.</p>
<h2>You don't have to walk through this season alone</h2>
<ul>
<li><a href="/tuesday-prayer-call/">Join the free Tuesday marriage prayer and fasting call</a> on Zoom every Tuesday at 6:00 PM CT.</li>
<li><a href="/blog/break-generational-curses-marriage-prayer/">Pray the Break the Curse declarations</a> over your marriage.</li>
<li><a href="/blog/how-to-fight-for-your-marriage/">Learn how to fight for your marriage without fighting your spouse</a>.</li>
<li><a href="/marriage-coaching/">Book Christian marriage coaching</a> with Terrie for help in a hard season.</li>
</ul>
<p>Be encouraged. God is able to do what only He can do through the good, the bad and the ugly seasons of your marriage.</p>
""",
    },
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
<p>Going through a hard season right now? Read <a href="/blog/good-bad-ugly-seasons-of-marriage/">The Good, the Bad and the Ugly Seasons of Marriage</a> and remember that God is still writing your story.</p>
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
<h2>Pray with authority</h2>
<p>Fasting is a powerful time to break old patterns in prayer. Use these <a href="/blog/break-generational-curses-marriage-prayer/">declarations to break generational curses off your marriage</a> as part of your fast.</p>
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
    return f'''<aside class="author card"><div class="portrait xs">{PORTRAIT.format(extra='loading="lazy"')}</div><div><p class="eyebrow">Written by</p><h2><a href="/about/">Terrie Beeman</a></h2><p>Certified Christian Counselor, marriage coach, prayer warrior and founder of Fight to Win Marriages. Married 34 years, Terrie hosts a weekly Tuesday prayer and fasting call for couples.</p></div></aside>'''

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
     f'<section class="section"><div class="wrap narrow prose"><h1>Privacy Policy</h1><p>Fight to Win Marriages collects the information you submit through forms on this site (such as your name, email and message) only to respond to you and provide the services you request. We do not sell your information.</p><p>Questions about your information? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>',
     crumb=[("/", "Home"), ("/privacy/", "Privacy Policy")])

# 404
page("/404.html", "Page Not Found | Fight to Win Marriages", "Page not found.",
     '<section class="page-hero"><div class="wrap narrow"><h1>Page not found</h1><p class="lead">Don\'t give up. Try the <a href="/">home page</a>, <a href="/marriage-coaching/">coaching</a> or the <a href="/blog/">blog</a>.</p></div></section>')

# sitemap + robots
urls = ["/", "/about/", "/marriage-coaching/", "/tuesday-prayer-call/", "/prayer-call-notes/", "/events/", "/testimonials/", "/blog/", "/contact/", "/privacy/"] + [f"/blog/{p['slug']}/" for p in POSTS]
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{SITE}{u}</loc><lastmod>2026-10-23</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nDisallow: /thank-you/\n\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(urls), "indexable urls")
