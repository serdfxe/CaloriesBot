import os
from dotenv import load_dotenv


load_dotenv(override=True)

TOKEN = os.getenv('TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
GPT_API_KEY = os.getenv('GPT_API_KEY')
GPT_API_URL = os.getenv('GPT_API_URL')

GPT_SYSTEM_MESSAGE = "You are an AI assistant specialized in nutritional analysis. When given a description of a dish, reply with exactly four int numbers representing Calories, Protein, Fat, and Carbohydrates, in that order, separated by commas, and nothing else. In case of HARD illegibility, output 'exc'."

OWNER_ID = os.getenv('OWNER_ID')

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
