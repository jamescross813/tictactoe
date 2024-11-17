from random import randint

import time
import sys
import re

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
 #works if one game played, need to blank the board
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

    def human_turn(self):
        self.check_turn()
        self.slow()
        print("It's your turn")
        self.slow()
        if self.turn <=9:
            placement = input("Where do you want to place your mark?  ")

            if self.spaces[(int_placement -1)] != "X" and self.spaces[(int_placement -1)] != "O":
                    self.spaces[(int_placement -1)] = "X"      
            else: 
                    print("That spot has already been filled, try again.")
                    self.human_turn()
            self.turn + 1
            self.slow()
            self.winning("X")
            self.board()
            return self.ai_turn()
        
    def ai_turn(self):
        self.check_turn()
        self.slow()
        if self.turn <=9:
            placement = randint(1, 8)
            if self.spaces[(placement -1)] != "X" and self.spaces[(placement -1)] != "O":
                self.spaces[(placement -1)] = "O"
            else: 
                self.ai_turn()
            print("robo's turn")
            print(placement)
            self.turn + 1
            self.slow()
            self.winning("O")
            self.board()
            return self.human_turn()

    def winning(self, shape):
        # check rows
        if self.spaces[0] == shape and self.spaces[1] == shape and self.spaces[2] == shape:
            return self.win(shape)
        elif self.spaces[3] == shape and self.spaces[4] == shape and self.spaces[5] == shape:
            return self.win(shape)
        elif self.spaces[6] == shape and self.spaces[7] == shape and self.spaces[8] == shape:
            return self.win(shape)
        #check columns
        elif self.spaces[0] == shape and self.spaces[3] == shape and self.spaces[6] == shape:
            return self.win(shape)
        elif self.spaces[1] == shape and self.spaces[4] == shape and self.spaces[7] == shape:
            return self.win(shape)
        elif self.spaces[2] == shape and self.spaces[5] == shape and self.spaces[8] == shape:
            return self.win(shape)
        #check diagonals
        elif self.spaces[0] == shape and self.spaces[4] == shape and self.spaces[8] == shape:
            return self.win(shape)
        elif self.spaces[2] == shape and self.spaces[4] == shape and self.spaces[6] == shape:
            return self.win(shape)
        else:
            return "Next turn"
        
    def win(self, shape):
        if shape == "X":
            print("You win!")
        else:
            print("You lose!")
        return self.end()

    def end(self):
        cont = input("Do you want to play again?  ")
        if cont == "Yes" or cont == "Y" or cont == "y":
            self.reset()
        elif cont == "No" or "N":
            print("Hope to see you again soon!")
            sys.exit()
        else:
            print("Sorry I didn't get that.....")
            self.end()

    def reset(self):
        self.spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # print(self.spaces)
        return self.human_turn()

    def check_turn(self):
        if self.turn > 9:
            print("Draw!")
            self.end()
        else:
            return "something"
    
    def make_sure_its_a_number(self, placement):
        if placement != 1:
            int_placement = int(placement)
        else: 
            print("That's not a number, try again")
            self.human_turn()
        return int_placement
    
    def slow(self):
        time.sleep(0.5)


        