import telebot
token = '420957925:AAHyL8MRSpvMM8qxJnhF0mL6KbtmsZbvFw4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет! Я буду повторять всё, что ты скажешь.')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)