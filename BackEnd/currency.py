import sqlite3
from pathlib import Path
import yfinance as yf
#Buscamos la dirección de la carpeta Data para poner ahi la DB
BASE_DIR = Path(__file__).resolve().parent.parent / "Data"
DB_PATH = BASE_DIR / "financial_data.db"

# Función para agregar registros
def add_currency(db_path, currencys):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #Agregamos las divisas
    for currency in currencys:
        try:
            #Consulta SQL
            query = "INSERT OR IGNORE INTO CURRENCY (name) VALUES (?)"
            #Insertamos el currency a la DB
            cursor.execute(query, (currency,))

        except Exception as e:
            print(f"Error al obtener datos de {currency}: {e}")

    conn.commit()
    conn.close()

# Función para eliminar registros
def delete_currency(db_path, currencys):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #Agregamos las divisas
    for currency in currencys:
        try:
            #Consulta SQL
            query = "DELETE FROM CURRENCY WHERE name = ?"
            #Eliminamos el currency a la DB
            cursor.execute(query, (currency,))

        except Exception as e:
            print(f"Error al obtener datos de {currency}: {e}")

    conn.commit()
    conn.close()

# ============================ Llamamos las funciones ==========================================
add_currency(DB_PATH, ["USD", "MXN"])