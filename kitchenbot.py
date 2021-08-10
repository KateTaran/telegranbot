import telebot
bot = telebot.TeleBot('1934919773:AAERubaFtRNaym9hCAG259YW7qOwaFVD6AI')
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hi Kate!")
bot.polling()