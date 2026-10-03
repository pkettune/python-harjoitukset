import json
import random
from player import Player
from room import create_rooms
from items import Item
from tools import clear_screen, start_menu, save_game, load_game_into

komento = ""
player = None

# Start menu: uusi (new) or lataa (load)
name, age, player = start_menu()
# create fresh world
rooms, bedRoom = create_rooms()
# if we loaded a player, remove picked items from rooms and resolve location
if player is not None:
    # clear room items that player already has
    for item in player.items:
        for value in rooms.values():
            if value.itemToFind == item.name:
                value.itemToFind = None

    # resolve saved location: player.location may already be a Room object or a saved name
    for r in rooms.values():
        if player.location == r or player.location == r.name:
            player.location = r
            break

itemList = []

while komento != "lopeta":
    if age < 12:
        print("alaikäinen")
        break
    if age >= 12:
        print("\nTervetuloa " + name)
        if player is None:
            player = Player(name)
        if not player.location:
            player.location = bedRoom
        clear_screen()

        while True:
            print("\nKomennot:\n'a(add item)'\n's(show items)'\n'l(look around)'\n'name(change name)'\n'm(move)'\n'save(save game)'\n'load(load game)'\n'lopeta'\n")
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
            elif komento == "save":
                save_game(player, age)
            elif komento == "load":
                new_age = load_game_into(player, rooms)
                if new_age is not None:
                    age = new_age
            elif komento == "lopeta":
                break
            else:
                print("\nWRONG INPUT!")
