class Parent():
    def __init__(self):     # constructor
        print("Parent constructor")
        self.name = "Python"
    def get_var(self):
        print(self.name)
class Child(Parent):
    def disp(self):
        print("Child class instance method")

son = Child()
son.get_var()
son.disp()
print()
############################################################
class Father():
    def __init__(self):   # Super class constructor
        print("Father class constructor.")
        self.a = 10
    def get_val(self):
        print(self.a)
class Son(Father):
    def __init__(self):  # Sub class constructor
        #super().__init__()  # Use super method
        super(Son,self).__init__() # another type of using super metod.
        print("Son class constructor.")
        self.b = 20
    def get_var(self):
        print(self.b)
s = Son()
s.get_var()
s.get_val()   