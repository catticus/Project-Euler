#!/usr/bin/env python

memo = {0:1, 1:1}

def fib (n):
	if n < 0:
		return 0

	if not memo.has_key(n):
		memo[n] = fib(n-1) + fib(n-2)

	return memo[n]

# fib(100) >> 4,000,000,
# so let n range to 100.
total = 0
for n in xrange(100):
	fib_n = fib(n)
	if fib_n > 4000000:
		break
	if (fib_n%2 == 0):
		total += fib_n

print total

