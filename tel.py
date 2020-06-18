import telebot
import random


list = ['Говно', 'Очень красивый стикер','Неплохой стикер']

bot = telebot.TeleBot("1227121651:AAEF1kt8dw1rCg86v62v_9YBn8SHVGyC50U")

@bot.message_handler(content_types= ['text']) 
def send_welcome( message): 
	bot.reply_to(message,  "отправь мне стикер")

@bot.message_handler(content_types= ['sticker']) 
def send_welcome( message): 
	random.shuffle(list)
	bot.reply_to(message,  list)

bot.polling()