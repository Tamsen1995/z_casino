import random
import math
import sys
import random
from affichage import print_game
from determine import is_odd, deter_round
from choose import make_bet, subtract_bet_from_budget, choose_number

# data about the game and the user
class gameInfo:
    numberChosen = random.randrange(0, 49)
class userInfo:
    budget = 500
    betMade = 0
    numberChosen = 0


# this funciton saves the final budget of the game into a text file 
# in case the user would like to continue his last session.
def save_game_status(userInfo):
    my_file = open("saving.txt", "w")
    my_file.write(str(userInfo.budget))
    my_file.close()


def new_game_or_no():
    try:
        print("Would you like to start a new game?")
        new_game = input("Please type in (yes) or (no): ")
        if new_game == "yes":
            return 500
        elif new_game == "no":
            my_file = open("saving.txt", "r")
            contenu = my_file.read() 
            my_file.close
            return float(contenu)
    except:
        print("Error in the new_game_or_no function! ")


# this function will serve as the contnuous loop
# it is the main function so to speak
def centerStream():
    try:
        userInfo.budget = new_game_or_no()
        print("The budget available to you is:", userInfo.budget)
        while (1):
            userInfo.numberChosen = choose_number(userInfo)
            userInfo.betMade = make_bet(userInfo)
            userInfo.budget = subtract_bet_from_budget(userInfo)
            deter_round(userInfo, gameInfo)
            print_game(userInfo, gameInfo)
            keepGoing = input("Type in ( q ) in order to quit. ( c ) to continue: ")
            if keepGoing == "q":
                break
            elif keepGoing == "c":
                continue
        save_game_status(userInfo)
        print("You've quit the game with", userInfo.budget, "moneys")

        return
    except:
        print("Error in the center stream")

    
centerStream()