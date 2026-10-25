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
]
