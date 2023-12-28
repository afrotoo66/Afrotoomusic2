import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["مصنع","المصنع","مصنع فيجا"])
    & filters.group
    
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""[⭑ٖٖ𝚆ٰٖ𝙴ٰٖ𝙻ٰٖ𝙲ٰٰ𝙾ٰٖ𝙼ٰٖ𝙴ٰٖٖ ٰٖ𝚃ٰٖ𝙾ٰٖٓᯓ 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌♬⁩♪ٰ ٰٖ𝚂ٰٖ𝙴ٰٖ𝙲ٰٖ𝚃ٰٖ𝙸ٰٖ𝙾ٰٖ𝙽ٰٖ𝚂ٰٖٖ](https://t.me/T_Y_E_X) 

★ هاا هالو عزيزي : \n│ \n└ʙʏ: {message.from_user.mention()}**
★ اختار ما تشاء من أقسام فيحا المختلفه
★ من مصانع..عفرتو مختلفه..و بمميزاتها""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹𝚂𝙾𝚄𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌♬⁩", url=f"https://t.me/T_Y_E_X"),
                   ],
                   [
                    InlineKeyboardButton(
                       "⋆ٰ𝗠ٰ𝐔᚜𝐕𝐄ٰ𝐆ٰ𝐀᚛𝗦ٰ𝐈ٰ𝐂ٰٖ", url=f"https://t.me/Gyyihubot"),
                   InlineKeyboardButton(
                        "⋆ٰ𝐌𝐊.𝐓𝐞𝐥𝐞𝐡𝐨𝐧", url=f"https://t.me/VG_TEllE_BOT"),
                   ],
                   [     
                    InlineKeyboardButton(
                        "⋆ٰ 𝐒𝐓𝐎𝐑𝐄ٖ", url=f"https://t.me/MK1_VEGA_bt"),    
                   InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
        ),
    )