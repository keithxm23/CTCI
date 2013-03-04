#write an algo such that if, in an MxN matrix if an element is 0.. change its entire row and column to 0

matrix = [[1,5,9,0,3,5],[1,5,9,1,3,0],[1,5,9,1,3,5],[1,25,0,0,3,5],]

for m in matrix:
	print m

#first scan for zeros and record rownumbers and column numbers for which zero exists

zerorows = set()
zerocols = set()

for i in xrange(len(matrix)): #iterating over rows
	for j in xrange(len(matrix[i])): #iterating over columns
		if matrix[i][j] == 0:
			zerorows.add(i)
			zerocols.add(j)

print zerorows, zerocols


for x in zerorows:
	matrix[x] = [0]*len(matrix[x])

for x in zerocols:
	for j in xrange(len(matrix)):
		matrix[j][x] = 0


for m in matrix:
	print m