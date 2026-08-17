pituus_str = input("Kuinka pitkä kuha? (cm)\n")
pituus = float(pituus_str)

if (pituus < 37):
    print(f"Laske takaisin järveen, anna kasvaa vielä\n{37 - pituus}cm")

else:
    print("Hyvä koko")