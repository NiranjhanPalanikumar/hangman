# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## milestone_2.py description
This python file is made to perform the basic steps individually, in order to get the idea of the flow of algorithm. The steps involved are as follows:
### Task 1
Task 1 - Created a list of 5 possible words (names of 5 favourite fruits)

### Task 2
Task 2 - Chooses a random word from the list (using random.choice() function)

### Task 3
Task 3 - Ask the user for their guess

### Task 4
Task 4 - Validate if the user input is acceptable (should be a single character and must be an alphabet)

## milestone_3.py description
This python file is made to perfect the algorithm in milestone_2.py by making the validation of user input to run continuously and making them into callable functions. The steps are as follows:

### Task 1
Task 1 - Iteratively check if the user input is valid (ie. if it is both a single character and an alphabet). This was done using a while loop and isalpha() method on the input.

### Task 2
Task 2 - To check if the validated user input is in the "word" that was randomly chosen from the word list.

### Task 3
Task 3 - Both task-1 and task-2 algorithms were put into callable functions, to make it easier to understand which block of code performs which task(s). 

The ask_for_input() funtion gets the user input and perform a validation check, which runs iteratively till the conditions are met.

The check_guess(guess) function takes in the argument "guess" which is the validated user input, and checks if the guessed alphabet is in the randomly chosen "word" from the word list.

## milestone_4.py description
This python file converts all the above algorithms and functions into class objects and attributes which makes the code much more readable and easy to understand.

The addition to this file from milestone_3.py file are as follows:

1. The class Hangamn has some extra attributes to make the game working
- word_guessed    : a list of '_' for each letter of the word chosen and fills up as user guesses the right letters
- num_letters     : the number of unique letters in the word
- num_lives       : the number of lives a palyer has to guess correctly
- list_of_guesses : a list of guesses made by the user to avoid guess repetition

2. The guessed letter by the user is comapred with the random word chosen by the computer, and replaces it with the guess in "word_guessed" at the right index if present.

3. If the guessed letter is not present in the word, 1 life is subtracted from the total lives.

