from tools import CurrencyConverter, CustomException
import config, telebot

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет тебе узнать курс валюты.')
    bot.send_message(message.chat.id, 'Напиши мне <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>')
    bot.send_message(message.chat.id, 'Например: рубль доллар 100')
    bot.send_message(message.chat.id, 'Доступны валюты: рубль, доллар, евро')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Напиши мне <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>')
    bot.send_message(message.chat.id, 'Например: рубль доллар 100')
    bot.send_message(message.chat.id, 'Доступны валюты: рубль, доллар, евро')

@bot.message_handler(content_types=['text'])
def dialog(message):

    currency_conversion = CurrencyConverter('https://api.freecurrencyapi.com/v1/latest?apikey=' + config.API_KEY, message.chat.id)
    bot.send_message(message.chat.id, currency_conversion.currency_conversion(message.text))


while True:
    try:
        bot.polling(none_stop=True)
    except CustomException as e:
        bot.send_message(e.chat_id, e)