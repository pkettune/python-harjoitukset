class Work:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class Book(Work):
    def __init__(self, work, authorFirstName, authorLastName, pages):
        self.work = work
        super().__init__(authorFirstName, authorLastName)
        self.pages = pages

    def print_information(self):
        #super().print_information()
        print(f"Name: {self.work} \nAuthor: {self.firstName} {self.lastName}\nPages:{self.pages}\n")

class Magazine(Work):
    def __init__(self, work, publisherFirstName, publisherLastName):
        self.work = work
        super().__init__(publisherFirstName, publisherLastName)

    def print_information(self):
        #super().print_information()
        print(f"Name: {self.work}\nPublisher: {self.firstName} {self.lastName}\n")

works = []
works.append(Magazine("Aku Ankka", "Aki", "Hyyppä"))
works.append(Book("Hytti n:o 6", "Rosa", "Liksom", "200"))

for w in works:
    w.print_information()