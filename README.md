# Digital Rename Bot

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=𝗪𝗘𝗟𝗖𝗢𝗠+𝗧𝗢+𝗗𝗜𝗚𝗜𝗧𝗔𝗟+𝗥𝗘𝗡𝗔𝗠𝗘+𝗕𝗢𝗧!;𝗖𝗥𝗘𝗔𝗧𝗘𝗗+𝗕𝗬+𝗗𝗜𝗚𝗜𝗧𝗔𝗟+𝗕𝗢𝗧𝗭!;𝗜+𝗔𝗠+𝗣𝗢𝗪𝗘𝗥𝗙𝗨𝗟+𝗧𝗚+𝗥𝗘𝗡𝗔𝗠𝗘+𝗕𝗢𝗧!&color=4169E1)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<p align="center">
  <img src="https://telegra.ph/file/b746aadfe59959eb76f59.jpg" alt="Digital Rename Bot" width="220">
</p>

<p align="center">
  <strong>Fast, reliable Telegram file renaming and metadata bot</strong><br>
  Rename files, customize captions, add thumbnails, edit metadata, and manage uploads from Telegram.
</p>

<p align="center">
  <a href="https://github.com/DigitalBotz/Digital-Rename-Bot/releases/latest"><img src="https://img.shields.io/github/v/release/DigitalBotz/Digital-Rename-Bot?display_name=tag&style=for-the-badge&label=latest%20release" alt="Latest GitHub release"></a>
  <a href="https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/DigitalBotz/Digital-Rename-Bot?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/DigitalBotz/Digital-Rename-Bot/issues"><img src="https://img.shields.io/github/issues/DigitalBotz/Digital-Rename-Bot?style=for-the-badge" alt="Issues"></a>
</p>


## What it does

Digital Rename Bot is a Pyrogram-based Telegram bot for quickly renaming documents, videos, and audio files. It also supports thumbnails, custom captions, prefix/suffix rules, FFmpeg metadata editing, force subscription, premium plans, broadcasts, and admin moderation tools.

### Highlights

- Fast file renaming with document, video, and audio output options.
- 2 GB support by default and larger-file support with a valid premium string session.
- Custom filename prefix and suffix.
- Permanent thumbnails and custom captions with `{filename}`, `{filesize}`, and `{duration}` placeholders.
- FFmpeg metadata editing for title, author, video, audio, and subtitle streams.
- Daily upload limits, premium plans, and a 12-hour free trial.
- Force-subscription, ban/unban, broadcast, logs, and status commands.
- Responsive web status dashboard.
- Throttled Pyrogram progress updates to avoid Telegram flood limits.

## Requirements

- Python **3.11+**
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Telegram `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org)
- MongoDB connection string from [MongoDB Atlas](https://www.mongodb.com/atlas)
- FFmpeg installed on the host (included in the Docker image)
- A Telegram premium user string session for files larger than 2 GB

## Configuration

Set these environment variables before starting the bot:

| Variable | Required | Description |
|---|:---:|---|
| `BOT_TOKEN` | **Yes** | Telegram bot token from BotFather |
| `API_ID` | **Yes** | Telegram application ID |
| `API_HASH` | **Yes** | Telegram application hash |
| `DB_URL` | **Yes** | MongoDB connection URI |
| `DB_NAME` | **No** | MongoDB database name; default: `Digital_Rename_Bot` |
| `ADMIN` | **Yes** | Space-separated admin user IDs; at least one numeric ID is required and the first numeric ID is used for the premium contact button |
| `ADMIN_USERNAME` | **Yes** | Telegram username fallback for the premium contact button, with or without `@` |
| `FORCE_SUB` | **No** | Channel username or channel ID for force subscription |
| `LOG_CHANNEL` | **Yes** | Channel ID for logs; leave empty to disable |
| `STRING_SESSION` | **No** | Premium user session for 2 GB+ file support |
| `RKN_PIC` | **No** | Start-message image URL |
| `PORT` | **No** | Web status port; default: `8080` |

> Never commit tokens, API hashes, database credentials, or string sessions to GitHub.

## Local installation

```bash
git clone https://github.com/DigitalBotz/Digital-Rename-Bot.git
cd Digital-Rename-Bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python bot.py
```

For Docker:

```bash
docker build -t digital-rename-bot .
docker run --env-file .env -p 8080:8080 digital-rename-bot
```

The web dashboard is available at `http://localhost:8080` when the bot is running.

