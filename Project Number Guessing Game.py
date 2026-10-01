import random

correct_number = random.randint(1, 100)
attempt = 0 
guess = int(input("Guess the correct number between 1-100: ").strip())

while guess > 100 or guess < 1 or 1 < guess < 100:
    if guess > 100 or guess < 1 : 
        print("Invalid Input")
    elif guess == correct_number: 
        print(f"You are correct! The number was {correct_number}")
    elif guess < correct_number:
        print("The number is higher!")
    elif guess > correct_number:
        print("The number is lower!")
    else:
        print(("Invalid input").strip())
    attempt +=1
    guess = int(input(f"Attempt = {attempt} || Retry: ").strip())
    

# Grab: Simplify While condition guess != correct
# Diagnose: Check with "if,elif" -> conditions
# If guess = correct. The while loop bypasses -> final victory message
