import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Fixed to 1-100 with 8 attempts for now. The level menu replaces this in feature/difficulty-levels.
low = 1
high = 100
max_attempts = 8

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
    if attempts_used == 1:
        print("Correct! You got it in 1 attempt.")
    else:
        print(f"Correct! You got it in {attempts_used} attempts.")
else:
    print(f"Out of attempts. The number was {secret_number}.")