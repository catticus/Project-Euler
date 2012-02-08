#!/usr/bin/env python

from libeuler import nCr

N = 100
L = 1000000

count = 0
for n in xrange(1, N + 1):
	for r in xrange(1, n + 1):
		if (nCr(n, r) > L):
			count += 1

print count

