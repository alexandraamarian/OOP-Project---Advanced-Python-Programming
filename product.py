from json import JSONEncoder, JSONDecoder, loads


# define the Encoder class used in serialization
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
        product = Product(*vals)
        return product
 # define the Product class, which is the base class for all the  products in the store

class Product:
    def __init__(self, name, price=0, category='', quantity=0):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        
    def __str__(self):
         return f"{self.name}, {self.material}, {self.category}, {self.quantity}"

    def __repr__(self):
        return "Product('{}', '{}', '{}', '{}')".format(self.name, self.material, self.category, self.quantity)

    def __eq__(self, other):
        if(isinstance(other, Product)):
            return self.name == other.name
    def __hash__(self):
        return hash(self.name)
    
    def getProductName(self):
        return self.name

    def getProductPrice(self):
        return self.price
    
    def getProductCategory(self):
        return self.category
    
    def getProductQuantity(self):
        return self.quantity

    