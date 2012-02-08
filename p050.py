#!/usr/bin/env python

from libeuler import is_prime

N = 1000000

# the longest sequence under 1000 has length 21,
# so by way of hand-waving,
# we limit our search to lengths less than N/21.
M = 21

print "Finding primes."
L = xrange(2, N)
primes = filter(is_prime, L)
print "Done."

max_seq = None
cur_len = len(primes) / M
while not max_seq:
	#print "Checking length:", cur_len
	lim = len(primes) - cur_len
	for beg in xrange(lim):
		end = beg + cur_len
		seq = primes[beg:end]
		if sum(seq) > N:
			break
		if sum(seq) in primes:
			max_seq = seq
			break
	cur_len -= 1

print
print len(max_seq), " -> ", max_seq
print
print sum(max_seq)

