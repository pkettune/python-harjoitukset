first_number = True

while (input):
    input_raw = input("Insert number\n")

    if (input_raw == ""):
        print(f"{smallest} {biggest}")
        break
    input_number = float(input_raw)

    if (first_number == True):
        smallest = input_number
        biggest = input_number
        first_number = False

    if (input_number >= biggest):
        biggest = input_number

    if (input_number <= smallest):
        smallest = input_number