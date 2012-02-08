#!/usr/bin/env python

from libeuler import digital_reverse

N = 1000000

def is_dec_palindrome (n):
	return (n == digital_reverse(n))

def is_bin_palindrome (n):
	bin_num = bin(n)[2:]
	bin_rev = ''.join(reversed(bin_num))
	return (bin_num == bin_rev)

P = []
for n in xrange(N):
	if is_dec_palindrome(n) and is_bin_palindrome(n):
		P += [n]

print sum(P)

