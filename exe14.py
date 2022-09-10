"""prompt, which means it’s something the computer displays to tell you it’s ready for your instructions.
 You can type things into that window, and the computer will obey them when it understands your commands"""
from sys import argv
script, user_name = argv
prompt = " > " 
print(f"hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a some questions.")
print("Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
'''print(f"""Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")'''
print("..........................................")
script,user_name = argv
prompt = ">>>"
print(f"hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a some questions.")
print("Do you like me {user_name}?")
a = input(prompt)
print(f"Where do you live {user_name}?")
b = input(prompt)
print("What kind of computer do you have?")
c = input(prompt)
print(f"""Alright, so you said {a} about liking me.
You live in {b}. Not sure where that is.
And you have a {c} computer. Nice.""")