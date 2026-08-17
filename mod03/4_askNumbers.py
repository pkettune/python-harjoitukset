import math

a_str = input("Anna ensimmäinen numero\n")
b_str = input("Anna toinen numero\n")
c_str = input("Anna kolmas numero\n")

a = float(a_str)
b = float (b_str)
c = float (c_str)

summa = a + b + c
tulo = a * b * c
keskiarvo = (a + b + c) / 3

print (f" summa on = {summa}\n tulo on = {tulo}\n keskiarvo on = {keskiarvo:.2}")