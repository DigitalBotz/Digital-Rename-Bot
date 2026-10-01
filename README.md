# Digital Rename Bot

<p align="center">
  <img src="https://telegra.ph/file/b746aadfe59959eb76f59.jpg" alt="Digital Rename Bot" width="220">
</p>

<p align="center">
  <strong>Fast, reliable Telegram file renaming and metadata bot</strong><br>
  Rename files, customize captions, add thumbnails, edit metadata, and manage uploads from Telegram.
</p>

<p align="center">
  <a href="https://github.com/DigitalBotz/Digital-Rename-Bot"><img src="https://img.shields.io/badge/version-3.1.1-5865F2?style=for-the-badge" alt="Version 3.1.1"></a>
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
| `BOT_TOKEN` | Yes | Telegram bot token from BotFather |
| `API_ID` | Yes | Telegram application ID |
| `API_HASH` | Yes | Telegram application hash |
| `DB_URL` | Yes | MongoDB connection URI |
| `DB_NAME` | No | MongoDB database name; default: `Digital_Rename_Bot` |
| `ADMIN` | No | Space-separated admin user IDs |
| `FORCE_SUB` | No | Channel username or channel ID for force subscription |
| `LOG_CHANNEL` | No | Channel ID for logs; leave empty to disable |
| `STRING_SESSION` | No | Premium user session for 2 GB+ file support |
| `RKN_PIC` | No | Start-message image URL |
| `PORT` | No | Web status port; default: `8080` |

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

## Bot commands

### User commands

| Command | Purpose |
|---|---|
| `/start` | Start the bot |
| `/plans` | View premium plans |
| `/myplan` | View current plan and upload usage |
| `/set_caption` | Set a custom output caption |
| `/see_caption` | View the current caption |
| `/del_caption` | Delete the custom caption |
| `/view_thumb` | View the saved thumbnail |
| `/del_thumb` | Delete the saved thumbnail |
| `/metadata` | Enable/disable and configure metadata editing |
| `/set_prefix` | Set a filename prefix |
| `/see_prefix` | View the current prefix |
| `/del_prefix` | Delete the prefix |
| `/set_suffix` | Set a filename suffix |
| `/see_suffix` | View the current suffix |
| `/del_suffix` | Delete the suffix |

### Admin commands

| Command | Purpose |
|---|---|
| `/status` | View bot status and ping |
| `/logs` | Download the bot log file |
| `/broadcast` | Broadcast a replied message to users |
| `/addpremium` | Add a premium plan |
| `/remove_premium` | Remove a premium plan |
| `/ban` | Ban a user for a number of days |
| `/unban` | Remove a user ban |
| `/banned_users` | List banned users |
| `/restart` | Notify users and restart the bot |

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

The project includes deployment files for Docker, Render, Heroku-compatible platforms, and other Python hosting providers. Add all required environment variables in the hosting provider's secrets/settings panel.

- [Deploy on Render](https://render.com/deploy?repo=https://github.com/DigitalBotz/Digital-Rename-Bot)
- [Deploy on Heroku-compatible platforms](https://heroku.com/deploy?template=https://github.com/DigitalBotz/Digital-Rename-Bot)

## Version 3.1.1

- Improved Pyrogram progress updates with throttling and final 100% updates.
- Fixed zero-division, invalid ETA, and concurrent progress issues.
- Improved filename sanitization and upload cleanup.
- Fixed premium database method and quota rollback bugs.
- Fixed FFmpeg subprocess handling and metadata fallback.
- Added safer configuration validation and cleaner startup logs.
- Redesigned the web status dashboard.

## Credits and license

This project is released under the [Apache License 2.0](LICENSE). Please retain the original project credits when modifying or redistributing it.

Special thanks to [RknDeveloper](https://github.com/RknDeveloper), [DigitalBotz](https://github.com/DigitalBotz), and [JayMahakal98](https://github.com/JayMahakal98).

For bug reports and support, contact the [Digital Botz Support](https://t.me/DigitalBotz_Support).

**Last updated:** `01 October 2026, 11:52 PM NPT (UTC+05:45)`  
**Current version:** `3.1.1`
