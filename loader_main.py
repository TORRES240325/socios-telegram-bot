import os
import logging
import sys
from dotenv import load_dotenv
import subprocess

# --- Configuración ---
# RUTA EXPLÍCITA AL ARCHIVO .env (Asumiendo que está en la misma carpeta)
# Esto garantiza que lo encuentre donde sea que lo ejecutes.
load_dotenv(os.path.join(os.getcwd(), '.env'))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- Verificación de Token ---
TOKEN = os.getenv('BOT_MAIN_TOKEN')
if not TOKEN:
    print("------------------------------------------------------------------")
    print("🚨 ERROR FATAL: BOT_MAIN_TOKEN no encontrado.")
    print("Asegúrate de que BOT_MAIN_TOKEN esté definido en el archivo .env.")
    print("------------------------------------------------------------------")
    sys.exit(1)

print(f"Cargando BOT PRINCIPAL (Token: {TOKEN[:5]}...{TOKEN[-5:]})")
print("El Bot se está iniciando. La consola se quedará activa.")

try:
    subprocess.run([sys.executable, 'bot_main.py'])

except KeyboardInterrupt:
    print("\nDeteniendo BOT PRINCIPAL por el usuario.")
except Exception as e:
    logging.error(f"Error inesperado durante la ejecución del Bot Principal: {e}")