from os import getenv
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = getenv("DATABASE")
SECRET = getenv("SECRET")
ALGORITHM = getenv("ALGORITHM")
