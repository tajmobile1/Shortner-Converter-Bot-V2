# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "20804756"))
API_HASH = os.environ.get("API_HASH", "ecd0e2a4cc383ae5717059e7ae120adb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5782196670:AAERLLFpI4T3zRKb9HW8tFswwhBfW4SsSJs")
ADMINS = [int(i.strip()) for i in os.environ.get("1782059495").split("5576458964")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "grolink")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://MdMatin:x7bdggKJ9zb9JSK@cluster0.89bzvjn.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5576458964")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001959918356")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Grolink_Official_Channel") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
