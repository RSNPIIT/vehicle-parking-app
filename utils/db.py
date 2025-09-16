import sqlite3
from pathlib import Path

def get_connection():
    base_dir = Path(__file__).resolve().parents[1]
    db_path = base_dir / "instance" / "parking.db"
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row  
    return conn
