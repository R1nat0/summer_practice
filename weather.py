import requests
import telebot
from yandex_speech import TTS

bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'

yandex_token = 'YOUR_YANDEX_CLOUD_FUNCTIONS_TOKEN'

bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получаем текст сообщения от пользователя
    user_text = message.text

    # Получаем данные о погоде из API 
    weather_api_key = 'YOUR_WEATHER_API_KEY'
    city = user_text 
    weather_data = get_weather_data(city, weather_api_key)

    if weather_data:
        # Генерируем речь с использованием Yandex SpeechKit
        tts = TTS('Прогноз погоды для {}: {}'.format(city, weather_data), lang='ru_RU')
        tts.generate()

        # Отправляем сгенерированную речь пользователю через Telegram Bot
        audio = tts.save_to_file('weather_audio.ogg')
        bot.send_audio(message.chat.id, audio)

def get_weather_data(city, api_key):
    
    return 'Температура: 25°C, Облачность: Переменная'

if __name__ == '__main__':
    bot.polling()