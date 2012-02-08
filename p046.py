#!/usr/bin/env python

from libeuler import is_prime

def is_goldbach (n, primes, squares):
	if is_prime(n):
		return True
	for p in primes:
		for s in squares:
			if (n == p + (2 * s)):
				return True
	return False

primes = [2, 3]
squares = [1, 4]
sq_cnt = 2
next_sq = 9

n = 5
while True:
	if is_prime(n - 1):
		primes += [n - 1]
	elif is_prime(n):
		primes += [n]

	if (n - 1 == next_sq):
		squares += [n - 1]
		sq_cnt += 1
		next_sq = (sq_cnt + 1)**2
	elif (n == next_sq):
		squares += [n]
		sq_cnt += 1
		next_sq = (sq_cnt + 1)**2

	flag = is_goldbach(n, primes, squares)
	if not flag:
		break

	n += 2

print n

