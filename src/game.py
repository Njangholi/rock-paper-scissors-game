"""Play a round of Rock, Paper, Scissors.
Author: Narges Jangholi
Date: 2025-09-18
Description: This module contains the main class and methods for game of Rock, Paper, Scissors.
"""

import random
from typing import List


class RockPaperScissors:
    """Main class to represent the game of Rock, Paper, Scissors.

    This class handles player input, computer choice,
    and determines the winner of each round.
    """

    # Win combinations where the first item beats the second item.
    WIN_COMBINATIONS = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]

    def __init__(self, name: str):
        self.choices: List[str] = ["rock", "paper", "scissors"]
        self.player_name: str = name

    def get_player_choice(self) -> str:
        """Prompt the player to enter their choice of rock, paper, or scissors."""
        player_choice = input(
            f"{self.player_name}, enter your choice ({self.choices}): "
        ).lower()
        if player_choice in self.choices:
            return player_choice
        print(f"{self.player_name}, enter a right choices of {self.choices}")
        return self.get_player_choice()

    def get_computer_choice(self) -> str:
        """Randomly select the computer's choice from choices of rock, paper, scissors."""
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Determine the winner of the game round based on user and computer choices.

        :param user_choice: The choice made by the user (rock, paper, or scissors).
        :param computer_choice: The choice made by the computer (rock, paper, or scissors).
        :return: The result of the game as a string message who is the winner or if it's a tie.
        """
        if user_choice == computer_choice:
            return "It`s a tie!"
        for win_comb in self.WIN_COMBINATIONS:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return f"Congratulations {self.player_name}! You WIN"
        return "OH, sorrry, maybe you will win next time!..."

    def play(self):
        """Play a round of Rock, Paper, Scissors.
        - Get the player's choice.
        - Get the computer's choice.
        - Decide and print the winner.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"Your choice was: {user_choice}\nComputer choice was: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == "__main__":
    print("Welcome to the Rock, Paper, Scissors game!")
    user_name = input("What is your name? ")
    game = RockPaperScissors(user_name)

    while True:
        game.play()

        continue_game = input(
            "Do you want to play again?"
            "(Enter any key to continue, otherwise press q/Q to exit)"
        )
        if continue_game.lower() == "q":
            print("Thank you for playing! Goodbye!")
            break
