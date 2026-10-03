roomList = {}

class Room:
    def __init__(self, name, itemToFind):
        self.name = name
        self.itemToFind = itemToFind
        roomList[name] = itemToFind
        return roomList