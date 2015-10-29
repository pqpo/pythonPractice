class Student:

	className = 'Student'

	def __init__(self,name,score):
		self.name = name
		self.score = score 

	@classmethod
	def classMethon(cls):
		print cls.__name__

	@staticmethod
	def staticMethon():
		print 'Staic Methon'

	def printStu(self):
		print '%s   name:%s  score:%s' % (Student.className,self.name,self.score)


stu = Student('Tom',98)

stu.printStu();
stu.classMethon();
stu.staticMethon();

Student.classMethon();
Student.staticMethon();
#Student.printStu();