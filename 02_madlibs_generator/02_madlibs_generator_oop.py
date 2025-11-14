# The first version was made by following a tutorial; the OOP version was implemented by me.
# Mad Libs Game - OOP Version
# The MadLibsGenerator class handles reading the story, finding placeholders,
# collecting user input, and generating the final story.
# __init__(): Initializes the game, loads the story from a file, and sets up data structures.
# story_enumerate(): Finds all unique placeholders in the story surrounded by '<' and '>'.
# replace_words(): Prompts the user for replacement words and substitutes them into the story.
# play(): Runs the game flow: enumerates placeholders, replaces words, and prints the final story.

class MadLibsGenerator:
    def __init__(self):
        self.words = set()
        self.start_of_word = -1

        with open("story", "r") as f:
            self.story = f.read()

        self.answers = {}

    def story_enumerate(self):
        target_start = "<"
        target_end = ">"

        for i, char in enumerate(self.story):
            if char == target_start:
                self.start_of_word = i
            if char == target_end and self.start_of_word != -1:
                word = self.story[self.start_of_word:i+1]
                self.words.add(word)
                self.start_of_word = -1

    def replace_words(self):
        for word in self.words:
            answer = input(f"Enter a word for {word}: ")
            self.answers[word] = answer

        for word in self.words:
            self.story = self.story.replace(word, self.answers[word])

    def play(self):
        self.story_enumerate()
        self.replace_words()
        print("\nYour story:\n")
        print(self.story)


if __name__ == "__main__":
    madlibs = MadLibsGenerator()
    madlibs.play()

class MadLibsGenerator:
    def __init__(self):
        self.words = set()
        self.start_of_word = -1

        with open("story", "r") as f:
            self.story = f.read()

        self.answers = {}

    def story_enumerate(self):
        target_start = "<"
        target_end = ">"

        for i, char in enumerate(self.story):
            if char == target_start:
                self.start_of_word = i
            if char == target_end and self.start_of_word != -1:
                word = self.story[self.start_of_word:i+1]
                self.words.add(word)
                self.start_of_word = -1

    def replace_words(self):
        for word in self.words:
            answer = input(f"Enter a word for {word}: ")
            self.answers[word] = answer

        for word in self.words:
            self.story = self.story.replace(word, self.answers[word])

    def play(self):
        self.story_enumerate()
        self.replace_words()
        print("\nYour story:\n")
        print(self.story)


if __name__ == "__main__":
    madlibs = MadLibsGenerator()
    madlibs.play()
