#!/usr/bin/env python

from libeuler import count_divs

N = 500

def gen_triangle ():
	n = 1
	tri = 1
	while True:
		yield tri
		n += 1
		tri += n

trigen = gen_triangle()
for x in trigen:
	count = count_divs(x)
	if count > N:
		break

print x

