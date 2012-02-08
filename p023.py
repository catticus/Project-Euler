#!/usr/bin/env python

from libeuler import find_divs
from itertools import combinations_with_replacement

N = 28124

def is_abundant (n):
	m = sum(find_divs(n))
	return (m > n)

abundants = []
for i in xrange(1, N):
	if is_abundant(i):
		abundants += [i]

is_a_sum = [False] * N
for a, b in combinations_with_replacement(abundants, 2):
	if (a + b < N):
		is_a_sum[a + b] = True

not_abundant_sums = [i for (i, n) in enumerate(is_a_sum) if not n]

print sum(not_abundant_sums)

