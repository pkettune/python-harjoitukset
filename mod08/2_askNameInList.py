names = set()
name_input = input("Syötä ensimmäinen nimi ")
names.add(name_input)

while (name_input != ""):
    name_input = input("Tarkista löytyykö nimi joukosta ")
    if name_input == "":
        break
    if name_input in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(name_input)

for name in names:
    print(name)