import requests
from pyrogram import Client as Bot

from callsmusic import run
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="SDRemixBot"),
)

print("[INFO]: SDREMIX STARTED!")

bot.start()
run()
