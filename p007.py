#!/usr/bin/env python

from libeuler import is_prime

N = 10001

num = 1
count = 0
while count < N:
	num += 1
	if is_prime(num):
		count += 1

print num

