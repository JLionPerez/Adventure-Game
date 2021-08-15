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

    # player stats
    name = ""
    health = 10
    spells = {
        "Minor Heal" : ["heal", 5],
        "Glitter Slap" : ["attack", 3]
    }
    Character.player(name, health, spells)

    os.system("cls")

    # game introduction
    typewriter(read_text("story/introduction.txt"))

    input("> Press enter to continue...")
    os.system("cls")

    # tell the rules of the world
    colors = {
        "RED" : "goblins",
        "BLUE" : "Common_Chests Common_Chest Minor_Heal",
        "GREEN" : "Uncommon_Chests",
        "YELLOW" : "Rare_Chests",
        "MAGENTA" : "Legendary_Chests",
        "CYAN" : "mermaids"
    }
    
    typewriter(change_color(read_text("story/rules.txt"), colors))

    input("> Press enter to continue...")
    os.system("cls")

    # name character (might be moved when introducing player to the prophet)
    typewriter("What is your name?\n")
    name = input("> ")
    typewriter("\nLet's begin your adventure, " + name + ".")

    time.sleep(1)
    os.system("cls")

    # start adventure
    # You wake up from your slumber. The light shining through the opening of your tent.
    # You get out of your sleeping bag and out of the tent. Standing up you stretch and bask in the morning light before taking down your tent.
    # Before setting off on the road again you ramage through your backpack for a snack bar and a canteen for coffee. The flavor of the snack bar has a hint of cinnamon with fresh blueberries.
    # Using the dying embers of the campfire that you made last night you put your canteen filled with water on top of the embers to boil. 
    # 

if __name__ == "__main__":
    main()