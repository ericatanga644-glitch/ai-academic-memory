# AI Academic Memory — KNUST Classroom Pilot

Deploy on Streamlit Community Cloud from this private GitHub repository.

## Required Streamlit Secrets (Settings > Secrets)
Set each value **in Streamlit Cloud only**, never commit it:

```toml
DATABASE_URL = "postgresql://<user>:<password>@<neon-pooled-host>/<database>?sslmode=require"
OPENAI_API_KEY = "<your-openai-key>" # optional; omit to use rule-based search
PILOT_ADMIN_EMAILS = "your-registered-email@example.com"
PILOT_INVITE_CODE = "a-long-random-classroom-registration-code"
```

The admin email must match the account you register on the new hosted database. The first user should register using the invitation code and then create the class. Students register with the invitation code, then join using the class join code. Keep the invitation code within the pilot group.

## IMPORTANT
- This hosted deployment uses a **new Neon PostgreSQL database**. Existing SQLite accounts and announcements **do not automatically migrate**. Back up your old `academic_memory.db` locally and keep it out of GitHub. The class and test accounts will be recreated online.
- Email preference saving is included, but **automatic email delivery, email verification, WhatsApp, and push alerts are not enabled**.
- Class creation is limited to `PILOT_ADMIN_EMAILS`. The creator becomes representative. Joining a class does not grant representative privileges.
- Registration is gated by `PILOT_INVITE_CODE` but email ownership is not yet verified. Keep the pilot small and supervised. Do not use real student passwords reused from other services.
- Streamlit sessions do not provide enterprise-grade identity security. This is a controlled classroom pilot, **not a production system**.
- OpenAI calls cost money. Consider leaving `OPENAI_API_KEY` unset until your basic pilot is working.
- Do not publish confidential academic or personal data. Review the app's permissions before a wider rollout.

## Deployment
1. Upload ONLY files from this folder to the `ai-academic-memory` private GitHub repository (upload the contents, not the ZIP). Include `.streamlit/config.toml` if GitHub upload supports it; it is optional.
2. Create Streamlit Community Cloud app, select repository and `app.py`, and deploy.
3. In Advanced settings / Secrets add the values above before first successful launch.
4. Test as organizer, then as student on a second device. Check that a student cannot publish.
5. Test persistence after reloading the page, and confirm the database tables in Neon.

## Known limits
- No server-side rate limiting or verified email identity yet.
- Date extraction stores one date/category per announcement. Representatives should split multi-topic announcements into separate entries.
- Conflict review is heuristic and must be verified by a representative.
- Hosted Streamlit Community Cloud and Neon free tiers may sleep, rate-limit or impose resource limits.
