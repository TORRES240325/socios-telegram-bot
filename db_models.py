# --- EN db_models.py ---

# ... (Todo el código de las clases y la función inicializar_db) ...

# --- Función de Inicialización ---

def inicializar_db(engine): 
    # ... (el código de inicializar_db) ...
    # ...

# --- MODIFICACIÓN DE LA CONEXIÓN AL FINAL DEL ARCHIVO ---
# Railway/Render pasa la URL como variable de entorno. La usamos.

if __name__ == '__main__':
    # Carga el .env localmente, pero en Railway usa las variables inyectadas.
    load_dotenv() 
    
    # Intenta obtener la URL de la variable de entorno, que ahora es la de Railway
    DATABASE_URL = os.getenv('DATABASE_URL') 
    
    if not DATABASE_URL:
        print("ERROR: DATABASE_URL no encontrada. Asegúrate de definirla en .env o en el hosting.")
        sys.exit(1) # Importar sys

    print(f"Conectando a PostgreSQL Remoto: {DATABASE_URL}")

    try:
        # Crea el motor de conexión
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        print("Inicializando la base de datos y creando/verificando tablas...")
        
        # Ejecuta la función de creación de tablas
        inicializar_db(engine) 
        print("¡Proceso de creación de tablas finalizado con éxito!")
        
    except Exception as e:
        print(f"\n--- ERROR CRÍTICO DE CONEXIÓN ---\nNo se pudo conectar a la base de datos en {DATABASE_URL}")
        print("Asegúrate de que la URL y las credenciales sean correctas.")
        print(f"Detalle del error: {e}\n")
