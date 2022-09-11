# All function contains two arguments a & b & also use the string litral(f-string) formatted method.
def add(a,b): # Perform addition operation
    print(f"Addition {a} + {b} ")
    return a + b # return output value when this function call it.
def sub(a,b):
    print(f"Substraction {a} - {b} ")
    return a - b
def mul(a,b):
    print(f"Multiplication {a} * {b} ")
    return a * b
def div(a,b):
    print(f"Division {a} / {b} ")
    return a / b
def float_no(a,b):
    print(".......................")
    print("Floating number operation")
    print(f"Addition {a} + {b} ")
    print(a + b)
    print(f"Substraction {a} - {b} ")
    print(a - b)
    print(f"Multiplication {a} * {b} ")
    print(a * b)
    print(f"Division {a} / {b} ")
    print(a / b)
    print(".....................")
age = add(30, 5)
print(age)
weight = sub(70, 10)
print(weight)
height = mul(90, 2)
print(height)
iq = div(100, 2)
print(iq)
print(int(iq)) # Type casting.
float_no(25.5, 10.5)
print(f"Age: {age}, Weight: {weight}, Height: {height}, Iq: {iq}")
what = add(age, sub(height, mul(weight,div(iq,2)))) # In this line use math function
print("...........................")
print(what)
