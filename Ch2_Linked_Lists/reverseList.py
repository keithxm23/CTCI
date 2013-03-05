#reverse a list

from ll import Node
import copy

data = raw_input("Enter linked list nodes separate by space e.g. 1 2 3 2 4 9: ")

data = data.split()

head = Node(data[0])

current = head
for x in xrange(1,len(data)):
	current.next = Node(data[x])
	current = current.next
current.next = None


def reverse(node):
	last = None
	curr = node
	while(curr != None):
		nxt = curr.next
		curr.next = last
		last = curr
		curr = nxt
	return last

tmp = reverse(head)

while (tmp != None):
	print tmp.data
	tmp = tmp.next