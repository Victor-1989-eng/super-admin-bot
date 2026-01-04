from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ChatType

from bot.keyboards.admin_panel import main_panel
from bot.services.permissions import is_admin

router = Router()


@router.message(Command("panel"))
async def open_panel(message: Message, bot):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

    if not await is_admin(bot, message):
        await message.reply("❌ Только для администраторов")
        return

    await message.reply(
        "🎛 Панель администратора",
        reply_markup=main_panel()
    )


@router.callback_query(F.data == "stats")
async def stats_cb(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("📊 Статистика (V1)\n\nВ разработке…", reply_markup=main_panel())


@router.callback_query(F.data == "antispam")
async def antispam_cb(call: CallbackQuery):
    await call.answer("Антиспам переключён (V1)")


@router.callback_query(F.data == "welcome")
async def welcome_cb(call: CallbackQuery):
    await call.answer("Приветствие переключено (V1)")


@router.callback_query(F.data == "moderation")
async def moderation_cb(call: CallbackQuery):
    await call.answer("Модерация (V1)")


@router.callback_query(F.data == "logs")
async def logs_cb(call: CallbackQuery):
    await call.answer("Логи (V1)")


@router.callback_query(F.data == "settings")
async def settings_cb(call: CallbackQuery):
    await call.answer("Настройки (V1)")
