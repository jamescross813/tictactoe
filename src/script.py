
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

def board():
    print(one + "  |  " + two + "  |  " + three)
    print("_____________")
    print ("")
    print(four + "  |  " + five + "  |"   + six)
    print("_____________")
    print ("")
    print(seven + "  |  " + eight + "  |  " + nine)


def intro():
    choice = input("readt for a game of Tic Tac Toe? Will you be X or O?")
    if choice == "X" or choice == "x":
        print("You have chosen X, and go first")
    elif choice == "O" or choice == "o":
        print("You have chosen O, and go second")

# board()
intro()