from utils.utils import Utils
import logging
from aiogram import Bot, Dispatcher
from settings.config import USER_UUID


class BotHelper:
    def __init__(self) -> None:
        self.bot = None
        self.dp = None

    def run(self):
        logging.basicConfig(level=logging.INFO)
        # Объект бота
        self.bot = Bot(token=Utils().get_tg_bot_token(USER_UUID))
        # Диспетчер
        self.dp = Dispatcher()

    def get_dp(self):
        if self.dp is None:
            raise Exception("Dispatcher is not initialized")
        return self.dp

    def get_bot(self):
        if self.bot is None:
            raise Exception("Bot is not initialized")
        return self.bot


bot = BotHelper()
