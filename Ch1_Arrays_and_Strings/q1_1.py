#Determine if string has unique characters

import sys

if len(sys.argv) < 2:
	raise Exception("Please provide input string. Run 'python q1_1.py <string-here>'")
else:
	str = sys.argv[1]


"""
#By using a set
seen = set()
for c in str:
	if c in seen:
		print "The string does not have unique characters."
		sys.exit()
	seen.add(c)

print "The string has unique characters."
"""


#By sorting
str = sorted(str)
for c in xrange(0,len(str)-1):
	if str[c] == str[c+1]:
		print "The string does not have unique characters."
		sys.exit()

print "The string has unique characters."