from sqlite3 import Cursor

from database import create_table, get_entries
from view import display_greeting, display_menu, prompt_new_entry, view_entries


display_greeting()
create_table()


while (user_input := display_menu()) != "3":
    print()
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        cursor: Cursor = get_entries()
        view_entries(cursor)
    else:
        print("\nUser entered an invalid option >:(\n")
