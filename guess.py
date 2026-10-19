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
# keep asking until the player picks Classic or Time Challenge
while True:
    print("Choose a mode:")
    print("1. Classic")
    print(f"2. Time Challenge ({TIME_LIMIT} seconds)")
    mode = input("Enter 1 or 2 \n").strip()

    if mode in ["1", "2"]:                        # check - is it a valid mode?
        break

    print("Please enter 1 or 2.")

if mode == "2":
    timed = True
else:
    timed = False

# ---------- Set up the round ----------
# use DEBUG_SECRET when testing, otherwise pick a random number in the range
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

attempts_used = 0
won = False
timed_out = False
start_time = time.time()                          # start the clock once, before the loop

# ---------- Guess loop ----------
# keep asking until the player wins, runs out of attempts, or runs out of time
while attempts_used < max_attempts:
    # show the seconds remaining before each guess (Time Challenge only)
    if timed:
        remaining = max(0, TIME_LIMIT - (time.time() - start_time))
        print(f"Time remaining: {round(remaining)} seconds")

    guess = input(f"Guess a number from {low} to {high} \n").strip()

    if guess.isdigit():                           # check - is it a whole number?
        guess_number = int(guess)

        if low <= guess_number <= high:           # check - is it in range?
            attempts_used += 1                    # only valid guesses use an attempt

            # check - has time run out? (before the answer, so a late correct guess loses)
            if timed and time.time() - start_time > TIME_LIMIT:
                timed_out = True
                break

            if guess_number > secret_number:      # check - compare with the secret
                print("Too high.")
            elif guess_number < secret_number:
                print("Too low.")
            else:
                won = True
                break

            print(f"Attempts remaining: {max_attempts - attempts_used}")

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
elif timed_out:
    print(f"Time is up! The number was {secret_number}.")
else:
    print(f"Out of attempts. The number was {secret_number}.")