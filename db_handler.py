# db_handler.py - DB Interaction

import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS moderation_reports (
            id INTEGER PRIMARY KEY,
            text TEXT,
            prediction TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_report(text, prediction):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO moderation_reports (text, prediction) VALUES (?, ?)
    ''', (text, prediction))
    conn.commit()
    conn.close()
