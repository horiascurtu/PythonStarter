secret = 7
guess = -1

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("You guessed it!")
    else:
        print("Try again!")
