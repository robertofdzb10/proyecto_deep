# config.py
import os
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env
load_dotenv()

# Acceder a las variables de entorno
API_KEY_GPT4O = os.getenv("API_KEY_GPT4O")
MODEL_PATH = os.getenv("MODEL_PATH")
DATA_RAW_PATH = os.getenv("DATA_RAW_PATH")
DATA_PROCESSED_PATH = os.getenv("DATA_PROCESSED_PATH")
