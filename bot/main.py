import asyncio
from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN

# handlers
from bot.handlers import (
    panel,
    basic,
    antispam,
    welcome,
    moderation,
    stats,
)

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    # порядок важен
    dp.include_router(panel.router)
    dp.include_router(stats.router)
    dp.include_router(moderation.router)
    dp.include_router(welcome.router)
    dp.include_router(antispam.router)
    dp.include_router(basic.router)

    print("🤖 Super Admin Assistant Bot запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
