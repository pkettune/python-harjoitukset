input_raw = int(input("What year is it?\n"))

if (input_raw % 4 == 0 or input_raw % 400 == 0):
    print("It's a leap year!")
else:
    print("It's not a leap year :(")