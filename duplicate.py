'''
`duplicate` file is a composition of functions
`duplicate` and `initialize` function return matrix after initializing them
and return them for use in main file.
'''

# duplicate uses m(rows), n(columns), matrix(input matrix)
# and l2 (for deep copy) as parameters.


def duplicate(m, n, matrix, l2):
	for i in range(m):
		for j in range(n):
			l2[i][j] = matrix[i][j]
            # picking each element from matrix and placing it in l2
	return l2

# initialize uses m, n, and any multidimensional array
# initialize any array..
def initialize(m, n, array):
	for i in range(m):
	    array.append([])
	    for j in range(n):
		    array[i].append(0)
	return array
