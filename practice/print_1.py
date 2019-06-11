import telepot,sys,time
from pprint import pprint # receive messages updates
from telepot.loop import MessageLoop #receive messages
from telepot.namedtuple import InlineKeyboardButton,InlineKeyboardMarkup
Token = "827755652:AAEYBQ_ZFNzUQYgVkYn6kjKgYEw3euiXhPw"

bot = telepot.Bot(Token) #get a token
#print(bot.getMe())

response = bot.getUpdates()
#pprint(response)

# def handle(msg):  #receive message
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id) #받은메세지의 (메세지 형식, [개인,그룹,else], 내 챗id)

#     if content_type == 'text':
#         bot.sendMessage(chat_id, msg['text'])

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="press me", callback_data="press")],])
    bot.sendMessage(chat_id, "use inline keyboard", reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
    print("Callback Query", query_id,from_id,query_data)
    bot.answerCallbackQuery(query_id, text="Got it")


MessageLoop(bot, {"chat": on_chat_message,"callback_query":on_callback_query}).run_as_thread() #receive message
print("Listening...")

while 1:
    time.sleep(100)





#bot.sendMessage(847661055, "Hello") #sending message