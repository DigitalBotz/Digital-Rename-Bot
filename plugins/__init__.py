#  Telegram MTProto API Client Library for Pyrogram
#  Copyright (C) 2017-present DigitalBotz <https://github.com/DigitalBotz>
#  I am a telegram bot, I created it using pyrogram library. https://github.com/pyrogram
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

__name__ = "Digital-Rename-Bot"
__version__ = "3.1.0"
__license__ = " Apache License, Version 2.0"
__copyright__ = "Copyright (C) 2022-present Digital Botz <https://github.com/DigitalBotz>"
__programer__ = "<a href=https://github.com/DigitalBotz/Digital-Rename-Bot>Digital Botz</a>"
__library__ = "<a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>"
__language__ = "<a href=https://www.python.org/>Pyᴛʜᴏɴ 3</a>"
__database__ = "<a href=https://cloud.mongodb.com/>Mᴏɴɢᴏ DB</a>"
__developer__ = "<a href=https://t.me/Digital_Botz>Digital Botz</a>"
__maindeveloper__ = "<a href=https://t.me/RknDeveloper>RknDeveloper</a>"

# main copyright herders (©️)
# I have been working on this repo since 2022


# main working files 
# - bot.py
# - web_support.py
# - plugins/
# - start_&_cb.py
# - Force_Sub.py
# - admin_panel.py
# - file_rename.py
# - metadata.py
# - prefix_&_suffix.py
# - thumb_&_cap.py
# - config.py
# - utils.py
# - database.py

# bot run files
# - bot.py
# - Procfile
# - Dockerfile
# - requirements.txt
# - runtime.txt

from plugins.force_sub import not_subscribed, forces_sub, handle_banned_user_status
from pyrogram import Client, filters

@Client.on_message(filters.private)
async def _(bot, message):
    await handle_banned_user_status(bot, message)
    
@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub_handler(bot, message):
    await forces_sub(bot, message)
