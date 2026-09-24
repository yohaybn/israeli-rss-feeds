# israeli-rss-feeds

קטלוג פידי RSS ישראלי מתוחזק, מסודר ב-20 קטגוריות: חדשות, טכנולוגיה, כלכלה, ספורט, תרבות, בריאות, מדע, מוזיקה, גיימינג, אוכל, תיירות, רכב, אופנה, נדל"ן, הורות, דעה, פודקאסטים, קריירה, צרכנות ותרבות דיגיטלית.

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

<!-- catalog:start -->
**53 פידים ב-20 קטגוריות** (11 מהן עם פידים כרגע; השאר ריקות עד שהגילוי השבועי ימצא מקורות מתאימים).

| קטגוריה | תחום | פידים |
|---|---|---|
| חדשות ואקטואליה | חדשות בארץ ובעולם, מבזקים | 25 |
| טכנולוגיה וגאדג'טים | חדשות הייטק, מוצרי צריכה | 10 |
| כלכלה ועסקים | שוק ההון, פיננסים, יזמות | 5 |
| ספורט | חדשות ספורט, תוצאות, פרשנויות | 2 |
| תרבות ופנאי | קולנוע, טלוויזיה, ספרות | 0 |
| בריאות ורפואה | חדשות רפואיות, בריאות הציבור | 1 |
| מדע וסביבה | תגליות, אקולוגיה, חלל | 0 |
| מוזיקה | עדכוני אמנים, ביקורות אלבומים | 0 |
| גיימינג | חדשות משחקי וידאו, קונסולות | 0 |
| אוכל וקולינריה | מתכונים, מסעדות | 1 |
| תיירות ופנאי | טיולים, חופשות, תעופה | 0 |
| רכב ותחבורה | חדשות רכב, תחבורה ציבורית | 0 |
| אופנה ולייף סטייל | טרנדים, טיפוח | 1 |
| נדל"ן ועיצוב הבית | שוק הדיור, עיצוב פנים | 1 |
| הורות ומשפחה | גידול ילדים, חינוך | 0 |
| דעה וטורים אישיים | מאמרי דעה, בלוגים כלליים | 4 |
| פודקאסטים | עדכונים על פרקים חדשים | 0 |
| קריירה ועבודה | חיפוש עבודה, ניהול, התפתחות מקצועית | 1 |
| צרכנות ומבצעים | חדשות צרכנות, דילים | 2 |
| תרבות דיגיטלית ורשת | ממים, טרנדים ברשתות חברתיות | 0 |

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

### כלכלה ועסקים (Economy & Business)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - בארץ](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=9917) | Globes | he | 125 | 12,406 |
| [גלובס - שוק ההון והשקעות](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=585) | Globes | he | 41 | 12,406 |
| [גלובס - גלובלי ושוקי עולם](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=1225) | Globes | he | 28 | 12,406 |
| [גלובס - ראשי](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=1725) | Globes | he | 4 | 12,406 |
| [TheMarker - כל הכתבות](https://www.themarker.com/srv/tm-all-articles) | TheMarker | he | 18 | 36,286 |

### ספורט (Sports)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [וואלה - ספורט](https://rss.walla.co.il/feed/7) | Walla | he | - | 13,743 |
| [ONE](https://www.one.co.il/rss) | ONE | he | 2 | 46,456 |

### תרבות ופנאי (Culture & Entertainment)

_אין עדיין פידים בקטגוריה הזו._

### בריאות ורפואה (Health & Medicine)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [וואלה - בריאות](https://rss.walla.co.il/feed/18) | Walla | he | - | 13,743 |

### מדע וסביבה (Science & Environment)

_אין עדיין פידים בקטגוריה הזו._

### מוזיקה (Music)

_אין עדיין פידים בקטגוריה הזו._

### גיימינג (Gaming)

_אין עדיין פידים בקטגוריה הזו._

### אוכל וקולינריה (Food & Cooking)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [פודי](https://foody.co.il/feed/) | Foody | he | 0 | 682,324 |

### תיירות ופנאי (Travel & Leisure)

_אין עדיין פידים בקטגוריה הזו._

### רכב ותחבורה (Cars & Transportation)

_אין עדיין פידים בקטגוריה הזו._

### אופנה ולייף סטייל (Fashion & Lifestyle)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [את - מגזין את](https://www.atmag.co.il/feed/) | At Magazine | he | 8 | 429,306 |

### נדל"ן ועיצוב הבית (Real Estate & Home Design)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - נדל"ן ותשתיות](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=607) | Globes | he | 14 | 12,406 |

### הורות ומשפחה (Parenting & Family)

_אין עדיין פידים בקטגוריה הזו._

### דעה וטורים אישיים (Opinion & Personal Columns)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [Israellycool](https://www.israellycool.com/feed/) | Israellycool | en | 8 | 500,196 |
| [מידה](https://mida.org.il/feed/) | Mida | he | 12 | 623,959 |
| [Elder of Ziyon](https://elderofziyon.blogspot.com/feeds/posts/default) | Elder of Ziyon | en | 1 | - |
| [Unpacked (ISRAEL21c)](https://unpacked.media/feed/) | Unpacked | en | 0 | 326,223 |

### פודקאסטים (Podcasts)

_אין עדיין פידים בקטגוריה הזו._

### קריירה ועבודה (Career & Work)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [גלובס - ניהול וקריירה](https://www.globes.co.il/webservice/rss/rssfeeder.asmx/FeederNode?iID=3266) | Globes | he | 8 | 12,406 |

### צרכנות ומבצעים (Consumer & Deals)

| פיד | אתר | שפה | עוקבים ב-Feedly | דירוג Tranco |
|---|---|---|---|---|
| [mako - צרכנות וכלכלה](https://rcs.mako.co.il/rss/news-money.xml) | Mako (N12) | he | 8 | 6,072 |
| [וואלה - כסף וצרכנות](https://rss.walla.co.il/feed/3) | Walla | he | 1 | 13,743 |

### תרבות דיגיטלית ורשת (Digital Culture & Web)

_אין עדיין פידים בקטגוריה הזו._
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

## קטלוג בינלאומי

בתיקייה [`world/`](world/) יש קטלוג פידים בינלאומי באותה סכמה ובאותן קטגוריות, שמומר מ-[plenaryapp/awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) וכל פיד בו אומת מול האתר החי. מסתנכרן ומאומת מחדש כל שבוע. כתובת גלם לאפליקציות:

`https://raw.githubusercontent.com/yohaybn/israeli-rss-feeds/main/world/feeds.json`
