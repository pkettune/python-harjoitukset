pituus = float(input("Kuinka pitkä kuha? (cm)\n"))

if (pituus < 37):
    print(f"Laske takaisin järveen, anna kasvaa vielä\n{37 - pituus}cm")

else:
    print("Hyvä koko")