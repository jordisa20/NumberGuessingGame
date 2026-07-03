# Number Guessing Game

A simple command-line Number Guessing Game built with Python.

The program generates a random number between **1 and 100**, and the player must guess the correct number before running out of attempts. The game includes multiple difficulty levels and provides feedback after each guess.

## Features

- Random number generation between 1 and 100
- Three difficulty levels:
  - Easy (10 guesses)
  - Medium (5 guesses)
  - Hard (3 guesses)
- Interactive command-line interface
- Feedback after each guess
  - Too high
  - Too low
- Tracks the number of attempts used
- Displays the correct number if the player loses

## Technologies Used

- Python 3
- Built-in `random` module

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

2. Navigate to the project folder:

```bash
cd number-guessing-game
```

3. Run the program:

```bash
python main.py
```

## Example

```text
=== Menu ===
1. Play
2. Exit

Choose an option: 1

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
4. Exit

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Enter your guess: 50
Incorrect! The number is greater than 50

Enter your guess: 75
Incorrect! The number is less than 75

Enter your guess: 63
Congratulations! You guessed the correct number in 3 attempts.
```

## Project Structure

```
.
├── main.py
└── README.md
```

## Future Improvements

- Input validation for non-numeric values
- Allow the player to play again without returning to the main menu
- Add a custom difficulty option
- Track wins, losses, and best scores
- Add a leaderboard
- Save game statistics to a file

## Project Source

This project was built as part of the Backend Developer roadmap on roadmap.sh.

https://roadmap.sh/projects/number-guessing-game