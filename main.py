from tools import CurrencyConverter, CustomException
import config, telebot

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет тебе узнать курс валюты.')

@bot.message_handler(content_types=['text'])
def dialog(message):

    currency_conversion = CurrencyConverter('https://api.freecurrencyapi.com/v1/latest?apikey=' + config.API_KEY)
    bot.send_message(message.chat.id, currency_conversion.currency_conversion(message.text))

    

try:
    bot.polling(none_stop=True)
except CustomException as e:
    print(e) 

# currency_conversion = CurrencyConverter('https://api.freecurrencyapi.com/v1/latest?apikey=' + config.API_KEY)
# print(currency_conversion.currency_conversion('рубль доллар 100'))