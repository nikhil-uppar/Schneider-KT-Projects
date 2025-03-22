class bike:
    catergory= "motor_vehicle"
    def __init__(self,model,displacement):
        self.model=model
        self.displacement=displacement
Bike1=bike("Yezdi", 250)
print(Bike1.model,)
print()
print(Bike1.catergory)