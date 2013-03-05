#partition a list around a value x

from ll import Node
import copy

data = raw_input("Enter linked list nodes separate by space e.g. 1 2 3 2 4 9: ")
num = int(raw_input("Enter a value x around which you want to partition the list: "))

data = data.split()

head = Node(int(data[0]))

current = head
for x in xrange(1,len(data)):
	current.next = Node(int(data[x]))
	current = current.next
current.next = None


#current points to the last node right now
lessThanX = head
greaterThanX = current
end = current
prev = None

"""
current = head
while(current != None):
	print current.data
	current = current.next
"""

cur = head
while not(cur is end):
	if lessThanX.data > num:
		if head == lessThanX:
			print "head is ltx"
			head = lessThanX.next
			prev = None
		else:
			prev.next = lessThanX.next

		print "moving large " + str(lessThanX.data)
		temp = copy.copy(lessThanX) #GOTCHA
		temp.next = None
		greaterThanX.next = temp
		lessThanX = lessThanX.next			
		greaterThanX = temp
		
	else:
		print "moving from " + str(lessThanX.data) + " to "+ str(lessThanX.next.data)
		prev = lessThanX
		lessThanX = lessThanX.next
		

current = head
while(current != None):
	print current.data
	current = current.next