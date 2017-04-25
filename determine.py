
# Self explanatory
def is_odd(num):
   return num % 2 != 0


# Here we determine if the user won or lost and how much.
def deter_round(userInfo, gameInfo):
    try:
        #print_board(userInfo, gameInfo)
        same_color = False
        if is_odd(userInfo.numberChosen) == is_odd(gameInfo.numberChosen):
            same_color = True
        if gameInfo.numberChosen == userInfo.numberChosen:
            userInfo.budget = userInfo.budget + (userInfo.betMade * 3)
        elif same_color == True:
            userInfo.budget = userInfo.budget + (userInfo.betMade / 2)
    except:
        print("Error in the deter_round module")
        