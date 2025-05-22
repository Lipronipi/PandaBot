from distutils.dist import command_re
from email import message_from_bytes
from gc import callbacks

import requests
from io import BytesIO
from PIL import Image

from deep_translator import GoogleTranslator

import random
import datetime
import time
import datetime
import telebot
import webbrowser
from telebot import types
import sqlite3

from panda_class import PandaBot

bot = telebot.TeleBot(${{ secrets.bot }})
panda_bot = PandaBot()


# Обработчики команд
@bot.message_handler(commands=['start', 'logovo'])
def handle_commands(message):
    panda_bot.show_main_menu(message.chat.id)


# Обработчик кнопок
@bot.message_handler(func=lambda m: True)
def handle_actions(message):
    try:
        text = message.text.lower()

        if text == 'кормить панду':
            result = panda_bot.feed_panda(message.from_user.id)
            bot.send_message(message.chat.id, result)

        elif text == 'смотреть на панд':
            msg = bot.send_message(message.chat.id, "Опиши панду:")
            bot.register_next_step_handler(msg, handle_panda_description)

        # Автоматический возврат
        panda_bot.return_to_lair(message)

    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")
        panda_bot.return_to_lair(message)


def handle_panda_description(message):
    image_data = panda_bot.generate_panda_image(message.text)
    if image_data:
        bot.send_photo(message.chat.id, image_data)
    else:
        bot.send_message(message.chat.id, "Не удалось сгенерировать панду :(")
    panda_bot.return_to_lair(message)
