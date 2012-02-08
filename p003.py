#!/usr/bin/env python

from libeuler import is_prime

x = 600851475143.

end = int(x**.5) + 1
for i in xrange(end, 1, -1):
	if (x % i == 0):
		print "Factor: %d" % i
		if is_prime(i):
			print i
			break

