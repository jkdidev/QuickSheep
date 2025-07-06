feeds = [
    "https://www.ft.com/rss/home",
    "https://fortune.com/feed/fortune-feeds/?id=3230629",
    "https://seekingalpha.com/feed.xml",
    "https://www.fool.com/a/feeds/partner/googlechromefollow?apikey=5e092",
    "https://www.business-standard.com/rss/latest-news",
    "https://www.thestreet.com/.rss/full",
    "https://www.marketbeat.com/feed",
    "https://money.com/money/feed",
    "https://www.gfmag.com/feed",
    "https://www.financialsamurai.com/feed",
    "https://moneyweek.com/feed/all",
    "https://www.finance-monthly.com/feed",
    "https://europeanfinancialreview.com/feed",
    "https://moneymorning.com/feed",
    "https://dealbreaker.com/.rss/full",
    "https://www.worldfinance.com/feed",
    "https://www.finews.com/news/english-news/rss",
    "https://www.financeasia.com/rss/latest",
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "https://markets.businessinsider.com/rss/news",
    "https://www.barchart.com/rss",
    "https://www.afr.com/rss",
    "https://www.economywatch.com/rss",
    "https://www.cfi.co/rss",
    "https://www.google.com/finance/rss",
    "https://www.forbes.com/investing/feed",
    "https://www.financialexpress.com/feed",
    "https://feeds.content.dowjones.io/public/rss/mw_marketpulse",
    "https://www.wsj.com/xml/rss/3_7014.xml",
    "https://www.fnlondon.com/rss",
    "https://www.bloomberg.com/feed/podcast/bloomberg-surveillance.xml",
    "https://www.barrons.com/feed",
    "https://finance.yahoo.com/news/rssindex",
    "https://www.investing.com/rss/news_25.rss",
    "https://www.investopedia.com/feedbuilder/feed",
    "https://www.nerdwallet.com/blog/finance/feed/",
    "https://www.economist.com/latest/rss.xml",
    "https://www.bankrate.com/rss/",
    "https://www.morningstar.com/rss",
    "https://www.kiplinger.com/rss",
    "https://www.ibtimes.com/rss",
    "https://www.policygenius.com/rss/news",
    "https://www.investors.com/rss/news"
]

keywords = [
    # Currency-related
    "USD", "dollar", "U.S. dollar", "greenback", "de-dollarization", "reserve currency",

    # Gold and commodities
    "gold", "precious metal", "bullion", "safe haven", "commodity prices", "oil prices", "energy prices",

    # Economic indicators
    "interest rate", "rate hike", "rate cut", "inflation", "CPI", "PPI",
    "unemployment", "jobless claims", "labor market", "payrolls", "NFP",
    "GDP", "recession", "economic slowdown", "economic growth", "deflation",
    "yield curve", "bond yields", "treasury yield",

    # Central banks and policy
    "federal reserve", "fed", "FOMC", "central bank", "ECB", "monetary policy",
    "quantitative easing", "quantitative tightening", "QE", "QT",
    "fiscal policy", "stimulus", "debt ceiling", "government shutdown",

    # Risk sentiment and volatility
    "risk-on", "risk-off", "market volatility", "VIX", "flight to safety", "market panic",

    # Banking/financial system risk
    "bank failure", "bank collapse", "credit crunch", "liquidity crisis", "capital flight",

    # Sovereign and credit risk
    "ratings downgrade", "sovereign debt", "default", "IMF", "bailout",

    # Trade and global finance
    "trade war", "tariffs", "sanctions", "export restrictions",

    # Geopolitical hotspots and events
    "geopolitical tension", "conflict", "war", "military action", "airstrike", "missile", "nuclear",
    "invasion", "occupation", "terror attack", "cyberattack", "proxy war",
    "Israel", "Iran", "Palestine", "Gaza", "Hamas", "Hezbollah",
    "Ukraine", "Russia", "Crimea", "Donbas",
    "China", "Taiwan", "South China Sea", "Beijing", "Xi Jinping",
    "North Korea", "Pyongyang", "Kim Jong-un",
    "Middle East", "Red Sea", "Houthi", "strait of hormuz",
    "BRICS", "OPEC", "NATO", "UN Security Council",
    "coup", "military junta", "political instability", "election violence", "civil unrest"
]


