# DECISIONS

החלטות מתמשכות בפרויקט, כדי שסוכנים ותורמים לא יעבדו כפול.
לכל החלטה: מה הוחלט, למה, ומה נפסל. חדשות בסוף.

## 1. הריפו הזה הוא הקטלוג היחיד של המלצות המקורות באפליקציה (2026-09-24)
האפליקציה (Pirate RSS, ריפו פרטי) טוענת את `feeds.json` מרחוק מהריפו הזה. פידים
נכנסים רק דרך PR כאן, לעולם לא בקוד האפליקציה. ריפו ציבורי גם כדי לעודד תרומות קהילה.
נדחה: קטלוג מוטמע ב-APK; ריפו נפרד למקורות עולמיים (ראו סעיף 4).

## 2. RSS מקורי מנצח (2026-09-30)
אתר עם פיד RSS/Atom מקורי שמיש משתמש בפיד המקורי. פידים מגונרטים מ-
`israeli-no-rss-feeds` נכנסים רק כשאין RSS מקורי שמיש. דוגמה: ל-The Verifier יש
RSS שבור כרגע; אם המפרסם יתקן אותו, חוזרים לפיד המקורי.

## 3. כלכליסט: בדיוק 13 הקטגוריות הראשיות (2026-09-30)
הקטלוג, הגנרטור והפרסום החי מכסים בדיוק את 13 הקטגוריות הראשיות של כלכליסט.
תתי-הקטגוריות הוסרו (תיקון להחלטה מוקדמת של 87 פידים). קטגוריה חדשה של המפרסם
דורשת עדכון מפורש בסקופ.

## 4. מקורות עולמיים חיים כאן, לא בריפו נפרד (2026-09-24)
מקורות בינלאומיים נמצאים ב-`world/feeds.json` באותו ריפו, ממופים לאותן 21 הקטגוריות.
נדחה: ריפו `world-rss-feeds` נפרד.

## 5. דיווח בריאות מתוארך, לא הבטחות (2026-09)
ה-README ו-FEEDS-STATUS.md מדווחים תמונת מצב מתוארכת (תקין / מיושן / חסום לבדיקה /
נכשל). לא להצהיר שכל הפידים עובדים; חסימה של בדיקה אוטומטית אינה הוכחה שהפיד
שבור בטלפון, ופיד בלי תאריכים אינו הוכחה שהוא מתעדכן.

## 6. `feeds.json` הוא הממשק היציב לאפליקציה
21 מזהי קטגוריות קבועים (id לכל קטגוריה), שדה שפה, ושדות פופולריות למיון
(עוקבים ב-Feedly, דירוג Tranco). שינוי סכמה דורש תאום מול האפליקציה.

---

# English

1. This repo is the app's single source-recommendation catalog; feeds enter only via PR here, never in app code. (2026-09-24)
2. Native RSS wins: generated feeds only when no usable native RSS exists; revert to native if a broken one is repaired. (2026-09-30)
3. Calcalist scope is exactly the 13 main categories across catalog, generator and live publication; subcategories were retired. (2026-09-30)
4. International sources live in `world/feeds.json` in this repo, not a separate repo. (2026-09-24)
5. Health reporting is a dated snapshot (valid/stale/blocked/failing), never a universal availability claim; automated-blocked does not mean broken on a phone.
6. `feeds.json` is the stable app interface: 21 fixed category IDs, language field, Feedly/Tranco popularity fields; schema changes need app coordination.

## 7. One active feeds repo, no compatibility mirror (2026-10-01)

The owner approved importing generator/worker code here, deploying generated
feeds from this repo, then switching catalog and OPML URLs. Native/world catalog
interfaces remain unchanged. The old repo is archived, not deleted, only after
new live publication and the owner's manual re-subscription check. No app
migration and no ongoing legacy-URL mirror. Existing subscribers must re-add
new URLs (possibly using a rewritten OPML); history/read-state transfer is not
promised. Rejected: a second maintained generator repo, a compatibility mirror,
and automatic app subscription-ID migration. This decision is approved; the
migration is not yet complete.

## Imported generator constraints

The following record describes the source project before consolidation. The
new no-mirror decision above supersedes its separate-repo references. The
30-minute schedule starts only at cutover, and all request PRs now require
manual owner merge.

# DECISIONS

החלטות מתמשכות בפרויקט, כדי שסוכנים ותורמים לא יעבדו כפול.
לכל החלטה: מה הוחלט, למה, ומה נפסל. חדשות בסוף.

## 1. html2rss auto-source על GitHub Actions, לא סקרייפר לאתר ולא שרת (2026-09-25)
רשימת `sites.json` אחת + job מתוזמב (כל 30 דקות) שמריץ html2rss במצב auto-source.
הריפו ציבורי כי דקות Actions חינמיות בריפו ציבורי; ריפו פרטי היה חורג ממכסת הדקות.
נדחה: html2rss-web עצמי על Synology ("אני לא רוצה שרת אצלי"), rss-bridge (סלקטור
לכל אתר), RSSHub (אין routes לאתרים), הטמעת html2rss באפליקציה או פורט ל-Kotlin
(Ruby עם תלויות native; בעלות על היוריסטיקות לנצח ועדכוני extractor כגרסאות אפליקציה).

