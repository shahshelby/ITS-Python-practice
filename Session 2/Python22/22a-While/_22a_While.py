capitalGuess = input("What is the capital of Latvia? ")
numberOfGuesses = 1

while capitalGuess != "Riga":
    numberOfGuesses = numberOfGuesses + 1
    capitalGuess = input("Try again ")

print("You guessed it right and you took " + str(numberOfGuesses) + " guesses.")
