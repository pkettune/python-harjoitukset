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
        try:
            itemName = self.location.itemToFind
        except Exception:
            print("Ei kerättäviä esineitä.")
            return

        if itemName == None:
            print("Ei kerättäviä esineitä.")
            return
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
        # If room is a Room, show its name. If it's a plain string (unresolved),
        # show the string and do not try to access room attributes.
        try:
            room_name = room.name
        except Exception:
            try:
                room_name = str(room)
            except Exception:
                room_name = None

        if not self.items:
            print("Ei käytettäviä tavaroita")
        else:
            print("Tavarasi:")
            for item in self.items:
                print(item.name)
            try:
                itemToUse = input("\nMitä esinettä haluat käyttää?\n").casefold()
            except Exception:
                print("Virhe")
                return
            if itemToUse == "kivi" and room_name == "Takapiha":
                print("Rikoit ikkunan kivellä ja sait vajan oven auki")
                for item in list(self.items):
                    if item.name.casefold() == "kivi":
                        weight = item.weight or 0
                        self.itemLoad = self.itemLoad - weight
                        self.items.remove(item)
                        print("Kivi katosi jonnekin")
                        break
                self.shedIsLocked = False
            elif itemToUse == "lapio" and room_name == "Takapiha":
                print("Kaivoit kuopan ja löysit sieltä MAHTIMIEKAN!")
                if self.itemLoad > 3.05:
                    print("Mutta tavarasi painavat liikaa, etkä voi kantaa mahtimiekkaa mukanasi...")
                    print("Ainoa mahdollisuutesi on vain yrittää uudelleen")
                    return
                else:
                    self.sword = True
                    print("Mahtimiekka on nyt mukanasi!")
                    sword = items.Item("Mahtimiekka")
                    self.items.append(sword)
            elif itemToUse == "mahtimiekka" and room_name == "Ulko-ovi":
                try:
                    answer = input("Oletko valmis lähtemään levittämään tasa-arvoa? (kyllä/ei)\n").casefold()
                except Exception:
                    print("Virhe")
                    return
                if answer == "ei":
                    print("rohkeutesi ei riittänyt, hävisit pelin")
                    input("paina Enter sulkeaksesi pelin...")
                    quit()
                else:
                    print("voitit pelin")
                    input("paina Enter sulkeaksesi pelin...")
                    quit()
            elif itemToUse == "viesti":
                print("Viestissä sanotaan: 'Kaiva takapihalla'")
            elif itemToUse == "veitsi":
                print("Veitsellä ei ole käyttöä tässä pelissä, kannat sitä kuitenkin mukanasi, iäti")
            else:
                print("Et voi käyttää tätä esinettä")

    def change_name(self):
        newName = input("Uusi nimesi?\n")
        self.name = newName
        print("\nHei " + self.name)
        return

    def look_around(self):
        #except: show the string and do not try to access room attributes.
        try:
            location_name = self.location.name
        except Exception:
            location_name = str(self.location)

        print(f"Olet paikassa: {location_name}")

        try:
            item_name = self.location.itemToFind
        except Exception:
            item_name = None

        if item_name:
            print(f"Huoneessa on: {item_name}")
        else:
            print("Huoneessa ei ole mitään tärkeää")
        return
