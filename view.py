from datetime import datetime
from sqlite3 import Cursor

from database import add_entry, get_entries
from menu import MENU


def display_greeting():
    welcome = "Welcome."
    print(welcome, end="\n\n")


def display_invalid_option_message():
    print("\nUser entered an invalid option >:(\n")


def display_menu():
    return input(MENU)


def prompt_new_entry():
    entry_content = input("What's up for today, you? ")
    current_datetime = datetime.now()
    entry_date = current_datetime.date()
    add_entry(entry_content, entry_date)


def view_entries():
    cursor: Cursor = get_entries()

    for entry in cursor:
        content, date = entry
        print(date)
        print(content, end="\n\n")
