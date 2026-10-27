"""Scheduled email dispatcher. Run from GitHub Actions with repository secrets.
Only verified and opted-in email addresses receive mail.
"""
import os, smtplib, ssl
from email.message import EmailMessage
from datetime import datetime, date, timedelta, timezone
import psycopg
from psycopg.rows import dict_row


def send_email(to, subject, body):
    msg=EmailMessage()
    msg['From']=os.environ['SMTP_SENDER']; msg['To']=to
    msg['Subject']=subject; msg.set_content(body)
    host=os.environ['SMTP_HOST']; port=int(os.environ.get('SMTP_PORT','587'))
    if port==465:
        with smtplib.SMTP_SSL(host,port,context=ssl.create_default_context(),timeout=20) as s:
            s.login(os.environ['SMTP_USERNAME'],os.environ['SMTP_PASSWORD']); s.send_message(msg)
    else:
        with smtplib.SMTP(host,port,timeout=20) as s:
            s.starttls(context=ssl.create_default_context())
            s.login(os.environ['SMTP_USERNAME'],os.environ['SMTP_PASSWORD']); s.send_message(msg)


def main():
    required=['DATABASE_URL','SMTP_HOST','SMTP_USERNAME','SMTP_PASSWORD','SMTP_SENDER']
    if any(not os.environ.get(k) for k in required):
        raise SystemExit('Missing email worker configuration; no emails sent.')
    if os.environ.get('ENABLE_EMAIL_DELIVERY') != 'true':
        print('Email delivery disabled; no emails sent.'); return
    now=datetime.now(timezone.utc)
    today=now.date()
    sent=0
    with psycopg.connect(os.environ['DATABASE_URL'],row_factory=dict_row) as conn:
        # Prevent concurrent worker runs from sending the same message.
        with conn.cursor() as cur:
            cur.execute('SELECT pg_try_advisory_lock(73401911)')
            if not cur.fetchone()['pg_try_advisory_lock']:
                print('Another worker is active.'); return
        try:
            with conn.cursor() as cur:
                cur.execute('''SELECT u.id user_id, p.notification_email, p.announcements_enabled,
                    p.reminders_enabled, a.id announcement_id, a.course, a.category,
                    a.deadline, a.message, a.created_at
                    FROM memberships m JOIN users u ON u.id=m.user_id
                    JOIN email_preferences p ON p.user_id=u.id
                    JOIN announcements a ON a.class_id=m.class_id
                    WHERE p.verified=1 AND p.notification_email IS NOT NULL
                    AND (p.announcements_enabled=1 OR p.reminders_enabled=1)
                    ORDER BY a.id DESC''')
                rows=cur.fetchall()
            for row in rows:
                events=[]
                try:
                    created=datetime.fromisoformat(row['created_at'])
                    if created.tzinfo is None: created=created.replace(tzinfo=timezone.utc)
                except (ValueError,TypeError): created=now-timedelta(days=100)
                if row['announcements_enabled'] and timedelta(0) <= now-created <= timedelta(hours=48):
                    events.append(('announcement','New academic announcement'))
                if row['reminders_enabled'] and row['deadline']:
                    try: days=(date.fromisoformat(row['deadline'])-today).days
                    except (ValueError,TypeError): days=-100
                    if days in (7,1,0):
                        events.append((f'deadline_{days}',f'Academic deadline {"today" if days==0 else f"in {days} day(s)"}'))
                for event_type, subject in events:
                    with conn.cursor() as cur:
                        cur.execute('''SELECT 1 FROM email_delivery_log WHERE user_id=%s AND announcement_id=%s AND event_type=%s''',
                                    (row['user_id'],row['announcement_id'],event_type))
                        if cur.fetchone(): continue
                    body=f"{row['course']} · {row['category']}\n\n{row['message']}\n"
                    if row['deadline']: body+=f"\nDeadline: {row['deadline']}\n"
                    body+='\nYou are receiving this because you enabled emails in AI Academic Memory. Sign in to change your preferences.'
                    try:
                        send_email(row['notification_email'],subject+f" — {row['course']}",body)
                    except Exception as exc:
                        print(f'Email delivery failed for user {row["user_id"]}: {type(exc).__name__}')
                        continue
                    with conn.cursor() as cur:
                        cur.execute('''INSERT INTO email_delivery_log(user_id,announcement_id,event_type,sent_at)
                            VALUES(%s,%s,%s,%s) ON CONFLICT DO NOTHING''',
                            (row['user_id'],row['announcement_id'],event_type,now.isoformat()))
                    conn.commit(); sent+=1
        finally:
            with conn.cursor() as cur: cur.execute('SELECT pg_advisory_unlock(73401911)')
    print(f'Email dispatch complete: {sent} sent')

if __name__=='__main__': main()
