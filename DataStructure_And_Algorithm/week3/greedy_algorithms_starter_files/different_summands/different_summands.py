# Uses python3
import sys


def optimal_summands(n):
    summands = []
    init = 1
    while n > 0:
        if init <= n:
            summands.append(init)
            n = n - init
            init = init + 1
        else:
            summands[len(summands) - 1] = summands[len(summands) - 1] + n
            n = 0

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
