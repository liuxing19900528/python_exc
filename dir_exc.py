#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

def search(postfix, d = os.path.abspath('.')):
	for i in os.listdir(d):
		path = os.path.join(d,i)
		if os.path.isfile(path) and os.path.splitext(path)[1] == postfix:
			print path
			#print os.path.splitext(path)[0]
		if os.path.isdir(path):
			search(postfix,path)

if __name__=='__main__':
	print 'begin'
	search(sys.argv[1])
	print 'done'
