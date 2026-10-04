# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To (https://github.com/JayMahakal98) & @ReshamOwner
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

# extra imports
import math, time, re, datetime, pytz, os, asyncio
from config import Config, rkn 

# pyrogram imports
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

_progress_last_update = {}
_progress_locks = {}
_progress_samples = {}
_PROGRESS_UPDATE_INTERVAL = 3.0


async def progress_for_pyrogram(current, total, ud_type, message, start):
    """Update a Telegram progress message without flooding Telegram.

    Pyrogram can call this callback many times per second.  The old modulo
    based check could update repeatedly in the same second, divide by zero,
    and create negative/overlong progress bars.  Updates are now throttled
    per message and the final update is always sent.
    """
    now = time.monotonic()
    key = (getattr(message, "chat", None).id if getattr(message, "chat", None) else 0,
           getattr(message, "id", id(message)))
    current = max(0, int(current or 0))
    total = max(0, int(total or 0))
    is_complete = total > 0 and current >= total

    lock = _progress_locks.setdefault(key, asyncio.Lock())
    async with lock:
        previous = _progress_samples.get(key)
        _progress_samples[key] = (current, now)
        last_update = _progress_last_update.get(key, 0.0)
        if not is_complete and now - last_update < _PROGRESS_UPDATE_INTERVAL:
            return
        _progress_last_update[key] = now

        try:
            if previous:
                previous_current, previous_time = previous
                speed = max(0, current - previous_current) / max(now - previous_time, 0.001)
            else:
                # Call sites pass time.time(), so use the same clock here.
                elapsed = max(time.time() - float(start or time.time()), 0.001)
                speed = current / elapsed
            percentage = min(100.0, (current * 100.0 / total)) if total else 0.0
            filled = min(20, max(0, int(percentage / 5)))
            progress = "▣" * filled + "▢" * (20 - filled)
            remaining = max(0, total - current)
            eta = TimeFormatter(milliseconds=(remaining / speed) * 1000) if speed else "0 s"
            tmp = progress + rkn.RKN_PROGRESS.format(
                round(percentage, 2),
                humanbytes(current),
                humanbytes(total),
                humanbytes(speed),
                eta or "0 s",
            )
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="close")
                ]]),
            )
        except Exception:
            # Telegram may return MessageNotModified/FloodWait while a file
            # transfer is finishing; never break the actual transfer for UI.
            pass
        finally:
            if is_complete:
                _progress_last_update.pop(key, None)
                _progress_samples.pop(key, None)
                _progress_locks.pop(key, None)

def humanbytes(size):    
    if size is None:
        return "0 B"
    if size == 0:
        return "0 B"
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size >= power and n < len(Dic_powerN) - 1:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'ʙ'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "ᴅ, ") if days else "") + \
        ((str(hours) + "ʜ, ") if hours else "") + \
        ((str(minutes) + "ᴍ, ") if minutes else "") + \
        ((str(seconds) + "ꜱ, ") if seconds else "") + \
        ((str(milliseconds) + "ᴍꜱ, ") if milliseconds else "")
    return tmp[:-2] 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

async def send_log(b, u):
    if Config.LOG_CHANNEL:
        curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        log_message = (
            "**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\n"
            f"Uꜱᴇʀ: {u.mention}\n"
            f"Iᴅ: `{u.id}`\n"
            f"Uɴ: @{u.username}\n\n"
            f"Dᴀᴛᴇ: {curr.strftime('%d %B, %Y')}\n"
            f"Tɪᴍᴇ: {curr.strftime('%I:%M:%S %p')}\n\n"
            f"By: {b.mention}"
        )
        await b.send_message(Config.LOG_CHANNEL, log_message)

async def get_seconds_first(time_string):
    conversion_factors = {
        's': 1,
        'min': 60,
        'hour': 3600,
        'day': 86400,
        'month': 86400 * 30,
        'year': 86400 * 365
    }

    parts = time_string.split()
    total_seconds = 0

    for i in range(0, len(parts), 2):
        value = int(parts[i])
        unit = parts[i+1].lower().rstrip('s')
        total_seconds += value * conversion_factors.get(unit, 0)

    return total_seconds

async def get_seconds(time_string):
    conversion_factors = {
        's': 1,
        'min': 60,
        'hour': 3600,
        'day': 86400,
        'month': 86400 * 30,
        'year': 86400 * 365
    }

    total_seconds = 0
    pattern = r'(\d+)\s*(seconds?|mins?|minutes?|hours?|days?|months?|years?)\b'
    matches = re.findall(pattern, time_string)

    for value, unit in matches:
        unit = unit.lower()
        unit = {'second': 's', 'seconds': 's', 'minute': 'min', 'minutes': 'min',
                'mins': 'min', 'hour': 'hour', 'hours': 'hour', 'day': 'day',
                'days': 'day', 'month': 'month', 'months': 'month',
                'year': 'year', 'years': 'year'}.get(unit, unit)
        total_seconds += int(value) * conversion_factors.get(unit, 0)

    return total_seconds

async def add_prefix_suffix(input_string, prefix='', suffix=''):
    input_string = os.path.basename(str(input_string)).strip()
    prefix = str(prefix or '').strip()
    suffix = str(suffix or '').strip()
    pattern = r'(?P<filename>.*?)(\.\w+)?$'
    match = re.search(pattern, input_string)
    
    if match:
        filename = match.group('filename')
        extension = match.group(2) or ''
        
        prefix_str = f"{prefix} " if prefix else ""
        suffix_str = f" {suffix}" if suffix else ""
        
        return f"{prefix_str}{filename}{suffix_str}{extension}"
    else:
        return input_string

async def remove_path(*paths):
    for path in paths:
        if path and os.path.lexists(path):
            os.remove(path)

async def metadata_text(metadata_text):
    author = None
    title = None
    video_title = None
    audio_title = None
    subtitle_title = None

    flags = [i.strip() for i in metadata_text.split('--')]
    for f in flags:
        if "change-author" in f:
            author = f[len("change-author"):].strip()
        if "change-title" in f:
            title = f[len("change-title"):].strip()
        if "change-video-title" in f:
            video_title = f[len("change-video-title"):].strip()
        if "change-audio-title" in f:
            audio_title = f[len("change-audio-title"):].strip()
        if "change-subtitle-title" in f:
            subtitle_title = f[len("change-subtitle-title"):].strip()

    return author, title, video_title, audio_title, subtitle_title

# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
