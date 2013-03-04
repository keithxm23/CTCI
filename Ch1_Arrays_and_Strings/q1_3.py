#Check if one string is permutation of the other

import sys

if len(sys.argv) != 3:
	raise Exception("Please provide input string. Run 'python q1_3.py <string-here> <string-here>'")
else:
	str1 = sys.argv[1]
	str2 = sys.argv[2]


"""
#method1 by sorting both

if sorted(str1) == sorted(str2):
	print "Strings are anagrams of each other"
else:
	print "strings are not anagrams of each other"

"""

#method2: by counting occurences of each char in both


count = {}


str1 = list(str1)
str2 = list(str2)

if len(str1) != len(str2):
	print "Strings are not anagrams of each other"
	sys.exit()
else:
	for i in xrange(0,len(str1)):
		if str1[i] in count:
			count[str1[i]] +=1 
		else:
			count[str1[i]] = 1

		if str2[i] in count:
			count[str2[i]] -= 1 
		else:
			count[str2[i]] = -1


for key, value in count.items():
	if value != 0:
		print "Strings are not anagrams of each other"
		sys.exit()

print "Strings are anagrams of each other"
		