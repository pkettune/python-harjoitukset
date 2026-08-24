numberList = []

askedNumbers = input("Give me a number ")

while (askedNumbers != ""):
    numberList.append(askedNumbers)
    askedNumbers = input("Give me a number ")

numberList.sort(reverse=True)

for luku in range(0,5):
    print (numberList[luku])