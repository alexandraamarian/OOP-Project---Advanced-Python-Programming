from categories import Categories
from products import Products
from orders import Orders

def print_categories_menu():
    print("1. Add a category\n2. Remove a category\n3. Display all the categories\n")
    option = int(input("Enter an option between 1 and 3: "))

    category_actions = {1: add_category_in_menu, 2: remove_category_from_menu, 3: display_categories}

    category_action = category_actions.get(option, error_handler)
    category_action()


def print_products_menu():
    print("1. Add a product\n2. Remove a product\n3. Display all the products\n")
    option = int(input("Enter an option between 1 and 3: "))

    product_actions = {1: add_product_in_menu, 2: remove_product_from_menu, 3: display_products}

    product_action = product_actions.get(option, error_handler)
    product_action()


def print_orders_menu():
    print("1. Place a new order\n2. Display all orders\n")
    option = int(input("Enter an option between 1 and 2: "))

    order_actions = {1: place_an_order, 2: display_orders}

    order_action = order_actions.get(option, error_handler)
    order_action()


def add_category_in_menu():
    category = input("Enter the category name you want to add: ")
    Categories.create_category(category)


def remove_category_from_menu():
    category = input("Enter the category name you want to remove: ")
    Categories.delete_category(category)

def display_categories():
    Categories.display_categories()


def add_product_in_menu():
    product_name = input("Enter the product name you want to add: ")
    product_price = input("Enter the product price you want to add: ")
    product_category = input("Enter the product category: ")
    product_quantity = input("Enter the product quantity: ")
    Products.create_product(product_name, product_price, product_category, product_quantity)

def remove_product_from_menu():
    print("\n")
    display_products()
    print("\n")
    product_name = input("Enter the product name you want to remove: ")
    Products.delete_product(product_name)

def display_products():
    Products.display_products()


def place_an_order():
    print("\n")
    display_products()
    print("\n")
    product_name = input("Enter the product name you want to order: ")
    product_quantity = input("Enter the product quantity you want to order: ")
    product_destination = input("Enter the destination of the order: ")
    Orders.create_order(product_name, product_quantity, product_destination)


def display_orders():
    Orders.display_orders()


def error_handler():
    print("Action not supported")
