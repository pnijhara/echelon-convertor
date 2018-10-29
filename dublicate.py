'''dublicate file is a composition of functions 
dublicate and intialize fuction returning matrix after intializing them
and returning them for the use in main file'''

#dublicate uses m(rows),n(columns),matrix(input matrix) and l2(for deep copy) as parameters
def dublicate(m,n,matrix,l2):
	for i in range(m):
		for j in range(n):
			l2[i][j]=matrix[i][j]     # picking each element from matrix and placing it in l2
	return l2

#intialize uses m,n, any multidimensional array 
#intialize any array 
def intialize(m,n,array):
	for i in range(m):
	    array.append([])
	    for j in range(n):
		    array[i].append(0)
	return array
