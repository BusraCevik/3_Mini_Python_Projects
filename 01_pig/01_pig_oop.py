# The first version was made by following a tutorial; the OOP version was implemented by me.
# Pig Dice Game - OOP Version
# The DiceGame class handles the entire game logic for 2-4 players.
# __init__(): Initializes the game with maximum score, number of players, and player scores.
# get_number_of_players(): Prompts the user for the number of players and validates input.
# roll_dice(): Returns a random integer between 1 and 6, simulating a dice roll.
# play_turn(player_index): Handles a single player's turn, including dice rolls,
#   accumulating turn score, handling rolling a 1, and updating total scores.
# play(): Main game loop. Each player takes turns until someone reaches max_score,
#   declaring the winner at the end.
# The game uses input validation to ensure correct choices and displays current scores
#   after each turn.

import random

class DiceGame:
    def __init__(self, max_score=50):
        self.max_score = max_score
        self.players = self.get_number_of_players()
        self.player_scores = [0 for _ in range(self.players)]

    def get_number_of_players(self):
        while True:
            players = input("Enter the number of players(1-4): ")
            if players.isdigit():
                players = int(players)
                if 2<=players<=4:
                    return players
                else:
                    print("Please enter a number between 1 and 4")
            else:
                print("Please enter a valid input")

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self, player_index):
        current_score = 0
        print(f"\nPlayer {player_index + 1}'s turn starts!")
        print(f"Current total score: {self.player_scores[player_index]}")

        while True:
            should_roll = input("Roll the dice? (y/n): ").lower()
            if should_roll not in ["y", "n"]:
                print("Please enter 'y' or 'n'.")
                continue
            if should_roll == "n":
                break

            roll_value = self.roll_dice()
            print(f"You rolled: {roll_value}")

            if roll_value == 1:
                print("Oh no! You rolled a 1. Turn over.")
                current_score = 0
                break
            else:
                current_score += roll_value
                print(f"Current turn score: {current_score}")

        self.player_scores[player_index] += current_score
        print(f"Total score after this turn: {self.player_scores[player_index]}")
        print("Current scores of all players:", self.player_scores)

    def play(self):
        while True:
            for i in range(self.players):
                self.play_turn(i)
                if self.player_scores[i] >= self.max_score:
                    print(f"\n Player {i + 1} wins with a score of {self.player_scores[i]}!")
                    return


if __name__ == "__main__":
    game = DiceGame()
    game.play()



