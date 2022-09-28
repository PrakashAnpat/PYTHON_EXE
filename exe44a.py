class Parent(object):
    def implicit(self):
        print("PARENT class implicit() instance method.")
class Child(Parent):
    pass
dad = Parent() # creating instance of Parent class.
son = Child()  # creating instance of Child class.
dad.implicit() # called instance implicit() method of Parent class.
son.implicit() # called instance implicit() method of Parent class by using child class object.

class Father():
    def override(self):
        print("Father override().")
class Son(Father):
    def override(self):
        print("Son override().")
dad = Father()
son = Son()
dad.override() # called instance method of father class.
son.override() # called instance method of Son class.Child overrides that function by defining its own version.