# Pig Dice Game in Python
# This game allows 2-4 players to take turns rolling a die.
# Players can keep rolling to accumulate points in their turn.
# Rolling a 1 resets the turn score to 0 and passes the turn to the next player.
# Each player's total score is tracked, and the first to reach 50 points wins.
# The 'roll()' function simulates a die roll between 1 and 6.
# Input validation ensures correct number of players and turn choices.

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
while True:
    players = input("Enter the number of players (1-4): ")
    #check if its a valid input
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Invalid, Please enter a number between 1 and 4")
    else:
        print("Invalid input. Please enter a number between 1 and 4")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("Player ", player_idx + 1, "turn has just started\n")
        print("Your current score is: ", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower()  != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your current score: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player ", winning_idx + 1, "wins! with a score of ", max_score)



