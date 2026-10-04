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

    rooms = {
        "k": kitchen,
        "o": livingRoom,
        "m": bedRoom,
        "t": yard,
        "v": shed
    }
    return rooms, bedRoom
