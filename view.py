from datetime import datetime
from sqlite3 import Cursor

from database import add_entry


def display_greeting():
    welcome = "Welcome."
    print(welcome, end="\n\n")


def display_menu():
    menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

    return input(menu)


def prompt_new_entry():
    entry_content = input("What's up for today, you? ")
    current_datetime = datetime.now()
    entry_date = current_datetime.date()
    add_entry(entry_content, entry_date)


def view_entries(cursor: Cursor):
    for entry in cursor:
        content, date = entry
        print(date)
        print(content, end="\n\n")
