import items

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = None
        self.itemLoad = 0

    def move(self, room):
        self.location = room
        print(f"Olet paikassa: {room.name}")

    def collect_item(self):
        if self.location.itemToFind == None:
            print("Ei kerättäviä esineitä.")
            return
        itemName = self.location.itemToFind
        item = items.Item(itemName)
        self.items.append(item)
        self.itemLoad = self.itemLoad + item.weight
        self.location.itemToFind = None
        print("Picked up: " + itemName)
        return

    def show_items(self):
        if not self.items:
            print("No items")
            return
        for item in self.items:
            print(item.name)
        return

    def change_name(self):
        newName = input("Tell me your new name\n")
        self.name = newName
        print("\nHei " + self.name)
        return

    def look_around(self):
        print(f"Olet paikassa: {self.location.name}")
        item_name = self.location.itemToFind
        if item_name:
            print(f"Huoneessa on: {item_name}")
        else:
            print("Huoneessa ei ole mitään tärkeää")
        return
