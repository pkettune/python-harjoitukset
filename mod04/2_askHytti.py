hytti_input = input("Mikä hyttiluokka?\n")

hytti = hytti_input.strip().casefold()
#.strip() ignore leading/trailing whitespace
#.casefold() compare case-insensitively

if hytti == "lux":
    print ("Parvekkeellinen hytti yläkannella")
elif hytti == "a":
    print ("Ikkunallinen hytti autokannen yläpuolella")
elif hytti == "b":
    print ("ikkunaton hytti autokannen yläpuolella")
elif hytti == "c":
    print ("ikkunaton hytti autokannen yläpuolella")
else:
    print("Virheellinen hyttiluokka") 