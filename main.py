import telebot
import config
from pyowm import OWM
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == '/weather':
    bot.send_message(message.from_user.id, "Введите название города")
    bot.register_next_step_handler(message, get_weather)
  else:
    bot.send_message(message.from_user.id, 'Напиши /weather')

def get_weather(message):
  city = message.text
  try:
    w = weather(city)

    bot.send_message(message.from_user.id, f'В городе {city} сейчас {round(w[0]["temp"])} градусов,'
                     f' чувствуется как {round(w[0]["feels_like"])} градусов')
    bot.send_message(message.from_user.id, f' Скорость ветра {w[1]} м/с')
    bot.send_message(message.from_user.id, w[2])
    bot.send_message(message.from_user.id, 'Введите название города')
    bot.register_next_step_handler(message, get_weather)
  except Exception:
    bot.send_message(message.from_user.id, 'Такого города нет в базе попробуйте еще раз')
    bot.send_message(message.from_user.id, 'Введите название города')
    bot.register_next_step_handler(message, get_weather)

def get_location(lat, lon):
    url = f"https://yandex.ru/pogoda/maps.nowcat?lat={lat}&lon={lon}&via=hnav&le_Lightning=1"
    return url

def weather(city: str):
    owm = OWM('4f6561b0f9634a9e6852942a41ad20df')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    location = get_location(observation.location.lat, observation.location.lon)
    temperature = weather.temperature("celsius")
    wind_speed = weather.wind()['speed']
    return temperature, wind_speed, location

# RUN
bot.polling(none_stop=True)