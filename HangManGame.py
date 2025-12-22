
import random

words = ['welcome','hello','work','health','music','python']
selected_word = random.choice(words)

chances = len(selected_word) + 3

word_list = list(selected_word)


new_list = []

print("---------- Welcome to Hangman game ----------")
print("\nTry to guess letters to fill the blanks : ")

for i in range(0,len(selected_word)):
	print("_",end=' ')
	new_list.insert(i,"_")
		

while chances>0:
	
	letter = input("\nEnter a letter to fill the blanks : ").lower()
	if letter in word_list:
		print("Correct guess")
		for i in range(0,len(word_list)):
			if word_list[i]==letter:
				# print(word_list[i],end='')
				new_list.pop(i)
				new_list.insert(i,word_list[i])

		for k in range(0,len(new_list)):
			print(new_list[k],end='')		
		chances-=1

		if new_list==word_list:
			print("\nYou won the game.")
			break
		

	else:
		chances -= 1
		print(f"Wrong guess.You have only {chances} left.")

if new_list!=word_list or chances==0:
	print("\nYou lost the game.")

			
	


	
