# Timed Math Challenge - Procedural Version
# This script generates simple math problems for the user to solve under a timed session.
# OPERATORS: List of mathematical operators used in problems.
# MIN_OPERAND, MAX_OPERAND: Define the range of numbers used in the problems.
# TOTAL_PROBLEMS: Number of math problems in one session.
# generate_problem(): Creates a random math problem and computes the correct answer.
# User input is compared with the correct answer; wrong attempts are counted.
# The total time taken to solve all problems is measured and displayed.
# Demonstrates use of random number generation, loops, input validation, and timing in Python.
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("press enter to start!")
print("---------------------")

start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) +  ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()

total_time = round(end_time - start_time, 2)

print("---------------------")
print("Nice work! You finished in", total_time, "seconds!")

