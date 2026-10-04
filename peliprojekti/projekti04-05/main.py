import json
import random
from player import Player
from items import Item
from tools import clear_screen, new_game, save_game, load_game, initialize_game

komento = ""
player = None

player, name, age, rooms, bedRoom, itemList = initialize_game()

while komento != "lopeta":
    if age < 12:
        print("alaikäinen")
        break

    if age >= 12:
        clear_screen()
        print("\nTervetuloa " + name)
        if player is None:
            player = Player(name)
        if not player.location:
            player.location = bedRoom

        while True:
            print("\nKomennot:\n'a(add item)'\n's(show items)'\n'l(look around)'\n'nimi(muuta nimesi)'\n'm(move)'\n'tallenna(tallenna peli)'\n'lataa(lataa peli)'\n'lopeta'\n")
            komento = input("Anna komento: ")
            clear_screen()
            if komento == "a":
                new_item = player.collect_item()
                if new_item:
                    itemList.append(new_item)
            elif komento == "s":
                print("Hallussasi on:")
                player.show_items()
            elif komento == "l":
                player.look_around()
            elif komento == "m":
                newRoom = input("Minne haluat mennä?\n\nKeittiö(k)\nMakuuhuone(m)\nOlohuone(o)\nTakapiha(t)\nVaja(v)): ")
                #https://note.nkmk.me/en/python-dict-get/
                room = rooms.get(newRoom)
                if room:
                    player.move(room)
                else:
                    print("Unknown room")
            elif komento == "nimi":
                player.change_name()
            elif komento == "tallenna":
                save_game(player, age)
            elif komento == "lataa":
                new_age = load_game(player=player, rooms=rooms)
                if new_age is not None:
                    age = new_age
            elif komento == "lopeta":
                break
            else:
                print("\nVÄÄRÄ KOMENTO!")
