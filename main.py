import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault

from app.handlers import router

async def set_default_commands(bot: Bot):
    """Функция для установки команд меню. Вызовите её при старте бота."""
    commands = [
        BotCommand(command="start", description="🚀 Начать работу"),
        BotCommand(command="about", description="📋 О нас"),
        BotCommand(command="reglament", description="📄 Получить регламент работы в PDF")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())

async def main():
    bot = Bot(token = '8278309679:AAEeggZzF1gTeGUN7kdNoyavY2eZankkoMw')
    dp = Dispatcher()
    dp.include_router(router)
    await set_default_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print("Бот по поиску мастеров начал работать!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот по поиску мастеров выключен!")