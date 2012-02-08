#!/usr/bin/env python

from fractions import Fraction

curious = []

for i in xrange(1, 100):
	for j in xrange(1, 100):
		i1 = i/10
		i2 = i%10

		j1 = j/10
		j2 = j%10

		if (j2 == 0):
			# divide by zero.
			continue

		if (i2 == 0) and (j2 == 0):
			# trivial example.
			continue

		if (i1 == i2) and (j1 == j2):
			# trivial example.
			continue

		ij = float(i)/j
		i1j2 = float(i1)/j2

		if (i2 == j1) and (ij == i1j2) and (i1j2 < 1.0):
			curious += [Fraction(i,j)]
			print "%d/%d = %f <==> %f = %d/%d" % (i, j, ij, i1j2, i1, j2)

print reduce(Fraction.__mul__, curious)

