old = 0
new = 0
cur = 1
while(cur < 100):
	print(cur, end=" ")
	new = old + cur
	old = cur
	cur = new