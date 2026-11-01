# Gold Edition QA report — 2026-11-01

## Completed checks
- Inspected application, database initialization, Streamlit configuration, notification worker and GitHub Actions schedule.
- Python compilation passed for `app.py` and `email_worker.py`.
- TOML configuration parsed successfully.
- Input/selection CSS includes white backgrounds and dark text, including mobile-specific rules.
- Removed broad sidebar CSS rule that forced light text on every descendant, including controls.
- Streamlit toolbar is set to `viewer`; top bar is requested hidden and detailed error display is disabled.
- Escaped user-controlled names and academic-material headings in selected Markdown output.
- Existing table definitions and database URL handling were preserved.

## Not verified / release blockers
- No live Neon database credentials or isolated PostgreSQL test database available; migrations, login, upload/download, search and real data retention are NOT integration-tested.
- No interactive mobile browser session was run; visual appearance and Fork/menu visibility are NOT verified on an actual phone.
- Streamlit Community Cloud sleeping and host-level Fork UI cannot be removed reliably from app code.
- SMTP delivery and 15-minute GitHub scheduled workflow have not been tested live; scheduled Actions can be delayed.
- AI model integration has not been tested with valid provider credits.
- User-uploaded materials are stored in PostgreSQL; confirm size and free-tier storage constraints before scaling.
- This archive is a QA candidate, not a certified production release.

## Safe deployment sequence
1. Back up the production Neon database and ensure materials are included.
2. Create an isolated test deployment with the exact branch and test database.
3. Test student signup/login, class join, representative publishing, search, material upload/download, notifications and role boundaries.
4. Test iPhone Safari and Android Chrome at narrow widths; verify login fields, search boxes, metrics and select menus.
5. Test failure/recovery with a deliberately unavailable TEST database; never deliberately break the production DB.
6. Only promote after all tests pass, keeping the old deployment available for rollback.

## Important limitation
Setting `toolbarMode=viewer` is an application-side preference; it cannot guarantee the removal of every Community Cloud-hosted Fork or sleep screen.
