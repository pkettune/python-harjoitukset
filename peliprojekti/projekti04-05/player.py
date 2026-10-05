import items

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = None
        self.itemLoad = 0
        self.shedIsLocked = True
        self.sword = False

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
        print("Keräsit esineen: " + itemName)
        return

    def show_items(self):
        if not self.items:
            print("Ei esineitä")
            return
        for item in self.items:
            print(item.name)
        return

    def use_item(self, room):
        if not self.items:
            print("Ei käytettäviä tavaroita")
        else:
            print("Tavarasi:\n")
            for item in self.items:
                print(item.name)
            itemToUse = input("Mitä esinettä haluat käyttää?\n").casefold()
            print (itemToUse)
            if itemToUse == "kivi" and room.name == "Takapiha":
                print("Rikoit ikkunan kivellä ja sait vajan oven auki")
                self.shedIsLocked = False
                #return self.shedIsLocked
            elif itemToUse == "lapio" and room.name == "Takapiha":
                self.sword = True
                print("Kaivoit kuopan ja löysit sieltä MAHTIMIEKAN!")
                sword = items.Item("Mahtimiekka")
                self.items.append(sword)
            elif itemToUse == "mahtimiekka" and room.name == "Ulko-ovi":
                answer = input("Oletko valmis lähtemään levittämään tasa-arvoa? (kyllä/ei)").casefold()
                if answer == "ei":
                    print("rohkeutesi ei riittänyt, hävisit pelin")
                    input("paina Enter sulkeaksesi pelin...")
                    quit()
                else:
                    print("voitit pelin")
                    input("paina Enter sulkeaksesi pelin...")
                    quit()
            else:
                print("Väärä komento")

    def change_name(self):
        newName = input("Uusi nimesi?\n")
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

    def end_game(self):
        pass
