<<<<<<< HEAD:peliprojekti/player.py
import items
=======
import peliprojekti.projekti04.item as item
>>>>>>> 0a4762588685130a1b76dbf14766f40617105648:peliprojekti/projekti04/player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = 0, 0
        self.itemLoad = 0

    def move(self, room):
        self.location = room
        print(f"You are in room: {room}")

    def collect_item(self, item):
        if item in self.location.items:
            self.items.append(item)
        newItem = (itemName, itemWeight)
        self.itemLoad += itemWeight
        return
