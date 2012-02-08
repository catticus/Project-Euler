from math import factorial
from itertools import chain, combinations

def is_prime (n):
	if (n < 0):
		n *= -1
	if (n < 2):
		return False
	if (n == 2):
		return True
	if (n % 2 == 0):
		return False
	lim = int(n**.5) + 1
	for i in xrange(3, lim, 2):
		if (n % i == 0):
			return False
	return True

def find_prime_factors (n):
	factors = []
	lim = int(n**.5) + 1
	for i in xrange(2, lim):
		while (n % i == 0):
			factors += [i]
			n /= i
	if (n != 1):
		factors += [n]
	return factors

def count_divs (n):
	factors = find_prime_factors(n)
	unique_factors = set(factors)
	f = lambda x: factors.count(x) + 1
	x = map(f, unique_factors)
	y = reduce(int.__mul__, x, 1)
	return y

def find_divs (n):
	factors = find_prime_factors(n)
	factor_sets = (combinations(factors, L) for L in xrange(1, len(factors) + 1))
	factor_powerset = chain.from_iterable(factor_sets)

	divisor_sets = set(factor_powerset)
	divisors = [reduce(int.__mul__, s, 1) for s in divisor_sets]

	divisors.append(1)
	divisors.sort()
	divisors.pop(-1)

	return divisors

def digital_sum (n):
	total = 0
	while n > 0:
		total += n % 10
		n /= 10
	return total

def digital_prod (n):
	product = 1
	while n > 0:
		product *= n % 10
		n /= 10
	return product

def digital_split (n):
	digits = []
	while n > 0:
		digits.insert(0, n % 10)
		n /= 10
	return digits

def digital_reverse (n):
	reverse = 0
	while n > 0:
		reverse *= 10
		reverse += n % 10
		n /= 10
	return reverse

def digital_length (n):
	return len(digital_split(n))

def is_digital_palindrome (n):
	return (n == digital_reverse(n))

def nCr (n, r):
	a = factorial(n)
	b = factorial(r)
	c = factorial(n-r)
	return float(a) / (b * c)

def totient (n):
	factors = set(find_prime_factors(n))
	tot = n
	for p in factors:
		tot *= (1. - 1./p)
	return tot

