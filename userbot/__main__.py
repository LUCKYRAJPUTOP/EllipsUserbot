from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, ellipsversion
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

print(f"""Ellips π±πΎπ πΈπ π°π»πΈππ΄ π½πΎπ!!! ELLIPSπ±πΎπ ππ΄πππΈπΎπ½ :- **1.0** ππΎππ ELLIPSπΉππ πΈπ π½πΎπ ππ΄π°π³π ππΎ πππ΄! π΅πΎπ π²π·π΄π²πΊ ππΎππ π±πΎπ ππΎππΊπΈπ½πΆ πΎπ π½πΎπ πΏπ»π΄π°ππ΄ πππΏπ΄ (.alive/.ping) π½πΎπ ππΎπ π²π°π½ π΄π½πΉπΎπ ππΎππ π±πΎπ! πΉπΎπΈπ½ π΅πΎπ πΌπΎππ΄ π΅πππππ΄π³ ππΏπ³π°ππ΄π @EllipsSupport .""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
