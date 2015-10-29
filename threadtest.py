import time,threading,random

def loop():
	print 'thread %s is running.....\r\n'% threading.current_thread().name
	for n in range(5):
		print 'thread %s>>>>%s'%(threading.current_thread().name,n)
		time.sleep(random.random()*3)
	print 'thread %s ended'%threading.current_thread().name 

if __name__ == '__main__':
	thread1 = threading.Thread(target=loop)
	thread2 = threading.Thread(target=loop)
	thread3 = threading.Thread(target=loop)
	thread4 = threading.Thread(target=loop)

	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

