i = 0 
numbers = []
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
print("The numbers: ")
for num in numbers:
    print(num)
empty = []
def function_1(no):
    j = 0
    while j < no:
        empty.append(j)
        j += 1
    return empty
user = int(input("Enter number of elements:"))        
updated_list = function_1(user)       
print(updated_list)
# for i in updated_list:
#     print(i)