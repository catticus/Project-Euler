#!/usr/bin/env python

from libeuler import digital_split

N = 5

f = lambda x: int.__pow__(x, N)

vals = []
lim = N * 9**N
for x in xrange(2, lim):
	digits = digital_split(x)
	y = sum(map(f, digits))
	if x == y:
		vals += [x]

print sum(vals)
