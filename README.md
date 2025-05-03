# Tic-Tac-Toe (OOP Edition with JSON Logging)

This is a Python implementation of the classic Tic-Tac-Toe game, built using **Object-Oriented Programming (OOP)** principles. The game supports:

- Two-player local gameplay
- Animated and color-coded game board using `colorama`
- Highlighting of winning cells
- Game replay option
- Score tracking
- Game and move logging to a JSON file with timestamps

---

## Project Structure

This project includes three main classes:

### 1. `Board`
Handles all logic related to the game board.

**Key Methods:**
- `__init__()` – Initializes a 3x3 board with blank values.
- `display(highlight=[])` – Prints the board with optional highlighted winning cells.
- `update(space, mark)` – Updates a space with the player's mark.
- `is_valid_move(space)` – Validates a player's input.
- `is_full()` – Checks if the board is completely filled.
- `check_winner(mark)` – Checks for a win and returns the winning combination if found.

---

### 2. `Player`
Represents each player in the game.

**Attributes:**
- `name` – The player's name.
- `symbol` – The player's mark, either `'X'` or `'O'`.

---

### 3. `Game`
Controls the game loop, user interaction, and logging.

**Key Methods:**
- `__init__()` – Initializes the game, player info, score tracking, and log file setup.
- `switch_player()` – Switches turns between players.
- `ask_replay()` – Prompts players to continue or exit.
- `play_game()` – Executes a full game round, handling:
  - User input
  - Move validation
  - Board updates
  - Win/tie detection
  - Score updates
  - JSON logging of each game
- `start()` – Runs the game loop until the players choose to stop.

---

## Features

### Colorized Terminal Output
- Red for `'X'`
- Blue for `'O'`
- Yellow highlight for winning cells

### Animated Display
- Board clears and updates with smooth transitions using `os.system`

### JSON Move Logging
All games are saved in `ttt_log.json` with:

- Player names and roles
- Each move recorded with a timestamp
- Game result
- Start and end time

**Example JSON entry:**
```json
{
  "game": 1,
  "start_time": "2025-05-03T13:45:00",
  "players": {
    "X": "Justin",
    "O": "Jefe"
  },
  "moves": [
    {
      "timestamp": "2025-05-03T13:45:12",
      "player": "Justin",
      "symbol": "X",
      "move": "5"
    }
  ],
  "result": "Justin wins",
  "end_time": "2025-05-03T13:48:17"
}
