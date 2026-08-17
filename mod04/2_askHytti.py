hytti_input = input("Mikä hyttiluokka?\n")

hytti_clean = hytti_input.strip().casefold()
#.strip() ignore leading/trailing whitespace
#.casefold() compare case-insensitively

if hytti_clean == "lux":
    print ("Parvekkeellinen hytti yläkannella")
elif hytti_clean == "a":
    print ("Ikkunallinen hytti autokannen yläpuolella")
elif hytti_clean == "b":
    print ("ikkunaton hytti autokannen yläpuolella")
elif hytti_clean == "c":
    print ("ikkunaton hytti autokannen yläpuolella")
else:
    print("Virheellinen hyttiluokka") 