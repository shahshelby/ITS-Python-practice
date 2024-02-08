capitalGuess = input("What is the capital of Latvia? ").upper()
numberOfGuesses = 1

# before it was not .upper so typing riga will not match it
while capitalGuess != "RIGA":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("You guessed incorrectly three times. Game over.")
        break
    capitalGuess = input("Guess again. ")


print("You guessed it. Riga is the capital of Latvia. It took you " + str(numberOfGuesses) + " guesses.")
