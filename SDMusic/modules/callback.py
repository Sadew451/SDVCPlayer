from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from SDMusic.helpers.decorators import authorized_users_only
from SDMusic.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from SDMusic.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 **Hey, i'm {query.message.from_user.mention}** \n
 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Allow You to Play Music On Groups Through The New Telegram Voice Chat !**
 Find Out All The Bot's Commands & How They Work By Click On The » Commands Button !**
❓ **For Information About All Feature Of This Bot, Just**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "How to use Me ❓ ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "Commands Help ❔", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "Support Group 👥", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "BOT NEWS 🙋🏼‍♀️", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "Source Code 💾", url="https://github.com/Sadew451/SDVCPlayer"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 Hello there, welcome to the help menu !</b>
**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Fun Commands", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🔥 here is the basic commands</b>
🎧 [ Group Music Commands ]
- `/play` (`song name)` - `play song from youtube`
- `/ytpplay` `(song name)` - `play song directly from youtube` 
- `/playlist` - `show the list song in queue`
- `/song` `(song name)` - `download song from youtube`
- `/search` `(video name)` - `search video from youtube detailed`
- `/video` `(video name)` - `download video from youtube detailed`
- `/lyrics` - `(song name)` `lyrics scrapper`
🎧 [ Channel Music Commands ]
- `/cplay` - `stream music on channel voice chat`
- `/cplayer` - `show the song in streaming`
- `/cpause` - `pause the streaming music`
- `/cresume` - `resume the streaming was paused`
- `/cskip` - `skip streaming to the next song`
- `/cend` - `end the streaming music`
- `/admincache` - `refresh the admin cache`
- `/userbotjoin`: Invite @{ASSISTANT_NAME} Userbot to your chat
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🔥 Here is the Advanced Commands</b>
`/start` `(in group)` - `see the bot alive status`
`/reload` - `reload bot and refresh the admin list`
`/admincache` - `refresh the admin cache`
`/ping` - `check the bot ping status`
`/uptime` - `check the bot uptime status`
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🔥 Here is the Admin Commands</b>
`/player` - `show the music playing status`
`/pause` - `pause the music streaming`
`/resume` - `resume the music was paused`
`/skip` - `skip to the next song`
`/end` - `stop music streaming`
`/userbotjoin` - `invite assistant join to your group`
`/auth` - `authorized user for using music bot`
`/deauth` - `unauthorized for using music bot`
`/control` - `open the player settings panel`
`/delcmd` `(on | off)` - `enable / disable del cmd feature`
`/musicplayer` `(on / off)` - `disable / enable music player in your group`
`/b` `and` `/tb` `(ban / temporary ban)` - `banned permanently or temporarily banned user in group`
`/ub` - `to unbanned user you're banned from group`
`/m` `and` `/tm` `(mute / temporary mute)` - `mute permanently or temporarily muted user in group`
`/um` - `to unmute user you're muted in group`
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🔥 Here is the Sudo Commands</b>
`/userbotleaveall` - `order the assistant to leave from all group`
`/gcast` - `send a broadcast message trought the assistant`
`/stats` - `show the bot statistic`
`/rmd` - `remove all downloaded files`
`/clean` - `Remove all raw files`
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🔥 Here is the Owner Commands</b>
`/stats` - `show the bot statistic`
`/broadcast` - `send a broadcast message from bot`
`/block` `(user id - duration - reason)` - `block user for using your bot`
`/unblock` `(user id - reason)` - `unblock user you blocked for using your bot`
`/blocklist` - `show you the list of user was blocked for using your bot`
📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🔥 Here is the Fun Commands</b>
`/chika` - `check it by yourself`
`/wibu` - `check it by yourself`
`/asupan` - `check it by yourself`
`/truth` - `check it by yourself`
`/dare` - `check it by yourself`
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""How To Use 🤔:
1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "All Commads", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**🔥 Here is the Control Menu Of Bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Anti Commands", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Group Tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Close ❌", callback_data="close"
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
        f"""<b>🔥 This is the Feature Information :</b>
🔥 **Feature:** This Feature Contains Functions That Can, Mute, Unban, Unmute Users in Your Group.
And You Can Also Set A Time For the Ban And Mute Penalties For Members in Yur Goup So They Can Released Pnishment With The Secified Time.
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
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbback"
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
        f"""<b>This is The Feature Information :</b>
        
**🔥 Feature:** Delete Every Commands Sent By Users to Avoid Spam in Groups !
❔ usage:**
 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 Hello there, Welcome to the Help Menu !</b>
**in This Menu You Can Open Several Available Command Menus, in Each Command Menu There is Also A Brief Explanation Of Each Command**
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Fun Commands", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🤔 How To Use Me 🤔:
1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
