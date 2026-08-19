import math

def gas_converter(gallons):
    if (gallons < 0):
        return
    liters = gallons * 3.785
    return liters

gallonsInput = 0

while(gallonsInput >= 0):
    gallonsInput = int(input("How many gallons? "))
    print (gas_converter(gallonsInput))