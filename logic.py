'''logic a function of filename logic is a key component of whole snippet
takes input m,n and matrix on which logic is to be performed and returning the same matrix
after the operation'''


#logic takes m,n and deeeply copied matrix l2 as parameter
#operations are performed on l2
def logic(m,n,l2):
	j = 0
	for l in range(m):                                   
	    for i in range(l,m):
		    if l2[i][j]!=0:						# checking if 1st element is 0 or not
			    for j in range(n-1,0,-1):		#if not then dividing whole row with checked element
				    l2[i][j]=l2[i][j]/l2[i][l]
		    else:
			    for k in range(i+1,n):
				    if l2[k][l]!=0:				# if element is zero replacing the whole row with consecutive
					    for j in range(l,n):
						    d=l2[i][j]
						    l2[i][j]=l2[k][j]
						    l2[k][j]=d
						    break
			    if l2[i][l]!=0:					# further checking element of next row and column
				    for j in range(n-1,l+1,-1): # if not zero dividing whole row with checked element
					    l2[i][j]=l2[i][j]/l2[i][l]
	    for i in range(l+1,m):					# and so on till we reach last row
		    for j in range(l,n):
			    if l2[i][j]!=0:
				    l2[i][j]=l2[i][j]-l2[l][j]
	return l2
	# returning l2 after operation as echelon form matrix