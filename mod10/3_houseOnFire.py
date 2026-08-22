class Hissi:
    def __init__(self, bottomFloor, highestFloor):
        self.bottomFloor = bottomFloor
        self.highestFloor = highestFloor
        self.currentFloor = bottomFloor

    def move_to_floor(self, targetFloor):
        while (targetFloor > self.currentFloor):
            self.move_up(targetFloor)
        while (targetFloor < self.currentFloor):
            self.move_down(targetFloor)     
            
    def move_up(self, targetFloor):
        if self.currentFloor < targetFloor:
            self.currentFloor += 1
            print (self.currentFloor)
            return

    def move_down(self, targetFloor):
        if self.currentFloor > targetFloor:
            self.currentFloor -= 1
            print (self.currentFloor)
            return

class Talo:
    def __init__(self, bottomFloor, highestFloor, numberOfElevators):
        self.bottomFloor = bottomFloor
        self.highestFloor = highestFloor
        self.elevators = []# this should be left empty!!!!!!!!!!!!!!!!!!!!!

        for i in range(numberOfElevators):
            self.elevators.append(Hissi(bottomFloor, highestFloor))

    def use_elevator(self, elevatorNumber, targetFloor):
        self.elevators[elevatorNumber - 1].move_to_floor(targetFloor)# - 1 for correct elevator number (staring from 1.)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.move_to_floor(self.bottomFloor)

#https://stackoverflow.com/questions/522563/how-can-i-access-the-index-value-in-a-for-loop

t = Talo(1, 9, 4)
t.use_elevator(1, 2)
t.use_elevator(2, 3)
t.use_elevator(3, 4)
t.use_elevator(4, 5)

t.fire_alarm()
# t.use_elevator(1, 9)
# t.use_elevator(2, 4)
# t.use_elevator(3, 7)
# t.use_elevator(4, 5)
# h = Hissi(1, 15)
# h.move_to_floor(15)
# h.move_to_floor(1)