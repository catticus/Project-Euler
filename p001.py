#!/usr/bin/env python

def f (x):
	return (x%3 == 0) or (x%5 == 0)

total = sum(filter(f, xrange(1000)))

print total

