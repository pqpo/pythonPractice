from multiprocessing import Pool
import time,random,os

__author__ = 'pqpo'

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
    return end-start

def callback(result):
    print result

if __name__ == '__main__':
    p = Pool()
    p.apply_async(long_time_task,('task',),{},callback)

    p.close()
    p.join()