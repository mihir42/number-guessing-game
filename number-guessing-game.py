import random

num = int(input("Guess a number from 1-9: "))

number = random.randint(1, 9)

if num == number :
    print("You guessed it right")
else:
    print("Your guess was wrong")


