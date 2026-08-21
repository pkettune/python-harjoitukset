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


h = Hissi(1, 15)
h.move_to_floor(15)
h.move_to_floor(1)