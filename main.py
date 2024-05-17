import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from config_data.config import BotSettings
from handlers import start


async def main():
    settings = BotSettings()
    bot = Bot(
        token=settings.bot_token.get_secret_value()
    )
    # Раскомментировать при деплое через Docker хранилище хоста, а локальное, наоборот, - закомментировать
    # storage = RedisStorage.from_url(str(settings.redis_dsn))
    storage = RedisStorage.from_url("redis://localhost:6379")
    dp = Dispatcher(storage=storage)
    dp.include_routers(start.router)

    print("Starting bot")
    await dp.start_polling(bot)
    print("Bot stopped")

asyncio.run(main())
