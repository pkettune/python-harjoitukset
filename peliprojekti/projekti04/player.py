import peliprojekti.projekti04.item as item

class Player:
    def __init__(self, name, items, locX, locY):
        self.name = name
        self.items = items
        self.location = locX, locY
        self.itemLoad = 0

    def collect_item(self, itemName, itemWeight):
        newItem = (itemName, itemWeight)
        self.items.append(newItem)
        self.itemLoad += itemWeight
        return
    