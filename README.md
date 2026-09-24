# israeli-rss-feeds

קטלוג פידי RSS ישראלי מתוחזק, מסודר ב-21 קטגוריות: חדשות, טכנולוגיה, כלכלה, ספורט, תרבות, בריאות, מדע, מוזיקה, גיימינג, אוכל, תיירות, רכב, אופנה, נדל"ן, הורות, דעה, פודקאסטים, קריירה, צרכנות, תרבות דיגיטלית ובינה מלאכותית.

כל פיד בקטלוג אומת מול האתר החי (תשובת HTTP תקינה, XML שמתפעל, ופריטים עדכניים) לפני שהוא נכנס, ונבדק מחדש אוטומטית כל שבוע. חלק מהקטגוריות עדיין דלילות או ריקות - הגילוי השבועי מחפש להן מקורות.

## שימוש

- **קוראי RSS** (Feedly, Inoreader, NetNewsWire וכו׳): מייבאים את קובץ ה-OPML - [`opml/israeli-rss-feeds.opml`](opml/israeli-rss-feeds.opml), או קובץ OPML לקטגוריה בודדת מתוך [`opml/by-category/`](opml/by-category/).
- **אפליקציות**: מושכים את [`feeds.json`](feeds.json) (JSON מסודר לפי קטגוריה, כולל שדה פופולריות למיון). כתובת גלם:

  `https://raw.githubusercontent.com/yohay-ai/israeli-rss-feeds/main/feeds.json`

## הקטגוריות

לכל קטגוריה יש `id` קבוע ב-`feeds.json` וקובץ `opml/by-category/<id>.opml`. פידים באנגלית מסווגים לפי נושא (שדה `language: en`), וכולם מרוכזים גם ב-[`opml/by-language/en.opml`](opml/by-language/en.opml).

| id | קטגוריה |
|---|---|
| `news` | חדשות ואקטואליה |
| `tech` | טכנולוגיה וגאדג'טים |
| `business` | כלכלה ועסקים |
| `sports` | ספורט |
| `culture` | תרבות ופנאי |
| `health` | בריאות ורפואה |
| `science` | מדע וסביבה |
| `music` | מוזיקה |
| `gaming` | גיימינג |
| `food` | אוכל וקולינריה |
| `travel` | תיירות ופנאי |
| `auto` | רכב ותחבורה |
| `fashion` | אופנה ולייף סטייל |
| `real-estate` | נדל"ן ועיצוב הבית |
| `parenting` | הורות ומשפחה |
| `opinion` | דעה וטורים אישיים |
| `podcasts` | פודקאסטים |
| `career` | קריירה ועבודה |
| `consumer` | צרכנות ומבצעים |
| `digital-culture` | תרבות דיגיטלית ורשת |
| `ai` | בינה מלאכותית |

<!-- catalog:start -->
**248 פידים ב-21 קטגוריות** (21 מהן עם פידים כרגע; השאר ריקות עד שהגילוי השבועי ימצא מקורות מתאימים).

| קטגוריה | תחום | פידים |
|---|---|---|
| חדשות ואקטואליה | חדשות בארץ ובעולם, מבזקים | 25 |
| טכנולוגיה וגאדג'טים | חדשות הייטק, מוצרי צריכה | 20 |
| כלכלה ועסקים | שוק ההון, פיננסים, יזמות | 15 |
| ספורט | חדשות ספורט, תוצאות, פרשנויות | 8 |
| תרבות ופנאי | קולנוע, טלוויזיה, ספרות | 18 |
| בריאות ורפואה | חדשות רפואיות, בריאות הציבור | 9 |
| מדע וסביבה | תגליות, אקולוגיה, חלל | 20 |
| מוזיקה | עדכוני אמנים, ביקורות אלבומים | 8 |
| גיימינג | חדשות משחקי וידאו, קונסולות | 5 |
| אוכל וקולינריה | מתכונים, מסעדות | 19 |
| תיירות ופנאי | טיולים, חופשות, תעופה | 13 |
| רכב ותחבורה | חדשות רכב, תחבורה ציבורית | 10 |
| אופנה ולייף סטייל | טרנדים, טיפוח | 7 |
| נדל"ן ועיצוב הבית | שוק הדיור, עיצוב פנים | 9 |
| הורות ומשפחה | גידול ילדים, חינוך | 5 |
| דעה וטורים אישיים | מאמרי דעה, בלוגים כלליים | 10 |
| פודקאסטים | עדכונים על פרקים חדשים | 22 |
| קריירה ועבודה | חיפוש עבודה, ניהול, התפתחות מקצועית | 4 |
| צרכנות ומבצעים | חדשות צרכנות, דילים | 12 |
| תרבות דיגיטלית ורשת | ממים, טרנדים ברשתות חברתיות | 2 |
| בינה מלאכותית | חדשות, בלוגים ומדריכים על בינה מלאכותית | 7 |

