from json import JSONEncoder, JSONDecodeError, dump, loads
from product import Mobile, Headphones, Laptop
from product import Decoder as ProductDecoder

class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""

    def default(self, o):
        return o.__dict__


class Products:
    products = []  # list of products

    def checktype(no):
        if no == 1:
            return "mobiles.txt"
        if no == 2:
            return "headphones.txt"
        if no == 3:
            return "laptops.txt"

    @classmethod
    def load_products(cls, no) -> list:
        """ load the products from the disk """
        decoder = ProductDecoder()
        try:
            with open(cls.checktype(no)) as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data, no)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []
        return cls.products

    @classmethod
    def display_products(cls, no):
        """ display the products """
        try:
            products = cls.load_products(no)
            for product in products:
                print(
                    f"{product.name} with price: {product.price}. Pieces left: {product.quantity}"
                )
        except JSONDecodeError as e:
            products = None

    @classmethod
    def add_product(cls, product, no):
        """ add a product to the products collection """
        cls.load_products(no)
        if product not in cls.products:
            with open(cls.checktype(no), 'a') as f:
                e = Encoder()
                encoded_product = e.encode(product)
                dump(encoded_product, f)
                f.write("\n")

    @classmethod
    def create_product(cls, data, no):
        """ creates a new product object and adds it to the products collection """
        if no == 1:
            cls.add_product(Mobile(*data), 1)
        if no == 2:
            cls.add_product(Headphones(*data), 2)
        if no == 3:
            cls.add_product(Laptop(*data), 3)

    @classmethod
    def remove_product(cls, product, no):
        """ removes a product from the products collection """
        cls.load_products(no)
        if product in cls.products:
            cls.products.remove(product)
            with open(cls.checktype(no), 'w') as f:
                for product in cls.products:
                    if ((no == 1 and isinstance(product, Mobile))
                            or (no == 2 and isinstance(product, Headphones))
                            or (no == 3 and isinstance(product, Laptop))):
                        e = Encoder()
                        encoded_product = e.encode(product)
                        dump(encoded_product, f)
                        f.write("\n")

    @classmethod
    def delete_product(cls, data, no):
        """ deletes a product from the products collection """
        if no == 1:
            cls.remove_product(Mobile(data), 1)
        if no == 2:
            cls.remove_product(Headphones(data), 2)
        if no == 3:
            cls.remove_product(Laptop(data), 3)