## 2. קו חוקי קבוע (2026-09-25)
דפים ציבוריים בלבד, בלי עקיפת הגנות או התחברות. robots.txt נכבד. הפידים מכילים
כותרת + קישור + תקציר קצר (עד 500 תווים) ותמונה ממוזערת בלבד; גוף כתבה מלא
(`content:encoded`, תיאורים ארוכים) חסום ונאכף ב-CI. אתר שמבקש להוסר - מוסר.

## 3. רק אתרים בלי RSS מקורי שמיש (2026-09-30)
כל אתר נבדק שאין לו פיד RSS/Atom נגלה לפני הוספה. אם מתגלה או מתקן פיד מקורי,
מעדיפים אותו על המגונרט (מקרה The Verifier: RSS שבור; אם יתוקן - חוזרים אליו).
אתרים עם RSS תקין (Geektime, TGspot, GadgetSite וכו') לא משוכפלים.

## 4. כלכליסט: בדיוק 13 הקטגוריות הראשיות (2026-09-30)
ב-`sites.json`, בפרסום ובקטלוג ההמלצות. תתי-קטגוריות הוסרו (תיקון להחלטת 87 פידים).
טבלאות מניות, דפי משפט/יצירת קשר וחנויות קורסים חיצוניות אינם קטגוריות כתבות
ולא הופכים לפידים. קבצי פידים שהוסרו מהסקופ נמחקים מהפרסום בריצה הבאה.
קטגוריה חדשה של המפרסם דורשת עדכון מפורש; אין גילוי ניווט מחדש בכל ריצה.

## 5. בקשות פיד בשירות עצמי עם שער אימות (2026-09)
בקשות שנפתחות על ידי בעל הריפו מתמזגות אוטומטית רק אחרי אימות: https, מינימום
3 פריטים, וקישורי פריטים באותו דומיין. בקשות של כל אחד אחר מחכות לסקירה ידנית
(מיגון ספאם).

## 6. WordPress: generator גנרי, לא תצורה לאתר (2026-09)
`"generator": "wordpress"` ב-`sites.json`; ה-endpoint נגזר מהדומיין
(`/wp-json/wp/v2/posts`). נשלפים 25 הפוסטים האחרונים, מטא-דאטה בלבד (מזהה, תאריך
UTC, קישור, כותרת, תקציר), לעולם לא גוף מלא. API כבוי/שבור/לא-JSON מדולג עם סיבה
ברורה, והפיד האחרון שעבד נשמר.

## 7. TECH-IL relay: Worker צר, לא פרוקסי פתוח (2026-09-30)
ה-Cloudflare Worker משרת רק את robots.txt ואת רשימת ה-WordPress הקבועה של TECH-IL.
ללא העברת cookies/כותרות, ללא hosts אחרים, ללא שיטות כתיבה. cache של 15 דקות,
שגיאות upstream לא נשמרות, תוכנית חינמית בלבד, והטוקן רק ב-GitHub secrets.
אם `TECH_IL_WORKER_URL` לא מוגדר - חוזרים לשליפה ישירה.

## 8. פרסום: gh-pages נכתב מחדש, last-good נשמר (2026-09)
`gh-pages` מקבל force push בכל ריצה כדי לא לנפח את ההיסטוריה. כשל זמני באתר
משאיר את הפיד האחרון שעבד באוויר ומסמן את האתר בדף הסטטוס.

---

# English

1. html2rss auto-source on GitHub Actions (every 30 min) over a single `sites.json`; public repo because Actions minutes are free there. Rejected: self-hosted html2rss-web, rss-bridge, RSSHub, in-app embedding or a Kotlin port. (2026-09-25)
2. Fixed legal line: public pages only, robots.txt respected, title + link + <=500-char teaser + thumbnail; full bodies blocked and enforced in CI; removal on request. (2026-09-25)
3. Only sites without usable native RSS; a discovered or repaired native feed wins over the generated one (The Verifier case). (2026-09-30)
4. Calcalist scope is exactly the 13 main categories in sites.json, publication and catalog; retired files are deleted from publication; quote tables, legal pages and course stores are not feeds. (2026-09-30)
5. Self-service feed requests: owner-opened requests auto-merge only after validation (https, >=3 items, same-domain item links); all others wait for manual review. (2026-09)
6. WordPress: generic `generator: "wordpress"` with the endpoint derived from the domain; latest 25 posts, metadata only, never full bodies; broken APIs are skipped with a clear reason and last-good XML stays. (2026-09)
7. TECH-IL relay is a narrow Worker (robots.txt + the fixed listing only), not an open proxy: no header forwarding, 15-minute cache, free plan only, token only in GitHub secrets. (2026-09-30)
8. Publishing: gh-pages is force-pushed each run; temporary failures keep the last working feed live and flag the site on the status page. (2026-09)
