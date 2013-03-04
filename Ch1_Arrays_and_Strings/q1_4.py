#replace all spaces in a string with %20

str = raw_input("Enter an string: \n")

spacecount = str.count(" ")

str = list(str)
strlen = len(str)

for i in xrange(0,spacecount*2):
	str.append("")
print str
index = len(str)-1
for j in xrange(strlen-1,-1,-1):
	print str[j]
	if str[j] == " ":
		str[index] = "0"
		str[index-1] = "2"
		str[index-2] = "%"
		index -= 3
	else:
		str[index] = str[j]
		index -= 1

print "".join(str)