import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
from transliterate import translit
# Для скачивания библиотек введите в терминал это: pip install requests beautifulsoup4 pyTelegramBotAPI transliterate

bot = telebot.TeleBot('8591232915:AAG4zTRqJHpMANdEdCYu9WCB6vQNCmIYrxs')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Узнать погоду⛅", callback_data="ask_city")
    markup.add(button)
    bot.send_message(message.chat.id, 'Приветствуем вас! Это бот для считывания погоды с открытого источника. '
                                      'Нажмите кнопку "Узнать погоду⛅" для начала', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "ask_city")
def callback_ask_city(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    msg = bot.send_message(call.message.chat.id, 'Введите название города на кириллице (Москва, Новосибирск...):')
    bot.register_next_step_handler(msg, get_weather_data)


def get_weather_data(message):
    city_rus = message.text.strip()
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        city_en = translit(city_rus, 'ru', reversed=True).lower().replace(' ', '-')
        url = f'https://world-weather.ru/pogoda/russia/{city_en}/'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            temp = soup.find('div', id='weather-now-number')
            if temp:
                bot.send_message(message.chat.id, f"Температура в {city_rus.capitalize()}: {temp.text}")
            else:
                bot.send_message(message.chat.id, "Не удалось найти данные о погоде. Возможно, город указан неверно.")
        else:
            bot.send_message(message.chat.id, "Ошибка соединения с сайтом погоды.")

    except:
        bot.send_message(message.chat.id, "Произошла ошибка при получении данных.")


if __name__ == "__main__":
    bot.polling(none_stop=True)