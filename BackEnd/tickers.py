import sqlite3
from pathlib import Path
import yfinance as yf

# Find the Data folder path to store the DB
BASE_DIR = Path(__file__).resolve().parent.parent / "Data"
DB_PATH = BASE_DIR / "financial_data.db"

# Function to add records
def add_ticker(db_path, lista_tickers):
    """This function basically adds new tickers to the table currency"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Add ticker from the list, along with the name from Yfinance
    for ticker in lista_tickers:
        try:
            # Instantiate the object
            ticker_object = yf.Ticker(ticker)
            # Get the ticker name
            ticker_name = ticker_object.info.get("longName", "Desconocido")
            # SQL Query
            query = "INSERT OR IGNORE INTO TICKERS (ticker, name) VALUES (? , ?)"
            # Insert the ticker into the DB
            cursor.execute(query, (ticker.upper(), ticker_name))

        except Exception as e:
            print(f"Error getting data for {ticker}: {e}")

    conn.commit()
    conn.close()

# Function to delete records
def delete_ticker(db_path, lista_tickers):
    """This function basically delete new tickers to the table currency"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Delete ticker from the list
    for ticker in lista_tickers:
        try:
            # SQL Query
            query = "DELETE FROM TICKERS WHERE ticker = ?"
            # Insert the ticker into the DB
            cursor.execute(query, (ticker.upper(),))

        except Exception as e:
            print(f"Error getting data for {ticker}: {e}")
            
    conn.commit()
    conn.close()

# ============================ Call the functions ==========================================
mis_tickers = ['AAPL']
#add_ticker(DB_PATH, mis_tickers)
delete_ticker(DB_PATH, mis_tickers)