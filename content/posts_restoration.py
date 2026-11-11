"""Blog posts for the restoration and prayer clusters."""

_SCRIPTURES = [
    ("Joel 2:25", "God restores the years that were stolen.", "Lord, restore every year the enemy has eaten in our marriage."),
    ("Mark 10:9", "What God joined together, no one should separate.", "Father, guard what You have joined. Let nothing separate us."),
    ("Ecclesiastes 4:12", "A threefold cord is not quickly broken.", "Be the third strand in our marriage, Lord."),
    ("Ephesians 6:12", "Our struggle is not against flesh and blood.", "Help me see my husband is not my enemy."),
    ("2 Corinthians 10:4", "Our weapons have divine power to pull down strongholds.", "Tear down every stronghold over our home."),
    ("Isaiah 43:19", "God is doing a new thing.", "Do a new thing in our marriage, and let me see it spring up."),
    ("Jeremiah 32:27", "Nothing is too hard for the Lord.", "Nothing in our marriage is too hard for You."),
    ("Ezekiel 36:26", "God gives a new heart and a new spirit.", "Replace every heart of stone in our home with a heart of flesh."),
    ("Romans 8:28", "All things work together for good to those who love God.", "Use even this season for Your purpose."),
    ("Philippians 1:6", "He who began a good work will complete it.", "Finish the good work You started in our marriage."),
    ("1 Corinthians 13:4-7", "Love is patient, kind, and never fails.", "Fill me with love that bears, believes, hopes and endures."),
    ("Colossians 3:13-14", "Forgive as the Lord forgave you; put on love.", "Help us bear with and forgive one another."),
    ("Ephesians 4:31-32", "Put away bitterness; be kind and tenderhearted.", "Pull every root of bitterness out of my heart."),
    ("Ephesians 4:2-3", "Keep the unity of the Spirit in the bond of peace.", "Make our home a place of peace and unity."),
    ("Genesis 2:24", "The two become one flesh.", "Restore our oneness in body, soul and spirit."),
    ("Proverbs 3:5-6", "Trust the Lord and He will direct your paths.", "I trust You more than what I see. Direct my steps."),
    ("Psalm 34:18", "The Lord is near the brokenhearted.", "Be near to me and to my husband in our brokenness."),
    ("Psalm 147:3", "He heals the broken in heart and binds up their wounds.", "Heal every wound in our marriage."),
    ("Isaiah 54:5", "Your Maker is your husband.", "When I feel alone, remind me You are with me."),
    ("Matthew 18:19", "Where two agree in prayer, it will be done.", "Send prayer partners to agree with me for this marriage."),
    ("James 5:16", "Confess and pray for one another, that you may be healed.", "Bring honesty and healing into our marriage."),
    ("1 Peter 4:8", "Love covers a multitude of sins.", "Let love be the strongest thing in our home."),
    ("Galatians 6:9", "Do not grow weary; in due season we will reap.", "Strengthen me when I'm tired of standing."),
    ("Isaiah 61:3", "Beauty for ashes, joy for mourning.", "Trade our ashes for beauty and our mourning for joy."),
    ("Lamentations 3:22-23", "His mercies are new every morning.", "Give us fresh mercy for each new day."),
    ("Psalm 127:1", "Unless the Lord builds the house, they labor in vain.", "Be the builder of our home."),
    ("2 Corinthians 5:17", "In Christ we are new creations.", "Make my husband and me new in You."),
    ("Mark 11:24", "Believe that you receive what you ask in prayer.", "I believe You for a restored marriage."),
    ("Zechariah 4:6", "Not by might, nor by power, but by My Spirit.", "Win this battle by Your Spirit, not my striving."),
    ("Hebrews 13:4", "Marriage is honorable and the marriage bed undefiled.", "Restore honor, purity and faithfulness to our marriage."),
]

_scripture_list = "".join(
    f"<li><strong>{ref}</strong>: {summary} <em>Pray it: \"{prayer}\"</em></li>" for ref, summary, prayer in _SCRIPTURES
)

