from random import randint

# def space():
one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "  

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
    choice = input("Are you ready for a game of Tic Tac Toe? Will you be X or O?")
    if choice == "X" or choice == "x":
        print("You have chosen X, and go first!")
        turn()
    elif choice == "O" or choice == "o":
        print("You have chosen O, and go second!")
        ai_turn()
    else:
        print("Try again")
        intro()

def human_turn():
    print("It's your turn")
    
def ai_turn():
    print("robo's turn")
    if turn <=9:

# board()
intro()