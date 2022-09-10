from sys import argv
from os.path import exists
script, onefile, tofile = argv
inone = open(onefile)
data = inone.read()
print(len(data))
print(data)
e = exists(tofile)
print(e)
input()
copy = open(tofile,"w")
#print(copy.read())
copy.write(data)
print(copy)
print(copy.read())