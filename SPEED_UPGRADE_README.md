# AI Academic Memory — Speed Upgrade

This package contains the existing Premium Edition with targeted performance improvements.

## Changes
- Shared, bounded PostgreSQL connection pool (maximum five connections per app process) instead of opening a new TCP/TLS connection for every query.
- Database schema initialization and additive index creation once per running Streamlit server process rather than every widget interaction.
- Indexes for class announcement listing and membership lookups.
- No change to email credentials, SMTP delivery behavior, authentication, announcement editing, deletion, or restoration.

## Deployment
1. Keep the existing Gold Edition unchanged. Use the existing `premium-test` GitHub branch.
2. Back up the Neon test branch before deployment. The app will add non-destructive indexes.
3. Extract this ZIP, and upload its contents to the root of `premium-test` (not the containing directory). `app.py` and `requirements.txt` must be at the root.
4. Commit, then reboot the Streamlit `premium-test` deployment. No secrets changes are required.
5. Verify login, announcements, edit/delete/restore, materials, and email. Compare cold start and repeated clicks before/after.

## Limits
- Initial startup may still take time while Streamlit boots and the pool opens its first connection.
- Email sending is still synchronous. Publishing to many recipients may remain slow. Moving email delivery to a durable background queue requires additional implementation and testing; it is intentionally not changed in this safe first performance patch.
- Streamlit still reruns the script on many interactions. This patch reduces DB setup and connection overhead but cannot make every click instantaneous.
- Compilation/static checks do not substitute for live integration tests.
