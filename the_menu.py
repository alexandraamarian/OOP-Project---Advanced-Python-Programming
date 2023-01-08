import mini_menus

def print_main_menu():
    print("Welcome to our shop!\n\n1. Categories\n2. Products\n3. Orders\n4. Exit\n")
    option = int(input("Enter an option between 1 and 4: "))
    actions = {1: categories_click, 2: products_click, 3: orders_click, 4: exit_click}
    action = actions.get(option, error_handler)
    action()


def categories_click():
    print("\nCATEGORIES:")
    mini_menus.print_categories_menu()


def products_click():
    print("\nPRODUCTS")
    mini_menus.print_products_menu()


def orders_click():
    print("\nORDERS")
    mini_menus.print_orders_menu()


def exit_click():
    exit()


def error_handler():
    print("Action not supported")


print_main_menu()