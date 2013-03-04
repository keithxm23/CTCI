#rotate NxN matrix inplace
n = int(raw_input("Enter size of the matrix"))

matrix = []

for i in xrange(0,n):
	temp = []
	for j in xrange(0,n):
		temp.append(str(i)+str(j))
	print temp
	matrix.append(temp)


print "\n\n"

#rotating clockwise
for j in xrange(0,n/2):
	for k in xrange(j,n-j-1):
		#backup bottom left
		temp = matrix[n-1-j-k][j]
		
		#bottom right to bottom left
		matrix[n-1-j-k][j] = matrix[n-1-j][n-1-j-k]

		#top right to bottom right
		matrix[n-1-j][n-1-j-k] = matrix[j+k][n-1-j]

		#top left to top right
		matrix[k][n-1-j] = matrix[j][j+k]

		#bottom left to top left
		matrix[j][j+k] = temp


for x in matrix:
	print x

		