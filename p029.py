#!/usr/bin/env python

N = 100

terms = {}
for a in xrange(2, N+1):
	for b in xrange(2, N+1):
		val = a**b
		terms[val] = 1

print len(terms)
