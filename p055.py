#!/usr/bin/env python

from libeuler import digital_reverse, is_digital_palindrome

def is_lychrel (n, bound=50):
	for i in xrange(bound):
		n += digital_reverse(n)
		if is_digital_palindrome(n):
			return False
	return True

x = xrange(10000)
y = map(is_lychrel, x)
z = filter(None, y)

print len(z)

