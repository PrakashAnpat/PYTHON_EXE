from sys import argv
script, input_file = argv
def print_all(f):
    print(f.read()) 
def rewind(f):
    f.seek(0) 
"""The seek() method sets the current file position in a file stream. Thhe seek() method also 
returns the new position. Sntax:- file.seek(offset)"""    
def print_a_line(line_count, f):
    print(line_count, f.readline()) # readline() returns one line from the file.
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
#print(current_line)
print_a_line(current_line, current_file)
#print(current_line)
current_line = current_line + 1
#print(current_line)
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)