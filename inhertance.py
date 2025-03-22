#Single level inheritance
class Car:
    def __init__(self,max_speed,color):
        self.max_speed = max_speed
        self.color = color
    def show_max_speed(self):
        print(self.max_speed)
    def show_color(self):
        print(self.color)        

class Car2(Car):
    def show_max_speed(self):
        print("140kmph")
    def show_car_type(self):
        print("SUV")   
#multiple inhertance 
class car3(Car2,Car):
    def show_max_speed(self):
        print("290kmph")
#Multi level Inheritance
class car4(car3):
    def show_max_speed(self):
        print("250kmnph")
    def show_color(self):
        print('White')

   
obj=Car("123","BlaCK")   
obj.show_max_speed()
obj.show_color()


