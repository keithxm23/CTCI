#implement reverse of a string

import sys

if len(sys.argv) < 2:
	raise Exception("Please provide input string. Run 'python q1_2.py <string-here>'")
else:
	str = sys.argv[1]


str = list(str)
for c in xrange(0,len(str)/2):
	temp = str[c]
	str[c] = str[len(str)-c-1]
	str[len(str)-c-1] = temp

print "".join(str)