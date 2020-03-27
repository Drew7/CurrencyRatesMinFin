# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import telebot
import os
import time
import requests


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

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=8, minute=10)
def send_message_to_group():
    min_fin_api_key = os.environ['MIN_FIN_API_KEY']
    all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
    print("load from min fin for gazik")
    
    dictionary_all = json.loads(all_json)
    buy_usd  = float(dictionary_all['usd']['ask'])
    sell_usd = float(dictionary_all['usd']['bid'])

    today = time.strftime("%d.%m.%Y")

    message_rate = f'{today}. Курс купівлі на валютному аукціоні {buy_usd} грн/$, курс продажу {sell_usd} грн/$'
    message_acc = f'Курс для розрахунку {round(sell_usd + 0.5, 2)} грн/$.'
    bot.send_message(-260766133, message_rate)
    bot.send_message(-260766133, message_acc)
    bot.send_message(-225550033, message_rate)
    bot.send_message(-225550033, message_acc)
    
        
    priceUSD_MikroTik_hAP_Lite_TC = 24.80
    
    priceUSD_TP_LINK_Archer_C20 = 33.96
    
    priceUSD_Xiaomi_Mi_WiFi_Router_4A_Gigabit_Edition = 39.96
    
    priceUSD_TP_LINK_Archer_C6 = 59.96
    
    priceUSD_Mikrotik_cAP_ac = 69.96
    
    priceUSD_MikroTik_hAP_ac2 = 67.96
    
    
    rateUSD = round(sell_usd + 0.5, 2)

    html_text = """<style type='text/css'>
.tg  {border-collapse:collapse;border-spacing:0;border-color:#93a1a1;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#002b36;background-color:#fdf6e3;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#fdf6e3;background-color:#657b83;}
.tg .tg-2bhk{background-color:#eee8d5;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-ezbu{background-color:#eee8d5;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-alz1{background-color:#eee8d5;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-i6s1{background-color:#eee8d5;text-align:center;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class='tg' style='undefined;table-layout: fixed; width: 931px'>
<colgroup>
<col style='width: 474px'>
<col style='width: 109px'>
<col style='width: 93px'>
<col style='width: 255px'>
</colgroup>
  <tr>
    <th class='tg-0pky'>Роутери</th>
    <th class='tg-c3ow'>Ціна в  '$'</th>
    <th class='tg-c3ow'>Ціна в 'ГРН'</th>
    <th class='tg-c3ow'>Ціна для  клієнта в дома +100 грн</th>
  </tr>
  <tr>
    <td class='tg-2bhk'>MikroTik hAP Lite TC  (MT RB941-2nD-TC)</td>
    <td class='tg-ezbu'>""" + str(priceUSD_MikroTik_hAP_Lite_TC) + """ $</td>
    <td class='tg-ezbu'>""" + str(round(priceUSD_MikroTik_hAP_Lite_TC * rateUSD, 2)) + """ ₴</td>
    <td class='tg-ezbu'>""" + str(round(priceUSD_MikroTik_hAP_Lite_TC * rateUSD, 2) + 100) + """ ₴</td>
  </tr>
  <tr>
    <td class='tg-0pky'>TP-LINK Archer C20</td>
    <td class='tg-c3ow'>""" + str(priceUSD_TP_LINK_Archer_C20) + """ $</td>
    <td class='tg-c3ow'>""" + str(round(priceUSD_TP_LINK_Archer_C20 * rateUSD, 2)) + """ ₴</td>
    <td class='tg-c3ow'>""" + str(round(priceUSD_TP_LINK_Archer_C20 * rateUSD, 2) + 100) + """ ₴</td>
  </tr>
  <tr>
    <td class='tg-alz1'>Xiaomi Mi WiFi Router 4A Gigabit Edition</td>
    <td class='tg-i6s1'>""" + str(priceUSD_Xiaomi_Mi_WiFi_Router_4A_Gigabit_Edition) + """ $</td>
    <td class='tg-i6s1'>""" + str(round(priceUSD_Xiaomi_Mi_WiFi_Router_4A_Gigabit_Edition * rateUSD, 2)) + """ ₴</td>
    <td class='tg-i6s1'>""" + str(round(priceUSD_Xiaomi_Mi_WiFi_Router_4A_Gigabit_Edition * rateUSD, 2) + 100) + """ ₴</td>
  </tr>
  <tr>
    <td class='tg-0lax'>TP-LINK Archer C6</td>
    <td class='tg-baqh'>""" + str(priceUSD_TP_LINK_Archer_C6) + """ $</td>
    <td class='tg-baqh'>""" + str(round(priceUSD_TP_LINK_Archer_C6 * rateUSD, 2)) + """ ₴</td>
    <td class='tg-baqh'>""" + str(round(priceUSD_TP_LINK_Archer_C6 * rateUSD, 2) + 100) + """ ₴</td>
  </tr>
  <tr>
    <td class='tg-alz1'>Mikrotik cAP ac (RBcAPGi-5acD2nD)</td>
    <td class='tg-i6s1'>""" + str(priceUSD_Mikrotik_cAP_ac) + """ $</td>
    <td class='tg-i6s1'>""" + str(round(priceUSD_Mikrotik_cAP_ac * rateUSD, 2)) + """ ₴</td>
    <td class='tg-i6s1'>""" + str(round(priceUSD_Mikrotik_cAP_ac * rateUSD, 2) + 100) + """ ₴</td>
  </tr>
  <tr>
    <td class='tg-0lax'>MikroTik hAP ac² (RBD52G-5HacD2HnD-TC)</td>
    <td class='tg-baqh'>""" + str(priceUSD_MikroTik_hAP_ac2) + """ $</td>
    <td class='tg-baqh'>""" + str(round(priceUSD_MikroTik_hAP_ac2 * rateUSD, 2)) + """ ₴</td>
    <td class='tg-baqh'>""" + str(round(priceUSD_MikroTik_hAP_ac2 * rateUSD, 2) + 100) + """ ₴</td>
  </tr>
</table>"""
    

    HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
    HCTI_API_USER_ID = os.environ['HCTI_API_USER_ID']
    HCTI_API_KEY = os.environ['HCTI_API_KEY']

    data = { 'html': html_text,
         'css': '.box { color: white; background-color: #0f79b9; padding: 10px; font-family: Roboto }',
         'google_fonts': "Roboto" }

    image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))
    image_url = image.json()['url']
 
    tags = 'Ціни на роутери'
    message_text = '<a href="' + image_url + '">' + tags + '</a>'

    bot.send_message(parse_mode='HTML', chat_id=-225550033, text=message_text)
    

'''@sched.scheduled_job('cron', day_of_week='mon-sat', hour=8, minute=30)
def send_message_to_group_gazik_lviv():
    min_fin_api_key = os.environ['MIN_FIN_API_KEY']
    all_json = get_quote(f'http://api.minfin.com.ua/auction/info/{min_fin_api_key}/')
    print("load from min fin for gazik_lviv")
    
    dictionary_all = json.loads(all_json)
    buy_usd  = float(dictionary_all['usd']['ask'])
    sell_usd = float(dictionary_all['usd']['bid'])

    today = time.strftime("%d.%m.%Y")

    message_rate = f'{today}. Курс купівлі на валютному аукціоні {buy_usd} грн/$, курс продажу {sell_usd} грн/$'
    message_acc = f'Курс для розрахунку {round(sell_usd + 0.1, 2)} грн/$.'
    
    bot.send_message(-260766133, message_rate)
    bot.send_message(-260766133, message_acc)
    bot.send_message(-265791926, message_rate)
    bot.send_message(-265791926, message_acc)'''

sched.start()
bot.polling(none_stop=True, interval=0)
