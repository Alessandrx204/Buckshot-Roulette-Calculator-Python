import math
import time
from fractions import Fraction

# Initialize variables
cartidge = []  # List to store the cartridge
BLANK = 0  # Number of blanks
FULL = 0  # Number of full shots
arte1_is_running = True  # Flag to keep the loop running

#______________________________________________
def parte1():
	# Declare variables as global so they can be modified inside the function
	global BLANK, FULL, cartidge, arte1_is_running
	
	arte1_is_running = True  # Start of the first part of the process
	
	# Main loop that runs while arte1_is_running is True
	while arte1_is_running:
		# Get input from the user for the number of blanks and full shots
		BLANK = int(input("insert number of Blanks: "))
		FULL =  int(input("insert number of Full shots: "))
		
		total_ammo = FULL + BLANK  # Total ammo is the sum of blanks and full shots
		
		# Print the number of bullets in the cartridge and the remaining blanks and fulls
		print(f"there are {total_ammo} bullets in this cartridge, {BLANK} blanks & {FULL} fulls left")
		
		# Represent the cartridge with '[X]' for each bullet
		cartidge = '[X]' * total_ammo
		print(cartidge)
		
		# Print the probability of blanks and full shots remaining
		print(f"Probability is {Fraction(BLANK, total_ammo)} blanks & {Fraction(FULL, total_ammo)}")
		
		
		print(f'% is {(BLANK/total_ammo)*100:.3f}% a Blank & {(FULL/total_ammo)*100:.3f}% a full Shot')
		
		# End the loop after the first run
		arte1_is_running = False
		
	# Start second loop to check for any updates
	anyNEWS = True
	Tuduku = True
	while Tuduku:
		#ciclo while TSUDZUKU
		while anyNEWS:
			condizione = input(f'any news?(y/n): ')  
			
			if condizione == 'y':
				#  
				UPDATE = input('どのcontidion?(shot/soda[S] OR else): ').strip().upper()
				if UPDATE == 'S':  # If S
					'''anyNEWS = False  # End the loop'''
					
					Used_bullet = input('B/F?: ').upper()  # Ask if the used bullet is blank or full
					if Used_bullet == 'B':  # If blank is used
						BLANK -= 1 if BLANK != 0 else BLANK
						
							
					elif Used_bullet == 'F':  # If full is used
						FULL -= 1 if FULL != 0 else FULL
						#ifから出た
					# Calculate the new total_ammo
					total_ammo = BLANK + FULL
					
					# Print the updated status
					print(f"there are {total_ammo} bullets in this cartridge, {BLANK} blanks & {FULL} fulls left")
					
					# UPDATE the cartridge display
					#cartidge = '[X]' * total_ammo
					cartidge = '[X]' * total_ammo if (BLANK != 0 and FULL != 0) else '[B]'*total_ammo if FULL==0 else '[F]'*total_ammo
					
					'''上乃教育(キョウイク)Is basically Cartridge is [X] total ammo Times only if Blank is not 0 and at same time full is also not zero. Otherwise just [B] total ammo times only if tho full is 0 else [F] total ammo times'''
					print(cartidge) if total_ammo != 0 else print('Cartridge is over, I reccomend to start a new instance sis') 
					if total_ammo == 0:
						anyNEWS = False
						print('this stupid programme took days show respect and donate pls(even a coffe)')
						print('PS: Dont worry about the error, the programme is 終わった anyway (^ω^)7')
					else:
						 pass
					
					
					
					# Print the updated probability
					print(f"Probability is {Fraction(BLANK, total_ammo)} blanks & {Fraction(FULL, total_ammo)}")
					print(f'% is {(BLANK/total_ammo)*100:.3f}% a Blank & {(FULL/total_ammo)*100:.3f}% a full Shot')
					
				else:
					print('COMING IN NEXT VERSION')  # Placeholder for other updates
					'''こっちにアイテムのコードのすべてタイプするべきだ'''
			else:
				pass  # If no news, just つづく
	
			
# Start the first part of the process
parte1()

# Condizione is commented out, it's not used in the code
