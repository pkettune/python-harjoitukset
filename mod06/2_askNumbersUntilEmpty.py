numberList = []

askedNumbers = input("Give me a number ")

while (askedNumbers != ""):
    numberList.append(int(askedNumbers))#TÄNNE PITI LAITTAA INT, MUUTEN SORT EI TOIMI OIKEIN
    askedNumbers = input("Give me a number ")

numberList.sort(reverse=True)

for luku in range(0,5):
    print (numberList[luku])