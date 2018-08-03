# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import telebot
import os
import time


def get_quote(url):
    return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})).read().decode(encoding='UTF-8')

bot = telebot.TeleBot(os.environ['TELEGRAM_KEY'])
sched = BlockingScheduler()

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! " + message.from_user.first_name + " I am Currency rates bot. How can i help you?")
        
    elif message.text == "Rates":
        
        file_path = os.getcwd() + '/tmp/min_fin_rates.json'
        if not os.path.isfile(file_path):
            min_fin_api_key = os.environ['MIN_FIN_API_KEY']
            all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
            print("load from min fin")
            with open(file_path, 'w') as f: 
                f.write(all_json)
        time_edit = os.path.getmtime(file_path)
        time_now = time.time()
        diff_time = time_now - time_edit
        print(f'{diff_time}')
        if diff_time > 360:
            min_fin_api_key = os.environ['MIN_FIN_API_KEY']
            all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
            print("load from min fin")
            with open(file_path, 'w') as f: 
                f.write(all_json)
        else:
            with open(file_path) as f: 
                all_json = f.read()
                print("load from file")
        
        dictionary_all = json.loads(all_json)
        buy_usd  = dictionary_all['usd']['ask']
        sell_usd = dictionary_all['usd']['bid']

        bot.send_message(message.from_user.id, f'Average buy uah/usd rate {buy_usd}')
        bot.send_message(message.from_user.id, f'Average sell uah/usd rate {sell_usd}')
        
        bot.send_message(message.from_user.id, 'Source of rates: www.minfin.com.ua/currency/')
        bot.send_message(-260766133, f'Average sell uah/usd rate {sell_usd}')
        #bot.send_message(-225550033, f'Average sell uah/usd rate {sell_usd}')
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

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=7)
def send_message_to_group():
    min_fin_api_key = os.environ['MIN_FIN_API_KEY']
    all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
    print("load from min fin for gazik")
    
    dictionary_all = json.loads(all_json)
    buy_usd  = float(dictionary_all['usd']['ask'])
    sell_usd = float(dictionary_all['usd']['bid'])

    today = time.strftime("%d.%m.%Y")

    message_rate = f'{today}. Курс купівлі на валютному аукціоні {buy_usd} грн/$, курс продажу {sell_usd} грн/$'
    message_acc = f'Курс для розрахунку {sell_usd + 0.5} грн/$.'
    bot.send_message(-260766133, message_rate)
    bot.send_message(-260766133, message_acc)
    bot.send_message(-225550033, message_rate)
    bot.send_message(-225550033, message_acc)

@sched.scheduled_job('cron', day_of_week='mon-sat', hour=7, minute=30)
def send_message_to_group_gazik_lviv():
    min_fin_api_key = os.environ['MIN_FIN_API_KEY']
    all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
    print("load from min fin for gazik_lviv")
    
    dictionary_all = json.loads(all_json)
    buy_usd  = float(dictionary_all['usd']['ask'])
    sell_usd = float(dictionary_all['usd']['bid'])

    today = time.strftime("%d.%m.%Y")

    message_rate = f'{today}. Курс купівлі на валютному аукціоні {buy_usd} грн/$, курс продажу {sell_usd} грн/$'
    message_acc = f'Курс для розрахунку {sell_usd + 0.1} грн/$.'
    
    bot.send_message(-260766133, message_rate)
    bot.send_message(-260766133, message_acc)
    bot.send_message(-265791926, message_rate)
    bot.send_message(-265791926, message_acc)

sched.start()
bot.polling(none_stop=True, interval=0)