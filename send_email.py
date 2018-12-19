import smtplib #파이썬 내장 모듈. smpt : 전자우편 전송 프로토콜.
from email.message import EmailMessage

import getpass # 비밀번호 보안을 위해
password = getpass.getpass('what`s your password? : ') #아래에 적을 비밀번호

email_list = ['tastera@naver.com', 'tlstjd436@naver.com']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "안녕 난 거니야" #dict 에다가 키 값을 부여한 것임. 원래 []라면 list인뎅?
    msg['From'] = "iamkunhee@naver.com"
    msg['To'] = email
    msg.set_content('리눅스 환경에서 파이썬을 이용해 메일을 보내봅니다 :D') #msg.set_content : 내용 함수.

    smtp_url = 'smtp.naver.com' # 네이버 메일 - 환경설정 - POP/IMAP 설정 들어가면 있음!
    smtp_port = 465

    s = smtplib.SMTP_SSL(smtp_url, smtp_port) #smptlib.SMPT_SLL()은 보안 연결을 위해 하는 작업임.
    
    s.login('iamkunhee', password) #s.login(id, pw)
    s.send_message(msg)
