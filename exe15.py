from sys import argv
script, file_name = argv
txt = open(file_name)
print(f"Here's your file {file_name}:")
print(txt.read())
print("Type the file name again:") # above file or any type of other file.
#input(" > ") = file_name1 # Syntax erro
file_1 = input(" > ")
txt_1 = open(file_1)
print(txt_1.read())