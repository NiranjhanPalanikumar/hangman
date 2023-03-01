import random

word_list = ["mango", "lychee", "watermelon", "orange", "apple"]

word = random.choice(word_list)

while True:
    guess = input("Enter your guess (single alphabetical character): ")

    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character")


if guess in word:
    print(f"Good guess! {guess} is in the word")
else:
    print(f"Sorry, {guess} is not in the word. Try again")