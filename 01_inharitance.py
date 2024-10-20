class employe:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")



class programmer(employe):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and the language is {self.language}")

a = employe()
b = programmer()
print(a.company, b.company)