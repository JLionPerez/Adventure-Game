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

    time.sleep(1.5)
    os.system("cls")

    # tell the rules of the world
    # typewriter(read_text("story/rules.txt"))

    # time.sleep(1.5)/
    # os.system("cls")

    colors = {
        "RED" : "goblins",
        "BLUE" : "",
        "GREEN" : "",
        "YELLOW" : "",
        "MAGENTA" : "",
        "CYAN" : "mermaids"
    }
    
    typewriter(change_color(read_text("story/spells.txt"), colors))

    time.sleep(1.5)
    os.system("cls")

    # name character
    typewriter("What is your name?\n")
    name = input("> ")
    typewriter("\nLet's begin your adventure, " + name + ".")

    time.sleep(1.5)
    os.system("cls")

    # start adventure

if __name__ == "__main__":
    main()