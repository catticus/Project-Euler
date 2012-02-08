#!/usr/bin/env python

N = 1000000

def collatz (n):
	if (n % 2 == 0):
		return (n/2)
	else:
		return (3*n + 1)

lengths = {}
for i in xrange(1, N):
	cur = i
	cnt = 1
	while cur != 1:
		if lengths.has_key(cur):
			cnt += lengths[cur]
			cur = 1
		else:
			cnt += 1
			cur = collatz(cur)
	lengths[i] = cnt

rev = [(v,k) for (k,v) in lengths.iteritems()]
rev.sort(reverse=True)

print rev[0][1]

