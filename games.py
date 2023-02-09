# Guessing games codes generation
# Get the guess
# Generate computer code

import random

def get_guess():
    return input("What's your guess?")

# Run game
# x = get_guess
# print(x)
# print(type(x))

# GENERATE COMPUTER CODE 
def generate_code():
    digits = [str(num) for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits);
    # Grab the first three
    return digits[:3]

# GENERATE CLUES
def generate_clues(code, user_guess):

    if user_guess == code:
        return "CODE CRACKED!";
    
    clues = []

    for ind,num in enumerate(user_guess):
        if (num == code[ind]):
            clues.append("match")
        elif num in code:
            clues.append("close");

    if clues == []:
        return ["Nope"]
    else:
        return clues

# RUN THE GAME LOGIC

print("Welcome to Code breaker!")

secret_code = generate_code()

print("Secret code",secret_code)

clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("here is the result of your guess")
    for clue in clue_report:
        print(clue)

        





