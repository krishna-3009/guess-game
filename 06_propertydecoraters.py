class employe:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employe()
e.a = 45

e.name = "harry khan"
print(e.fname,e.lname)

e.show()