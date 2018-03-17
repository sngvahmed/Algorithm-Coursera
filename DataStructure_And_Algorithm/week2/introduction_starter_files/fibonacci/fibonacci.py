# Uses python3
import sys
from random import randint


def fib(n):
    """calculate fibonanchi"""

    if mem[n] != 0:
        return mem[n]

    if (n <= 1):
        return n

    mem[n] = (fib(n - 1) + fib(n - 2))
    return mem[n]


if __name__ == '__main__':
    mem = []
    input = sys.stdin.read()
    n = int(input)
    mem = [int(0) for x in range(n + 1)]
    print(fib(n))
