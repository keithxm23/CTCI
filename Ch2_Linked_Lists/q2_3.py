#delete a node in the middle of a singly linked list given access only to that node

#NOTE: Cannot delete the last node of a linked list if you are only given that node
from ll import Node

data = raw_input("Enter linked list nodes separate by space e.g. 1 2 3 2 4 9: ")

data = data.split()

head = Node(data[0])

current = head
for x in xrange(1,len(data)):
	current.next = Node(data[x])
	current = current.next
current.next = None


def deleteNode(node):
	current = node
	while(current.next != None):
		current.data = current.next.data
		prev = current
		current = current.next
	prev.next = None #GOTCHA! Be sure to set the next of the last element to none

#deletes the 5th element
deleteNode(head.next.next.next.next)


current = head
while (current != None):
	print current.data
	current = current.next