class Father():
    def __init__(self,n):
        self.name = n
        print("Father class constructor.")
    def showF(self):
        print("Father class instance method.")
class Son(Father):
    def __init__(self, n,a):
        super().__init__(n)
        self.age = a
        print("Son class constructor.")
    def showS(self):
        print("Son class instance method.")
class GrandSon(Son):
    def __init__(self, n, a, s):
        super().__init__(n, a)
        self.salary = s
        print("Grandson class constructor.")
    def showG(self):
        print("Grandson class instance method.")
        print("Name:",self.name,"Age:",self.age,"Salary:",self.salary)
g = GrandSon("Prakash",26,10000)
g.showF()
g.showS()
g.showG()