#!/usr/bin/env python

def reverse (x):
	rev = 0
	while x > 0:
		rev *= 10
		rev += x%10
		x /= 10
	return rev

def is_palindrome (x):
	return (x == reverse(x))

max_pp = 0
for a in xrange(100, 1000):
	for b in xrange(100, 1000):
		if is_palindrome(a*b):
			max_pp = max(a*b, max_pp)

print max_pp
