from json import JSONEncoder, JSONDecoder, loads


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__


class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o,no):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        if no == 1:
            product = Mobile(*vals)
        if no == 2:
            product = Headphones(*vals)
        if no == 3:
            product = Laptop(*vals)
        return product
 # define the Product class, which is the base class for all the  products in the store

class Product:
    def __init__(self, name, price=0, category='', quantity=0):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        
    def __str__(self):
         return f"{self.name}, {self.price}, {self.category}, {self.quantity}"

    def __repr__(self):
        return "Product('{}', '{}', '{}', '{}')".format(self.name, self.price, self.category, self.quantity)

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

class Mobile(Product):
    def __init__(self, name, price=0, category='', quantity=0, brand='', model='',color=''):
        super().__init__(name, price, category, quantity)
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return super().__str__() + f", {self.brand}, {self.model}, {self.color}"

    def __repr__(self):
        return "Mobile('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.price, self.category, self.quantity, self.brand, self.model, self.color)

    def __eq__(self, other):
        if(isinstance(other, Mobile)):
            return self.name == other.name    
    
    def __hash__(self):
        return super().__hash__()

class Headphones(Product):
    def __init__(self, name, price=0, category='', quantity=0, brand='', model='', battery=''):
        super().__init__(name, price, category, quantity)
        self.brand = brand
        self.model = model
        self.battery= battery

    def __str__(self):
        return super().__str__() + f", {self.brand}, {self.model}, {self.battery}"

    def __repr__(self):
        return "Headphones('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.price, self.category, self.quantity, self.brand, self.model, self.battery)

    def __eq__(self, other):
        if(isinstance(other, Headphones)):
            return self.name == other.name
    
    def __hash__(self):
        return super().__hash__()

class Laptop(Product):
    def __init__(self, name, price=0, category='', quantity=0, brand='', model='', camera=''):
        super().__init__(name, price, category, quantity)
        self.brand = brand
        self.model = model
        self.camera = camera

    def __str__(self):
        return super().__str__() + f", {self.brand}, {self.model}, {self.camera}"

    def __repr__(self):
        return "Laptop('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.price, self.category, self.quantity, self.brand, self.model, self.camera)

    def __eq__(self, other):  
        if(isinstance(other, Laptop)):
            return self.name == other.name
    
    def __hash__(self):
        return super().__hash__()