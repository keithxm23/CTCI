#implement algo to find the kth to last element of a singly linked list

from ll import Node

data = raw_input("Enter linked list nodes separate by space e.g. 1 2 3 2 4 9: ")

data = data.split()

head = Node(data[0])

current = head
for x in xrange(1,len(data)):
	current.next = Node(data[x])
	current = current.next
current.next = None

k = int(raw_input("Enter the index of the kth last element you want to locate"))
if k >= len(data):
	raise Exception("Index out of bounds")


now = head
kLate = None

count = 0

while (now != None):
	if count == k:
		kLate = head
	count += 1
	now = now.next
	if kLate != None:
		kLate = kLate.next

print kLate.data