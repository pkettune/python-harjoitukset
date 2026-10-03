class Room:
    def __init__(self, name, itemToFind):
        self.name = name
        self.itemToFind = itemToFind


def create_rooms():
    """Create and return the game's rooms and a default starting room."""
    kitchen = Room("Keittiö", "Knife")
    livingRoom = Room("Olohuone", "Note")
    bedRoom = Room("Makuuhuone", "Rock")
    yard = Room("Yard", None)
    shed = Room("Shed", "Knife")

    rooms = {
        "k": kitchen,
        "o": livingRoom,
        "m": bedRoom,
        "t": yard,
        "v": shed
    }
    return rooms, bedRoom
