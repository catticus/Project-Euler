#!/usr/bin/env python

from libeuler import is_prime
from itertools import permutations

f = lambda x, y: ((x * 10) + y)

x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
y = permutations(x)
print x

while True:
	try:
		n = reduce(f, y.next())
		if is_prime(n):
			break
	except StopIteration:
		x.pop(0)
		y = permutations(x)
		print x

		if len(x) == 0:
			print "Search failed!"
			n = 0
			break

print
print n

