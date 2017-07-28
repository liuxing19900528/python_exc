#!/usr/bin/env python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8]
    b = [1,5,8,9,0,3,1]
    N = len(a)
    print a
    for i in range(len(a) / 2):
        a[i],a[N-i-1] = a[N-i-1],a[i]
    print a

    print b
    b.reverse()
    print b
