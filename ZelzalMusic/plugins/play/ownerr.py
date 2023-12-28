import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv
#▒▒▒▒▒▒▒▒▒▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▇▒▒▒▒▒▒▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇
#▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒ ▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▇▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▒▒▆▆▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▜▒▒▇▇▒▒▆▆▆▆▆▆▆▆▆
#▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▇▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▒▒▙▇▇▇▇▇▇▉▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▇
#▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒AFROTOO▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["احمد","عفرتو","مبرمج","مطور السورس","المبرمج"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("IIUll_l")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛\n\n⭐ ¦Afrotoo :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n🎃 ¦𝙸𝙳 :`{usr.id}`\n💌 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛**",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )





@app.on_message(
    command(["مطور", "المطور"])
    & filters.group
  
)
async def kimmyy(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    async for photo in client.iter_profile_photos(OWNER, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛**
                    
🔥 ¦𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
📀 ¦𝚄𝚂𝙴𝚁 :@{OWNER} 
🆔 ¦𝙸𝙳 :`{usr.id}`
 
**ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛** """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")


@app.on_message(command("تحويل لصوره"))
async def elkatifh(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



