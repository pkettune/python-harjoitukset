while (input):
    input_raw = float(input("Inches?\n"))
    cm = input_raw * 2.54
    if (input_raw < 0):
        break
    else:
        print(f"{cm} cm")