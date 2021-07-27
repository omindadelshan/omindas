import os
impprt telebot

bot=telebot.TeleBot("1867389893:AAEhOoduV-aOecDnJ5mZ-WlMcwu_YfqxA94")

@bot.massege_handler(commands=["start"])
def send_welcome(massege):
  bot.reply_to(massege,"Hello i am ominsda")

bot.polling()
