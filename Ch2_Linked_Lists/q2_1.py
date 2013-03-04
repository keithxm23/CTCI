#remove duplicates from an unsorted linked list

from ll import Node

data = raw_input("Enter linked list nodes separate by space e.g. 1 2 3 2 4 9: ")

data = data.split()

head = Node(data[0])

current = head
for x in xrange(1,len(data)):
	current.next = Node(data[x])
	current = current.next
current.next = None


print "Before removing duplicates: "
current = head
while(current != None):
	print current.data
	current = current.next




seen = set()
prev = head
seen.add(prev.data)
current = head.next

while(current != None):
	if current.data in seen:
		prev.next = current.next
		#remove this node
	else: #GOTCHA!: Be sure to increment the prev to next only when there is no deletion.. since if there is a deleting the previous node remains previous for the next node
		prev = current
	seen.add(current.data)
	current = current.next


print "After removing duplicates: "
current = head
while(current != None):
	print current.data
	current = current.next

