import asyncio
import logging
import os

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from bot.config import BOT_TOKEN
from bot.handlers import router  # твой главный router

# ================= НАСТРОЙКИ =================

WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = os.getenv("RENDER_EXTERNAL_URL")  # Render сам даёт
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# =============================================

async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)
    logging.info(f"Webhook set: {WEBHOOK_URL}")

async def on_shutdown(bot: Bot):
    await bot.delete_webhook()
    await bot.session.close()
    logging.info("Webhook deleted")

def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # подключаем все хендлеры
    dp.include_router(router)

    # aiohttp app
    app = web.Application()

    # регистрируем webhook handler
    webhook_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_handler.register(app, path=WEBHOOK_PATH)

    # lifecycle
    app.on_startup.append(lambda app: on_startup(bot))
    app.on_shutdown.append(lambda app: on_shutdown(bot))

    setup_application(app, dp, bot=bot)

    # Render PORT
    port = int(os.getenv("PORT", 10000))

    web.run_app(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
