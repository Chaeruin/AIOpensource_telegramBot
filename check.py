import telegram
import time, schedule
import pytz
import datetime


token = "6476668027:AAFB2RPrne7Q9W1RLzYoAtaE2BpPKTVhD8w"
bot = telegram.Bot(token = token)

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    public_chat_name = "@chm1231Test"
    text = "current time = " + str(now)
    bot.send_message(chat_id=public_chat_name, text=text)

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


