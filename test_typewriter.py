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

typewriter(message)