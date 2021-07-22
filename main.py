# import sys
# import time
# import os
# import random
# import math
# import re
from colorama import init, deinit, Fore, Back, Style
from functions import read_text, typewriter, change_color, os, time
from classes import Character

"""
Name: main
Description: Runs a series of functions.
Arguments: none
Returns: none
"""
def main():
    init(convert=True)

    os.system("cls")

    # game introduction
    typewriter(read_text("story/introduction.txt"))

    time.sleep(2)
    os.system("cls")

    # tell the rules of the world
    items = {
        "BLUE" : "Iron Dagger",
        "GREEN" : "",
        "YELLOW" : "",
        "MAGENTA" : "",
        "CYAN" : ""
    }

    typewriter(change_color(read_text("story/rules.txt"), items))

    time.sleep(2)
    os.system("cls")

    # no professions
    # select weapon
    # weapons = {
    #     "RED" : "Iron Dagger",
    #     "BLUE" : "",
    #     "GREEN" : "",
    #     "YELLOW" : "",
    #     "MAGENTA" : "",
    #     "CYAN" : ""
    # }

    # typewriter(read_text("story/starting_weapons.txt"))
    # weapon = input("> ")

    # typewriter("You chose " + weapon + ".\n" )

    # time.sleep(2)
    # os.system("cls")

    # name character
    typewriter("What is your name?\n")
    name = input("> ")
    typewriter("\nLet's begin your adventure, " + name + ".")

    time.sleep(2)
    os.system("cls")

    # start adventure

    # CLASS TESTING
    # spells = {
    #     "Potion" : ["heal", 5],
    #     "Punch" : ["attack", 2]
    # }

    # char = Character("Mary", 10, spells)
    # print("name: %s, health: %d, spells: " % (char.name, char.health), end="")
    # print(char.spells)

    # char.new_spell("Soul Heal", "heal", 20)

    # print("Char's spells: ", end="")
    # print(char.spells)

    # print("\nOriginal spells: ", end="")
    # print(spells)

if __name__ == "__main__":
    main()