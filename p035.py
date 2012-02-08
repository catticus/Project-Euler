#!/usr/bin/env python

from libeuler import is_prime, digital_split

N = 1000000

def is_circ_prime (n):
	if not is_prime(n):
		return False

	digits = digital_split(n)
	count = len(digits) - 1
	f = lambda x, y: ((x * 10) + y)

	for i in xrange(count):
		digits.append(digits.pop(0))
		m = reduce(f, digits)
		if not is_prime(m):
			return False

	return True

x = map(is_circ_prime, xrange(N))
y = filter(None, x)
print len(y)

