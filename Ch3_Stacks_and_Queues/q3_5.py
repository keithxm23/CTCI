#implement queue using two stacks


from stacks import Stack

class Queue():

	def __init__(self):
		self.base = Stack()
		self.buff = Stack()

	#insertion in O(n)
	def enqueue(self, data):
		while(True):
			try:
				self.buff.push(self.base.pop().data)
			except:
				self.base.push(data)
				while(True):
					try:
						self.base.push(self.buff.pop().data)
					except:
						break
				break

	#removal in O(1)
	def dequeue(self):
		return self.base.pop()
	


q= Queue()

for x in [1,2,3,4,5,6,7,8,9,0]:
	q.enqueue(x)

print q.dequeue().data
print q.dequeue().data

print q.dequeue().data

