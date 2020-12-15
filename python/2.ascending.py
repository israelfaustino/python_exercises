from random import seed
from random import randint

# Random generator seed
seed(1)
# Array for the random numbers
vec = []
# Loop index
a = 0

temp = 0

size = input("Insert the amount of number to rearange: ")
size = int(size)

print("\nThe random generated numbers are: ")

for i in range(size):

	# Generate random number up to 999
	vec.append(randint(0,1000))
	print(vec[i], end=" ")

# rearrange the random numbers in ascending order
for a in range(0,size,1):
	for b in range(a + 1,len(vec),1):
		#print (vec[a])
		if vec[a] > vec[b]:
			temp = vec[a]
			vec[a] = vec[b]
			vec[b] = temp

print("\n\nNow in ascending order: ")
for a in vec:
	print (a, end=" ")

print("")