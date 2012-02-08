#!/usr/bin/env python

from libeuler import digital_length

# Assume that exponents beyond 100 will fail.

count = 0

for exp in xrange(100):
	base = 0
	len_power = 0

	while (len_power <= exp):
		base += 1
		len_power = digital_length(base**exp)

		if (len_power == exp):
			count += 1

print count

