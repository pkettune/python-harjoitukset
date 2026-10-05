import os
import json
from player import Player
from items import Item
from room import create_rooms

def intro():
    filename = "intro.txt"
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


def manual():
    filename = "ohjeet.txt"
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


def initialize_game():
    filename="save.txt"

    rooms = create_rooms()

    player, name, age = start_menu(filename, rooms)

    itemList = []
    # remove items player has from rooms, so they don't appear in the room again after loading a save.
    if player is not None:
        for item in player.items:
            for room in rooms.values():
                if room.itemToFind == item.name:
                    room.itemToFind = None

        # Resolve player's location so it is always a Room object.
        # Prefer a direct key match (e.g. 'm'). Next, try to match by room.name
        # case-insensitively. If neither works, default to the bedroom ('m').
        resolved = False
        try:
            saved_loc = player.location
            #isinstance(object, classinfo) Return True if the object argument is an instance of the classinfo argument.
            if isinstance(saved_loc, str) and rooms is not None and saved_loc in rooms:
                player.location = rooms[saved_loc]
                resolved = True
            else:
                # If the saved location is already a Room-like object, it will
                # have a .name attribute; if so, keep it. Otherwise, try
                # matching against room names (case-insensitive).
                try:
                    _ = saved_loc.name
                    resolved = True
                except Exception:
                    loc_str = str(saved_loc)
                    for room in rooms.values():
                        try:
                            if room.name.lower() == loc_str.lower():
                                player.location = room
                                resolved = True
                                break
                        except Exception:
                            continue
        except Exception:
            resolved = False

        if not resolved:
            # Fall back to bedroom if resolution failed; bedroom key is 'm'.
            try:
                bedRoom = rooms.get('m') if rooms is not None else None
                if bedRoom is not None:
                    player.location = bedRoom
            except Exception:
                # Last resort: leave player's location unchanged.
                pass

    return player, name, age, rooms, itemList


def start_menu(filename="save.txt", rooms=None):
    while True:
        clear_screen()
        print("\nAlkuvalikko:")
        print("'uusi' - Aloita uusi peli")
        if os.path.exists(filename):
            print("'lataa' - Lataa tallennettu peli")
            print("'poista' - Poista tallennus")
        print("'lopeta' - Poistu")
        try:
            choice = input("Valintasi: ")
        except Exception:
            print("\nVirheellinen valinta.")
        if choice == "uusi":
            return new_game()
        elif choice == "lataa":
            # Pass rooms so load_game can resolve location and restore room state
            return load_game(filename, rooms=rooms)

        elif choice == "poista":
            remove_save(filename)
            continue

        elif choice == "lopeta":
            exit()
        else:
            print("Virhe")


def new_game():
    name = input("MIKÄ ON NIMESI?\n")
    while True:
        try:
            age = int(input("KUINKA VANHA OLET?\n"))
            break
        except ValueError:
            print("Virheellinen ikä.")
    clear_screen()
    intro()
    input("\nPaina enter jatkaaksesi...")
    clear_screen()
    manual()
    input("\nPaina enter jatkaaksesi...")
    # None for new game, since no player object exists yet. The caller will create it.
    return None, name, age


def save_game(player, age, rooms=None):
    filename="save.txt"

    #Prefer storing the room key from the rooms mapping when possible.
    #Fall back to room.name or the raw player.location value.

    try:
        location_value = None
        if rooms is not None and player is not None and player.location is not None:
            for key, room_obj in rooms.items():
                if room_obj is player.location:
                    location_value = key
                    break
                try:
                    if str(room_obj.name).casefold() == str(player.location).casefold():
                        location_value = key
                        break
                except Exception:
                    pass

        if location_value is None:
            try:
                location_value = player.location.name
            except Exception:
                location_value = player.location

        # Also save room states (which item is in each room) if rooms mapping is provided.
        rooms_state = None
        if rooms is not None:
            rooms_state = {key: (room.itemToFind if room.itemToFind is not None else None) for key, room in rooms.items()}

        data = {
            "name": player.name,
            "age": age,
            "items": [item.name for item in player.items],
            "location": location_value,
            "itemLoad": player.itemLoad,
            "shedIsLocked": player.shedIsLocked,
            "sword": player.sword,
        }

        if rooms_state is not None:
            data["rooms"] = rooms_state
#https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print("Save written to " + filename)

    except IOError:
        print("Error saving game")


def remove_save(filename="save.txt"):
    try:
        os.remove(filename)
        print("Tallennus poistettu: " + filename)
    except FileNotFoundError:
        print("Tallennusta ei löytynyt")
    except IOError:
        print("Virhe poistettaessa tallennusta")


def load_game(filename="save.txt", rooms=None):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        player = Player(data.get("name", "Player"))
        name = data.get("name", "Player")
        age = int(data.get("age", 0))
        player.location = data.get("location")

        for item_name in data.get("items", []):
            player.items.append(Item(item_name))

        total = 0
        for item in player.items:
            if item.weight is not None:
                total = total + item.weight
        player.itemLoad = total

        player.shedIsLocked = data.get("shedIsLocked", True)
        player.sword = data.get("sword", False)

        # If rooms mapping provided and saved rooms state exists, restore it.
        saved_rooms = data.get("rooms")
        if rooms is not None and isinstance(saved_rooms, dict):
            for key, value in saved_rooms.items():
                try:
                    if key in rooms:
                        rooms[key].itemToFind = value
                except Exception:
                    continue

        # If rooms mapping provided, resolve player's location to a Room
        # object immediately (key or room.name). This makes the returned
        # player.location usable by the game without further resolution.
        if rooms is not None:
            saved_loc = player.location
            if isinstance(saved_loc, str) and saved_loc in rooms:
                player.location = rooms[saved_loc]
            else:
                loc_str = str(saved_loc)
                for room in rooms.values():
                    try:
                        if room.name.lower() == loc_str.lower():
                            player.location = room
                            break
                    except Exception:
                        continue

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
