#!/usr/bin/env python
# -*- coding:utf-8 -*-

mkw = {'name':'Tom','age':'23'}

def show(**kw):
	for k in kw:
		print '%s : %s' % (k,kw[k])
	return	

show(**mkw)
