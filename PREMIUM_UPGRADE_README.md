# AI Academic Memory — Premium Announcement Management Upgrade

## Included in this build
- **Class-representative announcement management**: edit course, category, date and message; pin; soft delete; restore; and view audit events.
- **Student visibility**: deleted announcements are excluded from class feeds, notifications, search, deadline calendar, and conflict checks.
- **Scheduled email worker**: excludes deleted announcements from subsequent emails and reminders.
- **Design refinement**: updated mobile spacing, button hover states and edition label.
- All existing account, membership, materials, SMTP, and AI functionality is retained.

## Not yet included
The broader requested premium roadmap (lecturer roles, rich calendar, AI document retrieval, password recovery, file storage redesign, notifications for edits, dark-mode switch, multi-university support) requires additional implementation and testing. This package does **not** claim these features are ready.

## Safe deployment
1. Take a **database backup** and preserve the current production branch. Never include credentials in a ZIP.
2. Create a **separate testing deployment** pointing to a separate Neon test database or a restored copy. Avoid running this build against production until verified.
3. Upload the changed files as a new Git branch. Keep existing Streamlit Cloud secrets; no new secrets are required.
4. On first launch, `initialize()` adds columns and the audit table using `IF NOT EXISTS`. Database user must have schema-alter privileges.
5. Test as a class rep: publish a demo announcement, edit it, pin it, delete it, show deleted, restore it.
6. Test as a student: deleted announcements must disappear from feed, search, unread counts, and calendar. Restored announcements should return.
7. Test GitHub Actions email worker with test recipients, including deletion before a scheduled reminder.
8. If anything fails, switch Streamlit deployment back to the old commit. Database additive schema changes are backward-compatible; do not drop the added columns without a deliberate migration.

## Important limitations
- Existing sent emails cannot be recalled. Editing/deleting does not automatically send a correction email. Publish a clearly labeled correction as a new announcement for now.
- Audit records log old/new data for edits; delete/restore log actions.
- This code was syntax-checked locally but **not** integration-tested against your private Neon database or SMTP service.
- The archive's older README may describe a previous pilot version. This file describes this upgrade.
