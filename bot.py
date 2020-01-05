# -*- coding: utf-8 -*-
import telebot
from telebot import types
import time

# ----------------------------------------------
TOKEN = '960630878:AAHevNPjoDkVZ7ayBeqIE2chIRkoneFbdss'
bot = telebot.TeleBot(TOKEN)
First = 'Матан'
Second = 'Алгебра'
Third = 'Ангем'
Fourth = 'Общ. физика'
Fives = 'Эвм'
# ----------------------------------------------
markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
markup.add(First, Second, Third, Fourth, Fives)
hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    check = False
    if not check:
        bot.send_message(message.chat.id, 'Unnamed MM bot v1.0\n'
                                          'Чтобы узнать функционал бота набери\n /help.\n\n'
                                          'Отзывы, пожелания по работе, баги присылайте на\n'
                                          '@mansur_korigov')
        bot.send_chat_action(message.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        time.sleep(0.5)
        msg = bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=markup)
        bot.register_next_step_handler(msg, answer)
        check = True


def answer(message):
    text = message.text
    if text == 'Матан':
        markup_mathan = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup_mathan.add('Первый семестр', 'Второй семестр', 'Третий семестр', 'Четвертый семестр')
        msg = bot.send_message(message.chat.id, 'Вы выбрали: ' + text + '\n', reply_markup=markup_mathan)
        bot.register_next_step_handler(msg, mathan)


def mathan(message):
    text = message.text
    if text == 'Первый семестр':
        bot.send_message(message.chat.id, 'Вот материал для первого семестра:', reply_markup=hideBoard)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.3)
        doc = open('D://Programms/Zorich1.pdf', 'rb')
        bot.send_document(message.chat.id, doc)
    if text == 'Второй семестр':
        bot.send_message(message.chat.id, 'Вот материал для второго семестра:', reply_markup=hideBoard)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.3)
    if text == 'Третий семестр':
        bot.send_message(message.chat.id, 'Вот материал для третьего семестра:', reply_markup=hideBoard)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.3)
    if text == 'Четвертый семестр':
        bot.send_message(message.chat.id, 'Вот материал для четвертого семестра:', reply_markup=hideBoard)
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.3)
    check = False


bot.polling()
