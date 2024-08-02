# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28238792"))
API_HASH = getenv("API_HASH", "89b0d1f463a860525e1c117ccdef5aa3")
BOT_TOKEN = getenv("BOT_TOKEN", "6360468548:AAG--HzheT_KQvGKYXM135XmGNumPIi0a2Y")
OWNER_ID = int(getenv("OWNER_ID", "1236569704"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://shubhp97:RI9LlWYGuMIJFJ1w@mrpanchall.p0lnx7k.mongodb.net/?retryWrites=true&w=majority&appName=Mrpanchall")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
