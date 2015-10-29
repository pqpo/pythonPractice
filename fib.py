class Fib(object):

	def __init__(self):
		self.a = 0
		self.b = 1

	def next(self):
		self.a,self.b = self.b,self.a+self.b
		return self.a

	def __iter__(self):
		return self

	def __getitem__(self,n):
		fib = Fib()
		result = fib.next()
		for x in xrange(0, n):
			result = fib.next()
		return result

if __name__ == '__main__':
	fib = Fib()
	for x in xrange(0,100):
		print fib[x]