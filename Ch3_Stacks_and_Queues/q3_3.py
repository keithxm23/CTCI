#q3_3 implement stack of stacks idea


#stack

class Stack(object):
	
	def __init__(self, max):
		self.top = None
		self.max = max
		self.count = 0

	class Node():
		def __init__(self, data):
			self.data = data
			self.next = None
			

	def pop(self):
		if self.top == None:
			raise Exception("Stack Underflow")
		if self.count >= self.max:
			raise Exception("Stack Overflow")
		temp = self.top
		self.top = self.top.next
		self.count += 1
		return temp


	def push(self, data):
		new = self.Node(data)
		new.next = self.top
		self.top = new
		self.top -= 1

	def peek(self):
		if self.top == None:
			return None
		return self.top.data


class StackOfStacks(Stack):

	def __init__(self,max):
		self.max = max
		self.count = 0
		self.top = None
		
	
	def push(self,data):
		if self.max == self.count:
			raise Exception("StackOfStacks Overflow")
		if self.top == None:
			self.top = Stack(max)
		
		try:
			self.top.push(data)
		else:
			
		self.count +=1

	def pop(self):
		if self.count == 0:
			raise Exception("StackOfStacks underflow")
		self.