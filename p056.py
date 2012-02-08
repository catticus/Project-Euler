#!/usr/bin/env python

from libeuler import digital_sum

max_ds = 0
for a in xrange(1, 100):
	for b in xrange(1, 100):
		ds = digital_sum(a**b)
		max_ds = max(ds, max_ds)

print max_ds
