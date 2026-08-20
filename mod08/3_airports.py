spring = (3, 4, 5)
summer = (6, 7, 8)
fall = (9, 10, 11)
winter = (12, 1, 2)

seasons = [
    {
        "name": "spring",
        "monthNumber" : (3, 4, 5)
    },
    {
        "name": "summer",
        "monthNumber" : (6, 7, 8)
    },
    {
        "name": "fall",
        "monthNumber" : (9, 10, 11)
    },
    {
        "name": "winter",
        "monthNumber" : (12, 1, 2)
    }
]

numberOfMonth = int(input("Give number of a month (1-12)"))

season = seasons[numberOfMonth]

print(f"Season is {season}")
