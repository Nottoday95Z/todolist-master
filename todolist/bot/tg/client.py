import requests

from bot.tg import dc
from bot.tg.dc import GET_UPDATES_RESPONSE_SCHEMA, GetUpdatesResponse


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str) -> str:
        """
        URL для запроса к Telegram боту через токен
        """
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        url = self.get_url('getUpdates')
        response = requests.get(url=url, params={'offset': offset, 'timeout': timeout})
        return GET_UPDATES_RESPONSE_SCHEMA.load(response.json())

    def send_message(self, chat_id: int, text: str) -> dc.SendMessageResponse:
        """
        Получение пользователем сообщений от бота
        """
        url = self.get_url("sendMessage")
        response = requests.get(url, params={"chat_id": chat_id, "text": text})
        print(response.json())
        return dc.SEND_MESSAGE_RESPONSE_SCHEMA.load(response.json())
