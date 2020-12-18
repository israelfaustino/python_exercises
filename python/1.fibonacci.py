old = 0
new = 0
cur = 1
size = 100
count = 0

size = input("Insert the amount of numbers to be generated (0-1000): ")
size = int(size)

# Number limit
if size > 1000:
	print("Size cannot be bigger than 100")
	size = 100

# Main loop
while(count < size):
	count = count + 1
	# Prints the generated number with padded index
	print(str(count).rjust(4,'0'),". ", cur, end="\n", sep="")
	new = old + cur
	old = cur
	cur = new