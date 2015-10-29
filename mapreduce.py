def add(x,y):
	return x+y

def plus(x,y):
	return x*y

def power(x):
	return x**2

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2num(str):
	return map(char2num, str)

def fn(x,y):
	return x*10+y

def str2int(str):
	return reduce (lambda x,y:x*10+y,str2num(str))

def titleCase(names):
	def title(name):
		return name[0].upper()+name[1:].lower()
	return map(title, names)

print titleCase(['adam', 'LISA', 'barT'])