from database import create_table
from menu import ACTIONS
from view import (
    display_greeting,
    display_invalid_option_message,
    display_menu,
    prompt_new_entry,
    view_entries,
)


display_greeting()
create_table()


while (user_input := display_menu()) != ACTIONS["EXIT"]:
    print()
    if user_input == ACTIONS["ADD_ENTRY"]:
        prompt_new_entry()
    elif user_input == ACTIONS["VIEW_ENTRIES"]:
        view_entries()
    else:
        display_invalid_option_message()
