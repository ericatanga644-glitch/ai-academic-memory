# Student-facing release acceptance checks

- [ ] Neon branch confirmed non-expiring and backed up
- [ ] Render service healthy and app loads after a fresh browser session
- [ ] Student login, logout, incorrect password, and signup work
- [ ] Class representative can create and publish announcement
- [ ] Student sees announcement and can mark it read
- [ ] Verified opted-in student receives an immediate publication email
- [ ] Duplicate email is not sent for the same announcement
- [ ] Deadline reminder worker runs and records sent events
- [ ] Materials upload, search, and download work across devices
- [ ] Mobile inputs, metrics, menus and dropdowns are legible
- [ ] Students do not encounter Streamlit Cloud's sleep/fork screen
- [ ] Database disconnect results in a safe error, not traceback
- [ ] No API keys, database URLs or SMTP credentials in GitHub
- [ ] Rollback URL retained until production checks pass
