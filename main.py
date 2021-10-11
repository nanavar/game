secret = 7

guess = int(input("Guess the secret number: "))

if guess == secret:
    print("Wow! Congratulations, you guessed the secret number!")
else:
    print("Sorry, your guess was incorrect. The secet number is not " + str(guess))
