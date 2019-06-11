#-*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'].upper() == 'WHOAMI':
            bot.sendMessage(chat_id, "My name is hyojong")
        elif msg['text'].upper() == 'PHOTO':
            try:
                bot.sendMessage(chat_id, "IT works")
                bot.sendPhoto(chat_id, open("C:\\Users\\hyojong\\Desktop\\github\\practice\\1.jpg","rb"))
            except Exception as ex:
                print(ex)
        else:
            bot.sendMessage(chat_id, '지원하지 않는 기능입니다')


TOKEN = '827755652:AAEYBQ_ZFNzUQYgVkYn6kjKgYEw3euiXhPw'    # 텔레그램으로부터 받은 Bot API 토큰

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while True:
    time.sleep(1000)