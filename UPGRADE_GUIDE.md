# AI Academic Memory — UI & Notifications Upgrade

## What changed
- Responsive navy/white dashboard and student welcome, summary cards.
- In-app notification centre for unread announcements with mark-as-read state in Neon.
- Academic calendar summary of dated announcements.
- Email preferences now support six-digit verification codes via SMTP.
- Scheduled GitHub Actions worker sends opted-in, verified students announcement emails and deadline reminders 7 days, 1 day and on due date; log prevents duplicate sends.
- Existing login, representative permissions, classes, announcements, AI analysis and search retained.

## Safe deployment
1. **Back up the Neon database** (and retain the original GitHub commit). Never delete the existing Neon tables.
2. Upload the updated `app.py`, `email_worker.py`, `requirements.txt`, `.github/workflows/email-notifications.yml` and `.streamlit/config.toml` to your EXISTING GitHub repo, retaining the file paths. Streamlit redeploys automatically.
3. Test registration, sign-in, representative publishing, student join, AI analysis and notification read state with two accounts before inviting the whole class.
4. To enable verification emails, configure Streamlit Secrets (do not put credentials in GitHub):
   `SMTP_HOST`, `SMTP_PORT` (usually `587`), `SMTP_USERNAME`, `SMTP_PASSWORD`, `SMTP_SENDER`.
   Use an SMTP service that permits authenticated sending and verify the sender domain as required.
5. For scheduled emails, add `DATABASE_URL` and the same `SMTP_*` values as **GitHub repository Actions secrets**, plus `ENABLE_EMAIL_DELIVERY` set to `true` **only after successful test**. Until enabled, the worker sends nothing.
6. Under GitHub Actions, run `Academic email notifications` manually once and inspect the run log (do not share secret values). Daily cron is 07:15 UTC = 07:15 Ghana time, subject to GitHub Actions scheduling delays. GitHub scheduled workflows may be delayed or disabled on inactive repositories; production reliability may require a dedicated scheduler.
7. Have a student save a notification email, request the code, verify it, and enable email options. Run the worker and check receipt. Email sending is not guaranteed until the SMTP provider and scheduler are configured and tested.

## Privacy and limitations
- **No email** is sent to unverified or opted-out addresses.
- Email notifications are sent once per event per student using `email_delivery_log`.
- Emails only cover announcements created within 48 hours of a worker run; deadline reminders occur on 7-day, 1-day, and due-date milestones. Deadlines are dates, not times, so no three-hour reminder is claimed.
- In-app notifications are generated from unread announcements when a student opens the app. They are **not phone push notifications**.
- Keep `DATABASE_URL`, `OPENAI_API_KEY`, SMTP credentials and invite codes out of GitHub and ZIP uploads.
- This upgrade has passed static syntax checks but **has not been tested against your live Neon database or SMTP provider**; deploy and test carefully.
