no = [1,2,3,4,5] # creating numeric list.
fruits = ["apple", "mango", "banana", "oranges", "custard-apple"] # creating string list.
mix = [10, "a", 20, "b", 30, "c", 40, "d"] # numeric & string means mixed list.
print(no)
print(fruits)
print(mix)
for num in no: # Use for loop.
    print(f"This is number: {num}")
for fruit in fruits:
    print(f"Fruits name: {fruit}")
for i in mix:
    print(f"Mixed list: {i}")
empty_list = list() # Also create list using list() function.
print("Empty list:",empty_list)
for i in range(0, 6): # Use range function for creating sequence of numbers.
    print(f"Range for index: {i}")
    empty_list.append(i) # use append() function for add elements in specified empty list.  
print(empty_list)    
# elements = [] # Creating empty list.
# print(elements)
# for i in range(0, 6):
#     i = int(input("Enter element:"))    
#     elements.append(i) # append is a function that list understand.
# print(elements)
# for i in elements: # Accessing elements by this for loop.
#     print(i)
# a = range(0, 5) # range() function assign to variable.
# print(a)
# print("Two dimensional list")
# b = [[1,2,3,4,5],[6,7,8,9,0]] # Creating two dimensional list.
# print(b)
# print(type(b))