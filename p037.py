#!/usr/bin/env python

from libeuler import is_prime, digital_split

N = 11

def is_trunc_prime (n):
	if not is_prime(n):
		return False

	digits = digital_split(n)

	count = len(digits) - 1
	f = lambda x, y: ((x * 10) + y)

	for i in xrange(count):
		digits.pop(0)
		m = reduce(f, digits)
		if not is_prime(m):
			return False

	digits = digital_split(n)

	for i in xrange(count):
		digits.pop(-1)
		m = reduce(f, digits)
		if not is_prime(m):
			return False

	return True

n = 10
primes = []
count = 0
while (count < N):
	n += 1
	if is_trunc_prime(n):
		print count, " : ", n
		primes += [n]
		count += 1

print
print sum(primes)

