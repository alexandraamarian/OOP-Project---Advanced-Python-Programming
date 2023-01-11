from json import JSONEncoder, JSONDecoder, JSONDecodeError, decoder, dump, loads
import order
import products
from products import Products
from product import Laptop, Headphones, Mobile
class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""
    def default(self, o):
        return o.__dict__

class Orders:
    
    orders = [] # list of orders

    @classmethod
    def load_orders(cls):
        """ load the orders from the disk """
        decoder = order.Decoder()
        try:
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.decode(data)
                    if decoded_order not in cls.orders:
                        cls.orders.append(decoded_order)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.orders = []
        return cls.orders

    @classmethod
    def display_orders(cls):
        """ display the orders """
        try:
            orders = cls.load_orders()
            for order in orders:
                print("Product ordered: " + order.product + " Quantity: " + order.quantity + ". Destination: " + order.destination)
        except JSONDecodeError as e:
            orders = None
    
    @classmethod
    def add_order(cls, order):
        """ add an order to the orders collection """
        cls.load_orders()
        if order not in cls.orders:
            with open("orders.txt", 'a') as f:
                e = Encoder()
                encoded_order = e.encode(order)
                dump(encoded_order, f)
                f.write("\n")
    
    @classmethod
    def create_order(cls, name, quantity, destionation):
        """ creates a new order object and adds it to the orders collection """
        laptop_products = list(filter( lambda x: isinstance(x, Laptop),Products.load_products(3)))
        headphone_products = list(filter( lambda x: isinstance(x,Headphones ),Products.load_products(2)))
        mobile_products = list(filter( lambda x: isinstance(x, Mobile),Products.load_products(1)))
        try:
            k=0
            for prod in mobile_products:
                no=1
                if prod.name == name:
                    k=1
                    cls.add_order(order.Order(name, quantity, destionation))
                    prod.quantity = int(prod.quantity) - int(quantity)
                    products.Products.delete_product(name,no)
                    data = [prod.name, prod.price, prod.category, str(prod.quantity), prod.brand, prod.model, prod.color]
                    products.Products.create_product(data, no)

            for prod in headphone_products:
                no=2
                if prod.name == name:
                    k=1
                    cls.add_order(order.Order(name, quantity, destionation))
                    prod.quantity = int(prod.quantity) - int(quantity)
                    products.Products.delete_product(name,no)
                    data = [prod.name, prod.price, prod.category, str(prod.quantity), prod.brand, prod.model, prod.battery]
                    products.Products.create_product(data , no)

            for prod in laptop_products:
                    no=3
                    if prod.name == name:
                        k=1
                        cls.add_order(order.Order(name, quantity, destionation))
                        prod.quantity = int(prod.quantity) - int(quantity)
                        products.Products.delete_product(name,no)
                        data = [prod.name, prod.price, prod.category, str(prod.quantity), prod.brand, prod.model, prod.camera]
                        products.Products.create_product(data, no)
            if k!=1:
                print("\n Product not found. Please try again with a product that is in stock. \n")
                
        except JSONDecodeError as e:
            laptop_products = None      
            headphone_products = None
            mobile_products = None

            