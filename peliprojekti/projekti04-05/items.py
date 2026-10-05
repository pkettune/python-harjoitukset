item_list = [
    {"name": "Veitsi", "weight": 1.2},
    {"name": "Kivi", "weight": 0.3},
    {"name": "Viesti", "weight": 0.05},
    {"name": "Lapio", "weight": 3.0},
    {"name": "Mahtimiekka", "weight": 6.0}
]


class Item():
    def __init__(self, name):
        self.name = name
        self.weight = None
        for item in item_list:
            if item["name"] == name:
                self.weight = item["weight"]
