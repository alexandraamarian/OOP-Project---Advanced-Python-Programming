from json import JSONEncoder, JSONDecoder, JSONDecodeError, decoder, dump, loads
import product 

class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""
    def default(self, o):
        return o.__dict__

class Products:
    products = [] # list of products

    @classmethod
    def load_products(cls):
        """ load the products from the disk """
        decoder = product.Decoder()
        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []
        return cls.products

    @classmethod
    def display_products(cls):
        """ display the products """
        try:
            products = cls.load_products()
            for product in products:
                print(f"{product.name} with price: {product.price}. Pieces left: {product.quantity}")
        except JSONDecodeError as e:
            products = None

    @classmethod
    def add_product(cls, product):
        """ add a product to the products collection """
        cls.load_products()
        if product not in cls.products:
            with open("products.txt", 'a') as f:
                e = Encoder()
                encoded_product = e.encode(product)
                dump(encoded_product, f)
                f.write("\n")
    
    @classmethod
    def create_product(cls, name, price, category, quantity):
        """ creates a new product object and adds it to the products collection """
        cls.add_product(product.Product(name, price, category, quantity))
    
    @classmethod
    def remove_product(cls, product):
        """ removes a product from the products collection """
        cls.load_products()
        if product in cls.products:
            cls.products.remove(product)
            with open("products.txt", 'w') as f:
                for product in cls.products:
                    e = Encoder()
                    encoded_product = e.encode(product)
                    dump(encoded_product, f)
                    f.write("\n")

    @classmethod
    def delete_product(cls, name, price=0, category=0, quantity=0):
        """ deletes a product from the products collection """
        cls.remove_product(product.Product(name,price,category,quantity))