import requests

from bot.tg import dc


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str) -> str:
        """
        URL для запроса к Telegram боту через токен
        """
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> dc.GetUpdatesResponse:
        """
        Получение ботом исходящих сообщений от пользователя
        """
        url = self.get_url("getUpdates")
        response = requests.get(url, params={"offset": offset, "timeout": timeout})
        print(response.json())
        return dc.GET_UPDATES_RESPONSE_SCHEMA.load(response.json())

    def send_message(self, chat_id: int, text: str) -> dc.SendMessageResponse:
        """
        Получение пользователем сообщений от бота
        """
        url = self.get_url("sendMessage")
        response = requests.get(url, params={"chat_id": chat_id, "text": text})
        print(response.json())
        return dc.SEND_MESSAGE_RESPONSE_SCHEMA.load(response.json())