## Botfather Commands
```
start - 𝖈ʜᴇᴄᴋ 𝖎 𝖆ᴍ ʟɪᴠᴇ.
plans - ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ.
myplan - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ʜᴇʀᴇ.
view_thumb - 𝖙ᴏ 𝖘ᴇᴇ 𝖞ᴏᴜʀ 𝖈ᴜ𝖘ᴛᴏᴍ 𝖙ʜᴜᴍʙɴᴀɪʟ !!
del_thumb - 𝖙ᴏ 𝖉ᴇʟᴇᴛᴇ 𝖞ᴏᴜʀ 𝖈ᴜ𝖘ᴛᴏᴍ 𝖙ʜᴜᴍʙɴᴀɪʟ !!
set_caption - Sᴇᴛ A Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ !!
see_caption - Sᴇᴇ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ !!
del_caption - Dᴇʟᴇᴛᴇ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ !!
metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ
set_prefix - Tᴏ Sᴇᴛ Yᴏᴜʀ Pʀᴇғɪx !!
see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
del_prefix - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
set_suffix - Tᴏ Sᴇᴛ Yᴏᴜʀ Sᴜғғɪx !!
see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
del_suffix - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!
restart - ᴛᴏ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴀʟʟ ᴅʙ ᴜsᴇʀs (Aᴅᴍɪɴ Oɴʟʏ)
addpremium - ᴀᴅᴅ ᴘʀᴇᴍɪᴜᴍ (Aᴅᴍɪɴ Oɴʟʏ)
remove_premium - ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ (Aᴅᴍɪɴ Oɴʟʏ)
ban - ban members using command (admin only)
unban - unban members using command (admin only)
banned_users - check bot all ban users using command (admin only)
logs - ᴄʜᴇᴄᴋ ʙᴏᴛ ʟᴏɢs (Aᴅᴍɪɴ Oɴʟʏ)
status - Cʜᴇᴄᴋ Bᴏᴛ Sᴛᴀᴛᴜs (Aᴅᴍɪɴ Oɴʟʏ)
broadcast - Sᴇɴᴅ Mᴇssᴀɢᴇ Tᴏ Aʟʟ Usᴇʀs (Aᴅᴍɪɴ Oɴʟʏ)
```


## Custom caption example

```text
/set_caption 📁 File: {filename}
💾 Size: {filesize}
⏱ Duration: {duration}
```

## Metadata example

```text
--change-title My Title
--change-video-title Video Stream
--change-audio-title Audio Stream
--change-subtitle-title Subtitle Stream
--change-author Digital Botz
```

## Deployment

The project includes deployment files for Docker and common Python hosting platforms. Before deploying, add the required environment variables in the provider's secrets/settings panel. Do not put credentials directly in `README.md`, `render.yaml`, `app.json`, or source files.

<details>
<summary><strong>Render</strong></summary>

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/DigitalBotz/Digital-Rename-Bot)

The repository includes `render.yaml`. Add `BOT_TOKEN`, `API_ID`, `API_HASH`, `DB_URL`, `ADMIN`, and the optional variables in Render environment settings.
</details>

<details>
<summary><strong>Koyeb</strong></summary>

[Deploy this repository on Koyeb](https://app.koyeb.com/deploy?type=git&repository=github.com/DigitalBotz/Digital-Rename-Bot&branch=main&run_command=python%20bot.py&name=digital-rename-bot)

Set the required environment variables and use `python bot.py` as the run command.
</details>

<details>
<summary><strong>Railway</strong></summary>

[Open Railway](https://railway.app/new)

Create a project from this GitHub repository, then add the environment variables from the [Configuration](#configuration) table. The default start command is `python bot.py`.
</details>

<details>
<summary><strong>Heroku-compatible platforms</strong></summary>

[![Deploy to Heroku](https://img.shields.io/badge/Deploy%20to%20Heroku-430098?style=for-the-badge&logo=heroku)](https://heroku.com/deploy?template=https://github.com/DigitalBotz/Digital-Rename-Bot)

The repository includes `app.json`, `Procfile`, and `runtime.txt` for Heroku-compatible deployment.
</details>

> **Deployment note:** Free hosting plans may sleep, limit disk space, or restrict long-running file transfers. For reliable 24/7 operation and large files, use a suitable paid or persistent worker/server.

## Version 3.1.2

- Improved code and final 100% updates.
- Fixed metadata button issues.
- Improved filename sanitization and upload cleanup.
- Fixed premium database method and quota rollback bugs.
- Fixed FFmpeg subprocess handling and metadata fallback.

## Credits and license

This repository is a modified and maintained version of the Digital Rename Bot project. The original copyright and attribution notices are retained in the source files.

### Original project credits

- **Original repository:** [DigitalBotz/Digital-Rename-Bot](https://github.com/DigitalBotz/Digital-Rename-Bot)
- **RknDeveloper:** [GitHub](https://github.com/RknDeveloper) · [Telegram](https://t.me/RknDeveloperr)
- **Digital Botz:** [GitHub](https://github.com/DigitalBotz) · [Telegram](https://t.me/Digital_Botz)
- **Jay Mahakal:** [GitHub](https://github.com/JayMahakal98)
- Special thanks to the contributors and maintainers named in the original source headers.

If you redistribute this repository or a derivative work:

1. Keep the original copyright, attribution, and license notices.
2. Include a copy of the [Apache License 2.0](LICENSE).
3. Clearly mark files that you changed, as required by the license.
4. Do not imply that the original authors endorse your modified version.

This project is provided under the [Apache License 2.0](LICENSE). The license permits modification and redistribution subject to its terms; credits and notices must not be removed.

For bug reports and support, contact [Digital Botz Support](https://t.me/DigitalBotz_Support).

**Last updated:** `04 October 2026, 12:52 PM NPT (UTC+05:45)`  
**Current version:** `3.1.2`
