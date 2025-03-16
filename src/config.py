import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración global
API_KEY = os.getenv("API_NINJA_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/motorcycles"
EXCEL_OUTPUT_PATH = os.path.join("data", "resultados_motos.xlsx")