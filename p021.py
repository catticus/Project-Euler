#!/usr/bin/env python

from libeuler import find_divs

N = 10000

amicable = set()
for a in xrange(N):
	b = sum(find_divs(a))
	c = sum(find_divs(b))
	if (a == c) and (a != b):
		amicable.add(a)
		amicable.add(c)

print sum(amicable)

