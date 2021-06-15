import sys
import time
import os
import random
import math
from colorama import init, deinit, Fore, Back, Style

"""
Name: read_text
Description: Reads in the contents of text files and returns them as a string.
Arguments: string
Returns: string
"""


def read_text(file):
    message = []
    with open(file) as f:
        message = f.read()
    return message


"""
Name: typewriter
Description: Prints string onto the terminal as if being written by a typewriter.
Arguments: string
Returns: none
"""


def typewriter(message):
    pauses = ['\n', '.', ',', '!', '?']

    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char in pauses:
            time.sleep(0.5)  # time for end of line or text
        else:
            time.sleep(0.05)  # time for middle of text


"""
Name: 
Description: 
Arguments: 
Returns: 
"""


def change_color(text, substr, color):
    # colored_substr = Fore.RED + substr
    # index_substr = text.find(substr)

    # temp = list(text)
    # for idx

    # message = text.split()
    # # for each word in string
    # for word in message:
    #     # print(word, end='\n')
    #     if word == substr:
    #         colored = Fore.RED + word

    string_array = []

    textSplit = text.split()
    textSplitLines = text.splitlines(keepends=True)

    for word in textSplit:
        if word in substr.split():
            word2 = Fore.BLUE + word + Style.RESET_ALL
            string_array.append(word2)
        else:
            string_array.append(word)

    return (' '.join(string_array))

    # if sub string found
    # if selected color is GREEN
    # return text in color
    # if selected color is YELLOW
    # return text in color
    # if selected color is BLUE
    # return text in color
    # if selected color is MAGENTA
    # return text in color
    # if selected color is CYAN
    # return text in color


"""
Name: main
Description: Runs a series of functions.
Arguments: none
Returns: none
"""


def main():
    init(convert=True)
    # print(Fore.RED + 'some red text')

    # name = []
    # weapon = []
    # armor = []

    # os.system("cls")

    # # game introduction
    # typewriter(read_text("story/introduction.txt"))

    # time.sleep(2)
    # os.system("cls")

    # # tell the rules of the world
    # typewriter(read_text("story/rules.txt"))

    # time.sleep(2)
    # os.system("cls")

    # # select weapon
    # typewriter(read_text("story/starting_weapons.txt"))
    # weapon = input("> ")

    # typewriter("You chose " + weapon + ".\n" )

    # time.sleep(2)
    # os.system("cls")

    # # confirm selection with name
    # typewriter("What is your name?\n")
    # name = input("> ")
    # typewriter("\nLet's begin your adventure, " + name + ".")

    # time.sleep(2)
    # os.system("cls")

    # # start adventure

    typewriter(change_color("Hello Me, I'm Joggo Bob", "Joggo", "RED"))
    # text1 = change_color(read_text("story/rules.txt"), "Iron Dagger", "RED")
    # typewriter(text1)
    # text2 = change_color(text1, "Black Hood", "RED")
    # typewriter(text2)


if __name__ == "__main__":
    main()
