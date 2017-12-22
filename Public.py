#Importing different files and libraries
import random
import Alice as al
import Bob as bo

def main():
	#Declare the biggest and lowest value of G
	min_val = 1469
	max_val = 2084

	#Get random number in range
	G = random.randint(min_val, max_val)
	n = random.randint(10, 100)

	#Executes the first public key encryption
	#See the alice and bob files for more info
	bo.bob(G, n)
	al.alice(G, n)

	#Stores the result of the first key encryption
	alice_key = al.encrypt_one
	bob_key = bo.encrypt_one

	#Executes the secret encryption of data
	al.part_two(bob_key, n)
	bo.part_two(alice_key, n)

	#Stores the final result
	Alice_Key = al.resultAlice
	Bob_Key = bo.resultBob

	#Check if the keys match
	if(Alice_Key == Bob_Key):
		print ("Correct encryption")
	else:
		print ("Something went wrong")

if(__name__ == '__main__'):
	main()