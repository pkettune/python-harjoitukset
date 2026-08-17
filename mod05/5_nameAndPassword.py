while(input):
    name = input("User Name:\n")
    password = input("Password:\n")

    if (name == "python" and password == "rules"):
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")