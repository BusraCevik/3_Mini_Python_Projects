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
