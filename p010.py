#!/usr/bin/env python

from libeuler import is_prime

N = 2000000

L = xrange(2, N)
primes = filter(is_prime, L)

print sum(primes)

