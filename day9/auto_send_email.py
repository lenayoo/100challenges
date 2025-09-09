import smtplib
from email.message import EmailMessage
import sys
import os
import os
from pathlib import Path
from dotenv import load_dotenv
from email.message import EmailMessage

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# sender/receiver설정
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = "socheca@naver.com"

# 명령줄 인자 확인
if len(sys.argv) < 3:
    print("사용법: python send_mail.py '제목' '내용'")
    sys.exit(1)

subject = sys.argv[1]
body = sys.argv[2]

# 이메일 메시지 객체 생성
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = SENDER_EMAIL
msg['To'] = RECIPIENT_EMAIL
msg.set_content(body)

with open("email_template.html", "r", encoding="utf-8") as f:
    html_body = f.read()

html_body = (html_body
             .replace("{{ subject }}", subject)
             .replace("{{ body }}", body.replace("\n", "<br>")))


msg.add_alternative(html_body, subtype="html")


try:
    # SMTP 서버 연결
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # TLS 보안 시작
        smtp.starttls()
        # 로그인
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        # 이메일 전송
        smtp.send_message(msg)

    print("메일 전송 완료 🥳")

except Exception as e:
    print(f"메일 전송 실패: {e}")