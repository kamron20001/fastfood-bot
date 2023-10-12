from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_default_start_keyboard():
    course = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text="Telefon raqamini yuborish📲"),
            ],
            [
                KeyboardButton(text="📍Joylashuvni yuboring")
            ],
            [
                KeyboardButton(text="")
            ]
        ],
        resize_keyboard=True
    )


    return course