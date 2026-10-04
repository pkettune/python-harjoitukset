import subprocess
import platform
import os
import json
from player import Player
from items import Item
from room import create_rooms


def intro(filename="intro.txt"):
    try:
        base = os.path.dirname(__file__)
        path = os.path.join(base, filename)
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
        print(text)
    except FileNotFoundError:
        print("Intro file not found.")
    except IOError:
        print("Error reading intro file.")


def manual(filename="ohjeet.txt"):
    try:
        base = os.path.dirname(__file__)
        path = os.path.join(base, filename)
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
        print(text)
    except FileNotFoundError:
        print("Manual file not found.")
    except IOError:
        print("Error reading manual file.")


def initialize_game(filename="save.txt"):
    player, name, age = start_menu(filename)
    rooms, bedRoom = create_rooms()
    itemList = []

    if player is not None:
        # remove items from rooms that the player already has
        for item in player.items:
            for room in rooms.values():
                if room.itemToFind == item.name:
                    room.itemToFind = None

        for room in rooms.values():
            if player.location == room or player.location == room.name:
                player.location = room
                break

    return player, name, age, rooms, bedRoom, itemList


def start_menu(filename="save.txt"):
    while True:
        clear_screen()
        print("\nAlkuvalikko:")
        print("'uusi' - Aloita uusi peli")
        if os.path.exists(filename):
            print("'lataa' - Lataa tallennettu peli")
        print("'lopeta' - Poistu")

        choice = input("Valintasi: ")
        if choice == "uusi":
            return new_game()

        elif choice == "lataa":
            result = load_game(filename)
            if result:
                return result

        elif choice == "lopeta":
            exit()
        else:
            print("Unknown choice")


def new_game():
    name = input("MIKÄ ON NIMESI?\n")
    age = int(input("KUINKA VANHA OLET?\n"))
    clear_screen()
    intro()
    print("\nPaina enter jatkaaksesi...")
    input("")
    clear_screen()
    manual()
    print("\nPaina enter jatkaaksesi...")
    input("")
    # return player first (None for a new game), then name and age
    return None, name, age


def save_game(player, age, filename="save.txt"):
    try:
        data = {}
        data["name"] = player.name
        data["age"] = age
        items = []
        for item in player.items:
            items.append(item.name)
        data["items"] = items
        data["location"] = player.location.name
        data["itemLoad"] = player.itemLoad
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file)
        print("Save written to " + filename)
    except IOError:
        print("Error saving game")


def load_game(filename="save.txt", player=None, rooms=None):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        player = Player(data.get("name", "Player"))
        name = data.get("name", "Player")
        age = int(data.get("age", 0))
        location = data.get("location")
        player.itemLoad = data.get("itemLoad", 0)

        # If a rooms mapping was provided, try to resolve the saved location to a Room.
        # Accept either a room key (e.g. 'm') or a room.name (case-insensitive).
        if location and rooms:
            # Direct key lookup (saved as room key)
            if isinstance(location, str) and location in rooms:
                player.location = rooms[location]
            else:
                # Match by room.name (case-insensitive)
                loc_str = str(location)
                for room in rooms.values():
                    if isinstance(room.name, str) and room.name.lower() == loc_str.lower():
                        player.location = room
                        break
        else:
            # Fallback: keep whatever was stored (string or None)
            player.location = location

        for item in data.get("items", []):
            player.items.append(Item(item))

        print("Save loaded")
        return player, name, age

    except FileNotFoundError:
        print("Save not found")
    except IOError:
        print("Error loading save")
    return None


def clear_screen():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        pass
