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

    def drive(self, hours):
        self.distanceTravelled += self.currentSpeed * hours
        return self.distanceTravelled

auto = Auto("ABC-123", 142)
        
auto.accelerate(30)
auto.drive(5)
print(auto.distanceTravelled)
auto.accelerate(70)
auto.drive(1)
print(auto.distanceTravelled)
auto.accelerate(50)
auto.drive(2)
print(auto.currentSpeed)
print(auto.distanceTravelled)
auto.accelerate(-200)
#print(auto.currentSpeed)
#print(f"{auto.reg}, {auto.topSpeed}km/h, {auto.currentSpeed}, {auto.distanceTravelled}")