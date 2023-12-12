import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "14356452"))
    API_HASH = os.environ.get("API_HASH" "cac21249a0c6373a1b742afb8dbc9cb7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6507590352:AAFewW2HXfbxfiMgk_tra0BmzhxToRHkCOw")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5720092781"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1001623272368")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Nandesha:alabal18@cluster0.6qjsxnq.mongodb.net/?retryWrites=true&w=majority")
