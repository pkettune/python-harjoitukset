class Car:
    reg = ""
    topSpeed = int()
    currentSpeed = int()
    distanceTravelled = int()

    def __init__(self, regNumber, topSpeed, powerCap):#leave "autofillers" out of these parameters = currentSpeed & distanceTravelled
        self.reg = regNumber
        self.topSpeed = topSpeed
        self.powerCap = powerCap#kWh or liters
        self.currentSpeed = 0
        self.distanceTravelled = 0

    def drive(self, hours):
        self.distanceTravelled += self.currentSpeed * hours
        return self.distanceTravelled

class ElectricCar(Car):
    def __init__(self, regNumber, topSpeed, batteryCap):
        super().__init__(regNumber, topSpeed, batteryCap)

class GasCar(Car):
    def __init__(self, regNumber, topSpeed, fuelTankCap):
        super().__init__(regNumber, topSpeed, fuelTankCap)

eCar = ElectricCar("ABC-15", 180, 52.5)
gCar = GasCar("ABC-123", 165, 32.3)
cars = [eCar, gCar]
eCar.currentSpeed = 90
gCar.currentSpeed = 120

for car in cars:
    car.drive(3)
    print(car.distanceTravelled)

    #print(f"Reg: {car.reg}, Top speed: {car.topSpeed}, Current speed: {car.currentSpeed}, Distance travelled: {car.distanceTravelled}")