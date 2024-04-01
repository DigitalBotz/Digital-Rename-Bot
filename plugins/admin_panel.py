#(©) @RknDeveloper

from config import Config
from helper.database import db
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import os, sys, time, asyncio, logging, datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
 
@Client.on_message(filters.command(["stats", "status"]) & filters.user(Config.ADMIN))
async def get_stats(bot, message):
    total_users = await db.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - bot.uptime))    
    start_t = time.time()
    rkn = await message.reply('**ᴘʀᴏᴄᴇssɪɴɢ.....**')    
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rkn.edit(text=f"**--Bᴏᴛ Sᴛᴀᴛᴜꜱ--** \n\n**⌚️ Bᴏᴛ Uᴩᴛɪᴍᴇ:** {uptime} \n**🐌 Cᴜʀʀᴇɴᴛ Pɪɴɢ:** `{time_taken_s:.3f} ᴍꜱ` \n**👭 Tᴏᴛᴀʟ Uꜱᴇʀꜱ:** `{total_users}`")

#bot logs process 
@Client.on_message(filters.command('logs') & filters.user(Config.ADMIN))
async def log_file(b, m):
    try:
        await m.reply_document('BotLog.txt')
    except Exception as e:
        await m.reply(str(e))
     
#Restart to cancell all process 
@Client.on_message(filters.private & filters.command("restart") & filters.user(Config.ADMIN))
async def restart_bot(b, m):
    rkn = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)
    failed = 0
    success = 0
    deactivated = 0
    blocked = 0
    start_time = time.time()
    total_users = await db.total_users_count()
    all_users = await db.get_all_users()
    async for user in all_users:
        try:
            restart_msg = f"ʜᴇʏ, {(await b.get_users(user['_id'])).mention}\n\n**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**"
            await b.send_message(user['_id'], restart_msg)
            success += 1
        except InputUserDeactivated:
            deactivated +=1
         #   await db.delete_user(user['_id'])
        except UserIsBlocked:
            blocked +=1
         #   await db.delete_user(user['_id'])
        except Exception as e:
            failed += 1
           # await db.delete_user(user['_id'])
            print(e)
            pass
        try:
            await rkn.edit(f"<u>ʀᴇsᴛᴀʀᴛ ɪɴ ᴩʀᴏɢʀᴇꜱꜱ:</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {total_users}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
        except FloodWait as e:
            await asyncio.sleep(e.value)
    completed_restart = datetime.timedelta(seconds=int(time.time() - start_time))
    await rkn.edit(f"ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʀᴇsᴛᴀʀᴛ: {completed_restart}\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {total_users}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMIN) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    await bot.send_message(Config.LOG_CHANNEL, f"{m.from_user.mention} or {m.from_user.id} Iꜱ ꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ Bʀᴏᴀᴅᴄᴀꜱᴛ......")
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("Bʀᴏᴀᴅᴄᴀꜱᴛ Sᴛᴀʀᴛᴇᴅ..!") 
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await db.total_users_count()
    async for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
           success += 1
        else:
           failed += 1
        if sts == 400:
           await db.delete_user(user['_id'])
        done += 1
        if not done % 20:
           await sts_msg.edit(f"Bʀᴏᴀᴅᴄᴀꜱᴛ Iɴ Pʀᴏɢʀᴇꜱꜱ: \nTᴏᴛᴀʟ Uꜱᴇʀꜱ {total_users} \nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}")
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"Bʀᴏᴀᴅᴄᴀꜱᴛ Cᴏᴍᴩʟᴇᴛᴇᴅ: \nCᴏᴍᴩʟᴇᴛᴇᴅ Iɴ `{completed_in}`.\n\nTᴏᴛᴀʟ Uꜱᴇʀꜱ {total_users}\nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}")
           
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : Bʟᴏᴄᴋᴇᴅ Tʜᴇ Bᴏᴛ")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : Uꜱᴇʀ Iᴅ Iɴᴠᴀʟɪᴅ")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500
 
