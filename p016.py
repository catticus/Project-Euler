#!/usr/bin/env python

from libeuler import digital_sum

N = 1000

x = 2**N
y = digital_sum(x)

print y
