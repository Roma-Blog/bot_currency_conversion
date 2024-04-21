import requests

class CustomException(Exception):

    def __init__(self, chat_id: int, message: str):
        self.chat_id = chat_id
        self.message = message

    def __str__(self):
        return self.message


class CurrencyConverter:

    __сurrency_list = {
        'рубль': 'RUB',
        'доллар': 'USD',
        'евро': 'EUR',
    }

    def __init__(self, url: str, chat_id: int):
        self.__url = url
        self.__chat_id = chat_id

    @staticmethod
    def __get_exchange_rate(url: str, currencies: str, base_currency: str):
        data_json = requests.get(url + '&currencies=' + currencies + '&base_currency=' + base_currency).json()
        return data_json['data'][currencies]

    @staticmethod
    def __processing_string(str: str, currency_list: dict, id: int):
        list_word = str.split(' ')
        if len(list_word) != 3:
            raise CustomException(id, 'Недопустимое количество параметров. Нужно ввести 3 параметра: имя валюты, имя валюты, количество. В единственном числе.')
        
        # currencies / base_currency / count
        try:
            return currency_list[list_word[0]], currency_list[list_word[1]], int(list_word[2])
        except KeyError:
            raise CustomException(id, 'Недопустимое имя валюты. Нужно ввести рубль, доллар или евро в единственном числе.')

    def currency_conversion(self, str: str):
        currencies, base_currency, count = self.__processing_string(str, self.__сurrency_list, self.__chat_id)
        return self.__get_exchange_rate(self.__url, currencies, base_currency) * count