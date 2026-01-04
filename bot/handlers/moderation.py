from aiogram import Router, F
from aiogram.types import CallbackQuery
from datetime import timedelta

router = Router()


@router.callback_query(F.data.startswith("mute_"))
async def mute(call: CallbackQuery):
    _, minutes, user_id = call.data.split("_")
    until = call.message.date + timedelta(minutes=int(minutes))

    await call.bot.restrict_chat_member(
        call.message.chat.id,
        int(user_id),
        until_date=until,
        permissions={}
    )
    await call.answer("🔇 Пользователь замьючен")


@router.callback_query(F.data.startswith("ban_"))
async def ban(call: CallbackQuery):
    user_id = int(call.data.split("_")[1])
    await call.bot.ban_chat_member(call.message.chat.id, user_id)
    await call.answer("🔨 Пользователь забанен")
