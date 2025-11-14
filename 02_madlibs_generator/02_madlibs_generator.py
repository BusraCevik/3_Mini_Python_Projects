# Mad Libs Game in Python
# This script reads a story from a file and allows the user to fill in blanks.
# Words in the story that are surrounded by '<' and '>' are treated as placeholders.
# The program collects all unique placeholders, prompts the user to enter replacement words,
# and then generates the final story with the user's inputs.
# The game demonstrates file handling, string manipulation, loops, and user input in Python.

with open("story", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for "+word+ ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)


