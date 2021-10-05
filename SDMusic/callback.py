#Ur motherfucker If U Kang And Don't Give Creadits

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from zaidmusic.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **ʜᴇʏ {message.from_user.first_name}** \n
💭 **ɪ'ᴍ[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡꜱ ᴜ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ᴠᴄ ᴄʜᴀᴛꜱ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴢᴀɪᴅ ᴍᴜꜱɪᴄ!
☑️ ꜰɪɴᴅ ᴏᴜᴛ ᴀʟʟ ʙᴏᴛꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ʜᴇʟᴘꜱ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ ᴀɴᴅ /help[.](https://telegra.ph/file/42fa9676f01c6fd0e15bb.jpg)
**
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


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello there, welcome to the help menu Powered by @superior_bots !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☑️ ʙᴀꜱɪᴄ ᴄᴍᴅꜱ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "➡️ ᴀᴅᴠᴀᴄᴇᴅ ᴄᴍᴅꜱ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➡️ ᴀᴅᴍɪɴ ᴄᴍᴅꜱ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "➡️ ꜱᴜᴅᴏ ᴡᴀʟᴇ ᴋ ʟɪᴇ", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➡️ᴏᴡɴᴇʀ ᴄᴍᴅꜱ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➡️ ꜰᴜɴ ᴄᴍᴅꜱ", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 ʙᴀᴄᴋ", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the basic commands</b>

🎧 [ ᴢᴀɪᴅ ɢʀᴘ ᴄᴍᴅꜱ ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode

🎧 [ ᴢᴀɪᴅ ᴄʜᴀɴɴᴇʟꜱ ᴄᴍᴅꜱ ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 z ʙᴀᴄᴋ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴢ ʙᴀᴄᴋ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) **first, add me to your group**.
2.) **then promote me as admin and give all permissions except anonymous admin**.
3.) **add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her**.
4.) **turn on the voice chat first before start to play music**.

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 ᴄʟᴏꜱᴇ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
@cb_admin_check
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ ᴘᴀᴜꜱᴇ", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ ʀᴇꜱᴜᴍᴇ", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ ꜱᴋɪᴘ", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ ᴇɴᴅ", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ ᴀɴᴛɪ ᴄᴍᴅ", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 ɢʀᴘ ᴛᴏᴏʟꜱ", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 ᴄʟᴏꜱᴇ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

💡 **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

❔ **usage:**

1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user

2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user

📝 note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 ʙᴀꜱɪᴄ ᴄᴍᴅꜱ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 ᴀᴅᴠᴀᴄᴇᴅ ᴄᴍᴅꜱ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 ᴀᴅᴍɪɴ ᴄᴍᴅꜱ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 ꜱᴜᴅᴏ ᴄᴍᴅꜱ", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 ᴏᴡɴᴇʀ ᴄᴍᴅꜱ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 ꜰᴜɴ ᴄᴍᴅꜱ", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} ᴢᴀɪᴅ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 ᴢ ʙᴀᴄᴋ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
