class employe:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e = employe()
e.a = 45

e.show()