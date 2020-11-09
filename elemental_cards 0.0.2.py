import time
from random import randint
import sys

water = ["water", "w", "1"]
fire = ["fire", "f","2"]
plant = ["plant", "p", "3"]
air = ["air", "a", "4"]


instructions = ("Here's the instructions. They are very simple!\n\nWater = 1\nFire = 2\
    \nPlant = 3\nAir = 4\n\nWater beats fire.\
    \nFire beats plant.\nPlant beats air.\nAnd air beats water(it freezez it)!\n")
notice = ("(this is the alpha version, major changes and improvements will come in the future)")

want_instructions = input("Hello, would you like instructions?\n")
yes = ["yes", "yeah", "yea", "ye", "y", "yos", "ya"]
no = ["no", "nah", "nop", "nope", "na", "n", "neh", "ne"]
understood = ()

if want_instructions in yes:
    print("\n" + instructions + notice + "\n")
    time.sleep(2)
    understood = input("Got it?\n")
    if understood in yes:
        print("\nOk good")
    elif understood in no:
        print("\nRead them again then")
        time.sleep(4)
elif want_instructions in no:
    print("\nok!")

def run_game():
    water = ["water", "w", "1"]
    fire = ["fire", "f","2"]
    plant = ["plant", "p", "3"]
    air = ["air", "a", "4"]

    number = randint(1,4)

    pick = input("\nChose a card! (water, fire, plant or air)\n")
    invalid = False

    equal = ("It's equal :/")
    win = ("You win! :D")
    lost = ("You lost! :(")

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
        invalid = True

    if invalid:
        result = ("\n That is not a valid input! :/")
        time.sleep(1)
        print("(if you think this is an error, please report the bug)")

    if invalid is False:
        print(opponent_result)
        print(result)


stop = ["stop", "no", "pls stop", "nah", "n"]

run_game()
again = True

while again:
    again = input("\nWanna play again?\n")
    if again in yes:
        run_game()
        again = True
    elif again in no or stop:
        again = False
        break
    if again in no:
        break

print("\nk bye")
print("This program will close in:\n")
print("7",end="\r",)
time.sleep(1)
print("6",end="\r")
time.sleep(1)
print("5",end="\r")
time.sleep(1)
print("4",end="\r")
time.sleep(1)
print("3",end="\r")
time.sleep(1)
print("2",end="\r")
time.sleep(1)
print("1",end="\r")
time.sleep(1)
print("0",end="\r")
time.sleep(1)
