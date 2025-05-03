import sys
import os
import time
from colorama import init, Fore, Style

init(autoreset=True)


class Board:
    ALL_SPACES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    BLANK = " "

    def __init__(self):
        self.spaces = {space: self.BLANK for space in self.ALL_SPACES}

    # -------------------old Display ---------------------------------------
    # def display(self):
    #     b = self.spaces
    #     print(
    #         f"""
    #       {b['1']}|{b['2']}|{b['3']}  123
    #              -+-      -+-
    #       {b['4']}|{b['5']}|{b['6']}  456
    #              -+-      -+-
    #       {b['7']}|{b['8']}|{b['9']}  789
    #     """
    #     )
    # ---------------------Old display-------------------------------

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")  # Clear terminal
        b = {
            k: (
                Fore.RED + "X" + Style.RESET_ALL
                if v == "X"
                else Fore.BLUE + "O" + Style.RESET_ALL if v == "O" else k
            )
            for k, v in self.spaces.items()
        }  # Colorize and label empty spots

        print("\n")
        lines = [
            "     |     |     ",
            f"  {b['1']}  |  {b['2']}  |  {b['3']}      1 | 2 | 3",
            "_____|_____|_____",
            "     |     |     ",
            f"  {b['4']}  |  {b['5']}  |  {b['6']}      4 | 5 | 6",
            "_____|_____|_____",
            "     |     |     ",
            f"  {b['7']}  |  {b['8']}  |  {b['9']}      7 | 8 | 9",
            "     |     |     ",
        ]

        for line in lines:
            print(line)
            time.sleep(0.05)  # animate each line
        print("\n")

    def update(self, space, mark):
        self.spaces[space] = mark

    def is_valid_move(self, space):
        return space in self.ALL_SPACES and self.spaces[space] == self.BLANK

    def is_full(self):
        return all(value != self.BLANK for value in self.spaces.values())

    def check_winner(self, mark):
        b = self.spaces
        return (
            (b["1"] == b["2"] == b["3"] == mark)
            or (b["4"] == b["5"] == b["6"] == mark)
            or (b["7"] == b["8"] == b["9"] == mark)
            or (b["1"] == b["4"] == b["7"] == mark)
            or (b["2"] == b["5"] == b["8"] == mark)
            or (b["3"] == b["6"] == b["9"] == mark)
            or (b["1"] == b["5"] == b["9"] == mark)
            or (b["3"] == b["5"] == b["7"] == mark)
        )


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        print("Welcome to OOP Tic-Tac-Toe!")
        self.player1 = Player(input("Enter Player 1's name: "), "X")
        self.player2 = Player(input("Enter Player 2's name: "), "O")

        self.board = Board()

        self.scores = {self.player1.name: 0, self.player2.name: 0}
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def ask_replay(self):
        response = input("Would you like to play again? (y/n): ").lower()
        return response.startswith("y")

    def play_game(self):
        self.board = Board()
        self.current_player = self.player1

        while True:
            self.board.display()

            while True:
                move = input(
                    f"{self.current_player.name} ({self.current_player.symbol}), enter your move (1-9 or Q to quit): "
                ).strip()

                if move.lower() == "q":
                    print("👋 Adios! Game exited.")
                    sys.exit()

                if move not in Board.ALL_SPACES:
                    print("Please enter a number from 1 to 9.")
                    continue

                if not self.board.is_valid_move(move):
                    print("That space is already taken. Try another.")
                    continue

                break  # input is valid, exit inner loop

            self.board.update(move, self.current_player.symbol)

            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f"{self.current_player.name} wins!")
                self.scores[self.current_player.name] += 1
                break

            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break

            self.switch_player()
        print("\n Current Score:")

        for name, score in self.scores.items():
            print(f"{name}: {score}")
        print()
        print("Thanks for playing!\n")

    def start(self):
        while True:
            self.play_game()
            if not self.ask_replay():
                print("Adios!!!")
                break


if __name__ == "__main__":
    Game().start()
