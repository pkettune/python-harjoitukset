#Sähkölaskulaskin

kulutus = float(input("sähkönkulutus kWh? "))

summa = 0

if kulutus <= 50:
    summa = kulutus * 10

elif kulutus <= 200:
    summa = 50 * 10
    summa += (kulutus - 50) * 8

elif kulutus > 200:
    summa += 50 * 10
    summa += 150 * 8
    summa += (kulutus - 200) * 6

print(summa)