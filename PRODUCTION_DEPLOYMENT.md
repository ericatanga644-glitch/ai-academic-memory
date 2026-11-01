# AI Academic Memory — Production deployment runbook

## Why this is different
The included Render Blueprint provisions a paid **Starter** Python web service. Unlike free sleeping services, it is intended to run continuously. This is not an uptime guarantee. Confirm current Render pricing, region, and plan availability before approving charges. The existing Streamlit application and database schema are preserved.

## Before changing anything
1. In Neon, identify the active database currently used by the Gold Edition. Confirm it is a durable production branch, **not** a temporary expiring test branch.
2. Make a verified backup of that database, including users, memberships, announcements, materials and notification logs. Do not put backups or credentials in GitHub.
3. Keep the existing Streamlit deployment online until the replacement is fully tested.
4. Confirm the app's Streamlit `DATABASE_URL` and GitHub Actions `GOLD_DATABASE_URL` refer to the intended **same** database. Do not paste secret values into chat or screenshots.

## Deploy the replacement
1. Upload the contents of this folder to the GitHub repository's `gold_upgrade` branch, preserving `.github/workflows/email-reminders.yml`.
2. On Render, choose **New → Blueprint**, select that repository and branch, and review `render.yaml`.
3. Confirm the service plan is **Starter (paid)** before approving. Supply the `DATABASE_URL`, `SMTP_HOST`, `SMTP_USERNAME`, `SMTP_PASSWORD`, and `SMTP_SENDER` values privately in Render's environment configuration. Set SMTP_PORT to 465 if your provider requires implicit TLS, otherwise use 587 for STARTTLS.
4. Deploy. Visit the Render URL and check that the app loads, without exposing the GitHub repository or developer menus to students.
5. Configure the GitHub Actions repository secret `GOLD_DATABASE_URL` to the same Neon production database. SMTP secrets must also be present in GitHub Actions. The scheduled email worker is separate from Render.
6. Test with an organizer and a student account on two devices. Confirm new announcements, immediate email to a verified opted-in recipient, material upload/download, deadline reminders, searches, and mobile contrast. Check logs for errors without exposing secrets.
7. Only after successful verification, distribute the new Render URL to students. Keep the old deployment as a rollback option until confidence is established.

## Failure and rollback
- A failed database connection shows a retry screen in the app. If it persists, check whether the Neon branch is active, the connection string is valid, and database networking is allowed.
- A working `/ _stcore/health` check (without the space) confirms the Streamlit process responds, **not** that the database, login or email works. Use the end-to-end checks above.
- If the new deployment fails, continue using the old deployment. Do not restore an old database backup over new student data without a deliberate recovery plan.
- GitHub Actions scheduled workflows may run late. Immediate announcement email is best-effort, and is not a durable queue. Production-grade guaranteed notification delivery would require a queue and independent worker.

## Known limitations
- The Streamlit interface still includes Streamlit framework chrome. The Render-hosted app does not show Streamlit Community Cloud's sleep/fork landing page, but it is not a bespoke frontend.
- A paid always-on service is not immune to provider outages or Neon failures.
- This package was syntax-checked offline; no real credentials or student data were accessed, and live deployment tests are still required.
