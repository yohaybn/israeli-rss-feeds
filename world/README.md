# world - קטלוג פידים בינלאומי

המרה של [plenaryapp/awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) (רישיון CC0) לאותה סכמה של [`feeds.json`](../feeds.json) הישראלי - אותן 21 קטגוריות, אותם שדות - כך שאפליקציה יכולה לקרוא את שני הקבצים באותו קוד.

ההבדל מהמקור: **כל פיד כאן אומת מול האתר החי** (HTTP תקין, RSS/Atom שמתפעל, פריט אחרון מ-90 הימים האחרונים). פידים מתים, קפואים או שאי אפשר לאמת לא נכנסים. הרשימה המלאה של מה שנפסל ולמה: [`FEEDS-STATUS.md`](FEEDS-STATUS.md).

## שימוש

- **אפליקציות**: [`feeds.json`](feeds.json). כתובת גלם:

  `https://raw.githubusercontent.com/yohaybn/israeli-rss-feeds/main/world/feeds.json`

- **קוראי RSS**: [`opml/world-rss-feeds.opml`](opml/world-rss-feeds.opml), או קובץ לקטגוריה מתוך [`opml/by-category/`](opml/by-category/) (קיים קובץ לכל 21 הקטגוריות, גם לריקות, כדי שהנתיבים יהיו יציבים).

## הסכמה

זהה ל-`feeds.json` הישראלי (`version: 2`, `categories[].feeds[]` עם `title`, `url`, `site`, `homepage`, `language`, `popularity`). `popularity` ריק כאן (`null`). שדות נוספים, שאפשר להתעלם מהם:

- `upstream_category` - הקטגוריה המקורית ב-plenaryapp (למשל `Apple`, `Cricket`, `Country: India`).
- `country` - קוד מדינה (ISO) לפידים שהגיעו מקובצי המדינות.
- `last_item` - תאריך הפריט האחרון שנמצא בבדיקה.
- `source_url` - הכתובת כפי שהופיעה במקור (`url` מתעדכן ל-https כשהאתר מפנה לשם).

## מיפוי קטגוריות