POSTS = [
    {
        "slug": "scriptures-for-marriage-restoration",
        "title": "30 Scriptures for Marriage Restoration",
        "seo_title": "30 Scriptures for Marriage Restoration (With Prayers) | Fight to Win Marriages",
        "desc": "30 Bible verses for marriage restoration, each with a short prayer to pray over your husband and your home. Stand on God's promises for your marriage.",
        "date": "2026-10-25",
        "hub": "restoration",
        "intent": "faith",
        "excerpt": "Stand on God's Word for your marriage. Thirty verses, each with a short prayer you can pray today.",
        "body": f"""
<p>When your feelings shift by the hour, God's Word doesn't. These 30 Scriptures for marriage restoration are the promises many wives and couples in the Fight to Win community stand on. Read one each day for a month, or pray through them all tonight.</p>
<p>Write a few on cards, tape them to your mirror, and speak them out loud. As 2 Corinthians 10:4 reminds us, the weapons we fight with have divine power.</p>
<h2>Scriptures to pray over your marriage</h2>
<ol class="declarations">{_scripture_list}</ol>
<h2>How to use these verses</h2>
<ul class="checks">
<li><strong>Personalize them.</strong> Put your husband's name and your own in the prayer.</li>
<li><strong>Pair them with fasting.</strong> See [[/blog/praying-and-fasting-for-your-marriage/|Praying and Fasting for Your Marriage]].</li>
<li><strong>Declare them.</strong> Add them to the [[/blog/break-generational-curses-marriage-prayer/|Break the Curse declarations]].</li>
<li><strong>Pray them with others.</strong> Bring them to the [[/tuesday-prayer-call/|Tuesday prayer call]].</li>
</ul>
<p>Read more about [[/christian-marriage-restoration/|Christian marriage restoration]] or explore our [[/prayers-for-marriage/|prayers for your marriage]].</p>
""",
        "faqs": [
            ("What is the best Bible verse for marriage restoration?", "Many people stand on Joel 2:25, where God promises to restore the years the locust has eaten, along with Mark 10:9 and Isaiah 43:19."),
            ("How do I pray Scripture over my marriage?", "Read the verse, then turn it into a personal prayer using your and your husband's names. Speaking it aloud and repeating it daily helps it take root."),
            ("Which Bible verses help when my husband left?", "Psalm 34:18, Isaiah 54:5, Galatians 6:9 and Lamentations 3:22-23 are comforting when you are standing alone."),
        ],
    },
    {
        "slug": "marriage-restoration-testimonies",
        "title": "Marriage Restoration Testimonies: Stories of Couples God Restored",
        "seo_title": "Marriage Restoration Testimonies: Real Stories | Fight to Win Marriages",
        "desc": "Real marriage restoration testimonies from Terrie Beeman and the Fight to Win Marriages community: a husband who wanted out, a wife who filed for divorce twice, and more.",
        "date": "2026-12-04",
        "hub": "restoration",
        "intent": "proof",
        "excerpt": "A husband who wanted out. A wife who filed for divorce twice. Real stories of what God is doing in marriages right now.",
        "body": """
<p>When you're in the middle of a marriage crisis, it helps to know someone else made it through. These are real stories from the Fight to Win Marriages community, shared with permission.</p>
<blockquote class="verse">"And they overcame him by the blood of the Lamb, and by the word of their testimony."<cite>Revelation 12:11 (KJV)</cite></blockquote>

<h2>Terrie and Donald: "He wanted out"</h2>
<p>Several years ago, Terrie's husband told her he no longer wanted to be married. She describes the 365 days that followed as a battle of spiritual warfare full of dark days and endless tears. One day she heard a still, small voice: "Terrie, what about Me? You haven't asked Me how to win your marriage back." She silenced the outside voices, followed God's instructions, and learned to be a kingdom wife. Today their marriage is fully restored and 34 years strong. [[/about/#story|Read Terrie's full story]].</p>

<h2>Donna A.: "I filed for divorce two times"</h2>
<blockquote class="testimonial-quote">"I filed for divorce two times, but through this ministry I have learned what it means to be a woman of God who fights for her marriage... I am not where I would love to be yet, but thanks to Fight to Win Marriages, I am further along than I was when I filed for divorce. My faith has been restored in God coming through for me and my family."</blockquote>
<p>Donna's story is a reminder that restoration is often a process, not an overnight event.</p>

<h2>The Kellys: "On the same team"</h2>
<blockquote class="testimonial-quote">"We learned that fighting for our marriage does not mean fighting against each other. It means recognizing that we are on the same team and taking our battles to God in prayer."</blockquote>
<p>After 29 years of marriage, the Kellys found new strength through the weekly Tuesday calls and fasting.</p>

<h2>A prayer-call participant: "Trust God more"</h2>
<blockquote class="testimonial-quote">"The weekly marriage prayer calls have strengthened my faith, taught me to trust God more in my marriage, and helped me go deeper in prayer."</blockquote>

<h2>S.W.: "Not by accident"</h2>
<blockquote class="testimonial-quote">"Strong, Christ-centered marriages do not happen by accident, and this ministry is helping couples fight for what God intended."</blockquote>

<h2>Your story is still being written</h2>
<p>Read every story on our [[/testimonials/|testimonials page]], learn more about [[/christian-marriage-restoration/|Christian marriage restoration]], or join the [[/tuesday-prayer-call/|Tuesday prayer call]] to stand with others who are believing God.</p>
<p>Has God restored your marriage? We'd love to hear your story. <a href="/contact/">Share your testimony</a>.</p>
""",
        "faqs": [
            ("Are there real stories of marriages restored after divorce was filed?", "Yes. In the Fight to Win community, Donna A. filed for divorce twice and is now standing for her marriage, and Terrie Beeman's own marriage was restored after her husband said he wanted out."),
            ("How can I share my marriage restoration testimony?", "Send your story through the contact page. Testimonies are shared only with permission."),
            ("Why do testimonies matter for a struggling marriage?", "Hearing what God has done for others builds faith and hope when your own situation feels impossible."),
        ],
    },
    {
        "slug": "prayer-for-husband-who-left",
        "title": "A Prayer for My Husband When He Has Walked Away",
        "seo_title": "Prayer for a Husband Who Left: Prayers to Bring Him Home | Fight to Win Marriages",
        "desc": "A heartfelt prayer for your husband when he has walked away from you, your marriage or God, plus Scriptures and guidance for praying while you wait.",
        "date": "2026-10-27",
        "hub": "prayers",
        "intent": "faith",
        "excerpt": "When he's gone and you don't know what to say to God, pray this.",
        "body": """
<p>He packed a bag, or he moved out, or he simply stopped coming home in his heart. You don't know what to say to him anymore. But you can still talk to God about him. Here is a prayer for your husband when he has walked away.</p>

<h2>A prayer for my husband</h2>
<blockquote class="verse">"Father, You know where my husband is right now. You know his thoughts and the battles he's facing that I can't see. I lift him up to You. Draw him close to You first, before he comes back to me. Open his eyes to truth. Break every lie he is believing about himself, about me and about our marriage. Surround him with godly voices and remove the influences that pull him away from You. Protect his mind, his body and his heart. Soften what has grown hard. And Lord, guard my heart too. Keep me from bitterness. Make me whole in You, whatever he chooses. I trust You with my husband and my marriage. In Jesus' name, amen."</blockquote>

<h2>Scriptures to pray over him</h2>
<ul class="checks">
<li><strong>Ezekiel 36:26</strong>: a new heart and a new spirit.</li>
<li><strong>Luke 15:17-20</strong>: like the prodigal, may he "come to himself."</li>
<li><strong>2 Timothy 2:25-26</strong>: that God may grant repentance and freedom from the snare.</li>
<li><strong>Proverbs 21:1</strong>: the king's heart is in the hand of the Lord.</li>
</ul>

<h2>Pray for yourself, too</h2>
<p>Ask God for peace that guards your heart (Philippians 4:7), wisdom for practical decisions, and strength for single parenting days. Your healing matters regardless of his choices.</p>

<h2>Keep praying with others</h2>
<p>Every Tuesday at 6:00 PM CT, women and couples pray together on Zoom. [[/tuesday-prayer-call/|Join the free Tuesday prayer call]] or submit a prayer request. For more prayers, see our [[/prayers-for-marriage/|prayers for your marriage]] page and [[/blog/husband-wants-divorce-i-dont/|My Husband Wants a Divorce and I Don't]].</p>
""",
        "faqs": [
            ("How do I pray for a husband who left?", "Pray for his relationship with God first, for truth to replace lies, for godly influences, for protection, and for a softened heart. Pray for your own healing as well."),
            ("Can prayer bring my husband back?", "Prayer invites God to work in ways you cannot. It doesn't control your husband's free will, but many wives have seen hearts change through persistent prayer."),
            ("What Scripture should I pray for my prodigal husband?", "Luke 15:17-20, Ezekiel 36:26, 2 Timothy 2:25-26 and Proverbs 21:1 are good places to start."),
        ],
    },
    {
        "slug": "prayer-for-wife-who-left",
        "title": "A Prayer for My Wife When She Has Walked Away",
        "seo_title": "Prayer for a Wife Who Left: Prayers to Bring Her Home | Fight to Win Marriages",
        "desc": "A heartfelt prayer for your wife when she has walked away from you, your marriage or God, plus Scriptures and guidance for praying while you wait.",
        "date": "2026-10-29",
        "hub": "prayers",
        "intent": "faith",
        "excerpt": "When she's gone and you don't know what to say to God, pray this.",
        "body": """
<p>She packed a bag, or she moved out, or she simply stopped being present in your marriage. You don't know what to say to her anymore. But you can still talk to God about her. Here is a prayer for your wife when she has walked away.</p>

<h2>A prayer for my wife</h2>
<blockquote class="verse">"Father, You know where my wife is right now. You know her thoughts and the hurts she carries that I can't see. I lift her up to You. Draw her close to You first, before she comes back to me. Open her eyes to truth. Break every lie she is believing about herself, about me and about our marriage. Forgive me where I have wounded her, and show me where I need to change. Surround her with godly voices and remove the influences that pull her away from You. Protect her mind, her body and her heart. Soften what has grown hard. And Lord, guard my heart too. Keep me from bitterness and pride. Make me whole in You, whatever she chooses. I trust You with my wife and my marriage. In Jesus' name, amen."</blockquote>

<h2>Scriptures to pray over her</h2>
<ul class="checks">
<li><strong>Ezekiel 36:26</strong>: a new heart and a new spirit.</li>
<li><strong>Psalm 34:18</strong>: the Lord is close to the brokenhearted.</li>
<li><strong>2 Timothy 2:25-26</strong>: that God may grant repentance and freedom from the snare.</li>
<li><strong>Proverbs 21:1</strong>: the king's heart is in the hand of the Lord.</li>
</ul>

<h2>Pray for yourself, too</h2>
<p>Ask God for peace that guards your heart (Philippians 4:7), humility to own your part, wisdom for practical decisions, and strength for the days ahead. Your healing matters regardless of her choices. If she has told you she wants a divorce, read [[/blog/wife-wants-divorce-i-dont/|My Wife Wants a Divorce and I Don't]] for what to stop, what to start and how to stand.</p>

<h2>Keep praying with others</h2>
<p>Every Tuesday at 6:00 PM CT, husbands, wives and couples pray together on Zoom. [[/tuesday-prayer-call/|Join the free Tuesday prayer call]] or submit a prayer request. For more prayers, see our [[/prayers-for-marriage/|prayers for your marriage]] page and [[/christian-marriage-advice-for-husbands/|Christian marriage advice for husbands]].</p>
""",
        "faqs": [
            ("How do I pray for a wife who left?", "Pray for her relationship with God first, for truth to replace lies, for godly influences, for protection, and for a softened heart. Pray for your own healing and humility as well."),
            ("Can prayer bring my wife back?", "Prayer invites God to work in ways you cannot. It doesn't control your wife's free will, but many spouses have seen hearts change through persistent prayer."),
            ("What Scripture should I pray for my wife?", "Ezekiel 36:26, Psalm 34:18, 2 Timothy 2:25-26 and Proverbs 21:1 are good places to start."),
        ],
    },
    {
        "slug": "spiritual-warfare-prayer-for-marriage",
        "title": "Spiritual Warfare Prayer for Your Marriage",
        "seo_title": "Spiritual Warfare Prayer for Marriage | Fight to Win Marriages",
        "desc": "A powerful spiritual warfare prayer for your marriage rooted in Ephesians 6, plus how to put on the armor of God and stand against attacks on your home.",
        "date": "2026-11-17",
        "hub": "prayers",
        "intent": "faith",
        "excerpt": "Your marriage is in a battle, and your husband is not the enemy. Put on the armor and pray this.",
        "body": """
<p>Fight to Win Marriages is founded on two Scriptures: 2 Corinthians 10:4 and Ephesians 6:12. Our struggle is not against flesh and blood, and our weapons have divine power. When Terrie Beeman's husband said he wanted out, the Holy Spirit revealed that what she was facing was a spiritual battle. That revelation changed how she fought.</p>

<h2>Put on the full armor of God</h2>
<p>Ephesians 6:13-18 lists the armor: the belt of truth, the breastplate of righteousness, shoes of the gospel of peace, the shield of faith, the helmet of salvation, and the sword of the Spirit, which is the Word of God. Then it says to pray "always with all prayer."</p>

<h2>A spiritual warfare prayer for marriage</h2>
<blockquote class="verse">"Father, in the name of Jesus, I put on the full armor of God. I take my stand against every scheme of the enemy against my marriage. My husband is not my enemy. I bind every spirit of division, deception, lust, bitterness, pride and unforgiveness assigned to our home, and I break its power by the blood of Jesus. I cancel every word spoken against our covenant. I declare that what You have joined together, no one will separate. I loose peace, truth, love and unity over our marriage. Holy Spirit, fill our home. Restore what was stolen and make us new. In Jesus' mighty name, amen."</blockquote>

<h2>Practical warfare</h2>
<ul class="checks">
<li><strong>Guard the gates.</strong> Be careful what you watch, listen to and let into your home.</li>
<li><strong>Use your words.</strong> Speak life, not curses, over your husband, even when he's not there.</li>
<li><strong>Fast.</strong> See [[/blog/praying-and-fasting-for-your-marriage/|Praying and Fasting for Your Marriage]].</li>
<li><strong>Break old patterns.</strong> Pray the [[/blog/break-generational-curses-marriage-prayer/|Break the Curse declarations]].</li>
<li><strong>Don't fight alone.</strong> Join the [[/tuesday-prayer-call/|Tuesday prayer call]].</li>
</ul>
<p>See all our [[/prayers-for-marriage/|prayers for your marriage]].</p>
""",
        "faqs": [
            ("What is spiritual warfare in marriage?", "It is recognizing that many marriage battles have a spiritual dimension, as Ephesians 6:12 says, and responding with prayer, Scripture, fasting and the armor of God rather than fighting your spouse."),
            ("How do I pray spiritual warfare prayers for my marriage?", "Put on the armor of God (Ephesians 6), pray in Jesus' name against division and deception, declare Scripture over your home, and pray consistently."),
            ("Is my husband the enemy?", "No. Ephesians 6:12 teaches that our struggle is not against flesh and blood. Your husband is not the enemy, even when his choices hurt you."),
        ],
    },
    {
        "slug": "is-my-marriage-worth-saving",
        "title": "Is My Marriage Worth Saving? A Spiritual Heart Check Before You Decide",
        "seo_title": "Is My Marriage Worth Saving? A Biblical Heart Check | Fight to Win Marriages",
        "desc": "Wondering if your marriage is worth saving? Walk through a 5-part spiritual heart check, signs there's still hope, and when safety has to come first.",
        "date": "2026-11-07",
        "hub": "restoration",
        "intent": "decision",
        "excerpt": "Before you decide whether your marriage is worth saving, look beneath the surface. Here's a five-part spiritual heart check.",
        "body": """
<p>Most people don't ask "Is my marriage worth saving?" on a good day. They ask it after the same fight for the hundredth time, after a betrayal, or after months of silence in the same house. If that's where you are, take a breath. You don't have to answer that question tonight, and you don't have to answer it alone.</p>
<p><strong>The short answer:</strong> a marriage is usually worth fighting for when at least one spouse is willing to put God back at the center, look honestly at their own heart and get help, and when home is safe. Exhaustion, distance and repeated fights are signs your marriage needs care, not proof that it's over. Abuse is different. If you are unsafe, safety comes first.</p>

<h2>Start with a heart check, not a verdict</h2>
<p>On the October 20 Tuesday prayer call, Terrie Beeman taught on a prayer that changes how you ask the question:</p>
<blockquote class="verse">"Search me, O God, and know my heart: try me, and know my thoughts: and see if there be any wicked way in me, and lead me in the way everlasting."<cite>Psalm 139:23-24 (KJV)</cite></blockquote>
<p>Before you decide what your marriage is worth, ask God to show you what is happening beneath the surface. Terrie compared it to a medical checkup. A doctor doesn't judge your health by how you look in the waiting room. They check your history, your heartbeat, your blood pressure and your bloodwork.</p>

<h2>A 5-part spiritual heart check for your marriage</h2>
<p>Work through these on your own first. If your spouse is open to it, go through them together later.</p>
<ol class="checks">
<li><strong>Relationship history.</strong> What unhealthy habits or unresolved experiences did each of you bring into this marriage? Many marriage problems started long before the wedding.</li>
<li><strong>Heartbeat and rhythm.</strong> Are you listening to each other and showing respect? Do your actions at home line up with the faith you profess on Sunday?</li>
<li><strong>Blood pressure.</strong> Is your home marked by tension, silence, avoidance or dismissive words? High pressure doesn't mean the marriage is dead. It means something needs attention now.</li>
<li><strong>Bloodwork.</strong> Is bitterness or unforgiveness quietly building up inside you? It rarely shows on the outside until it has spread.</li>
<li><strong>Blockages.</strong> What is keeping love, grace, trust, honesty, prayer, peace and joy from flowing freely between you?</li>
</ol>
<p>Want a guided version? Take our free 2-minute [[/marriage-quiz/|"Is my marriage worth saving?" quiz]]. It points you to the right next step for your situation.</p>

<h2>Signs your marriage is still worth fighting for</h2>
<p>Every marriage is different, but these are hopeful signs:</p>
<ul class="checks">
<li><strong>One of you still wants to try.</strong> Restoration often starts with one person. Terrie stood alone for 365 days before her marriage was restored.</li>
<li><strong>You can name the problems.</strong> Specific problems like poor communication, broken trust or old wounds can be worked on.</li>
<li><strong>You still pray for your spouse,</strong> even when you're angry with them.</li>
<li><strong>You miss the friendship,</strong> not just the idea of being married.</li>
<li><strong>You're willing to look at your own part.</strong> This is the most important sign, and it's the one you control.</li>
<li><strong>Home is safe.</strong> Hard and unhappy is not the same as dangerous.</li>
</ul>

<h2>Look inward before you look outward</h2>
<p>It's natural to keep a list of everything your spouse has done wrong. The heart check asks a harder question: what is God showing <em>me</em>? On the call, Terrie named the inner obstacles that quietly damage a marriage: pride, resentment, jealousy, selfishness, anger, bitterness and unforgiveness.</p>
<p>This isn't about taking the blame for your spouse's choices. It's about the part you can actually change. When God puts His finger on something, that's conviction, and it leads to repentance and restoration. Condemnation is different. It only leads to shame. If what you're hearing makes you want to hide, it isn't coming from God.</p>
<p>If your spouse isn't ready to pray with you, you can still pray. One praying spouse can keep a marriage covered while God works on both hearts. Read [[/save-my-marriage-alone/|how to save your marriage when you're the only one fighting]].</p>

<h2>When the real question is safety</h2>
<p>If your spouse hits, threatens, controls or frightens you, the question isn't whether your marriage is worth saving. The question is how to get safe. Forgiveness does not mean accepting abuse, unsafe behavior or responsibility for another person's choices. Read [[/blog/when-standing-isnt-safe/|When Standing Isn't Safe]], and if you're in danger, call 911 or the National Domestic Violence Hotline at <a href="tel:18007997233">1-800-799-7233</a>.</p>

<h2>If infidelity is part of your story</h2>
<p>An affair raises its own questions about what God allows and whether trust can come back. Start with [[/blog/can-a-marriage-survive-infidelity/|Can a Marriage Survive Infidelity?]] and [[/blog/bible-divorce-adultery/|what the Bible says about divorce for adultery]].</p>

<h2>Don't decide in the dark</h2>
<p>Big decisions made in pain and isolation are rarely the right ones. Before you decide anything:</p>
<ul>
<li><strong>Talk with someone who has been there.</strong> [[/marriage-coaching/|Faith-based marriage coaching]] with Terrie is online, and you can start alone or together.</li>
<li><strong>Pray with others.</strong> Join the free [[/tuesday-prayer-call/|Tuesday marriage prayer call]] on Zoom every Tuesday at 6:00 PM CT.</li>
<li><strong>Make the heart check a habit,</strong> not just something you do in a crisis. Read the full [[/prayer-call-notes/2026-10-20-spiritual-heart-check/|Spiritual Heart Check call notes]] and download the PDF.</li>
</ul>
<p>Worn out from carrying it all? Read [[/blog/tired-of-fighting-for-my-marriage/|Tired of Fighting for Your Marriage? How Not to Grow Weary]].</p>
""",
        "faqs": [
            ("How do I know if my marriage is worth saving?", "Look beneath the surface before you decide. Ask God to search your heart (Psalm 139:23-24), name the specific problems, and notice whether at least one of you is willing to keep God at the center and get help. Repeated fights and distance are signs a marriage needs care, not proof that it is over. If there is abuse, safety comes first."),
            ("Is there a quiz to tell if my marriage is worth saving?", "Fight to Win Marriages offers a free 2-minute Christian marriage reflection quiz. It won't decide for you, but it points you to the right guide for your situation, whether that is infidelity, standing alone, restoration or prayer."),
            ("Can a marriage be saved if only one spouse is trying?", "Often, yes. Restoration frequently begins with one spouse who keeps praying, works on their own heart and gets support. Terrie Beeman stood alone for 365 days before God restored her marriage. You can't force your spouse to change, so focus on your part and your safety."),
            ("What does the Bible say about giving up on your marriage?", "Scripture treats marriage as a covenant (Mark 10:9) and encourages believers not to grow weary in doing good (Galatians 6:9). It never asks anyone to stay in danger. If you are wrestling with whether to stay, pray, seek wise counsel and avoid making permanent decisions in a moment of pain."),
        ],
    },
    {
        "slug": "trusting-god-when-marriage-restoration-feels-delayed",
        "title": "Trusting God When Marriage Restoration Feels Delayed",
        "seo_title": "Trusting God When Marriage Restoration Feels Delayed | Fight to Win Marriages",
        "desc": "When restoration is taking longer than you hoped, the story of Lazarus offers hope. Learn why delay isn't abandonment and what couples can do while they wait.",
        "date": "2026-11-11",
        "hub": "restoration",
        "intent": "faith",
        "excerpt": "When answers are slow and your marriage feels beyond repair, the story of Lazarus shows why a delay is not the same as God's absence.",
        "body": """
<p>You have prayed for months, maybe years. You have waited, fasted and held on. And your marriage still feels cold, stuck or beyond repair. In that silence it is easy to hear a "no," or to decide that God has stepped away. If that is where you are, you are not alone, and you are not the first believer to wonder why God has not moved yet.</p>
<p>On the November 10 Tuesday prayer call, Terrie Beeman taught from John 11, the raising of Lazarus, on trusting God when answers and restoration seem delayed. This article draws on those themes and adds some practical steps for the waiting. You can also <a href="/prayer-call-notes/2026-11-10-trust-me-i-know-what-im-doing/">read the Prayer Call Notes for November 10</a> or <a href="/assets/notes/fight-to-win-marriages-prayer-call-notes-2026-11-10.pdf" download>download the PDF handout</a>.</p>
<p><strong>The short answer:</strong> a delay does not prove that God has abandoned your marriage. In John 11, Jesus waited on purpose, and the wait served a larger purpose. While you wait, tell the truth about what is broken, take it to God first, and keep taking wise, faithful steps.</p>

<h2>What the story of Lazarus teaches about delay</h2>
<p>Mary and Martha sent word to Jesus that their brother Lazarus, whom He loved, was sick (John 11:3). If you had been in their place, you would have expected Him to come right away. Instead, Scripture says He stayed where He was for two more days (John 11:6). By the time He arrived, Lazarus had been in the tomb four days (John 11:17).</p>
<p>Jesus had already told His disciples how to read the situation:</p>
<blockquote class="verse">This sickness is not unto death, but for the glory of God, that the Son of God may be glorified through it.<cite>John 11:4 (NKJV)</cite></blockquote>
<p>The sisters could only see the delay and the grief. Jesus saw what He was about to do. A marriage can feel like that tomb: sealed, silent and long past hope. The story invites you to ask a different question than "Why isn't God doing anything?" Ask instead, "What might God be doing that I can't see yet?"</p>

<h2>Why delay does not necessarily mean abandonment</h2>
<p>Look at how John tells it. He writes that Jesus loved Martha, her sister and Lazarus, and then that He stayed two more days (John 11:5-6). Love and delay sit side by side in the same passage. God's slowness is not the same as God's absence.</p>
<p>The story also leaves room for honest disappointment. Both Martha and Mary said, "If You had been here, my brother would not have died" (John 11:21, 32). Jesus did not scold them for saying it. He met them in their grief, and John records that He wept (John 11:35). You can bring your frustration and sorrow to God without losing your faith.</p>
<p>A delayed answer can become the setting for deeper faith, for healing in you, and for a testimony that encourages other couples. That does not make the pain good. It means pain is not the end of the story.</p>

<h2>Acknowledging marriage problems without surrendering hope</h2>
<p>When Jesus spoke plainly, He did not pretend: "Lazarus is dead" (John 11:14). Faith does not mean denying reality. It means telling the truth and still believing God can act.</p>
<p>In your marriage, that may mean naming things like lost trust, cold communication, old wounds or years of distance. Saying them out loud to God is not unbelief. Pretending everything is fine is more likely to leave the root problems untouched.</p>
<p>Naming a problem is also different from blaming your spouse. Ephesians 6:12 reminds us that the struggle is not against flesh and blood. Your husband or wife is not the enemy. The battle is fought through prayer, fasting and Scripture, not through retaliation, contempt or advice that pushes you to harden your heart. If you are weighing whether to keep going, our <a href="/blog/is-my-marriage-worth-saving/">heart check for deciding whether your marriage is worth saving</a> can help you slow down.</p>

<h2>Bring the crisis to God first</h2>
<p>Notice what Mary and Martha did first: they sent word to Jesus. The first move was toward Him. A simple way to say it is this: run to the throne before you run to the phone.</p>
<p>That does not mean you should never talk to a pastor, a counselor or a trusted friend. It means order matters. When you pray first, you are less likely to act on panic, to say something you cannot take back, or to collect advice from people who only want you to feel justified. If you are not sure how to start, read <a href="/blog/praying-and-fasting-for-your-marriage/">how to pray and fast for your marriage</a>, or join the <a href="/tuesday-prayer-call/">free Tuesday prayer call</a> and pray with others who are standing for their marriages.</p>

<h2>Productive actions couples can take while waiting</h2>
<p>Waiting does not have to mean doing nothing. These four habits keep you steady:</p>
<ul class="checks">
<li><strong>Pause.</strong> Do not let urgency push you into harsh words or hasty decisions. A calm "I need to pray about this" is better than something you will regret.</li>
<li><strong>Pray.</strong> Invite God into what you cannot control. Ask Him to fight for your marriage and to show you your part in it.</li>
<li><strong>Examine your own heart.</strong> Ask what God may be healing or changing in you: bitterness, fear, old childhood wounds or unhealthy patterns. This is not about taking all the blame. It is about the one area you can truly influence.</li>
<li><strong>Persevere.</strong> Keep reading Scripture, keep praying and fasting if you are able, and keep taking small, constructive steps. Galatians 6:9 says not to grow weary in doing good, because in due season we will reap.</li>
</ul>
<p>Wise outside help is part of faithful waiting too. If wounds or patterns run deep, a pastor, a licensed counselor or a <a href="/marriage-coaching/">Christian marriage coach</a> can walk with you. If you want to meet other couples in person, see our <a href="/events/">upcoming events</a>, or <a href="/contact/">contact the ministry</a> with questions. For more encouragement, explore our guide to <a href="/christian-marriage-restoration/">Christian marriage restoration</a>.</p>
<p class="micro"><strong>A note on safety:</strong> waiting on God does not mean staying where you are in danger. If you or your children are experiencing abuse, get safe first. Call 911 or the National Domestic Violence Hotline at 1-800-799-7233. Healthy boundaries and trust in God go together.</p>

<h2>Reflection questions</h2>
<ol>
<li>What part of my marriage feels delayed, lifeless or beyond my control right now?</li>
<li>Am I reading God's delay as abandonment? What might He be developing in me, and in us?</li>
<li>What painful reality do I need to name honestly before God?</li>
<li>What would it look like to see this season from God's point of view?</li>
<li>What is one faithful, constructive step I can take this week?</li>
</ol>

<h2>A short prayer while you wait</h2>
<blockquote class="verse">Lord, You see what I cannot. I bring You the parts of my marriage that feel dead and the parts I am afraid to name. Give me courage to be honest, patience to wait, and a soft heart toward my spouse. Show me what You are doing in me. I choose to trust You, even when I do not understand Your timing. In Jesus' name, amen.</blockquote>

<h2>Take the notes with you</h2>
<p>If this spoke to you, the full call recap includes the five key teachings, reflection questions, prayer focus and next steps. <a href="/prayer-call-notes/2026-11-10-trust-me-i-know-what-im-doing/">Read the November 10 Prayer Call Notes</a> online, or <a href="/assets/notes/fight-to-win-marriages-prayer-call-notes-2026-11-10.pdf" download>download the Prayer Call Notes (PDF)</a> to print, share with your spouse or keep beside your Bible.</p>
""",
        "faqs": [
            ("Does a delayed answer mean God is saying no to my marriage?", "Not necessarily. In John 11, Jesus loved Lazarus and his sisters and still waited before coming. A delay can be part of God's timing and purpose. Keep praying, stay honest and keep taking wise steps."),
            ("How do I keep faith while my marriage is still struggling?", "Tell God the truth about what hurts, keep praying and reading Scripture, ask Him to examine your own heart, and stay connected to a supportive faith community. Small, steady habits carry you through long seasons."),
            ("Should I keep waiting if my marriage is unsafe?", "No. Waiting on God does not mean staying in danger. If you or your children are being abused, get to safety first and contact 911 or the National Domestic Violence Hotline at 1-800-799-7233."),
        ],
    },
]
