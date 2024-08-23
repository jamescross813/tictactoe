from random import randint

import time

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
    slow()
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
    slow()
    print("It's your turn")
    slow()
    if turn <=9:
        placement = input("Where do you want to place your mark?  ")
        int_placement = int(placement)
        if spaces[(int_placement -1)] != "X" and spaces[(int_placement -1)] != "O":
            spaces[(int_placement -1)] = choice
            # not working, 
        else: 
            print("That spot has already been filled, try again.")
            human_turn(choice)
        turn + 1
        slow()
        board()
        if choice == "X":
            ai_turn("O")
        else:
            ai_turn("X")
    
def ai_turn(shape):
    slow()
    print("robo's turn")
    if turn <=9:
        placement = randint(1, 8)
        print(placement)
        if spaces[(placement -1)] != "X" and spaces[(placement -1)] != "O":
            spaces[(placement -1)] = shape
        else: 
            ai_turn(shape)
        turn + 1
        slow()
        board()
        if shape == "X":
            human_turn("O")
        else:
            human_turn("X")

def winning():
    win_conditions = {1 :{ 0: 'X', 1: "X", 2: "X"},
    2 : {3: "X", 4: "X", 5: "X"},
    3 : {6: "X", 7: "X", 8: "X"},
    4 : {0: "X", 3: "X", 6: "X"},
    5 : {1: "X", 4: "X", 7: "X"},
    6 : {2: "X", 5: "X", 8: "X"},
    7 : {0: "X", 4: "X", 8: "X"},
    8 : {6: "X", 4: "X", 2: "X"},
    9 :{ 0: 'X', 1: "X", 2: "X"},
    10 : {3: "X", 4: "X", 5: "X"},
    11 : {6: "X", 7: "X", 8: "X"},
    12 : {0: "X", 3: "X", 6: "X"},
    13 : {1: "X", 4: "X", 7: "X"},
    14 : {2: "X", 5: "X", 8: "X"},
    15 : {0: "X", 4: "X", 8: "X"},
    16 : {6: "X", 4: "X", 2: "X"}}
    

   

def slow():
    time.sleep(0.5)


def slow_print(input):
    for char in input:
        time.sleep(0.5)
        print(char, end='')
        
# intro()
winning()