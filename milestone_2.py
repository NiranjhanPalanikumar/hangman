import random

word_list = ["Mango", "Lychee", "Watermelon", "Orange", "Apple"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter your guess (single character): ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")