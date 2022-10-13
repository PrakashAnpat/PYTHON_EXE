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
class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("Grandson class constructor.")
    def showG(self):
        print("Grandson class instance method.")

g = GrandSon()
g.showF()
g.showS()
g.showG()