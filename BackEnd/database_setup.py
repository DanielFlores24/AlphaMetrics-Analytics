import sqlite3
from pathlib import Path

#Buscamos la dirección de la carpeta Data para poner ahi la DB
BASE_DIR = Path(__file__).resolve().parent.parent / "Data"
DB_PATH = BASE_DIR / "financial_data.db"


def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #Creación del Esquema SQL
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS USERS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            cash REAL
        );

        CREATE TABLE IF NOT EXISTS TICKERS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT UNIQUE NOT NULL,
            name TEXT
        );

        CREATE TABLE IF NOT EXISTS CURRENCY (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );

        CREATE TABLE IF NOT EXISTS CURRENCY_LINE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_currency TEXT,
            date DATE,
            currency_rate REAL
        );
        CREATE TABLE IF NOT EXISTS PRICE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ticker INTEGER,
            date DATE,
            open REAL,
            close REAL,
            high REAL,
            low REAL,
            volume REAL,
            FOREIGN KEY (id_ticker) REFERENCES TICKERS(id)
        );

        CREATE TABLE IF NOT EXISTS COMPANY_METRICS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ticker INTEGER,
            fiscal_year INTEGER,
            fiscal_quarter INTEGER,
            revenue REAL,
            net_income REAL,
            total_assets REAL,
            total_liability REAL,
            operating_cash_flow REAL,
            capital_expenditure REAL,
            free_cash_flow REAL,
            shares_outstanding REAL,
            FOREIGN KEY (id_ticker) REFERENCES TICKERS(id)
        );

        CREATE TABLE IF NOT EXISTS DIVIDENDS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ticker INTEGER,
            id_currency INTEGER,
            date DATE,
            dividend_amount REAL,
            FOREIGN KEY (id_ticker) REFERENCES TICKERS(id),
            FOREIGN KEY (id_currency) REFERENCES CURRENCY(id)
        );

        CREATE TABLE IF NOT EXISTS PORTFOLIO (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER,
            id_ticker INTEGER,
            id_currency INTEGER,
            cost REAL,
            number_actions INTEGER,
            FOREIGN KEY (id_user) REFERENCES USERS(id),
            FOREIGN KEY (id_ticker) REFERENCES TICKERS(id),
            FOREIGN KEY (id_currency) REFERENCES CURRENCY(id)
        );
    ''')

    conn.commit()
    conn.close()
    print("Base de datos creada exitosamente.")


# ============================ Llamamos la función ==========================================
init_db(DB_PATH)