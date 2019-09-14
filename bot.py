import telebot
import json
from difflib import get_close_matches

bot = telebot.TeleBot('910173641:AAExcjvXF4i7-gn-xeQZ7K9d9WbtpaWwHfc')

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif get_close_matches(w, data.keys()):
        return 'There is no this word, maybe you want to print:\n{}'.format(get_close_matches(w, data.keys())[0])
    else:
        return 'There is no this word!'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! It\'s English Dictionary Bot. Please enter any wrod')

@bot.message_handler(content_types=['text'])
def send_text(message):
    res = translate(message.text)
    output = ''
    if len(res) > 0:
        for item in res:
            output = '{} its list'.format(item)
    else:
        output = res
    bot.send_message(message.chat.id, res)

bot.polling()
