#!/usr/bin/env python
# -*- coding: UTF-8 -*-

fileObject = open('1.txt')
try:
	all_line_the_text = fileObject.readlines()
	for line in range(0,len(all_line_the_text)):
		print all_line_the_text[line],
finally:
	fileObject.close()
