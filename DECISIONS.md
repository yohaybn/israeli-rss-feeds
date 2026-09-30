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
