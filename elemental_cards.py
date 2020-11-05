import time
from random import randint
import sys

water = ["water", "w", "1"]
fire = ["fire", "f","2"]
plant = ["plant", "p", "3"]
air = ["air", "a", "4"]

understood = ()

instructions = ("Here's the instructions. They are very simple!\n\nWater = 1\nFire = 2\
    \nPlant = 3\nAir = 4\n\nWater beats fire.\
    \nFire beats plant.\nPlant beats air.\nAnd air beats water(it freezez it)!\n")
notice = ("(this is the alpha version, major changes and improvements will come in the future)")

want_instructions = input("Hello, would you like instructions?\n")
yes = ["yes", "yeah", "yea", "ye", "y", "yos", "ya"]
no = ["no", "nah", "nop", "nope", "na", "n", "neh", "ne"]

if want_instructions in yes:
    print("\n" + instructions + notice + "\n")
    time.sleep(4)
    understood = input("Got it?\n")
    if understood in yes:
        print("\nOk good\n")
    elif understood in no:
        print("\nRead them again then\n")
        time.sleep(8)
elif want_instructions in no:
    print("\nok!\n")

number = randint(1,4)

# game

pick = input("Chose a card! (water, fire, plant or air)\n")
invalid = ("no")

if number == 1:
    opponent_pick = 1
    opponent_result = ("\nOpponent chose water!")
elif number == 2:
    opponent_pick = 2
    opponent_result = ("\nOpponent chose fire!")
elif number == 3:
    opponent_pick = 3
    opponent_result = ("\nOpponent chose plant!")
elif number == 4:
    opponent_pick = 4
    opponent_result = ("\nOpponent chose air!")


equal = ("It's equal :/")
win = ("You win! :D")
lost = ("You lost! :(")

if pick.lower() in water and opponent_pick == 1:  #If result is equal
    result = equal
elif pick.lower() in fire and opponent_pick == 2:
    result = equal
elif pick.lower() in plant and opponent_pick == 3:
    result = equal
elif pick.lower() in air and opponent_pick == 4:
    result = equal
elif pick.lower() in water and opponent_pick == 2:  #If you win
    result = win
elif pick.lower() in fire and opponent_pick == 3:
    result = win
elif pick.lower() in plant and opponent_pick == 4:
    result = win
elif pick.lower() in air and opponent_pick == 1:
    result = win
elif pick.lower() in water and opponent_pick == 4:  #If you lose
    result = lost
elif pick.lower() in fire and opponent_pick == 1:
    result = lost
elif pick.lower() in plant and opponent_pick == 2:
    result = lost
elif pick.lower() in air and opponent_pick == 3:
    result = lost
else:
    invalid = ("yes")

if invalid in yes:
    result = ("\n That is not a valid input! :/")
    print(result)
    time.sleep(2)
    print("(if you think this is an error, please report the bug)")
    time.sleep(2)
    print("\nReopen the file to play again")

if invalid in no:
    print(opponent_result)
    print(result)
    time.sleep(4)
    print("\n(Reopen the file to play again)")

input()