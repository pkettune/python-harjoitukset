import json
import random
from player import Player
from room import Room
from items import Item
from tools import clear_screen

name = input("MIKÄ ON NIMESI?\n")
age = int(input("KUINKA VANHA OLET?\n"))
komento = ""

itemList = []

kitchen = Room("Keittiö", "Knife")
livingRoom = Room("Olohuone", "Note")
bedRoom = Room("Makuuhuone", "Rock")
yard = Room("Yard", None)
shed = Room("Shed", "Knife")

rooms = {
    "k": kitchen,
    "o": livingRoom,
    "m": bedRoom,
    "p": yard,
    "v": shed
}

def save_game(self):
    print("Tallennetaan peli.")
    try:
        with open("mod13/save.txt", "w") as file:
            data = {"age": self.age, "points": self.points}
            json.dump(data, file)
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")

def load_game(self):
    try:
        with open("mod13/save.txt", "r") as file:
            data = json.load(file)
            #print("Ladattu tallennusdata:", data)
            self.points = data["points"]
            self.age = data["age"]
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")

while komento != "lopeta":
    if age < 12:
        print("alaikäinen")
        break
    if age >= 12:
        print("\nTervetuloa " + name)
        player = Player(name)
        player.location = bedRoom
        clear_screen()

        while True:
            print("\nKomennot:\n'a(add item)'\n's(show items)'\n'l(look around)'\n'name(change name)'\n'm(move)'\n'lopeta'\n")
            komento = input("Anna komento: ")
            if komento == "a":
                new_item = player.collect_item()
                if new_item:
                    itemList.append(new_item)
            elif komento == "s":
                player.show_items()
            elif komento == "l":
                player.look_around()
            elif komento == "name":
                player.change_name()
            elif komento == "m":
                clear_screen()
                newRoom = input("Where to? (keittiö(k)/makuuhuone(m)/olohuone(o)/takapiha(t)/vaja(v)): ")
                #https://note.nkmk.me/en/python-dict-get/
                room = rooms.get(newRoom)
                if room:
                    player.move(room)
                else:
                    print("Unknown room")
            elif komento == "lopeta":
                break
            else:
                print("\nWRONG INPUT!")
