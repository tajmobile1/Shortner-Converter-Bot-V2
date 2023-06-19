# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "9738903"))
API_HASH = os.environ.get("API_HASH", "d05599b2b23fd03e208ca54a2ff93445")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5757877293:AAFHlhjUuZImCH2f_5GBVpx6f6igbsdtNEQ")
ADMINS = [int(i.strip()) for i in os.environ.get("1030188110").split("1030188110")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "talink")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://converter:l8ZNNpb4Cy1eJvbi@cluster0.gavigeg.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1030188110")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1030188110)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001916541234"))
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "tajlinkofficial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
