import math

pizzaValueList = []
pizzaCount = 0
def compare_pizzas(diameter, price):
    pizzaSize = math.pi * (diameter/2)**2
    pizzaValue = price/pizzaSize
    pizzaValueList.append(pizzaValue)

    if pizzaCount < 2:
        return
    else:
        if pizzaValueList[0] < pizzaValueList[1]:
            print("first pizza has greater value")
        elif pizzaValueList[0] == pizzaValueList[1]:
            print("Equal value!")
        else:
            print("second pizza has greater value")






while (pizzaCount < 2):
    pizzaDiameter = float(input("Diameter of the pizza? "))
    pizzaPrice = float(input("Price of the pizza? "))
    pizzaCount = pizzaCount + 1
    compare_pizzas(pizzaDiameter, pizzaPrice)









    # pizza2diameter = float(input("Diameter of the 2nd pizza? "))
    # pizza2price = float(input("Price of the 2nd pizza? "))