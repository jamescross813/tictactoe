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
        winning()
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
    if spaces[0] and spaces[1] and spaces[2] == "X" or spaces[0] and spaces[1] and spaces[2] == "O":
        print("You win!!")  
    elif spaces[3] and spaces[4] and spaces[5] == "X" or spaces[3] and spaces[4] and spaces[5] == "O":
        print("You win!!")  
    elif spaces[6] and spaces[7] and spaces[8] == "X" or spaces[6] and spaces[7] and spaces[8] == "O":
        print("You win!!")   
    elif spaces[0] and spaces[3] and spaces[6] == "X" or spaces[0] and spaces[3] and spaces[6] == "O":
        print("You win!!")
    elif spaces[1] and spaces[4] and spaces[7] == "X" or spaces[1] and spaces[4] and spaces[7] == "O":
        print("You win!!")  
    elif spaces[2] and spaces[5] and spaces[8] == "X" or spaces[2] and spaces[5] and spaces[8] == "O":
        print("You win!!") 
    elif spaces[0] and spaces[4] and spaces[8] == "X" or spaces[0] and spaces[4] and spaces[8] == "O":
        print("You win!!")     
    elif spaces[6] and spaces[4] and spaces[2] == "X" or spaces[6] and spaces[4] and spaces[2] == "O":
        print("You win!!")  
    else:
        ai_turn("O")
    end()

def end():
    cont = input("Do you want to play again?  ")
    if cont == "Yes" or cont == "Y":
        intro()
    elif cont == "No" or "N":
        print("Hope to see you again soon!")
    else:
        print("Sorry I didn't get that.....")
        end()

def slow():
    time.sleep(0.5)

intro()

# def slow_print(input):
#     for char in input:
#         time.sleep(0.5)
#         print(char, end='')
        

# winning()

    # win_conditions = [{ 0: 'X', 1: "X", 2: "X"},
    # {3: "X", 4: "X", 5: "X"},
    # {6: "X", 7: "X", 8: "X"},
    # {0: "X", 3: "X", 6: "X"},
    # {1: "X", 4: "X", 7: "X"},
    # {2: "X", 5: "X", 8: "X"},
    # {0: "X", 4: "X", 8: "X"},
    # {6: "X", 4: "X", 2: "X"},
    # {0: 'X', 1: "X", 2: "X"},
    # {3: "X", 4: "X", 5: "X"},
    # {6: "X", 7: "X", 8: "X"},
    # {0: "X", 3: "X", 6: "X"},
    # {1: "X", 4: "X", 7: "X"},
    # {2: "X", 5: "X", 8: "X"},
    # {0: "X", 4: "X", 8: "X"},
    # {6: "X", 4: "X", 2: "X"}]

    # for i in win_conditions:
    #     print(i.keys())
    
        # need to then go through array and compare to board/spaces==>does spaces need to be array?