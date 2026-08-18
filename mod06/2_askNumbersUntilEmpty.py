numberList = []

askedNumbers = input("Give me a number")

while (askedNumbers != ""):
    numberList.append(askedNumbers)
    print(askedNumbers)
    askedNumbers = input("Give me a number")

#https://stackoverflow.com/questions/25374190/how-to-sort-an-integer-list-in-python-in-descending-order
numberList.sort(key=int,reverse=True)

#for-looppia käyttäen
i = 0
for luku in range(0,5):
    print (numberList[i])
    i = i + 1

##ilman for-looppia
#print (numberList[0:5])