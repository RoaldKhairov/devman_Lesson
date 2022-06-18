import os
import ptbot
from pytimeparse import parse

TG_TOKEN = os.environ['TELEGRAM_TOKEN']  # подставьте свой ключ API
TG_CHAT_ID = '458765057'  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)



def wait(chat_id, question):
    time_wait = parse(question)
    bot.create_timer(time_wait, notify, author_id=chat_id, message=question)

def notify(author_id, message):
    answer = 'Время вышло'
    bot.send_message(author_id, answer)



bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()