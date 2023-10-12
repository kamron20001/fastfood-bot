from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_keyboards():
    start_keyboards = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("🍴 Menyu"),
                KeyboardButton("📃 Mening buyrtmalrim")
            ],
            [
                KeyboardButton("📥 Savat"),
                KeyboardButton("🗳 Xabar yuborish"),
                KeyboardButton("📞 Aloqa"),
                KeyboardButton("⚙️ Sozlamalar")
            ]
        ]
    )