#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import sys

for i in range(1, 15):
	for j in range(1,i+1):
		print "%s %s\t" % (j,i),
	print " "
