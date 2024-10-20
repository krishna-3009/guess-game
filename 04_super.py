class emplye:
    def __init__(self):
        print("constructor of emplye")
    a = 2

class programmer(emplye):
    def __init__(self):
        print("constructor of programmer")
    b = 1

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c=3

o = emplye()
print(o.a)

o = programmer()
print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)