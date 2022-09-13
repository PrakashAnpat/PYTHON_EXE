print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')# Wen we have to use one "\"(backslach),then at that time use double "\\"(backslach).
print('\n newlines and \t tabs.')# "\n" takes output to the new line & "\t" takes one tab between string.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)     
print("--------------")
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}") # Use f-string litral string format method.
def secreat_formula(started): # Function define
    jelly_beans =started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates # Returns values to the calling defination.
start_point = 10000
values = secreat_formula(start_point)
print("Return values stored in one variable :",values) # In the form of tuple.
print(type(values))
beans, jars, creates = secreat_formula(start_point) # Passing actual parameter to the formal parameter.
print("With a staring point of: {}".format(start_point)) # Use string format method.
print(f"we'd have {beans} beans, {jars} jars, {creates} creates.")
start = start_point / 10
print("We can also do that this way.")
formula = secreat_formula(start) # All returned values from the function stored in one variable in the form of tuple.
print(formula)
print(type(formula)) #prints the type of data.
print("We'd have {} beans, {} jars, and {} creates.".format(*formula)) # Use function variable length argument.