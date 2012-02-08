#!/usr/bin/env python

from libeuler import find_prime_factors

N = 21

pf_list = [[]] * N
for i in xrange(2, N):
	pf_list[i] = find_prime_factors(i)

pfc_list = [0] * N
for i in xrange(2, N):
	max_pfc = 0
	for pf in pf_list:
		pfc = pf.count(i)
		max_pfc = max(pfc, max_pfc)
	pfc_list[i] = max_pfc

lcm = 1
for x,y in enumerate(pfc_list):
	if (y > 0):
		lcm *= x**y

print lcm
