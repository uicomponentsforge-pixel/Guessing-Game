# Guessing Game

A simple command-line Python game where the player tries to guess a randomly chosen number between 1 and 10.

## Features

- Random number generation between 1 and 10.
- Input validation to ensure valid integer entries within the allowed range.
- Real-time feedback ("Too high!" or "Too low!") after each guess.
- Tracks total number of attempts.

## Prerequisites

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Open a terminal/command prompt and navigate to the project directory.
3. Run the following command:

```bash
python3 guessing_game.py
```

## Example Gameplay

```text
Welcome to the Guessing Game!
I have chosen a number between 1 and 10.
Enter your guess (1-10): 5
Too low! Try again.
Enter your guess (1-10): 8
Too high! Try again.
Enter your guess (1-10): 7
Correct! You won!
The secret number was: 7
Attempts: 3
```
