from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "29564931"))
API_HASH = environ.get("API_HASH", "bbdd3112171a5a7716617aa704c20856")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7736806808:AAFv5j33MkQCTTg0HzIXxKga6l2XxyZ1OXw")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6937441525")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002338288864")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://SBHVIP:SBHVIP@cluster0.dlygo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
