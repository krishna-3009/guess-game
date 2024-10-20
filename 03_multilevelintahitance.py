class emplye:
    a = 2

class programmer(emplye):
    b = 1

class manager(programmer):
    c=3

o = emplye()
print(o.a)

o = programmer()
print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)