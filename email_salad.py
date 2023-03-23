import win32com.client
import datetime
import pytz

# 서울 표준시를 기준으로 현재 시간을 구한다
seoul = pytz.timezone('Asia/Seoul')
now = datetime.datetime.now(seoul)

# 현재 날짜가 무슨 요일인지 계산
today = now.date()
weekday = today.weekday()

# 다음주 월요일, 금요일 계산
days_to_monday = (7 - weekday) % 7
days_to_friday = (11 - weekday) % 7 + 7
next_monday = today + datetime.timedelta(days=days_to_monday)
next_friday = today + datetime.timedelta(days=days_to_friday)

# 아웃룩 인스턴스 생성
outlook = win32com.client.Dispatch("Outlook.Application")

# 이메일 보내는 함수
def send_mail(to, subject, body, attachments=None):
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    if attachments:
        for attachment in attachments:
            mail.Attachments.Add(attachment)
    mail.Send()

# 이메일 보내기
to = "ilhwa.kim@ourhome.co.kr"
subject = f"건강 샐러드 식사 신청 건 ({next_monday.month}/{next_monday.day}({next_monday.strftime('%a')}) ~ {next_friday.month}/{next_friday.day}({next_friday.strftime('%a')}))"
body = f"""안녕하십니까!
LS엠트론 전자부품생산팀 김종욱입니다.
아래와 같이 건강 샐러드 식사 신청합니다.

1.	성명 : 김종욱
2.	부서명 : 전자부품생산팀
3.	사번 : 20031107
4.	이메일주소 : iuj180@lsmtron.com
5.	핸드폰번호 : 010-7700-5578
6.	신청일 : {next_monday.month}/{next_monday.day}({next_monday.strftime('%a')}) ~ {next_friday.month}/{next_friday.day}({next_friday.strftime('%a')})

감사합니다."""

send_mail(to, subject, body)
