import random

secret_number = random.randint(1,20) # should not change
for attempt in range(5):
    print("enter your guess")
    guess_number = int(input()) # asking for user input should inside the loop.
    if guess_number == secret_number:
        print("you guessed it right. Congratz!")
        break # break the loop, exits the loop
    elif guess_number < secret_number:
        print(f"your guess {guess_number} is too low")
    elif guess_number>secret_number:
        print(f"your guess {guess_number} is too high")