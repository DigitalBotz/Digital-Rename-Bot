# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔

import aiohttp, asyncio, warnings, pytz, datetime
import logging
import glob, sys
import importlib.util
from pathlib import Path

from pyrogram import Client, __version__, errors, idle
from pyrogram.raw.all import layer

from config import Config
from plugins.web_support import web_server
from plugins.file_rename import app

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler('BotLog.txt'), logging.StreamHandler()]
)
logging.getLogger("pyrofork").setLevel(logging.WARNING)


class DigitalRenameBot(Client):
    def __init__(self):
        super().__init__(
            name="DigitalRenameBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,

            # 🔥🔥🔥 LOCAL BOT API (MAIN FIX)
            base_url=Config.BOT_API_URL,

            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=5,
            max_concurrent_transmissions=50
        )

    async def start(self):
        await super().start()
        me = await self.get_me()

        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME
        self.premium = Config.PREMIUM_MODE
        self.uploadlimit = Config.UPLOAD_LIMIT_MODE
        Config.BOT = self

        runner = aiohttp.web.AppRunner(await web_server())
        await runner.setup()
        await aiohttp.web.TCPSite(runner, "0.0.0.0", Config.PORT).start()

        for file in glob.glob("plugins/*.py"):
            plugin_name = Path(file).stem
            spec = importlib.util.spec_from_file_location(
                f"plugins.{plugin_name}", file
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.modules[f"plugins.{plugin_name}"] = module
            print(f"Loaded Plugin: {plugin_name}")

        print(f"{me.first_name} Bot Started Successfully ✅")

        for admin in Config.ADMIN:
            try:
                if Config.STRING_SESSION:
                    await self.send_message(
                        admin,
                        "✅ Local Bot API + STRING_SESSION ENABLED\n"
                        "🚀 2GB+ / 4GB+ file support ACTIVE"
                    )
                else:
                    await self.send_message(
                        admin,
                        "✅ Local Bot API ENABLED\n"
                        "🚀 2GB+ file support ACTIVE"
                    )
            except:
                pass

        if Config.LOG_CHANNEL:
            try:
                now = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"🤖 {me.mention} Restarted\n"
                    f"📅 {now.strftime('%d %B %Y')}\n"
                    f"⏰ {now.strftime('%I:%M:%S %p')}\n"
                    f"🧩 Pyrogram v{__version__} (Layer {layer})"
                )
            except:
                pass

    async def stop(self, *args):
        for admin in Config.ADMIN:
            try:
                await self.send_message(admin, "🛑 Bot Stopped")
            except:
                pass
        await super().stop()


digital_instance = DigitalRenameBot()


def main():
    async def runner():
        if Config.STRING_SESSION:
            await asyncio.gather(app.start(), digital_instance.start())
        else:
            await digital_instance.start()

        await idle()

        if Config.STRING_SESSION:
            await asyncio.gather(app.stop(), digital_instance.stop())
        else:
            await digital_instance.stop()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner())


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    try:
        main()
    except errors.FloodWait as e:
        asyncio.run(asyncio.sleep(e.value))
        main()
