#!/usr/bin/env python

from math import log

N = 10

A = []
with open("p013.txt", "r") as f:
	for line in f:
		n = int(line.strip("\n"))
		A += [n]

x = sum(A)
y = int(log(x)/log(10))
z = 10**(y - (N - 1))

print x/z

