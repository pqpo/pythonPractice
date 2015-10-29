import decorator

l = [36, 5, 12, 9, 21]

def reversed_cmp(x, y):
	if x>y:
		return -1
	elif x==y:
		return 0
	return 1
	

print sorted(l,reversed_cmp)