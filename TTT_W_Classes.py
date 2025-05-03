import sys
import os
import time
import json
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically reset color after each print


class Board:
    ALL_SPACES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    BLANK = " "

    def __init__(self):
        # Initialize board with all spaces set to blank
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

    def display(self, highlight=[]):
        os.system("cls" if os.name == "nt" else "clear")  # Clear terminal for animation
        b = self.spaces

        def format_cell(k):
            val = b[k]
            if val == self.BLANK:
                return k  # Show number if the space is blank
            elif k in highlight:
                return Fore.YELLOW + val + Style.RESET_ALL  # Highlight winning cell
            elif val == "X":
                return Fore.RED + "X" + Style.RESET_ALL
            elif val == "O":
                return Fore.BLUE + "O" + Style.RESET_ALL
            return val

        print("\n")
        print("     |     |     ")
        print(
            f"  {format_cell('1')}  |  {format_cell('2')}  |  {format_cell('3')}      1 | 2 | 3"
        )
        print("_____|_____|_____")
        print("     |     |     ")
        print(
            f"  {format_cell('4')}  |  {format_cell('5')}  |  {format_cell('6')}      4 | 5 | 6"
        )
        print("_____|_____|_____")
        print("     |     |     ")
        print(
            f"  {format_cell('7')}  |  {format_cell('8')}  |  {format_cell('9')}      7 | 8 | 9"
        )
        print("     |     |     \n")

    def update(self, space, mark):
        self.spaces[space] = mark  # Place 'X' or 'O' on the board

    def is_valid_move(self, space):
        # Returns True if the selected space is in range and blank
        return space in self.ALL_SPACES and self.spaces[space] == self.BLANK

    def is_full(self):
        # Returns True if no spaces are blank
        return all(value != self.BLANK for value in self.spaces.values())

    # ------------------------------------old Checking method -------------------------------------
    # def check_winner(self, mark):
    #     b = self.spaces
    #     return (
    #         (b["1"] == b["2"] == b["3"] == mark)
    #         or (b["4"] == b["5"] == b["6"] == mark)
    #         or (b["7"] == b["8"] == b["9"] == mark)
    #         or (b["1"] == b["4"] == b["7"] == mark)
    #         or (b["2"] == b["5"] == b["8"] == mark)
    #         or (b["3"] == b["6"] == b["9"] == mark)
    #         or (b["1"] == b["5"] == b["9"] == mark)
    #         or (b["3"] == b["5"] == b["7"] == mark)
    #     )
    # ----------------------------------old Checking method ---------------------------------------

    def check_winner(self, mark):
        # Return winning combination list if player has won, else None
        b = self.spaces
        wins = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["1", "4", "7"],
            ["2", "5", "8"],
            ["3", "6", "9"],
            ["1", "5", "9"],
            ["3", "5", "7"],
        ]
        for combo in wins:
            if all(b[pos] == mark for pos in combo):
                return combo
        return None


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol  # 'X' or 'O'


class Game:
    def __init__(self):
        print("Welcome to OOP Tic-Tac-Toe!")
        self.player1 = Player(input("Enter Player 1's name: "), "X")
        self.player2 = Player(input("Enter Player 2's name: "), "O")
        self.board = Board()
        self.scores = {self.player1.name: 0, self.player2.name: 0}
        self.current_player = self.player1
        self.json_log_file = "ttt_log.json"
        self.game_count = 0

        # Create Json file as list.
        if not os.path.exists(self.json_log_file):
            with open(self.json_log_file, "w") as f:
                json.dump([], f)

    def switch_player(self):
        # Alternate between player1 and player2
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def ask_replay(self):
        # Ask to play again
        response = input("Would you like to play again? (y/n): ").lower()
        return response.startswith("y")

    def play_game(self):
        self.board = Board()  # Reset board
        self.current_player = self.player1
        self.game_count += 1

        # Initialize log structure for this game
        current_game_log = {"game": self.game_count, "moves": [], "result": None}

        while True:
            self.board.display()

            while True:
                move = input(
                    f"{self.current_player.name} ({self.current_player.symbol}), enter your move (1-9 or Q to quit): "
                ).strip()

                if move.lower() == "q":
                    print("Thanks for playing! Game exited.")
                    sys.exit()

                if move not in Board.ALL_SPACES:
                    print("Please enter a number from 1 to 9.")
                    continue

                if not self.board.is_valid_move(move):
                    print("That space is already taken. Try another.")
                    continue

                break  # Valid input

            self.board.update(move, self.current_player.symbol)

            # Log this move
            current_game_log["moves"].append(
                {
                    "player": self.current_player.name,
                    "symbol": self.current_player.symbol,
                    "move": move,
                }
            )

            winning_combo = self.board.check_winner(self.current_player.symbol)
            if winning_combo:
                self.board.display(winning_combo)  # Highlight win
                print(f"{self.current_player.name} wins!")
                self.scores[self.current_player.name] += 1
                current_game_log["result"] = f"{self.current_player.name} wins"
                break

            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                current_game_log["result"] = "Tie"
                break

            self.switch_player()

        # Save this game log to the JSON file
        with open(self.json_log_file, "r+") as f:
            data = json.load(f)
            data.append(current_game_log)
            f.seek(0)
            json.dump(data, f, indent=2)

        print("\n Current Score:")
        for name, score in self.scores.items():
            print(f"{name}: {score}")
        print("\nThanks for playing!\n")

    def start(self):
        while True:
            self.play_game()
            if not self.ask_replay():
                print("Adios!")
                break


if __name__ == "__main__":
    Game().start()
