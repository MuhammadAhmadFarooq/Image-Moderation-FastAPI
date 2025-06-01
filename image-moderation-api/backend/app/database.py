from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["image_moderation"]

tokens_collection = db["tokens"]
usages_collection = db["usages"]