from random import randint

spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

turn = 0

def board():
    print(spaces[0] + "  |  " + spaces[1] + "  |  " + spaces[2])
    print("_____________")
    print ("")
    print(spaces[3] + "  |  " + spaces[4] + "  |  "   + spaces[5])
    print("_____________")
    print ("")
    print(spaces[6] + "  |  " + spaces[7] + "  |  " + spaces[8])


def intro():
    choice = input("Are you ready for a game of Tic Tac Toe? Will you be X or O?  ")
    if choice == "X" or choice == "x":
        print("You have chosen X, and go first!")
        human_turn(choice)
    elif choice == "O" or choice == "o":
        print("You have chosen O, and go second!")
        ai_turn(shape = "X")
    else:
        print("Try again")
        intro()

# can probably have a seperate check function later
def human_turn(choice):
    print("It's your turn")
    if turn <=9:
        placement = input("Where do you want to place your mark?  ")
        int_placement = int(placement)
        if spaces[(int_placement -1)] != "X" or spaces[(int_placement -1)] != "O":
            spaces[(int_placement -1)] = choice
        else: 
            print("That spot already has already been filled, try again.")
            human_turn(choice)
        turn + 1
        board()
        if choice == "X":
            ai_turn("O")
        else:
            ai_turn("X")
    
def ai_turn(shape):
    print("robo's turn")
    if turn <=9:
        placement = randint(1, 8)
        print(placement)
        if spaces[(placement -1)] != "X" or spaces[(placement -1)] != "O":
            spaces[(placement -1)] = shape
        else: 
            ai_turn(shape)
        turn + 1
        board()
        if shape == "X":
            human_turn("O")
        else:
            human_turn("X")
# board()
intro()