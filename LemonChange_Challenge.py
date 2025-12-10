
# Problem 
# ------------------

# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue 
# to buy from you and order one at a time (in the order specified by bills). 
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
# You must provide the correct change to each customer so that the net transaction
# is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, 
# return true if you can provide every customer with the correct change, 
# or false otherwise.

# ------------------------------------------------------------------------------------

customer_bill = list(map(int,input().strip().split()))

customer_bill_invalid = any((x !=5 and  x!=10 and x!=20) for x in customer_bill)


if customer_bill_invalid == True:

	print("Sorry! We can't accept bill other than $5,$10 or $20.")

else:

	bill_freq = {5:0,10:0,20:0}

	change_available = True
	
	for b in customer_bill:
		if b == 5:
			bill_freq[5] += 1

		elif b==10:
			change = bill_freq[5]  
			if change == 0:
				change_available = False
				break
			else:
				bill_freq[10] += 1
				bill_freq[5] -= 1
			
		elif b==20:
			if not ((bill_freq[10]>=1 and bill_freq[5]>=1) or bill_freq[5]>=3 ):
				change_available = False
				break
			else:
				bill_freq[20] += 1

				if (bill_freq[10]>=1 and bill_freq[5]>=1):
					
					bill_freq[10]-=1
					bill_freq[5] -= 1

				elif bill_freq[5] >= 3:
					bill_freq[5] -= 3
					

	if change_available==True:
		print("true")
	else:
		print("false")

			


