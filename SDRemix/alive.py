from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/8eb4cf7ef38841037bdba.jpg",
        caption=f"""**➮Hey I'm [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
➮ **Music System is Working**
➮ **Music Version : 5.0 Lҽƚҽʂƚ**
➮ **owner : [{OWNER_NAME}](https://t.me/{OWNER_NAME})**
➮ **Service Uptime : `{uptime}`**
**Keep & Support Us**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support ɢʀᴏᴜᴘ 👥", url=f"https://t.me/SDBOTz"
                    ),
                    InlineKeyboardButton(
                        "SDBOTs IniFinity", url=f"https://t.me/SDBOTs_Inifinity"
                    )
                ]
            ]
        )
    )
