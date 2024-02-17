from pymongo import MongoClient
from config import MONGO_URL
my_client = MongoClient(
    host=MONGO_URL)
my_db = my_client["inrl"]

from config import BASE_URL, MONGO_URL,SESSION_ID, PREFIX, OWENER_ID, BOT_INFO
from .handler import inrl,commands
from .Message import Message
#from .database.main import db