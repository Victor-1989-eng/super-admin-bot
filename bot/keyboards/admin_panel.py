from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_panel():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Статистика", callback_data="stats")],
        [InlineKeyboardButton(text="🚫 Антиспам", callback_data="antispam")],
        [InlineKeyboardButton(text="👋 Приветствие", callback_data="welcome")],
        [InlineKeyboardButton(text="👮 Модерация", callback_data="moderation")],
        [InlineKeyboardButton(text="📜 Логи", callback_data="logs")],
        [InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")]
    ])
