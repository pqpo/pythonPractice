class chain(object):

	def __init__(self,path=''):
		self.__path = path


	def __getattr__(self,path):
		return chain('%s/%s'%(self.__path,path))

	def __str__(self):
		return self.__path

	def __call__(self,name):
		return chain('%s/:%s'%(self.__path,name))


if __name__ == '__main__':
	print chain().users('michael').repos