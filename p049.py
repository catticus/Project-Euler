#!/usr/bin/env python

from libeuler import is_prime, digital_split, find_prime_factors

M = 1000
N = 10000

def are_digital_permutations (x, y, z):
	f = lambda x, y: ((x * 10) + y)
	a = digital_split(x)
	b = digital_split(y)
	c = digital_split(z)
	a.sort()
	b.sort()
	c.sort()
	A = reduce(f, a)
	B = reduce(f, b)
	C = reduce(f, c)
	return (A == B == C)

L = xrange(M, N)
primes = filter(is_prime, L)

seq = None
step = 3330
for p1 in primes:
	p2 = p1 + step
	p3 = p2 + step
	if (p3 > N):
		break
	if are_digital_permutations(p1, p2, p3) \
		and is_prime(p2) \
		and is_prime(p3) \
		and (p1 != 1487):
			seq = (p1, p2, p3)
			break

f = lambda x, y: ((x * 10000) + y)
print reduce(f, seq)

