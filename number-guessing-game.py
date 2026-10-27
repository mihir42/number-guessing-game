import random

num = random.randint(1,10)
guess = ""
attempt = 0
counter = 3

print("\nNUMBER GUESSING GAME")
print("\nGuess a number between 1 to 10.")

while True:
    try:
        print(f"{counter} attempts left.")
        guess = int(input("\nGuess: "))
        attempt += 1
        counter -= 1

        if num == guess:
            print(f"\nYou guessed the number in {attempt} attempts.\n")
            break
        elif guess > 10 or guess <= 0:
            print("\nguess between 1-10.")
            attempt -= 1
            counter += 1
        elif counter == 0 :
            print(f"\nSecret no.: {num}")
            print("\nGAME OVER!\n")
            break
        elif guess > num: 
            print("\nGuess lower")
        elif guess < num : 
            print("\nGuess higher")

    except ValueError:
        print("\nInvalid input!")