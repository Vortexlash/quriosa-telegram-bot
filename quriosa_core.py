import telebot
from telebot import types
import os
import time
import config

bot = telebot.TeleBot(config.token)

# bot.send_message(message.chat.id, "Ping!")

# updates = bot.get_updates()
# print(updates)

# last_update = updates[-1]
# incoming_messages = last_update.message
# print(incoming_messages)

def log(message, answer):
    print("/n")
    from datetime import datetime
    print(datetime.now())
    print("Incoming message from {0} {1}. (id = {2}) \n Message text: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))

@bot.message_handler(commands=['info'])
def bot_info(message):
    answer = "You can control me by using these commands: \n /status — record your current status \n /records — request recent status logs"
    log(message, answer)
    voice=open('voicelines/info.oga', 'rb')
    bot.send_voice(message.chat.id, voice)
    voice.close()
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['status'])
def request_status(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(status) for status in ['In action', 'Curious', 'Playful 📣🐋', 'Inspired', 'Mindful', '🐲', 'Exhausted', 'Depressed', 'Mad 💢']])
    answer = "Let's check your status."
    log(message, answer)
    bot.send_message(message.chat.id, answer, reply_markup = markup)

@bot.message_handler(content_types='text')
def give_advice(message):
    if message.text == "In action":
        answer = "Godspeed, space wanderer."
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Inspired":
        answer = None
        log(message, answer)
        voice=open('voicelines/inspired.oga', 'rb')
        bot.send_voice(message.chat.id, voice)
        voice.close()
    if message.text == "Exhausted":
        answer = "Have you tried meditating?"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Depressed":
        answer = "Please follow the instructions on the link:"
        markup = types.InlineKeyboardMarkup()
        forward_to = types.InlineKeyboardButton(text='You feel like shit.', url='http://philome.la/jace_harr/you-feel-like-shit-an-interactive-self-care-guide/play')
        markup.add(forward_to)
        log(message, answer)
        bot.send_message(message.chat.id, answer, reply_markup = markup)
    elif message.text == "Mad 💢":
        answer = None
        log(message, answer)
        voice=open('voicelines/mad.oga', 'rb')
        bot.send_voice(message.chat.id, voice)
        voice.close()
    else:     
        answer = None
        log(message, answer)
        voice=open('voicelines/interrupt.oga', 'rb')
        bot.send_voice(message.chat.id, voice)
        voice.close()

# @bot.message_handler(commands=['records'])
# def request_logs(message):
#    answer = "Let's see your records."
#    log(message, answer)
#    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)