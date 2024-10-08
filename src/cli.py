from random import randint

import time

class Cli:
    spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    turn = 0

    def board(self):
        print(self.spaces[0] + "  |  " + self.spaces[1] + "  |  " + self.spaces[2])
        print("_____________")
        print ("")
        print(self.spaces[3] + "  |  " + self.spaces[4] + "  |  "   + self.spaces[5])
        print("_____________")
        print ("")
        print(self.spaces[6] + "  |  " + self.spaces[7] + "  |  " + self.spaces[8])

#simplfiy by assigning letter
    def intro(self):
        choice = input("Are you ready for a game of Tic Tac Toe?   Y/N")
        self.slow()
        if choice == "Y" or choice == "y":
            print("You have chosen X, and go first!")
            self.human_turn()
        elif choice == "N" or choice == "n":
            print("I need to end the game")
        else:
            print("Try again")
            self.intro()

    # can probably have a seperate check function later
    def human_turn(self):
        self.slow()
        print("It's your turn")
        self.slow()
        if self.turn <=9:
            placement = input("Where do you want to place your mark?  ")
            int_placement = int(placement)
            if self.spaces[(int_placement -1)] != "X" and self.spaces[(int_placement -1)] != "O":
                self.spaces[(int_placement -1)] = "X"
                
            else: 
                print("That spot has already been filled, try again.")
                self.human_turn()
            self.turn + 1
            self.slow()
            self.winning()
            self.board()
            self.ai_turn()
        
    def ai_turn(self):
        self.slow()
        print("robo's turn")
        if self.turn <=9:
            placement = randint(1, 8)
            print(placement)
            if self.spaces[(placement -1)] != "X" and self.spaces[(placement -1)] != "O":
                self.spaces[(placement -1)] = "O"
            else: 
                self.ai_turn()
            self.turn + 1
            self.slow()
            self.board()
            self.human_turn()

    def winning(self):
        #needs to actually work out if game is won, and who won
        return "something"

    #bug in this function--> need to know how to get a cli program to close - exit()/quit()?
    def end(self):
        cont = input("Do you want to play again?  ")
        if cont == "Yes" or cont == "Y" or cont == "y":
            self.intro()
        elif cont == "No" or "N":
            print("Hope to see you again soon!")
        else:
            print("Sorry I didn't get that.....")
            self.end()

    def slow():
        time.sleep(0.5)

    

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

            
    # def winning(self):
    #     #needs to actually work out who won==> return shape to end function which will check if ai or human
    #     #need to refactor this
    #     if self.spaces[0] and self.spaces[1] and self.spaces[2] == "X" or self.spaces[0] and self.spaces[1] and self.spaces[2] == "O":
    #         print("You win!!")  
    #     elif self.spaces[3] and self.spaces[4] and self.spaces[5] == "X" or self.spaces[3] and self.spaces[4] and self.spaces[5] == "O":
    #         print("You win!!")  
    #     elif self.spaces[6] and self.spaces[7] and self.spaces[8] == "X" or self.spaces[6] and self.spaces[7] and self.spaces[8] == "O":
    #         print("You win!!")   
    #     elif self.spaces[0] and self.spaces[3] and self.spaces[6] == "X" or self.spaces[0] and self.spaces[3] and self.spaces[6] == "O":
    #         print("You win!!")
    #     elif self.spaces[1] and self.spaces[4] and self.spaces[7] == "X" or self.spaces[1] and self.spaces[4] and self.spaces[7] == "O":
    #         print("You win!!")  
    #     elif self.spaces[2] and self.spaces[5] and self.spaces[8] == "X" or self.spaces[2] and self.spaces[5] and self.spaces[8] == "O":
    #         print("You win!!") 
    #     elif self.spaces[0] and self.spaces[4] and self.spaces[8] == "X" or self.spaces[0] and self.spaces[4] and self.spaces[8] == "O":
    #         print("You win!!")     
    #     elif self.spaces[6] and self.spaces[4] and self.spaces[2] == "X" or self.spaces[6] and self.spaces[4] and self.spaces[2] == "O":
    #         print("You win!!")  
    #     else:
    #         self.ai_turn()

    #     self.end()