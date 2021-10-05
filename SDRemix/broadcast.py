import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from callsmusic.callsmusic import client as veez
from config import SUDO_USERS


@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent = 0
    failed = 0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Waiting Broadcast...`")
        if not message.reply_to_message:
            await wtf.edit("Please Reply to a Message to Start Broadcast!")
            return
        lmao = message.reply_to_message.text
        async for dialog in veez.iter_dialogs():
            try:
                await veez.send_message(dialog.chat.id, lmao)
                sent = sent + 1
                await wtf.edit(
                    f"`Broadcasting...` \n\n**Sent to:** `{sent}` chats \n**Failed in:** {failed} Chats"
                )
                await asyncio.sleep(3)
            except:
                failed = failed + 1
        await message.reply_text(
            f"`Gcast succesfully` \n\n**Sent to:** `{sent}` chats \n**Failed in:** {failed} Chats"
        )
