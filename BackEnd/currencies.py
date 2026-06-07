import sqlite3
from pathlib import Path
import yfinance as yf

# Find the Data folder path to store the DB
BASE_DIR = Path(__file__).resolve().parent.parent / "Data"
DB_PATH = BASE_DIR / "financial_data.db"

# Function to add records
def add_currency(db_path, currencys):
    """This function basically adds new currencies to the table currency"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Add currencies
    for currency in currencys:
        try:
            # SQL Query
            query = "INSERT OR IGNORE INTO CURRENCY (name) VALUES (?)"
            # Insert the currency into the DB
            cursor.execute(query, (currency,))

        except Exception as e:
            print(f"Error getting data for {currency}: {e}")

    conn.commit()
    conn.close()

# Function to delete records
def delete_currency(db_path, currencys):
    """This function basically deletes currencies from the table currency"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Delete currencies
    for currency in currencys:
        try:
            # SQL Query
            query = "DELETE FROM CURRENCY WHERE name = ?"
            # Delete the currency from the DB
            cursor.execute(query, (currency,))

        except Exception as e:
            print(f"Error getting data for {currency}: {e}")

    conn.commit()
    conn.close()

# ============================ Call the functions ==========================================
add_currency(DB_PATH, ["USD", "MXN"])