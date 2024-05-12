# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import (aiohttp, asyncio, warnings, pytz, datetime,
logging, logging.config, glob, sys, importlib, pyromod)
from pathlib import Path
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from plugins.web_support import web_server
from plugins.file_rename import app

# Get logging configurations
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)

class Digital_FileRenameBot(Client):
    def __init__(self):
        super().__init__(
            name="Digital_FileRenameBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15)
        
    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME
        app = aiohttp.web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await aiohttp.web.TCPSite(app, bind_address, Config.PORT).start()
        path = "plugins/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as a:
                patt = Path(a.name)
                plugin_name = patt.stem.replace(".py", "")
                plugins_path = Path(f"plugins/{plugin_name}.py")
                import_path = "plugins.{}".format(plugin_name)
                spec = importlib.util.spec_from_file_location(import_path, plugins_path)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["plugins" + plugin_name] = load
                print("Digital Botz Imported " + plugin_name)
                
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        for id in Config.ADMIN:
            try: await self.send_message(id, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")                                
            except: pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped 🙄")

bot_instance = Digital_FileRenameBot()

def main():
    async def start_services():
        if Config.STRING_SESSION:
            await asyncio.gather(
                app.start(),        # Start the Pyrogram Client
                bot_instance.start()  # Start the bot instance
            )
        else:
            await asyncio.gather(
                bot_instance.start())
            
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())
    loop.run_forever()

if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="There is no current event loop")
    main()
    
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
