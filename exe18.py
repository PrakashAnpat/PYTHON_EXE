def two(*val): # variable length argument.
#    arg1, arg2 = args
    print(f"arg1: {val}, arg2: {val}")
    print(f"arg1: {val[0]}, arg2: {val[1]}")
def two_again(arg1, arg2): # Positional argument.
    print(f"arg1: {arg1}, arg2: {arg2}")
def one(arg1):
    print(f"arg: {arg1}")
def none():
    print("I got nothing")
two("zed","shaw")
two_again("zed","shaw")
one("First!")
none()
def fun_name(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} arg2: {arg2}")
def fun_name1(*abc):
    val1, val2, val3 = abc
    print(f"val1: {val1}, val2: {val2}, vla3: {val3}") 
fun_name(10.55, 20.11)
fun_name1(1,2,3)
  
