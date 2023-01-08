from json import JSONEncoder, JSONDecoder, loads
from product import Product

class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        order = Order(*vals)
        return order

class Order:

    def __init__(self, product, quantity, destination):
        self.product = product
        self.quantity = quantity
        self.destination = destination

    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.destination}"
    
    def __repr__(self):
        return "Order('{}', '{}', '{}')".format(self.product, self.quantity, self.destination)
    
    def __eq__(self, other):
        if(isinstance(other, Order)):
            return self.destination == other.destination and self.product == other.product and self.quantity == other.quantity

    
    def getDestination(self):
        return self.destination
    
    def getOrder(self):
        return self

    def getProduct(self):
        return self.product.getProductName()  

    def getQuantity(self):
        return self.quantity 