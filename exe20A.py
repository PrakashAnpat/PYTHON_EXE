from sys import argv
script, file = argv
def read_file(f): # For reading file
    print(f.read())
def pos(f): # For file current postion
    print(f.tell())
def set_pos(s): # For set the file position
    print(s.seek(0))
def count_and_line(count, file): # For line no count & read line
    print(count,file.readline())

current = open(file)
read_file(current)
pos(current)
set_pos(current)

current_line = 1
count_and_line(current_line, current)
current_line = current_line + 1
count_and_line(current_line, current)
current_line = current_line + 1
count_and_line(current_line, current)

# current_line = 2
# count_and_line(current_line,current)
# current_line = current_line + 1
# count_and_line(current_line, current)
# current_line = current_line + 1
# count_and_line(current_line, current)