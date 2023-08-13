"""
Apache License 2.0
Copyright (c) 2022 @RknDeveloper

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

Telegram Link : https://t.me/RknDeveloper 
Repo Link : https://github.com/RknDeveloper/Rkn-rename-bot-V3
License Link : https://github.com/RknDeveloper/Rkn-rename-bot-V3/blob/main/LICENSE
"""

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻 Dᴇᴠꜱ 👨‍💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀ𝚃ᴇꜱ 📯', url='https://t.me/RknDeveloper'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀ𝚃 👯‍♂', url='https://t.me/RknDeveloperSupport')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴏυᴛ 🎛️', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ 🩸', callback_data='help')
        ],[
        InlineKeyboardButton('🎬 𝙼𝙾𝚅𝙸𝙴 𝚂𝙴𝙰𝚁𝙲𝙷 𝙶𝚁𝙾𝚄𝙿 🎬', url='https://t.me/CG_OF_MOVIES_GROUP')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("👨‍💻 Dᴇᴠꜱ 👨‍💻", callback_data='dev')
                ],[
                InlineKeyboardButton('📯 Uᴩᴅᴀ𝚃ᴇꜱ 📯', url='https://t.me/RknDeveloper'),
                InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀ𝚃 👯‍♂', url='https://t.me/RknDeveloperSupport')
                ],[
                InlineKeyboardButton('🎛️ Aʙᴏυᴛ 🎛️', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴩ 🩸', callback_data='help')
                ],[
                InlineKeyboardButton('🎬 𝙼𝙾𝚅𝙸𝙴 𝚂𝙴𝙰𝚁𝙲𝙷 𝙶𝚁𝙾𝚄𝙿 🎬', url='https://t.me/CG_OF_MOVIES_GROUP')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("💞 𝚂ᴏᴜʀᴄᴇ 𝙲ᴏᴅᴇ 💞", url="https://github.com/RknDeveloper/Rkn-rename-bot-V3")
                ],[
                InlineKeyboardButton("❤️‍🔥 𝙰𝙳𝙼𝙸𝙽 ❤️‍🔥", url='https://t.me/RknDeveloperr'),
                InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀ𝚃 👯‍♂', url='https://t.me/RknDeveloperSupport')
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                ],[
                InlineKeyboardButton('🎬 𝙹𝙾𝙸𝙽 𝙼𝙾𝚅𝙸𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🎬', url='https://t.me/CG_OF_MOVIES')
                ],[
                InlineKeyboardButton('🎬 𝙼𝙾𝚅𝙸𝙴 𝚂𝙴𝙰𝚁𝙲𝙷 𝙶𝚁𝙾𝚄𝙿 🎬', url='https://t.me/CG_OF_MOVIES_GROUP')
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("💞 𝚂ᴏᴜʀᴄᴇ 𝙲ᴏᴅᴇ 💞", url="https://github.com/RknDeveloper/Rkn-rename-bot-V3")
                ],[
                InlineKeyboardButton("👨‍🦱 ᴀᴅᴍɪɴ 👨‍🦱", url="https://t.me/RknDeveloperr"),
                InlineKeyboardButton('📯 Uᴩᴅᴀ𝚃ᴇꜱ 📯', url='https://t.me/RknDeveloper')
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                ],[
                InlineKeyboardButton('🎬 𝙹𝙾𝙸𝙽 𝙼𝙾𝚅𝙸𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🎬', url='https://t.me/CG_OF_MOVIES')
            ]])            
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("💞 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 💞", url="https://github.com/RknDeveloper/Rkn-rename-bot-V3")
                ],[
                InlineKeyboardButton("🏹 𝙰𝙳𝙼𝙸𝙽 🏹", url="https://t.me/RknDeveloperr"),
                InlineKeyboardButton('📯 Uᴩᴅᴀ𝚃ᴇꜱ 📯', url='https://t.me/RknDeveloper')
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                ],[
                InlineKeyboardButton('🎬 𝙹𝙾𝙸𝙽 𝙼𝙾𝚅𝙸𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🎬', url='https://t.me/CG_OF_MOVIES')
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()




