#!/usr/bin/env python

from libeuler import is_prime

max_n = 0
max_a = 0
max_b = 0
for a in xrange(-1000, 1000):
	for b in xrange(-1000, 1000):
		f = lambda n : n**2 + a*n + b

		n = 0
		while True:
			if is_prime(f(n)):
				n += 1
			else:
				break

		if n > max_n:
			max_n = n
			max_a = a
			max_b = b

print max_a * max_b

