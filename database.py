import sqlite3

def create_connection():
    return sqlite3.connect("crm_web.db")

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            vehiculo TEXT,
            matricula TEXT,
            telefono TEXT,
            servicio TEXT,
            fecha_cita TEXT,
            proximo_servicio TEXT
        )
    """)
    conn.commit()
    conn.close()

def insertar_cita(cliente, vehiculo, matricula, telefono, servicio, fecha_cita, proximo_servicio):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO citas (cliente, vehiculo, matricula, telefono, servicio, fecha_cita, proximo_servicio)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (cliente, vehiculo, matricula, telefono, servicio, fecha_cita, proximo_servicio))
    conn.commit()
    conn.close()