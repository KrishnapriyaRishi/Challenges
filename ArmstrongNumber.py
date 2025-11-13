# To check whether a given number is armstrong number or not.

num = int(input("Enter a number :- "))

str1 = str(num)
no_of_digits = len(str1)
sum = 0

if num==0:
	print("0 is an armstrong number.")
else:
	
	while num>0:
		sum = sum + (num%10)**no_of_digits
		num = num//10

	if sum == int(str1):
		print(str1,"is an armstrong number.")
	else:
		print(str1,"is not an armstrong number.")
