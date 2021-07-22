def max_sqare_in_matrix(matrix):
  #x,y are variables to read elements in x& y axis respectively
	x=1
	y=1
  #Matrix size is m*n
	m=len(matrix)
	n=len(matrix[0])
	maxsqare=0
	coordinates=[0,0]
	if m<0:
		print("Empty Matrix")
		return
	else:
		while x<m:
			y=1
			while y<n:
				if matrix[x][y]==0:
					print("x,y,matrix[x,y]",x,y,matrix[x][y])
					y+=1
					continue
				else:
					print("x,y,matrix[x,y]",x,y,matrix[x][y])
					matrix[x][y]=1+min(
					matrix[x-1][y],
					matrix[x][y-1],
					matrix[x-1][y-1]
					)
					if matrix[x][y]>maxsqare:
						maxsqare=matrix[x][y]
						coordinates=x,y
					y+=1	
			x=x+1
	return maxsqare,coordinates

matrix=[
[0, 0, 1, 0, 1, 1],
[0, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 1, 1],
[1, 1, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 1, 1],
[1, 0, 1, 1, 1, 1],
[1, 1, 1, 0, 1, 1]
]
        
ms,co=max_sqare_in_matrix(matrix)
print(ms,co)
			
#output
# 3 (4, 5)
	
