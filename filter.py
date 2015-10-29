def getprime(max):
	return [x for x in range(1,max) if  not [p for p in range(2,x) if x%p==0]]

def is_prime(x):
	for n in range(2,x):
		if x%n==0:
			return False
	return True		

print filter(lambda x:not is_prime(x), range(101))