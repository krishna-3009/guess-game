class employe:
    company = "ITC"
    name = "defalt name"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.company}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of all the language here is your language: {self.language}")

class programmer(employe,coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and the language is {self.language}")

a = employe()
b = programmer()
print(a.company, b.company)

b.show()
b.printlanguage()
b.showlanguage()