#!/usr/bin/env python

N = 1000

num_digits = 10
mod_factor = 10**num_digits

tower = lambda x: x**x

L = xrange(1, N + 1)
x = map(tower, L)
y = sum(x)

print y % mod_factor
