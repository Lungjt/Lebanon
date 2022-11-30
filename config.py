import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID","17189115"))
API_HASH = os.getenv("API_HASH", "ad6127f6f268f1570e71816fe8d4b337")
SESSION = os.getenv("SESSION", "BABb62y3Ho97oz_Dsc39zJx3NJ0HSCSu8qIRZwkapE8fKSh2jMqhcttGfjK4eciBva4JJOBfGjJEtGkqt9J0Qr1iaQ0f0S8E81RJzeYhzMenFHTdfH7896HoO5EwCLihEsGCR2hNGgzTsVfUJZzpSyMEG83o6gczQMUN426QUQUP-zsb5XVYOfigqwpgTgsjcmr3Clrvy1sbxLndua9gNTNWVxBkxB0qAjlRUOVaUVn-Ccfc2wViFqi-_cNfg5hJondZVgeoZm5cAsZFx1FuITKNmkrOAhtlHpGeeMR--0_aoWj6pAi0Y6OPRE4j1ON3gqLoJ6MoPhbAP71jWwDUk74WfaTslgA")
HNDLR = os.getenv("HNDLR", "$")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "2107960470").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
