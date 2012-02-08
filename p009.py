#!/usr/bin/env python

from sys import exit

N = 1000

lim = N - 3
for i in xrange(1, lim):
	for j in xrange(i, lim):
		for k in xrange(j, lim):
			if (i + j + k == N):
				if (i**2 + j**2 == k**2):
					ans = i*j*k
					print "%d * %d * %d = %d" % (i, j, k, ans)
					exit(0)

