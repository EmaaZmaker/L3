class veichle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
class bus(veichle):
    pass
obj=bus("Horwal",80,50)
print(f"the Veichle name is {obj.name}")
print(f"the max speed is {obj.max_speed}")
print(f"the milage for the bus is {obj.milage}")

        