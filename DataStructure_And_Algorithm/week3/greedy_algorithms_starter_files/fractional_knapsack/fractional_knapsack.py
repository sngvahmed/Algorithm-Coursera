# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    indx = 0
    arr = []
    for weight in weights:
        val = values[indx]
        arr.append((val / weight, val, weight))
        indx = indx + 1
    arr = sorted(arr, reverse=True)
    for i in arr:
        if capacity > 0:
            if capacity >= i[2]:
                capacity = capacity - i[2]
                value = value + i[1]
            else:

                value = value + (i[0] * capacity)
                break
        else:
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
