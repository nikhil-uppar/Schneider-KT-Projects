# #Without Parameters
class Parent:
    def __init__(self):
        print("Class Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Class Child")

Obj = Child()

#With Parameters
class Laptop1:
    def __init__(self,brand):
        self.brand=brand
        print(f"The brand is: {self.brand}")

class Laptop2(Laptop1):
    def __init__(self,brand,processor,price):
        super().__init__(brand)
        self.processor=processor
        self.price=price
        print(f"Processor is {self.processor}",f"\nPrice is {self.price}")

Spec = Laptop2("HP","i3",35000)