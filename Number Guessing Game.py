import random

def getRandomNumber():
    return random.randrange(1, 100)

def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "Cold"
    elif number == guess:
        return "Right"
    else:
        return "Hot"

def runGuess():
    secretNumber = getRandomNumber()
    # Update the code below
    while True:
        user_guess = int(input("Enter a number between 1 and 100: "))
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it Right!")
            break
        else:
            print(hint)
            
if __name__ == '__main__':
    runGuess()
