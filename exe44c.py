class Parent():
    def override(self):
        print("PARENT override().")

    def implicit(self):
        print("PARENT implicit().")

    def altered(self):
        print("PARENT altered().")

class Child(Parent):
    def override(self):
        print("CHILD override().")

    def altered(self):
        print("CHILD,Before print altered().")
        super(Child,self).altered()
        print("CHIILD,After print altered().")

dad = Parent()
son = Child()

dad.implicit()
son.implicit() # called parent class implicit() method by using child class object.

dad.override() # called parent class method by it self object.
son.override() #  override parent class method.

dad.altered() # called parent class altered method by themsleves object.
son.altered() # called child class altered method.
    