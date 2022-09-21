class Song():
    def __init__(self,lyrics):      # constructor(class special method).It automatically calls when it's class objects created.
        self.lyrics = lyrics        # self variable is referance of the instance.
    def sing_me_a_song(self,p):     # Instance(object) metod for accessing instance variables.
        price = p
        print(price)                # Local variable
        for line in self.lyrics:
            print(line)
            #print(type(line))
        
happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])# call constructor with parameter.
bulls_on_parade = Song(["They rally around the family","With pockets full of shells"])
string_pass = Song("Hello I'm Prakash Anpat")
happy_bday.sing_me_a_song(1000)        # calling instance method.
bulls_on_parade.sing_me_a_song(2000)   # pass actual argument to formal argument of the instance method.
#string_pass.sing_me_a_song(3000)
a = happy_bday.lyrics              # accessing the instance variable.
print(a)