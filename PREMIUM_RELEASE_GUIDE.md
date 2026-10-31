# AI Academic Memory — Premium Integrated Release

## Included in this package
- Existing Gold Edition login, student/class-rep membership, class announcement publishing, immediate email and scheduled reminder worker.
- Class representative announcement editing, soft deletion, restoration, pinning and audit history.
- Personal student tasks with completion status and target dates.
- Weekly class timetable with class representative management.
- Saved/bookmarked announcements, searchable materials and announcement search.
- Responsive styling refinements and existing dashboard/notification centre.
- AI provider integration inherited from Gold Edition with rule-based search fallback on API errors.

## Important limitations
This is a comprehensive upgrade of the existing Streamlit pilot, not a verified university-scale product. Lecturer roles, true calendar synchronization, push notifications, file OCR, document-grounded AI answers, email correction notifications, full administration, automated backup, and production-scale security review are NOT implemented. Do not represent them as finished.

## Safe deployment
1. Back up your Neon PostgreSQL database using a snapshot/branch before deploying.
2. Create a new Streamlit test app using a test branch and a separate database branch.
3. Keep existing Streamlit secrets configured in the hosting console. Never upload real secrets.
4. Run `pip install -r requirements.txt` and `python -m compileall -q .`.
5. Test sign-up/login, rep and student permissions, announcement create/edit/delete/restore, email notification, upload/download, bookmarks, personal tasks, timetable, and mobile UI.
6. Only after tests pass, deploy the same code to production.

No secrets or real student data are included in this ZIP.