seed_data = {'https://fortune.com/feed/fortune-feeds/?id=3230629': (['The world could get carved up into these 3 blocs as Trump tariffs fuel deglobalization. Here’s which side each country might join', 'The world could get carved up into these 3 blocs as Trump tariffs fuel deglobalization. Here’s which side each country might join', 'Musk forms America Party ‘to give you back your freedom’ after reigniting bitter feud with Trump', 'Ford CEO Jim Farley warns AI will wipe out half of white-collar jobs, but the ‘essential economy’ has a huge shortage of workers', 'As Trump pushes Apple to make iPhones in the U.S., Google’s brief effort building smartphones in Texas 12 years ago offers critical\xa0lessons'], 12.434812000006787), 'https://seekingalpha.com/feed.xml': (['Gold Fields: No Longer An Attractive Risk-Reward', 'Gold Fields: No Longer An Attractive Risk-Reward', 'Bank of Montreal Is Strategically Positioned, But Valuation And Retracement Warrant A Hold Rating', 'Markets Weekly Outlook - RBA And RBNZ Rate Decisions, July 9th Trump Deadline And BRICS Meeting'], 11.978762099999585), 'https://moneyweek.com/feed/all': (['8 of the best properties for sale with award-winning gardens', 'Little-known way inheritance tax pension raid could put thousands of businesses at risk – ‘issue is flying under the radar’', 'NS&I cuts interest rates on 7 savings products – full list of changes', 'Is property investment still as safe as houses? Why golden era could be over', "Tariffs 'were a terrible idea but shunning the US is a big mistake'", 'MPs warn over Lifetime ISAs which could leave savers out of pocket', "Israel claims victory in the '12-day war' with Iran", 'Investors remain calm as the Middle East war unfolds', 'Marcus boosts interest rates to provide top deals on savings'], 11.048054999992019), 'https://www.worldfinance.com/feed': (['How to educate in a time of conflict'], 9.554587699996773), 'https://feeds.content.dowjones.io/public/rss/mw_marketpulse': (['Jobless claims fall to lowest level since mid-May', 'Jobless claims stay low in latest week', 'Trump asks Supreme Court to pause TikTok ban', 'U.S. stock futures and bond yields drop on reports Putin has updated nuclear doctrine', 'Nobel economics prize awarded to three who studied wealth of nations', 'Nobel Peace Prize awarded to Japanese atomic bomb survivors'], 5.419974799995543), 'https://www.investing.com/rss/news_25.rss': (['Trump’s Big Beautiful Bill poses risks for Indian exporters', 'Ingram Micro says identified ransomware on certain of its internal systems'], 3.5670367999991868), 'https://www.economist.com/latest/rss.xml': (['Macron will beat Trump to London', 'Economic data, commodities and markets', 'Beware tomes of Chinese political gossip!', 'China’s bid to influence the Philippines heats up', 'Canada makes a first concession to Donald Trump', 'The Israel-Iran war has not yet transformed the Middle East', 'Israel’s weird war clock: 12 days for Iran, 21 months in Gaza', 'Turkey’s strongman is becoming Donald Trump’s point man', 'The Supreme Court keeps helping Donald Trump', 'Inside Iran’s war economy', 'Trumponomics 2.0 will erode the foundations of America’s prosperity', 'How to strike a trade deal with Donald Trump', 'Will bowing to Trump win Paramount its merger?', 'The big beautiful bill reveals the hollowness of Trumponomics', 'How Donald Trump’s “One Big Beautiful Bill” will transform America', 'How South Africa could harness Donald Trump’s wrath', 'Ten charts to explain Trump’s big, beautiful bill', 'Can Trump end America’s $1.8trn student-debt nightmare?', 'The War Room newsletter: The daddy of all summits', 'Xi Jinping wages war on price wars', 'Trump brokered peace between Rwanda and Congo. Can it hold?', 'A blow to judicial power and a win for Trump', 'Zohran Mamdani, Trump’s “worst nightmare”, may really be a gift to him', 'Economic data, commodities and markets', 'Japan’s civil war over surnames', 'The gold bull-market has a dirty secret', 'Has Donald Trump solved Iran from the air?', 'The fallout from Trump’s Iran strikes is political, too', 'A bitcoin scandal is good news for the Czech Donald Trump', 'Ukraine is inching towards robot-on-robot fighting', 'The culture wars are coming for cousin marriage in Britain', 'The war in Ukraine shows the West can re-arm without re-industrialising', 'Israel’s war with Iran is over', 'India gets no favours from Trump', 'Call centres could be a gold mine for Africa', 'Why commodities are on a rollercoaster ride', 'Mapping Iran’s nuclear programme', 'At a tricky NATO summit, a Trumpian meltdown is averted', 'Feckless Europe accepts Trump’s Lone Ranger diplomacy', 'Ceasefire may stave off War Powers clash', 'Trump says the war is over. How 14 bombs may change the Middle East', 'Trump says the war is over. How 14 bombs may change the Middle East', 'After Iran’s knife-edge missile strike Trump says “no more hate”', 'The War Room newsletter: The aftermath of America’s strike', 'Do Americans really want war with Iran?', 'H.R. McMaster on how to play the inconsistencies in Trump’s worldview', 'Trump must offer Iran more than bombs, rage and humiliation', 'The American attacks allow Netanyahu to end the wars with Iran and in Gaza, says his predecessor', 'Trump’s Iran attack was ambitious. But has it actually worked?', 'Trump smashes Iran—and gambles the regime will now capitulate', 'MAGA devotees are split over going to war with Iran', 'MAGA devotees are split over going to war with Iran', 'Trump v Iran: a negotiation made in hell', 'How the US may join the war between Iran and Israel', 'Does Donald Trump fear a nuclear Iran more than he hates war?', 'Does Donald Trump fear a nuclear Iran more than he hates war?', 'Economic data, commodities and markets', 'China has become the most important enabler of Russia’s war machine', 'Could Trump can AUKUS?', 'Africa’s scary new age of high-tech warfare', 'Drone warfare is hitting Haiti', 'The war in Sudan is spilling over its borders', 'China is trying to win over Africa in the global trade war', 'China is trying to win over Africa in the global trade war', 'Our model suggests President Trump is under water in every swing state', 'Europe wants to show it’s ready for war. Would anyone show up to fight?', 'This week’s NATO summit will be all about placating Donald Trump', 'Where will the Iran-Israel war end?', 'Why MAGA’s pro-natalist plans are ill-conceived', 'Will the Iran war trigger a refugee crisis?', 'Will the Iran war trigger a refugee crisis?', 'Inside the spy dossier that led Israel to war'], 2.3144320999999763)}
