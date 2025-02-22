# Hangman Game

## Overview
The **Hangman Game** is a GUI-based word-guessing game built using Python and Tkinter. The objective is to guess the hidden word by selecting one letter at a time, with a limited number of incorrect guesses allowed.

## Features
- Graphical User Interface (GUI) with Tkinter.
- Randomly selects a word from a predefined list.
- Displays guessed letters and underscores for unguessed letters.
- Limits incorrect guesses to 6 attempts.
- Alerts for invalid inputs and repeated guesses.
- Shows success and failure messages.
- Includes a "New Game" button to restart the game.

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Tkinter (included by default in Python, install if necessary)

### Install Tkinter (if needed)
#### Windows/macOS (usually pre-installed)
```sh
pip install tk
```

#### Linux (Debian-based)
```sh
sudo apt-get install python3-tk
```

### Clone the Repository
```sh
git clone <repository_url>
cd hangman-game
```

### Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### Run the Game
```sh
python hangman.py
```

## Usage
1. Enter a single letter in the input field.
2. Click the **Guess** button to submit your guess.
3. The game will reveal correct guesses and track incorrect ones.
4. Win the game by guessing all letters before running out of attempts.
5. Click **New Game** to restart at any time.

## Technologies Used
- **Python**: Core language for the game logic.
- **Tkinter**: GUI framework for interface design.
- **Random module**: Selects random words from the predefined list.

## License
This project is open-source and available under the MIT License.

## Author
Developed by [Your Name]. Feel free to contribute or reach out for suggestions!

