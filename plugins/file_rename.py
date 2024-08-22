# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support

from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.utils import progress_for_pyrogram, convert, humanbytes, add_prefix_suffix
from helper.database import digital_botz
from asyncio import sleep
from PIL import Image
import os, time, asyncio
from config import Config

UPLOAD_TEXT = """ᴜᴩʟᴏᴀᴅ sᴛᴀʀᴛᴇᴅ...."""
app = Client("4gb_FileRenameBot", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.STRING_SESSION)
   
@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    user_id  = message.from_user.id
    if await digital_botz.has_premium_access(user_id):
        rkn_file = getattr(message, message.media.value)
        filename = rkn_file.file_name
        filesize=humanbytes(rkn_file.file_size)
        mime_type = rkn_file.mime_type
        dcid = FileId.decode(rkn_file.file_id).dc_id
        extension_type = mime_type.split('/')[0]
        if not Config.STRING_SESSION:
            if rkn_file.file_size > 2000 * 1024 * 1024:
                 return await message.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ+")

        try:
            await message.reply_text(
            text=f"**__ᴍᴇᴅɪᴀ ɪɴꜰᴏ\n\n◈ ᴏʟᴅ ꜰɪʟᴇ ɴᴀᴍᴇ: `{filename}`\n\n◈ ᴇxᴛᴇɴꜱɪᴏɴ: `{extension_type.upper()}`\n◈ ꜰɪʟᴇ ꜱɪᴢᴇ: `{filesize}`\n◈ ᴍɪᴍᴇ ᴛʏᴇᴩ: `{mime_type}`\n◈ ᴅᴄ ɪᴅ: `{dcid}`\n\nᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴇᴡ ғɪʟᴇɴᴀᴍᴇ ᴡɪᴛʜ ᴇxᴛᴇɴsɪᴏɴ ᴀɴᴅ ʀᴇᴘʟʏ ᴛʜɪs ᴍᴇssᴀɢᴇ....__**",
	    reply_to_message_id=message.id,  
	    reply_markup=ForceReply(True)
        )       
            await sleep(30)
        except FloodWait as e:
            await sleep(e.value)
            await message.reply_text(
            text=f"**__ᴍᴇᴅɪᴀ ɪɴꜰᴏ\n\n◈ ᴏʟᴅ ꜰɪʟᴇ ɴᴀᴍᴇ: `{filename}`\n\n◈ ᴇxᴛᴇɴꜱɪᴏɴ: `{extension_type.upper()}`\n◈ ꜰɪʟᴇ ꜱɪᴢᴇ: `{filesize}`\n◈ ᴍɪᴍᴇ ᴛʏᴇᴩ: `{mime_type}`\n◈ ᴅᴄ ɪᴅ: `{dcid}`\n\nᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴇᴡ ғɪʟᴇɴᴀᴍᴇ ᴡɪᴛʜ ᴇxᴛᴇɴsɪᴏɴ ᴀɴᴅ ʀᴇᴘʟʏ ᴛʜɪs ᴍᴇssᴀɢᴇ....__**",
	    reply_to_message_id=message.id,  
	    reply_markup=ForceReply(True)
        )
        except:
            pass
    else:
        btn = [
            [InlineKeyboardButton("⚠️ ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ ⚠️", callback_data="close")]
        ]
        reply_markup = InlineKeyboardMarkup(btn)
        m=await message.reply_sticker("CAACAgIAAxkBAAIBTGVjQbHuhOiboQsDm35brLGyLQ28AAJ-GgACglXYSXgCrotQHjibHgQ")         
        await message.reply_text(f"**😢 You Don't Have Any Premium Subscription.\n\n Check Out Our Premium /plan**",reply_markup=reply_markup)
        await sleep(20)
        await m.delete()

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text 
        await message.delete() 
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton("📁 Dᴏᴄᴜᴍᴇɴᴛ",callback_data = "upload_document")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("🎥 Vɪᴅᴇᴏ", callback_data = "upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎵 Aᴜᴅɪᴏ", callback_data = "upload_audio")])
        await message.reply(
            text=f"**Sᴇʟᴇᴄᴛ Tʜᴇ Oᴜᴛᴩᴜᴛ Fɪʟᴇ Tyᴩᴇ**\n**• Fɪʟᴇ Nᴀᴍᴇ :-**`{new_name}`",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )



