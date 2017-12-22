#import libraries
import random
import numpy

#Declare the biggest and lowest values of B
min_val = 1469
max_val = 20845

#Create the bob key with the different variables
b = random.randint(min_val, max_val)

#First key [Public]
#Formula: G^a mod(n
def bob(G, n):
	global encrypt_one
	encrypt_one = G**b % n

#Second and secret key
#Formula: G^B*A mod(n)
def part_two(alice_result, n):
	global resultBob
	resultBob = alice_result ** b % n