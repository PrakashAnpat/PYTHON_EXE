from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Copying from file {from_file} to {to_file}")
in_file = open(from_file)
#print(in_file)
indata = in_file.read()
#print(indata)
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN TO continue,CTRL-c to abort.")
input()
out_file = open(to_file,"w")
out_file.write(indata)
print("Alright, all done.")
in_file.close
out_file.close