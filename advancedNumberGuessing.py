import random
BINGO = random.randint(1, 100)
attempt = 0

while True: 
    GUESS = input("Enter a valid number between 1-100: ").strip()
    if not GUESS.isdigit() or GUESS == "": #Valid digit/whitespace checking with isdigit. And rerunning from continue
        print("Enter a valid number mf'er")
        continue #CONTINUE needed here. TO BAIL OUT EARLY

    GUESS = int(GUESS)
    # REMEMBER to typecast after string check done with .isdigit()
    
    if 1 > GUESS or GUESS > 100:
        print("Out of bounds! Retry again")
        continue #CONTINUE needed here. TO BAIL OUT EARLY. CUZ it's a deadend
    
    attempt+=1 #AFTER all the checks are done. Number is valid to guess. Now count attempts
    if GUESS > BINGO: 
        print("The number is lower!")
    elif GUESS < BINGO: 
        print("The number is higher!")
    else:
        print(f"Correct! {BINGO} was the correct number!")
        break

# Doesn't need the extra continue at the last loop. Cuz it ends anyway at any of the if/elif then the while loop re-runs
# REDUNDANCY






