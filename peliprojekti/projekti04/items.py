item_list = [
    {"name": "Knife", "weight": 1.2},
    {"name": "Rock", "weight": 0.3},
    {"name": "Note", "weight": 0.05},
    {"name": "Shovel", "weight": 2.0}
]

class Item():
    def __init__(self, name):
        self.name = name
        self.weight = None
        for item in item_list:
            if item["name"] == name:
                self.weight = item["weight"]