# Number Guessing Game

A small number guessing game you play in the terminal. I wrote it in Python as a way to practice loops, input validation and working with time.

The computer picks a secret number and you try to guess it. After each guess it tells you whether you were too low or too high. You pick a difficulty first, then choose between two modes:

- **Classic**: you have a set number of attempts.
- **Time Challenge**: the same game, but you also have 60 seconds to find the number.

## Running it

You need Python 3. There are no packages to install.

Clone the repo and `cd` into the folder. A virtual environment is optional, but if you want one:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

(On Windows, activate it with `.venv\Scripts\activate` instead.)

Then start the game:

```bash
python3 guess3.py
```

Pick a level (1, 2 or 3), then a mode (1 for Classic, 2 for Time Challenge), then start guessing.

### Which file is which

The repo has the game at three stages. `guess3.py` is the finished version.

| File        | What it has                                         |
|-------------|-----------------------------------------------------|
| `guess.py`  | Basic game: fixed 1 to 100 range, 8 attempts        |
| `guess2.py` | Adds the difficulty menu and "Attempts remaining"   |
| `guess3.py` | Adds the Classic / Time Challenge mode menu and timer |

## Difficulty levels

| Level  | Range    | Attempts |
|--------|----------|----------|
| Easy   | 1 to 50  | 10       |
| Medium | 1 to 100 | 8        |
| Hard   | 1 to 500 | 10       |

Hard gets more attempts than Medium because the range is five times bigger. If you halve the range with every guess, 10 attempts is just enough to always win.

## A couple of things worth knowing

- In Time Challenge the attempt limit still applies, so you can lose by running out of guesses before time runs out.
- The timer is checked after you press Enter. If you wait past 60 seconds and then type the right answer, you still lose. The game can't interrupt you while you're typing.
- Invalid input (letters, blank entries, numbers outside the range) shows an error and doesn't use up an attempt.

## Testing

All tests were run against `guess3.py`.

**Setup:** open `guess3.py` and change `DEBUG_SECRET = None` to `DEBUG_SECRET = 42`, so the secret number is always 42. Leave `TIME_LIMIT = 60`. Then run `python3 guess3.py` and follow the steps in each test case. **Set `DEBUG_SECRET` back to `None` when you're done**, or the answer will always be 42.

Tests 14 and 15 need real waiting: pause a few seconds before your first guess in test 14, and wait more than 60 seconds before guessing in test 15.

# Test Cases

## 1. Too low
Medium, classic, guessed 10.
Expected: "Too low." and attempts go from 8 to 7.
Result: Pass. Showed "Too low." then "Attempts remaining: 7".

## 2. Too high
Medium, classic, guessed 90.
Expected: "Too high." and attempts go down by 1.
Result: Pass. Showed "Too high." then "Attempts remaining: 7".

## 3. Correct guess
Guessed 10, then 90, then 42.
Expected: "Correct! You got it in 3 attempts."
Result: Pass. Showed "Too low.", "Too high.", then "Correct! You got it in 3 attempts."

## 4. Letters
Typed abc.
Expected: "Please enter a whole number." and attempts don't change.
Result: Pass. Showed "Please enter a whole number." Guessing 42 next gave "You got it in 1 attempt", so abc didn't count.

## 5. Blank
Just hit enter.
Expected: same as test 4.
Result: Pass. Same as test 4.

## 6. Number too small
Medium, typed 0.
Expected: "Please enter a number from 1 to 100." and attempts don't change.
Result: Pass. Showed "Please enter a number from 1 to 100." The next guess counted as attempt 1.

## 7. Number too big
Medium, typed 101.
Expected: same as test 6.
Result: Pass. Same as test 6.

## 8. Easy
Picked 1.
Expected: 1 to 50, 10 attempts, 51 gets rejected.
Result: Pass. Prompt said 1 to 50, 51 gave "Please enter a number from 1 to 50.", and the game ended after 10 wrong guesses.

## 9. Medium
Picked 2.
Expected: 1 to 100, 8 attempts.
Result: Pass. Prompt said 1 to 100 and the game ended after 8 wrong guesses.

## 10. Hard
Picked 3.
Expected: 1 to 500, 10 attempts, 500 works.
Result: Pass. Prompt said 1 to 500, 500 was accepted ("Too high."), and the game ended after 10 guesses.

## 11. Bad level
Typed 5, then abc, then 2.
Expected: error twice, then starts medium.
Result: Pass. "Please enter 1, 2 or 3." twice, then the game asked for 1 to 100.

## 12. Bad mode
Typed 3, then 1.
Expected: error, then starts classic.
Result: Pass. "Please enter 1 or 2." once, then classic started (no timer shown).

## 13. Out of attempts
Medium, 8 wrong guesses.
Expected: "Out of attempts. The number was 42."
Result: Pass. Attempts went from 7 down to 0, then "Out of attempts. The number was 42."

## 14. Timer
Time challenge, 2 guesses.
Expected: shows 60 seconds before the first guess, less before the second.
Result: Pass. Showed "Time remaining: 60 seconds". I waited 3 seconds and guessed, then it showed "Time remaining: 57 seconds".

## 15. Time runs out
Time challenge, waited over 60 seconds, then typed 42.
Expected: "Time is up! The number was 42." even though 42 was right.
Result: Pass. Waited 61 seconds, typed 42, got "Time is up! The number was 42."

## 16. Attempts in time mode
Time challenge, medium, 8 quick wrong guesses.
Expected: "Out of attempts. The number was 42." before the timer ends.
Result: Pass. The timer still showed 60 seconds, and after 8 guesses it said "Out of attempts. The number was 42."

**Result: 16 of 16 passed.**

## Ideas for later

- Save a high score for each difficulty
- Let the player choose their own time limit
- Ask "play again?"