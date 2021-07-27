import os
impprt telebot

bot=telebot.TeleBot("")

@bot.massege_handler(commands=["start"])
def send_welcome(massege):
  bot.reply_to(massege,"Hello i am ominsda")

bot.polling()