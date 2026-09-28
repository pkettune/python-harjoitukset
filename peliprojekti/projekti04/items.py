
item_list = [
    {
        "name": "Knife",
        "weight": 1.2
    },
    {
        "name": "Rock",
        "weight": 0.3
    },
    {   "name": "Note",
        "weight": 0.05
    }
]

class Item():
    def __init__(self, name):
        self.name = name
        for item in item_list:
            if item["name"] == name:
                self.weight = item["weight"]
        print (name)
        print (self.weight)
        return f"{self.name}, {self.weight}"

    def show_items(self, itemList):
        for item in itemList:
            print(item)

#print (Item("Note"))