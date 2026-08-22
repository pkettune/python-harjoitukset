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

class Race:
    name = ""
    length = int()# km
    participants = []

    def __init__(self, name, length, participants):
        self.name = name
        self.length = length
        self.participants = []
        for i in range(participants):
            self.participants.append(Auto(i+1))

    def hour_is_passed(self):
        for car in self.participants:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        
    def checkpoint_positions(self):
        for car in self.participants:
            print(f"Reg: {car.reg}, Top speed: {car.topSpeed}, Current speed: {car.currentSpeed}, Distance travelled: {car.distanceTravelled}")

    def race_ended(self):
        for car in self.participants:
            if car.distanceTravelled >= self.length:
                print("\nFinal Stats\n")
                self.checkpoint_positions()
                return True
            else:
                return False


r = Race("Suuri Romuralli", 8000, 10)

hoursPassed = 0

while (r.race_ended() == False):
    r.race_ended()
    r.hour_is_passed()
    hoursPassed += 1
    if (hoursPassed % 10 == 0):
        r.checkpoint_positions()

# for auto in autot:
#     print(f"Reg: {auto.reg}, Top speed: {auto.topSpeed}, Current speed: {auto.currentSpeed}, Distance travelled: {auto.distanceTravelled}")