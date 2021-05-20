import random
import time

difficulty_file = open("difficulty.txt", "r")
difficulty = difficulty_file.read()

if difficulty == "easy":
    max_number = 25
elif difficulty == "medium":
    max_number = 100
else:
    max_number = 200

secret_number = random.randint(1,max_number)
guess = 0
tries = 0
n = 6

print ("\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n")
print("Welcome to the number guessing game.")
print("There is a secret number between 1 to", max_number,".")
print("You have got six tries to get secret number. Good luck!")

while guess != secret_number and tries < 6:
    valid_number = False
    while valid_number == False:
        guess = input("\nPlease input your guess. ")
        if guess.isdigit() == True:
            valid_number = True
        else:
            print("\nNot a valid guess.")

    guess = int(guess)

    if guess > secret_number and tries < n-1:
        print("\nThat is too high.")
    elif guess < secret_number and tries < n-1:
        print("\nThat is too low.")

    tries = tries + 1
if guess == secret_number:
    print("\nYou guessed secret number!")
else:
    print("\nBetter luck next time")
    print("\nThe secret number was", secret_number)

time.sleep(3)
