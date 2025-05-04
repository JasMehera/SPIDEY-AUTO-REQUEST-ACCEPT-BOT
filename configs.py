# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    
    CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "-1002618481745").split(","))) # for the multiple forcesub
    
    REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
    # Spidey
    ADMINS = list(map(int, getenv("ADMINS", "7518139247").split()))
    DATABASE_URI = getenv("DATABASE_URI", "mongodb+srv://f00il:anler0.qhc7amc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1002100963256")) 

class temp(object):    
    U_NAME = None
    B_NAME = None
      
Spidey = Config()

# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777
