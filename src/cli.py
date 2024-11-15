from random import randint

import time
import sys

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

#could expand here by allowing choice of X or O
    def intro(self):
        choice = input("Are you ready for a game of Tic Tac Toe?   Y/N ")
        self.slow()
        if choice == "Y" or choice == "y":
            print("You are X, and go first!")
            self.human_turn()
        elif choice == "N" or choice == "n":
            print("I need to end the game")
            sys.exit()
        else:
            print("Try again")
            self.intro()

    # can probably have a seperate check function later
    def human_turn(self):
        # add in check for move, do if less the turn 9
        self.check_turn()
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
            self.winning("X")
            # self.board()
            # self.ai_turn()
        
    def ai_turn(self):
        # need to include win check for ai
        self.check_turn()
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
            self.ai_win("O")
            # self.board()
            self.human_turn()

    def winning(self, shape):
        # check rows
        if self.board[0] == "X" and self.board[1] == "X" and self.board[2]:
            return "you win!"
        elif self.board[3] == "X" and self.board[4] == "X" and self.board[5]:
            return "you win!"
        elif self.board[6] == "X" and self.board[7] == "X" and self.board[8]:
            return "you win!"
        #check columns
        elif self.board[0] == "X" and self.board[3] == "X" and self.board[5]:
            return "you win!"
        elif self.board[1] == "X" and self.board[4] == "X" and self.board[6]:
            return "you win!"
        elif self.board[2] == "X" and self.board[5] == "X" and self.board[7]:
            return "you win!"
        #check diagonals
        elif self.board[0] == "X" and self.board[4] == "X" and self.board[8]:
            return "you win!"
        elif self.board[2] == "X" and self.board[4] == "X" and self.board[6]:
            return "you win!"
        else:
            self.ai_turn()
        # return "something"

    def check_turn(self):
        if self.turn > 9:
            print("Draw!")
            # need actual way to end game 
            self.end()
        else:
            return "something"

    #bug in this function--> need to know how to get a cli program to close - exit()/quit()?
    def end(self):
        cont = input("Do you want to play again?  ")
        if cont == "Yes" or cont == "Y" or cont == "y":
            self.intro()
        elif cont == "No" or "N":
            print("Hope to see you again soon!")
            sys.exit()
        else:
            print("Sorry I didn't get that.....")
            self.end()

    def slow(self):
        time.sleep(0.5)


        # def win_ai(self):
    #     #need to refactor these two functions into one function with variable passed in previous function
    #     # check rows
    #     if self.board[0] == "O" and self.board[1] == "O" and self.board[2]:
    #         return "you win!"
    #     elif self.board[3] == "O" and self.board[4] == "O" and self.board[5]:
    #         return "you win!"
    #     elif self.board[6] == "O" and self.board[7] == "O" and self.board[8]:
    #         return "you win!"
    #         #check columns
    #     elif self.board[0] == "O" and self.board[3] == "O" and self.board[5]:
    #         return "you win!"
    #     elif self.board[1] == "O" and self.board[4] == "O" and self.board[6]:
    #         return "you win!"
    #     elif self.board[2] == "O" and self.board[5] == "O" and self.board[7]:
    #         return "you win!"
    #         #check diagonals
    #     elif self.board[0] == "O" and self.board[4] == "O" and self.board[8]:
    #         return "you win!"
    #     elif self.board[2] == "O" and self.board[4] == "O" and self.board[6]:
    #         return "you win!"
    #     else:
    #         self.human_turn()
    #         # return "something"

# Cli.intro()


