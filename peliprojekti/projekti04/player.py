import items

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
            self.itemLoad += item
        return

    def show_items():
        for item in Player.self.items:
            print(item)
        return
