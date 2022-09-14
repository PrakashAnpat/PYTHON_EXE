"""The if..elif..else statement is used when we need to check multiple conditions."""
people = 30
cars = 40
trucks = 15
if cars > people: # if conditional statement.
    print("We should take the cars.")
elif cars < people: # elif is short for else if.
    print("We should not take the cars.")
else:
    print("We can't decide.")
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cant't decide.")
if people > trucks:
    print("Alright, let's just take the truck's.")
else:
    print("Fine,let's stay home then.")
print("...........................................")
num = 1122
if 9 < num < 99:
    print("Two digit number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number")
else:
    print("number is <= 9 or >= 9999")