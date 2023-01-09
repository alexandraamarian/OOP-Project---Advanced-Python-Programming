from json import JSONEncoder, JSONDecoder, JSONDecodeError, decoder, dump, loads
import order
import products

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
        productss = products.Products.load_products()
        try:
            k=0
            for prod in productss:
                if prod.name == name:
                    k=1
                    cls.add_order(order.Order(name, quantity, destionation))
                    prod.quantity = int(prod.quantity) - int(quantity)
                    products.Products.delete_product(name)
                    products.Products.create_product(prod.name, prod.price, prod.category, str(prod.quantity))
            if k!=1:
                print("\n Product not found. Please try again with a product that is in stock. \n")
        except JSONDecodeError as e:
            productss = None        
            