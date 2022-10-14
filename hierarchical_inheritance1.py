class Father():
    def __init__(self):
        print("Father class constructor.")
    def showF(self):
        print("Father class instance method.")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class constructor.")
    def showS(self):
        print("Son class instance method.")
class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter class constructor.")
    def showD(self):
        print("Daughter class instance method.")

s = Son()
s.showF()
s.showS()
print()

d = Daughter()
d.showF()
d.showD()