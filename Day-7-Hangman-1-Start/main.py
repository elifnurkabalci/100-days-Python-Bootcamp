#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print("Guess a letter")
guess = input().lower()
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
for i in range(len(chosen_word)):
  if chosen_word[i] == guess:
    print("True")
  else:
    print("False")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
