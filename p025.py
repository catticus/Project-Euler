#!/usr/bin/env python

from math import log

N = 1000
lim = (N-1) * log(10)

def fib_gen ():
	count = 1
	prev = 0
	curr = 1
	while True:
		yield count, curr
		count += 1
		temp = curr
		curr += prev
		prev = temp

# stop search when:
# log(x)/log(10) > N-1
fib = fib_gen()
for n,x in fib:
	if log(x) > lim:
		break

print n
