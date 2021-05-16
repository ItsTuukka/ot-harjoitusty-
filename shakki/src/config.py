import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except:
    print('The .env file not found :(')

DB_PATH = os.getenv("DB")
