from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


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


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **ʜᴇʏ {message.from_user.first_name}** \n
💭 **ɪ'ᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡꜱ ᴜ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ᴠᴄ ᴄʜᴀᴛꜱ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴢᴀɪᴅ ᴍᴜꜱɪᴄ!

☑️ ꜰɪɴᴅ ᴏᴜᴛ ᴀʟʟ ʙᴏᴛꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ʜᴇʟᴘꜱ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ ᴀɴᴅ /help** [.](https://telegra.ph/file/42fa9676f01c6fd0e15bb.jpg)

</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        " ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ᴄʜᴀᴛꜱ ☑️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        " ꜱᴇᴛᴜᴘ⚡", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                        "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 💫", url="https://github.com/Itsunknown-12/Zaid-Vc-Player")
                ],[
                    InlineKeyboardButton(
                        "⚡ ᴏꜰꜰɪᴄɪᴀʟ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/SUPERIOR_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ☑️", url=f"https://t.me/SUPERIOR_BOTS")
                ],[
                    InlineKeyboardButton(
                        " ℹ️ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="cbcmds"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **ᴢᴀɪᴅ ɪꜱ ʀᴜɴɴɪɴɢ**\n<b>💠 **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/SUPERIOR_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ ☑️", url=f"https://t.me/SUPERIOR_BOTS"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands powered By Zaid!**

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ ʙᴀꜱɪᴄ ᴄᴍᴅꜱ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        " ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴍᴅꜱ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " ᴀᴅᴍɪɴ ᴄᴍᴅꜱ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        " ꜱᴜᴅᴏ ᴄᴍᴅꜱ", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " ᴏᴡɴᴇʀ ᴄᴍᴅꜱ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " ꜰᴜɴ ᴄᴍᴅꜱ", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴢ ᴘɪɴɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "𝚣 `ᴘᴏɴɢ!!`\n"
        f"🇿  `{delta_ping * 1000:.3f} ᴍꜱ`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 ᴢᴀɪᴅ ꜱᴛᴀᴛᴜꜱ:\n"
        f"• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **ꜱᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )
