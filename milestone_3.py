
while True:
    guess = input("Enter your guess (single alphabetical character): ")

    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character")