@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):
    # Creating Directory for Metadata
    if not os.path.isdir("Metadata"):
        os.mkdir("Metadata")

    user_id = int(update.message.chat.id) 
    new_name = update.message.text
    new_filename_ = new_name.split(":-")[1]
    try:
        # adding prefix and suffix
        prefix = await digital_botz.get_prefix(user_id)
        suffix = await digital_botz.get_suffix(user_id)
        new_filename = add_prefix_suffix(new_filename_, prefix, suffix)
    except Exception as e:
        return await update.message.edit(f"⚠️ Something went wrong can't able to set Prefix or Suffix ☹️ \n\n❄️ Contact My Creator -> @RknDeveloperr\nError: {e}")

    # msg file location 
    file = update.message.reply_to_message

    # file downloaded path
    file_path = f"Renames/{new_filename}"
    
    # metadata downloaded path
    metadata_path = f"Metadata/{new_filename}"
	
    ms = await update.message.edit("`Try To Download....`")    
    try:
        dl_path = await bot.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram, progress_args=("ᴅᴏᴡɴʟᴏᴀᴅ sᴛᴀʀᴛᴇᴅ....", ms, time.time()))                    
    except Exception as e:
     	return await ms.edit(e)

    metadata_mode = await digital_botz.get_metadata_mode(user_id)
    if (metadata_mode):
        metadata = await digital_botz.get_metadata_code(user_id)
        if metadata:
            await ms.edit("I Fᴏᴜɴᴅ Yᴏᴜʀ Mᴇᴛᴀᴅᴀᴛᴀ\n\n__**Pʟᴇᴀsᴇ Wᴀɪᴛ...**__\n**Aᴅᴅɪɴɢ Mᴇᴛᴀᴅᴀᴛᴀ Tᴏ Fɪʟᴇ....**")
            cmd = f"""ffmpeg -i {dl_path} {metadata} {metadata_path}"""
	    
            process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await process.communicate()
            er = stderr.decode()
            try:
                if er:
                    return await ms.edit(str(er) + "\n\n**Error**")
            except BaseException:
                pass
        await ms.edit("**Metadata added to the file successfully ✅**\n\n**Tʀyɪɴɢ Tᴏ Uᴩʟᴏᴀᴅɪɴɢ....**")
    else:
        await ms.edit("`Tʀʏɪɴɢ Tᴏ Uᴩʟᴏᴀᴅɪɴɢ....`")
	    
    duration = 0
    try:
        parser = createParser(file_path)
        metadata = extractMetadata(parser)
        if metadata.has("duration"):
            duration = metadata.get('duration').seconds
        parser.close()
    except:
        pass
	    
    ph_path = None
    media = getattr(file, file.media.value)
    c_caption = await digital_botz.get_caption(user_id)
    c_thumb = await digital_botz.get_thumbnail(user_id)

    if c_caption:
         try:
             # adding custom caption 
             caption = c_caption.format(filename=new_filename, filesize=humanbytes(media.file_size), duration=convert(duration))
         except Exception as e:
             return await ms.edit(text=f"Yᴏᴜʀ Cᴀᴩᴛɪᴏɴ Eʀʀᴏʀ Exᴄᴇᴩᴛ Kᴇyᴡᴏʀᴅ Aʀɢᴜᴍᴇɴᴛ ●> ({e})")             
    else:
         caption = f"**{new_filename}**"
 
    if (media.thumbs or c_thumb):
         # downloading thumbnail path
         if c_thumb:
             ph_path = await bot.download_media(c_thumb) 
         else:
             ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")

    type = update.data.split("_")[1]
    if media.file_size > 2000 * 1024 * 1024:
        try:
            if type == "document":
                filw = await app.send_document(
                    Config.LOG_CHANNEL,
                    document=metadata_path if metadata_mode else file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                await bot.delete_messages(from_chat, mg_id)
            elif type == "video":
                filw = await app.send_video(
                    Config.LOG_CHANNEL,
                    video=metadata_path if metadata_mode else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                await bot.delete_messages(from_chat, mg_id)
            elif type == "audio":
                filw = await app.send_audio(
                    Config.LOG_CHANNEL,
                    audio=metadata_path if metadata_mode else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                await bot.delete_messages(from_chat, mg_id)
        except Exception as e:
            if file_path:
                os.remove(file_path)
            if ph_path:
                os.remove(ph_path)
            if metadata_path:
                os.remove(metadata_path)
            if dl_path:
                os.remove(dl_path)
            return await ms.edit(f" Eʀʀᴏʀ {e}")
    else:
        try:
            if type == "document":
                await bot.send_document(
                    update.message.chat.id,
                    document=metadata_path if metadata_mode else file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))
            elif type == "video":
                await bot.send_video(
                    update.message.chat.id,
                    video=metadata_path if metadata_mode else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))
            elif type == "audio":
                await bot.send_audio(
                    update.message.chat.id,
                    audio=metadata_path if metadata_mode else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))
        except Exception as e:
            if file_path:
                os.remove(file_path)
            if ph_path:
                os.remove(ph_path)
            if metadata_path:
                os.remove(metadata_path)
            if dl_path:
                os.remove(dl_path)
            return await ms.edit(f" Eʀʀᴏʀ {e}")

# some new feature adding soon ( sample screenshot & sample video )
# please give fork & star and share with your friends repo
# please don't sell the repo ( it's free 🥰)
# please give 200 Fork & 200 star target 🎯 
# fast guys now support again started 
	
    await ms.delete()
    if ph_path:
        os.remove(ph_path)
    if file_path:
        os.remove(file_path)
    if metadata_path:
        os.remove(metadata_path)
    
#@RknDeveloper
#✅ Team-RknDeveloper
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
