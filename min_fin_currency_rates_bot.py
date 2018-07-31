# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
import json
import telebot
import os
import time


def get_quote(url):
    return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})).read().decode(encoding='UTF-8')

bot = telebot.TeleBot(os.environ['TELEGRAM_KEY'])

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! " + message.from_user.first_name + " I am Currency rates bot. How can i help you?")
        
    elif message.text == "Rates":
        
        file_path = os.getcwd() + '/tmp/min_fin_rates.json'
        if not os.path.isfile(file_path):
            min_fin_api_key = os.environ['MIN_FIN_API_KEY']
            all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
            with open(file_path, 'w') as f: 
                f.write(all_json)
        time_edit = os.path.getmtime(file_path)
        time_now = time.time()
        diff_time = time_now - time_edit

        if diff_time > 360:
            min_fin_api_key = os.environ['MIN_FIN_API_KEY']
            all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
            with open(file_path, 'w') as f: 
                f.write(all_json)
        else:
            with open(file_path) as f: 
                all_json = f.read()
        
        dictionary_all = json.loads(all_json)
        buy_usd  = dictionary_all['usd']['ask']
        sell_usd = dictionary_all['usd']['bid']

        bot.send_message(message.from_user.id, f'Average buy uah/usd rate {buy_usd}')
        bot.send_message(message.from_user.id, f'Average sell uah/usd rate {sell_usd}')
        
        bot.send_message(message.from_user.id, 'Source of rates: www.minfin.com.ua/currency/')

        
    else:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*[telebot.types.KeyboardButton(name) for name in ['Hi', 'Rates']])
        bot.send_message(message.chat.id, "Choose one option:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Help yourself.")

@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    bot.send_message(message.from_user.id, "What?")

bot.polling(none_stop=True, interval=0)