class car: 
    wheels                           = 4
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
        return "This car has " + str(self.wheels) + " wheels"

mycar = car(6,1,"purple","slow","fat")
print(mycar.description())
print(mycar.get_color())

yourcar = car(44,0,"orange","slow","fat")
print(yourcar.description())