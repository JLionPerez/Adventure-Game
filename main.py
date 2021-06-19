from classes.character import Character
import sys
import time
import os
import random
import math
import re
from colorama import init, deinit, Fore, Back, Style
import classes


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
            time.sleep(0.5)  # pace for end of line
        else:
            time.sleep(0.05)  # pace for middle of text


"""
Name: change_color
Description: Changes the color of the substring you want and returns the original string with the modified sub string.
Arguments: string, dictionary
Returns: string
"""
def change_color(text, dict): # needs to be perfected in the future, for now works fine
    string_array = []
    textSplitLines = text.splitlines(keepends=True)
    endings = ['.', ',', '!', '?']

    for line in textSplitLines:
        words = re.findall(r'\S+|\n| ', line)
        for word in words:
            original_word = word
            word = re.sub('[!?@#$&,.]', '', word)
            if word in dict["RED"].split():
                color_word = Fore.RED + word + Style.RESET_ALL
                string_array.append(''.join(color_word))
            elif word in dict["BLUE"].split():
                color_word = Fore.BLUE + word + Style.RESET_ALL
                string_array.append(color_word)
            elif word in dict["GREEN"].split():
                color_word = Fore.GREEN + word + Style.RESET_ALL
                string_array.append(color_word)
            elif word in dict["YELLOW"].split():
                color_word = Fore.YELLOW + word + Style.RESET_ALL
                string_array.append(color_word)
            elif word in dict["MAGENTA"].split():
                color_word = Fore.MAGENTA + word + Style.RESET_ALL
                string_array.append(color_word)
            elif word in dict["CYAN"].split():
                color_word = Fore.CYAN + word + Style.RESET_ALL
                string_array.append(color_word)
            else:
                string_array.append(original_word)
    return (''.join(string_array))


"""
Name: main
Description: Runs a series of functions.
Arguments: none
Returns: none
"""
def main():
    init(convert=True)

    name = []
    weapon = []
    armor = []

    os.system("cls")

    # game introduction
    typewriter(read_text("story/introduction.txt"))

    time.sleep(2)
    os.system("cls")

    # tell the rules of the world
    typewriter(read_text("story/rules.txt"))

    time.sleep(2)
    os.system("cls")

    # select weapon
    typewriter(read_text("story/starting_weapons.txt"))
    weapon = input("> ")

    typewriter("You chose " + weapon + ".\n" )

    time.sleep(2)
    os.system("cls")

    # confirm selection with name
    typewriter("What is your name?\n")
    name = input("> ")
    typewriter("\nLet's begin your adventure, " + name + ".")

    time.sleep(2)
    os.system("cls")

    # start adventure

    # testing change color
    # strs_colors = {
    #     "RED": "Iron Dagger",
    #     "BLUE": "Black Hood",
    #     "GREEN": "thief",
    #     "YELLOW": "armor",
    #     "MAGENTA": "weapons",
    #     "CYAN": "example"
    # }

    # typewriter(change_color(read_text("story/rules.txt"), strs_colors))


if __name__ == "__main__":
    main()