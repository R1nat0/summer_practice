import requests
import json

def handle_message(event):
    # Получение данных из входящего запроса
    update = json.loads(event['body'])
    message = update['message']
    chat_id = message['chat']['id']
    text = message['text']
    
    # Отправка эхо-ответа
    send_message(chat_id, text)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Ошибка отправки сообщения: {response.text}")

def handler(event, context):
    try:
        handle_message(event)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    return {
        'statusCode': 200
    }