import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
IG_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")