animals = ["bear", "peacock", "kangaroo", "whale","platypus", "zebra"] # creating list.
print(animals)
print("Accessing elements of list by it's index number.")
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
print(animals[4])
print(animals[5])
print("Accessing list elements using for loop")
for element in animals:
    print(element)
print("Using index number")
for i in range(len(animals)):
    print(i, "=", animals[i])