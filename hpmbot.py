# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:24:54 2022

@author: User
"""

import telebot
import datetime as dt
import portion
import random

token = '5465560133:AAEj3anQ-lD3QIThYFTCsEGBuzXRXrJuBbE'
bot = telebot.TeleBot(token)

def hello():
    helloWay = random.choice([0,1])
    if (helloWay == 0):
        return random.choice(['Здравствуй!', 'Привет!'])
    elif (helloWay == 1):
        now = dt.datetime.now()
        morning = portion.open(5, 10)
        daytime = portion.open(11, 16)
        evening = portion.open(17, 23)
        night = portion.open(0, 4)
        if (now.hour in morning):
            return 'Доброе утро!'
        elif (now.hour in daytime):
            return 'Добрый день!'
        elif (now.hour in evening):
            return 'Добрый вечер!'
        elif (now.hour in night):
            return 'Доброй ночи!'

@bot.message_handler(content_types=['text'])
def send(message):
    bot.send_message(message.chat.id, hello())
    
# RUN
bot.polling(none_stop=True)