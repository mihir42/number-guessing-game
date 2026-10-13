import random

num = random.randint(1,10)
guess = None
attempt= 0

while guess != num :
    try:
        guess = int(input("Guess a number between 1-10: "))
        attempt += 1
        
        if guess > num : 
            print("Guess lower")
        elif guess < num : 
            print("Guess higher")
        else :
            print("You guessed the number")
            print("Attempts: ", attempt)
    except ValueError:
        print("Enter valid value")

