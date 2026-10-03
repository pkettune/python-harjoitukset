import subprocess
import platform
import json
from player import Player
from items import Item

def start_menu(filename="save.txt"):
    while True:
        print("\nAlkuvalikko:\n'uusi' (Aloita uusi peli)\n'lataa' (Lataa tallennettu peli)\n'lopeta' (Poistu)")
        val = input("Valintasi: ")

        if val == "uusi":
            name = input("MIKÄ ON NIMESI?\n")
            age = int(input("KUINKA VANHA OLET?\n"))
            return name, age, None

        elif val == "lataa":
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    name = data.get("name", "Player")
                    age = int(data.get("age", 0))
                    player = Player(name)

                    for item in data.get("items", []):
                        player.items.append(Item(item))

                    player.itemLoad = data.get("itemLoad", 0)
                    player.location = data.get("location")
                    return name, age, player

            except FileNotFoundError:
                print("Tallennusta ei löytynyt.")
            except Exception:
                print("Tallennuksen latauksessa tapahtui virhe.")

        elif val == "lopeta":
            raise SystemExit
        else:
            print("Tuntematon valinta")

def save_game(player, age, filename="save.txt"):
    print("Tallennetaan peli.")
    try:
        file = open(filename, "w")
        data = {}
        data["name"] = player.name
        data["age"] = age
        items = []

        for item in player.items:
            items.append(item.name)
        data["items"] = items

        if player.location:
            data["location"] = player.location.name

        else:
            data["location"] = None

        data["itemLoad"] = player.itemLoad
        json.dump(data, file)
        file.close()
        print("Peli tallennettu " + filename)

    except Exception:
        print("Tiedoston käsittelyssä tapahtui virhe.")

def load_game_into(player, rooms, filename="save.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            player.name = data.get("name", player.name)
            new_age = int(data.get("age", 0))

            # restore items
            from items import Item
            player.items = []

            for item in data.get("items", []):
                player.items.append(Item(item))
            player.itemLoad = data.get("itemLoad", player.itemLoad)
            loc_name = data.get("location")

            if loc_name:
                for room in rooms.values():
                    if room.name == loc_name:
                        player.location = room
                        break

            print("Tallennus ladattu.")
            return new_age
    except FileNotFoundError:
        print("Tallennusta ei löytynyt.")
    except Exception:
        print("Tallennuksen latauksessa tapahtui virhe.")
    return None

def clear_screen():
    system = platform.system().lower()
    if system == 'windows':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)