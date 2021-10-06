import os
from SDMusic.config import SOURCE_CODE
from SDMusic.config import ASSISTANT_NAME
from SDMusic.config import PROJECT_NAME
from SDMusic.config import SUPPORT_GROUP
from SDMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n I am an Very advanced bot created for playing music in the voice chats of Telegram Groups & Channels.\n\n✅ Send me /help for more info.\n\n 🚀 Join @SDBOTs_Inifinity"
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**

Join @SDBOTs_Inifinity
""",

f"""
**Setting Up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**

1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

Join @SDBOTs_Inifinity
""",
f"""

**Commands**

**=>> Song Playing 🎧**

- `/play`: `Play the requestd song`
- `/play` `[yt url] : Play the given yt url`
- `/play` `[reply yo audio]: Play replied audio`
- `/splay`: `Play song via jio saavn`
- `/ytplay`: `Directly play song via Youtube Music`

**=>> Playback ⏯**

- `/player`: `Open Settings menu of player`
- `/skip`: `Skips the current track`
- `/pause`: `Pause track`
- `/resume`: `Resumes the paused track`
- `/end:` `Stops media playback`
- `/current`: `Shows the current Playing track`
- `/playlist`: `Shows playlist`

*Player Cmd and All Other Cmds Except /play, /current  and /playlist  Are Only For Admins Of The Group.

Join @SDBOTs_Inifinity
""",

f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )
⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)

Join @SDBOTs_Inifinity
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

Join @SDBOTs_Inifinity
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer
**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics

Join @SDBOTs_Inifinity
""",

f"""
**=>> Commands for Sudo Users ⚔️**
 
 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message

*Sudo Users can execute any command in any groups

Join @SDBOTs_Inifinity
"""
      ]
