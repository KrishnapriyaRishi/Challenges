# 
# Program to convert Roman to Integer number.
#  
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.



roman_numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

roman_doubles = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}


ch = 'y'

while ch=='y':

	integer_number = 0
	validity = True
	roman_number = input("Enter a Roman number : ").upper()

	i = 0
	while i <(len(roman_number)):
		if roman_number[i:i+2] in roman_doubles:
			integer_number += roman_doubles[roman_number[i:i+2]]
			i += 2

		elif roman_number[i] in roman_numerals:
			integer_number += roman_numerals[roman_number[i]]
			i += 1

		else:
			print("Invalid Roman number.")
			validity = False
			break
			
	if validity == True:
		print(f"Integer number equvalent to {roman_number} is {integer_number} \n")

	ch = input("Do you want to convert again?(y/n) : ")




	
