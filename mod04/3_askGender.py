gender_raw = input("What is your gender at birth? (m or f)\n")
hemoglobin = int(input("What is your hemoglobin (g/l)\n"))

gender = gender_raw.strip().casefold()

if (gender == "m") and (hemoglobin < 134):
    print("low")
elif (195 >= hemoglobin >= 134):
    print("normal")
else:
    print("high")

if (gender == "f") and (hemoglobin < 117):
    print("low")
elif (175 >= hemoglobin >= 117):
    print("normal")
else:
    print("high")