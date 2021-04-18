from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, darkversion
from pathlib import Path
import asyncio
import telethon.utils


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""𝙳𝙰𝚁𝙺 𝙱𝙾𝚃 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴 𝙽𝙾𝚆!!! 𝙳𝙰𝚁𝙺𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :- **1.0** 𝚈𝙾𝚄𝚁 𝔻𝔸ℝ𝕂𝔹𝕆𝕋 𝙸𝚂 𝙽𝙾𝚆 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝚄𝚂𝙴! 𝙵𝙾𝚁 𝙲𝙷𝙴𝙲𝙺 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙾𝚁 𝙽𝙾𝚃 𝙿𝙻𝙴𝙰𝚂𝙴 𝚃𝚈𝙿𝙴 (.alive/.ping) 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙴𝙽𝙹𝙾𝚈 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃! 𝙹𝙾𝙸𝙽 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙵𝚄𝚃𝚄𝚁𝙴𝙳 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 @Dark_bot_updates .""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
