# Performance update

- Database table/index initialization now runs once per Streamlit server process rather than on every widget rerun.
- Immediate announcement emails reuse one SMTP connection/login per recipient batch and one database connection for delivery logs.
- Existing class-representative Edit/Delete controls remain unchanged.
- Announcement email delivery remains synchronous, so posting to large classes or a slow SMTP server can still take time. No live speed guarantee is made.
- No secrets or database records were changed. Test posting with a temporary announcement, then verify student email delivery and deletion.
