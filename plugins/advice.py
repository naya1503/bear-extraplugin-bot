from pyrogram import filters
from TheApi import api

from config import LOG_GROUP_ID
from KNMusic import app
from SafoneAPI import SafoneAPI


@app.on_message(filters.command("advice"))
async def advice(_, message):
    A = await message.reply_text("...")
    res = api.get_advice()
    await A.edit(res)


@app.on_message(filters.command("astronomical"))
async def advice(_, message):
    a = await SafoneAPI().astronomy()
    if a["success"]:
        c = a["date"]
        url = a["imageUrl"]
        b = a["explanation"]
        caption = f"Tᴏᴅᴀʏ's [{c}] ᴀsᴛʀᴏɴᴏᴍɪᴄᴀʟ ᴇᴠᴇɴᴛ:\n\n{b}"
        await message.reply_photo(url, caption=caption)
    else:
        await message.reply_photo("ᴛʀʏ ᴀғᴛᴇʀ sᴏᴍᴇ ᴛɪᴍᴇ")
        await app.send_message(LOG_GROUP_ID, "/astronomical not working")


__MODULE__ = "Advice"
__HELP__ = """
/advice - Get random advice
/astronomical - To get today's astronomical fact"""
