import product

class Phone(product):
    def __init__(self,name,price,category,quantity,brand) -> None:
        super().__init__(name,price,category,quantity)
        self.brand = brand
    
    def __str__(self) -> str:
        return "Phone('{}', '{}', '{}', '{}','{}')".format(self.name, self.material, self.category, self.quantity,self.brand)
    
    def __repr__(self) -> str:
        return "Phone('{}', '{}', '{}', '{}','{}')".format(self.name, self.material, self.category, self.quantity,self.brand)