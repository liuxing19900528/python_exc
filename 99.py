#!/usr/bin/env python
# -*- coding: UTF-8 -*-

for i in range(1,10):
    for j in range(1,10):
        print "%d*%d=%2d" % (i,j,i*j),
    print "\n"

print "----------------------------------------------------------------\n"

for i in range(1,10):
    for j in range(i,10):
        print "%d*%d=%2d" % (i,j,i*j),
    print "\n"

print "----------------------------------------------------------------\n"

for i in range(1,10):
    for k in range(1,i):
        print "      ",
    for j in range(i,10):
        print "%d*%d=%2d" % (i,j,i*j),
    print "\n"

print "----------------------------------------------------------------\n"

for i in range(1,10):
    for j in range(1,i+1):
        print "%d*%d=%2d" % (i,j,i*j),
    print "\n"

print "----------------------------------------------------------------\n"

for i in range(1,10):
    for k in range(1,10-i):
        print "      ",
    for j in range(1,i+1):
        print "%d*%d=%2d" % (i,j,i*j),
    print "\n"