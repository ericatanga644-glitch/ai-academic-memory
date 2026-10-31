from pathlib import Path
import ast

root=Path(__file__).resolve().parents[1]
src=(root/'app.py').read_text()
ast.parse(src)
for token in ('premium_initialize','Delete announcement','Restore announcement','student_tasks','announcement_bookmarks','class_timetable','send_immediate_announcement_emails'):
    assert token in src, token
print('Static feature checks passed')
