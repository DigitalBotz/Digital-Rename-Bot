# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

# pyrogram imports
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import ListenerTimeout

# extra imports
from helper.database import digital_botz
from config import rkn

TRUE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ', callback_data='metadata_1'),
       InlineKeyboardButton('✅', callback_data='metadata_1')
       ],[
       InlineKeyboardButton('Sᴇᴛ Cᴜsᴛᴏᴍ Mᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]
FALSE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏғғ', callback_data='metadata_0'),
        InlineKeyboardButton('❌', callback_data='metadata_0')
       ],[
       InlineKeyboardButton('Sᴇᴛ Cᴜsᴛᴏᴍ Mᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]


@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    RknDev = await message.reply_text("**Please Wait...**", reply_to_message_id=message.id)
    bool_metadata = await digital_botz.get_metadata_mode(message.from_user.id)
    user_metadata = await digital_botz.get_metadata_code(message.from_user.id)

    await RknDev.edit(
        f"Your Current Metadata:-\n\n➜ `{user_metadata}`",
        reply_markup=InlineKeyboardMarkup(TRUE if bool_metadata else FALSE)
    )


@Client.on_callback_query(filters.regex(r'^(?:metadata_[01]|custom_metadata)$'))
async def query_metadata(bot: Client, query: CallbackQuery):
    data = query.data
    await query.answer()
    if data.startswith('metadata_'):
        _bool = data.split('_')[1]
        user_metadata = await digital_botz.get_metadata_code(query.from_user.id)
        if _bool not in {'0', '1'}:
            return
        bool_meta = _bool == '1'
        await digital_botz.set_metadata_mode(query.from_user.id, bool_meta=not bool_meta)
        await query.message.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}`", reply_markup=InlineKeyboardMarkup(FALSE if bool_meta else TRUE))
           
    elif data == 'custom_metadata':
        await query.message.delete()
        try:
            metadata = await bot.ask(text=rkn.SEND_METADATA, chat_id=query.from_user.id, filters=filters.text, timeout=30, disable_web_page_preview=True)
            RknDev = await query.message.reply_text("**Please Wait...**", reply_to_message_id=metadata.id)
            await digital_botz.set_metadata_code(query.from_user.id, metadata_code=metadata.text)
            await RknDev.edit("**Your Metadata Code Set Successfully ✅**")
        except ListenerTimeout:
            await query.message.reply_text("⚠️ Error!!\n\n**Request timed out.**\nRestart by using /metadata", reply_to_message_id=query.message.id)
        except Exception as e:
            print(e)

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
