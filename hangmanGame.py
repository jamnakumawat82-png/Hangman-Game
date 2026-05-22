#hangman Game!

import random

words = ['python','lion','tiger','rhino','snake']

word = random.choice(words)
print(word)
guessed_letter = []
wrong_guesses = 0
max_wrong = 6

display_word = ['_']*len(word)

print('Welcome to Hangman Game!')

while wrong_guesses < max_wrong and '_' in display_word:
	print('Word :',' '.join(display_word))
	print('Wrong guesses left:',max_wrong-wrong_guesses)

	letter = input('Enter a letter:').lower()

	if letter in guessed_letter:
		print('You already guessed that letter!')
		continue

	guessed_letter.append(letter)

	if letter in word:
		print('Correct!')

		for i in range(len(word)):
			if word[i] == letter:
				display_word[i] = letter

	else:
		print('Wrong!')
		wrong_guesses+=1

if "_" not in display_word:
	print("\n You won!")
	print("The word was :",word)
else:
	print("\n You lost!")
	print("The word was :",word)

	
