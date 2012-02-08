#!/usr/bin/env python

# read raw file.
with open("p022.txt", "r") as f:
	A = f.readline()

# parse file into list.
s = lambda x : x.strip("\"")
B = A.split(",")
names = map(s, B)

# sort list.
names.sort()

# compute!
total = 0
w = lambda x : ord(x) - 64
for i, name in enumerate(names):
	value = sum(map(w, name))
	total += (i+1) * value

print total

