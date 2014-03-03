#!/usr/bin/env python
import sys
terse = "-t" in sys.argv[1:] or "--terse" in sys.argv[1:]

for i in range(2 if terse else 10):
    for j in range(30, 38):
        for k in range(40, 48):
            if terse:
                print "\33[%d;%d;%dm%d;%d;%d\33[m " % (i, j, k, i, j, k),
            else:
                print ("%d;%d;%d: \33[%d;%d;%dm Hello, World! \33[m " %
                    (i, j, k, i, j, k, ))
        print 
