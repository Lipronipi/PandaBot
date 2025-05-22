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
class PandaBot:
    def __init__(self):
        self.phrases = ["Нужно больше спать...", "Язык мой – враг мой", "Даже солнце не всем одинаково светит", "Не руби сук на котором сидишь", "Большому кораблю, большое плавание", "Лучше синица в руках, чем журавль в небе", "Скоро сказка сказывается, да не скоро дело делается", "Хороша Маша, да не наша"]
        self.actions = {
            'feed': self.feed_panda,
            'wash': self.wash_panda,
            'train': self.train_panda,
            'view': self.view_pandas
        }

    # Основные методы
    def return_to_lair(self, message):
        """Показывает главное меню"""
        self.show_main_menu(message.chat.id)

    def show_main_menu(self, chat_id):
        """Отображает клавиатуру логова"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # ... создание кнопок
        btn1 = types.KeyboardButton('Смотреть на панд')
        btn2 = types.KeyboardButton('Кормить панду', )
        btn3 = types.KeyboardButton('Купать панду')
        btn4 = types.KeyboardButton('Тренировка')
        a.row(btn2, btn3)
        a.row(btn4)
        a.row(btn1)
        #
        bot.send_photo(chat_id, open('./panda.jpg', 'rb'),
                      caption='Ты в логове. Слышишь как растёт бамбук?',
                      reply_markup=markup)

    # Методы работы с пандой
    def feed_panda(self, mas):
        """Логика кормления панды"""
        with sqlite3.connect('power_panda.sql') as conn:
            # ... запросы к БД
            bot.send_message(mas.chat.id, 'Подожди чуток. Твоя панда ест...')
            time = 0
            cur = conn.cursor()

            id = mas.from_user.id
            cur.execute(f"SELECT * FROM users WHERE idTG = {id}")

            el = cur.fetchone()
            t1 = el[4]
            t2 = datetime.datetime.now().timestamp()
            cur.execute(f"UPDATE users SET eat = '{t2}' WHERE idTG = {id}")
            t = (t2 - t1) // 1

            conn.commit()
            cur.close()
            conn.close()

            bot.send_photo(mas.chat.id, open('./eat.png', 'rb'))
            bot.send_message(mas.chat.id,
                             f'До этого момента твоя панда не ела целых {t} секунд! /logovo')
        return "Панда накормлена!"

    def wash_panda(self, user_id):
        """Логика купания панды"""
        bot.send_photo(mas.chat.id, open('./vanna.webp', 'rb'))
        return random.choice(self.phrases)

    # Методы генерации
    def view_pandas(self, description):
        """Генерация изображения через API"""
        prompt = GoogleTranslator(source='auto', target='en').translate(f"Панда {description}")
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{MODEL_NAME}",
            headers={"Authorization": f"Bearer {HF_API_KEY}"},
            json={"inputs": prompt}
        )
        return response.content if response.status_code == 200 else None

    def train_panda(self, message):
        bot.send_photo(message.chat.id, open('./vanna.webp', 'rb'))
