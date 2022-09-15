ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(len(ten_things)) # call len() function.
print("Wait there are not 10 things in that list.Let's fix that.")
stuff = ten_things.split(" ") # callsplit() method.
print(stuff)
print(type(stuff))
print(len(stuff))
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn","Banana","Girl","Boy"]
print(more_stuff)
while len(stuff) != 10:
    next_one = more_stuff.pop() # pop() function call.
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(stuff[1]) # Access elements by it's index no 1.
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))
