def filter_oddnumbers(list, evenList):
    list = numberList
    evenList = []
    for i in list:
        if i % 2 == 0:
            evenList.append(i)
    return (list, evenList)


numberList = 1,2,3,4,5,23,345,64,4,14,77
numberList = filter_oddnumbers(numberList, [])
print (numberList)