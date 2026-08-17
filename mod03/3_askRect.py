import math

kantaStr = input("Kannan pituus (cm)?\n")
korkeusStr = input("Korkeus (cm)?\n")

kanta = float(kantaStr)
korkeus = float(korkeusStr)

piiri = float(kanta*2 + korkeus*2)
area = float(kanta * korkeus)

print (f"piiri on {piiri:.2f}cm")
print (f"pinta-ala on {area:.2f}cm²")