### חדשות ואקטואליה (News & Current Affairs)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [ynet - חדשות](https://www.ynet.co.il/Integration/StoryRss2.xml) | Ynet | he | 15 | 2,351 |
| [mako - חדשות בארץ](https://rcs.mako.co.il/rss/news-israel.xml) | Mako (N12) | he | 10 | 6,072 |
| [mako - חדשות בעולם](https://rcs.mako.co.il/rss/news-world.xml) | Mako (N12) | he | 7 | 6,072 |
| [mako - פוליטי וצבאי](https://rcs.mako.co.il/rss/news-military.xml) | Mako (N12) | he | 6 | 6,072 |
| [מעריב - חדשות](https://www.maariv.co.il/rss/rsschadashot) | Maariv | he | 1 | 11,332 |
| [וואלה - חדשות בעולם](https://rss.walla.co.il/feed/2) | Walla | he | 11 | 13,743 |
| [וואלה - חדשות בארץ](https://rss.walla.co.il/feed/1) | Walla | he | 8 | 13,743 |
| [וואלה - פלילים ומשפט](https://rss.walla.co.il/feed/10) | Walla | he | 1 | 13,743 |
| [וואלה - פוליטיקה וממשל](https://rss.walla.co.il/feed/9) | Walla | he | - | 13,743 |
| [וואלה - מזרח תיכון](https://rss.walla.co.il/feed/13) | Walla | he | - | 13,743 |
| [הארץ - כל הכתבות](https://www.haaretz.co.il/srv/htz-all-articles) | Haaretz | he | - | 15,069 |
| [ערוץ 7](https://www.inn.co.il/Rss.aspx?act=.1) | INN | he | 2 | 49,922 |
| [Now 14](https://www.now14.co.il/feed/) | Now 14 | he | 5 | 681,642 |
| [כיכר השבת](https://www.kikar.co.il/feed) | Kikar Hashabbat | he | 0 | 53,481 |
| [בחדרי חרדים](https://www.bhol.co.il/feed/) | Bhol | he | - | 55,370 |
| [סרוגים](https://www.srugim.co.il/feed) | Srugim | he | 2 | 58,451 |
| [כיפה](https://www.kipa.co.il/rss.xml) | Kipa | he | 1 | 65,752 |
| [Times of Israel](https://www.timesofisrael.com/feed/) | Times of Israel | en | 116 | 3,977 |
| [Jerusalem Post](https://rss.jpost.com/rss/rssfeedsfrontpage.aspx) | JPost | en | 34 | 4,085 |
| [Haaretz - Latest Headlines](https://www.haaretz.com/srv/haaretz-latest-headlines) | Haaretz English | en | 264 | 5,979 |
| [Haaretz - Israel News](https://www.haaretz.com/srv/israel-news-rss) | Haaretz English | en | 163 | 5,979 |
| [Ynetnews](https://www.ynetnews.com/Integration/StoryRss2.xml) | Ynetnews | en | 2 | 12,828 |
| [Israel National News](https://www.israelnationalnews.com/Rss.aspx?act=.1) | INN English | en | 3 | 21,149 |
| [JNS](https://www.jns.org/feed/) | JNS | en | 522 | 36,674 |
| [Algemeiner](https://www.algemeiner.com/feed/) | Algemeiner | en | 7 | 59,625 |

### טכנולוגיה וגאדג'טים (Technology & Gadgets)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - טכנולוגיה](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=594) | Globes | he | 38 | 12,406 |
| [וואלה - טכנולוגיה](https://rss.walla.co.il/feed/4) | Walla | he | - | 13,743 |
| [גיקטיים](https://www.geektime.co.il/feed/) | Geektime | he | 30 | 142,301 |
| [אנשים ומחשבים](https://www.pc.co.il/feed/) | PC | he | 10 | 428,615 |
| [Gadgety](https://www.gadgety.co.il/feed/) | Gadgety | he | 14 | 445,237 |
| [CTech](https://feeds.feedburner.com/ctech) | CTech (Calcalist) | en | 0 | - |
| [פלאנט תוכנה חופשית בישראל](http://planet.linux.org.il/rss20.xml) | Planet FOSS-IL | he | 126 | - |
| [אינטרנט ישראל (רן בר-זיק)](https://internet-israel.com/feed/) | Internet Israel | he | 42 | - |
| [מגזין HT (הום ת'יאטר)](https://www.hometheater.co.il/feed/) | HomeTheater | he | - | - |
| [Haaretz - Tech](https://www.haaretz.com/srv/technology-news-rss) | Haaretz English | en | 14 | 5,979 |
| [ynet - דיגיטל](https://www.ynet.co.il/Integration/StoryRss544.xml) | Ynet | he | - | - |
| [מעריב - טכנולוגיה](https://www.maariv.co.il/rss/rssfeedstechnologeya) | Maariv | he | - | - |
| [וואלה - חדשות טכנולוגיה](https://rss.walla.co.il/feed/4000) | Walla | he | - | - |
| [TheMarker - TechNation](https://www.themarker.com/srv/tm-technation) | TheMarker | he | - | - |
| [Jerusalem Post - Tech](https://www.jpost.com/rss/rsstechandstartups) | JPost | en | - | - |
| [IT News](https://www.itnews.co.il/feed/) | IT News | he | - | - |
| [Techtime - אלקטרוניקה והייטק](https://www.techtime.co.il/feed/) | Techtime | he | - | - |
| [HWzone](https://www.hwzone.co.il/feed/) | HWzone | he | - | - |
| [Digital Whisper - גיליונות אבטחת מידע](https://www.digitalwhisper.co.il/rss) | Digital Whisper | he | - | - |
| [וואלה - סייבר](https://rss.walla.co.il/feed/12765) | Walla | he | - | - |

### כלכלה ועסקים (Economy & Business)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - בארץ](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=9917) | Globes | he | 125 | 12,406 |
| [גלובס - שוק ההון והשקעות](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=585) | Globes | he | 41 | 12,406 |
| [גלובס - גלובלי ושוקי עולם](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=1225) | Globes | he | 28 | 12,406 |
| [גלובס - ראשי](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=1725) | Globes | he | 4 | 12,406 |
| [TheMarker - כל הכתבות](https://www.themarker.com/srv/tm-all-articles) | TheMarker | he | 18 | 36,286 |
| [ynet - כלכלה](https://www.ynet.co.il/Integration/StoryRss6.xml) | Ynet | he | - | - |
| [מעריב - כלכלה](https://www.maariv.co.il/rss/rssfeedsasakim) | Maariv | he | - | - |
| [מעריב - כלכלה בארץ](https://www.maariv.co.il/rss/rssfeedskalkalabaarez) | Maariv | he | - | - |
| [TheMarker - שוק ההון](https://www.themarker.com/srv/tm-markets) | TheMarker | he | - | - |
| [TheMarker - גלובל](https://www.themarker.com/srv/tm-global) | TheMarker | he | - | - |
| [Jerusalem Post - Business & Innovation](https://www.jpost.com/rss/rssbusinessandinnovation) | JPost | en | - | - |
| [Jerusalem Post - Banking & Finance](https://www.jpost.com/rss/rssbankingandfinance) | JPost | en | - | - |
| [וואלה כסף - חדשות](https://rss.walla.co.il/feed/557) | Walla | he | - | - |
| [וואלה כסף - מגזין](https://rss.walla.co.il/feed/12964) | Walla | he | - | - |
| [Globes English](https://en.globes.co.il/WebService/Rss/RssFeeder.asmx/FeederNode?iID=942) | Globes English | en | - | - |

### ספורט (Sports)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [וואלה - ספורט](https://rss.walla.co.il/feed/7) | Walla | he | - | 13,743 |
| [ONE](https://www.one.co.il/rss) | ONE | he | 2 | 46,456 |
| [ynet - ספורט](https://www.ynet.co.il/Integration/StoryRss3.xml) | Ynet | he | - | - |
| [ynet - כדורגל ישראלי](https://www.ynet.co.il/Integration/StoryRss57.xml) | Ynet | he | - | - |
| [ynet - כדורגל עולמי](https://www.ynet.co.il/Integration/StoryRss56.xml) | Ynet | he | - | - |
| [וואלה - כדורגל ישראלי](https://rss.walla.co.il/feed/156) | Walla | he | - | - |
| [וואלה - כדורסל](https://rss.walla.co.il/feed/151) | Walla | he | - | - |
| [הארץ - ספורט](https://www.haaretz.co.il/srv/%D7%A1%D7%A4%D7%95%D7%A8%D7%98--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |

### תרבות ופנאי (Culture & Entertainment)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [ynet - תרבות ובידור](https://www.ynet.co.il/Integration/StoryRss538.xml) | Ynet | he | - | - |
| [ynet - קולנוע](https://www.ynet.co.il/Integration/StoryRss540.xml) | Ynet | he | - | - |
| [מעריב - תרבות](https://www.maariv.co.il/rss/rssfeedstarbot) | Maariv | he | - | - |
| [מעריב - קולנוע](https://www.maariv.co.il/rss/rssfeedskolnoa) | Maariv | he | - | - |
| [מעריב - אמנות ובמה](https://www.maariv.co.il/rss/rssfeedsomanotvebama) | Maariv | he | - | - |
| [וואלה - תרבות](https://rss.walla.co.il/feed/249) | Walla | he | - | - |
| [וואלה - קולנוע](https://rss.walla.co.il/feed/270) | Walla | he | - | - |
| [וואלה - במה](https://rss.walla.co.il/feed/5545) | Walla | he | - | - |
| [הארץ - תרבות](https://www.haaretz.co.il/srv/htz---culture---rss) | Haaretz | he | - | - |
| [הארץ - ספרים](https://www.haaretz.co.il/srv/%D7%A1%D7%A4%D7%A8%D7%99%D7%9D--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [Jerusalem Post - Culture](https://www.jpost.com/rss/rssfeedsculture.aspx) | JPost | en | - | - |
| [אלכסון](http://feeds.feedburner.com/AlaxonAll) | Alaxon | he | - | - |
| [ערב רב](https://www.erev-rav.com/feed/) | Erev Rav | he | - | - |
| [המקום הכי חם בגיהנום](https://www.ha-makom.co.il/feed/) | Ha-Makom | he | - | - |
| [יקום תרבות](https://www.yekum.org/feed/) | Yekum | he | - | - |
| [Secret Tel Aviv](https://www.secrettelaviv.com/feed) | Secret Tel Aviv | en | - | - |
| [מגזין פורטפוליו](https://www.prtfl.co.il/feed/) | Portfolio | he | - | - |
| [ספר הקולנוע הישראלי](https://cinemaofisrael.co.il/feed/) | Cinema of Israel | he | - | - |

### בריאות ורפואה (Health & Medicine)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [וואלה - בריאות](https://rss.walla.co.il/feed/18) | Walla | he | - | 13,743 |
| [מעריב - בריאות](https://www.maariv.co.il/rss/rssfeedsbriotveyeoz) | Maariv | he | - | - |
| [וואלה - פסיכולוגיה](https://rss.walla.co.il/feed/1870) | Walla | he | - | - |
| [וואלה - תזונה ודיאטה](https://rss.walla.co.il/feed/585) | Walla | he | - | - |
| [הארץ - בריאות](https://www.haaretz.co.il/srv/%D7%91%D7%A8%D7%99%D7%90%D7%95%D7%AA--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [Jerusalem Post - Health & Wellness](https://www.jpost.com/rss/rsshealth-and-wellness) | JPost | en | - | - |
| [Jerusalem Post - Nutrition](https://www.jpost.com/rss/rssnutrition) | JPost | en | - | - |
| [MedNews](https://www.mednews.co.il/feed/) | MedNews | he | - | - |
| [שוונג - ריצה, אופניים, טריאתלון](https://www.shvoong.co.il/feed/) | Shvoong | he | - | - |

### מדע וסביבה (Science & Environment)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [הארץ - מדע](https://www.haaretz.co.il/srv/%D7%9E%D7%93%D7%A2--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [הארץ - סביבה ואקלים](https://www.haaretz.co.il/srv/%D7%A1%D7%91%D7%99%D7%91%D7%94-%D7%95%D7%90%D7%A7%D7%9C%D7%99%D7%9D--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [מעריב - איכות הסביבה](https://www.maariv.co.il/rss/rssfeedsenvironment) | Maariv | he | - | - |
| [וואלה - מדע](https://rss.walla.co.il/feed/13308) | Walla | he | - | - |
| [Jerusalem Post - Science](https://www.jpost.com/rss/rssscience) | JPost | en | - | - |
| [Jerusalem Post - Archaeology](https://www.jpost.com/rss/rssarchaeology) | JPost | en | - | - |
| [Jerusalem Post - Environment](https://www.jpost.com/rss/rssenvironment) | JPost | en | - | - |
| [הידען](https://www.hayadan.org.il/feed) | Hayadan | he | - | - |
| [זווית - סוכנות ידיעות למדע ולסביבה](https://www.zavit.org.il/feed/) | Zavit | he | - | - |
| [בשער - מדע וחברה](https://www.bashaar.org.il/feed/) | Bashaar | he | - | - |
| [החברה להגנת הטבע](https://www.teva.org.il/feed/) | SPNI | he | - | - |
| [Nature Israel](https://natureisrael.org/feed/) | Nature Israel | he | - | - |
| [אוניברסיטת תל אביב - חדשות](https://www.tau.ac.il/rss.xml) | Tel Aviv University | he | - | - |
| [אוניברסיטת בר-אילן - חדשות](https://www.biu.ac.il/rss.xml) | Bar-Ilan University | he | - | - |
| [אוניברסיטת חיפה - חדשות](https://www.haifa.ac.il/feed/) | University of Haifa | he | - | - |
| [סוכנות החלל הישראלית](https://www.space.gov.il/rss.xml) | Israel Space Agency | he | - | - |
| [סיור מוחות](https://brains-tour.com/feed/) | Brains Tour | he | - | - |
| [Q-Israel - קוונטים](https://www.q-israel.com/blog-feed.xml) | Q-Israel | he | - | - |
| [פיזיקטבע](https://physicateva.com/feed/) | Physicateva | he | - | - |
| [חיידקים, נגיפים ושאר ירקות (ד"ר דרור בר-ניר)](https://drorbn.blogspot.com/feeds/posts/default) | Dror Bar-Nir | he | - | - |

### מוזיקה (Music)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [ynet - מוזיקה](https://www.ynet.co.il/Integration/StoryRss542.xml) | Ynet | he | - | - |
| [מעריב - מוזיקה](https://www.maariv.co.il/rss/rssfeedsmozika) | Maariv | he | - | - |
| [וואלה - מוזיקה](https://rss.walla.co.il/feed/272) | Walla | he | - | - |
| [יוסמיוסיק](https://yosmusic.com/feed/) | YosMusic | he | - | - |
| [בעיקר מוזיקה (עומר שומרוני)](https://omershomrony.com/feed/) | Omer Shomrony | he | - | - |
| [עונג שבת - להתרגש ביחד ממוזיקה](https://haoneg.substack.com/feed) | Haoneg | he | - | - |
| [מוזיקאסט עם גיא ממן (פודקאסט)](https://www.spreaker.com/show/7249143/episodes/feed) | Osim Historia | he | - | - |
| [כאן - שיר אחד (פודקאסט)](https://www.omnycontent.com/d/playlist/23f697a0-7e6a-4e96-a223-a82c00962b12/acf55018-3331-41be-9c34-a919008d593c/bd9198c9-39cc-41f7-8612-a919008d593c/podcast.rss) | Kan | he | - | - |

### גיימינג (Gaming)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [ynet - משחקים](https://www.ynet.co.il/Integration/StoryRss571.xml) | Ynet | he | - | - |
| [Vgames](https://www.vgames.co.il/rss) | Vgames | he | - | - |
| [GamePro](https://gamepro.co.il/feed/) | GamePro | he | - | - |
| [IGN Israel](https://il.ign.com/feed.xml) | IGN Israel | he | - | - |
| [הפונדק - משחקי תפקידים ומשחקי קופסה](https://pundak.games/feed/) | Pundak | he | - | - |

### אוכל וקולינריה (Food & Cooking)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [פודי](https://foody.co.il/feed/) | Foody | he | 0 | 682,324 |
| [מעריב - אוכל](https://www.maariv.co.il/rss/rssfeedsochel) | Maariv | he | - | - |
| [מעריב - חדשות אוכל](https://www.maariv.co.il/rss/rssfoodnews) | Maariv | he | - | - |
| [וואלה - אוכל](https://rss.walla.co.il/feed/1132) | Walla | he | - | - |
| [וואלה - חדשות האוכל](https://rss.walla.co.il/feed/905) | Walla | he | - | - |
| [וואלה - יין ואלכוהול](https://rss.walla.co.il/feed/902) | Walla | he | - | - |
| [הארץ - אוכל](https://www.haaretz.co.il/srv/%D7%90%D7%95%D7%9B%D7%9C--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [Jerusalem Post - Food and Recipes](https://www.jpost.com/rss/rssfoodandrecipes) | JPost | en | - | - |
| [בישולים מבית אסם](https://www.bishulim.co.il/rss.xml) | Bishulim | he | - | - |
| [עוגיו.נט](https://www.oogio.net/feed/) | Oogio | he | - | - |
| [קרוטית](https://www.krutit.co.il/feed/) | Krutit | he | - | - |
| [המטבח של נטע](https://netacooks.co.il/feed/) | Neta Cooks | he | - | - |
| [רותם ליברזון - בלוג אוכל](https://rotteml.com/feed/) | Rotem Liberzon | he | - | - |
| [מדע בצלחת](https://scienceinmyplate.com/feed/) | Science in My Plate | he | - | - |
| [The Kitchen Coach](https://www.thekitchencoach.co.il/feed/) | The Kitchen Coach | he | - | - |
| [טבעוניות נהנות יותר](https://vegansontop.co.il/feed/) | Vegans on Top | he | - | - |
| [ניקי ב - אוכל עושים באהבה](https://www.nikib.co.il/feed/) | Niki B | he | - | - |
| [קולינרטיקה](https://culinartica.co.il/feed/) | Culinartica | he | - | - |
| [יופי במטבח](https://fromhayawithlove.com/feed/) | From Haya with Love | he | - | - |

### תיירות ופנאי (Travel & Leisure)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [מעריב - תיירות](https://www.maariv.co.il/rss/rssfeedstayarot) | Maariv | he | - | - |
| [וואלה - תיירות](https://rss.walla.co.il/feed/2501) | Walla | he | - | - |
| [וואלה - טיולים בארץ](https://rss.walla.co.il/feed/5735) | Walla | he | - | - |
| [וואלה - טיולים בעולם](https://rss.walla.co.il/feed/779) | Walla | he | - | - |
| [הארץ - טיולים](https://www.haaretz.co.il/srv/%D7%98%D7%99%D7%95%D7%9C%D7%99%D7%9D---%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [גלובס - תיירות](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=9010) | Globes | he | - | - |
| [Jerusalem Post - Travel](https://www.jpost.com/rss/rsstravel) | JPost | en | - | - |
| [ynet - חופש](https://www.ynet.co.il/Integration/StoryRss598.xml) | Ynet | he | - | - |
| [תיירות קום](https://www.tayarut.com/feed/) | Tayarut | he | - | - |
| [מטיילת מחוץ לקופסא](https://www.trvbox.co.il/feed/) | Trvbox | he | - | - |
| [בא לי לטייל](https://baliletayel.co.il/feed/) | Ba Li Letayel | he | - | - |
| [מטיילים בכיפה](https://metaylimbkipa.com/feed/) | Metaylim Bkipa | he | - | - |
| [מטיילת](https://metayelet.co.il/feed/) | Metayelet | he | - | - |

### רכב ותחבורה (Cars & Transportation)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [ynet - רכב](https://www.ynet.co.il/Integration/StoryRss550.xml) | Ynet | he | - | - |
| [מעריב - רכב](https://www.maariv.co.il/rss/rssfeedsrechev) | Maariv | he | - | - |
| [וואלה - רכב](https://rss.walla.co.il/feed/4700) | Walla | he | - | - |
| [וואלה - מבחני רכב](https://rss.walla.co.il/feed/4701) | Walla | he | - | - |
| [וואלה - דו-גלגלי](https://rss.walla.co.il/feed/4739) | Walla | he | - | - |
| [גלובס - רכב ותחבורה](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=3220) | Globes | he | - | - |
| [אוברדרייב - רכב ואופנועים](https://over-drive.co.il/feed/) | Over-Drive | he | - | - |
| [Wheel - חדשות רכב](https://wheel.co.il/feed/) | Wheel | he | - | - |
| [autocom](https://www.autocom.co.il/feed/) | Autocom | he | - | - |
| [קארטיוב](https://www.cartube.co.il/?format=feed&type=rss) | Cartube | he | - | - |

### אופנה ולייף סטייל (Fashion & Lifestyle)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [את - מגזין את](https://www.atmag.co.il/feed/) | At Magazine | he | 8 | 429,306 |
| [מעריב - אופנה](https://www.maariv.co.il/rss/rssfeedsofna) | Maariv | he | - | - |
| [מעריב - לייף סטייל](https://www.maariv.co.il/rss/rssfeedslayfstyle) | Maariv | he | - | - |
| [מעריב TMI - אופנה](https://www.maariv.co.il/rss/rssfeedstmifashion) | Maariv | he | - | - |
| [וואלה - אופנה](https://rss.walla.co.il/feed/2120) | Walla | he | - | - |
| [וואלה - טרנדים](https://rss.walla.co.il/feed/2101) | Walla | he | - | - |
| [וואלה - טיפוח ויופי](https://rss.walla.co.il/feed/1860) | Walla | he | - | - |

### נדל"ן ועיצוב הבית (Real Estate & Home Design)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - נדל"ן ותשתיות](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=607) | Globes | he | 14 | 12,406 |
| [מעריב - נדל"ן](https://www.maariv.co.il/rss/rssfeedsnadlan) | Maariv | he | - | - |
| [TheMarker - נדל"ן](https://www.themarker.com/srv/tm-real-estate) | TheMarker | he | - | - |
| [Jerusalem Post - Real Estate](https://www.jpost.com/rss/rssrealestate) | JPost | en | - | - |
| [וואלה - בית ועיצוב](https://rss.walla.co.il/feed/4418) | Walla | he | - | - |
| [וואלה - עיצוב פנים](https://rss.walla.co.il/feed/3237) | Walla | he | - | - |
| [וואלה - אדריכלות](https://rss.walla.co.il/feed/4410) | Walla | he | - | - |
| [בניין ודיור](https://www.bvd.co.il/feed/) | BVD | he | - | - |
| [WALLS - מגזין עיצוב](https://wallsmag.co.il/feed/) | Walls | he | - | - |

### הורות ומשפחה (Parenting & Family)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [וואלה - הורות וילדים](https://rss.walla.co.il/feed/594) | Walla | he | - | - |
| [וואלה - הריון ולידה](https://rss.walla.co.il/feed/590) | Walla | he | - | - |
| [מעריב - חינוך](https://www.maariv.co.il/rss/rsseducation) | Maariv | he | - | - |
| [הארץ - משפחה](https://www.haaretz.co.il/srv/rss---%D7%9E%D7%A9%D7%A4%D7%97%D7%94) | Haaretz | he | - | - |
| [רון שמעוני - הורות](https://www.ronshimoni.co.il/feed/) | Ron Shimoni | he | - | - |

### דעה וטורים אישיים (Opinion & Personal Columns)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [Israellycool](https://www.israellycool.com/feed/) | Israellycool | en | 8 | 500,196 |
| [מידה](https://mida.org.il/feed/) | Mida | he | 12 | 623,959 |
| [Elder of Ziyon](https://elderofziyon.blogspot.com/feeds/posts/default) | Elder of Ziyon | en | 1 | - |
| [Unpacked (ISRAEL21c)](https://unpacked.media/feed/) | Unpacked | en | 0 | 326,223 |
| [ynet - דעות](https://www.ynet.co.il/Integration/StoryRss194.xml) | Ynet | he | - | - |
| [מעריב - דעות](https://www.maariv.co.il/rss/rssfeedsopinions) | Maariv | he | - | - |
| [הארץ - דעות](https://www.haaretz.co.il/srv/rss-opinion) | Haaretz | he | - | - |
| [TheMarker - פרשנויות](https://www.themarker.com/srv/tm-opinions) | TheMarker | he | - | - |
| [Jerusalem Post - Opinion](https://www.jpost.com/rss/rssopinion) | JPost | en | - | - |
| [וואלה כסף - דעות](https://rss.walla.co.il/feed/4997) | Walla | he | - | - |

### פודקאסטים (Podcasts)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [הארץ - פודקאסטים](https://www.haaretz.co.il/srv/%D7%A4%D7%95%D7%93%D7%A7%D7%90%D7%A1%D7%98%D7%99%D7%9D--%D7%94%D7%90%D7%A8%D7%A5-rss) | Haaretz | he | - | - |
| [השבוע - פודקאסט הארץ](https://www.omnycontent.com/d/playlist/397b9456-4f75-4509-acff-ac0600b4a6a4/fdef9415-eb17-45d7-85fd-ac08009235b2/4c9f1a8f-8a0e-4f10-b01f-ac08009235b7/podcast.rss) | Haaretz | he | - | - |
| [Jerusalem Post - Podcasts](https://www.jpost.com/rss/rssfeedpodcast) | JPost | en | - | - |
| [פודקאסט·ישראל - פרקים חדשים](https://pod-il.co.il/feed.xml) | Pod-IL | he | - | - |
| [עושים היסטוריה עם רן לוי](https://www.spreaker.com/show/4227531/episodes/feed) | Osim Historia | he | - | - |
| [עושים טכנולוגיה עם ד"ר יובל דרור](https://www.spreaker.com/show/4231127/episodes/feed) | Osim Historia | he | - | - |
| [עושים חשבון](https://www.spreaker.com/show/4221239/episodes/feed) | Osim Historia | he | - | - |
| [עושים פסיכולוגיה](https://www.spreaker.com/show/5277195/episodes/feed) | Osim Historia | he | - | - |
| [כאן - חיות כיס](https://www.omnycontent.com/d/playlist/23f697a0-7e6a-4e96-a223-a82c00962b12/dbe32976-5401-4c93-87ed-a919008d58ae/1ea69f94-8d46-4ff2-aaca-a919008d58b8/podcast.rss) | Kan | he | - | - |
| [כאן דוקו - ההסכת](https://www.omnycontent.com/d/playlist/23f697a0-7e6a-4e96-a223-a82c00962b12/c40b8ac9-3853-41fc-a2bf-b02700be578d/d2f0ee29-6047-4c3b-bab9-b02700c0b25e/podcast.rss) | Kan | he | - | - |
| [כאן - ביג דיל](https://www.omnycontent.com/d/playlist/23f697a0-7e6a-4e96-a223-a82c00962b12/28750de1-4a5a-434d-8dd1-b358009ee1ee/fd0d099f-235e-4b91-b35a-b358009ee5e3/podcast.rss) | Kan | he | - | - |
| [כאן - גורי כיס](https://www.omnycontent.com/d/playlist/23f697a0-7e6a-4e96-a223-a82c00962b12/1a02e8c1-d119-40da-acf7-ae2f00c89258/e8990ce1-f3fa-44c6-8e39-ae2f00ca8b98/podcast.rss) | Kan | he | - | - |
| [עולים לרגל - פודקאסט כדורגל (ערוץ הספורט)](https://www.omnycontent.com/d/playlist/178d72a7-a889-4132-8008-a5cc014ed109/7050b47b-371e-469c-9d10-ae83012b5e4b/f6f3b580-aace-4226-9216-ae83012c09a2/podcast.rss) | Sport5 | he | - | - |
| [ספיק נ' רול - פודקאסט כדורסל (ערוץ הספורט)](https://www.omnycontent.com/d/playlist/178d72a7-a889-4132-8008-a5cc014ed109/76238410-3d22-4fe5-9071-ae83012ec9f3/a589b423-1724-4672-a3a4-ae83012f3b88/podcast.rss) | Sport5 | he | - | - |
| [השקעות לעצלנים](https://anchor.fm/s/ef1f5500/podcast/rss) | Tamir Mandovsky | he | - | - |
| [רגע לפני - פודקאסט פוליטי](https://anchor.fm/s/f80c84d0/podcast/rss) | Rega Lifney | he | - | - |
| [היסטוריה אדומה](https://feeds.redcircle.com/badd6290-0fec-4712-96c1-362df2ed4e3a) | Historia Aduma | he | - | - |
| [היסטוריה אינטלקטואלית גסה](https://anchor.fm/s/e3810720/podcast/rss) | HI Gasa | he | - | - |
| [תעלומות במדעטק](https://anchor.fm/s/f4db785c/podcast/rss) | Madatech | he | - | - |
| [קפה מדע (תל אביב 360)](https://anchor.fm/s/112721f4c/podcast/rss) | Tel Aviv 360 | he | - | - |
| [פרוטוקול פתוח - פודקאסט בריאות מבוסס מדע](https://rss.buzzsprout.com/2595895.rss) | Protocol Patuach | he | - | - |
| [כלכלה מבראשית (רדיו תל אביב)](https://rss.102fm.co.il/rss-feed/get-feed?category=BERESHIT) | 102FM | he | - | - |

### קריירה ועבודה (Career & Work)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - ניהול וקריירה](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=3266) | Globes | he | 8 | 12,406 |
| [וואלה - קריירה והשכלה](https://rss.walla.co.il/feed/12864) | Walla | he | - | - |
| [עידית כהנא - קריירה](https://www.iditcahana.co.il/feed/) | Idit Cahana | he | - | - |
| [קורות חיים - בלוג](https://korotchaim.com/feed.xml) | Korotchaim | he | - | - |

### צרכנות ומבצעים (Consumer & Deals)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [mako - צרכנות וכלכלה](https://rcs.mako.co.il/rss/news-money.xml) | Mako (N12) | he | 8 | 6,072 |
| [וואלה - כסף וצרכנות](https://rss.walla.co.il/feed/3) | Walla | he | 1 | 13,743 |
| [מעריב - צרכנות](https://www.maariv.co.il/rss/rssfeedszarchanot) | Maariv | he | - | - |
| [וואלה - צרכנות](https://rss.walla.co.il/feed/127) | Walla | he | - | - |
| [TheMarker - צרכנות](https://www.themarker.com/srv/tm-consumer) | TheMarker | he | - | - |
| [Jerusalem Post - Consumerism](https://www.jpost.com/rss/consumerism) | JPost | en | - | - |
| [קופונים](https://couponim.co.il/feed/) | Couponim | he | - | - |
| [דיל היום](https://dealhayom.co.il/feed/) | DealHayom | he | - | - |
| [דילים - סיילים ומבצעים](https://dilim.co.il/feed/) | Dilim | he | - | - |
| [יממה - מבצעים ודילים](https://yemama.co.il/feed/) | Yemama | he | - | - |
| [דילי](https://www.deali.co.il/feed.xml) | Deali | he | - | - |
| [דיל סקנר](https://deal-scanner.blogspot.com/feeds/posts/default) | Deal Scanner | he | - | - |

### תרבות דיגיטלית ורשת (Digital Culture & Web)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [וואלה - רשתות חברתיות](https://rss.walla.co.il/feed/13019) | Walla | he | - | - |
| [וואלה - ויראלי](https://rss.walla.co.il/feed/4027) | Walla | he | - | - |

### בינה מלאכותית (Artificial Intelligence)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [tzedek.me - חדשות ומדריכי AI](https://tzedek.me/rss.xml) | tzedek.me | he | - | - |
| [GoAI - בינה מלאכותית בעברית](https://www.goai.co.il/feed/) | GoAI | he | - | - |
| [VC Cafe](https://www.vccafe.com/feed/) | VC Cafe | en | - | - |
| [Machine Learning Israel](https://machinelearning.co.il/feed/) | Machine Learning Israel | he | - | - |
| [YUV.AI (יובל אבידני)](https://yuv.ai/rss.xml) | YUV.AI | he | - | - |
| [Israel-AI - ארגון ה-AI הישראלי](https://israel-ai.org/rss.xml) | Israel-AI | he | - | - |
| [יפית בשבקין - AI](https://www.bashevkin.co.il/blog-feed.xml) | Yafit Bashevkin | he | - | - |
<!-- catalog:end -->

## פופולריות

לכל פיד יש שדה `popularity` עם שני אותות פומביים, למיון בתוך קטגוריה:

- `feedly_subscribers` - מספר העוקבים של אותו פיד ב-Feedly (API ציבורי). `null` כש-Feedly לא עוקב אחרי אותו URL.
- `tranco_rank` - דירוג הדומיין של האתר ב[רשימת Tranco](https://tranco-list.eu/) (מיליון הדומיינים הפופולריים; נמוך = פופולרי יותר). `null` כשהדומיין מחוץ לרשימה.
- `source` - אילו אותות זמינים לפיד הזה.

## תחזוקה אוטומטית

- **בדיקת פידים מתים** - כל יום ראשון, GitHub Action מריץ את `scripts/check_feeds.py`: מאמת כל פיד מול האתר החי, מעדכן את `FEEDS-STATUS.md`, ופותח issue אם נמצאו פידים מתים או קפואים (אין פריט חדש 90 יום). אתרים שחוסמים בוטים (403/429) מסומנים כ"חסום לבדיקה" ולא כ"מת", כי הם עובדים לקוראים אמיתיים.
- **גילוי פידים חדשים** - כל יום רביעי, Action שני מריץ את `scripts/discover_feeds.py`: סורק את האתרים ב-`scripts/discovery-sites.txt` (autodiscovery של תגיות link ונתיבים נפוצים), מאתר פידים חיים שעוד לא בקטלוג, ופותח issue עם המועמדים לאישור ידני - מקובצים לפי הקטגוריה המוצעת, כשהקטגוריות הריקות מופיעות ראשונות. אתרי הסריקה מחולקים בקובץ לפי קטגוריה (כותרת `[id]`). רוצים להוסיף אתר לסריקה? PR ל-`discovery-sites.txt` תחת הקטגוריה המתאימה.

## תרומה

1. מוסיפים או מעדכנים פיד ב-`feeds.json` (הקובץ הוא מקור האמת) תחת אחת מ-20 הקטגוריות.
2. מריצים `python scripts/build_opml.py` כדי לייצר מחדש את קבצי ה-OPML ואת טבלאות הקטלוג ב-README.
3. פותחים PR. כל פיד חדש צריך להיות חי ומעודכן - בדיקה מקומית: `python scripts/check_feeds.py`.

הקטלוג מנותק בכוונה מכל אפליקציה ספציפית - כל קורא RSS או אפליקציה יכולים להשתמש בו.
