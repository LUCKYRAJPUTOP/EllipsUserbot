
from userbot import *

from userbot.utils import *

from telethon.events import NewMessage

from telethon.tl.custom import Dialog

from telethon.tl.types import Channel, Chat, User





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Darkbot User"



ludosudo = Config.SUDO_USERS

if ludosudo:



    sudou = "True"



else:

    sudou = "False"

    

dark = bot.uid



PM_IMG = "https://telegra.ph/file/bd05af18c9b4fc5b57233.mp4"



pm_caption = "__**π€γ ΓΞRΜ·α¦ γβBΓTβ Ι¨z ΦΥΌΚΙ¨ΥΌΙπ€**__\n\n"



pm_caption += (

    f"           π€MΝ‘ΝYΝ‘Ν BΝ‘ΝOΝ‘ΝSΝ‘ΝSΝ‘π€\n**γπ₯[{DEFAULTUSER}](tg://user?id={dark})π₯γ**\n\n"

)







pm_caption += f"π₯**γ ΓΞRΜ·α¦ γβBΓTβπ₯  : 1.0** \n\n"



pm_caption += f" ** βοΈππΌππΌπβπβ ππΌβπππβ βοΈ  : 6.9.0 ** \n\n"







pm_caption += "**β­π»πΈππΈπΉπΈππΌ πππΈπππβ­ :- π»πΈππΈπΉπΈππΌ ππβππβπΎ βπβππΈπππ **β\n\nβ"





pm_caption +=  "**β­ββπΈββπΌπβ­    : [α΄α΄ΙͺΙ΄](https://t.me/Dark_bot_support)**\n\n" 







pm_caption += "**β­ββπΌπΈππβ β­: [ Κα΄ΚsΚ Κα΄Κα΄](https://t.me/harsh_78)**\n\n"



pm_caption +=  "[β οΈα΄α΄Κα΄ Κα΄α΄ Κα΄α΄α΄ β οΈ ](https://github.com/Harsh-78/Dark-Userbot)\n "    





@bot.on(admin_cmd(outgoing=True, pattern="alive$"))

async def amireallyalive(alive):

    await alive.get_chat()

    await alive.delete()

    """ For .alive command, check if the bot is running.  """

    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)

    await alive.delete()





    



    
    
