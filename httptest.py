#!/usr/bin/env python
# -*- coding:utf-8 -*-

import httplib
import logging

__author__ = 'pqpo'

httpClient = None

try:
    print 'start'
    httpClient = httplib.HTTPConnection('www.baidu.com',timeout=30)
    httpClient.request('GET','')
    response = httpClient.getresponse()
    if response.status==200:
        print response.length
        print response.read(response.length)
except BaseException , e:
    logging.exception(e)
    raise BaseException('ddddddd')
finally:
    if httpClient:
        httpClient.close()
