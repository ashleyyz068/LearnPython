import sys 
import random 
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("enter...\n1 for rock \n2 for paper \n3for scissors\n\n")
    player = int(playerchoice)

    if playerchoice not in ["1", "2", "3"]:
        print("you must enter 1 2 or 3")
        return play_rps ()

    if player <1 | player >3: 
        sys.exist("you must enter 1,2, or 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("")
    print("you chose " + str(RPS(player)))
    print("python choice " + str(RPS(computer)))

    if player == 1 and computer == 3: 
        print('you win')
    elif player == 2 and computer == 1: 
        print('you win')
    elif player == 3 and computer == 2: 
        print('you win')
    elif player == computer: 
        print('tie')
    else: 
        print('python wins')

    while True: 
        playAgain = input("\n Play again Yes or Quit \n Y for yes \n Q for Quit\n\n")
        if playAgain.lower() not in ["y", "q"]: 
            continue 
        else: 
            break
    if playAgain.lower() == "y": 
        return play_rps()
    else:
        print("\n YAYAY")
        print("thank you for playing")
        playAgain = False
        sys.exit("bye") 


play_rps() 
