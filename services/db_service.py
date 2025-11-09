import sqlite3
from datetime import datetime

class DBService:
    def __init__(self, db_path="database/parkmate.db"):
        self.db_path = db_path
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_number TEXT,
                vehicle_type TEXT,
                driver_name TEXT,
                phone TEXT,
                entry_time TEXT,
                exit_time TEXT,
                fare REAL
            )
        """)
        conn.commit()
        conn.close()

    def add_history(self, vehicle, fare):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO history(vehicle_number, vehicle_type, driver_name, phone, entry_time, exit_time, fare)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            vehicle.vehicle_number,
            vehicle.__class__.__name__,
            vehicle.driver_name,
            vehicle.phone,
            vehicle.entry_time.strftime("%Y-%m-%d %H:%M:%S"),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            fare
        ))
        conn.commit()
        conn.close()

    def get_all_history(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM history ORDER BY id DESC")
        records = cursor.fetchall()
        conn.close()
        return records