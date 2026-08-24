while (input):
    inches = float(input("Inches?\n"))
    cm = inches * 2.54
    if (inches < 0):
        break
    else:
        print(f"{cm} cm")