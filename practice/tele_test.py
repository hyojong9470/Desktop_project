import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)

        articles = [InlineQueryResultArticle(
                        id='847661055',
                        title=query_string,
                        input_message_content=InputTextMessageContent(
                            message_text=query_string
                        )
                   )]

        return articles

    answerer.answer(msg, compute)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)

TOKEN = '827755652:AAEYBQ_ZFNzUQYgVkYn6kjKgYEw3euiXhPw'
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result}).run_as_thread()

while 1:
    time.sleep(10)