airports = {"EFHK": "Helsinki-Vantaa",
           "EFHV": "Hyvinkää Airport",
           "EFKS": "Kuusamo Airport",
           "EFTP": "Tampere-Pirkkala Airport"
           }

def insert_new_airport():
    icao_input = input("ICAO-code? ")
    name_input = input("Name of the airport? ")
    airports[icao_input] = name_input

def find_airport():
    icao_code = input("Search by ICAO ")
    if icao_code in airports:
        print (f"\nAirport {icao_code} is {airports[icao_code]}")

while True:
    user_input = input("\nWhat you want to do?\n\nAdd new airport (add)\nFind airport from database (find)\nQuit (q)\n\n")

    if user_input == "new":
        insert_new_airport()

    elif user_input == "find":
        find_airport()

    elif user_input == "q":
        print(airports)
        break
    
    else:
        print("Invalid input!")