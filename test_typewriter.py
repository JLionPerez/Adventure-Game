# citation: Python - Typewriter Style Animated Text Tutorial by Learn Learn Scratch Tutorials
# link: https://youtu.be/2h8e0tXHfk0
import sys, time, os

message = "Computer: hello joggo, nice to meet you.\n\
Me: hey nice to meet you too.\n\
Computer: aight see ya later."

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n" and char != ",":
            time.sleep(0.1) # time for middle of text
        else:
            time.sleep(1) # time for end of line or text

os.system("cls") # window's clear

# typewriter(message)

# reads in the whole text file
message = []
with open('texts/test.txt') as f:
    message = f.read()

typewriter(message)