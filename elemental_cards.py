import time
from random import randint

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
        time.sleep(6)
elif want_instructions in no:
    print("\nok!\n")

number = randint(1,4)

# game

pick = input("Chose a card! (water, fire, plant or air)\n")

if number == 1:
    opponent_pick = 1
    print("\nOpponent chose water!")
elif number == 2:
    opponent_pick = 2
    print("\nOpponent chose fire!")
elif number == 3:
    opponent_pick = 3
    print("\nOpponent chose plant!")
elif number == 4:
    opponent_pick = 4
    print("\nOpponent chose air!")

#  If result is equal
if pick in water and opponent_pick == 1:
    result = ("It's equal :/")
elif pick in fire and opponent_pick == 2:
    result = ("It's equal :/")
elif pick in plant and opponent_pick == 3:
    result = ("It's equal :/")
elif pick in air and opponent_pick == 4:
    result = ("It's equal :/")

#  If you win
if pick in water and opponent_pick == 2:
    result = ("You win! :D")
if pick in fire and opponent_pick == 3:
    result = ("You win! :D")
if pick in plant and opponent_pick == 4:
    result = ("You win! :D")
if pick in air and opponent_pick == 1:
    result = ("You win! :D")

#  If you lose
if pick in water and opponent_pick == 4:
    result = ("You lose! :(")
if pick in fire and opponent_pick == 1:
    result = ("You lose! :(")
if pick in plant and opponent_pick == 2:
    result = ("You lose! :(")
if pick in air and opponent_pick == 3:
    result = ("You lose! :(")

print(result)
time.sleep(6)
print("\n(Reopen the file to play again)")

input()