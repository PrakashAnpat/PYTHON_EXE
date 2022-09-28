class Parent(object):
    def altered(self):
        print("PARENT altered().")
class Child(Parent):
    def altered(self):
        print("CHILD before print altered.")
        super(Child,self).altered() # called parent class altered method.
        print("CHILD after print altered.")
dad = Parent()
son = Child()
dad.altered() # called parent class instance method using it self object.
son.altered() # called child class instance method using it self object.