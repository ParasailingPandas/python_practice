class car: 
    wheels = 4
    seats = 5
    color = "red"
    speed = "fast"
    weight = "heavy"

    def __init__(self, wheels, seats, color, speed, weight):    
        self.wheels = wheels
        self.seats = seats
        self.color = color
        self.speed = speed
        self.weight = weight
    
    def get_color(self):
        return self.color

    def description(self): 
        print("This car has", self.wheels, "wheels")

mycar = car(6,1,"purple","slow","fat")
mycar.description()
print(mycar.get_color())
