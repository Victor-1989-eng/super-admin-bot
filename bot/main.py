import asyncio
from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.handlers import panel, basic

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(panel.router)
    dp.include_router(basic.router)

    print("🤖 Super Admin Bot запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
