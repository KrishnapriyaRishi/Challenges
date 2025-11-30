# Snake & Ladder Game
# -------------------------------------------------------------------------------

# Two players : PlayerA and PlayerB
# Game Rules:
# 1. To start the game, the players should get 1 on their dice.
# 2. There are 5 ladders and 5 snakes in this game [10 x 10 square board].
# 3. Ladders move your position higher and snakes lower the position.
# 4. To finish the game, one player should reach the position 100.(Winner).
# --------------------------------------------------------------------------------

import random

# Initial position of PlayerA and PlayerB
positionA = 0
positionB = 0
# mapping for snakes and ladders.
snakes = {12 :6, 60:3, 70:10, 91:67, 97:38}
ladders = {5:58 , 14:52 ,21:43 ,56:83 ,75:94}

while positionA!=100 or positionB!=100:

	# Player A's turn.

	playerA = input("PlayerA (Type roll): ").lower()

	if playerA=='roll':

		playerAgotValue = random.randint(1,6)
		print(f"Player A got {playerAgotValue}")

		if playerAgotValue==1 and positionA==0:
			
			positionA = 1
			print(f"Player A started game and at position {positionA}")
		elif positionA>0 and positionA<=100: 
			
				if positionA not in (list(ladders.keys())+list(snakes.keys())):
					positionA += playerAgotValue

				if positionA>100:
					positionA -= playerAgotValue
				
				
				print(f"Now Player A at position {positionA}")

				if positionA in list(ladders.keys()):
					for key,val in ladders.items():
						if positionA == key:
							positionA = val
							print(f"Luckly you climb a ladder to {positionA}")
							break

				elif positionA in list(snakes.keys()):
					for key,val in snakes.items():
						if positionA == key:
							positionA = val
							print(f"A Snake got you and you come to {positionA}")
							break
				
				elif positionA == 100:
					print(f"Player A wins the game!! Game Over!!")
					break
			
# Player B 's turn.

	playerB = input("Player B (Type roll) : ").lower()
	if playerB =='roll':
		playerBgotValue = random.randint(1,6)
		print(f"Player B got {playerBgotValue}")

		if playerBgotValue==1 and positionB==0:
			
			positionB = 1
			print(f"Player B started game and at position {positionB}")

		elif positionB>0 and positionB<=100: 
			
				if positionB not in (list(ladders.keys())+list(snakes.keys())):
					positionB += playerBgotValue

				if positionB>100:
					positionB -= playerBgotValue

				print(f"Now Player B at position {positionB}")

				if positionB in list(ladders.keys()):
					for key,val in ladders.items():
						if positionB == key:
							positionB = val
							print(f"Luckly you climb a ladder to {positionB}")
							break

				elif positionB in list(snakes.keys()):
					for key,val in snakes.items():
						if positionB == key:
							positionB = val
							print(f"A Snake got you and you come to {positionB}")
							break
				
				elif positionB == 100:
					print(f"Player B wins the game!! Game Over!!")
					break
				
				
				
	







				


