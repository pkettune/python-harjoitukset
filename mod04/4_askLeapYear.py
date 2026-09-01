year = int(input("What year is it?\n"))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("It's a leap year!")
else:
    print("It's not a leap year :(")