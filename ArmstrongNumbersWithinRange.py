# To display armstrong numbers within a range.

start_limit = int(input("Enter the start-limit of your range: "))
end_limit = int(input("Enter the end-limit of your range: "))
flag = False
count = 0

for i in range(start_limit,end_limit+1):
	sum = 0
	str_original_Number = str(i)
	no_of_digits = len(str_original_Number)
	

	if i==0:
		print(i)
	elif i>0:
		while i>0:
			sum = sum + (i%10)**no_of_digits
			i = i//10

		if sum == int(str_original_Number):
			flag = True
			count += 1
			print(str_original_Number)
		else:
			pass

	else:
		print("Invalid range limit")

if flag==False:
	print("No Armstrong number within your range limit.")
else:
	print(count," Armstrong numbers available.")