import requests, config, re

class CurrencyConverter:

    __сurrency_list = {
        'рубль': 'RUB',
        'доллар': 'USD',
        'евро': 'EUR',
    }

    def __init__(self, url: str):
        self.__url = url

    @staticmethod
    def __get_exchange_rate(url: str, currencies: str, base_currency: str):
        data_json = requests.get(url + '&currencies=' + currencies + '&base_currency=' + base_currency).json()
        return data_json['data'][currencies]

    @staticmethod
    def __processing_string(str: str, currency_list: dict):
        list_word = str.split(' ')

        # currencies / base_currency / count
        return currency_list[list_word[0]], currency_list[list_word[1]], int(list_word[2])

    def currency_conversion(self, str: str):
        currencies, base_currency, count = self.__processing_string(str, self.__сurrency_list)
        return self.__get_exchange_rate(self.__url, currencies, base_currency) * count
        

currency_conversion = CurrencyConverter('https://api.freecurrencyapi.com/v1/latest?apikey=' + config.API_KEY)
currency_conversion.currency_conversion('рубль доллар 100')