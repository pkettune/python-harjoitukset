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

auto = Auto("ABC-123", 142)

print(f"{auto.reg}, {auto.topSpeed}km/h, {auto.currentSpeed}, {auto.distanceTravelled}")