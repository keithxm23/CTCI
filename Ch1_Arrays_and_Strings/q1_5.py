#Compress a string: e.g. aabcccccaaa > a2b1c5a3

import sys

#first iterate and check if number of changes in consecutive chars are equal to length of string
#worth doing compression only if at least one sequence of 3 repeated chars exist
#so we check if num of changes > len(string)/2
#e.g. aabbccdd = a2b2c2d2 .. not worth it
#e.g. aabbbccdd = a2b3c2d2 .. worth it. saved one char.

string = raw_input("Enter an string: \n")

if str == "":
	print "No input string given. Program terminated"
	sys.exit()

changecount = 1

string = list(string)

for i in xrange(0,len(string)- 1):
	if string[i] != string[i+1]:
		changecount += 1

print changecount

if changecount >= len(string)/2:
	print "".join(string)
	sys.exit()

#else compress the string
compressedstr = []

prev = string[0]
count = 1
for i in xrange(1, len(string)):
	if prev != string[i]:
		compressedstr += [prev, str(count)]
		count = 0
	prev = string[i]
	count += 1

compressedstr += [prev, str(count)]

print "".join(compressedstr)