- קובצי המדינות (חדשות כלליות לכל מדינה) נכנסים ל"חדשות ואקטואליה" עם שדה `country`.
- פיד עם פרקי אודיו (enclosure מסוג audio) נכנס ל"פודקאסטים", מכל נושא במקור.
- קטגוריות שאין להן מקבילה במקור נשארות ריקות: בריאות, הורות, דעות, קריירה, צרכנות.
- בינה מלאכותית: אין כזו במקור, אז הפידים באים מרשימה ידנית - [`curated.json`](curated.json) (מעבדות מחקר, ניוזלטרים, אתרי חדשות). הם עוברים את אותה בדיקה, והקטגוריה והשפה שלהם קבועות (פיד ידני עם פרקי אודיו לא עובר לפודקאסטים). Anthropic ו-Meta AI לא מפרסמות פיד רשמי, ולכן הפידים שלהן מגיעים מ-[Olshansk/rss-feeds](https://github.com/Olshansk/rss-feeds) (פיד קהילתי שנבנה מהאתר).

## סנכרון שבועי

`.github/workflows/sync-world.yml` רץ כל יום ראשון ומריץ את `scripts/sync_world.py`: מושך את הגרסה העדכנית של plenaryapp, מאמת מחדש את כל הפידים ומעדכן את הקבצים בתיקייה הזו. פיד שכבר בקטלוג יוצא רק אחרי שתי בדיקות שבועיות כושלות ברצף, ותשובת חסימה (401/403/429) לא נחשבת כישלון עבורו. אם יותר מ-40% מהפידים נכשלים בריצה אחת, הסקריפט לא כותב כלום (תקלת רשת, לא פידים מתים).

הרצה מקומית: `python scripts/sync_world.py`. אל תערכו את `world/feeds.json` ידנית - הוא נוצר מחדש בכל ריצה; שינויי מיפוי נעשים ב-`CATEGORY_MAP` בסקריפט, והוספת פיד ידני נעשית ב-`world/curated.json`. אחרי עריכה של `curated.json` אפשר להריץ `python scripts/sync_world.py --only-new` - בודק רק פידים שעוד לא נבדקו ומשאיר את השאר כמו שהם.

## הקטלוג

<!-- catalog:start -->
**572 פידים מאומתים ב-16 מתוך 21 קטגוריות** (עודכן 2026-09-24; 287 פידים מהמקור נפסלו בבדיקה - הפירוט ב-[`FEEDS-STATUS.md`](FEEDS-STATUS.md)).

| קטגוריה | פידים | קטגוריות במקור |
|---|---|---|
| חדשות ואקטואליה (News & Current Affairs) | 166 | News, כל קובצי המדינות |
| טכנולוגיה וגאדג'טים (Technology & Gadgets) | 81 | Tech, Android, Apple, Programming, Android Development, iOS Development, Web Development, UI - UX, Cyber security |
| כלכלה ועסקים (Economy & Business) | 45 | Business & Economy, Startups, Personal finance, Cryptocurrency |
| ספורט (Sports) | 25 | Sports, Football, Cricket, Tennis |
| תרבות ופנאי (Culture & Entertainment) | 22 | Movies, Television, Books, History, Photography |
| בריאות ורפואה (Health & Medicine) | 0 | - |
| מדע וסביבה (Science & Environment) | 32 | Science, Space, Environment, Nature, Animal & Wildlife |
| מוזיקה (Music) | 3 | Music |
| גיימינג (Gaming) | 21 | Gaming, Chess |
| אוכל וקולינריה (Food & Cooking) | 9 | Food |
| תיירות ופנאי (Travel & Leisure) | 8 | Travel |
| רכב ותחבורה (Cars & Transportation) | 9 | Cars |
| אופנה ולייף סטייל (Fashion & Lifestyle) | 13 | Fashion, Beauty |
| נדל"ן ועיצוב הבית (Real Estate & Home Design) | 27 | Interior design, Architecture, DIY |
| הורות ומשפחה (Parenting & Family) | 0 | - |
| דעה וטורים אישיים (Opinion & Personal Columns) | 0 | - |
| פודקאסטים (Podcasts) | 66 | כל פיד עם פרקי אודיו, מכל נושא |
| קריירה ועבודה (Career & Work) | 0 | - |
| צרכנות ומבצעים (Consumer & Deals) | 0 | - |
| תרבות דיגיטלית ורשת (Digital Culture & Web) | 23 | Funny, Memes |
| בינה מלאכותית (Artificial Intelligence) | 22 | רשימה ידנית (curated.json) |

### חדשות ואקטואליה (News & Current Affairs)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [BBC News](https://feeds.bbci.co.uk/news/world/rss.xml) | bbc.co.uk | en | News |
| [International: Top News And Analysis](https://www.cnbc.com/id/100727362/device/rss/rss.html) | cnbc.com | en | News |
| [NDTV News Search Records Found 1000](http://feeds.feedburner.com/ndtvnews-world-news) | ndtv.com | en | News |
| [NYT > World News](https://rss.nytimes.com/services/xml/rss/nyt/World.xml) | nytimes.com | en | News |
| [Top stories - Google News](https://news.google.com/rss) | news.google.com | en | News |
| [World](https://feeds.washingtonpost.com/rss/world) | washingtonpost.com | en | News |
| [World News](https://www.reddit.com/r/worldnews/.rss) | reddit.com | en | News |
| [World news \| The Guardian](https://www.theguardian.com/world/rss) | theguardian.com | en | News |
| [World News, Today World News, Latest International News, World Breaking News, Trending News of World - Times of India](https://timesofindia.indiatimes.com/rssfeeds/296589292.cms) | timesofindia.indiatimes.com | en | News |
| [ABC News](https://www.abc.net.au/news/feed/1948/rss.xml) | abc.net.au | en | Country: Australia |
| [Brisbane Times - Latest News](https://www.brisbanetimes.com.au/rss/feed.xml) | brisbanetimes.com.au | en | Country: Australia |
| [Business News - Latest Headlines](https://www.businessnews.com.au/rssfeed/latest.rss) | businessnews.com.au | en | Country: Australia |
| [Crikey](https://feeds.feedburner.com/com/rCTl) | crikey.com.au | en | Country: Australia |
| [Independent Australia](http://feeds.feedburner.com/IndependentAustralia) | independentaustralia.net | en | Country: Australia |
| [PerthNow](https://www.perthnow.com.au/news/feed) | perthnow.com.au | en | Country: Australia |
| [Sydney Morning Herald - Latest News](https://www.smh.com.au/rss/feed.xml) | smh.com.au | en | Country: Australia |
| [The Age - Latest News](https://www.theage.com.au/rss/feed.xml) | theage.com.au | en | Country: Australia |
| [The Canberra Times - Local News](https://www.canberratimes.com.au/rss.xml) | canberratimes.com.au | en | Country: Australia |
| [BD24Live.com](https://www.bd24live.com/feed/) | bd24live.com | en | Country: Bangladesh |
| [প্রথম আলো](https://www.prothomalo.com/feed/) | prothomalo.com | bn | Country: Bangladesh |
| [Brasil Wire](https://www.brasilwire.com/feed/) | brasilwire.com | en | Country: Brazil |
| [Folha de S.Paulo - Em cima da hora - Principal](https://feeds.folha.uol.com.br/emcimadahora/rss091.xml) | redir.folha.com.br | pt | Country: Brazil |
| [Jornal de Brasília](https://jornaldebrasilia.com.br/feed/) | jornaldebrasilia.com.br | pt | Country: Brazil |
| [The Rio Times](https://www.riotimesonline.com/feed/) | riotimesonline.com | en | Country: Brazil |
| [UOL](http://rss.home.uol.com.br/index.xml) | uol.com.br | pt | Country: Brazil |
| [CBC \| Top Stories News](https://www.cbc.ca/cmlink/rss-topstories) | cbc.ca | en | Country: Canada |
| [Financial Post](https://business.financialpost.com/feed/) | financialpost.com | en | Country: Canada |
| [globalnews.ca](https://globalnews.ca/feed/) | globalnews.ca | en | Country: Canada |
| [LaPresse.ca - Actualités](https://www.lapresse.ca/actualites/rss) | lapresse.ca | fr | Country: Canada |
| [National Post](https://nationalpost.com/feed) | nationalpost.com | en | Country: Canada |
| [Ottawa Citizen](https://ottawacitizen.com/feed) | ottawacitizen.com | en | Country: Canada |
| [The Province](https://theprovince.com/feed) | theprovince.com | en | Country: Canada |
| [Toronto Sun - RSS Feed](https://torontosun.com/category/news/feed) | torontosun.com | en | Country: Canada |
| [Aktuell - FAZ.NET](https://www.faz.net/rss/aktuell/) | faz.net | de | Country: Germany |
| [Deutsche Welle](https://rss.dw.com/rdf/rss-en-all) | dw.com | de | Country: Germany |
| [tagesschau.de - Die Nachrichten der ARD](http://www.tagesschau.de/xml/rss2) | tagesschau.de | de | Country: Germany |
| [ZEIT ONLINE \| Nachrichten, Hintergründe und Debatten](http://newsfeed.zeit.de/index) | zeit.de | de | Country: Germany |
| [EL PAÍS: el periódico global](https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada) | elpais.com | es | Country: Spain |
| [ElDiario.es - ElDiario.es](https://www.eldiario.es/rss/) | eldiario.es | es | Country: Spain |
| [España](https://rss.elconfidencial.com/espana/) | rss.elconfidencial.com | es | Country: Spain |
| [Euro Weekly News Spain](https://euroweeklynews.com/feed/) | euroweeklynews.com | en | Country: Spain |
| [huffingtonpost.es](https://www.huffingtonpost.es/feeds/index.xml) | huffingtonpost.es | es | Country: Spain |
| [Portada // expansion](https://e00-expansion.uecdn.es/rss/portada.xml) | expansion.com | es | Country: Spain |
| [The Local](https://feeds.thelocal.com/rss/es) | feeds.thelocal.com | en | Country: Spain |
| [france24.com](https://www.france24.com/en/rss) | france24.com | en | Country: France |
| [L'Obs - A la une](https://www.nouvelobs.com/a-la-une/rss.xml) | nouvelobs.com | fr | Country: France |
| [La Dépêche du Midi : actualités et info en direct de la région Occitanie et des environs - ladepeche.fr](https://www.ladepeche.fr/rss.xml) | ladepeche.fr | fr | Country: France |
| [Le Huffington Post](https://www.huffingtonpost.fr/feeds/index.xml) | huffingtonpost.fr | fr | Country: France |
| [Le Monde.fr - Actualités et Infos en France et dans le monde](https://www.lemonde.fr/rss/une.xml) | lemonde.fr | fr | Country: France |
| [Mediapart](https://www.mediapart.fr/articles/feed) | mediapart.fr | fr | Country: France |
| [Ouest-France - Actualité](https://www.ouest-france.fr/rss-en-continu.xml) | ouest-france.fr | fr | Country: France |
| [Paris Star](https://www.parisstaronline.com/feed) | parisstaronline.com | en | Country: France |
| [BBC News - Home](https://feeds.bbci.co.uk/news/rss.xml) | bbc.co.uk | en | Country: United Kingdom |
| [Daily Express :: News Feed](http://feeds.feedburner.com/daily-express-news-showbiz) | express.co.uk | en | Country: United Kingdom |
| [Home \| Mail Online](https://www.dailymail.co.uk/home/index.rss) | dailymail.com | en | Country: United Kingdom |
| [The Independent](https://www.independent.co.uk/news/uk/rss) | independent.co.uk | en | Country: United Kingdom |
| [Hong Kong Free Press HKFP](https://hongkongfp.com/feed/) | hongkongfp.com | en | Country: Hong Kong SAR China |
| [hongkongnews.net latest rss headlines](http://feeds.hongkongnews.net/rss/b82693edf38ebff8) | hongkongnews.net | en | Country: Hong Kong SAR China |
| [Republika Online RSS Feed](https://www.republika.co.id/rss/) | republika.co.id | id | Country: Indonesia |
| [All: BreakingNews.ie](https://feeds.breakingnews.ie/bntopstories) | breakingnews.ie | en | Country: Ireland |
| [Irish Mirror - Home](https://www.irishmirror.ie/?service=rss) | irishmirror.ie | en | Country: Ireland |
| [IrishCentral.com - Top Stories](https://feeds.feedburner.com/IrishCentral) | irishcentral.com | en | Country: Ireland |
| [IrishExaminer.com](https://feeds.feedburner.com/ietopstories) | feeds.feedburner.com | en | Country: Ireland |
| [The42](https://www.the42.ie/feed/) | the42.ie | en | Country: Ireland |
| [TheJournal.ie](https://www.thejournal.ie/feed/) | thejournal.ie | en | Country: Ireland |
| [BBC News - India](https://feeds.bbci.co.uk/news/world/asia/india/rss.xml) | bbc.co.uk | en | Country: India |
| [Business Line - Home](https://www.thehindubusinessline.com/feeder/default.rss) | thehindubusinessline.com | en | Country: India |
| [Deccan Chronicle - Latest India news \| Breaking news \| Hyderabad News \| World news \| Business news \| Politics \| Technology news](https://www.deccanchronicle.com/rss_feed/) | deccanchronicle.com | en | Country: India |
| [Free Press Journal](https://www.freepressjournal.in/stories.rss) | freepressjournal.in | en | Country: India |
| [Home Page](https://www.business-standard.com/rss/home_page_top_stories.rss) | business-standard.com | en | Country: India |
| [India News](https://www.dnaindia.com/feeds/india.xml) | dnaindia.com | en | Country: India |
| [India \| The Guardian](https://www.theguardian.com/world/india/rss) | theguardian.com | en | Country: India |
| [Latest And Breaking Hindi News Headlines, News In Hindi \| अमर उजाला हिंदी न्यूज़ \| - Amar Ujala](https://www.amarujala.com/rss/breaking-news.xml) | amarujala.com | hi | Country: India |
| [NDTV News -   Topstories](https://feeds.feedburner.com/ndtvnews-top-stories) | ndtv.com | en | Country: India |
| [OpIndia](https://feeds.feedburner.com/opindia) | opindia.com | en | Country: India |
| [Scroll.in](http://feeds.feedburner.com/ScrollinArticles.rss) | scroll.in | en | Country: India |
| [Swarajya](https://prod-qt-images.s3.amazonaws.com/production/swarajya/feed.xml) | swarajyamag.com | en | Country: India |
| [TechGenyz](http://feeds.feedburner.com/techgenyz) | techgenyz.com | en | Country: India |
| [The Hindu - Home](https://www.thehindu.com/feeder/default.rss) | thehindu.com | en | Country: India |
| [Times of India](https://timesofindia.indiatimes.com/rssfeedstopstories.cms) | timesofindia.indiatimes.com | en | Country: India |
| [देश \| दैनिक भास्कर](https://www.bhaskar.com/rss-feed/1061/) | bhaskar.com | hi | Country: India |
| [ઈન્ડિયા \| દિવ્ય ભાસ્કર](https://www.divyabhaskar.co.in/rss-feed/1037/) | divyabhaskar.co.in | gu | Country: India |
| [Adnkronos - ultimoratop](http://rss.adnkronos.com/RSS_PrimaPagina.xml) | adnkronos.com | it | Country: Italy |
| [Il Mattino Web](https://www.ilmattino.it/?sez=XML&args&p=search&args[box]=Home&limit=20&layout=rss) | ilmattino.it | it | Country: Italy |
| [Internazionale](https://www.internazionale.it/sitemaps/rss.xml) | internazionale.it | it | Country: Italy |
| [Italy \| The Guardian](https://www.theguardian.com/world/italy/rss) | theguardian.com | en | Country: Italy |
| [Libero Quotidiano](https://www.liberoquotidiano.it/rss.xml) | liberoquotidiano.it | it | Country: Italy |
| [Milan News](https://www.milannews.it/rss/) | milannews.it | it | Country: Italy |
| [Panorama](https://www.panorama.it/feeds/feed.rss) | panorama.it | it | Country: Italy |
| [Repubblica.it > Homepage](https://www.repubblica.it/rss/homepage/rss2.0.xml) | repubblica.it | it | Country: Italy |
| [RSS di   - ANSA.it](https://www.ansa.it/sito/ansait_rss.xml) | ansa.it | it | Country: Italy |
| [The Local](https://feeds.thelocal.com/rss/it) | feeds.thelocal.com | en | Country: Italy |
| [BRIDGE（ブリッジ）テクノロジー＆スタートアップ情報](http://feeds.feedburner.com/SdJapan) | thebridge.jp | ja | Country: Japan |
| [Japan Today](https://japantoday.com/feed) | japantoday.com | ja | Country: Japan |
| [News On Japan](http://www.newsonjapan.com/rss/top.xml) | newsonjapan.com | ja | Country: Japan |
| [NYT > Japan](https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/topic/destination/japan/rss.xml) | nytimes.com | en | Country: Japan |
| [ライブドアニュース - 主要トピックス](https://news.livedoor.com/topics/rss/top.xml) | news.livedoor.com | ja | Country: Japan |
| [朝日新聞デジタル](http://rss.asahi.com/rss/asahi/newsheadlines.rdf) | asahi.com | ja | Country: Japan |
| [24 Horas](https://24-horas.mx/feed/) | 24-horas.mx | es | Country: Mexico |
| [8 Columnas](https://8columnas.com.mx/feed/) | 8columnas.com.mx | es | Country: Mexico |
| [DEBATE](https://www.debate.com.mx/rss/feed.xml) | debate.com.mx | es | Country: Mexico |
| [El Financiero](https://www.elfinanciero.com.mx/arc/outboundfeeds/rss/?outputType=xml) | elfinanciero.com.mx | es | Country: Mexico |
| [El Informador :: Noticias de Jalisco, México, Deportes & Entretenimiento](https://www.informador.mx/rss/ultimas-noticias.xml) | informador.mx | es | Country: Mexico |
| [ElNorte](https://www.elnorte.com/rss/portada.xml) | elnorte.com | es | Country: Mexico |
| [Lo último en Vanguardia MX](https://vanguardia.com.mx/rss.xml) | vanguardia.com.mx | es | Country: Mexico |
| [Mexico News Daily](https://mexiconewsdaily.com/feed/) | mexiconewsdaily.com | en | Country: Mexico |
| [Mexico \| The Guardian](https://www.theguardian.com/world/mexico/rss) | theguardian.com | en | Country: Mexico |
| [Portada, El Siglo de Torreón](https://www.elsiglodetorreon.com.mx/index.xml) | elsiglodetorreon.com.mx | es | Country: Mexico |
| [Reforma](https://www.reforma.com/rss/portada.xml) | reforma.com | es | Country: Mexico |
| [Daily Post Nigeria](https://dailypost.ng/feed/) | dailypost.ng | en | Country: Nigeria |
| [Information Nigeria](https://www.informationng.com/feed) | informationng.com | en | Country: Nigeria |
| [Legit.ng](https://www.legit.ng/rss/all.rss) | legit.ng | en | Country: Nigeria |
| [Nigerian News. Latest Nigeria News. Your online Nigerian Newspaper.](http://feeds.feedburner.com/Nigerianeye) | nigerianeye.com | en | Country: Nigeria |
| [Premium Times Nigeria](https://www.premiumtimesng.com/feed) | premiumtimesng.com | en | Country: Nigeria |
| [Tribune Online](https://tribuneonlineng.com/feed/) | tribuneonlineng.com | en | Country: Nigeria |
| [BusinessWorld](https://bworldonline.com/feed/) | bworldonline.com | en | Country: Philippines |
| [Current PH](https://currentph.com/feed/) | currentph.com | en | Country: Philippines |
| [GMA News Online / News](https://data.gmanews.tv/gno/rss/news/feed.xml) | gmanetwork.com | en | Country: Philippines |
| [INQUIRER.net](https://www.inquirer.net/fullfeed/) | inquirer.net | en | Country: Philippines |
| [Interaksyon](https://www.interaksyon.com/feed/) | interaksyon.philstar.com | en | Country: Philippines |
| [philstar.com - RSS Headlines](https://www.philstar.com/rss/headlines) | philstar.com | en | Country: Philippines |
| [TechPinas : Philippines' Technology News, Tips and Reviews Blog](http://feeds.feedburner.com/Techpinas) | techpinas.com | en | Country: Philippines |
| [Top Gear: The Philippine authority on cars and the automotive industry](https://www.topgear.com.ph/feed/rss1) | topgear.com.ph | en | Country: Philippines |
| [UNBOX PH](https://unbox.ph/feed/) | unbox.ph | en | Country: Philippines |
| [News Blog](https://newsnblogs.com/feed/) | newsnblogs.com | en | Country: Pakistan |
| [The Express Tribune](https://tribune.com.pk/feed/home) | tribune.com.pk | en | Country: Pakistan |
| [The Nation - Top Stories](https://www.nation.com.pk/rss/top-stories) | nation.com.pk | en | Country: Pakistan |
| [UrduPoint.com All Urdu News](https://www.urdupoint.com/rss/urdupoint.rss) | urdupoint.com | ur | Country: Pakistan |
| [ایکسپریس اردو](https://www.express.pk/feed/) | express.pk | en | Country: Pakistan |
| [قومی خبریں](https://jang.com.pk/rss/1/1) | jang.com.pk | en | Country: Pakistan |
| [Dziennik.pl Dziennik - dziennik.pl](http://rss.dziennik.pl/Dziennik-PL/) | dziennik.pl | pl | Country: Poland |
| [GazetaPrawna.pl - biznes, podatki, prawo, finanse, wiadomości, praca](http://rss.gazetaprawna.pl/GazetaPrawna) | rss.gazetaprawna.pl | pl | Country: Poland |
| [https://www.rp.pl](https://www.rp.pl/rss/1019) | rp.pl | pl | Country: Poland |
| [Najnowsze](http://feeds.feedburner.com/wPolitycepl) | wpolityce.pl | pl | Country: Poland |
| [Newsweek Polska](https://www.newsweek.pl/rss.xml) | newsweek.pl | pl | Country: Poland |
| [RMF24.pl](https://www.rmf24.pl/feed) | rmf24.pl | pl | Country: Poland |
| [www.wirtualnemedia.pl](https://www.wirtualnemedia.pl/rss/wirtualnemedia_rss.xml) | wirtualnemedia.pl | pl | Country: Poland |
| [Lenta.ru : Новости](https://lenta.ru/rss) | lenta.ru | ru | Country: Russia |
| [Meduza.io](https://meduza.io/rss/all) | meduza.io | ru | Country: Russia |
| [PravdaReport](https://www.pravdareport.com/export.xml) | english.pravda.ru | en | Country: Russia |
| [RT - Daily news](https://www.rt.com/rss/) | rt.com | en | Country: Russia |
| [TASS](https://tass.com/rss/v2.xml) | tass.com | en | Country: Russia |
| [The Moscow Times - Independent News From Russia](https://www.themoscowtimes.com/rss/news) | themoscowtimes.com | en | Country: Russia |
| [Все материалы - Московский Комсомолец](https://www.mk.ru/rss/index.xml) | mk.ru | ru | Country: Russia |
| [Газета "Коммерсантъ". Главное](https://www.kommersant.ru/RSS/main.xml) | kommersant.ru | ru | Country: Russia |
| [Газета.Ru - Первая полоса](https://www.gazeta.ru/export/rss/first.xml) | gazeta.ru | ru | Country: Russia |
| [Российская Газета](https://rg.ru/xml/index.xml) | rg.ru | ru | Country: Russia |
| [Гордон - Самые популярные материалы](https://gordonua.com/xml/rss_category/top.html) | gordonua.com | ru | Country: Ukraine |
| [Еспресо - український погляд на світ!](https://espreso.tv/rss) | espreso.tv | uk | Country: Ukraine |
| [Информационное агентство УНИАН](https://rss.unian.net/site/news_rus.rss) | unian.net | uk | Country: Ukraine |
| [НВ](https://nv.ua/rss/all.xml) | nv.ua | ru | Country: Ukraine |
| [Новини на tsn.ua](https://tsn.ua/rss/full.rss) | tsn.ua | uk | Country: Ukraine |
| [Українська правда](https://www.pravda.com.ua/rss/) | pravda.com.ua | uk | Country: Ukraine |
| [Цензор.НЕТ - Новости](https://censor.net.ua/includes/news_ru.xml) | censor.net | ru | Country: Ukraine |
| [FOX News](http://feeds.foxnews.com/foxnews/latest) | foxnews.com | en | Country: United States |
| [NYT > Top Stories](https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml) | nytimes.com | en | Country: United States |
| [Playbook](https://rss.politico.com/playbook.xml) | rss.politico.com | en | Country: United States |
| [World & Nation](https://www.latimes.com/world-nation/rss2.0.xml) | latimes.com | en | Country: United States |
| [World News - Breaking News, Top Stories](https://www.huffpost.com/section/world-news/feed) | huffpost.com | en | Country: United States |
| [Axios](https://api.axios.com/feed/) | axios.com | en | Country: South Africa |
| [Daily Maverick](https://www.dailymaverick.co.za/dmrss/) | dailymaverick.co.za | en | Country: South Africa |
| [IOL section feed for News](https://rss.iol.io/iol/news) | iol.co.za | en | Country: South Africa |
| [Moneyweb](https://www.moneyweb.co.za/feed/) | moneyweb.co.za | en | Country: South Africa |
| [TechCentral](https://techcentral.co.za/feed/) | techcentral.co.za | en | Country: South Africa |
| [The Citizen](https://www.citizen.co.za/feed/) | citizen.co.za | en | Country: South Africa |
| [The South African](https://www.thesouthafrican.com/feed/) | thesouthafrican.com | en | Country: South Africa |

### טכנולוגיה וגאדג'טים (Technology & Gadgets)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [9to5Mac](https://9to5mac.com/feed/) | 9to5mac.com | en | Apple |
| [A List Apart: The Full Feed](https://alistapart.com/main/feed/) | alistapart.com | en | Web Development |
| [Alberto De Bortoli](https://albertodebortoli.com/rss/) | albertodebortoli.com | en | iOS Development |
| [Android](https://blog.google/products/android/rss) | blog.google | en | Android |
| [Android](https://www.reddit.com/r/android/.rss) | reddit.com | en | Android |
| [Android Authority](https://www.androidauthority.com/feed/) | androidauthority.com | en | Android |
| [Android Developers Blog](http://feeds.feedburner.com/blogspot/hsDu) | android-developers.googleblog.com | en | Android Development |
| [Apple Newsroom](https://www.apple.com/newsroom/rss-feed.rss) | apple.com | en | Apple |
| [AppleInsider News](https://appleinsider.com/rss/news/) | appleinsider.com | en | Apple |
| [Ars Technica - All content](http://feeds.arstechnica.com/arstechnica/index) | arstechnica.com | en | Tech |
| [Articles on Smashing Magazine — For Web Designers And Developers](https://www.smashingmagazine.com/feed) | smashingmagazine.com | en | UI - UX |
| [Blackhat Library: Hacking techniques and research](https://www.reddit.com/r/blackhat/.rss) | reddit.com | en | Cyber security |
| [CNET](https://www.cnet.com/rss/news/) | cnet.com | en | Tech |
| [Coding Horror](https://feeds.feedburner.com/codinghorror) | blog.codinghorror.com | en | Programming |
| [CSS-Tricks](https://css-tricks.com/feed/) | css-tricks.com | en | Web Development |
| [Cult of Mac](https://www.cultofmac.com/feed) | cultofmac.com | en | Apple |
| [Cyanogen Mods](https://cyanogenmods.org/feed/) | cyanogenmods.org | en | Android |
| [cybersecurity](https://www.reddit.com/r/cybersecurity/.rss) | reddit.com | en | Cyber security |
| [cybersecurity \| TechCrunch](https://techcrunch.com/tag/cybersecurity/feed/) | techcrunch.com | en | Cyber security |
| [Dan Lew Codes](https://blog.danlew.net/rss/) | blog.danlew.net | en | Android Development |
| [Daring Fireball](https://daringfireball.net/feeds/main) | daringfireball.net | en | Apple |
| [Darknet – Hacking Tools, Hacker News & Cyber Security](http://feeds.feedburner.com/darknethackers) | darknet.org.uk | en | Cyber security |
| [Developing Android Apps](https://www.reddit.com/r/androiddev.rss) | reddit.com | en | Android Development |
| [Droid Life – Opinionated Android news.](https://www.droid-life.com/feed/) | droid-life.com | en | Android |
| [Engadget - Technology News & Expert Reviews](https://www.engadget.com/rss.xml) | engadget.com | en | Tech |
| [Engineering at Meta](https://engineering.fb.com/feed/) | engineering.fb.com | en | Programming |
| [Engineering at Slack](https://slack.engineering/feed/) | slack.engineering | en | Programming |
| [Etsy Engineering \| Code as Craft](https://codeascraft.com/feed/atom/) | etsy.com | en | Programming |
| [GitLab](https://about.gitlab.com/atom.xml) | about.gitlab.com | en | Programming |
| [Gizmodo](https://gizmodo.com/rss) | gizmodo.com | en | Tech |
| [GSMArena.com - Latest articles](https://www.gsmarena.com/rss-news-reviews.php3) | gsmarena.com | en | Android |
| [Hacker News](https://news.ycombinator.com/rss) | news.ycombinator.com | en | Tech |
| [inessential.com](https://inessential.com/xml/rss.xml) | inessential.com | en | iOS Development |
| [InfoQ](https://feed.infoq.com) | infoq.com | en | Programming |
| [Jake Wharton](https://jakewharton.com/atom.xml) | jakewharton.com | en | Android Development |
| [JUST™ Creative](https://feeds.feedburner.com/JustCreativeDesignBlog) | justcreative.com | en | UI - UX |
| [Krebs on Security](https://krebsonsecurity.com/feed/) | krebsonsecurity.com | en | Cyber security |
| [Latest from Android Central](http://feeds.androidcentral.com/androidcentral) | androidcentral.com | en | Android |
| [Latest news](https://www.zdnet.com/topic/security/rss.xml) | zdnet.com | en | Cyber security |
| [Latest News - Apple Developer](https://developer.apple.com/news/rss/news.rss) | developer.apple.com | en | iOS Development |
| [Lifehacker](https://lifehacker.com/rss) | lifehacker.com | en | Tech |
| [Macworld](https://www.macworld.com/index.rss) | macworld.com | en | Apple |
| [Marco.org](https://marco.org/rss) | marco.org | en | Apple |
| [Martin Fowler](https://martinfowler.com/feed.atom) | martinfowler.com | en | Programming |
| [Mashable](http://feeds.mashable.com/Mashable) | mashable.com | en | Tech |
| [Mobile A11y](https://mobilea11y.com/index.xml) | mobilea11y.com | en | iOS Development |
| [NN/g latest articles and announcements](https://www.nngroup.com/feed/rss/) | nngroup.com | en | UI - UX |
| [NYT > Technology](https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml) | nytimes.com | en | Tech |
| [OS X Daily](http://feeds.feedburner.com/osxdaily) | osxdaily.com | en | Apple |
| [overreacted — A blog by Dan Abramov](https://overreacted.io/rss.xml) | overreacted.io | en | Programming |
| [ProAndroidDev - Medium](https://proandroiddev.com/feed) | proandroiddev.com | en | Android Development |
| [Public Object](https://publicobject.com/rss/) | publicobject.com | en | Android Development |
| [r/Apple: Unofficial Apple Community](https://www.reddit.com/r/apple/.rss) | reddit.com | en | Apple |
| [r/iPhone](https://www.reddit.com/r/iphone/.rss) | reddit.com | en | Apple |
| [ReadWrite](https://readwrite.com/feed/) | readwrite.com | en | Tech |
| [Schneier on Security](http://www.schneier.com/blog/index.rdf) | schneier.com | en | Cyber security |
| [Scott Hanselman's Blog](http://feeds.hanselman.com/ScottHanselman) | hanselman.com | en | Programming |
| [Scripting News](http://scripting.com/rss.xml) | scripting.com | en | Programming |
| [Security Affairs](http://securityaffairs.co/wordpress/feed) | securityaffairs.com | en | Cyber security |
| [Sink In - Tech Learnings](https://gosink.in/rss/) | gosink.in | en | Web Development |
| [Slashdot](https://rss.slashdot.org/Slashdot/slashdotMain) | slashdot.org | en | Tech |
| [SoundCloud Backstage Blog](https://developers.soundcloud.com/blog/blog.rss) | developers.soundcloud.com | en | Programming |
| [Stack Overflow Blog](https://stackoverflow.blog/feed/) | stackoverflow.blog | en | Programming |
| [Stratechery by Ben Thompson](https://stratechery.com/feed/) | stratechery.com | en | Tech |
| [Swift by Sundell](https://www.swiftbysundell.com/feed.rss) | swiftbysundell.com | en | iOS Development |
| [Swift by Sundell](https://swiftbysundell.com/feed.rss) | swiftbysundell.com | en | iOS Development |
| [TalkAndroid](http://feeds.feedburner.com/AndroidNewsGoogleAndroidForums) | talkandroid.com | en | Android |
| [Technical Information Security Content & Discussion](https://www.reddit.com/r/netsec/.rss) | reddit.com | en | Cyber security |
| [The Airbnb Tech Blog - Medium](https://medium.com/feed/airbnb-engineering) | medium.com | en | Programming |
| [The GitHub Blog](https://github.blog/feed/) | github.blog | en | Programming |
| [The Hacker News](http://thehackernews.com/feeds/posts/default) | thehackernews.com | en | Cyber security |
| [The Keyword](https://blog.google/rss/) | blog.google | en | Tech |
| [The Loop](https://loopinsight.com/feed/) | loopinsight.com | en | Apple |
| [The Next Web](https://thenextweb.com/feed) | thenextweb.com | en | Tech |
| [The One And Only Blog Of Joe Fabisevich](https://fabisevi.ch/feed.xml) | fabisevi.ch | en | iOS Development |
| [The Verge](https://www.theverge.com/rss/index.xml) | theverge.com | en | Tech |
| [User Experience](https://www.reddit.com/r/userexperience/.rss) | reddit.com | en | UI - UX |
| [UX Collective - Medium](https://uxdesign.cc/feed) | uxdesign.cc | en | UI - UX |
| [www.theregister.com - Articles](http://www.theregister.co.uk/security/headlines.atom) | theregister.com | en | Cyber security |
| [www.theregister.com - Articles](https://www.theregister.com/headlines.rss) | theregister.com | en | Tech |
| [Zac Sweers](https://www.zacsweers.dev/rss/) | zacsweers.dev | en | Android Development |

### כלכלה ועסקים (Economy & Business)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [All News](https://www.investing.com/rss/news.rss) | investing.com | en | Business & Economy |
| [Bitcoin - The Currency of the Internet](https://www.reddit.com/r/Bitcoin/.rss) | reddit.com | en | Cryptocurrency |
| [Bitcoin News](https://news.bitcoin.com/feed/) | news.bitcoin.com | en | Cryptocurrency |
| [Breaking News on Seeking Alpha](https://seekingalpha.com/market_currents.xml) | seekingalpha.com | en | Business & Economy |
| [Budgets Are Sexy](https://feeds2.feedburner.com/budgetsaresexy) | budgetsaresexy.com | en | Personal finance |
| [Cointelegraph.com News](https://cointelegraph.com/rss) | cointelegraph.com | en | Cryptocurrency |
| [Cryptocurrency News & Discussion](https://www.reddit.com/r/CryptoCurrency/.rss) | reddit.com | en | Cryptocurrency |
| [cryptocurrency \| TechCrunch](https://techcrunch.com/tag/cryptocurrency/feed/) | techcrunch.com | en | Cryptocurrency |
| [CryptoCurrency – Finance Magnates \| Financial and business news](https://www.financemagnates.com/cryptocurrency/feed/) | financemagnates.com | en | Cryptocurrency |
| [CryptoNinjas](https://www.cryptoninjas.net/feed/) | cryptoninjas.net | en | Cryptocurrency |
| [CryptoPotato](https://cryptopotato.com/feed/) | cryptopotato.com | en | Cryptocurrency |
| [DailyCoin](https://dailycoin.com/feed/) | dailycoin.com | en | Cryptocurrency |
| [Economic Times](https://economictimes.indiatimes.com/rssfeedsdefault.cms) | economictimes.indiatimes.com | en | Business & Economy |
| [Entrepreneur – Latest](http://feeds.feedburner.com/entrepreneur/latest) | entrepreneur.comrss-feed | en | Startups |
| [Ethereum](https://www.reddit.com/r/ethereum/.rss) | reddit.com | en | Cryptocurrency |
| [Ethereum Foundation Blog](https://blog.ethereum.org/feed.xml) | blog.ethereum.org | en | Cryptocurrency |
| [Feld Thoughts](https://feld.com/feed) | feld.com | en | Startups |
| [Financial Samurai](https://www.financialsamurai.com/feed/) | financialsamurai.com | en | Personal finance |
| [Forbes - Business](https://www.forbes.com/business/feed/) | forbes.com | en | Business & Economy |
| [Fortune \| FORTUNE](https://fortune.com/feed) | fortune.com | en | Business & Economy |
| [Hacker News: Front Page](https://hnrss.org/frontpage) | news.ycombinator.com | en | Startups |
| [Inc.com](https://www.inc.com/rss/) | inc.com | en | Startups |
| [INCRYPTED](https://incrypted.net/feed/) | incrypted.com | ru | Cryptocurrency |
| [Kraken Blog](https://blog.kraken.com/feed) | blog.kraken.com | en | Cryptocurrency |
| [Making Sense Of Cents](https://www.makingsenseofcents.com/feed) | makingsenseofcents.com | en | Personal finance |
| [Money Crashers](https://www.moneycrashers.com/feed/) | moneycrashers.com | en | Personal finance |
| [Money Saving Mom®](https://moneysavingmom.com/feed/) | moneysavingmom.com | en | Personal finance |
| [Money Under 30](https://www.moneyunder30.com/feed/) | moneyunder30.com | en | Personal finance |
| [MoneyNing](http://feeds.feedburner.com/MoneyNing) | moneyning.com | en | Personal finance |
| [NerdWallet](https://www.nerdwallet.com/blog/feed/) | nerdwallet.com | en | Personal finance |
| [News - Cryptonews](https://cryptonews.com/news/feed/) | cryptonews.com | en | Cryptocurrency |
| [NewsBTC](https://www.newsbtc.com/feed/) | newsbtc.com | en | Cryptocurrency |
| [Product Hunt — The best new products, every day](https://www.producthunt.com/feed) | producthunt.com | en | Startups |
| [SavingAdvice.com Blog](https://www.savingadvice.com/feed/) | savingadvice.com | en | Personal finance |
| [Small Business Trends](https://feeds2.feedburner.com/SmallBusinessTrends) | smallbiztrends.com | en | Startups |
| [Steve Blank](https://steveblank.com/feed/) | steveblank.com | en | Startups |
| [The College Investor](https://thecollegeinvestor.com/feed/) | thecollegeinvestor.com | en | Personal finance |
| [The Intercom Blog](https://www.intercom.com/blog/feed/) | intercom.com | en | Startups |
| [The Market's Compass Technical View](https://themarketscompass.substack.com/feed) | themarketscompass.substack.com | en | Cryptocurrency |
| [US Top News and Analysis](https://www.cnbc.com/id/100003114/device/rss/rss.html) | cnbc.com | en | Business & Economy |
| [VentureBeat](https://feeds.feedburner.com/venturebeat/SZYF) | venturebeat.com | en | Startups |
| [Well Kept Wallet](https://wellkeptwallet.com/feed/) | wellkeptwallet.com | en | Personal finance |
| [Wise Bread](http://feeds.killeraces.com/wisebread) | wisebread.com | en | Personal finance |
| [Yahoo Finance](https://finance.yahoo.com/news/rssindex) | finance.yahoo.com | en | Business & Economy |
| [ZebPay](https://zebpay.com/feed) | zebpay.com | en | Cryptocurrency |

### ספורט (Sports)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [BBC Sport](https://feeds.bbci.co.uk/sport/cricket/rss.xml) | bbc.co.uk | en | Cricket |
| [BBC Sport](https://feeds.bbci.co.uk/sport/football/rss.xml) | bbc.co.uk | en | Football |
| [BBC Sport](https://feeds.bbci.co.uk/sport/rss.xml) | bbc.co.uk | en | Sports |
| [BBC Sport](https://feeds.bbci.co.uk/sport/tennis/rss.xml) | bbc.co.uk | en | Tennis |
| [Cricket](https://www.reddit.com/r/Cricket/.rss) | reddit.com | en | Cricket |
| [Cricket news from ESPN Cricinfo.com](http://www.espncricinfo.com/rss/content/story/feeds/0.xml) | cricinfo.com | en | Cricket |
| [Cricket News Today, Latest Cricket Updates, Cricket Live Score, Upcoming Matches \| Times of India](https://timesofindia.indiatimes.com/rssfeeds/54829575.cms) | timesofindia.indiatimes.com | en | Cricket |
| [Cricket News: Stories, Features, Interviews, Opinion, Reports \| Wisden](https://www.wisden.com/feed) | wisden.com | en | Cricket |
| [Cricket \| The Guardian](https://www.theguardian.com/sport/cricket/rss) | theguardian.com | en | Cricket |
| [EFL Championship](https://www.reddit.com/r/Championship/.rss?format=xml) | reddit.com | en | Football |
| [Football - The People's Sport](https://www.reddit.com/r/football/.rss?format=xml) | reddit.com | en | Football |
| [Football News, Football Scores, Premier League, La Liga, ISL \| The Hindu](https://www.thehindu.com/sport/football/feeder/default.rss) | thehindu.com | en | Football |
| [Football \| The Guardian](https://www.theguardian.com/football/rss) | theguardian.com | en | Football |
| [NDTV News Search Records Found 1000](http://feeds.feedburner.com/ndtvsports-cricket) | ndtv.com | en | Cricket |
| [NYT > Sports > Soccer](https://rss.nytimes.com/services/xml/rss/nyt/Soccer.xml) | nytimes.com | en | Football |
| [NYT > Sports > Tennis](https://rss.nytimes.com/services/xml/rss/nyt/Tennis.xml) | nytimes.com | en | Tennis |
| [Perfect Tennis](https://www.perfect-tennis.com/feed/) | perfect-tennis.com | en | Tennis |
| [Soccer News](https://www.soccernews.com/feed/) | soccernews.com | en | Football |
| [Sport \| The Guardian](https://www.theguardian.com/uk/sport/rss) | theguardian.com | en | Sports |
| [Sports News - Latest Sports and Football News \| Sky News](https://feeds.skynews.com/feeds/rss/sports.xml) | news.sky.com | en | Sports |
| [Sports News: Cricket Live Scorecard, Latest Cricket News, Football, NBA, NFL, WWE, NHL, MLB News & More](https://timesofindia.indiatimes.com/rssfeeds/4719148.cms) | timesofindia.indiatimes.com | en | Sports |
| [sports.yahoo.com](https://sports.yahoo.com/rss/) | sports.yahoo.com | en | Sports |
| [Tennis News & Discussion](https://www.reddit.com/r/tennis/.rss) | reddit.com | en | Tennis |
| [Tennis News, Updates, Tennis Scores, ATP, WTA, Grand Slams \| The Hindu](https://www.thehindu.com/sport/tennis/feeder/default.rss) | thehindu.com | en | Tennis |
| [Tennis \| The Guardian](https://www.theguardian.com/sport/tennis/rss) | theguardian.com | en | Tennis |

### תרבות ופנאי (Culture & Entertainment)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [/Film](https://feeds2.feedburner.com/slashfilm) | slashfilm.com | en | Movies |
| [500px](https://iso.500px.com/feed/) | iso.500px.com | en | Photography |
| [A year of reading the world](https://ayearofreadingtheworld.com/feed/) | ayearofreadingtheworld.com | en | Books |
| [Ain't It Cool News Feed](https://www.aintitcool.com/node/feed/) | aintitcool.com | en | Movies |
| [BOOK RIOT](https://bookriot.com/feed/) | bookriot.com | en | Books |
| [ComingSoon.net – Movie Trailers, TV & Streaming News, and More](https://www.comingsoon.net/feed) | comingsoon.net | en | Movies |
| [Deadline](https://deadline.com/feed/) | deadline.com | en | Movies |
| [Digital Photography School](https://feeds.feedburner.com/DigitalPhotographySchool) | digital-photography-school.com | en | Photography |
| [FirstShowing.net](https://www.firstshowing.net/feed/) | firstshowing.net | en | Movies |
| [History in 28-minutes](https://www.historyisnowmagazine.com/blog?format=RSS) | historyisnowmagazine.com | en | History |
| [IndieWire](https://www.indiewire.com/feed/) | indiewire.com | en | Movies |
| [Light Stalking](https://www.lightstalking.com/feed/) | lightstalking.com | en | Photography |
| [Movie News and Discussion](https://www.reddit.com/r/movies/.rss) | reddit.com | en | Movies |
| [Movies](https://bleedingcool.com/movies/feed/) | bleedingcool.com | en | Movies |
| [NewInBooks](https://www.newinbooks.com/feed/) | newinbooks.com | en | Books |
| [PetaPixel](https://petapixel.com/feed/) | petapixel.com | en | Photography |
| [So many books, so little time](https://www.reddit.com/r/books/.rss) | reddit.com | en | Books |
| [Strobist](http://feeds.feedburner.com/blogspot/WOBq) | strobist.blogspot.com | en | Photography |
| [TV Fanatic](https://www.tvfanatic.com/rss.xml) | tvfanatic.com | en | Television |
| [TVLine - All TV. No Interference. TV News & Spoilers by TVLine](https://www.tvline.com/feed/) | tvline.com | en | Television |
| [Variety](https://variety.com/feed/) | variety.com | en | Movies |
| [📺Television News and Discussion](https://www.reddit.com/r/television/.rss) | reddit.com | en | Television |

### מדע וסביבה (Science & Environment)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [BBC News](https://feeds.bbci.co.uk/news/science_and_environment/rss.xml) | bbc.co.uk | en | Science |
| [BLOG POSTS – Mark Avery](https://markavery.info/blog/feed/) | markavery.info | en | Nature |
| [Blog \| Nature \| PBS](https://www.pbs.org/wnet/nature/blog/feed/) | pbs.org | en | Nature |
| [EarthPorn: Amazing images of light and landscape](https://www.reddit.com/r/EarthPorn/.rss) | reddit.com | en | Nature |
| [Environment](https://www.reddit.com/r/environment/.rss) | reddit.com | en | Environment |
| [Environment + Energy – The Conversation](https://theconversation.com/au/environment/articles.atom) | theconversation.com | en | Environment |
| [Environment News, Earth News, Global Warming, Wild Life, Carbon Trading, Climate Business, Climate Change & Pollution News](https://timesofindia.indiatimes.com/rssfeeds/2647163.cms) | timesofindia.indiatimes.com | en | Environment |
| [Environment \| The Guardian](https://www.theguardian.com/us/environment/rss) | theguardian.com | en | Environment |
| [FlowingData](https://flowingdata.com/feed) | flowingdata.com | en | Science |
| [Good Good Good](https://www.goodgoodgood.co/articles/rss.xml) | goodgoodgood.co | en | Environment |
| [Latest Science News -- ScienceDaily](https://www.sciencedaily.com/rss/all.xml) | sciencedaily.com | en | Science |
| [NASA](https://www.nasa.gov/rss/dyn/breaking_news.rss) | nasa.gov | en | Space |
| [Nature](http://feeds.nature.com/nature/rss/current?x=1) | feeds.nature.com | en | Nature |
| [Nature](https://www.reddit.com/r/nature/.rss) | reddit.com | en | Nature |
| [Nature](https://www.nature.com/nature.rss) | feeds.nature.com | en | Science |
| [Nature Gifs](https://www.reddit.com/r/NatureGifs/.rss) | reddit.com | en | Nature |
| [New Scientist - Space](https://www.newscientist.com/subject/space/feed/) | newscientist.com | en | Space |
| [NPR Topics: Environment](https://feeds.npr.org/1025/rss.xml) | npr.org | en | Environment |
| [NYT > Climate and Environment](https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml) | nytimes.com | en | Environment |
| [NYT > Science](https://rss.nytimes.com/services/xml/rss/nyt/Science.xml) | nytimes.com | en | Science |
| [Phys.org - latest science and technology news stories](https://phys.org/rss-feed/) | phys.org | en | Science |
| [Popular Science](https://www.popsci.com/arcio/rss/) | popsci.com | en | Science |
| [Prakati India](https://prakati.in/feed/) | prakati.in | en | Environment |
| [Reflections of the Natural World](https://reflectionsofthenaturalworld.com/feed/) | reflectionsofthenaturalworld.com | en | Nature |
| [Science](https://gizmodo.com/tag/science/rss) | gizmodo.com | en | Science |
| [Science Latest](https://www.wired.com/feed/category/science/latest/rss) | wired.com | en | Science |
| [Scientific American Content: Global](http://rss.sciam.com/ScientificAmerican-Global) | scientificamerican.com | en | Science |
| [Space \| The Guardian](https://www.theguardian.com/science/space/rss) | theguardian.com | en | Space |
| [Stories Archives - Nature Canada](https://naturecanada.ca/category/news/blog/feed/) | naturecanada.ca | en | Nature |
| [Wildlife Photography: Gear, Photos & Discussion](https://www.reddit.com/r/wildlifephotography/.rss) | reddit.com | en | Animal & Wildlife |
| [Wildlife \| The Guardian](https://www.theguardian.com/environment/wildlife/rss) | theguardian.com | en | Animal & Wildlife |
| [🔥 Nature Is Fucking Lit](https://www.reddit.com/r/NatureIsFuckingLit/.rss) | reddit.com | en | Animal & Wildlife |

### מוזיקה (Music)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Consequence](http://consequenceofsound.net/feed) | consequence.net | en | Music |
| [Music Business Worldwide](https://www.musicbusinessworldwide.com/feed/) | musicbusinessworldwide.com | en | Music |
| [RSS: News](http://pitchfork.com/rss/news) | pitchfork.com | en | Music |

### גיימינג (Gaming)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Better Chess](https://betterchess.net/feed/) | betterchess.net | en | Chess |
| [Chess News](https://en.chessbase.com/feed) | en.chessbase.com | en | Chess |
| [Chess \| The Guardian](https://www.theguardian.com/sport/chess/rss) | theguardian.com | en | Chess |
| [Chess.com News](https://www.chess.com/rss/news) | chess.com | en | Chess |
| [Chessable Blog](https://www.chessable.com/blog/feed/) | chessable.com | en | Chess |
| [Eurogamer.net Latest Articles Feed](https://www.eurogamer.net/?format=rss) | eurogamer.net | en | Gaming |
| [For the budding patzer](https://www.reddit.com/r/chessbeginners/.rss) | reddit.com | en | Chess |
| [GameSpot - All Content](https://www.gamespot.com/feeds/mashup/) | gamespot.com | en | Gaming |
| [IGN Articles](http://feeds.ign.com/ign/all) | ign.com | en | Gaming |
| [Indie Games Plus](https://indiegamesplus.com/feed/) | indiegamesplus.com | en | Gaming |
| [Kotaku](https://kotaku.com/rss) | kotaku.com | en | Gaming |
| [Lichess's Blog](https://lichess.org/blog.atom) | lichess.org | en | Chess |
| [PlayStation.Blog](http://feeds.feedburner.com/psblog) | blog.playstation.com | en | Gaming |
| [Polygon.com](https://www.polygon.com/rss/index.xml) | polygon.com | en | Gaming |
| [r/Chess](https://www.reddit.com/r/chess/.rss) | reddit.com | en | Chess |
| [r/gaming](https://www.reddit.com/r/gaming.rss) | reddit.com | en | Gaming |
| [Rock, Paper, Shotgun](http://feeds.feedburner.com/RockPaperShotgun) | rockpapershotgun.com | en | Gaming |
| [The Ancient Gaming Noob](http://feeds.feedburner.com/TheAncientGamingNoob) | tagn.wordpress.com | en | Gaming |
| [The Escapist](https://www.escapistmagazine.com/v2/feed/) | escapistmagazine.com | en | Gaming |
| [The Week in Chess](https://theweekinchess.com/twic-rss-feed) | theweekinchess.com | en | Chess |
| [TouchArcade - iPhone, iPad, Android Games Forum](https://toucharcade.com/community/forums/-/index.rss) | toucharcade.com | en | Gaming |

### אוכל וקולינריה (Food & Cooking)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Budget Bytes](http://budgetbytes.blogspot.com/feeds/posts/default) | budgetbytes.com | en | Food |
| [David Lebovitz](https://www.davidlebovitz.com/feed/) | davidlebovitz.com | en | Food |
| [How Sweet Eats](https://www.howsweeteats.com/feed/) | howsweeteats.com | en | Food |
| [Kitchn \| Inspiring cooks, nourishing homes](https://www.thekitchn.com/main.rss) | thekitchn.com | en | Food |
| [Love and Lemons](https://www.loveandlemons.com/feed/) | loveandlemons.com | en | Food |
| [Love and Olive Oil](https://www.loveandoliveoil.com/feed) | loveandoliveoil.com | en | Food |
| [NYT > Food](https://rss.nytimes.com/services/xml/rss/nyt/DiningandWine.xml) | nytimes.com | en | Food |
| [Shutterbean](https://www.shutterbean.com/feed/) | shutterbean.com | en | Food |
| [smitten kitchen](http://feeds.feedburner.com/smittenkitchen) | smittenkitchen.com | en | Food |

### תיירות ופנאי (Travel & Leisure)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Adventure.com](https://adventure.com/feed/) | adventure.com | en | Travel |
| [Atlas Obscura - Latest Articles and Places](https://www.atlasobscura.com/feeds/latest) | atlasobscura.com | en | Travel |
| [Everything Everywhere](http://feeds2.feedburner.com/EverythingEverywhere/) | everything-everywhere.com | en | Travel |
| [NYT > Travel](https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml) | nytimes.com | en | Travel |
| [The Points Guy Articles](http://feeds.feedburner.com/thepointsguy) | thepointsguy.com | en | Travel |
| [Travel Blog -](https://www.nomadicmatt.com/travel-blog/feed/) | nomadicmatt.com | en | Travel |
| [Travel Dudes](https://traveldudes.com/feed/) | traveldudes.com | en | Travel |
| [Travel \| The Guardian](https://www.theguardian.com/uk/travel/rss) | theguardian.com | en | Travel |

### רכב ותחבורה (Cars & Transportation)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Autocar RSS Feed](https://www.autocar.co.uk/rss) | autocar.co.uk | en | Cars |
| [BikeEXIF](https://www.bikeexif.com/feed) | bikeexif.com | en | Cars |
| [BMWBLOG](https://feeds.feedburner.com/BmwBlog) | bmwblog.com | en | Cars |
| [Carscoops](https://www.carscoops.com/feed/) | carscoops.com | en | Cars |
| [Formula 1](https://www.reddit.com/r/formula1/.rss) | reddit.com | en | Cars |
| [Jalopnik - Obsessed with the culture of cars](https://jalopnik.com/rss) | jalopnik.com | en | Cars |
| [Latest Content - Car and Driver](https://www.caranddriver.com/rss/all.xml/) | caranddriver.com | en | Cars |
| [The best vintage and classic cars for sale online \| Bring a Trailer](https://bringatrailer.com/feed/) | bringatrailer.com | en | Cars |
| [TheTruthAboutCars](https://www.thetruthaboutcars.com/feed/) | thetruthaboutcars.com | en | Cars |

### אופנה ולייף סטייל (Fashion & Lifestyle)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Beauty - ELLE](https://www.elle.com/rss/beauty.xml/) | elle.com | en | Beauty |
| [Fashion - ELLE](https://www.elle.com/rss/fashion.xml/) | elle.com | en | Fashion |
| [Fashion \| The Guardian](https://www.theguardian.com/fashion/rss) | theguardian.com | en | Fashion |
| [fashionbeans.com](https://www.fashionbeans.com/rss-feed/?category=fashion) | fashionbeans.com | en | Fashion |
| [Fashionista Full](https://fashionista.com/.rss/excerpt/beauty) | fashionista.com | en | Beauty |
| [Fashionista Full](https://fashionista.com/.rss/excerpt/) | fashionista.com | en | Fashion |
| [Latest from Who What Wear](https://www.whowhatwear.com/rss) | whowhatwear.com | en | Fashion |
| [NYT > Style](https://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml) | nytimes.com | en | Fashion |
| [POPSUGAR Beauty](https://www.popsugar.com/beauty/feed) | popsugar.com | en | Beauty |
| [POPSUGAR Fashion](https://www.popsugar.com/fashion/feed) | popsugar.com | en | Fashion |
| [Refinery29](https://www.refinery29.com/beauty/rss.xml) | refinery29.com | en | Beauty |
| [Refinery29](https://www.refinery29.com/fashion/rss.xml) | refinery29.com | en | Fashion |
| [The Beauty Look Book](https://thebeautylookbook.com/feed) | thebeautylookbook.com | en | Beauty |

### נדל"ן ועיצוב הבית (Real Estate & Home Design)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [A Beautiful Mess](https://abeautifulmess.com/feed/) | abeautifulmess.com | en | DIY |
| [ArchDaily Global](http://feeds.feedburner.com/Archdaily) | archdaily.com | en | Architecture |
| [Architectural Digest](https://www.architecturaldigest.com/feed/rss) | architecturaldigest.com | en | Architecture |
| [Architecture](https://www.reddit.com/r/architecture/.rss) | reddit.com | en | Architecture |
| [architecture archives \| designboom \| architecture & design magazine](https://www.designboom.com/architecture/feed/) | designboom.com | en | Architecture |
| [Architecture news and projects \| Dezeen](https://www.dezeen.com/architecture/feed/) | dezeen.com | en | Architecture |
| [BLOG - decor8](https://www.decor8blog.com/blog?format=rss) | decor8blog.com | en | Interior design |
| [Blog – Hackaday](https://hackaday.com/blog/feed/) | hackaday.com | en | DIY |
| [Core77](http://feeds.feedburner.com/core77/blog) | core77.com | en | Interior design |
| [design archives \| designboom \| architecture & design magazine](https://www.designboom.com/design/feed/) | designboom.com | en | Interior design |
| [Design MilkArchitecture, Architectural Designs, and House Designs \| Design Milk](https://design-milk.com/category/architecture/feed/) | design-milk.com | en | Architecture |
| [Design MilkInterior Design Ideas for Your Modern Home \| Design Milk](https://design-milk.com/category/interior-design/feed/) | design-milk.com | en | Interior design |
| [Fubiz Media](http://feeds.feedburner.com/fubiz) | fubiz.net | fr | Interior design |
| [How-To Geek](https://www.howtogeek.com/feed/) | howtogeek.com | en | DIY |
| [IKEA Hackers](https://ikeahackers.net/feed) | ikeahackers.net | en | DIY |
| [In My Own Style](https://inmyownstyle.com/feed) | inmyownstyle.com | en | Interior design |
| [Interior Design (Interior Architecture)](https://www.reddit.com/r/InteriorDesign/.rss) | reddit.com | en | Interior design |
| [Interior Design Ideas](https://www.home-designing.com/feed) | home-designing.com | en | Interior design |
| [Interior design \| Dezeen](https://www.dezeen.com/interiors/feed/) | dezeen.com | en | Interior design |
| [Latest from Ideal Home in News](https://www.idealhome.co.uk/feed) | idealhome.co.uk | en | Interior design |
| [MakeUseOf](https://www.makeuseof.com/feed/) | makeuseof.com | en | DIY |
| [The Inspired Room](https://theinspiredroom.net/feed/) | theinspiredroom.net | en | Interior design |
| [Thrifty Decor Chick \| Thrifty DIY, Decor and Organizing](http://feeds.feedburner.com/blogspot/ZBcZ) | thriftydecorchick.com | en | Interior design |
| [Trendir](https://www.trendir.com/feed/) | trendir.com | en | Interior design |
| [Yanko Design](http://feeds.feedburner.com/yankodesign) | yankodesign.com | en | Interior design |
| [Yatzer \| Live Beautifully. Explore Endlessly.](https://www.yatzer.com/rss.xml) | yatzer.com | en | Interior design |
| [Young House Love](https://www.younghouselove.com/feed/) | younghouselove.com | en | Interior design |

### פודקאסטים (Podcasts)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [30 for 30 Podcasts](https://feeds.megaphone.fm/ESP5765452710) | espnradio.espn.com | en | History |
| [60-Second Science](http://rss.sciam.com/sciam/60secsciencepodcast) | sciencequickly.com | en | Science |
| [Accidental Tech Podcast](https://atp.fm/rss) | atp.fm | en | Tech |
| [Analog(ue)](https://relay.fm/analogue/feed) | relay.fm | en | Tech |
| [Android Developers Backstage](http://feeds.feedburner.com/blogspot/androiddevelopersbackstage) | androidbackstage.blogspot.com | en | Android Development |
| [Bitcoin Audible](https://bitcoinaudible.com/feed/) | bitcoinaudible.com | en | Cryptocurrency |
| [Blind Android Users Podcast](https://anchor.fm/s/4495abac/podcast/rss) | blindandroidusers.com | en | Android |
| [Clockwise](https://relay.fm/clockwise/feed) | relay.fm | en | Tech |
| [CyberWire Daily](https://feeds.megaphone.fm/cyberwire-daily-podcast) | thecyberwire.com | en | Cyber security |
| [Dan Carlin's Hardcore History](https://feeds.feedburner.com/dancarlin/history?format=xml) | dancarlin.com | en | History |
| [Darknet Diaries](https://feeds.megaphone.fm/darknetdiaries) | darknetdiaries.com | en | Cyber security |
| [Developer Tea](https://feeds.simplecast.com/dLRotFGk) | developertea.com | en | Programming |
| [Discovery](https://podcasts.files.bbci.co.uk/p002w557.rss) | bbc.co.uk | en | Science |
| [EconTalk](https://feeds.simplecast.com/wgl4xEgL) | simplecast.econtalk.org | en | Business & Economy |
| [Epicenter - Learn about Crypto, Blockchain, Ethereum, Bitcoin and Distributed Technologies](https://feeds.simplecast.com/lKmQDG9R) | epicenter.tv | en | Cryptocurrency |
| [Fragmented - AI Developer Podcast](https://feeds.simplecast.com/LpAGSLnY) | fragmentedpodcast.com | en | Android Development |
| [Gastropod](https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/2a195077-f014-41d2-8313-ab190186b4c2/277bcd5c-0a05-4c14-8ba6-ab190186b4d5/podcast.rss) | gastropod.com | en | Science |
| [Hacking Humans](https://feeds.megaphone.fm/hacking-humans) | thecyberwire.com | en | Cyber security |
| [Hanselminutes with Scott Hanselman](https://feeds.simplecast.com/gvtxUiIf) | hanselminutes.com | en | Programming |
| [HBR IdeaCast](http://feeds.harvardbusiness.org/harvardbusiness/ideacast) | hbr.org | en | Business & Economy |
| [Hidden Brain](https://feeds.npr.org/510308/podcast.xml) | siriusxm.com | en | Science |
| [How I Built This with Guy Raz](https://feeds.npr.org/510313/podcast.xml) | wondery.com | en | Business & Economy |
| [Interviews](https://feed.podbean.com/nuggetsnews/feed.xml) | nuggetsnews.podbean.com | en | Cryptocurrency |
| [Invest Like the Best with Patrick O'Shaughnessy](http://investlikethebest.libsyn.com/rss) | colossus.com | en | Personal finance |
| [Invisibilia](https://feeds.npr.org/510307/podcast.xml) | npr.org | en | Science |
| [ISF Podcast](https://audioboom.com/channels/4991893.rss) | securityforum.org | en | Cyber security |
| [MacStories](https://www.macstories.net/feed/) | macstories.net | en | Apple |
| [Masters of Scale](https://rss.art19.com/masters-of-scale) | mastersofscale.com | en | Startups |
| [Money For the Rest of Us](https://rss.art19.com/money-for-the-rest-of-us) | moneyfortherestofus.com | en | Personal finance |
| [MyWifeQuitHerJob.com](https://mywifequitherjob.com/feed/) | mywifequitherjob.com | en | Personal finance |
| [Nerd's Eye View \| Kitces.com](http://feeds.feedblitz.com/kitcesnerdseyeview&x=1) | kitces.com | en | Personal finance |
| [Perpetual Chess Podcast](https://feeds.megaphone.fm/BLU4811105299) | perpetualchesspod.com | en | Chess |
| [Planet Money](https://feeds.npr.org/510289/podcast.xml) | npr.org | en | Business & Economy |
| [Podcast Archives - Software Engineering Daily](https://softwareengineeringdaily.com/category/podcast/feed) | softwareengineeringdaily.com | en | Programming |
| [Probably Science](https://probablyscience.libsyn.com/rss) | probablyscience.com | en | Science |
| [Programming Throwdown](http://feeds.feedburner.com/ProgrammingThrowdown) | programmingthrowdown.com | en | Programming |
| [Radiolab](http://feeds.wnyc.org/radiolab) | radiolab.org | en | Science |
| [Risky Business](https://risky.biz/feeds/risky-business/) | risky.biz | en | Cyber security |
| [Sawbones: A Marital Tour of Misguided Medicine](https://feeds.simplecast.com/y1LF_sn2) | maximumfun.org | en | Science |
| [Shirtloads of Science](https://shirtloadsofscience.libsyn.com/rss) | shirtloadsofscience.libsyn.com | en | Science |
| [Smashing Security](http://www.smashingsecurity.com/rss) | smashingsecurity.com | en | Cyber security |
| [So Money with Farnoosh Torabi](https://feeds.megaphone.fm/somoney) | somoneypodcast.com | en | Personal finance |
| [Software Defined Talk](https://feeds.fireside.fm/sdt/rss) | softwaredefinedtalk.com | en | Programming |
| [Software Engineering Radio - The Podcast for Professional Software Developers](http://feeds.feedburner.com/se-radio) | se-radio.net | en | Programming |
| [Song Exploder](https://feed.songexploder.net/songexploder) | songexploder.net | en | Music |
| [Stephan Livera Podcast](https://anchor.fm/s/7d083a4/podcast/rss) | stephanlivera.com | en | Cryptocurrency |
| [Stumped](https://podcasts.files.bbci.co.uk/p02gsrmh.rss) | bbc.co.uk | en | Cricket |
| [Switch Hit Podcast](https://feeds.megaphone.fm/ESP9247246951) | espncricinfo.com | en | Cricket |
| [Tailenders](https://podcasts.files.bbci.co.uk/p02pcb4w.rss) | bbc.co.uk | en | Cricket |
| [TED Talks Daily](https://pa.tedcdn.com/feeds/talks.rss) | ted.com | en | Science |
| [Test Match Special](https://podcasts.files.bbci.co.uk/p02nrsl2.rss) | bbc.co.uk | en | Cricket |
| [The Bitcoin Podcast](https://feeds.simplecast.com/xCQr3ykc) | thebitcoinpodcast.com | en | Cryptocurrency |
| [The Blog of Author Tim Ferriss](https://tim.blog/feed/) | tim.blog | en | Business & Economy |
| [The Clark Howard Podcast](https://feeds.megaphone.fm/clarkhoward) | clark.com | en | Personal finance |
| [The Cynical Developer](https://cynicaldeveloper.com/feed/podcast) | cynical.dev | en | Programming |
| [The Duct Tape Marketing Podcast](https://ducttape.libsyn.com/rss) | ducttapemarketing.com | en | Business & Economy |
| [the memory palace](http://feeds.thememorypalace.us/thememorypalace) | thememorypalace.us | en | History |
| [The Ramsey Show](https://daveramsey.libsyn.com/rss) | ramseysolutions.com | en | Personal finance |
| [The Stack Overflow Podcast](https://feeds.simplecast.com/XA_851k3) | art19.com | en | Programming |
| [The Stacking Benjamins Show](https://feeds.megaphone.fm/stacking-benjamins) | art19.com | en | Personal finance |
| [The Startup Junkies Podcast](https://startupjunkie.libsyn.com/rss) | startupjunkie.org | en | Startups |
| [The Tim Ferriss Show](https://rss.art19.com/tim-ferriss-show) | tim.blog | en | Startups |
| [The Vergecast](https://feeds.megaphone.fm/vergecast) | theverge.com | en | Tech |
| [This Week in Science – The Kickass Science Podcast](https://www.twis.org/feed/) | twis.org | en | Science |
| [This Week in Tech (Audio)](https://feeds.twit.tv/twit.xml) | twit.tv | en | Tech |
| [Throughline](https://feeds.npr.org/510333/podcast.xml) | npr.org | en | History |

### תרבות דיגיטלית ורשת (Digital Culture & Web)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [/r/Memes the original since 2008](https://www.reddit.com/r/memes/.rss) | reddit.com | en | Memes |
| [A sub for History Memes](https://www.reddit.com/r/historymemes/.rss) | reddit.com | en | Memes |
| [Advice Animals](https://www.reddit.com/r/AdviceAnimals/.rss) | reddit.com | en | Memes |
| [dankmemes](https://www.reddit.com/r/dankmemes/.rss) | reddit.com | en | Memes |
| [FAIL Blog](http://feeds.feedburner.com/failblog) | failblog.cheezburger.com | en | Funny |
| [I Can Has Cheezburger?](http://feeds.feedburner.com/icanhascheezburger) | icanhas.cheezburger.com | en | Funny |
| [Indian Memes](https://www.reddit.com/r/IndianMeyMeys/.rss) | reddit.com | en | Memes |
| [Internet for the Spirit](https://www.reddit.com/r/wholesomememes/.rss) | reddit.com | en | Memes |
| [Know Your Meme Newsfeed](https://knowyourmeme.com/newsfeed.rss) | knowyourmeme.com | en | Memes |
| [Memebase](https://memebase.cheezburger.com/rss) | memebase.cheezburger.com | en | Memes |
| [Penny Arcade](https://www.penny-arcade.com/feed) | penny-arcade.com | en | Funny |
| [PostSecret](https://postsecret.com/feed/?alt=rss) | postsecret.com | en | Funny |
| [PrequelMemes - Memes of the Star Wars Prequels](https://www.reddit.com/r/PrequelMemes/.rss) | reddit.com | en | Memes |
| [r/IndianDankMemes - India's Largest Meme Subreddit](https://www.reddit.com/r/IndianDankMemes/.rss) | reddit.com | en | Memes |
| [Saturday Morning Breakfast Cereal](https://www.smbc-comics.com/comic/rss) | smbc-comics.com | en | Funny |
| [selfies of the soul](https://www.reddit.com/r/me_irl/.rss) | reddit.com | en | Memes |
| [The Bloggess](https://thebloggess.com/feed/) | thebloggess.com | en | Funny |
| [The Daily WTF](http://syndication.thedailywtf.com/TheDailyWtf) | thedailywtf.com | en | Funny |
| [The Oatmeal - Comics by Matthew Inman](http://feeds.feedburner.com/oatmealfeed) | theoatmeal.com | en | Funny |
| [The Onion](https://www.theonion.com/rss) | theonion.com | en | Funny |
| [when things get too real for meirl](https://www.reddit.com/r/2meirl4meirl/.rss) | reddit.com | en | Memes |
| [xkcd.com](https://xkcd.com/rss.xml) | xkcd.com | en | Funny |
| [😎HAHA DAE MINIONS!!!😎](https://www.reddit.com/r/terriblefacebookmemes/.rss) | reddit.com | en | Memes |

### בינה מלאכותית (Artificial Intelligence)

| פיד | אתר | שפה | מקור |
|---|---|---|---|
| [Ahead of AI (Sebastian Raschka)](https://magazine.sebastianraschka.com/feed) | magazine.sebastianraschka.com | en | Curated |
| [AI at Meta Blog](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_meta_ai.xml) | ai.meta.com | en | Curated |
| [Anthropic News](https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml) | anthropic.com | en | Curated |
| [Apple Machine Learning Research](https://machinelearning.apple.com/rss.xml) | machinelearning.apple.com | en | Curated |
| [Berkeley AI Research (BAIR) Blog](https://bair.berkeley.edu/blog/feed.xml) | bair.berkeley.edu | en | Curated |
| [Google AI (The Keyword)](https://blog.google/innovation-and-ai/technology/ai/rss/) | blog.google | en | Curated |
| [Google DeepMind Blog](https://deepmind.google/blog/rss.xml) | deepmind.google | en | Curated |
| [Google Research Blog](https://research.google/blog/rss/) | research.google | en | Curated |
| [Hugging Face Blog](https://huggingface.co/blog/feed.xml) | huggingface.co | en | Curated |
| [Import AI (Jack Clark)](https://importai.substack.com/feed) | importai.substack.com | en | Curated |
| [Interconnects (Nathan Lambert)](https://www.interconnects.ai/feed) | interconnects.ai | en | Curated |
| [Last Week in AI](https://lastweekin.ai/feed) | lastweekin.ai | en | Curated |
| [Latent Space](https://www.latent.space/feed) | latent.space | en | Curated |
| [Microsoft Research Blog](https://www.microsoft.com/en-us/research/feed/) | microsoft.com | en | Curated |
| [MIT Technology Review AI](https://www.technologyreview.com/topic/artificial-intelligence/feed) | technologyreview.com | en | Curated |
| [One Useful Thing (Ethan Mollick)](https://www.oneusefulthing.org/feed) | oneusefulthing.org | en | Curated |
| [OpenAI News](https://openai.com/news/rss.xml) | openai.com | en | Curated |
| [Simon Willison's Weblog](https://simonwillison.net/atom/entries/) | simonwillison.net | en | Curated |
| [TechCrunch AI](https://techcrunch.com/category/artificial-intelligence/feed/) | techcrunch.com | en | Curated |
| [The Decoder](https://the-decoder.com/feed/) | the-decoder.com | en | Curated |
| [The Verge AI](https://www.theverge.com/rss/ai-artificial-intelligence/index.xml) | theverge.com | en | Curated |
| [VentureBeat AI](https://venturebeat.com/category/ai/feed) | venturebeat.com | en | Curated |
<!-- catalog:end -->
