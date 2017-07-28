#!/usr/bin/env python

count = 0
for index,line in enumerate(open('ZSUI_DEV_APK_20161011.xml', 'r')):
    count += 1
    print index, count, line

