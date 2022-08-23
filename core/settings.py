from os import getenv
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path.cwd().parent

load_dotenv()

DB_NAME = getenv('DB_NAME')
DB_USER_USERNAME = getenv('DB_USER_USERNAME')
DB_USER_PASSWORD = getenv('DB_USER_PASSWORD')