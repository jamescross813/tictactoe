from random import randint

spaces = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]

turn = 0

def board():
    print(one + "  |  " + two + "  |  " + three)
    print("_____________")
    print ("")
    print(four + "  |  " + five + "  |"   + six)
    print("_____________")
    print ("")
    print(seven + "  |  " + eight + "  |  " + nine)


def intro():
    choice = input("Are you ready for a game of Tic Tac Toe? Will you be X or O?  ")
    if choice == "X" or choice == "x":
        print("You have chosen X, and go first!")
        human_turn()
    elif choice == "O" or choice == "o":
        print("You have chosen O, and go second!")
        ai_turn()
    else:
        print("Try again")
        intro()
# can probably have a seperate check function later
def human_turn():
    print("It's your turn")
    if turn <=9:
        placement = input("Where do you want to place your mark?  ")
        print(placement)
        if spaces[(placement -1)] != "X" or spaces[(placement -1)] != "O":
            print("yay blank space")
        else: 
            print(spaces[(placement -1)])
    
def ai_turn():
    print("robo's turn")
    if turn <=9:
        placement = randint(1, 9)
        print(placement)
        if spaces[(placement -1)] != "X" or spaces[(placement -1)] != "O":
            print("yay blank space")
        else: 
            print(spaces[(placement -1)])
# board()
intro()