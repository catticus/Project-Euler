#!/usr/bin/env python

from math import factorial
from libeuler import digital_split

vals = []
for x in xrange(3, 100000):
	digits = digital_split(x)
	y = sum(map(factorial, digits))
	if x == y:
		vals += [x]

print sum(vals)
