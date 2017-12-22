#import libraries
import random
import numpy

#Declare the biggest and lowest values of A
min_val = 1469
max_val = 20845

#Create the alice key with the different variables
a = random.randint(min_val, max_val)

#First key [Public]
#Formula: G^a mod(n)
def alice(G, n):
	global encrypt_one
	encrypt_one = G**a % n

#Second and secret key
#Formula: G^A*B mod(n)
def part_two(bob_result, n):
	global resultAlice
	resultAlice = bob_result ** a % n