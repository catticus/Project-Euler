#!/usr/bin/env python

from itertools import permutations

N = 1000000

f = lambda x, y: ((x * 10) + y)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = permutations(x)

for i in xrange(N-1):
	y.next()
n = reduce(f, y.next())

print n

