from datetime import datetime
from sqlite3 import Cursor
from database import add_entry, create_table, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome."


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


print(welcome, end="\n\n")
create_table()


while (user_input := input(menu)) != "3":
    print()
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        cursor: Cursor = get_entries()
        view_entries(cursor)
    else:
        print("\nUser entered an invalid option >:(\n")
