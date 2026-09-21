class Hissi:
    def __init__(self, bottomFloor, highestFloor):
        self.bottomFloor = bottomFloor
        self.highestFloor = highestFloor
        self.currentFloor = bottomFloor

    def move_to_floor(self, targetFloor):
        while (targetFloor > self.currentFloor):
                self.move_up()
        while (targetFloor < self.currentFloor):
                self.move_down()     
            
    def move_up(self):
        if self.currentFloor < self.highestFloor:
            self.currentFloor += 1
            print (self.currentFloor)
            return

    def move_down(self):
        if self.currentFloor > self.bottomFloor:
            self.currentFloor -= 1
            print (self.currentFloor)
            return


h = Hissi(1, 15)
h.move_to_floor(15)
h.move_to_floor(7)
h.move_to_floor(9)
h.move_to_floor(1)