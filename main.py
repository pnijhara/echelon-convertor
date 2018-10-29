""" echelon convertor is a code snippet to convert any mxn matrix to it respective echelon form
code accepts an integer tyoe valure from user as m for rows and n for columns
further asks user for matrix input of float or integer type
which will later return a matrix converted to echelon form"""


# imorting functions from other files
from logic import logic
from dublicate import dublicate
from dublicate import intialize
matrix=[]
l2=[]


#entry1 takes input from user 
#m as rows and n as columns as integer type
def entry1():
	while True:
		try:
			m=int(input("enter number of rows >>>  \n"))
			n=int(input("enter number of columns >>>  \n"))
			break
		except ValueError:
			print("please enter integer type value only")
	return m,n

#entry2 uses entry1's return as parameter and an empty matrix as parameter for input
def entry2(m,n,matrix):

	#intializing input matrix using intialize function from dublicate file
    matrix = intialize(m,n,matrix)
    #input in matrix as float or int type
    for i in range (m):
        for j in range (n):
            print ('entry in row: ',i+1,' column: ',j+1)

            #applying try and except if user gives an input other than prescribed type
            while True:
            	try:
            		matrix[i][j] = float(input())
            		break
            	except ValueError:
            		print("no special characters are allowed \nplease enter valid float or integer type value")
    return matrix

''' calling all functions seperately from main as well from other files'''
#calling entry1
m,n=entry1()

#calling entry2
mat = entry2(m,n,matrix)

#initialzing l2 and creating a deep copy of matrix in l2
l2 = intialize(m,n,l2)
l2 = dublicate(m,n,mat,l2)
ans = logic(m,n,l2)
print(ans)
