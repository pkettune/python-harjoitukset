class Hissi:
    def __init__(self, bottomFloor, highestFloor):
        self.bottomFloor = bottomFloor
        self.highestFloor = highestFloor
        self.currentFloor = bottomFloor

    def move_to_floor(self, targetFloor):
        while (targetFloor > self.currentFloor < self.highestFloor):
            self.move_up(targetFloor)
        while (targetFloor < self.currentFloor > self.bottomFloor):
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
    def __init__(self, bottomFloor, highestFloor, numberOfElevator):
        self.bottomFloor = bottomFloor
        self.highestFloor = highestFloor
        self.numberOfElevator = []
        for i in range(numberOfElevator):
            self.numberOfElevator.append(Hissi(bottomFloor, highestFloor))

    def use_elevator(self, elevatorNumber, targetFloor):
        elevator = self.numberOfElevator[elevatorNumber]
        elevator.move_to_floor(targetFloor)
        
t = Talo(1, 9, 4)
t.use_elevator(2, 9)
t.use_elevator(3, 4)
t.use_elevator(2, 1)
# h = Hissi(1, 15)
# h.move_to_floor(15)
# h.move_to_floor(1)