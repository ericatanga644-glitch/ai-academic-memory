# Gold Interface + Academic Materials Library

## Included
- Premium black/white/gold Streamlit theme
- Class-scoped upload/search/download for PDF, PPTX, DOCX and TXT
- Representative-only upload and deletion
- File content persisted in the existing Neon PostgreSQL database
- 8 MB per-file limit; basic file signature checks; 100 visible results
- Existing announcements, AI, accounts and email worker retained

## Deployment
1. Make a new GitHub branch for testing, rather than replacing main immediately.
2. Upload the included files preserving folder paths.
3. Deploy the branch to a separate Streamlit test app using a **separate test database**. Never put production credentials into a public repository.
4. Test representative upload, student search/download, and confirm unauthorized class access is blocked.
5. Only then merge to main and verify existing email notifications and deadlines.

## Limits
- Materials search covers titles, descriptions, filenames and course codes, not full PDF/PPTX contents.
- Files are stored in Postgres for pilot simplicity; migrate to private object storage before scaling.
- No malware scanning; only authorized trusted representatives should upload.
- This code was syntax-checked, not integration-tested against your live Neon database.
