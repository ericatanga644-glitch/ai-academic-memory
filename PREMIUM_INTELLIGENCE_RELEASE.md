# Premium Intelligence + Mobile Upgrade

Built on the previous Speed Upgrade. Keeps existing accounts, SMTP settings, announcement edit/delete/restore, materials and database pool.

## Changes
- Improved mobile spacing, touch controls, responsive typography and accessible focus indicators.
- Student quick overview of next recorded deadline and latest unread announcement.
- Verified, intent-aware class memory search: course-specific deadlines, cancellations and materials.
- No Gemini API key required for verified record search.

## Deployment
1. Backup the existing premium-test branch before uploading.
2. Upload all files in this directory to the repository root of premium-test (not a nested directory).
3. Keep Streamlit Secrets and DATABASE_URL unchanged.
4. Allow Streamlit to redeploy.
5. Verify sign-in, notifications, edit/delete/restore, material downloads and mobile layout.
6. Test a CHE 291 assignment deadline query. A cancellation should not be returned as a deadline.

## Limitations
- The rule-based engine only uses stored verified announcements; it does not understand arbitrary language or extract searchable text from PDFs.
- Streamlit reruns and synchronous email delivery remain; this release does not claim native-app speed.
- Actual deployed behavior and mobile responsiveness require live testing.
