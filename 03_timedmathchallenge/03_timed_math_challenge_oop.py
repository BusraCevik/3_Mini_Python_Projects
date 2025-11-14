# The first version was made by following a tutorial; the OOP version was implemented by me.
# Timed Math Challenge - OOP Version
# The timed_math class encapsulates the logic for a timed math quiz game.
# __init__(): Initializes operators, operand range, total number of problems, and other attributes.
# problem_generator(): Generates a random math problem and computes its answer.
# timer(): Returns the current timestamp to measure elapsed time.
# play(): Main game loop. Presents problems to the user, checks answers,
#   awards 1 point for each correct first attempt, and tracks total time.
# Input validation is handled by checking answers, and the final score and total time
#   are displayed at the end of the game.
import random
import time

class Timed_math:
    def __init__(self):
        self.OPERATORS  = ["+", "-", "*"]
        self.OPERAND_MIN = 2
        self.OPERAND_MAX = 12
        self.TOTAL_PROBLEMS = 10

    def problem_generator(self):
        self.left = random.randint(self.OPERAND_MIN, self.OPERAND_MAX)
        self.right = random.randint(self.OPERAND_MIN, self.OPERAND_MAX)
        self.operator = random.choice(self.OPERATORS)

        self.expr = str(self.left) + " " + self.operator + " " + str(self.right)
        self.answer = eval(self.expr)
        return self.expr

    def timer(self):
        return time.time()


    def play(self):
        print("Welcome to Timed Math Challenge! Each correct answer on the first try gives you 1 point.")
        print("--------------------------------")

        self.score = 0
        self.start_time = self.timer()

        for i in range(self.TOTAL_PROBLEMS):
            self.problem_generator()
            self.first_try= True

            while True:
                guess = input(f"Problem {str(i+1)}#: {self.expr} = ")
                if guess == str(self.answer):
                    if self.first_try == True:
                        self.score += 1
                    break
                else:
                        print("Incorrect, try again!")
                        self.first_try = False


        self.end_time = self.timer()
        self.total_time = self.end_time - self.start_time

        print("--------------------------------")
        print("Finished at total: " + str(round(self.total_time,2))+ " seconds")
        print(f"Your score: {self.score}/{self.TOTAL_PROBLEMS}")

if __name__ == "__main__":
    problem =  timed_math()
    problem.play()