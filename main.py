import sys
import time
import os
import random
import math
import re
from colorama import init, deinit, Fore, Back, Style

# https://stackoverflow.com/questions/62366169/python-replace-string-with-color

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

    x = ""
    for line in textSplitLines:
        for word in line:
            if word in dict["RED"].split():
                x = text.replace (word, "{}pe{}".format(Fore.RED, Fore.RESET))
    return x

    # for line in textSplitLines:
    #     words = re.findall(r'\S+|\n| ', line)
    #     print("words:", words)
    #     for word in words:
    #         original_word = word
    #         # word = re.sub('[!?@#$&,.]', '', word)
    #         print(word)
    #         if word in dict["RED"].split():
    #             print("split", dict["RED"].split())
    #             color_word = []
    #             for char in word:
    #                 if char not in endings:
    #                     print(char)
    #                     color_char = Fore.RED + char + Style.RESET_ALL
    #                     color_word.append(color_char)
    #             string_array.append(''.join(color_word))
    #         elif word in dict["BLUE"].split():
    #             color_word = Fore.BLUE + word + Style.RESET_ALL
    #             string_array.append(color_word)
    #         elif word in dict["GREEN"].split():
    #             color_word = Fore.GREEN + word + Style.RESET_ALL
    #             string_array.append(color_word)
    #         elif word in dict["YELLOW"].split():
    #             color_word = Fore.YELLOW + word + Style.RESET_ALL
    #             string_array.append(color_word)
    #         elif word in dict["MAGENTA"].split():
    #             color_word = Fore.MAGENTA + word + Style.RESET_ALL
    #             string_array.append(color_word)
    #         elif word in dict["CYAN"].split():
    #             color_word = Fore.CYAN + word + Style.RESET_ALL
    #             string_array.append(color_word)
    #         else:
    #             string_array.append(original_word)
    # return (''.join(string_array))


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

    # typewriter(change_color("Hello Me, I'm Joggo Bob", "Joggo", "RED"))
    # text1 = change_color(read_text("story/rules.txt"), "Iron Dagger", "RED")
    # typewriter(text1)
    # text2 = change_color(text1, "Black Hood", "RED")
    # typewriter(text2)

    strs_colors = {
        "RED": "Iron Dagger",
        "BLUE": "Black Hood",
        "GREEN": "thief",
        "YELLOW": "armor",
        "MAGENTA": "weapons",
        "CYAN": "example"
    }

    print(change_color(read_text("story/rules.txt"), strs_colors))
    # typewriter(change_color(read_text("story/rules.txt"), strs_colors))

    # static_string = "I love chicken,"

    # x = static_string.replace("chicken", "{}chicken{}".format(Fore.BLUE, Fore.RESET))

    # print (x)


if __name__ == "__main__":
    main()
