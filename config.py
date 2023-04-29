from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ['BOT_TOKEN']
HOST = os.environ['HOST']
WEBHOOK_PATH = f'/{BOT_TOKEN}'
WEBHOOK_URL = f'{HOST}{WEBHOOK_PATH}'

DB_URL = os.environ['DB_URL']