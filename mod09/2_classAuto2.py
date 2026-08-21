class Auto:
    reg = ""
    topSpeed = int()
    currentSpeed = int()
    distanceTravelled = int()

    def __init__(self, reg, topSpeed):#leave "autofillers" out of these parameters = currentSpeed & distanceTravelled
        self.reg = reg
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.distanceTravelled = 0

    def accelerate(self, acceleration):
        if (self.currentSpeed + acceleration > self.topSpeed):
            self.currentSpeed = self.topSpeed

        elif (self.currentSpeed + acceleration <= 0):
            self.currentSpeed = 0

        else:
            self.currentSpeed += acceleration
            
        return self.currentSpeed
        
auto = Auto("ABC-123", 142)
        
auto.accelerate(30)
auto.accelerate(70)
auto.accelerate(50)
print(auto.currentSpeed)
auto.accelerate(-200)
print(auto.currentSpeed)
#print(f"{auto.reg}, {auto.topSpeed}km/h, {auto.currentSpeed}, {auto.distanceTravelled}")