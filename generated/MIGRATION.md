# Staged migration checklist

Approved: one active repo, new generated URLs, manual re-subscription, no mirror.
The owner merges PRs. Never archive the old repo before the final owner check.

1. Merge source/workflow import. No catalog URL change in this stage.
2. Enable this repo's Pages with GitHub Actions. Configure TECH_IL_WORKER_URL
   with the verified existing public relay. No token is needed for generation.
   Manual future relay deployment additionally needs CLOUDFLARE_ACCOUNT_ID and
   securely supplied CLOUDFLARE_API_TOKEN; no secret is stored in source.
3. Run Generate and publish feeds. First run copies old gh-pages; subsequent
   runs restore this repo's gh-pages. Last-good XML survives source failures.
   Validate each public feed, status and all 13 Calcalist categories plus TECH-IL.
   Compare article GUIDs/dates to the previous publication.
4. Follow-up PR switches catalog/OPML URLs, removes retired calcalist.xml,
   rebuilds derived catalog counts/status and adds the 30-minute schedule.
   Coordinate disabling the old schedule so there is only one ongoing scraper.
5. Owner imports a revised OPML or manually re-subscribes, checks refresh and
   folder/settings. Old URLs and cloud backups are not migrated automatically.
6. Only after the owner's check: stop old generation, add an unmaintained/moved
   README notice and archive the old repo. No deletion or XML compatibility.

Rollback requires restoring old generation and catalog/OPML from saved commit
references. New subscriptions also need switching back manually. Archived repo
must first be unarchived if its workflows need to run again.
