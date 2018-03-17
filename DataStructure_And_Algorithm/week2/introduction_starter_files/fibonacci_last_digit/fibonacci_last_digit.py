# Uses python3
import sys
from random import randint


def calc_fib_normal(n):
    """calculate fibonanchi"""
    if n == 1 or n == 2:
        return 1
    if mem1[n] != 0:
        return mem1[n]

    if (n <= 1):
        return n

    mem1[n] = (calc_fib_normal(n - 1) + calc_fib_normal(n - 2))
    return mem1[n]


def calc_fib_normal_with_rem(n):
    """calculate fibonanchi"""
    if n == 1 or n == 2:
        return 1
    if mem2[n] != 0:
        return mem2[n]

    if (n <= 1):
        return n

    mem2[n] = (calc_fib_normal_with_rem(n - 1) + calc_fib_normal_with_rem(n - 2)) % 10
    return mem2[n]


def cal_fib_mem(n):
    if n == 1 or n == 2:
        return 1
    mem = [int(0) for x in range(n + 1)]
    mem[1], mem[2] = 1, 1
    for i in range(3, n + 1):
        mem[i] = (mem[i - 1] + mem[i - 2]) % 10
    return mem[n]


def stress_test():
    for i in range(1000):
        rnNumber = randint(1, 1000)

        if rnNumber != 0:
            mem1 = [int(0) for x in range(rnNumber + 1)]
            mem2 = [int(0) for x in range(rnNumber + 1)]
            print(rnNumber)
            c1 = cal_fib_mem(rnNumber)
            c2 = calc_fib_normal(rnNumber) % 10
            c3 = calc_fib_normal_with_rem(rnNumber)
            if c1 == c2 and c1 == c3:
                print("YES")
            else:
                print("wrong answer in test ", rnNumber, "with error", c1, c2 , c3)
                break


if __name__ == '__main__':
    mem1 = []
    mem2 = []
    input = sys.stdin.read()
    n = int(input)

    print(cal_fib_mem(n))
