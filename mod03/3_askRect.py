kanta = float(input("Kannan pituus (cm)?\n"))
korkeus = float(input("Korkeus (cm)?\n"))

piiri = kanta*2 + korkeus*2
area = kanta * korkeus

print (f"piiri on {piiri:.2f}cm")
print (f"pinta-ala on {area:.2f}cm²")