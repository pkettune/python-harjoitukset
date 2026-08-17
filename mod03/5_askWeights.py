import math

leiviskat_str = input("Anna leiviskät.\n")
naulat_str = input("Anna naulat.\n")
luodit_str = input("Anna luodit.\n")

luoti = float(13.3)
naula = float(luoti * 32)
leiviska = float(naula * 20)

luodit = float(luodit_str) * 13.3
naulat = float(naulat_str) * (luoti * 32)
leiviskat = float(leiviskat_str) * (naula * 20)

kokonaispaino = luodit + naulat + leiviskat
kilot = int(kokonaispaino / 1000)
grammat = float (kokonaispaino % 1000)
print (f"Massa nykymittojen mukaan:\n{kilot} kilogrammaa ja {grammat:3.2f} grammaa.")


#leiviskä = 20 naulaa = 640 luotia = 640 * 13.3 grammaa
#naulat = 32 luotia = 32 * 13.3 grammaa
#luodit = 13.3 grammaa

