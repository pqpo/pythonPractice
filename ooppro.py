class Student(object):

	__slots__ = ('__name','__age','__score')

	def __init__(self,name='unknow',age=0,score=0):
		self.__name = name
		self.__age = age 
		self.__score = score 

	@property
	def name(self):
		return self.__name 

	@name.setter 
	def name(self,name):
		self.__name = name

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self,age):
		self.__age = age

	def __str__(self):
		return '%s:%s:%s'%(self.name,self.age,self.__score)

	__repr__ = __str__

	def __len__(self):
		return self.__score

	def __getattr__(self,attr):
		pass

if __name__ == '__main__':
	stu = Student('tom',23,88)
	print stu.name 
	print stu.age
	stu.age = 88
	print stu.age
	print stu
	print len(stu)


