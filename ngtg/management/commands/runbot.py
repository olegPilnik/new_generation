from django.core.management.base import BaseCommand
import asyncio # если бот будет асинхронный
from ngtg.tgbot import bot


# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'command run bot'

    def handle(self, *args, **kwargs):
        asyncio.run(bot.polling())

