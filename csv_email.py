import smtplib #파이썬 내장 모듈. smpt : 전자우편 전송 프로토콜.
from email.message import EmailMessage
import csv

import getpass # 비밀번호 보안을 위해
password = getpass.getpass('what`s your password? : ') #아래에 적을 비밀번호

smtp_url = 'smtp.naver.com' # 네이버 메일 - 환경설정 - POP/IMAP 설정 들어가면 있음!
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port) #smptlib.SMPT_SLL()은 보안 연결을 위해 하는 작업임.

s.login('iamkunhee', password) #s.login(id, pw)


f = open('pygj.csv', 'r', encoding = 'utf-8') # 파일 열기. 불러오고 싶은 파일과 같은 위치에 있어야 열 수 있음. 'r' : read
read_csv = csv.reader(f) #csv.reader라는 것으로 이 f(파일)을 열 것이다.


for line in read_csv:
    msg = EmailMessage()
    msg['Subject'] = "안녕하세요 송건희 입니다." #dict 에다가 키 값을 부여한 것임. 원래 []라면 list인뎅?
    msg['From'] = "iamkunhee@naver.com"  # '' vs "" 그냥 좀 차이가 있다. 라고만 일단 알아둘 것.
    msg['To'] = line[1]
    msg.set_content(line[0] + '님에게..' + '이 편지는 영국에서 최초로 시작되어 일년에 한 바퀴 돌면서 받는 사람에게 행운을 주었고 지금은 당신에게로 옮겨진 이 편지는 4일 안에 당신 곁을 떠나야 합니다. 이 편지를 포함해서 7통을 행운이 필요한 사람에게 보내 주셔야 합니다. 복사를 해도 좋습니다. 혹 미신이라 하실지 모르지만 사실입니다. 영국에서 HGXWCH이라는 사람은 1930년에 이 편지를 받았습니다. 그는 비서에게 복사해서 보내라고 했습니다. 며칠 뒤에 복권이 당첨되어 20억을 받았습니다. 어떤 이는 이 편지를 받았으나 96시간 이내 자신의 손에서 떠나야 한다는 사실을 잊었습니다. 그는 곧 사직되었습니다. 나중에야 이 사실을 알고 7통의 편지를 보냈는데 다시 좋은 직장을 얻었습니다. 미국의 케네디 대통령은 이 편지를 받았지만 그냥 버렸습니다. 결국 9일 후 그는 암살 당했습니다. 기억해 주세요. 이 편지를 보내면 7년의 행운이 있을 것이고 그렇지 않으면 3년의 불행이 있을 것입니다. 그리고 이 편지를 버리거나 낙서를 해서는 절대로 안됩니다. 7통입니다. 이 편지를 받은 사람은 행운이 깃들 것입니다. 힘들겠지만 좋은게 좋다고 생각하세요. 7년의 행운을 빌면서..') #msg.set_content : 내용 함수.

    s.send_message(msg)

    
f.close() #파일 닫기