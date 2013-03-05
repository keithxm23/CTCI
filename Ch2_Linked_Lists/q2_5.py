#sum two numbers given as linked lists

from ll import Node
import copy

num1 = raw_input("Enter the first number: ")
num2 = raw_input("Enter the second number: ")


numA = None
for x in num1:
	temp = Node(int(x))
	temp.next = numA
	numA = temp

numB = None
for x in num2:
	temp = Node(int(x))
	temp.next = numB
	numB = temp

carry = 0
sum = None
curA = numA
curB = numB

while(curA != None or curB != None):
	if curA == None:
		Aval = 0
		Bval = curB.data
		curB = curB.next
	elif curB == None:
		Bval = 0
		Aval = curA.data
		curA = curA.next
	else:
		Bval = curB.data
		Aval = curA.data
		curA = curA.next
		curB = curB.next

	data = (carry + Aval + Bval) % 10
	carry = (carry + Aval + Bval) / 10 
	if sum == None:
		sum = Node(data)
		sumhead = sum
	else:
		temp = Node(data)
		sum.next = temp
		sum = sum.next

if carry != 0:#GOTCHA!! Check if carry is 0
	sum.next = Node(carry)
cur = sumhead
while(cur != None):
	print cur.data
	cur = cur.next