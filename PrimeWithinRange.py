def primeWithinRange(start,end):
	
	if start>=1 and end!=0:
		count = 0
		if start==1:
			newStart = start+1
		else:
			newStart = start

		for num in range(newStart,end+1):
			isPrime = True
			for i in range(2,num):
				if num%i==0:
					isPrime=False
					break
			if isPrime==True:
				count += 1
				print(num,end=" ")

		print(f"\nNo.of Prime numbers within {start} to {end} is {count}")

	else:
		print("Invalid range limit.")



start_limit = int(input("Enter the start limit : "))
end_limit = int(input("Enter the end limit : "))
primeWithinRange(start_limit,end_limit)


