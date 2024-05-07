# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝗕𝗹𝗼𝗼𝗱𝘀 𝗦𝗶𝘁𝗲𝗥𝗶𝗽  : @Bloods_Siterip\n○ 𝗕𝗹𝗼𝗼𝗱𝘀 𝗢𝗻𝗹𝘆𝗳𝗮𝗻𝘀  : @Bloods_Onlyfans\n○ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿  : <a href='tg://user?id={5780372003}'>@Xthesanta</a> </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Close 🏝️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
