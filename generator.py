#1,1,2,3,5,8,13

def fib():
	a = 0
	b = 1
	while True:
		yield b
		c = a
		a = b
		b = c + b


o = fib()
for x in xrange(0, 100, 1):
	print o.next()