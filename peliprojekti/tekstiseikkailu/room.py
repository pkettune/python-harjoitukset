class Room:
    def __init__(self, name, itemToFind):
        self.name = name
        self.itemToFind = itemToFind


def create_rooms():
    kitchen = Room("Keittiö", "Veitsi")
    livingRoom = Room("Olohuone", "Viesti")
    bedRoom = Room("Makuuhuone", "Kivi")
    yard = Room("Takapiha", None)
    shed = Room("Vaja", "Lapio")
    door = Room("Ulko-ovi", None)

    rooms = {
        "k": kitchen,
        "o": livingRoom,
        "m": bedRoom,
        "t": yard,
        "v": shed,
        "u": door
    }

    return rooms
