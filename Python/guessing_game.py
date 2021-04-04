# guess a number by user

import random

def guess(x):

    random_number =  random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number please between 1 and {x}:"))
        if guess < random_number:
            print(f"your guess {guess} is too low")
        elif guess > random_number:
            print(f"your guess {guess} is too high")
    print("YAY!!! you have guessed the correct number")

# guess a number by computer

def computer_guess(x):
    
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too low (L), too hihg (H), or correct (C) ??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay!! The computer have guess your number, {guess}, correctly")

    


computer_guess(1000)


