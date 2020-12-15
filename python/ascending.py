vec = [10,9,8,7,6,5,4,3,2,1]
#print (vec[1])


for a in range(0,len(vec),1):
	#print (vec[a])
	for b in range(a + 1,len(vec),1):
		#print (vec[a])
		if vec[a] < vec[b]:
			temp = vec[a]
			vec[a] = vec[b]
			vec[b] = temp

print (vec)