# Uses python3
import sys
from random import randint


def gcd(a, b):
	""" get gcd """

	a, b = max(a, b), min(a, b)
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	""" get lcm """
	if a == b:
		return a
	return (a * b) // (gcd(a , b))


def lcm_naive(a, b):
	""" get native lcm """

	for l in range(1, a*b + 1):
		if (l % a == 0) and (l % b == 0):
			return l

	return a*b


def stressTesting():
	for _ in range(10000):
		r1, r2 = randint(1, 1000), randint(1, 10000)
		c1, c2 = lcm_naive(r1, r2), lcm(r1, r2)
		if c1 == c2:
			print("YES")
		else:
			print("WA , with error (", r1, r2, " result = ", c1, c2)
			break

if __name__ == '__main__':
	# stressTesting()
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(lcm(a, b))
