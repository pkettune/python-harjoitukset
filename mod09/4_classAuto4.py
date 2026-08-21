import random

class Auto:
    reg = ""
    topSpeed = int()
    currentSpeed = int()
    distanceTravelled = int()

    def __init__(self, regNumber):#leave "autofillers" out of these parameters = currentSpeed & distanceTravelled
        self.reg = "ABC-" + str(regNumber)
        self.topSpeed = random.randint(100, 200)
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
    
autot = []
for i in range(10):
    autot.append(Auto(i+1))

for auto in autot:
        #auto.accelerate(auto.topSpeed)
        while (auto.distanceTravelled < 10000):
            auto.drive(1)
            auto.accelerate(random.randint(-10, 15))

for auto in autot:
    print(f"Reg: {auto.reg}, Top speed: {auto.topSpeed}, Current speed: {auto.currentSpeed}, Distance travelled: {auto.distanceTravelled}")