# Gold Edition reliability release

## Changes
- PostgreSQL connections retry transient operational errors up to three times.
- Database startup errors show a safe retry screen instead of a traceback.
- Mobile metric numbers, input controls, dropdowns, and spacing have improved contrast.
- Scheduled email worker interval changed from hourly to every 15 minutes. GitHub Actions schedules are best effort and may be delayed.

## Before deployment
1. Back up the existing Neon production database. Do not create or switch databases without a migration plan.
2. Confirm Streamlit DATABASE_URL points to the intended active, non-expiring Neon production branch. Never put connection strings in GitHub.
3. Confirm GitHub Actions GOLD_DATABASE_URL points to the **same database** as the Streamlit app.
4. Upload these files to the gold_upgrade branch and redeploy that branch.
5. Verify organizer login, student login, announcements, materials, email preferences, deadline emails, and mobile layout.
6. Verify Streamlit logs after launch. If the database is unavailable, the retry screen will appear until it recovers.

## Important limits
- This patch cannot prevent Streamlit Community Cloud from sleeping or showing its own platform wake screen. An always-on hosting plan or migration to an appropriate provider is needed to avoid platform sleeping.
- Fifteen-minute scheduled polling does not provide immediate email delivery. For immediate delivery, a reliable event-driven queue/worker and deployment configuration are required.
- No live database, SMTP, GitHub Actions, or phone-browser end-to-end testing was possible in this offline package audit.
- Do not treat this as a production availability guarantee.
