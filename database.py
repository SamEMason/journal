from datetime import date
import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(entry_content: str, entry_date: date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, str(entry_date))
        )


def get_entries() -> sqlite3.Cursor:
    cursor = connection.execute("SELECT content, date FROM entries;")
    return cursor
