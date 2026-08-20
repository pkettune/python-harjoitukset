seasons = ("winter", "winter", "spring", "spring", "spring",
           "summer", "summer", "summer", "fall", "fall", "fall", "winter" )

numberOfMonth = int(input("Give number of a month (1-12) "))

season = seasons[numberOfMonth - 1]

print(f"Season is {season}")