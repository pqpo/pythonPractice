#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time


def powerBetter(x,n=2):
	if n == 1:
		return x
	if n%2==0:
		return power(x,n/2)*power(x,n/2)
	else:
		return x*power(x,n/2)*power(x,n/2)


def power(x,n=2):
	result = 1
	while n>0:
		result = result*x
		n = n - 1
	return result	

beginTime = time.time()
powerBetter(2,100000)
time1 = time.time() - beginTime

beginTime = time.time()
power(2,100000)
time2 = time.time() - beginTime

print time1
print time2

