#!/usr/bin/env python

N = 100

f = lambda x: x**2
L = xrange(1, N+1)
sum_of_squares = sum(map(f, L))
square_of_sums = sum(L)**2
diff = square_of_sums - sum_of_squares

print diff

