# Ideation:
#
# board as matrices to check for x or o
# print in following way:
#
#    A   B   C
# 1 [ ] [ ] [o]
# 2 [ ] [o] [x]
# 3 [o] [ ] [x]
#
# variables for every field with 3 states: empty, x, o
# ask alternating players for input
# check input for emptiness, otherwise return error + prompt to choose new field
# quit program at any time with q

import random
import time
import sys


class TicTacToe():

    def __init__(self, active_player=None, winner=None):
        self.active_player = active_player
        self.winner = winner
        self.board = {
            'A1': '[ ]',
            'A2': '[ ]',
            'A3': '[ ]',
            'B1': '[ ]',
            'B2': '[ ]',
            'B3': '[ ]',
            'C1': '[ ]',
            'C2': '[ ]',
            'C3': '[ ]',
        }

    def clear_board(self):
        self.board = {
            'A1': '[ ]',
            'A2': '[ ]',
            'A3': '[ ]',
            'B1': '[ ]',
            'B2': '[ ]',
            'B3': '[ ]',
            'C1': '[ ]',
            'C2': '[ ]',
            'C3': '[ ]',
        }

    def choose_beginner(self):

        time.sleep(1)

        print("\nSystem: Randomly choosing beginner\n...\n..\n.")

        time.sleep(1)

        random_number = random.randint(0, 1)
        if random_number == 0:
            self.active_player = "x"
        if random_number == 1:
            self.active_player = "o"
        print(self.active_player + " will begin!")
    
        time.sleep(1)

    def print_board(self):
        print()
        print("    A   B   C")
        print(" 1 " + self.board['A1'] + " " + self.board['B1'] + " " + self.board['C1'])
        print(" 2 " + self.board['A2'] + " " + self.board['B2'] + " " + self.board['C2'])
        print(" 3 " + self.board['A3'] + " " + self.board['B3'] + " " + self.board['C3'])
        print()

    def get_field(self):

        time.sleep(1)

        self.player_input = input("Choose your field! Input any combination from A1-C3:\n")

        if self.player_input == 'q':
            self.end_game()

        possible_fields = []
        for field_name in self.board.keys():
            possible_fields.append(field_name)
        if self.player_input not in possible_fields:
            print("\nError: You have to choose a valid input from A1-C3!")
            self.get_field()
        else:
            return
        
        

    def edit_field(self):
        for title, value in self.board.items():
            if self.player_input == title and value == '[ ]':
                self.board.update({title: '[' + self.active_player + ']'})
                break
            elif self.player_input == title and value != '[ ]':
                print("\nError: This field is already taken, please choose another one.")
                self.get_field()
            else:
                continue

    def change_player(self):
        if self.active_player == "x":
            self.active_player = "o"
        else:
            self.active_player = "x"
        
        print("Now it's your turn, " + self.active_player + "!")

    def play_game(self):
        self.choose_beginner()
        self.print_board()
        self.winner = "none"
        
        while self.winner == "none":
            self.get_field()
            self.edit_field()
            self.print_board()
            self.test_win()
            if self.winner != "none":
                break
            self.test_draw()
            if self.winner != "none":
                break
            self.change_player()
        
        self.end_game()

    def test_win(self):

        win_methods = {
            "A": [self.board["A1"], self.board["A2"], self.board["A3"]],
            "B": [self.board["B1"], self.board["B2"], self.board["B3"]],
            "C": [self.board["C1"], self.board["C2"], self.board["C3"]],
            "1": [self.board["A1"], self.board["B1"], self.board["C1"]],
            "2": [self.board["A2"], self.board["B2"], self.board["C2"]],
            "3": [self.board["A3"], self.board["B3"], self.board["C3"]],
            "xA1": [self.board["A1"], self.board["B2"], self.board["C3"]],
            "xA3": [self.board["A3"], self.board["B2"], self.board["C1"]],
        }

        for field in win_methods.values():
            if field[0] != "[ ]" and field[0] == field[1] and field[1] == field[2]:
                self.winner = self.active_player
            else: 
                continue

    def test_draw(self):
        non_empty_fields = 0
        for value in self.board.values():
            if value != '[ ]':
                non_empty_fields += 1 
        if non_empty_fields == 9:
            self.winner = "draw"

    def end_game(self):
        if self.winner == "draw":
            print("\nIt's a draw!")
        else:
            print("\nPlayer " + self.winner + " has won, congrats!")

        time.sleep(1)

        self.new_round()

    def new_round(self):
        next_round = input("\nDo you want to play another round? y/n\n")
        if next_round == "y":
            self.clear_board()
            self.play_game()
        elif next_round == "n" or next_round == "q":
            self.stop_game()
        else:
            print("Please input either y/n")
            self.new_round()

    def stop_game(self):
        print()
        sys.exit("---- You have left the arcade. Please come back soon! ----")

    def introduction(self):
        print("\n---- Welcome to Jonathan's TicTacToe Arcade! ----")
        print("Two players are required to play, the beginner is randomly decided by our NEXTGEN AI POWERED TECHNOLOGY.")
        print("(Press 'q' at any time to quit the game.)")
        initial_input = input("\nEnter any input to begin: ")

        if initial_input == "q":
            self.stop_game()
        else:
            self.play_game()

game = TicTacToe()
game.introduction()
game.play_game()