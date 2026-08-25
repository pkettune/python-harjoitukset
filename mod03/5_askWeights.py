import math

leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

luotiPaino = 13.3
naulaPaino = 32 * luotiPaino
leiviskaPaino = 20 * naulaPaino

kokonaispaino = luotiPaino * luodit + naulaPaino * naulat + leiviskaPaino * leiviskat
kilot = int(kokonaispaino / 1000)
# TAI kilot = kokonaispaino // 1000
grammat = kokonaispaino % 1000
print (f"Massa nykymittojen mukaan:\n{kilot} kilogrammaa ja {grammat:3.2f} grammaa.")


#leiviskä = 20 naulaa = 640 luotia = 640 * 13.3 grammaa
#naulat = 32 luotia = 32 * 13.3 grammaa
#luodit = 13.3 grammaa