from datetime import date
import sqlite3

from queries import (
    create_table_entries,
    insert_into_entries,
    select_content_and_date_from_entries,
)

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(create_table_entries)


def add_entry(entry_content: str, entry_date: date):
    with connection:
        connection.execute(insert_into_entries, (entry_content, entry_date))


def get_entries() -> sqlite3.Cursor:
    cursor = connection.execute(select_content_and_date_from_entries)
    return cursor
