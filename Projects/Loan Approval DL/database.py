import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('userdata.db')

# Create a cursor object
cur = conn.cursor()

# Create table schema
cur.execute('''
CREATE TABLE IF NOT EXISTS userecord (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    no_of_dependents INTEGER,
    income_annum REAL,
    loan_amount REAL,
    loan_term INTEGER,
    cibil_score REAL,
    residential_assets_value REAL,
    commercial_assets_value REAL,
    luxury_assets_value REAL,
    bank_asset_value REAL,
    education INTEGER,
    self_employed INTEGER,
    prediction TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

