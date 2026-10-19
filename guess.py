import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# keep asking until the player picks 1, 2 or 3
while True:
    print("Choose a level:")
    print("1. Easy   (1 to 50, 10 attempts)")
    print("2. Medium (1 to 100, 8 attempts)")
    print("3. Hard   (1 to 500, 10 attempts)")
    level = input("Enter 1, 2 or 3 \n").strip()

    if level in ["1", "2", "3"]:                  # check - is it a valid level?
        break

    print("Please enter 1, 2 or 3.")

# set the range and attempt limit for the chosen level
low = 1
if level == "1":
    high = 50
    max_attempts = 10
elif level == "2":
    high = 100
    max_attempts = 8
else:
    high = 500
    max_attempts = 10

# ---------- Choose a mode ----------
# Added in feature/time-challenge.

# ---------- Set up the round ----------
# use DEBUG_SECRET when testing, otherwise pick a random number in the range
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

attempts_used = 0
won = False

# ---------- Guess loop ----------
# keep asking until the player wins or runs out of attempts
while attempts_used < max_attempts:
    guess = input(f"Guess a number from {low} to {high} \n").strip()

    if guess.isdigit():                           # check - is it a whole number?
        guess_number = int(guess)

        if low <= guess_number <= high:           # check - is it in range?
            attempts_used += 1                    # only valid guesses use an attempt

            if guess_number > secret_number:      # check - compare with the secret
                print("Too high.")
            elif guess_number < secret_number:
                print("Too low.")
            else:
                won = True
                break

        else:
            print(f"Please enter a number from {low} to {high}.")

    else:
        print("Please enter a whole number.")

# ---------- End of round ----------
# show the result that matches how the round ended
if won:
    print(f"Correct! You got it in {attempts_used} attempts.")
else:
    print(f"Out of attempts. The number was {secret_number}.")