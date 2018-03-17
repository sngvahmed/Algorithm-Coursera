# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


mem = {
    0: [],
    1: [1],
    2: [1, 2]
}


def maxArray(arr1, arr2):
    if len(arr2) == 0:
        return arr1
    if len(arr1) < len(arr2):
        return arr1
    return arr2


def optimized_sequence(n):
    if n in mem:
        return mem.get(n)[:]

    res = []
    if n % 3 == 0:
        res = optimized_sequence(n // 3)
    elif n % 3 == 1:
        res = optimized_sequence(n // 3) + [n - 1]
    elif n % 3 == 2:
        res = optimized_sequence(n // 3) + [n - 2, n - 1]

    if n % 2 == 0:
        res = maxArray(optimized_sequence(n // 2), res)
    elif n % 2 == 1:
        res = maxArray(optimized_sequence(n // 2) + [n - 1], res)

    res.append(n)
    mem[n] = res[:]
    return res[:]


def pinp(arr):
    print(len(arr) - 1)
    for x in arr:
        print(x, end=' ')


input = sys.stdin.read()
n = int(input)
seq1 = list(optimized_sequence(n))
pinp(seq1)