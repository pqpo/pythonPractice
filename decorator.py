import functools
def log(logname):
	def decorator(fun):
		@functools.wraps(func)
		def wapper(*arg,**kw):
			print '[%s] function called:%s' % (logname,fun.__name__)
			return fun(*arg,**kw)
		return wapper
	return decorator


@log('Now')
def now():
	return '1993.11.2'


print now()