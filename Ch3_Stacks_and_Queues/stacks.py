#stack

class Stack(object):
	
	def __init__(self):
		self.top = None

	class Node():
		def __init__(self, data):
			self.data = data
			self.next = None
			

	def pop(self):
		if self.top == None:
			raise Exception("Stack Underflow")
		temp = self.top
		self.top = self.top.next
		return temp


	def push(self, data):
		new = self.Node(data)
		new.next = self.top
		self.top = new

	def peek(self):
		if self.top == None:
			return None
		return self.top.data

"""
#Test
s = Stack()
#s.pop()

for x in xrange(1,10):
	s.push(x)

print s.peek()
x = s.pop()
print x.data
print s.peek()
"""