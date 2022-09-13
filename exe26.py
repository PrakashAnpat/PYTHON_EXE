from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
script, filename = argv
txt = open(filename)
print("Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
print(".................................................................................")
print('Let\'s practice everything.') # Missing forward slach.
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # 
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
five = 10 - 2 + 3 
print(f"This should be five: {five}")
def secret_formula(started): # Missing colon.
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # Missing division symbol.
    return jelly_beans, jars, crates
start_point = 10000
beans, jars, creats = secret_formula(start_point)
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {creats} crates.") # Spelling mistake
start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
print(".........................................................................................")
people = 20
cats = 30 # Spelling mistake.
dogs = 15
if people < cats:
    print ("Too many cats! The world is doomed!")# Missing parenthesis.
if people < cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs: # Missing colon.
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs: # Missing colon.
    print("People are less than or equal to dogs.")# Missing double quotes.
if people == dogs: # Comparison operator missing.
    print("People are dogs.")





