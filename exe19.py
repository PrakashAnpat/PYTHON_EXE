def cheese_and_crackers(cheese_count, boxes_of_crackers,member = 100): # we can assign default value of formal argument in function defination.
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Toatal number of members {member}")
    print("Man that's enough for party!")
    print("Get a blanket.\n")
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
print("Or, we can use variables from our script.")
cheese = 10
crackers = 50
cheese_and_crackers(cheese, crackers)
print("We can perform maths operation inside too.")
cheese_and_crackers(10+30, 30+30) # Use match operation.
cheese_and_crackers("Prakash"+"Anpat", "Abhi"+"Phadtare") # Use string concatination.
cheese_and_crackers(0.123, 1.456) #Use floating point number.
cheese_and_crackers(cheese + 100, crackers + 200)
cheese_and_crackers("Learn", "Python") # pass string.