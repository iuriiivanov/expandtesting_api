import os

from dotenv import load_dotenv

API_BASE_URL = "https://practice.expandtesting.com/notes/api"
API_DEFAULT_TOKEN: str = os.getenv(key="API_DEFAULT_TOKEN", default="API_DEFAULT_TOKEN")


load_dotenv()
