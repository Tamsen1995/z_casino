# This function prints out the general status of the game every round
def print_game(userInfo, gameInfo):
    print('\n')
    print("The budget available to you is:", userInfo.budget)
    print("You've put up", userInfo.betMade, "As your bet.")
    print("The number you have chosen is:", userInfo.numberChosen)
    print("The number on which the ball fell on is: ->", gameInfo.numberChosen)
    print('\n')

