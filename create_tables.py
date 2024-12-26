import sqlite3
from typing import Dict, List, Optional, Union

# Define IVA as global constant
IVA_DEFAULT = 19.0 # Definimos IVA como una constante que puede variar

"""
Este script agrega 2 tablas a la base de datos proporcionada
la tabla contracts y la tabla discount_code rules como las
condiciones de los contratos y los descuentos pueden variar 
las funciones siguientes crean las tablas para poder calcular 
las comisiones. Si hay algún cambio en los contratos o los
descuentos este es el script donde se pueden hacer las modificiones
"""

def create_connection(db_path: str = 'database.sqlite') -> sqlite3.Connection:
    """Create a database connection."""
    return sqlite3.connect(db_path)

def create_tables(cursor: sqlite3.Cursor) -> None:
    """Create the necessary tables if they don't exist."""
    # Create contracts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contracts (
        contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
        commerce_id TEXT NOT NULL,
        min_requests INTEGER NOT NULL,
        max_requests INTEGER,
        rate INTEGER NOT NULL,
        iva REAL DEFAULT 19.0,
        discount REAL DEFAULT 0.0,
        FOREIGN KEY (commerce_id) REFERENCES commerce(commerce_id)
    )
    """)

    # Create discount_rules table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS discount_rules (
        discount_rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
        commerce_id TEXT NOT NULL,
        min_unsuccessful_requests INTEGER NOT NULL,
        max_unsuccessful_requests INTEGER,
        discount_percentage REAL NOT NULL,
        FOREIGN KEY (commerce_id) REFERENCES commerce(commerce_id)
    )
    """)

def insert_contract_rule(
    cursor: sqlite3.Cursor,
    commerce_id: str,
    min_requests: int,
    max_requests: Optional[int],
    rate: int,
    iva: float = IVA_DEFAULT,
    discount: float = 0.0
) -> None:
    """Insert a single contract rule."""
    cursor.execute("""
    INSERT INTO contracts (commerce_id, min_requests, max_requests, rate, iva, discount)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (commerce_id, min_requests, max_requests, rate, iva, discount))

def insert_discount_rule(
    cursor: sqlite3.Cursor,
    commerce_id: str,
    min_unsuccessful_requests: int,
    max_unsuccessful_requests: Optional[int],
    discount_percentage: float
) -> None:
    """Insert a single discount rule."""
    cursor.execute("""
    INSERT INTO discount_rules (
        commerce_id,
        min_unsuccessful_requests,
        max_unsuccessful_requests,
        discount_percentage
    ) VALUES (?, ?, ?, ?)
    """, (commerce_id, min_unsuccessful_requests, max_unsuccessful_requests, discount_percentage))

def insert_initial_contract_rules(cursor: sqlite3.Cursor) -> None:
    """Insert the initial contract rules."""
    contract_rules = [
        # Innovexa Solutions (Fixed contract)
        {"commerce_id": "KaSn-4LHo-m6vC-I4PU", "min_requests": 0, "max_requests": None, "rate": 300},
        
        # NexaTech Industries (Variable contract)
        {"commerce_id": "Vj9W-c4Pm-ja0X-fC1C", "min_requests": 0, "max_requests": 10000, "rate": 250},
        {"commerce_id": "Vj9W-c4Pm-ja0X-fC1C", "min_requests": 10001, "max_requests": 20000, "rate": 200},
        {"commerce_id": "Vj9W-c4Pm-ja0X-fC1C", "min_requests": 20001, "max_requests": None, "rate": 170},
        
        # QuantumLeap Inc (Fixed contract)
        {"commerce_id": "Rh2k-J1o7-zndZ-cOo8", "min_requests": 0, "max_requests": None, "rate": 600},
        
        # Zenith Corp (Variable contract)
        {"commerce_id": "3VYd-4lzT-mTC3-DQN5", "min_requests": 0, "max_requests": 22000, "rate": 250},
        {"commerce_id": "3VYd-4lzT-mTC3-DQN5", "min_requests": 22001, "max_requests": None, "rate": 130},
        
        # FusionWave Enterprises (Fixed contract)
        {"commerce_id": "GdEQ-MGb7-LXHa-y6cd", "min_requests": 0, "max_requests": None, "rate": 300}
    ]

    for rule in contract_rules:
        insert_contract_rule(
            cursor,
            rule["commerce_id"],
            rule["min_requests"],
            rule["max_requests"],
            rule["rate"]
        )

def insert_initial_discount_rules(cursor: sqlite3.Cursor) -> None:
    """Insert the initial discount rules."""
    discount_rules = [
        {
            "commerce_id": "3VYd-4lzT-mTC3-DQN5",
            "min_unsuccessful_requests": 6001,
            "max_unsuccessful_requests": None,
            "discount_percentage": 5.0
        },
        {
            "commerce_id": "GdEQ-MGb7-LXHa-y6cd",
            "min_unsuccessful_requests": 2500,
            "max_unsuccessful_requests": 4500,
            "discount_percentage": 5.0
        },
        {
            "commerce_id": "GdEQ-MGb7-LXHa-y6cd",
            "min_unsuccessful_requests": 4501,
            "max_unsuccessful_requests": None,
            "discount_percentage": 8.0
        }
    ]

    for rule in discount_rules:
        insert_discount_rule(
            cursor,
            rule["commerce_id"],
            rule["min_unsuccessful_requests"],
            rule["max_unsuccessful_requests"],
            rule["discount_percentage"]
        )

def initialize_database(db_path: str = 'database.sqlite') -> None:
    """Initialize the database with tables and initial data."""
    conn = create_connection(db_path)
    cursor = conn.cursor()
    
    create_tables(cursor)
    insert_initial_contract_rules(cursor)
    insert_initial_discount_rules(cursor)
    
    conn.commit()
    conn.close()
    print("Tables 'contracts' and 'discount_rules' created and data inserted successfully.")
    

if __name__ == "__main__":
    initialize_database()