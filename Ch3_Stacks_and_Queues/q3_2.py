#minStack
from stacks import Stack

class minStack(Stack):
	
	def __init__(self):
		super(minStack,self).__init__()
		self.minSta = Stack()
			

	def pop(self):
		if self.minSta.peek() != None and self.minSta.peek() >= self.peek():
			self.minSta.pop()
		return super(minStack, self).pop()

	def push(self, data):
		if self.minSta.peek() == None or self.minSta.peek() >= data:
			self.minSta.push(data)
		super(minStack, self).push(data)

	def peek(self):
		return super(minStack, self).peek()

	def min(self):
		return self.minSta.peek()

#Test
s = minStack()
#s.pop()

for x in [4,5,1,3,2,7,8,5,3,2,2,2]:
	s.push(x)

print s.min()
print s.pop().data

print s.min()
print s.pop().data

print s.min()
print s.pop().data

print s.min()
print s.pop().data

print s.min()
print s.pop().data

print s.min()
print s.pop().data


print s.min()
print s.pop().data

print s.min()
print s.pop().data
print s.min()
print s.pop().data

print s.min()
print s.pop().data
