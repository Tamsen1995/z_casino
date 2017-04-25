
# This function forces to user to place a bet which corresponds with their budget
def make_bet(userInfo):
    try:
        while (1):
            userInfo.betMade = int(input("Please choose the amount you'd like to put up: "))
            if (userInfo.betMade > userInfo.budget):
                print("You can't bet more than you have. Please choose a different amount: ")
                continue
            elif (userInfo.betMade < 0):
                print("You can't bet less than 0. Please choose a different amount: ")
                continue 
            else:
                return userInfo.betMade
    except:
        print("Error in the make_bet module")

# a function which lets the user choose a number to place their bet on
def choose_number(userInfo):
    try:
        while (1):
            numberChosen = int(input("This is a roullette game, please go ahead and enter a number: "))
            # figure out how to add an additional comparison that makes sure the number typed in is superior to 0
            if (numberChosen < 49):
                break
            else: 
                continue
        return numberChosen
    except:
        print("Error in choose_number")


# this function checks if the bet is valid and then subtracts it from the budget
def subtract_bet_from_budget(userInfo):
    return userInfo.budget - userInfo.betMade
