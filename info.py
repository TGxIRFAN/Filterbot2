import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '28643132'))
API_HASH = environ.get('API_HASH', '510c3009ea589830a89e045bf8aae656')
BOT_TOKEN = environ.get('BOT_TOKEN', '5828891683:AAHOVAa8cmzzP2FnJuVXP5qO0sAQKBCFzwk')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS' ,'https://graph.org/file/df17e1fad3d856caf5df8.jpg https://graph.org/file/4db7c2e38f273e3b239dd.jpg https://graph.org/file/e4ead277c0bb7ab445c31.jpg https://graph.org/file/10d81181913c5d4237640.jpg https://graph.org/file/40fef09781fb9ded8cd13.jpg https://graph.org/file/b7b5a32ea575fa7ff50ee.jpg https://graph.org/file/bca1ca2c91828161aa247.jpg https://graph.org/file/bcea1a4ae0176d38a68b7.jpg https://graph.org/file/18a9f945534afa9db5036.jpg https://graph.org/file/89975fb3c157c1ae01e43.jpg https://graph.org/file/c548df4d4a42a8646aa04.jpg')).split()
NOR_IMG = environ.get('NOR_IMG', "https://telegra.ph/file/f179e130b0e96e3fc9757.jpg")
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/b58f576fed14cd645d2cf.jpg")
BOT_START_TIME = time()

# Welcome area
MELCOW_IMG = environ.get('MELCOW_IMG',"https://telegra.ph/file/e54cae941b9b81f13eb71.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"")



# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '683891378 5845960615 2049083114').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001833339939').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://MONGOO:MONGOO@cluster0.rh6p7y3.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "MONGOO:MONGOO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "mongodb+srv://MONGOO:MONGOO@cluster0.rh6p7y3.mongodb.net/?retryWrites=true&w=majority")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", "-1001728000438")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

#url links
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '0171eba95f837a455105157e33525e949b2b95c2')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

#Auto approve 
#In private group or channel must enable request admin approval 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1001615358460').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour request has been approved")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
NO_RESULTS_MSG = is_enabled((environ.get('NO_RESULTS_MSG', "False")), True)
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "10"))
S_GROUP = environ.get('S_GROUP',"https://t.me/filesharebotusers")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/filesharebotusers")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/+u7M4GACWGB0yNTE1")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001857768683))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TGxIRFAN')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "📂Fɪʟᴇɴᴀᴍᴇ : {file_name}\n\n╔═════•✧❅✦❅✧•═════╗\n▣ <a href='https://t.me/filesharebotusers'> **AML UPDATES** </a>\n╚═════•✧❅✦❅✧•═════╝\n\n **JOIN, SHARE & SUPPORT**")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", """<b>⍞ 𝗧𝗶𝘁𝗹𝗲 : <a href={url}>{title}</a>
〄 𝗥𝗲𝗹𝗲𝗮𝘀𝗲𝗱 : {runtime} min | <a href={url}/releaseinfo>{year}</a>

⌗ 𝗚𝗲𝗻𝗿𝗲𝘀 : <i>{genres}</i>
★ 𝗥𝗮𝘁𝗶𝗻𝗴 : <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
〄𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀 : <i>{countries}</i>
⌬ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀 : <i>{languages}</i>

★𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗕𝘆 : <i>{message.chat.title}</i> </b>""")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
