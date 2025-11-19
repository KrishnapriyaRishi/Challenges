# Write a program to display Fibonacci series upto n terms.

def Fibonacci_series(n=1):
	first_term = 0
	second_term = 1
	next_term = first_term + second_term

	if n == 0:
		print("Invalid entry!!")
	elif n == 1:
		print(first_term)
	elif n == 2:
		print(first_term,second_term)
	elif n == 3:
		print(first_term,second_term,next_term)
	elif n>3:
		print(first_term,second_term,next_term,end=" ")

		for i in range(2,n-1):
			first_term = second_term
			second_term = next_term
			next_term = first_term + second_term
			print(next_term,end=" ")


numOfTerms = int(input("Enter the no. of terms : "))
Fibonacci_series(numOfTerms)