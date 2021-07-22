def flat_array(matrix):
	x=0
	y=0
	m=len(matrix)
	#Sub array length can be differnt for each one
	#n=len(matrix[x])
	maxsqare=0
	fa=[]
	if m<0:
		print("Empty Matrix")
		return
	else:
		while x<m:
			y=0
			while y<len(matrix[x]):
				fa.append(matrix[x][y])
				y+=1
			x+=1
			
	return fa

matrix=[
[0, 0, 1, 0],
[0, 1, 1, 1, 3],
]
        
fa=flat_array(matrix)
print(fa)
			
		
	
######### Output
[0, 0, 1, 0, 0, 1, 1, 1, 3]
