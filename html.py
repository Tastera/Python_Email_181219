import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('what`s your password? : ')

email_list = ['tastera@naver.com', 'tlstjd436@naver.com']


msg = EmailMessage()
msg['Subject'] = "안녕 난 거니야"
msg['From'] = "iamkunhee@naver.com"
msg['To'] = "skh4125@gmail.com"
#msg.set_content('')
msg.add_alternative('''
<h1>안녕하세요.</h1> 
<p>저는 송건희입니다.</p> 
''', subtype="html") 
#string을 여러 줄 거쳐서 보낼 때 ``` 사용함. subtype="html" : html 형식 사용.
#h1 : 글자 크고 진하게
#p : 

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port) #smptlib.SMPT_SLL()은 보안 연결을 위해 하는 작업임.

s.login("iamkunhee@naver.com", password) #s.login(id, pw)
s.send_message(msg)
