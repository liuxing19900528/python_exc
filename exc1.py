#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
d=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                d.append('%d%d%d' % (i,j,k))

print "counts is:", len(d)
print d
