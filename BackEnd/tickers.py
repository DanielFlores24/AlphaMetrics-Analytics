import sqlite3
from pathlib import Path
import yfinance as yf

#Buscamos la dirección de la carpeta Data para poner ahi la DB
BASE_DIR = Path(__file__).resolve().parent.parent / "Data"
DB_PATH = BASE_DIR / "financial_data.db"

# Función para agregar registros
def add_ticker(db_path, lista_tickers):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #Agregar ticker de la lista, junto con el nombre de Yfinance
    for ticker in lista_tickers:
        try:
            #Instanciamos el objeto
            ticker_object = yf.Ticker(ticker)
            #Obtenemmos el nombre de el ticker
            ticker_name = ticker_object.info.get("longName", "Desconocido")
            #Consulta SQL
            query = "INSERT OR IGNORE INTO TICKERS (ticker, name) VALUES (? , ?)"
            #Insertamos el ticker a la DB
            cursor.execute(query, (ticker.upper(), ticker_name))

        except Exception as e:
            print(f"Error al obtener datos de {ticker}: {e}")

    conn.commit()
    conn.close()

# Función para eliminar registros
def delete_ticker(db_path, lista_tickers):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #Eliminar ticker de la lista
    for ticker in lista_tickers:
        try:
            #Consulta SQL
            query = "DELETE FROM TICKERS WHERE ticker = ?"
            #Insertamos el ticker a la DB
            cursor.execute(query, (ticker.upper(),))

        except Exception as e:
            print(f"Error al obtener datos de {ticker}: {e}")
            
    conn.commit()
    conn.close()

# ============================ Llamamos las funciones ==========================================
mis_tickers = ['AAPL']
#add_ticker(DB_PATH, mis_tickers)
delete_ticker(DB_PATH, mis_tickers)